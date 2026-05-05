---
title: "Quantization"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/quantization.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:49.930566+00:00
content_hash: "9bf0f7960298ea49"
---

# Quantization

## quantize_fp16

-
void migraphx::internal::quantize_fp16(
[program](program.html#_CPPv4N8migraphx8internal7programE) &prog, const std::vector<std::string> &ins_names = {"all"})


## quantize_bf16

-
void migraphx::internal::quantize_bf16(
[program](program.html#_CPPv4N8migraphx8internal7programE) &prog, const std::vector<std::string> &ins_names = {"all"})


## quantize_int8

-
void migraphx::internal::quantize_int8(
[program](program.html#_CPPv4N8migraphx8internal7programE) &prog, const [target](targets.html#_CPPv4N8migraphx8internal6targetE) &t, const std::vector<parameter_map> &calibration, const std::unordered_set<std::string> &ins_names = {"dot", "convolution"})
