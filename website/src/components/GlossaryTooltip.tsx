import React, { useState, useEffect } from 'react';

// 内嵌术语表（构建时从 glossary/rocm-terms.yaml 预编译）
// 格式：{ "ROCm": { zh: "ROCm（Radeon 开放计算平台）", context: "..." }, ... }
const GLOSSARY: Record<string, { zh: string; context: string }> = {
  ROCm: {
    zh: 'ROCm（Radeon 开放计算平台）',
    context: "AMD 的开源 GPU 计算软件栈，对标 NVIDIA CUDA 生态",
  },
  HIP: {
    zh: 'HIP（异构接口可移植性）',
    context: "AMD 的 CUDA 兼容编程接口，允许同一份代码在 AMD 和 NVIDIA GPU 上运行",
  },
  CUDA: {
    zh: 'CUDA（统一计算设备架构）',
    context: "NVIDIA 的并行计算平台和编程模型",
  },
  CDNA: {
    zh: 'CDNA（计算 DNA 架构）',
    context: "AMD 数据中心 GPU 架构系列",
  },
  RDNA: {
    zh: 'RDNA（Radeon DNA 架构）',
    context: "AMD 消费级/游戏 GPU 架构系列",
  },
  Instinct: {
    zh: 'Instinct（AMD 数据中心 GPU 系列）',
    context: "AMD 面向 HPC/AI 的 GPU 产品线（MI50/MI100/MI210/MI250/MI300X）",
  },
  Wavefront: {
    zh: '波前 (Wavefront)',
    context: "AMD GPU 调度基本单元（通常 64 个线程），等同于 NVIDIA 的 Warp（32 线程）",
  },
  Kernel: {
    zh: '内核函数 (Kernel)',
    context: "在 GPU 上并行执行的函数，对应 CUDA 中的 __global__ 函数",
  },
  MIOpen: {
    zh: 'MIOpen（AMD 深度学习基元库）',
    context: "AMD 的深度学习算子库，对标 NVIDIA cuDNN",
  },
  rocBLAS: {
    zh: 'rocBLAS（ROCm 基础线性代数库）',
    context: "BLAS 接口的 ROCm 实现，对标 NVIDIA cuBLAS",
  },
  RCCL: {
    zh: 'RCCL（ROCm 集合通信库）',
    context: "多 GPU 集合通信库，对标 NVIDIA NCCL",
  },
  HIPIFY: {
    zh: 'HIPIFY（CUDA→HIP 自动转换工具）',
    context: "将 CUDA 代码自动转换为 HIP 代码的命令行工具",
  },
  HSA: {
    zh: 'HSA（异构系统架构）',
    context: "AMD 主导的异构计算标准，ROCm 的底层运行时基础",
  },
  amdgpu: {
    zh: 'amdgpu（AMD GPU 内核驱动）',
    context: "Linux 内核中 AMD GPU 的开源驱动模块",
  },
  WMMA: {
    zh: 'WMMA（波前矩阵乘加）',
    context: "AMD GPU 的矩阵运算硬件指令，对标 NVIDIA Tensor Core",
  },
  'Compute Unit': {
    zh: '计算单元 (CU)',
    context: "GPU 的基本计算核心组，包含多个 SIMD 单元",
  },
  Occupancy: {
    zh: '占用率 (Occupancy)',
    context: "GPU 上活跃 Wavefront 与理论最大值的比率",
  },
  'Infinity Fabric': {
    zh: 'Infinity Fabric（AMD 高速互联总线）',
    context: "AMD 芯片互联技术，多 GPU 间高带宽通信",
  },
};

interface GlossaryTooltipProps {
  /** 要查找的术语 */
  term: string;
  /** 可选：直接显示（用于正文内联） */
  children?: React.ReactNode;
}

export default function GlossaryTooltip({ term, children }: GlossaryTooltipProps) {
  const entry = GLOSSARY[term];

  if (!entry) {
    return <>{children || term}</>;
  }

  return (
    <span
      className="glossary-tooltip"
      data-tooltip={entry.context}
      style={{
        borderBottom: '1px dashed var(--ifm-color-primary)',
        cursor: 'help',
        position: 'relative',
      }}
      title={entry.context}
    >
      {children || entry.zh}
    </span>
  );
}

// 导出术语搜索函数（供其他组件使用）
export function searchGlossary(query: string): Array<{ term: string; zh: string; context: string }> {
  const lowerQuery = query.toLowerCase();
  return Object.entries(GLOSSARY)
    .filter(([term, info]) =>
      term.toLowerCase().includes(lowerQuery) ||
      info.zh.toLowerCase().includes(lowerQuery) ||
      info.context.toLowerCase().includes(lowerQuery)
    )
    .map(([term, info]) => ({ term, ...info }));
}

export { GLOSSARY };
