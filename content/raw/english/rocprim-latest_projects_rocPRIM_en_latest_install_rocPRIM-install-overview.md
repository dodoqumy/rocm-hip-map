---
title: "rocPRIM installation overview &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/install/rocPRIM-install-overview.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:17:28.733515+00:00
content_hash: "00f762b4cbf711fd"
---

# rocPRIM installation overview[#](#rocprim-installation-overview)

The rocPRIM source code is available from the [ROCm libraries GitHub Repository](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocprim). Use sparse checkout when cloning the rocPRIM project:

```
git clone --no-checkout --filter=blob:none https://github.com/ROCm/rocm-libraries.git
cd rocm-libraries
git sparse-checkout init --cone
git sparse-checkout set projects/rocprim
```

Then use `git checkout`

to check out the branch you need.

The develop branch is intended for users who want to preview new features or contribute to the rocPRIM code base.

If you don’t intend to contribute to the rocPRIM code base and won’t be previewing features, use a branch that matches the version of ROCm installed on your system.
