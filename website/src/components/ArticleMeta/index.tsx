import React from 'react';
import CredibilityStars from './CredibilityStars';
import LifecycleBadge from './LifecycleBadge';
import TagBadge from './TagBadge';
import styles from './styles.module.css';

export interface ArticleMetaProps {
  // Required fields from v2 frontmatter
  source_url: string;
  source_type: 'official' | 'github-issue' | 'github-pr' | 'blog' | 'paper' | 'community' | 'bilingual' | 'multilingual' | 'tool';
  source_org: string;
  published_date?: string;
  synced_date?: string;
  credibility: number;
  lifecycle: 'latest' | 'outdated' | 'deprecating' | 'deprecated';
  version?: string;
  rocm_versions?: string[];
  tags?: string[];
  os?: string[];
  gpu?: string[];
  gpu_arch?: string[];
  driver?: string[];
  frameworks?: string[];
  difficulty?: string;
}

const sourceTypeLabels: Record<string, string> = {
  official: '📄 官方文档',
  'github-issue': '🐛 GitHub Issue',
  'github-pr': '🔧 GitHub PR',
  blog: '📝 官方博客',
  paper: '📜 学术论文',
  community: '💬 社区讨论',
  bilingual: '🌐 双语对照',
  multilingual: '🌍 多语内容',
  tool: '🛠️ 工具页面',
};

const sourceOrgLabels: Record<string, string> = {
  amd: 'AMD',
  rocm: 'ROCm',
  pytorch: 'PyTorch',
  tensorflow: 'TensorFlow',
  paddle: 'PaddlePaddle',
  llvm: 'LLVM',
  mesa: 'Mesa',
  linux: 'Linux Kernel',
};

const osLabels: Record<string, string> = {
  linux: 'Linux',
  windows: 'Windows',
  'ubuntu-20.04': 'Ubuntu 20.04',
  'ubuntu-22.04': 'Ubuntu 22.04',
  'ubuntu-24.04': 'Ubuntu 24.04',
  rhel: 'RHEL',
  arch: 'Arch',
  wsl2: 'WSL2',
  docker: 'Docker',
  kubernetes: 'K8s',
};

const gpuLabels: Record<string, string> = {
  mi50: 'MI50',
  mi100: 'MI100',
  mi210: 'MI210',
  mi250: 'MI250',
  mi250x: 'MI250X',
  mi300x: 'MI300X',
  rx6800: 'RX 6800',
  rx6900: 'RX 6900',
  rx7900: 'RX 7900',
  rx7900xtx: 'RX 7900 XTX',
  apu: 'APU',
};

const archLabels: Record<string, string> = {
  cdna1: 'CDNA1',
  cdna2: 'CDNA2',
  cdna3: 'CDNA3',
  rdna2: 'RDNA2',
  rdna3: 'RDNA3',
};

const driverLabels: Record<string, string> = {
  'amdgpu-5.x': 'amdgpu 5.x',
  'amdgpu-6.x': 'amdgpu 6.x',
  'amdgpu-7.x': 'amdgpu 7.x',
};

const frameworkLabels: Record<string, string> = {
  pytorch: 'PyTorch',
  tensorflow: 'TensorFlow',
  jax: 'JAX',
  paddle: 'PaddlePaddle',
  onnx: 'ONNX',
};

const difficultyLabels: Record<string, string> = {
  beginner: '🟢 入门',
  intermediate: '🟡 进阶',
  advanced: '🔴 高级',
  reference: '📖 参考',
};

export default function ArticleMeta(props: ArticleMetaProps) {
  const {
    source_url,
    source_type,
    source_org,
    published_date,
    synced_date,
    credibility,
    lifecycle,
    version,
    rocm_versions,
    tags,
    os,
    gpu,
    gpu_arch,
    driver,
    frameworks,
    difficulty,
  } = props;

  return (
    <div className={styles.container}>
      {/* 第一行：来源 + 可信度 + 生命周期 */}
      <div className={styles.row}>
        <div className={styles.leftGroup}>
          <TagBadge
            label={sourceTypeLabels[source_type] || source_type}
            icon={null}
            color="primary"
          />
          <TagBadge
            label={sourceOrgLabels[source_org] || source_org}
            color="secondary"
          />
          <CredibilityStars level={credibility} size="sm" />
          <LifecycleBadge status={lifecycle} size="sm" />
        </div>
        <a
          href={source_url}
          target="_blank"
          rel="noopener noreferrer"
          className={styles.sourceLink}
        >
          📎 查看原文
        </a>
      </div>

      {/* 第二行：环境标签（OS / GPU / 架构 / 驱动 / 框架） */}
      <div className={styles.tagsRow}>
        {version && (
          <TagBadge label={`ROCm ${version}`} color="info" icon="📌" />
        )}
        {rocm_versions && rocm_versions.length > 1 && (
          <TagBadge
            label={`兼容 ${rocm_versions.join(', ')}`}
            color="info"
          />
        )}
        {difficulty && (
          <TagBadge
            label={difficultyLabels[difficulty] || difficulty}
            color="secondary"
          />
        )}
        {os && os.map((o) => (
          <TagBadge key={o} label={osLabels[o] || o} color="info" icon="💻" />
        ))}
        {gpu && gpu.map((g) => (
          <TagBadge key={g} label={gpuLabels[g] || g} color="warning" icon="🎮" />
        ))}
        {gpu_arch && gpu_arch.map((a) => (
          <TagBadge key={a} label={archLabels[a] || a} color="warning" />
        ))}
        {driver && driver.map((d) => (
          <TagBadge key={d} label={driverLabels[d] || d} color="secondary" icon="⚙️" />
        ))}
        {frameworks && frameworks.map((f) => (
          <TagBadge key={f} label={frameworkLabels[f] || f} color="success" icon="🧠" />
        ))}
        {tags && tags.map((t) => (
          <TagBadge key={t} label={t} color="secondary" />
        ))}
      </div>

      {/* 第三行：日期信息 */}
      {(published_date || synced_date) && (
        <div className={styles.dateRow}>
          {published_date && <span>📅 发布：{String(published_date)}</span>}
          {synced_date && <span>🔄 同步：{String(synced_date)}</span>}
        </div>
      )}
    </div>
  );
}
