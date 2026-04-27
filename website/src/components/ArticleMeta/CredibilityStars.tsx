import React from 'react';

interface CredibilityStarsProps {
  level: number; // 1-5
  showLabel?: boolean;
  size?: 'sm' | 'md' | 'lg';
}

const labels: Record<number, string> = {
  5: '官方权威',
  4: '官方渠道',
  3: '社区权威',
  2: '实验性质',
  1: '仅供参考',
};

const colors: Record<number, string> = {
  5: '#22c55e',
  4: '#3b82f6',
  3: '#8b5cf6',
  2: '#eab308',
  1: '#9ca3af',
};

export default function CredibilityStars({
  level,
  showLabel = true,
  size = 'sm',
}: CredibilityStarsProps) {
  const clampedLevel = Math.max(1, Math.min(5, level));
  const fontSize = { sm: '0.75rem', md: '0.9rem', lg: '1.1rem' }[size];
  const color = colors[clampedLevel] || colors[3];

  return (
    <span
      title={`可信度：${labels[clampedLevel]}`}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '2px',
        fontSize,
        color,
        cursor: 'help',
      }}
    >
      {/* Filled stars */}
      {Array.from({ length: clampedLevel }, (_, i) => (
        <span key={`filled-${i}`}>★</span>
      ))}
      {/* Empty stars */}
      {Array.from({ length: 5 - clampedLevel }, (_, i) => (
        <span key={`empty-${i}`} style={{ opacity: 0.3 }}>★</span>
      ))}
      {showLabel && (
        <span style={{ marginLeft: '4px', fontSize: '0.8em', opacity: 0.8 }}>
          {labels[clampedLevel]}
        </span>
      )}
    </span>
  );
}
