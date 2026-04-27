import React from 'react';

interface TagBadgeProps {
  label: string;
  color?: 'primary' | 'secondary' | 'info' | 'warning' | 'success';
  icon?: string | null;
}

const colorMap: Record<string, { bg: string; fg: string; border: string }> = {
  primary: { bg: '#dbeafe', fg: '#1e40af', border: '#93c5fd' },
  secondary: { bg: '#f3f4f6', fg: '#374151', border: '#d1d5db' },
  info: { bg: '#e0f2fe', fg: '#075985', border: '#7dd3fc' },
  warning: { bg: '#fef3c7', fg: '#92400e', border: '#fcd34d' },
  success: { bg: '#dcfce7', fg: '#166534', border: '#86efac' },
};

export default function TagBadge({ label, color = 'secondary', icon }: TagBadgeProps) {
  const c = colorMap[color] || colorMap.secondary;

  return (
    <span
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '2px',
        padding: '1px 7px',
        margin: '1px 3px 1px 0',
        borderRadius: '4px',
        fontSize: '0.7rem',
        fontWeight: 500,
        color: c.fg,
        backgroundColor: c.bg,
        border: `1px solid ${c.border}`,
        whiteSpace: 'nowrap',
        lineHeight: '1.5',
      }}
    >
      {icon && <span style={{ marginRight: '1px' }}>{icon}</span>}
      {label}
    </span>
  );
}
