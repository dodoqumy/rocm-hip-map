---
title: "rocSPARSE profiling functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/roctx.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:06.620001+00:00
content_hash: "3a67b87b44fbca57"
---

# rocSPARSE profiling functions[#](#rocsparse-profiling-functions)

This module contains all routines useful for profiling rocSPARSE programs.

## rocsparse_enable_roctx()[#](#rocsparse-enable-roctx)

-
void rocsparse_enable_roctx()
[#](#_CPPv422rocsparse_enable_roctxv) Enable rocTX instrumentation.

Note

This routine ignores the environment variable ROCSPARSE_ROCTX.


## rocsparse_disable_roctx()[#](#rocsparse-disable-roctx)

-
void rocsparse_disable_roctx()
[#](#_CPPv423rocsparse_disable_roctxv) Disable rocTX instrumentation.

Note

This routine ignores the environment variable ROCSPARSE_ROCTX.


## rocsparse_state_roctx()[#](#rocsparse-state-roctx)

-
int rocsparse_state_roctx()
[#](#_CPPv421rocsparse_state_roctxv) Query whether rocTX instrumentation has been enabled. See

[rocsparse_enable_roctx](#rocsparse-roctx_8h_1a35d7f1b4d2212cf164aa35c85321daba).- Returns:
1 if enabled, 0 otherwise.
