import React, {type ReactNode} from 'react';
import { useDoc } from '@docusaurus/plugin-content-docs/client';
import ArticleMeta, {type ArticleMetaProps} from './ArticleMeta';

/**
 * 文章头部元信息组件。
 * 在每篇文档的 MDX 中通过 `<ArticleHeader />` 使用，
 * 自动读取 frontmatter 并渲染 ArticleMeta。
 */
type ArticleHeaderFrontMatter = Partial<ArticleMetaProps> & {
  source_type?: ArticleMetaProps['source_type'];
};

export default function ArticleHeader(): ReactNode {
  const { metadata, frontMatter } = useDoc();
  const fm = frontMatter as ArticleHeaderFrontMatter;

  // Only render if v2 frontmatter is present (has credibility field)
  if (typeof fm.credibility !== 'number') {
    return null;
  }

  return (
    <ArticleMeta
      source_url={fm.source_url || ''}
      source_type={fm.source_type || 'official'}
      source_org={fm.source_org || 'unknown'}
      published_date={fm.published_date}
      synced_date={fm.synced_date}
      credibility={fm.credibility || 3}
      lifecycle={fm.lifecycle || 'latest'}
      version={fm.version}
      rocm_versions={fm.rocm_versions}
      tags={fm.tags || metadata.tags?.map((t: any) => t.label)}
      os={fm.os}
      gpu={fm.gpu}
      gpu_arch={fm.gpu_arch}
      driver={fm.driver}
      frameworks={fm.frameworks}
      difficulty={fm.difficulty}
    />
  );
}
