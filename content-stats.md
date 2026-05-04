# ROCm 文档抓取统计

> 更新时间: 2026-05-04 21:12 UTC

## 总计

- **总文件数**: 1246 篇
- **子项目数**: 38 个

## 各子项目详情

| 子项目 | 文件数 | 状态 |
|--------|--------|------|
| github | 215 | ⚠️ |
| rocm-docs-latest | 210 | ✅ |
| hip-latest | 89 | ✅ |
| rocm-docs-7.2.0 | 76 | ✅ |
| rocm-docs-7.0.0 | 68 | ✅ |
| amdsmi-latest | 57 | ✅ |
| rocprofiler-sdk-latest | 44 | ✅ |
| composable-kernel-latest | 41 | ✅ |
| hipify-latest | 31 | ✅ |
| hipsparsert-latest | 27 | ✅ |
| rocprofiler-latest | 27 | ✅ |
| rocsparse-latest | 26 | ✅ |
| hipsolver-latest | 25 | ✅ |
| install-linux-latest | 24 | ✅ |
| rocblas-latest | 24 | ✅ |
| rocrand-latest | 22 | ✅ |
| hipfort-latest | 22 | ⚠️ |
| miopen-latest | 21 | ⚠️ |
| hipblaslt-latest | 19 | ✅ |
| rocsolver-latest | 19 | ✅ |
| rocvisionx-latest | 18 | ✅ |
| rocprim-latest | 18 | ✅ |
| hipsparse-latest | 18 | ✅ |
| rocal-latest | 16 | ⚠️ |
| rocthunk-latest | 13 | ✅ |
| rocfft-latest | 13 | ✅ |
| hipcub-latest | 11 | ✅ |
| hipblas-latest | 10 | ✅ |
| install-windows-latest | 7 | ✅ |
| rocwmma-latest | 6 | ⚠️ |
| hiprand-latest | 6 | ⚠️ |
| rocm-install-linux | 5 | ⚠️ |
| hipfft-latest | 5 | ✅ |
| hip | 5 | ⚠️ |
| hipify | 4 | ⚠️ |
| llvm-project-latest | 2 | ⚠️ |

## 抓取配置

- 配置文件: `config/amd-sources.yaml`
- 状态文件: `data/fetch-state.json`
- 原始内容: `content/raw/english/`

## 增量抓取说明

使用 `--all` 模式增量抓取，已抓取的 URL 会自动跳过。
状态记录在 `data/fetch-state.json`，每次运行自动更新。

## 待完成子项目 (不可用/待排查)

```
# 404/不可用
- rccl-latest (404 — 文档站已移除)
- migraphx-latest (404 — 文档站已移除)
- rocgdb-latest (404)
- rocdecode-latest (sitemap 返回非XML)
- rocm-blog (RSS feed 404)
- rocm-ds-latest, rocm-ls-latest (spinx_nav discover 0 URLs)
- rocm-validation-suite-latest (404)
- rocm-agent-lib-latest (sitemap 返回非XML)
- hipfft-ext-latest (404)
- ai-developer-hub-latest (Cloudflare 拦截爬虫 UA)

# 历史版本不可访问
- rocm-docs-6.4.0, rocm-docs-6.2.0, rocm-docs-6.0.0

# 部分页面失效
- llvm-project-latest (doxygen 页面大量 404，rate limit)
```

## 本次运行详情 (2026-05-04 12:01 UTC)

- 运行时间: ~10 分钟（超时退出，46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，已抓取的 URL 跳过）
- 更新文件: 1 篇（rocm-docs-latest mi300x 页面内容清理）
- 新增文件: 1 篇（rocm-docs-latest jax-maxtext-v25.11 旧版本训练文档）
- 总计: 1245 篇（content/raw/english/ 下 .md 文件）

## 本次运行详情 (2026-05-04 15:10 UTC)

- 运行时间: ~10 分钟（超时退出，46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，全部 URL 已缓存，无新抓取）
- 更新文件: 0 篇
- 新增文件: 0 篇
- 总计: 1245 篇（content/raw/english/ 下 .md 文件）

## 本次运行详情 (2026-05-04 18:10 UTC)

- 运行时间: ~9 分钟（超时退出，46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，已抓取的 URL 跳过）
- 更新文件: 0 篇
- 新增文件: 1 篇（amdsmi-latest doxygen functions_vars_s 页面已缓存但之前被跳过，本次成功抓取）
- 总计: 1246 篇（content/raw/english/ 下 .md 文件）

## 本次运行详情 (2026-05-04 09:02 UTC)

- 运行时间: ~10 分钟（超时退出，46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，已抓取的 URL 跳过）
- 更新文件: 2 篇（amdsmi-latest doxygen functions_g + install-linux-latest multi-version-install-debian）
- 新增文件: 4 篇（amdsmi-latest doxygen: files, functions_o, functions_v, functions_vars_o）
- 总计: 1244 篇（content/raw/english/ 下 .md 文件）

## 历史运行 (2026-05-04 06:02 UTC)

- 运行时间: ~5 分钟（超时退出，约 46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，已抓取的 URL 跳过）
- 更新文件: 1 篇（rocm-docs-latest programming_guide 页面内容更新）
- 新增文件: 0 篇
- 总计: 1240 篇（content/raw/english/ 下 .md 文件）

## 历史运行 (2026-05-04 03:10 UTC)

- 运行时间: ~10 分钟（超时退出，约 46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，已抓取的 URL 跳过）
- 更新文件: 1 篇（amdsmi-latest doxygen functions_g 页面内容更新）
- 新增文件: 2 篇（rocm-docs-latest megatron-lm-v25.7 训练文档 + amdsmi-latest doxygen functions_t）
- 总计: 1240 篇（content/raw/english/ 下 .md 文件）
## 本次运行 (2026-05-04 21:12 UTC)

- 运行时间: ~10 分钟（600 秒超时退出，46 个源在增量模式下运行）
- 抓取源: 46 个子项目（增量模式，3 个 Doxygen 页面 re-fetch）
- 更新文件: 3 篇（amdsmi-latest functions_m, functions_t, setup-docker-container）
- 新增文件: 0 篇
- 总计: 1246 篇
- 未抓取源: 14 个（仍为 0 URL — rocm-docs-6.4.0/6.2.0/6.0.0, rocgdb, rocdecode, migraphx, rccl, ai-developer-hub, hipfft-ext, rocm-blog, rocm-ds, rocm-ls, rocm-validation-suite, rocm-agent-lib — URL 发现依然失败）

