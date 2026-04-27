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
    // {
    //   type: 'category', label: '📦 ROCm Core', items: [...],
    //   link: { type: 'generated-index', title: 'ROCm Core' },
    // },
    // {
    //   type: 'category', label: '💻 HIP Programming', items: [...],
    //   link: { type: 'generated-index', title: 'HIP 编程' },
    // },
    // {
    //   type: 'category', label: '🖥️ GPU Driver', items: [...],
    //   link: { type: 'generated-index', title: 'GPU 驱动' },
    // },
    // {
    //   type: 'category', label: '🧠 PyTorch on ROCm', items: [...],
    //   link: { type: 'generated-index', title: 'PyTorch ROCm' },
    // },
    // {
    //   type: 'category', label: '🔢 TensorFlow on ROCm', items: [...],
    //   link: { type: 'generated-index', title: 'TensorFlow ROCm' },
    // },
    // {
    //   type: 'category', label: '⚡ Performance', items: [...],
    //   link: { type: 'generated-index', title: '性能优化' },
    // },
    // {
    //   type: 'category', label: '🐛 Debugging', items: [...],
    //   link: { type: 'generated-index', title: '调试' },
    // },
    // {
    //   type: 'category', label: '📋 Compatibility', items: [...],
    //   link: { type: 'generated-index', title: '兼容性' },
    // },
    // {
    //   type: 'category', label: '📥 Installation', items: [...],
    //   link: { type: 'generated-index', title: '安装部署' },
    // },
    // {
    //   type: 'category', label: '📰 Release Notes', items: [...],
    //   link: { type: 'generated-index', title: '版本发布' },
    // },
    // {
    //   type: 'category', label: '🔄 CUDA → HIP 对照', items: [...],
    //   link: { type: 'generated-index', title: 'CUDA→HIP' },
    // },
    // {
    //   type: 'category', label: '📊 兼容性矩阵', items: [...],
    //   link: { type: 'generated-index', title: '兼容性矩阵' },
    // },
    // {
    //   type: 'category', label: '❗ 错误码库', items: [...],
    //   link: { type: 'generated-index', title: '错误码' },
    // },
  ],
};

export default sidebars;
