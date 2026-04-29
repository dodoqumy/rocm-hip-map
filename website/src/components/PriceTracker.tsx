import React, { useState, useMemo, useEffect } from 'react';

// ── 类型 ────────────────────────────────────────

interface PriceEntry {
  gpu_id: string;
  gpu_name: string;
  country: string;
  platform: string;
  condition: string;
  currency_original: string;
  median_usd: number;
  min_usd: number;
  max_usd: number;
  sample_size: number;
  original_sample_size: number;
  source_url: string;
  collected_at: string;
}

interface PriceWeek {
  updated: string;
  week: string;
  rates: Record<string, number>;
  entries: PriceEntry[];
}

// ── 国旗映射 ────────────────────────────────────

const COUNTRY_FLAGS: Record<string, string> = {
  US: '🇺🇸',
  DE: '🇩🇪',
  GB: '🇬🇧',
  CN: '🇨🇳',
  JP: '🇯🇵',
  KR: '🇰🇷',
  FR: '🇫🇷',
  RU: '🇷🇺',
  IT: '🇮🇹',
};

// ── 条件颜色 ─────────────────────────────────────

const CONDITION_COLORS: Record<string, string> = {
  new: '#22c55e',
  open_box: '#3b82f6',
  used: '#f59e0b',
  refurbished: '#ef4444',
  parts: '#6b7280',
};

const CONDITION_LABELS: Record<string, string> = {
  new: '全新',
  open_box: '开封',
  used: '二手',
  refurbished: '翻新',
  parts: '零件',
};

// ── 组件 ────────────────────────────────────────

export default function PriceTracker() {
  const [data, setData] = useState<PriceWeek | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [category, setCategory] = useState<'all' | 'instinct' | 'radeon'>('all');

  useEffect(() => {
    // 加载最新的标准化价格数据
    fetch('/data/prices/prices-latest.json')
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((json: PriceWeek) => {
        setData(json);
        setLoading(false);
      })
      .catch(() => {
        // 尝试加载本周数据
        const now = new Date();
        const year = now.getFullYear();
        const weekNum = getISOWeek(now);
        const weekTag = `${year}-W${String(weekNum).padStart(2, '0')}`;
        fetch(`/data/prices/prices-${weekTag}-normalized.json`)
          .then(res => res.json())
          .then((json: PriceWeek) => {
            setData(json);
            setLoading(false);
          })
          .catch(() => {
            setError('暂无价格数据。等待首次数据采集后自动显示。');
            setLoading(false);
          });
      });
  }, []);

  // 分组：GPU → 国家+平台
  const grouped = useMemo(() => {
    if (!data?.entries) return new Map<string, PriceEntry[]>();

    const map = new Map<string, PriceEntry[]>();
    for (const entry of data.entries) {
      const key = entry.gpu_name;
      let list = map.get(key);
      if (!list) {
        list = [];
        map.set(key, list);
      }
      list.push(entry);
    }
    return map;
  }, [data]);

  if (loading) {
    return (
      <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--ifm-color-secondary-darkest)' }}>
        ⏳ 加载价格数据...
      </div>
    );
  }

  if (error) {
    return (
      <div style={{
        padding: '2rem', textAlign: 'center',
        background: 'var(--ifm-color-warning-contrast-background)',
        borderRadius: 8,
      }}>
        <p style={{ margin: 0 }}>📊 {error}</p>
        <p style={{ fontSize: '0.85rem', marginTop: '0.5rem', color: 'var(--ifm-color-secondary-darkest)' }}>
          价格数据由 CI 每周一自动抓取并更新。
        </p>
      </div>
    );
  }

  return (
    <div>
      {/* ── 更新信息 ── */}
      <div style={{
        marginBottom: '1rem', padding: '0.5rem 1rem',
        background: 'var(--ifm-color-emphasis-100)',
        borderRadius: 6, fontSize: '0.85rem',
        display: 'flex', justifyContent: 'space-between', flexWrap: 'wrap',
      }}>
        <span>📅 更新：{data?.updated ? new Date(data.updated).toLocaleDateString('zh-CN') : '—'}</span>
        <span>📊 {data?.entries.length || 0} 条价格记录</span>
      </div>

      {/* ── 分类筛选 ── */}
      <div style={{ marginBottom: '1rem', display: 'flex', gap: '0.5rem' }}>
        {(['all', 'instinct', 'radeon'] as const).map(cat => (
          <button
            key={cat}
            onClick={() => setCategory(cat)}
            style={{
              padding: '0.3rem 0.8rem', border: '1px solid var(--ifm-color-emphasis-300)',
              borderRadius: 4, cursor: 'pointer', fontSize: '0.85rem',
              background: category === cat ? 'var(--ifm-color-primary)' : 'transparent',
              color: category === cat ? 'white' : 'var(--ifm-color-emphasis-700)',
            }}
          >
            {cat === 'all' ? '全部' : cat === 'instinct' ? '🧮 Instinct 计算卡' : '🎮 Radeon 消费卡'}
          </button>
        ))}
      </div>

      {/* ── 价格表格 ── */}
      <div style={{ overflowX: 'auto' }}>
        <table style={{ width: '100%', fontSize: '0.9rem', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid var(--ifm-color-emphasis-300)' }}>
              <th style={{ textAlign: 'left', padding: '0.5rem' }}>GPU 型号</th>
              <th style={{ textAlign: 'center', padding: '0.5rem' }}>国家</th>
              <th style={{ textAlign: 'center', padding: '0.5rem' }}>平台</th>
              <th style={{ textAlign: 'right', padding: '0.5rem' }}>中位数 (USD)</th>
              <th style={{ textAlign: 'right', padding: '0.5rem' }}>最低价</th>
              <th style={{ textAlign: 'right', padding: '0.5rem' }}>最高价</th>
              <th style={{ textAlign: 'center', padding: '0.5rem' }}>样本</th>
              <th style={{ textAlign: 'center', padding: '0.5rem' }}>来源</th>
            </tr>
          </thead>
          <tbody>
            {Array.from(grouped.entries()).map(([gpuName, entries]) => {
              // 分类过滤
              const isInstinct = gpuName.includes('Instinct') || gpuName.includes('MI');
              if (category === 'instinct' && !isInstinct) return null;
              if (category === 'radeon' && isInstinct) return null;

              return entries.map((entry, idx) => (
                <tr
                  key={`${entry.gpu_id}-${entry.country}-${entry.platform}`}
                  style={{
                    borderBottom: '1px solid var(--ifm-color-emphasis-200)',
                    background: idx === 0 ? 'var(--ifm-color-emphasis-100)' : undefined,
                  }}
                >
                  <td style={{ padding: '0.4rem 0.5rem', fontWeight: idx === 0 ? 600 : 400 }}>
                    {idx === 0 ? gpuName : ''}
                  </td>
                  <td style={{ textAlign: 'center', padding: '0.4rem 0.5rem' }}>
                    {COUNTRY_FLAGS[entry.country] || entry.country} {entry.country}
                  </td>
                  <td style={{ textAlign: 'center', padding: '0.4rem 0.5rem' }}>
                    {entry.platform}
                  </td>
                  <td style={{
                    textAlign: 'right', padding: '0.4rem 0.5rem',
                    fontWeight: 600, fontFamily: 'monospace',
                  }}>
                    ${entry.median_usd.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </td>
                  <td style={{
                    textAlign: 'right', padding: '0.4rem 0.5rem',
                    color: 'var(--ifm-color-success-darkest)', fontFamily: 'monospace',
                  }}>
                    ${entry.min_usd.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </td>
                  <td style={{
                    textAlign: 'right', padding: '0.4rem 0.5rem',
                    color: 'var(--ifm-color-danger-darkest)', fontFamily: 'monospace',
                  }}>
                    ${entry.max_usd.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </td>
                  <td style={{ textAlign: 'center', padding: '0.4rem 0.5rem' }}>
                    <span style={{
                      display: 'inline-block', padding: '0.1rem 0.4rem',
                      borderRadius: 10, fontSize: '0.8rem',
                      background: CONDITION_COLORS[entry.condition] || '#999',
                      color: 'white',
                    }}>
                      {CONDITION_LABELS[entry.condition] || entry.condition}
                    </span>
                    {' '}
                    <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-secondary-darkest)' }}>
                      n={entry.sample_size}
                    </span>
                  </td>
                  <td style={{ textAlign: 'center', padding: '0.4rem 0.5rem' }}>
                    <a href={entry.source_url} target="_blank" rel="noopener noreferrer"
                      style={{ fontSize: '0.8rem' }}>
                      🔗
                    </a>
                  </td>
                </tr>
              ));
            })}
          </tbody>
        </table>
      </div>

      {/* ── 数据说明 ── */}
      <div style={{
        marginTop: '1.5rem', padding: '0.8rem 1rem',
        background: 'var(--ifm-color-warning-contrast-background)',
        borderRadius: 6, fontSize: '0.8rem',
      }}>
        <strong>⚠️ 数据说明：</strong>
        价格为二手市场中位数（已过滤异常值），统一换算为 USD。
        价格可能因成色、地区、运费等因素浮动，仅供参考，不构成投资建议。
        {' '}来源包括 eBay (US/DE/UK)、闲鱼、Mercari 等平台公开数据。
      </div>
    </div>
  );
}

// ── 工具函数 ────────────────────────────────────

function getISOWeek(date: Date): number {
  const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
  const dayNum = d.getUTCDay() || 7;
  d.setUTCDate(d.getUTCDate() + 4 - dayNum);
  const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  return Math.ceil(((d.getTime() - yearStart.getTime()) / 86400000 + 1) / 7);
}
