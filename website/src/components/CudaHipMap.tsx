import React, { useState, useMemo } from 'react';

interface CudaHipPair {
  cuda: string;
  hip: string;
  category: string;
  notes: string;
}

// 从 data/cuda-hip-api-map.json 预编译的内联数据（核心 API）
const API_MAP: CudaHipPair[] = [
  // ── Device Management ──
  { cuda: 'cudaSetDevice', hip: 'hipSetDevice', category: '设备管理', notes: '' },
  { cuda: 'cudaGetDevice', hip: 'hipGetDevice', category: '设备管理', notes: '' },
  { cuda: 'cudaGetDeviceCount', hip: 'hipGetDeviceCount', category: '设备管理', notes: '' },
  { cuda: 'cudaGetDeviceProperties', hip: 'hipGetDeviceProperties', category: '设备管理', notes: '' },
  { cuda: 'cudaSetDeviceFlags', hip: 'hipSetDeviceFlags', category: '设备管理', notes: '' },
  { cuda: 'cudaDeviceSynchronize', hip: 'hipDeviceSynchronize', category: '设备管理', notes: '' },
  { cuda: 'cudaDeviceReset', hip: 'hipDeviceReset', category: '设备管理', notes: '' },
  { cuda: 'cudaChooseDevice', hip: 'hipChooseDevice', category: '设备管理', notes: '' },

  // ── Memory Management ──
  { cuda: 'cudaMalloc', hip: 'hipMalloc', category: '内存管理', notes: '' },
  { cuda: 'cudaMallocHost', hip: 'hipHostMalloc', category: '内存管理', notes: '参数顺序不同' },
  { cuda: 'cudaMallocManaged', hip: 'hipMallocManaged', category: '内存管理', notes: '' },
  { cuda: 'cudaFree', hip: 'hipFree', category: '内存管理', notes: '' },
  { cuda: 'cudaFreeHost', hip: 'hipHostFree', category: '内存管理', notes: '' },
  { cuda: 'cudaMemcpy', hip: 'hipMemcpy', category: '内存管理', notes: '' },
  { cuda: 'cudaMemcpyAsync', hip: 'hipMemcpyAsync', category: '内存管理', notes: '' },
  { cuda: 'cudaMemcpy2D', hip: 'hipMemcpy2D', category: '内存管理', notes: '' },
  { cuda: 'cudaMemcpyToSymbol', hip: 'hipMemcpyToSymbol', category: '内存管理', notes: '' },
  { cuda: 'cudaMemset', hip: 'hipMemset', category: '内存管理', notes: '' },
  { cuda: 'cudaMemGetInfo', hip: 'hipMemGetInfo', category: '内存管理', notes: '' },
  { cuda: 'cudaHostAlloc', hip: 'hipHostMalloc', category: '内存管理', notes: 'cudaHostAlloc → hipHostMalloc' },
  { cuda: 'cudaHostRegister', hip: 'hipHostRegister', category: '内存管理', notes: '' },

  // ── Stream Management ──
  { cuda: 'cudaStreamCreate', hip: 'hipStreamCreate', category: '流管理', notes: '' },
  { cuda: 'cudaStreamDestroy', hip: 'hipStreamDestroy', category: '流管理', notes: '' },
  { cuda: 'cudaStreamSynchronize', hip: 'hipStreamSynchronize', category: '流管理', notes: '' },
  { cuda: 'cudaStreamWaitEvent', hip: 'hipStreamWaitEvent', category: '流管理', notes: '' },

  // ── Event Management ──
  { cuda: 'cudaEventCreate', hip: 'hipEventCreate', category: '事件管理', notes: '' },
  { cuda: 'cudaEventRecord', hip: 'hipEventRecord', category: '事件管理', notes: '' },
  { cuda: 'cudaEventSynchronize', hip: 'hipEventSynchronize', category: '事件管理', notes: '' },
  { cuda: 'cudaEventElapsedTime', hip: 'hipEventElapsedTime', category: '事件管理', notes: '' },
  { cuda: 'cudaEventDestroy', hip: 'hipEventDestroy', category: '事件管理', notes: '' },

  // ── Kernel Launch ──
  { cuda: '__global__', hip: '__global__', category: 'Kernel', notes: '完全相同' },
  { cuda: '__device__', hip: '__device__', category: 'Kernel', notes: '完全相同' },
  { cuda: '__host__', hip: '__host__', category: 'Kernel', notes: '完全相同' },
  { cuda: '<<<>>>', hip: '<<<>>>', category: 'Kernel', notes: '启动语法相同' },
  { cuda: 'cudaDeviceSynchronize', hip: 'hipDeviceSynchronize', category: 'Kernel', notes: '' },

  // ── Error Handling ──
  { cuda: 'cudaGetLastError', hip: 'hipGetLastError', category: '错误处理', notes: '' },
  { cuda: 'cudaGetErrorString', hip: 'hipGetErrorString', category: '错误处理', notes: '' },
  { cuda: 'cudaSuccess', hip: 'hipSuccess', category: '错误处理', notes: '' },
  { cuda: 'cudaError_t', hip: 'hipError_t', category: '错误处理', notes: '' },

  // ── Math / Device Functions ──
  { cuda: '__syncthreads', hip: '__syncthreads', category: '同步', notes: '完全相同' },
  { cuda: 'threadIdx', hip: 'threadIdx', category: '线程索引', notes: '完全相同' },
  { cuda: 'blockIdx', hip: 'blockIdx', category: '线程索引', notes: '完全相同' },
  { cuda: 'blockDim', hip: 'blockDim', category: '线程索引', notes: '完全相同' },
  { cuda: 'gridDim', hip: 'gridDim', category: '线程索引', notes: '完全相同' },
  { cuda: 'warpSize', hip: 'warpSize', category: '线程索引', notes: 'HIP: 64 (Wavefront) vs CUDA: 32 (Warp)' },

  // ── Graph APIs ──
  { cuda: 'cudaGraphCreate', hip: 'hipGraphCreate', category: 'Graph API', notes: '' },
  { cuda: 'cudaGraphLaunch', hip: 'hipGraphLaunch', category: 'Graph API', notes: '' },
];

const CATEGORIES = [...new Set(API_MAP.map(a => a.category))];

export default function CudaHipMap() {
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');

  const filtered = useMemo(() => {
    return API_MAP.filter(a => {
      const q = search.toLowerCase();
      const matchSearch = !q || a.cuda.toLowerCase().includes(q) || a.hip.toLowerCase().includes(q) || a.notes.toLowerCase().includes(q);
      const matchCat = !category || a.category === category;
      return matchSearch && matchCat;
    });
  }, [search, category]);

  return (
    <div style={{ margin: '1.5rem 0' }}>
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap' }}>
        <input
          type="text"
          placeholder="搜索 CUDA 或 HIP API..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          style={{ padding: '6px 12px', borderRadius: '6px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.85rem', minWidth: '200px' }}
        />
        <select value={category} onChange={e => setCategory(e.target.value)}
          style={{ padding: '6px 12px', borderRadius: '6px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.85rem' }}>
          <option value="">全部类别</option>
          {CATEGORIES.map(c => <option key={c} value={c}>{c}</option>)}
        </select>
        <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', alignSelf: 'center' }}>
          {filtered.length} / {API_MAP.length} 匹配
        </span>
      </div>

      <table style={{ width: '100%', fontSize: '0.85rem', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ borderBottom: '2px solid var(--ifm-color-emphasis-300)' }}>
            <th style={thStyle}>CUDA</th>
            <th style={thStyle}>→</th>
            <th style={thStyle}>HIP</th>
            <th style={thStyle}>类别</th>
            <th style={thStyle}>备注</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((row, i) => (
            <tr key={i} style={{ borderBottom: '1px solid var(--ifm-color-emphasis-200)' }}>
              <td style={tdStyle}><code style={{ fontSize: '0.82rem', color: '#76b900' }}>{row.cuda}</code></td>
              <td style={{ ...tdStyle, width: '30px', textAlign: 'center', color: 'var(--ifm-color-emphasis-400)' }}>→</td>
              <td style={tdStyle}><code style={{ fontSize: '0.82rem', color: 'var(--ifm-color-primary)' }}>{row.hip}</code></td>
              <td style={tdStyle}><span style={{ fontSize: '0.75rem', background: 'var(--ifm-color-emphasis-100)', padding: '2px 6px', borderRadius: '4px' }}>{row.category}</span></td>
              <td style={{ ...tdStyle, color: 'var(--ifm-color-emphasis-600)', fontSize: '0.78rem' }}>{row.notes}</td>
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
