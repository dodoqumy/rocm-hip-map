# ROCm 文档抓取统计

> 更新时间: 2026-05-03 03:11

## 总计

- **总文件数**: 950 篇
- **子项目数**: 27 个

## 各子项目详情

| 子项目 | 文件数 | 状态 |
|--------|--------|------|
| github | 215 | ⚠️ |
| rocm-docs-latest | 195 | ✅ |
| hip-latest | 89 | ✅ |
| rocm-docs-7.2.0 | 63 | ✅ |
| rocm-docs-7.0.0 | 55 | ✅ |
| rocsparse-latest | 26 | ✅ |
| rocblas-latest | 24 | ✅ |
| hipsolver-latest | 23 | ✅ |
| miopen-latest | 20 | ⚠️ |
| hipsparsert-latest | 20 | ✅ |
| hipfort-latest | 20 | ⚠️ |
| composable-kernel-latest | 20 | ⚠️ |
| rocsolver-latest | 19 | ✅ |
| rocprofiler-sdk-latest | 19 | ✅ |
| rocprofiler-latest | 19 | ✅ |
| hipblaslt-latest | 19 | ✅ |
| hipsparse-latest | 18 | ✅ |
| rocrand-latest | 16 | ⚠️ |
| rocal-latest | 16 | ✅ |
| rocfft-latest | 13 | ✅ |
| hipblas-latest | 10 | ✅ |
| rocwmma-latest | 6 | ⚠️ |
| hiprand-latest | 6 | ⚠️ |
| rocm-install-linux | 5 | ⚠️ |
| hipfft-latest | 5 | ✅ |
| hip | 5 | ⚠️ |
| hipify | 4 | ⚠️ |

## 抓取配置

- 配置文件: `config/amd-sources.yaml`
- 状态文件: `data/fetch-state.json`
- 原始内容: `content/raw/english/`

## 增量抓取说明

使用 `--all` 模式增量抓取，已抓取的 URL 会自动跳过。
状态记录在 `data/fetch-state.json`，每次运行自动更新。

## 待完成子项目 (20 个)

```
1. rocm-docs-6.4.0, rocm-docs-6.2.0, rocm-docs-6.0.0 (历史版本)
2. llvm-project-latest, amdsmi-latest (系统管理/编译器)
3. rccl-latest (通信库)
4. hipify-latest, hipcub-latest, rocprim-latest (工具链)
5. rocgdb-latest, rocdecode-latest (调试/解码)
6. migraphx-latest, ai-developer-hub-latest (推理/AI Hub)
7. rocthunk-latest, rocvisionx-latest, hipfft-ext-latest
8. rocm-blog, rocm-ds-latest, rocm-ls-latest, rocm-validation-suite-latest
9. install-linux-latest, install-windows-latest
10. rocm-agent-lib-latest
```
