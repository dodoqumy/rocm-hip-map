import React from 'react';

type LifecycleStatus = 'latest' | 'outdated' | 'deprecating' | 'deprecated';

interface LifecycleBadgeProps {
  status: LifecycleStatus;
  size?: 'sm' | 'md';
}

const config: Record<LifecycleStatus, { label: string; color: string; bg: string; icon: string }> = {
  latest: {
    label: '最新推荐',
    color: '#166534',
    bg: '#dcfce7',
    icon: '✅',
  },
  outdated: {
    label: '已过时',
    color: '#854d0e',
    bg: '#fef9c3',
    icon: '⚠️',
  },
  deprecating: {
    label: '即将废弃',
    color: '#9a3412',
    bg: '#fed7aa',
    icon: '🔶',
  },
  deprecated: {
    label: '已弃用',
    color: '#991b1b',
    bg: '#fecaca',
    icon: '🚫',
  },
};

export default function LifecycleBadge({ status, size = 'sm' }: LifecycleBadgeProps) {
  const { label, color, bg, icon } = config[status] || config.latest;
  const fontSize = size === 'sm' ? '0.7rem' : '0.8rem';

  return (
    <span
      title={`内容状态：${label}`}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '3px',
        padding: '1px 8px',
        borderRadius: '10px',
        fontSize,
        fontWeight: 600,
        color,
        backgroundColor: bg,
        border: `1px solid ${color}30`,
        whiteSpace: 'nowrap',
      }}
    >
      {icon} {label}
    </span>
  );
}
