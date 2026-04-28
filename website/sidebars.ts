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
    {
      type: 'category',
      label: '📦 ROCm 核心文档',
      collapsible: true,
      collapsed: false,
      link: {
        type: 'generated-index',
        title: 'ROCm 官方文档（自动同步）',
        description: '从 rocm.docs.amd.com 每日自动抓取并翻译。共 68 篇文章，来源：AMD 官方文档。',
        slug: '/rocm-core',
      },
      items: [],
    },
    {
      type: 'category',
      label: '💻 HIP 编程',
      collapsible: true,
      collapsed: true,
      link: {
        type: 'generated-index',
        title: 'HIP 编程文档',
        slug: '/hip',
      },
      items: [],
    },
    {
      type: 'category',
      label: '📥 安装指南',
      collapsible: true,
      collapsed: true,
      link: {
        type: 'generated-index',
        title: '安装指南',
        slug: '/install',
      },
      items: [],
    },
    {
      type: 'category',
      label: '🔄 HIPIFY 迁移工具',
      collapsible: true,
      collapsed: true,
      link: {
        type: 'generated-index',
        title: 'HIPIFY 迁移工具',
        slug: '/hipify',
      },
      items: [],
    },
    {
      type: 'category',
      label: '📋 兼容性矩阵',
      collapsible: true,
      collapsed: true,
      link: { type: 'doc', id: 'compatibility/overview' },
      items: [],
    },
    {
      type: 'category',
      label: '🔄 CUDA → HIP',
      collapsible: true,
      collapsed: true,
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
