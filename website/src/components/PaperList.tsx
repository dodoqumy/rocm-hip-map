import React, { useEffect, useState } from "react";

interface Paper {
  arxiv_id: string;
  title: string;
  authors: string[];
  abstract: string;
  categories: string[];
  published: string;
  source_url: string;
}

export default function PaperList() {
  const [papers, setPapers] = useState<Paper[]>([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [visible, setVisible] = useState(20);

  useEffect(() => {
    fetch("/data/papers.json")
      .then((r) => r.json())
      .then((data) => {
        setPapers(data.papers || data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  const filtered = papers.filter((p) => {
    if (!search.trim()) return true;
    const q = search.toLowerCase();
    return (
      p.title.toLowerCase().includes(q) ||
      (p.abstract || "").toLowerCase().includes(q) ||
      (p.authors || []).some((a) => a.toLowerCase().includes(q)) ||
      (p.arxiv_id || "").toLowerCase().includes(q)
    );
  });

  if (loading) return <div style={{ opacity: 0.5 }}>加载论文数据...</div>;

  return (
    <div>
      <input
        type="text"
        placeholder="搜索论文标题、作者、关键词..."
        value={search}
        onChange={(e) => {
          setSearch(e.target.value);
          setVisible(20);
        }}
        style={{
          width: "100%",
          padding: "8px 12px",
          marginBottom: "1rem",
          border: "1px solid var(--ifm-color-emphasis-300)",
          borderRadius: "6px",
          fontSize: "0.9rem",
          backgroundColor: "var(--ifm-background-color)",
          color: "var(--ifm-font-color-base)",
        }}
      />

      <div style={{ fontSize: "0.8rem", color: "var(--ifm-color-secondary)", marginBottom: "8px" }}>
        {filtered.length} / {papers.length} 篇论文
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
        {filtered.slice(0, visible).map((paper) => (
          <a
            key={paper.arxiv_id}
            href={`/rocm-hip-map/docs/papers/${paper.arxiv_id}`}
            style={{
              display: "block",
              padding: "10px 12px",
              border: "1px solid var(--ifm-color-emphasis-300)",
              borderRadius: "6px",
              textDecoration: "none",
              color: "inherit",
              transition: "border-color 0.2s",
            }}
            onMouseOver={(e) => {
              (e.currentTarget as HTMLElement).style.borderColor = "var(--ifm-color-primary)";
            }}
            onMouseOut={(e) => {
              (e.currentTarget as HTMLElement).style.borderColor = "var(--ifm-color-emphasis-300)";
            }}
          >
            <div style={{ fontWeight: 600, fontSize: "0.9rem", marginBottom: "4px" }}>
              {paper.title}
            </div>
            <div style={{ display: "flex", gap: "12px", fontSize: "0.75rem", color: "var(--ifm-color-secondary)", flexWrap: "wrap" }}>
              <span>📅 {paper.published?.slice(0, 10) || "—"}</span>
              <span>👥 {(paper.authors || []).slice(0, 3).join(", ")}{(paper.authors || []).length > 3 ? " et al." : ""}</span>
              <span style={{ color: "#b31b1b", fontWeight: 700 }}>arXiv:{paper.arxiv_id}</span>
              {(paper.categories || []).slice(0, 3).map((c) => (
                <span key={c} style={{
                  padding: "1px 5px",
                  backgroundColor: "var(--ifm-color-primary-lightest)",
                  borderRadius: "3px",
                  fontSize: "0.65rem",
                }}>{c}</span>
              ))}
            </div>
          </a>
        ))}
      </div>

      {visible < filtered.length && (
        <button
          onClick={() => setVisible((v) => v + 20)}
          style={{
            display: "block",
            width: "100%",
            marginTop: "12px",
            padding: "8px",
            border: "1px solid var(--ifm-color-emphasis-300)",
            borderRadius: "6px",
            backgroundColor: "var(--ifm-color-emphasis-100)",
            cursor: "pointer",
            fontSize: "0.85rem",
          }}
        >
          加载更多 ({filtered.length - visible} 篇)
        </button>
      )}
    </div>
  );
}
