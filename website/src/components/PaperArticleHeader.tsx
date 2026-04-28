import React from "react";
import { useDoc } from "@docusaurus/plugin-content-docs/client";

/**
 * PaperArticleHeader — 论文文章头部元信息组件。
 *
 * 专用于 source_type="paper" 的 arXiv 论文页面。
 * 显示：arXiv ID、作者、分类标签、可信度、原文链接。
 */
export default function PaperArticleHeader(): JSX.Element | null {
  const { frontMatter } = useDoc();
  const fm = frontMatter as any;

  if (!fm.source_type || fm.source_type !== "paper") {
    return null;
  }

  const arxivId = fm.arxiv_id || "";
  const sourceUrl = fm.source_url || (arxivId ? `https://arxiv.org/abs/${arxivId}` : "");
  const authors = fm.authors || [];
  const categories = fm.categories || [];
  const published = fm.published_date || fm.published || "";
  const credibility = fm.credibility || 4;

  const arxivUrl = arxivId ? `https://arxiv.org/abs/${arxivId}` : "";

  return (
    <div
      style={{
        marginBottom: "1.5rem",
        padding: "1rem 1.2rem",
        border: "1px solid var(--ifm-color-emphasis-300)",
        borderRadius: "8px",
        backgroundColor: "var(--ifm-color-emphasis-100)",
        fontSize: "0.9rem",
        lineHeight: 1.7,
      }}
    >
      {/* 第一行：arXiv ID + 可信度 */}
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "12px",
          marginBottom: authors.length > 0 ? "6px" : 0,
          flexWrap: "wrap",
        }}
      >
        {arxivId && (
          <a
            href={arxivUrl}
            target="_blank"
            rel="noopener noreferrer"
            style={{
              display: "inline-flex",
              alignItems: "center",
              gap: "4px",
              padding: "2px 10px",
              backgroundColor: "#b31b1b",
              color: "#fff",
              borderRadius: "4px",
              fontSize: "0.8rem",
              fontWeight: 700,
              textDecoration: "none",
            }}
          >
            arXiv:{arxivId}
          </a>
        )}

        <span
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: "4px",
            padding: "2px 8px",
            backgroundColor: "var(--ifm-color-emphasis-200)",
            borderRadius: "4px",
            fontSize: "0.8rem",
          }}
        >
          📜 论文 · 同行评审
          {" "}
          <span style={{ color: "var(--ifm-color-warning)" }}>
            {"⭐".repeat(Math.min(credibility, 5))}
          </span>
        </span>

        {published && (
          <span style={{ color: "var(--ifm-color-secondary)", fontSize: "0.8rem" }}>
            📅 {published}
          </span>
        )}
      </div>

      {/* 第二行：作者 */}
      {authors.length > 0 && (
        <div
          style={{
            color: "var(--ifm-color-secondary)",
            fontSize: "0.85rem",
            marginBottom: categories.length > 0 ? "4px" : 0,
          }}
        >
          👥 {authors.slice(0, 6).join(", ")}
          {authors.length > 6 && ` et al. (${authors.length} authors)`}
        </div>
      )}

      {/* 第三行：分类标签 */}
      {categories.length > 0 && (
        <div style={{ display: "flex", gap: "4px", flexWrap: "wrap" }}>
          {categories.slice(0, 8).map((cat: string) => (
            <span
              key={cat}
              style={{
                display: "inline-block",
                padding: "1px 6px",
                backgroundColor: "var(--ifm-color-primary-lightest)",
                color: "var(--ifm-color-primary-darkest)",
                borderRadius: "3px",
                fontSize: "0.7rem",
                fontWeight: 500,
              }}
            >
              {cat}
            </span>
          ))}
        </div>
      )}

      {/* 底部：原文链接 */}
      {sourceUrl && (
        <div style={{ marginTop: "6px", fontSize: "0.75rem", color: "var(--ifm-color-secondary)" }}>
          📄 原文：{" "}
          <a href={sourceUrl} target="_blank" rel="noopener noreferrer">
            {sourceUrl}
          </a>
        </div>
      )}
    </div>
  );
}
