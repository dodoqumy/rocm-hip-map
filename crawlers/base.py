"""
基础爬虫抽象类 (Phase 2.1)
定义所有 crawler 的通用接口
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional, Set, List, Dict, Any
from pathlib import Path
import yaml
import time
from urllib.parse import urlparse
import logging

from .http_client import HTTPClient
from .extractor import ContentExtractor
from .dedup import Deduplicator
from .url_family import normalize_url_family

logger = logging.getLogger(__name__)


@dataclass
class CrawlerConfig:
    """单个源的配置"""
    slug: str
    name: str
    base_url: str
    sitemap: Optional[str] = None
    crawler: str = "sphinx_nav"
    credibility: int = 5
    rate_limit: float = 1.0
    interval_hours: int = 24
    is_archive: bool = False
    extract_api: bool = False
    skip_patterns: List[str] = field(default_factory=list)


@dataclass
class FetchResult:
    """抓取结果"""
    url: str
    content: str
    title: str
    version: str = "latest"
    is_canonical: bool = True
    url_family: str = ""
    content_hash: str = ""
    is_api_ref: bool = False
    error: Optional[str] = None


class BaseCrawler(ABC):
    """所有爬虫的基类"""
    
    def __init__(self, config: CrawlerConfig, http_client: HTTPClient):
        self.config = config
        self.http = http_client
        self.extractor = ContentExtractor()
        self.dedup = Deduplicator()
        self._visited: Set[str] = set()
        
    @property
    def domain(self) -> str:
        return urlparse(self.config.base_url).netloc
    
    @abstractmethod
    def discover(self, max_urls: int = 500) -> List[str]:
        """发现所有待抓取的 URL"""
        pass
    
    @abstractmethod
    def fetch(self, url: str) -> Optional[FetchResult]:
        """抓取单个页面"""
        pass
    
    def should_skip(self, url: str) -> bool:
        """检查是否应跳过此 URL"""
        for pattern in self.config.skip_patterns:
            if pattern in url:
                return True
        # 全局跳过模式
        global_skips = ["/_images/", "/_static/", "/_sources/", "/genindex", "/search.html"]
        for pattern in global_skips:
            if pattern in url:
                return True
        return False
    
    def run(self, dry_run: bool = False, max_urls: int = 0) -> Dict[str, Any]:
        """运行爬虫"""
        logger.info(f"🔄 Starting crawler: {self.config.name}")
        
        # 发现 URLs
        urls = self.discover(max_urls)
        logger.info(f"  📍 Discovered {len(urls)} URLs")
        
        if dry_run:
            for url in urls[:20]:
                print(f"    {url}")
            return {"discovered": len(urls), "dry_run": True}
        
        # 抓取
        results = []
        for i, url in enumerate(urls):
            if self.should_skip(url):
                continue
            
            # 速率限制 (按域名)
            self.http.rate_limit_per_domain(self.domain)
            
            result = self.fetch(url)
            if result:
                results.append(result)
                
            if (i + 1) % 50 == 0:
                logger.info(f"  📥 Progress: {i+1}/{len(urls)}")
        
        logger.info(f"  ✅ Done: {len(results)} pages")
        
        return {
            "slug": self.config.slug,
            "discovered": len(urls),
            "fetched": len(results),
        }


def load_sources(config_path: str = "config/amd-sources.yaml") -> List[CrawlerConfig]:
    """从 YAML 加载源配置"""
    with open(config_path) as f:
        data = yaml.safe_load(f)
    
    sources = []
    for item in data.get("sources", []):
        sources.append(CrawlerConfig(
            slug=item["slug"],
            name=item["name"],
            base_url=item["base_url"],
            sitemap=item.get("sitemap"),
            crawler=item.get("crawler", "sphinx_nav"),
            credibility=item.get("credibility", 5),
            rate_limit=item.get("rate_limit", 1.0),
            interval_hours=item.get("interval_hours", 24),
            is_archive=item.get("is_archive", False),
            extract_api=item.get("extract_api", False),
            skip_patterns=item.get("skip_patterns", []),
        ))
    
    return sources


def get_crawler(config: CrawlerConfig) -> BaseCrawler:
    """根据配置创建对应的爬虫"""
    from .sitemap import SitemapCrawler
    from .sphinx_nav import SphinxNavCrawler
    from .github_docs import GithubDocsCrawler
    from .rss import RSSCrawler
    
    crawlers = {
        "sitemap": SitemapCrawler,
        "sphinx_nav": SphinxNavCrawler,
        "github_docs": GithubDocsCrawler,
        "rss": RSSCrawler,
    }
    
    crawler_class = crawlers.get(config.crawler, SphinxNavCrawler)
    http = HTTPClient(config.rate_limit)
    return crawler_class(config, http)