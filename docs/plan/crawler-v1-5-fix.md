# Crawler V1.5 Fix — 内容抓取工作流修复

## 问题诊断

原 V1.0 的抓取链路是"半成品采集器"：

1. **fetch-official.py**
   - 手工 pages[] 数组，文件存在就 skip
   - 不检测页面更新，不自动发现新增页面

2. **sync-github.py**
   - 每仓库只拉 20 条，只看 4 个 repo
   - 标签过滤过严，releases 未覆盖

3. **classify.py**
   - 输出"68 files scanned"不展示 source_type 分布

4. **release-watch.py**
   - 仅 HIP + ROCm versions page，缺 MIOpen/RCCL 等库

---

## 修复内容

### fetch-official.py (v1.5)

新增参数：
```bash
--auto-discover  # 从 rocm.docs.amd.com/sitemap.xml 自动发现 URL
--dry-run      # 预览不抓取
--verbose, -v # 详细输出
```

增量更新：
```bash
data/fetch-state.json  # 保存 URL → content_hash 映射
# 抓取时对比 hash，内容变化则重新抓取
```

输出 stats：
```
📊 Stats:
   68 known urls
   12 updated
   5 new
   51 unchanged
```

---

### sync-github.py (v1.5)

扩展 repo 列表（12 个）：
- ROCm/ROCm, HIP, HIPIFY
- rocm-libraries, rocBLAS, rocFFT, rocSOLVER, rocSparse
- MIOpen, RCCL, composable_kernel
- pytorch, tensorflow-rocm

新增参数：
```bash
--type issues,releases  # 仅抓取 issue 或 release
--days 90           # 最近 90 天（默认）
```

输出 stats：
```
📊 Stats:
   42 issues
   15 releases
   Total: 57
```

---

### release-watch.py (v1.5)

扩展版本源（8 个）：
- ROCm docs versions page
- ROCm, HIP, MIOpen, RCCL
- rocBLAS, rocFFT, rocSOLVER, rocSparse

新增参数：
```bash
--verbose, -v  # 显示所有版本（包括 unchanged）
```

---

### classify.py (v1.5)

已有 stats 输出（无需修改）：
```
📊 68 files scanned, 42 classified
```

---

## 使用方法

### 完整抓取工作流

```bash
# 1. 抓取官方文档（自动发现）
python3 scripts/fetch-official.py --auto-discover

# 2. 抓取 GitHub issues + releases
python3 scripts/sync-github.py --type issues,releases --days 90

# 3. 分类打标签
python3 scripts/classify.py

# 4. 监控版本
python3 scripts/release-watch.py
```

### 调试模式

```bash
# 预览要抓取的内容（不实际抓）
python3 scripts/fetch-official.py --dry-run --auto-discover -v
python3 scripts/sync-github.py --dry-run -v

# 查看版本但不保存
python3 scripts/release-watch.py --verbose
```

---

## 后续 V2 升级路线

1. 调度器：Prefect Cloud flows（定时编排多个爬虫）
2. 并发：asyncio 多源并行抓取
3. 存储：SQLite 替换 JSON（已有 crawlers/ 框架）
4. 监控：Prometheus metrics + Grafana 面板

---

## Changelog

- 2026-05-01: V1.5 发布
  - fetch-official: sitemap 自动发现 + 增量更新
  - sync-github: 扩展 repo + releases + 时间过滤
  - release-watch: 扩展到 8 个版本源