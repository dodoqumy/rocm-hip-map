---
title: "ROCm 6.2.2 Release"
source_url: https://github.com/ROCm/ROCm/releases/tag/rocm-6.2.2
source_type: github-release
source_org: ROCm
published_date: 2024-09-27
credibility: 4
lifecycle: latest
tags: [github-release, rocm-6.2.2]
---

# ROCm 6.2.2 Release

> 📦 **Release:** [rocm-6.2.2](https://github.com/ROCm/ROCm/releases/tag/rocm-6.2.2)
> **发布:** 2024-09-27

# ROCm 6.2.2 release notes

These release notes provide a summary of notable changes since the previous ROCm release.

```{note}
As ROCm 6.2.2 was released shortly after 6.2.1, the changes between these versions
are minimal. For a comprehensive overview of recent updates,
refer to the ROCm 6.2.1 release notes.
```

The [Compatibility matrix](https://rocm.docs.amd.com/en/docs-6.2.2/compatibility/compatibility-matrix.html)
provides the full list of supported hardware, operating systems, ecosystems, third-party components, and ROCm components
for each ROCm release.

Release notes for previous ROCm releases are available in earlier versions of the documentation.
See the [ROCm documentation release history](https://rocm.docs.amd.com/en/latest/release/versions.html).

## Release highlights

The following is a significant fix introduced in ROCm 6.2.2.

### Fixed Instinct MI300X error recovery failure

Improved the reliability of AMD Instinct MI300X accelerators in scenarios involving
uncorrectable errors. Previously, error recovery did not occur as expected,
potentially leaving the system in an undefined state. This fix ensures that error
recovery functions as expected, maintaining system stability.

See the original issue noted in the ROCm 6.2.1 release notes.

