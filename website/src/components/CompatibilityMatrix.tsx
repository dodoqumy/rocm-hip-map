import React, { useState, useMemo } from 'react';

interface CompatEntry {
  gpu: string;
  rocm: string[];
  os: string[];
  pytorch: string;
  tensorflow: string;
  notes: string;
}

const COMPAT_DATA: CompatEntry[] = [
  { gpu: 'MI300X', rocm: ['6.2', '6.3', '7.0', '7.1', '7.2'], os: ['Ubuntu 22.04', 'RHEL 9'], pytorch: '2.4+', tensorflow: '2.15+', notes: '推荐旗舰配置' },
  { gpu: 'MI250X', rocm: ['5.7', '6.0', '6.1', '6.2', '6.3', '7.0'], os: ['Ubuntu 22.04', 'RHEL 8/9'], pytorch: '2.0+', tensorflow: '2.13+', notes: '' },
  { gpu: 'MI250', rocm: ['5.6', '5.7', '6.0', '6.1', '6.2', '6.3'], os: ['Ubuntu 20.04/22.04', 'RHEL 8'], pytorch: '2.0+', tensorflow: '2.13+', notes: '' },
  { gpu: 'MI210', rocm: ['5.5', '5.6', '5.7', '6.0', '6.1', '6.2'], os: ['Ubuntu 20.04/22.04', 'RHEL 8'], pytorch: '1.13+', tensorflow: '2.12+', notes: '' },
  { gpu: 'MI100', rocm: ['5.0', '5.1', '5.2', '5.3', '5.4', '5.5'], os: ['Ubuntu 20.04', 'RHEL 8'], pytorch: '1.12+', tensorflow: '2.11+', notes: 'CDNA1 架构' },
  { gpu: 'MI50', rocm: ['4.5', '5.0', '5.1', '5.2'], os: ['Ubuntu 20.04'], pytorch: '1.10+', tensorflow: '2.9+', notes: '即将停更' },
  { gpu: 'RX 7900 XTX', rocm: ['6.0', '6.1', '6.2', '6.3', '7.0', '7.1', '7.2'], os: ['Ubuntu 22.04', 'Arch'], pytorch: '2.2+', tensorflow: '⚠️ 实验', notes: 'RDNA3，消费级' },
  { gpu: 'RX 6800', rocm: ['5.5', '5.6', '5.7', '6.0', '6.1', '6.2'], os: ['Ubuntu 22.04'], pytorch: '2.0+', tensorflow: '⚠️ 实验', notes: 'RDNA2，部分支持' },
];

const ALL_ROCM = [...new Set(COMPAT_DATA.flatMap(d => d.rocm))].sort();
const ALL_OS = [...new Set(COMPAT_DATA.flatMap(d => d.os))].sort();
const ALL_GPU = COMPAT_DATA.map(d => d.gpu);

export default function CompatibilityMatrix() {
  const [filterGpu, setFilterGpu] = useState('');
  const [filterRocm, setFilterRocm] = useState('');
  const [filterOs, setFilterOs] = useState('');

  const filtered = useMemo(() => {
    return COMPAT_DATA.filter(d => {
      if (filterGpu && !d.gpu.toLowerCase().includes(filterGpu.toLowerCase())) return false;
      if (filterRocm && !d.rocm.some(v => v.includes(filterRocm))) return false;
      if (filterOs && !d.os.some(o => o.toLowerCase().includes(filterOs.toLowerCase()))) return false;
      return true;
    });
  }, [filterGpu, filterRocm, filterOs]);

  return (
    <div style={{ overflowX: 'auto', margin: '1.5rem 0' }}>
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap' }}>
        <select value={filterGpu} onChange={e => setFilterGpu(e.target.value)}
          style={{ padding: '4px 8px', borderRadius: '4px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.8rem' }}>
          <option value="">全部 GPU</option>
          {ALL_GPU.map(g => <option key={g} value={g}>{g}</option>)}
        </select>
        <select value={filterRocm} onChange={e => setFilterRocm(e.target.value)}
          style={{ padding: '4px 8px', borderRadius: '4px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.8rem' }}>
          <option value="">全部 ROCm 版本</option>
          {ALL_ROCM.map(v => <option key={v} value={v}>{v}</option>)}
        </select>
        <select value={filterOs} onChange={e => setFilterOs(e.target.value)}
          style={{ padding: '4px 8px', borderRadius: '4px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.8rem' }}>
          <option value="">全部 OS</option>
          {ALL_OS.map(o => <option key={o} value={o}>{o}</option>)}
        </select>
        <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', alignSelf: 'center' }}>
          {filtered.length} / {COMPAT_DATA.length} 匹配
        </span>
      </div>

      <table style={{ width: '100%', fontSize: '0.85rem', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid var(--ifm-color-emphasis-300)' }}>
            <th style={thStyle}>GPU</th>
            <th style={thStyle}>ROCm</th>
            <th style={thStyle}>OS</th>
            <th style={thStyle}>PyTorch</th>
            <th style={thStyle}>TensorFlow</th>
            <th style={thStyle}>备注</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((row, i) => (
            <tr key={i} style={{ borderBottom: '1px solid var(--ifm-color-emphasis-200)' }}>
              <td style={tdStyle}><strong>{row.gpu}</strong></td>
              <td style={tdStyle}>{row.rocm.join(', ')}</td>
              <td style={tdStyle}>{row.os.join(', ')}</td>
              <td style={tdStyle}>{row.pytorch}</td>
              <td style={tdStyle}>{row.tensorflow}</td>
              <td style={{ ...tdStyle, color: 'var(--ifm-color-emphasis-600)', fontSize: '0.78rem' }}>{row.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const thStyle: React.CSSProperties = {
  padding: '8px 12px',
  textAlign: 'left',
  fontWeight: 600,
  whiteSpace: 'nowrap',
};

const tdStyle: React.CSSProperties = {
  padding: '6px 12px',
  verticalAlign: 'top',
};
