---
title: "Passes"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/pass.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:37.038384+00:00
content_hash: "44e77b40fcd01628"
---

# Passes[#](#passes)

2025-10-14

3 min read time

## pass[#](#pass)

-
struct pass
[#](#_CPPv4N8migraphx4passE) An interface for applying a transformation to the instructions in a

`program`


## dead_code_elimination[#](#dead-code-elimination)

-
struct dead_code_elimination
[#](#_CPPv4N8migraphx8internal21dead_code_eliminationE) Remove instructions where the output is not used.


## eliminate_common_subexpression[#](#eliminate-common-subexpression)

-
struct eliminate_common_subexpression
[#](#_CPPv4N8migraphx8internal30eliminate_common_subexpressionE) Remove identical instructions.


## eliminate_concat[#](#eliminate-concat)

-
struct eliminate_concat
[#](#_CPPv4N8migraphx8internal16eliminate_concatE) Remove concat operators by having each operator can write to different chunk of memory.


## eliminate_contiguous[#](#eliminate-contiguous)

-
struct eliminate_contiguous
[#](#_CPPv4N8migraphx8internal20eliminate_contiguousE) Remove contiguous instructions by checking if the operator can use non-standard shapes.


## eliminate_identity[#](#eliminate-identity)

-
struct eliminate_identity
[#](#_CPPv4N8migraphx8internal18eliminate_identityE) Remove identity instructions. Currently when used as the last pass, it will preserve the semantics of previous program state, therefore dead code elimination should not be used afterwards.


## eliminate_pad[#](#eliminate-pad)

-
struct eliminate_pad
[#](#_CPPv4N8migraphx8internal13eliminate_padE) Remove pads if they can be written as an attribute to another op (im2col, convolution, pooling)


## propagate_constant[#](#propagate-constant)

-
struct propagate_constant
[#](#_CPPv4N8migraphx18propagate_constantE) Replace instructions which take all literals with a literal of the computation.


## rewrite_rnn[#](#rewrite-rnn)

-
struct rewrite_rnn
[#](#_CPPv4N8migraphx11rewrite_rnnE) Rewrite rnn to gemm and add.


## schedule[#](#schedule)

-
struct schedule
[#](#_CPPv4N8migraphx8scheduleE) Schedule instructions for concurrent execution


## simplify_algebra[#](#simplify-algebra)

-
struct simplify_algebra
[#](#_CPPv4N8migraphx16simplify_algebraE) Simplify many algebraic instructions to more efficient versions.


## simplify_reshapes[#](#simplify-reshapes)

-
struct simplify_reshapes
[#](#_CPPv4N8migraphx17simplify_reshapesE) Eliminate redundant reshapes.
