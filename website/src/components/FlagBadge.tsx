import React from 'react';

// ISO 3166-1 alpha-2 → flag emoji + country name
const COUNTRY_FLAGS: Record<string, { flag: string; name: string }> = {
  fi: { flag: '🇫🇮', name: 'Finland' },
  fr: { flag: '🇫🇷', name: 'France' },
  de: { flag: '🇩🇪', name: 'Germany' },
  it: { flag: '🇮🇹', name: 'Italy' },
  jp: { flag: '🇯🇵', name: 'Japan' },
  kr: { flag: '🇰🇷', name: 'South Korea' },
  es: { flag: '🇪🇸', name: 'Spain' },
  nl: { flag: '🇳🇱', name: 'Netherlands' },
  ru: { flag: '🇷🇺', name: 'Russia' },
  se: { flag: '🇸🇪', name: 'Sweden' },
};

interface FlagBadgeProps {
  country?: string;
}

export default function FlagBadge({ country }: FlagBadgeProps): JSX.Element | null {
  if (!country) return null;
  const info = COUNTRY_FLAGS[country.toLowerCase()];
  if (!info) return null;

  return (
    <span
      title={info.name}
      style={{
        fontSize: '1.2em',
        marginLeft: '0.5em',
        verticalAlign: 'middle',
        cursor: 'default',
      }}
    >
      {info.flag}
    </span>
  );
}
