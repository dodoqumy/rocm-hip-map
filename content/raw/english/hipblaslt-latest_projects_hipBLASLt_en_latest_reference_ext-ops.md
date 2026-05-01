---
title: "hipBLASLtExt operation API reference &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/ext-ops.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:53.916828+00:00
content_hash: "9012e6a8ce338ff2"
---

# hipBLASLtExt operation API reference[#](#hipblasltext-operation-api-reference)

hipBLASLt has the following extension operation APIs that are independent of GEMM operations. These extensions support the following:

`hipblasltExtSoftmax`

Softmax for 2D tensor. It performs softmax on the second dimension of input tensor and assumes the input is contiguous on the second dimension. For sample code, see

[Softmax for a 2D tensor](../samples/client_extop_softmax.html#client-extop-softmax).`hipblasltExtLayerNorm`

Converts a 2D tensor using LayerNorm to generate a new 2D normalized tensor. This is an independent function used to call and get the result. For sample code, see

[Converting a 2D tensor using LayerNorm](../samples/sample_hipblaslt_ext_op_layernorm.html#sample-hipblaslt-ext-op-layernorm).`hipblasltExtAMax`

Determines the absolute maximum value of a 2D tensor. This is an independent function used to call and get the result. For sample code, see

[Absolute maximum value of a 2D Tensor](../samples/sample_hipblaslt_ext_op_amax.html#sample-hipblaslt-ext-op-amax).

These APIs are explained in detail below.

## hipblasltExtSoftmax()[#](#hipblasltextsoftmax)

-
hipblasStatus_t hipblasltExtSoftmax(hipDataType datatype, uint32_t m, uint32_t n, uint32_t dim, void *output, void *input, hipStream_t stream)
[#](#_CPPv419hipblasltExtSoftmax11hipDataType8uint32_t8uint32_t8uint32_tPvPv11hipStream_t) Perform softmax on given tensor.

This function computes softmax on given 2D-tensor along specified dimension.

- Parameters:
**datatype**–**[in]**Datatype of input/output tensor, currently support HIP_R_32F only.**m**–**[in]**The first dimension of input/output tensor.**n**–**[in]**The second dimension of input/output tensor. Currently only values less than or equal to 256 are supported.**dim**–**[in]**Specified dimension to perform softmax on. Currently 1 is the only valid value.**input**–**[in]**input tensor buffer.**stream**–**[in]**The HIP stream where all the GPU work will be submitted.**output**–**[out]**output tensor buffer.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If it runs successfully.**HIPBLAS_STATUS_INVALID_VALUE**– If`n`

is greater than 256.**HIPBLAS_STATUS_NOT_SUPPORTED**– If`dim`

is not 1 or`datatype`

is not HIP_R_32F.



## hipblasltExtLayerNorm()[#](#hipblasltextlayernorm)

-
hipblasStatus_t hipblasltExtLayerNorm(hipDataType datatype, void *output, void *mean, void *invvar, void *input, uint32_t m, uint32_t n, float eps, void *gamma, void *beta, hipStream_t stream)
[#](#_CPPv421hipblasltExtLayerNorm11hipDataTypePvPvPvPv8uint32_t8uint32_tfPvPv11hipStream_t) Perform 2-D layernorm on with source input tensor and result output tensor.

This function computes layernorm on given 2D-tensor.

- Parameters:
**datatype**–**[in]**Datatype of input/output tensor, currently support HIP_R_32F only.**output**–**[out]**output tensor buffer. can’t be nullptr.**mean**–**[out]**tensor buffer. can’t be nullptr.**invvar**–**[out]**tensor buffer. 1 / sqrt(std). can’t be nullptr.**input**–**[in]**tensor buffer. can’t be nullptr.**m**–**[in]**The first dimension of input/output tensor.**n**–**[in]**The second dimension of input/output tensor.**eps**–**[in]**for sqrt to avoid inf value.**gamma**–**[in]**tensor buffer. nullptr means calculation doesn’t involve gamma.**beta**–**[in]**tensor buffer. nullptr means calculation doesn’t involve beta.**stream**–**[in]**The HIP stream where all the GPU work will be submitted.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If it runs successfully.**HIPBLAS_STATUS_INVALID_VALUE**– If`m`

is greater than 4096.**HIPBLAS_STATUS_NOT_SUPPORTED**– if`datatype`

is not HIP_R_32F.



## hipblasltExtAMax()[#](#hipblasltextamax)

-
hipblasStatus_t hipblasltExtAMax(const hipDataType datatype, const hipDataType outDatatype, void *output, void *input, uint32_t m, uint32_t n, hipStream_t stream)
[#](#_CPPv416hipblasltExtAMaxK11hipDataTypeK11hipDataTypePvPv8uint32_t8uint32_t11hipStream_t) Perform absmax on given 2-D tensor and output one value absmax(tensor) value.

This function computes amax on given 2D-tensor.

- Parameters:
**datatype**–**[in]**Datatype of input tensor, currently support HIP_R_32F and HIP_R_16F only.**outDatatype**–**[in]**Datatype of output tensor, currently support HIP_R_32F and HIP_R_16F only.**output**–**[out]**Amax tensor buffer. can’t be nullptr.**input**–**[in]**2-D tensor buffer. can’t be nullptr.**m**–**[in]**The first dimension of input/output tensor.**n**–**[in]**The second dimension of input/output tensor.**stream**–**[in]**The HIP stream where all the GPU work will be submitted.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If it runs successfully.**HIPBLAS_STATUS_INVALID_VALUE**– If`m`

or n is 0, or input or output is nullptr.**HIPBLAS_STATUS_NOT_SUPPORTED**– If`datatype`

is not (HIP_R_32F or HIP_R_16F).
