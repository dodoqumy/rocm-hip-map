# ROCm 文档抓取统计

> 更新时间: 2026-05-03 06:22

## 总计

- **总文件数**: 1159 篇 (+209 本次)
- **子项目数**: 35 个 (含新增 8 个)

## 各子项目详情

| 子项目 | 文件数 | 状态 | 本次新增 |
|--------|--------|------|----------|
| github | 215 | ⚠️ | 0 |
| rocm-docs-latest | 201 | ✅ | +6 |
| rocm-docs-7.2.0 | 67 | ✅ | +4 |
| rocm-docs-7.0.0 | 57 | ✅ | +2 |
| hip-latest | 89 | ✅ | 0 |
| rocsparse-latest | 26 | ✅ | 0 |
| rocblas-latest | 24 | ✅ | 0 |
| hipsolver-latest | 25 | ✅ | +2 |
| miopen-latest | 21 | ⚠️ | +1 |
| hipsparsert-latest | 23 | ✅ | +3 |
| hipfort-latest | 22 | ⚠️ | +2 |
| composable-kernel-latest | 36 | ⚠️ | +16 |
| rocsolver-latest | 19 | ✅ | 0 |
| rocprofiler-sdk-latest | 37 | ✅ | +18 |
| rocprofiler-latest | 27 | ✅ | +8 |
| hipblaslt-latest | 19 | ✅ | 0 |
| hipsparse-latest | 18 | ✅ | 0 |
| rocrand-latest | 19 | ⚠️ | +3 |
| rocal-latest | 16 | ⚠️ | 0 |
| rocfft-latest | 13 | ✅ | 0 |
| hipblas-latest | 10 | ✅ | 0 |
| rocwmma-latest | 6 | ⚠️ | 0 |
| hiprand-latest | 6 | ⚠️ | 0 |
| rocm-install-linux | 5 | ⚠️ | 0 |
| hipfft-latest | 5 | ✅ | 0 |
| hip | 5 | ⚠️ | 0 |
| hipify | 4 | ⚠️ | 0 |
| **amdsmi-latest** | **30** | **✅ 新增** | **+30** |
| **hipify-latest** | **30** | **✅ 新增** | **+26** |
| **install-linux-latest** | **22** | **✅ 新增** | **+17** |
| **install-windows-latest** | **7** | **✅ 新增** | **+7** |
| **rocvisionx-latest** | **18** | **✅ 新增** | **+18** |
| **rocthunk-latest** | **13** | **✅ 新增** | **+13** |
| **rocprim-latest** | **12** | **✅ 新增** | **+12** |
| **hipcub-latest** | **11** | **✅ 新增** | **+11** |
| **rocprofiler-sdk-latest** | **37** | ✅ | +18 |
| **rocprofiler-latest** | **27** | ✅ | +8 |

## 抓取配置

- 配置文件: `config/amd-sources.yaml`
- 状态文件: `data/fetch-state.json`
- 原始内容: `content/raw/english/`

## 增量抓取说明

使用 `--all` 模式增量抓取，已抓取的 URL 会自动跳过。
状态记录在 `data/fetch-state.json`，每次运行自动更新。

## 待完成子项目 (13 个)

```
1. rocm-docs-6.4.0, rocm-docs-6.2.0, rocm-docs-6.0.0 (历史版本，URL 不可访问)
2. llvm-project-latest (1篇/29错误，doxygen页面大量404)
3. rccl-latest (discovered=0，需检查URL)
4. rocgdb-latest, rocdecode-latest (discovered=0)
5. migraphx-latest, ai-developer-hub-latest (discovered=0)
6. hipfft-ext-latest, rocm-blog, rocm-ds-latest, rocm-ls-latest
7. rocm-validation-suite-latest, rocm-agent-lib-latest
```

## 本次运行详情 (2026-05-03 06:00)

- 运行时间: ~20分钟
- 抓取源: 46 个子项目
- 本次保存: 269 篇（含文件更新重写）
- 纯新增: 152 篇，文件更新: 57 篇
- Git commit: `7912eb7`
- 主要贡献: amdsmi(+30), hipify(+26), install-linux(+17), rocvisionx(+18),
  rocprofiler-sdk(+18), composable-kernel(+16), rocthunk(+13), rocprim(+12),
  hipcub(+11), rocprofiler(+8), install-windows(+7), rocrand(+3)
