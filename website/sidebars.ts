import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docs: [
    {
      type: 'category',
      label: '🚀 入门指南',
      collapsible: true,
      collapsed: false,
      link: { type: 'doc', id: 'getting-started/index' },
      items: [
        'getting-started/what-is-rocm',
      ],
    },
  ],
};

export default sidebars;
