# ROCm 文档抓取统计

> 更新时间: 2026-05-03 15:31 UTC

## 总计

- **总文件数**: 1228 篇 (+38 本次增量)
- **子项目数**: 38 个

## 各子项目详情

| 子项目 | 文件数 | 状态 |
|--------|--------|------|
| github | 215 | ⚠️ |
| rocm-docs-latest | 206 | ✅ |
| hip-latest | 89 | ✅ |
| rocm-docs-7.2.0 | 75 | ✅ |
| rocm-docs-7.0.0 | 66 | ✅ |
| amdsmi-latest | 48 | ✅ |
| rocprofiler-sdk-latest | 44 | ✅ |
| composable-kernel-latest | 41 | ✅ |
| hipify-latest | 31 | ✅ |
| hipsparsert-latest | 27 | ✅ |
| rocprofiler-latest | 27 | ✅ |
| rocsparse-latest | 26 | ✅ |
| hipsolver-latest | 25 | ✅ |
| rocblas-latest | 24 | ✅ |
| install-linux-latest | 24 | ✅ |
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

## 本次运行详情 (2026-05-03 15:00 UTC)

- 运行时间: ~17 分钟（46 个源完整跑完）
- 抓取源: 46 个子项目
- Git commit: `b3e9ad8`
- 本次新增: amdsmi-latest(+16), rocprofiler-sdk-latest(+7),
  rocprim-latest(+6), rocm-docs-latest(+5), install-linux-latest(+3),
  hipfort-latest(+3), rocrand-latest(+1), llvm-project-latest(+1),
  rocm-docs-7.2.0(+1), rocm-docs-7.0.0(+4)
- 新增文件: 38 篇
- 更新文件: 13 篇
- 总计: 1228 篇
