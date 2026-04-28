import React from 'react';
import styles from './styles.module.css';

interface ParallelViewProps {
  enContent: string;
  zhContent: string;
}

export default function ParallelView({ enContent, zhContent }: ParallelViewProps) {
  return (
    <div className={styles.parallel}>
      <div className={styles.column}>
        <div className={styles.columnHeader}>
          <span role="img" aria-label="English">🇺🇸</span> English (Original)
        </div>
        <div
          className={styles.content}
          dangerouslySetInnerHTML={{ __html: enContent }}
        />
      </div>
      <div className={styles.column}>
        <div className={styles.columnHeader}>
          <span role="img" aria-label="Chinese">🇨🇳</span> 中文翻译
        </div>
        <div
          className={styles.content}
          dangerouslySetInnerHTML={{ __html: zhContent }}
        />
      </div>
    </div>
  );
}
