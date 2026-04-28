/**
 * RelatedArticles — 文章底部推荐文章组件
 *
 * 根据关键词重叠度 + 标签相似度，展示 3-5 篇最相关的其他文章。
 *
 * 工作原理：
 *   1. 构建时由 scripts/related-articles.py 预计算所有文章的相关度
 *   2. 输出 data/related-articles.json 到 static/data/
 *   3. 本组件在客户端加载该 JSON，按当前文章 slug 查找推荐列表
 *
 * 未来扩展（阅读者评价）：
 *   - helpfulScore: 读者"有帮助"投票数
 *   - viewCount: 页面浏览量
 *   - 推荐排序公式: keywords_overlap * 0.6 + helpful_weight * 0.25 + view_weight * 0.15
 */

import React, { useEffect, useState } from "react";

// ── 类型定义 ──
interface RelatedArticle {
  slug: string;
  title: string;
  keywords_overlap_score: number;
}

interface RelatedData {
  version: number;
  updated: string;
  top_n: number;
  total_articles: number;
  related: Record<string, RelatedArticle[]>;
}

// ── Props ──
interface RelatedArticlesProps {
  /** 当前文章在 docs/ 下的相对路径（不含 .mdx），如 "rocm-core/概念/gpu-arch_mi250" */
  currentSlug: string;
  /** 最多显示几篇（默认 5） */
  maxArticles?: number;
}

// ── 加载缓存 ──
let cachedData: RelatedData | null = null;
let fetchPromise: Promise<RelatedData | null> | null = null;

async function loadRelatedData(): Promise<RelatedData | null> {
  if (cachedData) return cachedData;
  if (fetchPromise) return fetchPromise;

  fetchPromise = fetch("/data/related-articles.json")
    .then((res) => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json() as Promise<RelatedData>;
    })
    .then((data) => {
      cachedData = data;
      return data;
    })
    .catch((err) => {
      console.warn("[related-articles] 加载失败:", err.message);
      return null;
    });

  return fetchPromise;
}

// ── 分数转百分比 ──
function scoreToPercent(score: number): number {
  return Math.min(Math.round(score * 100), 100);
}

// ── 分数颜色 ──
function scoreColor(percent: number): string {
  if (percent >= 80) return "var(--ifm-color-success)";
  if (percent >= 60) return "var(--ifm-color-warning)";
  return "var(--ifm-color-secondary)";
}

// ── 图标：相关性条 ──
function ScoreBar({ percent }: { percent: number }) {
  const color = scoreColor(percent);
  return (
    <div
      style={{
        display: "inline-flex",
        alignItems: "center",
        gap: "4px",
        marginLeft: "8px",
        fontSize: "0.8em",
        opacity: 0.8,
      }}
    >
      <span
        style={{
          display: "inline-block",
          width: `${Math.max(percent / 10, 5)}px`,
          height: "8px",
          borderRadius: "2px",
          backgroundColor: color,
        }}
      />
      <span style={{ color, fontWeight: 600, minWidth: "2.5em" }}>
        {percent}%
      </span>
    </div>
  );
}

// ── 占位骨架屏 ──
function Skeleton() {
  return (
    <div style={{ marginTop: "3rem", opacity: 0.5 }}>
      <h3>📎 相关文章</h3>
      {[1, 2, 3].map((i) => (
        <div
          key={i}
          style={{
            height: "1.2em",
            width: `${60 + i * 10}%`,
            backgroundColor: "var(--ifm-color-emphasis-200)",
            borderRadius: "4px",
            marginBottom: "8px",
          }}
        />
      ))}
    </div>
  );
}

// ── 主组件 ──
export default function RelatedArticles({
  currentSlug,
  maxArticles = 5,
}: RelatedArticlesProps) {
  const [data, setData] = useState<RelatedData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadRelatedData().then((d) => {
      setData(d);
      setLoading(false);
    });
  }, []);

  if (loading) return <Skeleton />;
  if (!data || !data.related) return null;

  const recommendations = data.related[currentSlug];
  if (!recommendations || recommendations.length === 0) return null;

  const displayed = recommendations.slice(0, maxArticles);

  return (
    <div
      style={{
        marginTop: "3rem",
        padding: "1.5rem",
        border: "1px solid var(--ifm-color-emphasis-300)",
        borderRadius: "8px",
        backgroundColor: "var(--ifm-color-emphasis-100)",
      }}
    >
      <h3
        style={{
          marginTop: 0,
          fontSize: "1rem",
          color: "var(--ifm-color-primary)",
        }}
      >
        📎 相关文章推荐
        <span
          style={{
            fontSize: "0.75rem",
            fontWeight: 400,
            marginLeft: "8px",
            color: "var(--ifm-color-secondary)",
          }}
        >
          （基于关键词相似度）
        </span>
      </h3>

      <ul style={{ margin: 0, paddingLeft: "1.2rem", listStyle: "none" }}>
        {displayed.map((article) => {
          const percent = scoreToPercent(article.keywords_overlap_score);
          const articleUrl = `/docs/${article.slug}`;

          return (
            <li
              key={article.slug}
              style={{
                marginBottom: "6px",
                lineHeight: 1.6,
              }}
            >
              <a
                href={articleUrl}
                style={{
                  fontWeight: 500,
                  textDecoration: "none",
                  color: "var(--ifm-link-color)",
                }}
              >
                {article.title || article.slug.split("/").pop()?.replace(/_/g, " ")}
              </a>
              <ScoreBar percent={percent} />
            </li>
          );
        })}
      </ul>

      {/* 底部提示：未来读者评价 */}
      <div
        style={{
          marginTop: "12px",
          paddingTop: "8px",
          borderTop: "1px dashed var(--ifm-color-emphasis-300)",
          fontSize: "0.7rem",
          color: "var(--ifm-color-secondary)",
          textAlign: "right",
        }}
      >
        💡 推荐排序基于关键词匹配度 · 读者评价功能即将上线
      </div>
    </div>
  );
}
