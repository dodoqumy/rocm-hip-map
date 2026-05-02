import React from 'react';
import {describe, expect, it, vi} from 'vitest';
import {render, screen} from '@testing-library/react';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import ArticleHeader from './ArticleHeader';

vi.mock('@docusaurus/plugin-content-docs/client', () => ({
  useDoc: vi.fn(),
}));

vi.mock('./ArticleMeta', () => ({
  __esModule: true,
  default: (props: Record<string, unknown>) => (
    <pre data-testid="article-meta">{JSON.stringify(props)}</pre>
  ),
}));

const mockedUseDoc = vi.mocked(useDoc);

describe('ArticleHeader', () => {
  it('returns null when credibility is absent', () => {
    mockedUseDoc.mockReturnValue({
      metadata: {source: 'https://fallback.example', tags: []},
      frontMatter: {},
    } as never);

    const {container} = render(<ArticleHeader />);

    expect(container).toBeEmptyDOMElement();
  });

  it('maps frontmatter into ArticleMeta props with defaults', () => {
    mockedUseDoc.mockReturnValue({
      metadata: {
        source: 'https://fallback.example',
        tags: [{label: 'tag-a'}, {label: 'tag-b'}],
      },
      frontMatter: {
        source_type: 'tool',
        credibility: 4,
        published_date: '2026-05-01',
      },
    } as never);

    render(<ArticleHeader />);

    const meta = JSON.parse(screen.getByTestId('article-meta').textContent || '{}');
    expect(meta.source_url).toBe('');
    expect(meta.source_type).toBe('tool');
    expect(meta.source_org).toBe('unknown');
    expect(meta.credibility).toBe(4);
    expect(meta.lifecycle).toBe('latest');
    expect(meta.tags).toEqual(['tag-a', 'tag-b']);
  });
});
