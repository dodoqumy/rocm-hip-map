import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: '🚀 入门指南',
      collapsible: true,
      collapsed: false,
      link: { type: 'doc', id: 'getting-started/index' },
      items: ['getting-started/what-is-rocm'],
    },
    // Phase 2+: 逐批添加文档后启用以下分类
    {
      type: 'category',
      label: '📋 兼容性矩阵',
      collapsible: true,
      collapsed: false,
      link: { type: 'doc', id: 'compatibility/overview' },
      items: [],
    },
    {
      type: 'category',
      label: '🔄 CUDA → HIP',
      collapsible: true,
      collapsed: false,
      link: { type: 'doc', id: 'cuda-to-hip/api-map' },
      items: [],
    },
    {
      type: 'category',
      label: '❗ 错误码库',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'errors/index' },
      items: [],
    },
    {
      type: 'category',
      label: '📡 Issue 情报',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'issues/index' },
      items: [],
    },
  ],
};

export default sidebars;
