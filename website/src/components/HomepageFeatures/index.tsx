import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  icon: string;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: '🔄 中英对照',
    icon: '📖',
    description: (
      <>
        左右分栏或逐段对照两种阅读模式，英文原文 + 中文翻译同步呈现，
        消弭语言障碍，确保技术准确性。
      </>
    ),
  },
  {
    title: '📋 官方一手情报',
    icon: '🏛️',
    description: (
      <>
        只收录 <code>rocm.docs.amd.com</code> 官方文档，不转载二手内容。
        每篇文章标注版本号和原文链接，可追溯可验证。
      </>
    ),
  },
  {
    title: '🏷️ 多维分类',
    icon: '🔍',
    description: (
      <>
        按 ROCm 版本、操作系统（Linux/Windows）、GPU 架构（CDNA/RDNA）、
        应用领域（AI/HPC）、难度等级等多维度标签筛选。
      </>
    ),
  },
];

function Feature({title, icon, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center" style={{fontSize: '3rem', padding: '1rem'}}>
        {icon}
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
