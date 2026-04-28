# 🔧 用户操作手顺

> **定位：** 记录所有需要用户（JINYU LI）手动操作的环节。  
> **原则：** 每个操作 = 背景说明 + 前置条件 + 分步手顺 + 验证方法。  
> **最后更新：** 2026-04-28

---

## 操作索引

| # | 操作 | Phase | 状态 | 优先级 |
|---|------|-------|------|--------|
| OP-1 | 获取 opencode-go API Key | Phase 4 | ✅ 完成 | P0 |
| OP-2 | 创建 GitHub Actions `sync.yml` 定时工作流 | Phase 6 | ✅ 完成 | P1 |
| OP-3 | 创建 GitHub Actions `validate.yml` 校验工作流 | Phase 6 | ✅ 完成 | P1 |
| OP-4 | 配置 GitHub Secrets（翻译 API Key） | Phase 4+6 | ✅ 完成 | P0 |
| OP-5 | Algolia DocSearch 申请（搜索功能） | Phase 7.6 | ⏳ 远期 | P3 |
| OP-6 | 网站分析接入（Umami/GA） | Phase 7.8 | ⏳ 远期 | P3 |

---

## OP-1：获取 opencode-go API Key

### 背景

翻译管道（`scripts/translate.py`）已实现 opencode-go 后端支持。  
opencode-go 是你当前使用的 DeepSeek 代理，相对免费，无需额外付费。

脚本已配置默认值：  
```
TRANSLATE_PROVIDER = opencode
TRANSLATE_MODEL     = deepseek-v4-pro
TRANSLATE_BASE_URL  = https://opencode.ai/zen/go/v1
```

只需要提供 `TRANSLATE_API_KEY`。

### 前置条件

- opencode-go 账号（应该已有，因为 Hermes 正在用它）

### 操作手顺

1. **获取 API Key**
   - 打开 opencode.ai 控制台或设置页面
   - 找到 API Keys 管理
   - 复制你的 API Key（格式一般是 `sk-...` 或类似）

2. **本地测试验证**（可选，确认可用）
   ```bash
   cd ~/projects/hermes/rocm-hip-map
   TRANSLATE_PROVIDER=opencode \
   TRANSLATE_API_KEY="你的key" \
   python3 scripts/translate.py --dry-run
   ```
   期望输出：`🌐 rocm-hip-map translate.py` + `Provider: opencode`

3. **将 Key 告诉我**（通过 Telegram）
   - 我会写入 GitHub Secrets，脚本在 CI 中就能自动翻译
   - 或者如果你不想直接给 key，按 OP-4 自己配置 GitHub Secret 也行

### 验证标准

- 本地 `--dry-run` 不报认证错误
- 实际翻译 `--file <某篇英文原文>` 能产出中文 Markdown

---

## OP-2：GitHub Actions `sync.yml` — 定时内容同步

### 背景

当前 `scripts/` 下有 5 个自动化脚本（fetch / sync-github / classify / translate / release-watch），  
但都只能手动运行。需要创建 GitHub Actions 工作流实现：

- **每周自动抓取** → 官方文档 + GitHub Issues 更新
- **自动分类打标签** → 写入 `data/articles.json`
- **自动 AI 翻译** → 调用 opencode-go 翻译为中文
- **检测到新内容** → 自动 commit + push → 触发 deploy 重新部署

### 前置条件

- **OP-1 完成**（需 API Key）
- **OP-4 完成**（Key 已存入 GitHub Secrets）

### 操作手顺

> 此操作由 Agent 完成后台代码编写，用户无需手动创建文件。  
> 根据你的要求，我会在需要你介入时告知。

1. **等待通知** — 我会告诉你 `sync.yml` 已写好并 push
2. **确认运行** — 我可能让你手动触发一次测试运行
3. **检查结果** — 确认 commit 自动生成、deploy 正常触发

### 验证标准

- GitHub Actions 面板出现 `Sync Content` 工作流
- 每周运行或手动触发都能成功
- 运行后仓库出现新的自动 commit（如 `auto: sync 2026-05-01`）

---

## OP-3：GitHub Actions `validate.yml` — 链接与数据校验

### 背景

随着内容增多，需要自动检查：
- 所有原文链接是否可达（`validate-links.py`）
- frontmatter 字段是否符合 v2 规范
- 数据文件 JSON 格式是否正确

每次 PR 推送时自动运行，阻塞合并不合规内容。

### 前置条件

无。纯代码层面，不依赖 API Key。

### 操作手顺

> 同样由 Agent 完成后台代码编写。

1. **等待通知** — `validate.yml` 写好后告知
2. **无需额外操作** — 自动在 PR 上运行
3. **查看失败通知** — 如有链接失效会收到告警

### 验证标准

- 创建 PR 时自动触发 `Validate` 检查
- 检查通过显示绿色 ✅

---

## OP-4：配置 GitHub Secrets

### 背景

GitHub Actions 中运行的脚本需要访问 opencode-go 翻译 API，  
但 Key 不能写在代码里。需要存入 GitHub 仓库的 Secrets 中。

### 前置条件

- **OP-1 完成**（已获取 Key）
- 仓库 Settings → Secrets and variables → Actions 有访问权限

### 操作手顺

1. **打开仓库 Settings**
   - 浏览器访问：https://github.com/dodoqumy/rocm-hip-map/settings/secrets/actions

2. **新建 Repository Secret**
   - 点击 **New repository secret**

3. **填入信息**
   | 字段 | 值 |
   |------|-----|
   | Name | `TRANSLATE_API_KEY` |
   | Secret | `你的 opencode-go API Key` |

4. **保存**
   - 点击 **Add secret**

5. **（可选）再添加一个**
   | Name | `OPENCODE_BASE_URL` |
   |------|----------------------|
   | Secret | `https://opencode.ai/zen/go/v1` |

### 验证标准

- Secrets 列表中出现 `TRANSLATE_API_KEY`
- `sync.yml` 工作流运行时不报认证错误

---

## OP-5：Algolia DocSearch 申请（远期）

### 背景

Docusaurus 内置 Algolia DocSearch，提供中英双语全文搜索。  
需要向 Algolia 申请免费开源项目额度。

### 前置条件

- 网站已上线并有稳定流量
- 有公开的 GitHub 仓库

### 操作手顺

> 留待 Phase 7.6 时详细记录。

1. 访问 https://docsearch.algolia.com/apply/
2. 填写申请表单（仓库 URL + 网站 URL）
3. 等待审批（通常 1-2 周）
4. 获取 `appId` + `apiKey` + `indexName`
5. 配置到 `docusaurus.config.ts`

---

## OP-6：网站分析接入（远期）

### 背景

接入 Umami（开源/免费分析）或 Google Analytics 了解：
- 哪些文档被阅读最多
- 中英文用户比例
- 搜索关键词分布

### 前置条件

- Umami 账号（推荐自部署）或 GA 账号

### 操作手顺

> 留待 Phase 7.8 时详细记录。

---

> **更新规则：** 每次新增用户依赖操作时追加到此文档，完成后标记 ✅。
