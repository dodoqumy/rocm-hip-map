---
title: "Installing multiple ROCm versions"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/multi-version-install-index.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:13:42.991534+00:00
content_hash: "b181eb22732201aa"
---

# Installing multiple ROCm versions[#](#installing-multiple-rocm-versions)

2025-11-18

2 min read time

A multi-version ROCm installation covers situations where you need multiple versions of ROCm on the same machine–for compatibility with different applications and hardware, testing, and other use cases.

A multi-version ROCm installation involves the following:

Installing multiple instances of the ROCm stack on a system.

Using versioned ROCm meta-packages. ROCm packages are versioned with both a ROCm release version and package-specific semantic versioning. Extending a package name and its dependencies with the release version adds the ability to support multiple versions of packages simultaneously.


A single-version ROCm installation involves the following.

Installing a single instance of the ROCm release on a system.

Using non-versioned ROCm meta-packages.


See [Quick start installation guide](../quick-start.html) or [Detailed install](../detailed-install.html) for
a standard single-version installation.

Caution

You cannot install single-version and multi-version ROCm packages together on the same machine. The conflicting package versions might result in unpredictable behavior.

The following illustrations shows the difference between single-version and multi-version ROCm installations.

Select the install and uninstall instructions for your operating system

See also: [System requirements (Linux)](../../reference/system-requirements.html). If you encounter install issues, you can refer to the
[troubleshooting](../../reference/install-faq.html) page.
