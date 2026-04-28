# Phase 11：图片缓存管道 🖼️

> **最后更新：** 2026-04-28  
> **状态：** 🔲 未开始  
> **依赖：** Phase 0-7（现有管道就绪）  
> **目标：** 杜绝远程图片断链，本地/ECS 部署通用

---

## 为什么需要这个 Phase

### 当前问题

1. **图片全部热链** — 68 篇 raw markdown 中 ~25 张非 base64 图片，引用指向 `rocm.docs.amd.com` 的相对路径
2. **断链风险** — AMD 文档重构、CDN 路径变更、原文下线都会导致图片 404
3. **离线不可用** — GitHub Pages 加载时，图片依赖 AMD 服务器可用性
4. **没有缓存** — `generate-docs.py` 只做路径原样保留，`fetch-official.py` 只抓 HTML→MD，不抓图片

### 示例（已确认的断链点）

```
![AMD ROCm software stack](_images/rocm-software-stack-7_2_1.png)
![Single GCD structure](../../_images/image001.png)
![Dual-GCD architecture](../../_images/image002.png)
![MNIST training graph](../_images/mnist-1.png)
```

### 影响范围

`grep` 确认：以下文章含远程图片引用

```
content/raw/english/rocm_*what-is-rocm*.md          (软件栈图)
content/raw/english/rocm_*gpu-arch_mi250*.md        (3 张架构图)
content/raw/english/rocm_*gpu-arch_mi100*.md        (3 张架构图)
content/raw/english/rocm_*compatibility-matrix*.md  (浮点类型图)
content/raw/english/rocm_*contributing*.md          (2 张 GitHub 截图)
content/raw/english/hipify_*hipify-clang*.md        (CSV 统计图)
content/raw/english/rocm_*ai-pytorch-inception*.md  (损失/精度图)
content/raw/english/rocm_*deep-learning-rocm*.md    (MNIST 5 张)
content/raw/english/rocm_*inference*.md             (vLLM 截图)
content/raw/english/rocm_*rocm-for-hpc*.md          (HPC 栈图)
```

---

## 覆盖率预估

| | 当前 (Phase 3/7) | Phase 8 (arXiv) | Phase 9 (多语言) | Phase 10 (二手) |
|---|---|---|---|---|
| **文章数** | 68 | ~50+ | ~100+ | ~50+ |
| **图片数（估）** | ~25 | ~200（论文图表） | ~300（截图/示意图） | ~500（商品图） |
| **总大小（估）** | ~5 MB | ~40 MB | ~60 MB | ~100 MB |
| **Repo 影响** | 可忽略 | 中等 | 需关注 | 接近 1GB 限制 |

> ⚠ **Phase 10 商品图片是最大增量。** 如果图片总量接近 500MB，建议考虑：
> 1. 单独 `assets` 分支 / 子模块
> 2. 图片压缩（WebP → 50-80% 体积减少）
> 3. 外部存储（Cloudflare R2 / 阿里云 OSS）

---

## 计划任务

### 11.1 `scripts/cache-images.py` — 图片缓存脚本

**职责：** 扫描 raw markdown → 解析图片 URL → 下载到本地 → 返回路径映射

```
输入：content/raw/english/*.md
输出：website/static/img/cached/<source>/<slug>/<hash>-<filename>
      data/image-cache.json  (映射表)
```

**功能要求：**

| 功能 | 说明 |
|------|------|
| URL 解析 | 支持 `![](_images/foo.png)` 相对路径 + `![](https://...)` 绝对路径 |
| 路径解析 | 使用各个 source 的 `base_url` 解析相对路径为绝对 URL |
| 去重 | SHA256 哈希前 8 位做文件名前缀，相同图片只存一份 |
| 压缩 | 对 png/jpg 用 Pillow 转 WebP（可配置质量），**保留原始格式副本** |
| 跳过 base64 | data:image URI 不处理（已是自包含） |
| 重试 | 3 次指数退避 |
| 增量模式 | 已缓存的不重新下载（除非 `--force`） |
| 映射输出 | `data/image-cache.json` — original_url → local_path 映射，给 generate-docs.py 消费 |

**命令签名：**

```bash
python3 scripts/cache-images.py              # 增量缓存
python3 scripts/cache-images.py --force       # 强制重新下载所有
python3 scripts/cache-images.py --dry-run     # 预览
```

### 11.2 `fetch-official.py` 集成 — 同步抓取

在 `process_source()` 末尾调用缓存步骤：

```python
# ── 图片缓存 ──
# 每抓取完一个 source 的页面后，缓存该页面的所有图片
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from cache_images import cache_article_images

cache_article_images(out_path, config["base_url"])
```

**位置：** 紧接在写入 `.md` 文件之后、sleep 之前（第 326 行后）

**注意：** 这个集成是可选的——`cache-images.py` 也可以独立运行（CI 中作为 sync 流水线的一个 step）。

### 11.3 `generate-docs.py` 路径重写

在 `generate_mdx()` 的正文清洗流程中，**在花括号转义之前**，加一个图片路径重写步骤：

```python
def rewrite_image_paths(body: str, image_cache: dict) -> str:
    """将 Markdown 图片引用从远程路径重写为本地缓存路径。"""
    def replace_ref(m):
        alt = m.group(1) or ""
        url = m.group(2)
        
        # 跳过 data: URI
        if url.startswith("data:"):
            return m.group(0)
        
        # 跳过已经是本地缓存的
        if url.startswith("/img/cached/"):
            return m.group(0)
        
        # 查映射表
        if url in image_cache:
            local = image_cache[url]
            return f"![{alt}]({local})"
        
        # 找不到的保留原样（让 CI 校验捕获）
        return m.group(0)
    
    # 匹配 ![alt](url) 和 ![alt](url){.class}
    return re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_ref, body)
```

**优先级逻辑：**

1. `data:image/...` → 保留（自包含）
2. `/img/cached/...` → 已经是本地缓存，保留
3. 映射表命中 → 重写为本地路径
4. 未命中 → **保留原样 + 记录 warning**（不阻塞构建，让 CI 告警）

> ⚠ **不匹配的图片不应报错阻塞构建**——少量远程图片是可接受的，CI 校验去告警就行。

### 11.4 目录结构约定

```
website/static/img/cached/
├── rocm/                          # ROCm 官方文档图片
│   ├── what-is-rocm/
│   │   └── a1b2c3d4-rocm-software-stack-7_2_1.png
│   ├── gpu-arch-mi250/
│   │   └── e5f6a7b8-image001.png
│   │   └── c9d0e1f2-image002.png
│   │   └── a3b4c5d6-image003.png
│   └── ...
├── hip/                           # HIP 文档图片
├── hipify/                        # HIPIFY 文档图片
├── rocm-install-linux/            # 安装文档图片
├── papers/                        # Phase 8: arXiv 论文图片
│   └── <arxiv-id>/
├── multilingual/                  # Phase 9: 多语言情报图片
│   └── <lang>/<source>/
└── prices/                        # Phase 10: 二手商品图片
    └── <country>/<platform>/
```

### 11.5 映射表格式 (`data/image-cache.json`)

```json
{
  "version": 1,
  "updated": "2026-04-28T10:00:00Z",
  "mappings": {
    "_images/rocm-software-stack-7_2_1.png": {
      "local": "/img/cached/rocm/what-is-rocm/a1b2c3d4-rocm-software-stack-7_2_1.png",
      "hash": "a1b2c3d4e5f6a7b8",
      "size_bytes": 245760,
      "downloaded_at": "2026-04-28T10:00:00Z",
      "source_url": "https://rocm.docs.amd.com/en/latest/_images/rocm-software-stack-7_2_1.png"
    }
  }
}
```

**关键设计：**
- `mappings` 的 key 是原始 markdown 中出现的路径（如 `_images/foo.png`）
- `local` 是 Docusaurus 可用的路径（`/img/cached/...`）
- `hash` 用于去重和变更检测
- `source_url` 是解析后的绝对 URL，用于增量更新时比对

### 11.6 CI 集成 — 图片校验

在 `validate.yml` 中新增两个 step：

| Step | 说明 |
|------|------|
| `check-broken-images` | 扫描所有 MDX 中的 `![]()` 引用，逐条 HEAD 请求验证 |
| `check-cached-images-exist` | 验证 `image-cache.json` 中的所有 `local` 路径指向的文件真实存在 |

**配置：**

```yaml
# validate.yml 新增
- name: Check cached image files exist
  run: |
    python3 scripts/validate-images.py
    
- name: Check remote images reachable (exclude cached)
  run: |
    python3 scripts/validate-images.py --check-remote
```

### 11.7 ECS 部署适配

**无需额外处理。** 图片缓存在 `website/static/img/cached/` 下：

| 部署方式 | 图片如何工作 |
|----------|-------------|
| **GitHub Pages** | Docusaurus 构建时 `static/` → `build/` → 自动部署，图片走 GH CDN |
| **ECS (Docker)** | `docker build` 时 `COPY website/static/ .` → nginx 直接 serve |
| **ECS + CDN** | 阿里云 CDN 回源到 ECS，图片路径为 `/img/cached/...`，无需改代码 |
| **OSS 外挂（可选）** | `baseUrl: 'https://cdn.example.com'` 配置到 `docusaurus.config.ts` |

**对比分析：**

| 方案 | 优点 | 缺点 |
|------|------|------|
| **A. Repo 内嵌**（推荐） | 零运维，GH Pages 自动部署 | 接近 1GB 上限时需拆 repo |
| **B. OSS/CDN 外挂** | 无限容量 | 需付费，增加运维复杂度，本地预览需额外配置 |
| **C. 独立 assets 分支** | 主 repo 干净 | git clone 时需 `--recurse-submodules` |

> **建议：先走 A 方案。** 估算 68 篇文章图片 ~5MB，加上 Phase 8-10 总计 < 200MB，GitHub 1GB 限制够用。未来超过 500MB 时再迁移到 B。

### 11.8 后续 Phase 适配清单

| Phase | 需做的 | 改动点 |
|-------|--------|--------|
| **Phase 8** (arXiv 论文) | `fetch-papers.py` 下载论文后，pyMuPDF 提取图片，调用 `cache-images.py` | scripts/fetch-papers.py |
| **Phase 9** (多语言) | 抓取非英语文章时同步下载文中图片 | scripts/fetch-multilingual.py |
| **Phase 10** (二手价格) | 商品图下载 + WebP 压缩 + 水印避免版权问题 | scripts/fetch-prices.py |

---

## 预估工作量

| # | 任务 | 预估 | 复杂度 |
|---|------|------|--------|
| 11.1 | `cache-images.py` 脚本 | 2h | 中 |
| 11.2 | `fetch-official.py` 集成 | 15min | 低 |
| 11.3 | `generate-docs.py` 路径重写 | 1h | 中 |
| 11.4 | 目录结构创建 | 已包含在 11.1 | - |
| 11.5 | 映射表格式 | 已包含在 11.1 | - |
| 11.6 | CI 校验集成 | 30min | 低 |
| 11.7 | ECS 适配 | 0（无需改） | - |
| 11.8 | 后续 Phase 适配 | 后续各自评估 | - |
| **总计** | | **~4h** | |

---

## 其他建议

### 1. 图片格式压缩策略

```
原始格式 → WebP (quality=85) + 保留原格式
```

- **WebP 体积减少 50-80%，** Docusaurus/现代浏览器全部支持
- **保留原始 PNG/SVG** 用于特殊场景（透明背景、矢量图）
- 工具：Pillow + `pillow-heif`（WebP 支持）

### 2. 占位图组件

创建 `CachedImage` 组件替代原生 `<img>`：

```tsx
// website/src/components/CachedImage.tsx
function CachedImage({ src, alt, ...props }) {
  // 图片加载失败时显示占位符 + 文字说明
}
```

好处：
- 优雅降级（broken image → 灰色占位符）
- 可在占位符上显示"原图地址"
- 统一处理 `srcSet`（响应式图片）

### 3. 缓存清理

```bash
python3 scripts/cache-images.py --clean-orphans
# 删除 image-cache.json 中没有映射但存在于磁盘的孤立文件
```

CI 每周执行一次。

### 4. Git LFS 备选

如果图片总量超过 500MB，考虑：

```bash
git lfs track "website/static/img/cached/**"
```

但 GitHub LFS 免费带宽只有 1GB/月，使用时需评估。

---

> **下一步：** 将此 Phase 加入 `docs/PROGRESS.md`，排在 Phase 8 之前（因为它给所有后续 Phase 提供基础设施）。
