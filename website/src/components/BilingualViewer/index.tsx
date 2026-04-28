import React, { useState, useMemo } from 'react';
import ParallelView from './ParallelView';
import InterleavedView from './InterleavedView';
import styles from './styles.module.css';

type ViewMode = 'parallel' | 'interleaved';

interface BilingualViewerProps {
  /** 英文原文（已在 Docusaurus 构建时渲染为 HTML 的 React children） */
  enContent?: string;
  /** 中文翻译 HTML */
  zhContent?: string;
  /** 原文链接 */
  sourceUrl?: string;
  /** 是否显示标题行 */
  showHeader?: boolean;
}

export default function BilingualViewer({
  enContent,
  zhContent,
  sourceUrl,
  showHeader = true,
}: BilingualViewerProps) {
  const [viewMode, setViewMode] = useState<ViewMode>('parallel');

  // 如果没有中文翻译，只显示英文（降级处理）
  const hasTranslation = zhContent && zhContent.trim().length > 0;

  // 提取纯文本标题用于对比
  const enTitle = useMemo(() => {
    if (!enContent) return '';
    const match = enContent.match(/<h1[^>]*>(.*?)<\/h1>/i);
    return match ? match[1].replace(/<[^>]+>/g, '') : '';
  }, [enContent]);

  if (!enContent) {
    return null;
  }

  return (
    <div className={styles.container}>
      {/* 工具栏 */}
      <div className={styles.toolbar}>
        <div className={styles.modeToggle}>
          <button
            className={viewMode === 'parallel' ? styles.active : ''}
            onClick={() => setViewMode('parallel')}
            title="左右分栏对照"
          >
            ⬌ 左右对照
          </button>
          <button
            className={viewMode === 'interleaved' ? styles.active : ''}
            onClick={() => setViewMode('interleaved')}
            title="逐段交替对照"
          >
            ⬍ 逐段对照
          </button>
          {!hasTranslation && (
            <button className={styles.active} disabled>
              📖 仅原文
            </button>
          )}
        </div>

        {sourceUrl && (
          <a
            href={sourceUrl}
            target="_blank"
            rel="noopener noreferrer"
            className={styles.sourceLink}
          >
            📎 原文
          </a>
        )}
      </div>

      {/* 对照内容区 */}
      {!hasTranslation ? (
        <div className={styles.singleColumn}>
          <div
            className={styles.content}
            dangerouslySetInnerHTML={{ __html: enContent }}
          />
        </div>
      ) : viewMode === 'parallel' ? (
        <ParallelView enContent={enContent} zhContent={zhContent!} />
      ) : (
        <InterleavedView enContent={enContent} zhContent={zhContent!} />
      )}
    </div>
  );
}
