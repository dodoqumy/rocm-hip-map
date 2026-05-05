---
title: "ROCm release versioning"
source_url: "https://rocm.docs.amd.com/projects/install-on-windows/en/latest/about/release-versioning.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:45.734773+00:00
content_hash: "b8106dcbc22b3485"
---

# ROCm release versioning[#](#rocm-release-versioning)

2026-02-19

2 min read time

Windows will follow Linux version numbers, as Windows ROCm releases are based on Linux ROCm releases. However, not all Linux ROCm releases will have a corresponding Windows ROCm release. The following table shows all ROCm releases. Releases with both Windows and Linux are referred to as a joint release. Releases with only Linux support are referred to as a skipped release (from a Windows perspective).

ROCm version |
Linux support |
Windows support |
|---|---|---|
5.5 |
✅ |
✅ |
5.6 |
✅ |
❌ |
5.7 |
✅ |
✅ |
6.0 |
✅ |
❌ |
6.1 |
✅ |
✅ |
6.2 |
✅ |
✅ |
6.3 |
✅ |
❌ |
6.4 |
✅ |
✅ |
7.1 |
✅ |
✅ |

In general, Windows releases trail Linux releases. If you want to support both Linux and Windows using a single ROCm version, refrain from upgrading ROCm until there is a joint release.

## Windows documentation implications[#](#windows-documentation-implications)

The ROCm documentation website contains both Windows and Linux documentation. Just below each article title, a convenient article information section states whether the page applies to Linux only, Windows only, or both. To find the exact Windows documentation for a HIP SDK release, refer to the ROCm documentation with the same Major.Minor version number while ignoring the patch version (which is only relevant for Linux releases). For convenience, we will continue to include Windows documentation in release documentation for skipped Windows releases.

Windows release notes contain only information pertinent to Windows.

## Windows builds from source[#](#windows-builds-from-source)

Not all source code required to build Windows from source is available under a permissive open source license. We only provide Windows build instructions for projects that can be built from source on Windows using a toolchain that has closed source build prerequisites. The ROCm manifest file is not valid for Windows. AMD does not release a manifest or tag our components in Windows. You can use corresponding Linux tags to build on Windows.
