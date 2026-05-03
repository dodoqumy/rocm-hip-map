# ROCm 文档抓取统计

> 更新时间: 2026-05-03 09:11

## 总计

- **总文件数**: 1175 篇 (+16 本次增量)
- **子项目数**: 32 个

## 各子项目详情

| 子项目 | 文件数 | 状态 |
|--------|--------|------|
| github | 215 | ⚠️ |
| rocm-docs-latest | 203 | ✅ |
| composable-kernel-latest | 39 | ✅ |
| rocm-docs-7.2.0 | 74 | ✅ |
| rocm-docs-7.0.0 | 61 | ✅ |
| hip-latest | 89 | ✅ |
| rocsparse-latest | 26 | ✅ |
| hipsparsert-latest | 24 | ✅ |
| hipsolver-latest | 25 | ✅ |
| rocblas-latest | 24 | ✅ |
| hipfort-latest | 22 | ⚠️ |
| install-linux-latest | 22 | ✅ |
| miopen-latest | 21 | ⚠️ |
| amdsmi-latest | 30 | ✅ |
| rocprofiler-sdk-latest | 37 | ✅ |
| rocprofiler-latest | 27 | ✅ |
| hipblaslt-latest | 19 | ✅ |
| hipsparse-latest | 18 | ✅ |
| rocsolver-latest | 19 | ✅ |
| rocrand-latest | 19 | ⚠️ |
| rocfft-latest | 13 | ✅ |
| rocvisionx-latest | 18 | ✅ |
| hipify-latest | 30 | ✅ |
| rocthunk-latest | 13 | ✅ |
| rocprim-latest | 12 | ✅ |
| hipcub-latest | 11 | ✅ |
| hipblas-latest | 10 | ✅ |
| install-windows-latest | 7 | ✅ |
| rocal-latest | 16 | ⚠️ |
| hipfft-latest | 5 | ✅ |
| rocwmma-latest | 6 | ⚠️ |
| hiprand-latest | 6 | ⚠️ |
| rocm-install-linux | 5 | ⚠️ |
| hip | 5 | ⚠️ |
| hipify | 4 | ⚠️ |
| llvm-project-latest | 1 | ⚠️ |

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
- rccl-latest (404)
- migraphx-latest (404)
- rocgdb-latest, rocdecode-latest (discovered=0)
- rocm-blog, rocm-ds-latest, rocm-ls-latest
- rocm-validation-suite-latest, rocm-agent-lib-latest
- hipfft-ext-latest, ai-developer-hub-latest

# 问题子项目
- rocm-docs-6.4.0, rocm-docs-6.2.0, rocm-docs-6.0.0 (历史版本不可访问)
- llvm-project-latest (doxygen页面大量404)
```

## 本次运行详情 (2026-05-03 09:00)

- 运行时间: ~10分钟（超时，脚本未完整跑完）
- 抓取源: 46 个子项目（部分未完成）
- 本次保存: 35 files (16 new + 19 modified)
- Git commit: `ceb45b2`
- 本次新增: composable-kernel(+3), rocm-docs-7.2.0(+7), rocm-docs-7.0.0(+4),
  rocm-docs-latest(+2), hipsparsert(+1)
