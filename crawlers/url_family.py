"""
URL 跨版本归一化 (Phase 2.1)
用于跨版本去重和链接
"""

import re
from urllib.parse import urlparse


def normalize_url_family(url: str) -> str:
    """提取跨版本归一化的 URL 家族。
    
    https://rocm.docs.amd.com/en/latest/install/quick.html
    https://rocm.docs.amd.com/en/docs-7.0.0/install/quick.html
    → rocm/install/quick
    """
    parsed = urlparse(url)
    path = parsed.path
    
    # 移除版本前缀
    # /en/latest/ → /
    path = re.sub(r"/en/latest", "", path)
    # /en/docs-X.Y.Z/ → /
    path = re.sub(r"/en/docs-\d+\.\d+\.\d+", "", path)
    # /projects/PROJECT/en/latest/ → /projects/PROJECT/
    path = re.sub(r"/projects/[\w-]+/en/latest", "", path)
    
    path = path.strip("/")
    path = re.sub(r"\.html?$", "", path)
    
    if not path:
        path = "index"
    
    # 提取域名 + 路径
    domain = parsed.netloc
    # 移除端口和 www
    domain = domain.replace("www.", "")
    domain = domain.replace(":443", "")
    
    return f"{domain}/{path}"


def is_latest_version(url: str) -> bool:
    """判断是否为 latest 版本"""
    return "/en/latest/" in url or "/projects/" in url and "/en/" not in url.replace("/projects/", "")


def extract_version(url: str) -> str:
    """提取版本号"""
    # /en/docs-7.0.0/
    match = re.search(r"/en/docs-(\d+\.\d+\.\d+)/", url)
    if match:
        return match.group(1)
    
    if "/en/latest/" in url:
        return "latest"
    
    return "unknown"


def get_canonical_url(url: str, base_version: str = "latest") -> str:
    """获取 canonical URL"""
    # 简单替换版本号
    return re.sub(r"/en/docs-\d+\.\d+\.\d+/", f"/en/{base_version}/", url)