import React, { useState, useEffect, useMemo } from 'react';

// ── 类型 ────────────────────────────────────────

interface PricePoint {
  week: string;
  median_usd: number;
  min_usd: number;
  max_usd: number;
  sample_size: number;
}

interface GpuHistory {
  gpu_name: string;
  history: PricePoint[];
}

// ── 预定义 GPU 列表 ─────────────────────────────

const GPU_LIST = [
  { id: 'AMD_Instinct_MI50_16GB', name: 'MI50 (16GB)', cat: 'instinct' },
  { id: 'AMD_Instinct_MI100', name: 'MI100', cat: 'instinct' },
  { id: 'AMD_Instinct_MI210', name: 'MI210', cat: 'instinct' },
  { id: 'AMD_Radeon_RX_6800', name: 'RX 6800', cat: 'radeon' },
  { id: 'AMD_Radeon_RX_6800_XT', name: 'RX 6800 XT', cat: 'radeon' },
  { id: 'AMD_Radeon_RX_6900_XT', name: 'RX 6900 XT', cat: 'radeon' },
  { id: 'AMD_Radeon_RX_7900_XT', name: 'RX 7900 XT', cat: 'radeon' },
  { id: 'AMD_Radeon_RX_7900_XTX', name: 'RX 7900 XTX', cat: 'radeon' },
];

// ── 组件 ────────────────────────────────────────

export default function PriceChart() {
  const [history, setHistory] = useState<Record<string, PricePoint[]>>({});
  const [selectedGpu, setSelectedGpu] = useState('AMD_Radeon_RX_7900_XTX');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('/data/prices/price-history.json')
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(data => {
        const weeks = data.weeks || {};
        const gpuMap: Record<string, PricePoint[]> = {};

        for (const [weekTag, weekData] of Object.entries(weeks) as [string, any][]) {
          const entries = weekData.entries || [];
          for (const entry of entries) {
            const key = entry.gpu_id || entry.gpu_name?.replace(/[^a-zA-Z0-9]/g, '_');
            if (!gpuMap[key]) gpuMap[key] = [];
            gpuMap[key].push({
              week: weekTag,
              median_usd: entry.median_usd,
              min_usd: entry.min_usd,
              max_usd: entry.max_usd,
              sample_size: entry.sample_size,
            });
          }
        }

        // 排序每个 GPU 的历史
        for (const key of Object.keys(gpuMap)) {
          gpuMap[key].sort((a, b) => a.week.localeCompare(b.week));
        }

        setHistory(gpuMap);
        setLoading(false);
      })
      .catch(() => {
        setError('暂无历史价格数据。等待首次数据采集后自动显示。');
        setLoading(false);
      });
  }, []);

  const chartData = history[selectedGpu] || [];

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>⏳ 加载趋势数据...</div>;
  }

  if (error) {
    return (
      <div style={{ padding: '2rem', textAlign: 'center', background: 'var(--ifm-color-warning-contrast-background)', borderRadius: 8 }}>
        📈 {error}
      </div>
    );
  }

  return (
    <div>
      {/* ── GPU 选择器 ── */}
      <div style={{ marginBottom: '1rem', display: 'flex', gap: '0.4rem', flexWrap: 'wrap' }}>
        {GPU_LIST.map(gpu => (
          <button
            key={gpu.id}
            onClick={() => setSelectedGpu(gpu.id)}
            style={{
              padding: '0.3rem 0.7rem', border: '1px solid var(--ifm-color-emphasis-300)',
              borderRadius: 4, cursor: 'pointer', fontSize: '0.85rem',
              background: selectedGpu === gpu.id ? 'var(--ifm-color-primary)' : 'transparent',
              color: selectedGpu === gpu.id ? 'white' : 'var(--ifm-color-emphasis-700)',
              opacity: history[gpu.id]?.length ? 1 : 0.4,
            }}
            title={history[gpu.id]?.length ? `${history[gpu.id].length} 周数据` : '暂无数据'}
          >
            {gpu.name}
          </button>
        ))}
      </div>

      {/* ── 趋势图 ── */}
      {chartData.length > 0 ? (
        <PriceLineChart data={chartData} gpuName={GPU_LIST.find(g => g.id === selectedGpu)?.name || selectedGpu} />
      ) : (
        <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--ifm-color-secondary-darkest)' }}>
          该 GPU 暂无历史数据
        </div>
      )}

      {/* ── 数据表 ── */}
      {chartData.length > 0 && (
        <div style={{ marginTop: '1rem', overflowX: 'auto' }}>
          <table style={{ width: '100%', fontSize: '0.85rem', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ borderBottom: '2px solid var(--ifm-color-emphasis-300)' }}>
                <th style={{ textAlign: 'left', padding: '0.3rem' }}>周</th>
                <th style={{ textAlign: 'right', padding: '0.3rem' }}>中位数 (USD)</th>
                <th style={{ textAlign: 'right', padding: '0.3rem' }}>最低</th>
                <th style={{ textAlign: 'right', padding: '0.3rem' }}>最高</th>
                <th style={{ textAlign: 'right', padding: '0.3rem' }}>样本</th>
              </tr>
            </thead>
            <tbody>
              {chartData.map(pt => (
                <tr key={pt.week} style={{ borderBottom: '1px solid var(--ifm-color-emphasis-200)' }}>
                  <td style={{ padding: '0.25rem 0.3rem' }}>{pt.week}</td>
                  <td style={{ textAlign: 'right', padding: '0.25rem 0.3rem', fontWeight: 600, fontFamily: 'monospace' }}>
                    ${pt.median_usd.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </td>
                  <td style={{ textAlign: 'right', padding: '0.25rem 0.3rem', fontFamily: 'monospace', color: '#16a34a' }}>
                    ${pt.min_usd.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </td>
                  <td style={{ textAlign: 'right', padding: '0.25rem 0.3rem', fontFamily: 'monospace', color: '#dc2626' }}>
                    ${pt.max_usd.toLocaleString(undefined, { maximumFractionDigits: 0 })}
                  </td>
                  <td style={{ textAlign: 'right', padding: '0.25rem 0.3rem' }}>{pt.sample_size}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

// ── SVG 折线图 ──────────────────────────────────

function PriceLineChart({ data, gpuName }: { data: PricePoint[]; gpuName: string }) {
  const WIDTH = 700;
  const HEIGHT = 300;
  const PADDING = { top: 20, right: 20, bottom: 40, left: 60 };
  const chartW = WIDTH - PADDING.left - PADDING.right;
  const chartH = HEIGHT - PADDING.top - PADDING.bottom;

  const values = data.map(d => d.median_usd);
  const allValues = data.flatMap(d => [d.min_usd, d.max_usd, d.median_usd]);
  const yMin = Math.min(...allValues) * 0.9;
  const yMax = Math.max(...allValues) * 1.1;
  const yRange = yMax - yMin || 1;

  const xScale = (i: number) => PADDING.left + (i / Math.max(data.length - 1, 1)) * chartW;
  const yScale = (v: number) => PADDING.top + chartH - ((v - yMin) / yRange) * chartH;

  // 构建折线路径
  const linePath = data.map((d, i) => `${i === 0 ? 'M' : 'L'}${xScale(i)},${yScale(d.median_usd)}`).join(' ');
  const areaPath = linePath + ` L${xScale(data.length - 1)},${yScale(yMin)} L${xScale(0)},${yScale(yMin)} Z`;

  // Y轴刻度
  const yTicks = 5;
  const yTickValues = Array.from({ length: yTicks }, (_, i) => yMin + (yRange / (yTicks - 1)) * i);

  return (
    <div style={{ overflowX: 'auto' }}>
      <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} style={{ width: '100%', maxWidth: WIDTH, fontFamily: 'sans-serif' }}>
        {/* 网格线 */}
        {yTickValues.map(v => (
          <line key={v} x1={PADDING.left} y1={yScale(v)} x2={WIDTH - PADDING.right} y2={yScale(v)}
            stroke="var(--ifm-color-emphasis-200)" strokeDasharray="4,4" />
        ))}

        {/* Y轴标签 */}
        {yTickValues.map(v => (
          <text key={v} x={PADDING.left - 8} y={yScale(v) + 4}
            textAnchor="end" fontSize={11} fill="var(--ifm-color-emphasis-600)">
            ${Math.round(v).toLocaleString()}
          </text>
        ))}

        {/* 面积填充 */}
        <path d={areaPath} fill="var(--ifm-color-primary-lightest)" opacity={0.15} />

        {/* 中位数折线 */}
        <path d={linePath} fill="none" stroke="var(--ifm-color-primary)" strokeWidth={2.5}
          strokeLinecap="round" strokeLinejoin="round" />

        {/* 最低-最高范围线 */}
        {data.map((d, i) => (
          <line key={i} x1={xScale(i)} y1={yScale(d.min_usd)} x2={xScale(i)} y2={yScale(d.max_usd)}
            stroke="var(--ifm-color-emphasis-400)" strokeWidth={1} opacity={0.5} />
        ))}

        {/* 数据点 */}
        {data.map((d, i) => (
          <circle key={i} cx={xScale(i)} cy={yScale(d.median_usd)} r={3}
            fill="var(--ifm-color-primary)" stroke="white" strokeWidth={1} />
        ))}

        {/* X轴标签 */}
        {data.map((d, i) => (
          (data.length <= 12 || i % Math.ceil(data.length / 8) === 0) && (
            <text key={i} x={xScale(i)} y={HEIGHT - 8}
              textAnchor="middle" fontSize={10} fill="var(--ifm-color-emphasis-600)"
              transform={`rotate(-30,${xScale(i)},${HEIGHT - 8})`}>
              {d.week}
            </text>
          )
        ))}

        {/* 标题 */}
        <text x={WIDTH / 2} y={14} textAnchor="middle" fontSize={13} fontWeight={600}
          fill="var(--ifm-color-emphasis-800)">
          {gpuName} · 二手价格趋势 (USD)
        </text>
      </svg>
    </div>
  );
}
