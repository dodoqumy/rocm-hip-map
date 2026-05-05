---
title: "ROCm-LS 26.03 release notes"
source_url: "https://rocm.docs.amd.com/projects/rocm-ls/en/latest/about/release-notes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:26:40.653251+00:00
content_hash: "c74b9b4004ec5e0c"
---

# ROCm-LS 26.03 release notes[#](#rocm-ls-26-03-release-notes)


2 min read time

The release notes provide a summary of notable changes since the previous ROCm-LS release.

## Release highlights[#](#release-highlights)

The following are notable new features and improvements in ROCm-LS 26.03 since the 25.11 release. For detailed changes to individual components, see [detailed component changelogs](#detailed-component-changelogs).

**MONAI 1.5.2 on ROCm**exits Early Access (EA) state and is now production-ready for life sciences imaging workloads on AMD GPUs. It’s based on the upstream project[MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/releases/tag/1.5.2)**ROCm 7.2.0 support:**ROCm-LS 26.03 adds support for ROCm 7.2.0 while continuing support for ROCm 7.0.2.

## ROCm-LS components[#](#rocm-ls-components)

The following table lists the versions of ROCm-LS components for ROCm-LS 26.03, including any version changes from 25.11 to 26.03. Click the GitHub icon to go to the component’s source code.

| Category | Component name | Version | Source code |
|---|---|---|---|
| Imaging |
|

[MONAI on ROCm](https://rocm.docs.amd.com/projects/monai/en/docs-26.03/)[1.5.2](#monai-on-rocm-1-5-2)Note

The hipCIM version remains unchanged in this release.

## Detailed component changelogs[#](#detailed-component-changelogs)

The following sections describe key changes to the ROCm-LS components:

### hipCIM (25.10.00)[#](#hipcim-25-10-00)

#### Added[#](#added)

Support for ROCm 7.2.0 (support for ROCm 7.0.2 is maintained).

Support for AMD Instinct™ GPUs MI355X and MI300X.


#### Removed[#](#removed)

Support for ROCm 6.4.3.

Support for Ubuntu 22.04 and Python 3.10.

Support for AMD Instinct GPU MI300A.


### MONAI on ROCm (1.5.2)[#](#monai-on-rocm-1-5-2)

This release is based on the upstream [MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/releases/tag/1.5.2) release. Apart from the changes introduced in the [upstream MONAI 1.5.2](https://github.com/Project-MONAI/MONAI/compare/releasing/1.5.0...1.5.2), MONAI on ROCm 1.5.2 includes the following changes:

#### Added[#](#id1)

Support for ROCm 7.2.0.

Support for

[PyTorch for AMD ROCm](https://pytorch.org/blog/pytorch-for-amd-rocm-platform-now-available-as-python-package/)2.8 and later.Support for AMD Instinct GPUs MI355X and MI325X.

Support for Ubuntu 24.04 and Python 3.12.


#### Known issues[#](#known-issues)

Issues with GMM kernel on Multi-GPU.

MIOpen runtime issue with 3D data on Multi‑GPU for 3D convolutions.
