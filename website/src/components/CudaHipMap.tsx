import React, { useState, useMemo, useEffect } from 'react';

interface CudaHipPair {
  cuda: string;
  hip: string;
  category: string;
  status: string;
  notes: string;
}

// 内联备用数据（304 条完整映射在 /data/cuda-hip-api-map.json）
const FALLBACK_DATA: CudaHipPair[] = [
  { cuda: 'cudaMalloc', hip: 'hipMalloc', category: '内存管理', status: 'supported', notes: '' },
  { cuda: 'cudaFree', hip: 'hipFree', category: '内存管理', status: 'supported', notes: '' },
  { cuda: 'cudaMemcpy', hip: 'hipMemcpy', category: '内存管理', status: 'supported', notes: '' },
  { cuda: 'cudaSetDevice', hip: 'hipSetDevice', category: '设备管理', status: 'supported', notes: '' },
  { cuda: 'cudaGetDeviceCount', hip: 'hipGetDeviceCount', category: '设备管理', status: 'supported', notes: '' },
  { cuda: 'cudaStreamCreate', hip: 'hipStreamCreate', category: '流管理', status: 'supported', notes: '' },
  { cuda: 'cudaEventCreate', hip: 'hipEventCreate', category: '事件管理', status: 'supported', notes: '' },
  { cuda: 'cudaLaunchKernel', hip: 'hipLaunchKernel', category: '执行控制', status: 'supported', notes: '' },
  { cuda: 'cudaGetLastError', hip: 'hipGetLastError', category: '错误处理', status: 'supported', notes: '' },
  { cuda: 'cublasSgemm', hip: 'hipblasSgemm', category: 'Library: cuBLAS', status: 'supported', notes: '' },
];

export default function CudaHipMap() {
  const [data, setData] = useState<CudaHipPair[]>(FALLBACK_DATA);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');

  useEffect(() => {
    // 从 static/data/ 加载完整的 304 条映射
    fetch('/data/cuda-hip-api-map.json')
      .then(res => res.json())
      .then((json: CudaHipPair[]) => {
        if (Array.isArray(json) && json.length > 0) {
          setData(json);
        }
      })
      .catch(() => {
        // 使用 fallback
      });
  }, []);

  const categories = useMemo(() => [...new Set(data.map(a => a.category))].sort(), [data]);

  const filtered = useMemo(() => {
    return data.filter(a => {
      const q = search.toLowerCase();
      const matchSearch = !q || a.cuda.toLowerCase().includes(q) || a.hip.toLowerCase().includes(q) || a.notes.toLowerCase().includes(q);
      const matchCat = !category || a.category === category;
      return matchSearch && matchCat;
    });
  }, [data, search, category]);

  const unsupportedCount = data.filter(a => a.status !== 'supported').length;

  return (
    <div style={{ margin: '1.5rem 0' }}>
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap', alignItems: 'center' }}>
        <input
          type="text"
          placeholder="搜索 CUDA 或 HIP API..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          style={{ padding: '6px 12px', borderRadius: '6px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.85rem', minWidth: '200px' }}
        />
        <select value={category} onChange={e => setCategory(e.target.value)}
          style={{ padding: '6px 12px', borderRadius: '6px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.85rem' }}>
          <option value="">全部类别 ({categories.length})</option>
          {categories.map(c => <option key={c} value={c}>{c}</option>)}
        </select>
        <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', alignSelf: 'center' }}>
          {filtered.length} / {data.length} 匹配
          {unsupportedCount > 0 && <span style={{ color: 'var(--ifm-color-warning)', marginLeft: '0.5rem' }}>（{unsupportedCount} 条无等价API）</span>}
        </span>
      </div>

      <table style={{ width: '100%', fontSize: '0.85rem', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid var(--ifm-color-emphasis-300)' }}>
            <th style={thStyle}>CUDA</th>
            <th style={thStyle}>→</th>
            <th style={thStyle}>HIP</th>
            <th style={thStyle}>类别</th>
            <th style={thStyle}>状态</th>
            <th style={thStyle}>备注</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((row, i) => (
            <tr key={i} style={{ borderBottom: '1px solid var(--ifm-color-emphasis-200)' }}>
              <td style={tdStyle}><code style={{ fontSize: '0.82rem', color: '#76b900' }}>{row.cuda}</code></td>
              <td style={{ ...tdStyle, width: '30px', textAlign: 'center', color: 'var(--ifm-color-emphasis-400)' }}>→</td>
              <td style={tdStyle}>
                <code style={{
                  fontSize: '0.82rem',
                  color: row.status === 'supported' ? 'var(--ifm-color-primary)' : 'var(--ifm-color-warning)',
                  textDecoration: row.status === 'supported' ? 'none' : 'line-through',
                }}>
                  {row.hip}
                </code>
              </td>
              <td style={tdStyle}><span style={{ fontSize: '0.72rem', background: 'var(--ifm-color-emphasis-100)', padding: '1px 6px', borderRadius: '4px' }}>{row.category}</span></td>
              <td style={tdStyle}>
                <span style={{
                  fontSize: '0.7rem',
                  padding: '1px 6px',
                  borderRadius: '4px',
                  background: row.status === 'supported' ? '#dcfce7' : '#fef3c7',
                  color: row.status === 'supported' ? '#166534' : '#92400e',
                }}>
                  {row.status === 'supported' ? '✓' : '✗'}
                </span>
              </td>
              <td style={{ ...tdStyle, color: 'var(--ifm-color-emphasis-600)', fontSize: '0.75rem', maxWidth: '200px' }}>{row.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const thStyle: React.CSSProperties = {
  padding: '8px 12px', textAlign: 'left', fontWeight: 600, whiteSpace: 'nowrap',
};
const tdStyle: React.CSSProperties = {
  padding: '6px 12px', verticalAlign: 'top',
};
