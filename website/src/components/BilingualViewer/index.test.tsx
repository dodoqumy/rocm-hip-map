import React from 'react';
import {describe, expect, it} from 'vitest';
import {fireEvent, render, screen} from '@testing-library/react';
import BilingualViewer from './index';

describe('BilingualViewer', () => {
  it('renders parallel mode by default and toggles to interleaved mode', () => {
    render(
      <BilingualViewer
        enContent="<p>English paragraph one.</p><p>English paragraph two.</p>"
        zhContent="<p>中文段落一。</p><p>中文段落二。</p>"
        sourceUrl="https://example.com/source"
      />,
    );

    expect(screen.getByText('English (Original)')).toBeInTheDocument();
    expect(screen.getByText('中文翻译')).toBeInTheDocument();
    expect(screen.getByRole('link', {name: '📎 原文'})).toHaveAttribute('href', 'https://example.com/source');

    fireEvent.click(screen.getByRole('button', {name: '⬍ 逐段对照'}));

    expect(screen.getByText('English paragraph one.')).toBeInTheDocument();
    expect(screen.getByText('中文段落一。')).toBeInTheDocument();
  });

  it('falls back to original-only mode when translation is missing', () => {
    render(<BilingualViewer enContent="<p>English only.</p>" />);

    expect(screen.getByRole('button', {name: '📖 仅原文'})).toBeDisabled();
    expect(screen.getByText('English only.')).toBeInTheDocument();
  });
});
