import React, {type ReactNode} from 'react';
import {PageMetadata} from '@docusaurus/theme-common';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import Head from '@docusaurus/Head';

/**
 * 自定义 Metadata 组件，为每篇文章注入 SEO 元数据：
 *   - canonical URL（指向 AMD 官方原文）
 *   - Open Graph 标签（og:title / og:description / og:type）
 *   - 搜索引擎索引控制
 */
export default function DocItemMetadata(): ReactNode {
  const {metadata, frontMatter, assets} = useDoc();

  const fm = frontMatter as any;
  const sourceUrl = fm.source_url as string | undefined;
  const sourceOrg = fm.source_org as string | undefined;
  const sourceType = fm.source_type as string | undefined;
  const credibility = fm.credibility as number | undefined;
  const lifecycle = fm.lifecycle as string | undefined;
  const rocmVersions = fm.rocm_versions as string[] | undefined;
  const tags = fm.tags as string[] | undefined;
  const keywords = fm.keywords as string[] | undefined;

  // 可信度低于 3 的文章不索引
  const noIndex = credibility !== undefined && credibility < 3;

  // 构建 og:description（带可信度标记）
  const ogDescription = metadata.description
    ? `${metadata.description} | 可信度: ${'★'.repeat(credibility ?? 5)} | 来源: ${sourceOrg ?? 'AMD'}`
    : metadata.description;

  return (
    <>
      <PageMetadata
        title={metadata.title}
        description={ogDescription}
        keywords={keywords}
        image={assets.image ?? frontMatter.image}
      />

      {/* canonical URL → 指向 AMD 官方原文，搜索引擎权重归因到一手来源 */}
      {sourceUrl && (
        <Head>
          <link rel="canonical" href={sourceUrl} />
        </Head>
      )}

      {/* Open Graph 扩展 */}
      <Head>
        <meta property="og:type" content="article" />
        {sourceOrg && <meta property="og:site_name" content={sourceOrg.toUpperCase()} />}
        <meta property="og:locale" content="zh_CN" />
        {rocmVersions && rocmVersions.length > 0 && (
          <meta property="article:tag" content={`ROCm ${rocmVersions.join(', ')}`} />
        )}
        {tags && tags.map((tag) => (
          <meta key={`tag-${tag}`} property="article:tag" content={tag} />
        ))}
        {sourceUrl && <meta property="article:original_source" content={sourceUrl} />}
      </Head>

      {/* 索引控制 */}
      <Head>
        {noIndex ? (
          <meta name="robots" content="noindex, nofollow" />
        ) : (
          <meta name="robots" content="index, follow, max-image-preview:large" />
        )}
        {lifecycle === 'outdated' && (
          <meta name="robots" content="noindex, follow" />
        )}
      </Head>
    </>
  );
}
