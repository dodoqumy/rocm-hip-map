---
title: "hipBLASLt datatypes reference &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/datatypes.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:13.187787+00:00
content_hash: "eeac0b53a11b7c39"
---

# hipBLASLt datatypes reference[#](#hipblaslt-datatypes-reference)

## hipblasLtEpilogue_t[#](#hipblasltepilogue-t)

-
enum hipblasLtEpilogue_t
[#](#_CPPv419hipblasLtEpilogue_t) Specify the enum type to set the postprocessing options for the epilogue.

*Values:*-
enumerator HIPBLASLT_EPILOGUE_DEFAULT
[#](#_CPPv4N19hipblasLtEpilogue_t26HIPBLASLT_EPILOGUE_DEFAULTE) No special postprocessing, just scale and quantize the results if necessary.


-
enumerator HIPBLASLT_EPILOGUE_RELU
[#](#_CPPv4N19hipblasLtEpilogue_t23HIPBLASLT_EPILOGUE_RELUE) Apply ReLU point-wise transform to the results:(x:=max(x, 0))


-
enumerator HIPBLASLT_EPILOGUE_BIAS
[#](#_CPPv4N19hipblasLtEpilogue_t23HIPBLASLT_EPILOGUE_BIASE) Apply (broadcast) bias from the bias vector. Bias vector length must match matrix D rows, and it must be packed (such as stride between vector elements is 1). Bias vector is broadcast to all columns and added before applying the final postprocessing.


-
enumerator HIPBLASLT_EPILOGUE_RELU_BIAS
[#](#_CPPv4N19hipblasLtEpilogue_t28HIPBLASLT_EPILOGUE_RELU_BIASE) Apply bias and then ReLU transform.


-
enumerator HIPBLASLT_EPILOGUE_GELU
[#](#_CPPv4N19hipblasLtEpilogue_t23HIPBLASLT_EPILOGUE_GELUE) Apply GELU point-wise transform to the results (x:=GELU(x)).


-
enumerator HIPBLASLT_EPILOGUE_GELU_BIAS
[#](#_CPPv4N19hipblasLtEpilogue_t28HIPBLASLT_EPILOGUE_GELU_BIASE) Apply Bias and then GELU transform.


-
enumerator HIPBLASLT_EPILOGUE_RELU_AUX
[#](#_CPPv4N19hipblasLtEpilogue_t27HIPBLASLT_EPILOGUE_RELU_AUXE) Output GEMM results before applying RELU transform.


-
enumerator HIPBLASLT_EPILOGUE_RELU_AUX_BIAS
[#](#_CPPv4N19hipblasLtEpilogue_t32HIPBLASLT_EPILOGUE_RELU_AUX_BIASE) Output GEMM results after applying bias but before applying RELU transform.


-
enumerator HIPBLASLT_EPILOGUE_GELU_AUX
[#](#_CPPv4N19hipblasLtEpilogue_t27HIPBLASLT_EPILOGUE_GELU_AUXE) Output GEMM results before applying GELU transform.


-
enumerator HIPBLASLT_EPILOGUE_GELU_AUX_BIAS
[#](#_CPPv4N19hipblasLtEpilogue_t32HIPBLASLT_EPILOGUE_GELU_AUX_BIASE) Output GEMM results after applying bias but before applying GELU transform.


-
enumerator HIPBLASLT_EPILOGUE_DGELU
[#](#_CPPv4N19hipblasLtEpilogue_t24HIPBLASLT_EPILOGUE_DGELUE) Apply gradient GELU transform. Requires additional aux input.


-
enumerator HIPBLASLT_EPILOGUE_DGELU_BGRAD
[#](#_CPPv4N19hipblasLtEpilogue_t30HIPBLASLT_EPILOGUE_DGELU_BGRADE) Apply gradient GELU transform and bias gradient to the results. Requires additional aux input.


-
enumerator HIPBLASLT_EPILOGUE_BGRADA
[#](#_CPPv4N19hipblasLtEpilogue_t25HIPBLASLT_EPILOGUE_BGRADAE) Apply bias gradient to A and output gemm result.


-
enumerator HIPBLASLT_EPILOGUE_BGRADB
[#](#_CPPv4N19hipblasLtEpilogue_t25HIPBLASLT_EPILOGUE_BGRADBE) Apply bias gradient to B and output gemm result.


-
enumerator HIPBLASLT_EPILOGUE_SWISH_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t28HIPBLASLT_EPILOGUE_SWISH_EXTE) Apply Swish point-wise transform to the results (x:=Swish(x, 1)).


-
enumerator HIPBLASLT_EPILOGUE_SWISH_BIAS_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t33HIPBLASLT_EPILOGUE_SWISH_BIAS_EXTE) Apply Bias and then Swish transform.


-
enumerator HIPBLASLT_EPILOGUE_CLAMP_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t28HIPBLASLT_EPILOGUE_CLAMP_EXTE) Apply point-wise clamp to the results (x:=max(alpha, min(x, beta))).


-
enumerator HIPBLASLT_EPILOGUE_CLAMP_BIAS_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t33HIPBLASLT_EPILOGUE_CLAMP_BIAS_EXTE) Apply Bias and then clamp.


-
enumerator HIPBLASLT_EPILOGUE_CLAMP_AUX_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t32HIPBLASLT_EPILOGUE_CLAMP_AUX_EXTE) Output GEMM results before applying clamp transform.


-
enumerator HIPBLASLT_EPILOGUE_CLAMP_AUX_BIAS_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t37HIPBLASLT_EPILOGUE_CLAMP_AUX_BIAS_EXTE) Output GEMM results after applying bias but before applying clamp transform.


-
enumerator HIPBLASLT_EPILOGUE_SIGMOID_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t30HIPBLASLT_EPILOGUE_SIGMOID_EXTE) Apply the sigmoid transform.


-
enumerator HIPBLASLT_EPILOGUE_SIGMOID_BIAS_EXT
[#](#_CPPv4N19hipblasLtEpilogue_t35HIPBLASLT_EPILOGUE_SIGMOID_BIAS_EXTE) Apply the bias followed by sigmoid transform.


-
enumerator HIPBLASLT_EPILOGUE_DEFAULT

## hipblasLtPointerMode_t[#](#hipblasltpointermode-t)

## hipblasLtHandle_t[#](#hipblaslthandle-t)

-
typedef void *hipblasLtHandle_t
[#](#_CPPv417hipblasLtHandle_t) Handle to the hipBLASLt library context queue.

The

`hipblasLtHandle_t`

type is a pointer type to an opaque structure holding the hipBLASLt library context. A handle encapsulates the execution state and manages device-side resources associated with the submitted operations.A hipBLASLt handle is not safe for concurrent use across multiple HIP streams. Applications must ensure any previously submitted work associated with a handle has completed before reusing that handle on a different stream. For multi-stream execution, create one handle per stream.

Use the following functions to manipulate this library context:

[hipblasLtCreate()](api-reference.html#group__library__module_1ga8f48ee6fa147ddc87c2b6278016e8bd7): To initialize the hipBLASLt library context and return a handle to an opaque structure holding the hipBLASLt library context.[hipblasLtDestroy()](api-reference.html#group__library__module_1ga22b16d7255e78eb223d332957b4c6e80): To destroy a previously created hipBLASLt library context descriptor and release the resources.

## hipblasLtMatmulAlgo_t[#](#hipblasltmatmulalgo-t)

-
struct hipblasLtMatmulAlgo_t
[#](#_CPPv421hipblasLtMatmulAlgo_t) Description of the matrix multiplication algorithm.

This is an opaque structure holding the description of the matrix multiplication algorithm. This structure can be trivially serialized and later restored for use with the same version of hipBLASLt library to save on selecting the right configuration again.


## hipblasLtMatmulDesc_t[#](#hipblasltmatmuldesc-t)

-
typedef hipblasLtMatmulDescOpaque_t *hipblasLtMatmulDesc_t
[#](#_CPPv421hipblasLtMatmulDesc_t) Descriptor of the matrix multiplication operation.

This is a pointer to an opaque structure holding the description of the matrix multiplication operation

[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d). Use the following functions to manipulate this descriptor:[hipblasLtMatmulDescCreate()](api-reference.html#group__library__module_1ga58985f13b6e744a8e6c400e8936edaeb): To create one instance of the descriptor.[hipblasLtMatmulDescDestroy()](api-reference.html#group__library__module_1ga9eaf0f51f22408d96557d0424dedf87a): To destroy a previously created descriptor and release the resources.

## hipblasLtOrder_t[#](#hipblasltorder-t)

-
enum hipblasLtOrder_t
[#](#_CPPv416hipblasLtOrder_t) Enum for data ordering.

*Values:*-
enumerator HIPBLASLT_ORDER_COL
[#](#_CPPv4N16hipblasLtOrder_t19HIPBLASLT_ORDER_COLE) Column-major

Leading dimension is the stride (in elements) to the beginning of next column in memory.


-
enumerator HIPBLASLT_ORDER_ROW
[#](#_CPPv4N16hipblasLtOrder_t19HIPBLASLT_ORDER_ROWE) Row major

Leading dimension is the stride (in elements) to the beginning of next row in memory.


-
enumerator HIPBLASLT_ORDER_COL16_4R16
[#](#_CPPv4N16hipblasLtOrder_t26HIPBLASLT_ORDER_COL16_4R16E) Data is ordered in column-major ordered tiles of composite tiles with total 16 columns and 64 rows. A tile is composed of 4 inner tiles in column-major with total 16 rows and 16 columns. Element offset within the tile is calculated as row%16+16*col+(row/16)*16*16. Note that for this order, the number of columns(rows) of the tensor has to be multiple of 16(64) or pre-padded to 16(64).


-
enumerator HIPBLASLT_ORDER_COL16_4R8
[#](#_CPPv4N16hipblasLtOrder_t25HIPBLASLT_ORDER_COL16_4R8E) Data is ordered in column-major ordered tiles of composite tiles with total 16 columns and 32 rows. A tile is composed of 4 inner tiles in column-major with total 8 rows and 16 columns. Element offset within the tile is calculated as row%8+8*col+(row/8)*16*8. Note that for this order, the number of columns(rows) of the tensor has to be multiple of 16(32) or pre-padded to 16(32).


-
enumerator HIPBLASLT_ORDER_COL16_4R4
[#](#_CPPv4N16hipblasLtOrder_t25HIPBLASLT_ORDER_COL16_4R4E)

-
enumerator HIPBLASLT_ORDER_COL16_4R2
[#](#_CPPv4N16hipblasLtOrder_t25HIPBLASLT_ORDER_COL16_4R2E)

-
enumerator HIPBLASLT_ORDER_COL

## hipblasLtMatmulDescAttributes_t[#](#hipblasltmatmuldescattributes-t)

-
enum hipblasLtMatmulDescAttributes_t
[#](#_CPPv431hipblasLtMatmulDescAttributes_t) Specify the attributes that define the specifics of the matrix multiply operation.

*Values:*-
enumerator HIPBLASLT_MATMUL_DESC_TRANSA
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t28HIPBLASLT_MATMUL_DESC_TRANSAE) Specifies the type of transformation operation that should be performed on matrix A. Default value is HIPBLAS_OP_N (for example, non-transpose operation). See hipblasOperation_t. Data Type:int32_t


-
enumerator HIPBLASLT_MATMUL_DESC_TRANSB
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t28HIPBLASLT_MATMUL_DESC_TRANSBE) Specifies the type of transformation operation that should be performed on matrix B. Default value is HIPBLAS_OP_N (for example, non-transpose operation). See hipblasOperation_t. Data Type:int32_t


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t30HIPBLASLT_MATMUL_DESC_EPILOGUEE) Epilogue function. See hipblasLtEpilogue_t. Default value is: HIPBLASLT_EPILOGUE_DEFAULT. Data Type: uint32_t


-
enumerator HIPBLASLT_MATMUL_DESC_BIAS_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t34HIPBLASLT_MATMUL_DESC_BIAS_POINTERE) Bias or Bias gradient vector pointer in the device memory. Data Type:void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_BIAS_DATA_TYPE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t36HIPBLASLT_MATMUL_DESC_BIAS_DATA_TYPEE) Type of the bias vector in the device memory. Can be set same as D matrix type or Scale type. Bias case: see HIPBLASLT_EPILOGUE_BIAS. Data Type:int32_t based on hipDataType


-
enumerator HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t37HIPBLASLT_MATMUL_DESC_A_SCALE_POINTERE) Device pointer to the scale factor value that converts data in matrix A to the compute data type range. The scaling factor must have the same type as the compute type. If not specified, or set to NULL, the scaling factor is assumed to be 1. If set for an unsupported matrix data, scale, and compute type combination, calling

[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d)will return HIPBLAS_INVALID_VALUE. Default value: NULL Data Type: void* /const void*

-
enumerator HIPBLASLT_MATMUL_DESC_B_SCALE_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t37HIPBLASLT_MATMUL_DESC_B_SCALE_POINTERE) Equivalent to HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER for matrix B. Default value: NULL Type: void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_C_SCALE_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t37HIPBLASLT_MATMUL_DESC_C_SCALE_POINTERE) Equivalent to HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER for matrix C. Default value: NULL Type: void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_D_SCALE_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t37HIPBLASLT_MATMUL_DESC_D_SCALE_POINTERE) Equivalent to HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER for matrix D. Default value: NULL Type: void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_SCALE_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t48HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_SCALE_POINTERE) Equivalent to HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER for matrix AUX. Default value: NULL Type: void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t42HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_POINTERE) Epilogue auxiliary buffer pointer in the device memory. Data Type:void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_LD
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t37HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_LDE) The leading dimension of the epilogue auxiliary buffer pointer in the device memory. Data Type:int64_t


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_BATCH_STRIDE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t47HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_BATCH_STRIDEE) The batch stride of the epilogue auxiliary buffer pointer in the device memory. Data Type:int64_t


-
enumerator HIPBLASLT_MATMUL_DESC_POINTER_MODE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t34HIPBLASLT_MATMUL_DESC_POINTER_MODEE) Specifies alpha and beta are passed by reference, whether they are scalars on the host or on the device, or device vectors. Default value is: HIPBLASLT_POINTER_MODE_HOST (i.e., on the host). Data Type: int32_t based on hipblasLtPointerMode_t


-
enumerator HIPBLASLT_MATMUL_DESC_AMAX_D_POINTER
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t36HIPBLASLT_MATMUL_DESC_AMAX_D_POINTERE) Device pointer to the memory location that on completion will be set to the maximum of absolute values in the output matrix. Data Type:void* /const void*


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_DATA_TYPE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t44HIPBLASLT_MATMUL_DESC_EPILOGUE_AUX_DATA_TYPEE) Type of the aux vector in the device memory. Default value is: HIPBLASLT_DATATYPE_INVALID (using D matrix type). Data Type:int32_t based on hipDataType


-
enumerator HIPBLASLT_MATMUL_DESC_A_SCALE_MODE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t34HIPBLASLT_MATMUL_DESC_A_SCALE_MODEE) Scaling mode that defines how the matrix scaling factor for matrix A is interpreted. See hipblasLtMatmulMatrixScale_t


-
enumerator HIPBLASLT_MATMUL_DESC_B_SCALE_MODE
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t34HIPBLASLT_MATMUL_DESC_B_SCALE_MODEE) Scaling mode that defines how the matrix scaling factor for matrix B is interpreted. See hipblasLtMatmulMatrixScale_t


-
enumerator HIPBLASLT_MATMUL_DESC_COMPUTE_INPUT_TYPE_A_EXT
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t46HIPBLASLT_MATMUL_DESC_COMPUTE_INPUT_TYPE_A_EXTE) Compute input A types. Defines the data type used for the input A of matrix multiply.


-
enumerator HIPBLASLT_MATMUL_DESC_COMPUTE_INPUT_TYPE_B_EXT
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t46HIPBLASLT_MATMUL_DESC_COMPUTE_INPUT_TYPE_B_EXTE) Compute input B types. Defines the data type used for the input B of matrix multiply.


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_ACT_ARG0_EXT
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t43HIPBLASLT_MATMUL_DESC_EPILOGUE_ACT_ARG0_EXTE) first extra argument for the activation function. Data Type: float


-
enumerator HIPBLASLT_MATMUL_DESC_EPILOGUE_ACT_ARG1_EXT
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t43HIPBLASLT_MATMUL_DESC_EPILOGUE_ACT_ARG1_EXTE) second extra argument for the activation function. Data Type: float


-
enumerator HIPBLASLT_MATMUL_DESC_MAX
[#](#_CPPv4N31hipblasLtMatmulDescAttributes_t25HIPBLASLT_MATMUL_DESC_MAXE)

-
enumerator HIPBLASLT_MATMUL_DESC_TRANSA

## hipblasLtMatmulHeuristicResult_t[#](#hipblasltmatmulheuristicresult-t)

-
struct hipblasLtMatmulHeuristicResult_t
[#](#_CPPv432hipblasLtMatmulHeuristicResult_t) Description of the matrix multiplication algorithm.

This is a descriptor that holds the configured matrix multiplication algorithm descriptor and its runtime properties. This structure can be trivially serialized and later restored for use with the same version of hipBLASLt library to save on selecting the right configuration again.

- Param algo:
[hipblasLtMatmulAlgo_t](#structhipblas_lt_matmul_algo__t)struct- Param workspaceSize:
Actual size of workspace memory required

- Param state:
Result status. Other fields are valid only if, after call to

[hipblasLtMatmulAlgoGetHeuristic()](api-reference.html#group__library__module_1ga1bd22d6bb579baf5cb35c1a5b4df18c5), this member is set to HIPBLAS_STATUS_SUCCESS


## hipblasLtMatmulPreference_t[#](#hipblasltmatmulpreference-t)

-
typedef hipblasLtMatmulPreferenceOpaque_t *hipblasLtMatmulPreference_t
[#](#_CPPv427hipblasLtMatmulPreference_t) Descriptor of the matrix multiplication preference.

This is a pointer to an opaque structure holding the description of the preferences for

[hipblasLtMatmulAlgoGetHeuristic()](api-reference.html#group__library__module_1ga1bd22d6bb579baf5cb35c1a5b4df18c5)configuration. Use the following functions to manipulate this descriptor:[hipblasLtMatmulPreferenceCreate()](api-reference.html#group__library__module_1ga11f3921ce35e7d6ae739e901d12040f5): To create one instance of the descriptor.[hipblasLtMatmulPreferenceDestroy()](api-reference.html#group__library__module_1ga653735e31c6ba5fae4c0fde8a23cfc2c): To destroy a previously created descriptor and release the resources.

## hipblasLtMatmulPreferenceAttributes_t[#](#hipblasltmatmulpreferenceattributes-t)

-
enum hipblasLtMatmulPreferenceAttributes_t
[#](#_CPPv437hipblasLtMatmulPreferenceAttributes_t) It is an enumerated type used to apply algorithm search preferences while fine-tuning the heuristic function.

*Values:*-
enumerator HIPBLASLT_MATMUL_PREF_SEARCH_MODE
[#](#_CPPv4N37hipblasLtMatmulPreferenceAttributes_t33HIPBLASLT_MATMUL_PREF_SEARCH_MODEE) Search mode. Data Type: uint32_t


-
enumerator HIPBLASLT_MATMUL_PREF_MAX_WORKSPACE_BYTES
[#](#_CPPv4N37hipblasLtMatmulPreferenceAttributes_t41HIPBLASLT_MATMUL_PREF_MAX_WORKSPACE_BYTESE) Maximum allowed workspace memory. Default is 0 (no workspace memory allowed). Data Type: uint64_t


-
enumerator HIPBLASLT_MATMUL_PREF_MAX
[#](#_CPPv4N37hipblasLtMatmulPreferenceAttributes_t25HIPBLASLT_MATMUL_PREF_MAXE)

-
enumerator HIPBLASLT_MATMUL_PREF_SEARCH_MODE

## hipblasLtMatmulMatrixScale_t[#](#hipblasltmatmulmatrixscale-t)

-
enum hipblasLtMatmulMatrixScale_t
[#](#_CPPv428hipblasLtMatmulMatrixScale_t) Block scale mode for A and B.

*Values:*-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_SCALAR_32F
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t40HIPBLASLT_MATMUL_MATRIX_SCALE_SCALAR_32FE) Scaling factors are single-precision scalars applied to the whole tensors (this mode is the default for fp8).


-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_VEC16_UE4M3
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t41HIPBLASLT_MATMUL_MATRIX_SCALE_VEC16_UE4M3E) Not supported yet. Scaling factors are tensors that contain a dedicated scaling factor stored as an 8-bit HIP_R_8F_E4M3 value for each 16-element block in the innermost dimension of the corresponding data tensor.


-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_VEC32_UE8M0
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t41HIPBLASLT_MATMUL_MATRIX_SCALE_VEC32_UE8M0E) Scaling factors are tensors that contain a dedicated scaling factor stored as an 8-bit R_8F_UE8M0 value for each 32-element block in the innermost dimension of the corresponding data tensor.


-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_OUTER_VEC_32F
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t43HIPBLASLT_MATMUL_MATRIX_SCALE_OUTER_VEC_32FE) Scaling factors are single-precision vectors. This mode is only applicable to matrices A and B, in which case the vectors are expected to have M and N elements respectively, and each (i, j)-th element of product of A and B is multiplied by i-th element of A scale and j-th element of B scale.


-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_VEC128_32F
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t40HIPBLASLT_MATMUL_MATRIX_SCALE_VEC128_32FE) Not supported yet. Scaling factors are tensors that contain a dedicated FP32 scaling factor for each 128-element block in the innermost dimension of the corresponding data tensor


-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_BLK128x128_32F
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t44HIPBLASLT_MATMUL_MATRIX_SCALE_BLK128x128_32FE) Not supported yet. Scaling factors are tensors that contain a dedicated FP32 scaling factor for each 128x128-element block in the corresponding data tensor


-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_END
[#](#_CPPv4N28hipblasLtMatmulMatrixScale_t33HIPBLASLT_MATMUL_MATRIX_SCALE_ENDE)

-
enumerator HIPBLASLT_MATMUL_MATRIX_SCALE_SCALAR_32F

## hipblasLtMatrixLayout_t[#](#hipblasltmatrixlayout-t)

-
typedef hipblasLtMatrixLayoutOpaque_t *hipblasLtMatrixLayout_t
[#](#_CPPv423hipblasLtMatrixLayout_t) Descriptor of the matrix layout.

This is a pointer to an opaque structure holding the description of a matrix layout. Use the following functions to manipulate this descriptor:

[hipblasLtMatrixLayoutCreate()](api-reference.html#group__library__module_1ga1fe8371b1d02049687883b72e62a44ad): To create one instance of the descriptor.[hipblasLtMatrixLayoutDestroy()](api-reference.html#group__library__module_1ga32ab427d92d81c093562eeea667826fa): To destroy a previously created descriptor and release the resources.

## hipblasLtMatrixLayoutAttribute_t[#](#hipblasltmatrixlayoutattribute-t)

-
enum hipblasLtMatrixLayoutAttribute_t
[#](#_CPPv432hipblasLtMatrixLayoutAttribute_t) Specify the attributes that define the details of the matrix.

*Values:*-
enumerator HIPBLASLT_MATRIX_LAYOUT_BATCH_COUNT
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t35HIPBLASLT_MATRIX_LAYOUT_BATCH_COUNTE) Number of batch of this matrix. Default value is 1. Data Type: int32_t


-
enumerator HIPBLASLT_MATRIX_LAYOUT_STRIDED_BATCH_OFFSET
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t44HIPBLASLT_MATRIX_LAYOUT_STRIDED_BATCH_OFFSETE) Stride (in elements) to the next matrix for the strided batch operation. Default value is 0. Data Type: int64_t


-
enumerator HIPBLASLT_MATRIX_LAYOUT_TYPE
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t28HIPBLASLT_MATRIX_LAYOUT_TYPEE) Data type, see hipDataType.

uint32_t


-
enumerator HIPBLASLT_MATRIX_LAYOUT_ORDER
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t29HIPBLASLT_MATRIX_LAYOUT_ORDERE) Memory order of the data, see hipblasLtOrder_t.

int32_t, default: HIPBLASLT_ORDER_COL


-
enumerator HIPBLASLT_MATRIX_LAYOUT_ROWS
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t28HIPBLASLT_MATRIX_LAYOUT_ROWSE) Number of rows.

Usually only values that can be expressed as int32_t are supported.

uint64_t


-
enumerator HIPBLASLT_MATRIX_LAYOUT_COLS
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t28HIPBLASLT_MATRIX_LAYOUT_COLSE) Number of columns.

Usually only values that can be expressed as int32_t are supported.

uint64_t


-
enumerator HIPBLASLT_MATRIX_LAYOUT_LD
[#](#_CPPv4N32hipblasLtMatrixLayoutAttribute_t26HIPBLASLT_MATRIX_LAYOUT_LDE) Matrix leading dimension.

For HIPBLASLT_ORDER_COL this is stride (in elements) of matrix column, for more details and documentation for other memory orders see documentation for hipblasLtOrder_t values.

Currently only non-negative values are supported, must be large enough so that matrix memory locations are not overlapping (e.g. greater or equal to HIPBLASLT_MATRIX_LAYOUT_ROWS in case of HIPBLASLT_ORDER_COL).

int64_t;


-
enumerator HIPBLASLT_MATRIX_LAYOUT_BATCH_COUNT

## hipblasLtMatrixTransformDesc_t[#](#hipblasltmatrixtransformdesc-t)

-
typedef hipblasLtMatrixTransformDescOpaque_t *hipblasLtMatrixTransformDesc_t
[#](#_CPPv430hipblasLtMatrixTransformDesc_t) Opaque descriptor for

[hipblasLtMatrixTransform()](api-reference.html#group__library__module_1ga3ba8632f4440718ef830dfa70aa2d0c4)operation details.The hipblasLtMatrixTransformDesc_t is a pointer to an opaque structure holding the description of a matrix transformation operation.

[hipblasLtMatrixTransformDescCreate()](api-reference.html#hipblaslt_8h_1a0b4a79dedc3d2ca8cd1b8a56c05e947f): To create one instance of the descriptor.[hipblasLtMatrixTransformDescDestroy()](api-reference.html#hipblaslt_8h_1ac74774a9d6b4c64dc08871b34261c0b4): To destroy a previously created descriptor and release the resources.
