---
title: "[CK] Smart-build CTest invocation can run more tests than were built, causing spurious "Not Run" CI failures"
source_url: https://github.com/ROCm/rocm-libraries/issues/6956
source_type: github-issue
source_org: rocm
published_date: 2026-04-30
credibility: 3
lifecycle: latest
tags: [github-issue, bug, ci]
gpu: []
rocm_versions: []
---

# [CK] Smart-build CTest invocation can run more tests than were built, causing spurious "Not Run" CI failures

> 🐛 **GitHub Issue:** [ROCm/rocm-libraries#6956](https://github.com/ROCm/rocm-libraries/issues/6956)
> **状态:** open | **标签:** bug, ci
> **创建:** 2026-04-30 | **更新:** 2026-04-30

## Summary

In Composable Kernel's "smart build" CI pipeline (`projects/composablekernel/script/dependency-parser/`), there is a structural mismatch between the **set of tests selected/built** and the **set of tests CTest actually attempts to run**. When the runtime set ends up larger than the built set, CTest tries to launch binaries that do not exist, marks them `(Not Run)`, and exits non-zero — failing CI even when the PR under test contains no defect.

## How this was discovered

Surfaced on **PR #6761 (`[CK] Large tensor gemm workaround`)**, build **#19** (Jenkins job `users/zlakatos/ck/large_tensor_gemm_workaround`).

The PR modified two headers:
- `projects/composablekernel/include/ck/tensor_operation/gpu/device/impl/device_gemm_multiple_d_xdl_cshuffle_v3.hpp`
- `projects/composablekernel/include/ck/tensor_operation/gpu/device/impl/device_gemm_xdl_cshuffle_v3_mx.hpp`

Smart-build correctly identified **5 affected tests**, wrote them to `tests_to_run.json` / `build_targets.txt`, and ninja built **5 binaries** successfully.

CTest then attempted to run **8 tests**. The 3 extras —
- `example_gemm_multiply_multiply_xdl_fp8_ab_scale`
- `example_gemm_multiply_multiply_xdl_fp8_blockscale_bpreshuffle`
- `example_gemm_multiply_multiply_xdl_fp8_bpreshuffle`

— were never built (correctly: their `.cpp` files include sibling headers `_ab_scale.hpp` / `_blockscale_bpreshuffle.hpp` / `_b_preshuffle.hpp`, none of which transitively pull in the modified header). CTest reported them as `***Not Run`, returned a non-zero exit code, and the pipeline failed.

Relevant log excerpt:

```
1/8 Test #316: example_gemm_multiply_multiply_xdl_fp8_ab_scale .................***Not Run   0.00 sec
2/8 Test #317: example_gemm_multiply_multiply_xdl_fp8_blockscale_bpreshuffle ...***Not Run   0.00 sec
3/8 Test #318: example_gemm_multiply_multiply_xdl_fp8_bpreshuffle ..............***Not Run   0.00 sec
...
The following tests FAILED:
        316 - example_gemm_multiply_multiply_xdl_fp8_ab_scale (Not Run)
        317 - example_gemm_multiply_multiply_xdl_fp8_blockscale_bpreshuffle (Not Run)
        318 - example_gemm_multiply_multiply_xdl_fp8_bpreshuffle (Not Run)
Errors while running CTest
script returned exit code 8
```

## Root cause

The smart-build pipeline serializes the selected test set to `tests_to_run.json` and then drives CTest indirectly via a regex string. The "selected set" and the "actually-runnable set" are not enforced to match — they are coupled only by the semantics of whatever string is passed to `ctest -R`. Any time those semantics diverge from naive equality (substring matching, regex metacharacters, name-vs-target divergence, multiple independent regex builders, copy-pasted Jenkinsfile snippets that use a different field, etc.), the build/run sets can drift apart and unbuilt binaries get scheduled.

The current PR-6761 incident is one concrete instance of this drift (substring overmatch between selected and unselected test names that share a common prefix), but the underlying problem is structural, not specific to the regex form used today.

## Why a regex-anchoring patch is not sufficient

It would unblock PR #6761, but it leaves the same class of failure mode in place:

- Multiple independent producers/consumers of the test list exist in the tree (the dependency-parser scripts, local launcher script, README/Jenkinsfile examples). Each one re-derives the regex on its own — fixing one does not fix the others.
- The `regex` field in `tests_to_run.json` is consumed by README example snippets that downstream pipelines may have copied verbatim.
- The script already has the authoritative test name list in memory (it calls `ctest -N` for `--ctest-only` filtering) but still emits a regex-as-IPC contract instead of using exact names.
- Any future test name containing regex metacharacters, or any future divergence between executable basename and registered CTest name, reintroduces the drift.

## Acceptance criteria for a generic fix

The solution should make "CTest runs exactly the set that smart-build built" a **structural invariant**, not a property of careful string formatting. Suggested properties:

1. **Single source of truth** for the selected test set, consumed by every entry point (CI pipeline, local dev launcher, documentation examples). No script should re-derive the set from scratch.
2. **Exact-match selection at the CTest layer**, not a substring/regex contract that can over- or under-match. Any mechanism that enforces exact name equality is acceptable (`ctest --tests-from-file`, fixture-based driver, exact indices, etc.) — implementer's choice, but the chosen mechanism should be the only one in the tree.
3. **Fail fast on drift**: between build and test execution, the pipeline should assert that the count of CTest-runnable tests equals the count of selected tests, and abort with a clear message if not. This catches future regressions of *any* drift class, not just substring overmatch.
4. **Regression coverage**: a unit/integration test that selects a name which is a strict prefix of other registered test names and verifies that only the selected one is launched. Such a test would have caught PR #6761's failure.
5. **Documentation parity**: README snippets and any example Jenkinsfile/GitHub Actions blocks must use the same mechanism as the production scripts. No "two ways to consume `tests_to_run.json`."

## Affected files (for navigation, not as a fix proposal)

- `projects/composablekernel/script/dependency-parser/src/selective_test_filter.py`
- `projects/composablekernel/script/dependency-parser/smart_build_and_test.sh`
- `projects/composablekernel/script/dependency-parser/smart_build_ci.sh`
- `projects/composablekernel/script/dependency-parser/README.md`
- `projects/composablekernel/script/launch_tests.sh`
- `projects/composablekernel/script/dependency-parser/tests/`

## Impact

- Spurious CI failures on any PR whose selected test names are a strict prefix of other registered tests in the same CTest invocation. The collision pattern is common in CK because variant tests share long descriptive prefixes (`*_xdl_fp8`, `*_xdl_fp16`, `*_xdl_bf16`, etc.).
- Wasted developer time chasing "what did I break?" when the PR is fine.
- Erosion of trust in CI signal. Once reviewers learn that smart-build CI failures can be unrelated to the PR, real failures get rationalized away.

## References

- PR: https://github.com/ROCm/rocm-libraries/pull/6761
- Failing build: Jenkins job `users/zlakatos/ck/large_tensor_gemm_workaround` build #19
