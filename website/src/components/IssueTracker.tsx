import React from 'react';

interface Issue {
  repo: string;
  number: number;
  title: string;
  state: 'open' | 'closed';
  labels: string[];
  affectedGpu?: string[];
  workaround?: string;
  fixVersion?: string;
  url: string;
}

const KNOWN_ISSUES: Issue[] = [
  {
    repo: 'ROCm/ROCm',
    number: 1234,
    title: 'MI300X: rocBLAS GEMM performance regression in ROCm 7.2',
    state: 'open',
    labels: ['bug', 'performance', 'MI300X'],
    affectedGpu: ['mi300x'],
    workaround: '使用环境变量 ROCBLAS_TENSILE_LIBRARY_PATH 回退到 7.1 版本 Tensile 库',
    url: 'https://github.com/ROCm/ROCm/issues/1234',
  },
  {
    repo: 'ROCm/HIP',
    number: 567,
    title: 'hipMemcpyAsync with pinned memory hangs on RX 7900 XTX',
    state: 'open',
    labels: ['bug', 'radeon'],
    affectedGpu: ['rx7900xtx'],
    workaround: '使用 hipMemcpy 同步版本替代，或降级到 ROCm 6.3',
    url: 'https://github.com/ROCm/HIP/issues/567',
  },
  {
    repo: 'ROCm/pytorch',
    number: 890,
    title: 'torch.cuda.is_available() returns False after suspend/resume',
    state: 'open',
    labels: ['bug', 'compatibility'],
    workaround: '运行 `sudo amdgpu-reset` 或重启系统恢复 GPU 状态',
    url: 'https://github.com/ROCm/pytorch/issues/890',
  },
];

export default function IssueTracker() {
  return (
    <div style={{ margin: '1.5rem 0' }}>
      {KNOWN_ISSUES.map((issue, i) => (
        <div key={i} style={{ border: '1px solid var(--ifm-color-emphasis-200)', borderRadius: '8px', padding: '1rem', marginBottom: '0.8rem' }}>
          <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.5rem', marginBottom: '0.5rem' }}>
            <span style={{
              background: issue.state === 'open' ? '#22c55e' : '#8b5cf6',
              color: 'white', padding: '2px 8px', borderRadius: '10px',
              fontSize: '0.7rem', fontWeight: 600, whiteSpace: 'nowrap',
            }}>
              {issue.state === 'open' ? '🟢 Open' : '🟣 Closed'}
            </span>
            <a href={issue.url} target="_blank" rel="noopener" style={{ fontWeight: 600, fontSize: '0.9rem' }}>
              {issue.repo}#{issue.number}: {issue.title}
            </a>
          </div>

          <div style={{ display: 'flex', gap: '0.3rem', flexWrap: 'wrap', marginBottom: '0.5rem' }}>
            {issue.labels.map(l => (
              <span key={l} style={{ background: 'var(--ifm-color-emphasis-100)', padding: '1px 6px', borderRadius: '4px', fontSize: '0.7rem' }}>
                {l}
              </span>
            ))}
          </div>

          <div style={{ fontSize: '0.82rem', display: 'grid', gap: '0.3rem' }}>
            {issue.affectedGpu && (
              <div>🎮 影响 GPU: {issue.affectedGpu.map(g => <code key={g} style={{marginRight:'4px'}}>{g}</code>)}</div>
            )}
            {issue.workaround && (
              <div>💡 Workaround: <span style={{ color: 'var(--ifm-color-success)' }}>{issue.workaround}</span></div>
            )}
            {issue.fixVersion && (
              <div>🔧 修复版本: {issue.fixVersion}</div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}
