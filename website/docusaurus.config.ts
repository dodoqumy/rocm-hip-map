import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'ROCm 中外文对照文档',
  tagline: 'ROCm 官方技术文档 · 中英对照阅读 · 一手情报',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // 部署 URL — 创建 GitHub 仓库后更新
  url: 'https://dodoqumy.github.io',
  baseUrl: '/rocm-hip-map/',

  organizationName: 'dodoqumy',
  projectName: 'rocm-hip-map',

  onBrokenLinks: 'warn',

  // i18n 中英双语配置
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
    localeConfigs: {
      en: {
        htmlLang: 'en-US',
        label: 'English',
      },
      'zh-Hans': {
        htmlLang: 'zh-Hans',
        label: '简体中文',
      },
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/dodoqumy/rocm-hip-map/edit/main/website/',
          // 版本管理：当前版本映射到 /docs/
          lastVersion: 'current',
          versions: {
            current: {
              label: '7.2.2',
              banner: 'none',
            },
          },
          onlyIncludeVersions: ['current'],
        },
        blog: false, // Phase 2 启用
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'dark',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'ROCm Docs',
      logo: {
        alt: 'ROCm Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docs',
          position: 'left',
          label: '文档',
        },
        {
          href: 'https://rocm.docs.amd.com/en/latest/',
          label: '官方文档',
          position: 'right',
        },
        {
          href: 'https://github.com/ROCm/ROCm',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'localeDropdown',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '文档',
          items: [
            {
              label: '入门指南',
              to: '/docs/getting-started',
            },
            {
              label: 'ROCm 官方文档',
              href: 'https://rocm.docs.amd.com/en/latest/',
            },
          ],
        },
        {
          title: '社区',
          items: [
            {
              label: 'AMD ROCm GitHub',
              href: 'https://github.com/ROCm',
            },
            {
              label: 'ROCm Community',
              href: 'https://github.com/ROCm/ROCm/discussions',
            },
          ],
        },
        {
          title: '更多',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/dodoqumy/rocm-hip-map',
            },
          ],
        },
      ],
      copyright: `本站内容源自 <a href="https://rocm.docs.amd.com">AMD ROCm 官方文档</a>，仅作中英对照阅读之用。Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
