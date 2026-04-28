# rocm-hip-map 

> 定位：  
> 建设一个 **ROCm + HIP 一手情报中外文对照阅读网站**  
> 面向开发者、工程师、研究者。  
> 核心价值：官方优先、原文可追溯、双语对照、结构化检索。

---

# 一、项目目标

建立一个网站，解决以下问题：

当前 ROCm / HIP 资料存在：

- 官方文档英文为主
- 中文资料大量转载、失真、过时
- ROCm 版本变化快，兼容性混乱
- GPU / 驱动 / OS / 框架信息分散
- 开发者无法快速判断某文章适合自己环境

---

# 二、本站核心原则（必须写入 README）

## 内容原则

1. 只收录一手情报
2. 官方来源优先
3. 所有文章保留原文链接
4. 每篇文章标注发布时间 / 来源 / 版本
5. 提供中英双语阅读
6. 翻译内容与原文分离
7. 不收录搬运二手文章

---

## 一手来源定义

### 国外一手

- AMD ROCm Official Docs
- AMD Blog
- ROCm GitHub org
- PyTorch official ROCm docs
- TensorFlow official ROCm docs
- JAX official docs
- Linux kernel / Mesa / LLVM 官方资料
- GitHub Issues / PR / Discussions
- 学术论文原文

### 中文一手（允许）

- AMD 中国官方发布
- 官方中文镜像文档
- 中国高校原始论文
- 国产框架官方文档（如 PaddlePaddle）
- 国内芯片厂商官方适配文档
- 官方会议 PPT / 白皮书

---

# 三、双语规则

## 若原文为英文：

展示：

- 英文原文
- 中文对照翻译

## 若原文为中文：

展示：

- 中文原文
- 英文翻译

## 图片文字翻译

文档中的截图/示意图含有英文文字时：

1. **OCR 提取** — 识别图片中所有文字区域
2. **翻译** — 逐段翻译为中文
3. **重生成** — 将翻译后的文字覆写到原图对应位置（保持原字体/颜色/背景风格），输出为新的对照图片
4. **展示** — 原文图片与译文图片并排展示（类似文本左右对照模式）

技术路线：OCR (Tesseract/PaddleOCR) → 翻译 (术语表约束) → 图像编辑 (PIL/OpenCV inpainting + 文字覆写) 或 AI 图片重绘。

---

# 四、网站功能规划

## 1. 文档阅读功能（核心）

每篇文章页包含：

- 标题
- 来源网站
- 原文链接
- 发布时间
- 更新时间
- 原文语言
- 双语切换
- 中英对照模式（左右分栏）
- 标签系统

---

## 2. 分类系统（非常重要）

### 按主题分类

- ROCm Core
- HIP Programming
- GPU Driver
- PyTorch ROCm
- TensorFlow ROCm
- Performance
- Debugging
- Compatibility
- Installation
- Release Notes
- Hardware Support

### 按环境分类

- Ubuntu 20.04
- Ubuntu 22.04
- RHEL
- Arch
- WSL2
- Docker
- Kubernetes

### 按 GPU 分类

- MI50
- MI100
- MI210
- MI300X
- RX 6800
- RX 7900
- APU

### 按 ROCm 版本分类

- ROCm 5.x
- ROCm 6.0
- ROCm 6.1
- ROCm 6.2
- ROCm 6.3+

### 按驱动版本分类

- amdgpu 5.x
- amdgpu 6.x

---

## 3. 搜索功能

支持搜索：

- API 名称
- GPU 型号
- ROCm 版本
- 错误代码
- 驱动版本
- 原文标题

---

## 4. 兼容性矩阵（强烈建议）

例如：

| GPU | ROCm 6.1 | Ubuntu 22.04 | PyTorch 2.4 |
|-----|----------|-------------|------------|
| MI210 | ✅ | ✅ | ✅ |
| RX580 | ⚠️ | ⚠️ | ❌ |

---

## 5. Issue 情报系统（高价值）

同步 GitHub Issues：

- 已知 bug
- workaround
- fix version
- 影响硬件

---

## 6. Release Watch（建议）

自动追踪：

- ROCm 新版本
- HIP API 更新
- PyTorch ROCm 新版
- LLVM backend 更新

---

# 五、建议新增功能（你没提但非常重要）

## 1. 阅读可信度评级

每篇内容显示：

- 官方文档（★★★★★）
- 官方仓库 Issue（★★★★）
- 官方博客（★★★★）
- 社区讨论（★★★）
- 实验性质内容（★★）

---

## 2. 生命周期状态

标注：

- 最新推荐
- 已过时
- 即将废弃
- 已弃用

---

## 3. CUDA → HIP 对照数据库

例如：

| CUDA | HIP |
|------|-----|
| cudaMalloc | hipMalloc |

---

## 4. 常见错误码库

例如：

- hipErrorNoBinaryForGpu
- HSA_STATUS_ERROR

---

## 5. 收藏 / 阅读历史（后期）

---

# 六、技术栈建议

## 前端

- VitePress（首选）
- 或 Docusaurus

原因：

- Markdown 原生支持
- 搜索方便
- SEO 好
- 部署简单

## 数据层

- markdown + yaml frontmatter
- json metadata

## 部署

- GitHub Pages
- Cloudflare Pages

---

# 七、GitHub 仓库初始化结构（新版）

```text
rocm-hip-map/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── sources.md
├── roadmap.md
│
├── docs/
│   ├── index.md
│   │
│   ├── articles/
│   │   ├── official/
│   │   │   ├── amd/
│   │   │   ├── rocm/
│   │   │   ├── pytorch/
│   │   │   └── paddle/
│   │   │
│   │   ├── github/
│   │   │   ├── issues/
│   │   │   └── prs/
│   │   │
│   │   └── papers/
│   │
│   ├── bilingual/
│   │   ├── en-zh/
│   │   └── zh-en/
│   │
│   ├── compatibility/
│   │   ├── gpu.md
│   │   ├── os.md
│   │   ├── frameworks.md
│   │   └── drivers.md
│   │
│   ├── versions/
│   │   ├── rocm-5.x.md
│   │   ├── rocm-6.0.md
│   │   └── rocm-6.x.md
│   │
│   ├── cuda-to-hip/
│   │   ├── api-map.md
│   │   ├── hipify.md
│   │   └── migration.md
│   │
│   ├── errors/
│   │   ├── runtime.md
│   │   ├── install.md
│   │   └── compile.md
│   │
│   └── tags/
│
├── content/
│   ├── raw/
│   │   ├── english/
│   │   └── chinese/
│   │
│   └── translated/
│       ├── zh/
│       └── en/
│
├── data/
│   ├── articles.json
│   ├── versions.json
│   ├── gpu.json
│   ├── drivers.json
│   ├── issues.json
│   └── tags.json
│
├── scripts/
│   ├── fetch-official.py
│   ├── sync-github.py
│   ├── classify.py
│   ├── build-index.py
│   └── validate-links.py
│
├── website/
│   └── vitepress/
│       ├── config.mts
│       ├── sidebar.ts
│       └── theme/
│
└── .github/
    └── workflows/
        ├── build.yml
        ├── sync.yml
        └── validate.yml