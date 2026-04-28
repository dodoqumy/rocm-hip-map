import React from 'react';

interface IssueNoticeProps {
  completeness?: {
    status: string;
    score: number;
    notes: string;
    dimensions?: Record<string, boolean>;
  };
}

/**
 * Issue 类文章信息完整性提示条。
 * 缺什么信息就在顶部醒目提醒读者注意。
 */
export default function IssueNotice({ completeness }: IssueNoticeProps) {
  if (!completeness || completeness.status === 'skip') return null;

  const dims = completeness.dimensions || {};
  const missingLabels: Record<string, string> = {
    description: '问题描述',
    environment: '运行环境（OS/ROCm/GPU/驱动版本）',
    error_log: '错误日志 / 异常信息',
    resolution_status: '问题是否已解决',
    solution: '解决方案 / Workaround',
  };

  const missing = Object.entries(dims)
    .filter(([, v]) => !v)
    .map(([k]) => missingLabels[k] || k);

  const statusConfig = {
    pass: { bg: '#dcfce7', border: '#22c55e', icon: '✅', text: '信息完整' },
    warn: { bg: '#fef3c7', border: '#f59e0b', icon: '⚠️', text: '信息不完整' },
    fail: { bg: '#fee2e2', border: '#ef4444', icon: '❌', text: '严重缺失' },
  };

  const config = statusConfig[completeness.status as keyof typeof statusConfig] || statusConfig.warn;

  return (
    <div style={{
      margin: '1.2rem 0',
      padding: '0.8rem 1rem',
      borderRadius: '8px',
      borderLeft: `4px solid ${config.border}`,
      background: config.bg,
      fontSize: '0.85rem',
    }}>
      <div style={{ fontWeight: 700, marginBottom: missing.length > 0 ? '0.4rem' : 0 }}>
        {config.icon} {config.text}
        {completeness.status !== 'pass' && (
          <span style={{ fontWeight: 400, color: 'var(--ifm-color-emphasis-600)', marginLeft: '0.3rem' }}>
            — {completeness.notes}
          </span>
        )}
      </div>
      {missing.length > 0 && (
        <div style={{ color: 'var(--ifm-color-emphasis-700)', lineHeight: 1.6 }}>
          <strong>缺少以下信息：</strong>
          <ul style={{ margin: '0.3rem 0 0', paddingLeft: '1.2rem' }}>
            {missing.map((m, i) => (
              <li key={i}>{m}</li>
            ))}
          </ul>
        </div>
      )}
      {completeness.status === 'pass' && (
        <div style={{ color: 'var(--ifm-color-emphasis-600)', fontSize: '0.8rem', marginTop: '0.2rem' }}>
          描述 · 环境 · 日志 · 解决状态 · 方案 各项完整
        </div>
      )}
    </div>
  );
}
