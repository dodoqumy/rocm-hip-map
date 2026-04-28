import React, { useState, useMemo } from 'react';

interface ErrorEntry {
  code: string;
  type: 'runtime' | 'install' | 'compile';
  message: string;
  cause: string;
  workaround: string;
  fixVersion?: string;
  affectedGpu?: string[];
}

const ERROR_DB: ErrorEntry[] = [
  {
    code: 'hipErrorNoBinaryForGpu',
    type: 'runtime',
    message: 'No binary for GPU',
    cause: '编译时未包含当前 GPU 架构目标（如只编译了 gfx942 但在 gfx90a 上运行）',
    workaround: '重新编译并添加 `--offload-arch=<arch>` 参数，例如 `--offload-arch=gfx942,gfx90a` 覆盖所有目标 GPU',
    fixVersion: 'N/A（使用问题）',
    affectedGpu: ['all'],
  },
  {
    code: 'hipErrorOutOfMemory',
    type: 'runtime',
    message: 'Out of memory',
    cause: 'GPU 显存不足。可能原因：batch size 过大、模型过大、其他进程占用显存',
    workaround: '1) 减小 batch size 2) 使用 `hipSetDevice` 切换到空闲 GPU 3) 检查 `rocm-smi` 释放显存',
    affectedGpu: ['all'],
  },
  {
    code: 'hipErrorInvalidValue',
    type: 'runtime',
    message: 'Invalid argument value',
    cause: '传给 HIP API 的参数无效，通常是 NULL 指针或超出范围的参数',
    workaround: '检查 API 调用前的参数有效性，确保指针非空且值在合法范围',
  },
  {
    code: 'hipErrorNotReady',
    type: 'runtime',
    message: 'Device not ready',
    cause: 'GPU 尚未完成初始化或上一个操作',
    workaround: '在操作前调用 `hipDeviceSynchronize()` 确保设备就绪',
  },
  {
    code: 'HSA_STATUS_ERROR',
    type: 'install',
    message: 'HSA runtime error',
    cause: 'ROCm 驱动未正确加载，常见于 amdgpu 驱动版本与 ROCm 不匹配',
    workaround: '1) `dkms status` 检查驱动状态 2) `rocminfo` 验证 ROCm 可见 GPU 3) 重新安装匹配版本的 rocm-dkms',
    fixVersion: '确保 ROCm x.y.z 对应的 amdgpu 版本匹配',
    affectedGpu: ['all'],
  },
  {
    code: 'HSA_STATUS_ERROR_OUT_OF_RESOURCES',
    type: 'runtime',
    message: 'HSA out of resources',
    cause: 'GPU 资源耗尽，如可分配队列数超限',
    workaround: '减少并发 HIP stream 数量，确保 `hipStreamDestroy` 正确释放',
    affectedGpu: ['all'],
  },
  {
    code: 'rocBLAS_STATUS_INTERNAL_ERROR',
    type: 'runtime',
    message: 'rocBLAS internal error',
    cause: 'rocBLAS 内部状态异常，常见于输入 tensor 尺寸不合法或内存未对齐',
    workaround: '1) 检查矩阵维度是否合法（M/N/K > 0） 2) 确保 tensor 内存对齐到 128 字节',
    affectedGpu: ['all'],
  },
  {
    code: 'hipErrorInvalidDevice',
    type: 'runtime',
    message: 'Invalid device ordinal',
    cause: '指定的 GPU 设备 ID 不存在（如 8 GPU 系统指定 device 8）',
    workaround: '使用 `hipGetDeviceCount` 获取实际 GPU 数量，确保 device ID < count',
  },
  {
    code: 'MIOPEN_STATUS_NOT_INITIALIZED',
    type: 'runtime',
    message: 'MIOpen not initialized',
    cause: 'MIOpen handle 未创建或已销毁后继续使用',
    workaround: '确保 `miopenCreate` 在 `miopenDestroy` 之前调用，检查 handle 生命周期',
    affectedGpu: ['all'],
  },
  {
    code: 'LLVM ERROR: Unsupported GPU',
    type: 'compile',
    message: 'LLVM compilation for unsupported GPU arch',
    cause: '尝试为 HIP 不支持的 GPU 架构编译代码（如太旧的 GCN 架构）',
    workaround: '检查 GPU 是否在 HIP 支持列表中，使用 `rocminfo` 确认架构名',
    fixVersion: 'HIP 5.x 起仅支持 gfx90a+',
    affectedGpu: ['mi50', 'rx6800'],
  },
];

export default function ErrorCodeLookup() {
  const [search, setSearch] = useState('');
  const [typeFilter, setTypeFilter] = useState('');

  const filtered = useMemo(() => {
    return ERROR_DB.filter(e => {
      const q = search.toLowerCase();
      const matchQ = !q || e.code.toLowerCase().includes(q) || e.message.toLowerCase().includes(q) || e.cause.toLowerCase().includes(q);
      const matchT = !typeFilter || e.type === typeFilter;
      return matchQ && matchT;
    });
  }, [search, typeFilter]);

  const typeColor = (t: string) => t === 'runtime' ? '#3b82f6' : t === 'install' ? '#f97316' : '#8b5cf6';
  const typeLabel = (t: string) => t === 'runtime' ? '运行时' : t === 'install' ? '安装' : '编译';

  return (
    <div style={{ margin: '1.5rem 0' }}>
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap' }}>
        <input
          type="text" placeholder="搜索错误码或描述..."
          value={search} onChange={e => setSearch(e.target.value)}
          style={{ padding: '6px 12px', borderRadius: '6px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.85rem', minWidth: '220px' }}
        />
        <select value={typeFilter} onChange={e => setTypeFilter(e.target.value)}
          style={{ padding: '6px 12px', borderRadius: '6px', border: '1px solid var(--ifm-color-emphasis-300)', fontSize: '0.85rem' }}>
          <option value="">全部类型</option>
          <option value="runtime">运行时</option>
          <option value="install">安装</option>
          <option value="compile">编译</option>
        </select>
        <span style={{ fontSize: '0.8rem', color: 'var(--ifm-color-emphasis-600)', alignSelf: 'center' }}>
          {filtered.length} 个错误码
        </span>
      </div>

      {filtered.map((e, i) => (
        <div key={i} style={{ border: '1px solid var(--ifm-color-emphasis-200)', borderRadius: '8px', padding: '1rem', marginBottom: '0.8rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem', flexWrap: 'wrap' }}>
            <code style={{ fontWeight: 700, fontSize: '0.9rem', color: 'var(--ifm-color-danger)' }}>{e.code}</code>
            <span style={{ background: typeColor(e.type), color: 'white', padding: '1px 8px', borderRadius: '10px', fontSize: '0.7rem', fontWeight: 600 }}>
              {typeLabel(e.type)}
            </span>
            {e.fixVersion && <span style={{ fontSize: '0.75rem', color: 'var(--ifm-color-emphasis-500)' }}>修复版本: {e.fixVersion}</span>}
            {e.affectedGpu && <span style={{ fontSize: '0.75rem', color: 'var(--ifm-color-warning)' }}>影响: {e.affectedGpu.join(', ')}</span>}
          </div>
          <p style={{ margin: '0 0 0.3rem', fontWeight: 600, fontSize: '0.9rem' }}>{e.message}</p>
          <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr', gap: '0.3rem 0.8rem', fontSize: '0.82rem', marginTop: '0.5rem' }}>
            <span style={{ color: 'var(--ifm-color-emphasis-500)', fontWeight: 600 }}>原因:</span>
            <span>{e.cause}</span>
            <span style={{ color: 'var(--ifm-color-success)', fontWeight: 600 }}>解决:</span>
            <span>{e.workaround}</span>
          </div>
        </div>
      ))}
    </div>
  );
}
