---
title: "Targets"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/targets.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:55.902350+00:00
content_hash: "dd4a30ed402f800c"
---

# Targets[#](#targets)

2025-10-14

3 min read time

## target[#](#target)

-
struct target
[#](#_CPPv4N8migraphx8internal6targetE) An interface for a compilation target.

Public Functions

-
std::string name() const
[#](#_CPPv4NK8migraphx8internal6target4nameEv) A unique name used to identify the target.


-
std::vector<
[pass](pass.html#_CPPv4N8migraphx4passE)> get_passes(context &ctx, const compile_options &options) const[#](#_CPPv4NK8migraphx8internal6target10get_passesER7contextRK15compile_options) The transformation pass to be run during compilation.

- Parameters:
**ctx**– This is the target-dependent context that is created by`get_context`

**options**– Compiling options passed in by the user

- Returns:
The passes to be ran



-
context get_context() const
[#](#_CPPv4NK8migraphx8internal6target11get_contextEv) Construct a context for the target.

- Returns:
The context to be used during compilation and execution.



-
supported_segments target_is_supported(T&, const_module_ref mod, support_metric metric) const
[#](#_CPPv4NK8migraphx8internal6target19target_is_supportedER1T16const_module_ref14support_metric) Get the ranges of instructions that are supported on a target.

- Parameters:
**module**– Module to check for supported instructions**metric**– Used to define how the quality of the support should be measured

- Returns:
the supported segments of the graph



-
[argument](data.html#_CPPv4N8migraphx8internal8argumentE)copy_to(const[argument](data.html#_CPPv4N8migraphx8internal8argumentE)&arg) const[#](#_CPPv4NK8migraphx8internal6target7copy_toERK8argument) copy an argument to the current target.

- Parameters:
**arg**– Input argument to be copied to the target- Returns:
Argument in the target.



-
std::string name() const

## gpu::target[#](#gpu-target)

-
struct target
[#](#_CPPv4N8migraphx8internal3gpu6targetE)

## cpu::target[#](#cpu-target)

-
struct target
[#](#_CPPv4N8migraphx8internal3cpu6targetE)
