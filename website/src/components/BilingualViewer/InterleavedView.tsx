import React from 'react';
import styles from './styles.module.css';

interface InterleavedViewProps {
  enContent: string;
  zhContent: string;
}

export default function InterleavedView({ enContent, zhContent }: InterleavedViewProps) {
  // 按 <p> 标签分段
  const enParagraphs = enContent
    .split(/<\/p>\s*<p>/i)
    .filter((s) => s.trim());
  const zhParagraphs = zhContent
    .split(/<\/p>\s*<p>/i)
    .filter((s) => s.trim());

  const maxLen = Math.max(enParagraphs.length, zhParagraphs.length);

  return (
    <div className={styles.interleaved}>
      {Array.from({ length: maxLen }, (_, i) => (
        <div key={i} className={styles.pair}>
          {enParagraphs[i] && (
            <div className={styles.enBlock}>
              <div
                className={styles.content}
                dangerouslySetInnerHTML={{
                  __html: enParagraphs[i] + (enParagraphs[i].endsWith('</p>') ? '' : '</p>'),
                }}
              />
            </div>
          )}
          {zhParagraphs[i] && (
            <div className={styles.zhBlock}>
              <div
                className={styles.content}
                dangerouslySetInnerHTML={{
                  __html: zhParagraphs[i] + (zhParagraphs[i].endsWith('</p>') ? '' : '</p>'),
                }}
              />
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
