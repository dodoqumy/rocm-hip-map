---
title: "hipBLASLtExt API reference &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/ext-reference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:48.202160+00:00
content_hash: "64b71ebbae9f48f2"
---

# hipBLASLtExt API reference[#](#hipblasltext-api-reference)

hipBLASLt contains extension APIs with the namespace `hipblaslt_ext`

. They are only C++ compatible. The extensions support the following:

## hipBLASLtExt datatypes reference[#](#hipblasltext-datatypes-reference)

### GemmType[#](#gemmtype)

### GemmProblemType[#](#gemmproblemtype)

-
class GemmProblemType
[#](#_CPPv4N13hipblaslt_ext15GemmProblemTypeE) hipblasLt extension ProblemType for gemm problems.

This structure sets the problem type of a gemm problem.

Public Functions

-
void setOpA(
[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)op)[#](#_CPPv4N13hipblaslt_ext15GemmProblemType6setOpAE18hipblasOperation_t) Set the A martix transpose.


-
void setOpB(
[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)op)[#](#_CPPv4N13hipblaslt_ext15GemmProblemType6setOpBE18hipblasOperation_t) Set the B matrix transpose.


-
void setTypeA(hipDataType type)
[#](#_CPPv4N13hipblaslt_ext15GemmProblemType8setTypeAE11hipDataType) Set the A matrix datatype.


-
void setTypeB(hipDataType type)
[#](#_CPPv4N13hipblaslt_ext15GemmProblemType8setTypeBE11hipDataType) Set the B matrix datatype.


-
void setTypeC(hipDataType type)
[#](#_CPPv4N13hipblaslt_ext15GemmProblemType8setTypeCE11hipDataType) Set the C matrix datatype.


-
void setTypeD(hipDataType type)
[#](#_CPPv4N13hipblaslt_ext15GemmProblemType8setTypeDE11hipDataType) Set the D matrix datatype.


-
void setTypeCompute(hipblasComputeType_t type)
[#](#_CPPv4N13hipblaslt_ext15GemmProblemType14setTypeComputeE20hipblasComputeType_t) Set the compute datatype.


-
void setOrderA(
[hipblasLtOrder_t](datatypes.html#_CPPv416hipblasLtOrder_t)order)[#](#_CPPv4N13hipblaslt_ext15GemmProblemType9setOrderAE16hipblasLtOrder_t) Set the A martix data order.


-
void setOrderB(
[hipblasLtOrder_t](datatypes.html#_CPPv416hipblasLtOrder_t)order)[#](#_CPPv4N13hipblaslt_ext15GemmProblemType9setOrderBE16hipblasLtOrder_t) Set the B matrix data order.


-
[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)getOpA() const[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType6getOpAEv) The A matrix transpose.


-
[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)getOpB() const[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType6getOpBEv) The B matrix transpose.


-
hipDataType getTypeA() const
[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType8getTypeAEv) The A matrix datatype.


-
hipDataType getTypeB() const
[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType8getTypeBEv) The B matrix datatype.


-
hipDataType getTypeC() const
[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType8getTypeCEv) The C matrix datatype.


-
hipDataType getTypeD() const
[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType8getTypeDEv) The D matrix datatype.


-
hipblasComputeType_t getTypeCompute() const
[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType14getTypeComputeEv) The compute datatype.


-
[hipblasLtOrder_t](datatypes.html#_CPPv416hipblasLtOrder_t)getOrderA() const[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType9getOrderAEv) The A matrix data order.


-
[hipblasLtOrder_t](datatypes.html#_CPPv416hipblasLtOrder_t)getOrderB() const[#](#_CPPv4NK13hipblaslt_ext15GemmProblemType9getOrderBEv) The B matrix data order.


-
void setOpA(

### GemmEpilogue[#](#gemmepilogue)

-
class GemmEpilogue
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogueE) hipblasLt extension Epilogue for gemm problems.

This class sets the epilogue of a gemm problem.

Public Functions

-
void setMode(
[hipblasLtEpilogue_t](datatypes.html#_CPPv419hipblasLtEpilogue_t)mode)[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue7setModeE19hipblasLtEpilogue_t) Set the mode of epilogue. Default is gemm.


-
void setBiasDataType(hipDataType biasDataType)
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue15setBiasDataTypeE11hipDataType) Set the bias datatype. Only works if mode is set to bias related epilogues.


-
void setAuxDataType(hipDataType auxDataType)
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue14setAuxDataTypeE11hipDataType) Set the aux datatype. Only works if mode is set to aux related epilogues.


-
void setAuxLeadingDimension(int auxLeadingDimension)
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue22setAuxLeadingDimensionEi) Set the aux leading dimension. Only works if mode is set to aux related epilogues.


-
void setAuxBatchStride(int auxBatchStride)
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue17setAuxBatchStrideEi) Set the aux batch stride. Only works if mode is set to aux related epilogues.


-
void setScalingAType(
[hipblasLtMatmulMatrixScale_t](datatypes.html#_CPPv428hipblasLtMatmulMatrixScale_t)scalingAType)[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue15setScalingATypeE28hipblasLtMatmulMatrixScale_t) Only works if DataTypeA = DataTypeB = FP8.


-
void setScalingBType(
[hipblasLtMatmulMatrixScale_t](datatypes.html#_CPPv428hipblasLtMatmulMatrixScale_t)scalingBType)[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue15setScalingBTypeE28hipblasLtMatmulMatrixScale_t) Only works if DataTypeA = DataTypeB = FP8.


-
void setAct0(float act0)
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue7setAct0Ef) Set first extra argument for activation function.


-
void setAct1(float act1)
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue7setAct1Ef) Set second extra argument for activation function.


-
[hipblasLtEpilogue_t](datatypes.html#_CPPv419hipblasLtEpilogue_t)getMode() const[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue7getModeEv) The mode of epilogue. Default is gemm.


-
hipDataType getBiasDataType() const
[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue15getBiasDataTypeEv) The bias datatype. Only works if mode is set to bias related epilogues.


-
hipDataType getAuxDataType() const
[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue14getAuxDataTypeEv) The aux datatype. Only works if mode is set to aux related epilogues.


-
int getAuxLeadingDimension() const
[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue22getAuxLeadingDimensionEv) The aux leading dimension. Only works if mode is set to aux related epilogues.


-
int getAuxBatchStride() const
[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue17getAuxBatchStrideEv) The aux batch stride. Only works if mode is set to aux related epilogues.


-
[hipblasLtMatmulMatrixScale_t](datatypes.html#_CPPv428hipblasLtMatmulMatrixScale_t)getScalingAType() const[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue15getScalingATypeEv) 0 is scalar, 1 is vector. Only works if DataTypeA = DataTypeB = FP8.


-
[hipblasLtMatmulMatrixScale_t](datatypes.html#_CPPv428hipblasLtMatmulMatrixScale_t)getScalingBType() const[#](#_CPPv4NK13hipblaslt_ext12GemmEpilogue15getScalingBTypeEv) 0 is scalar, 1 is vector. Only works if DataTypeA = DataTypeB = FP8.


-
float getAct0()
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue7getAct0Ev) first extra argument for activation function.


-
float getAct1()
[#](#_CPPv4N13hipblaslt_ext12GemmEpilogue7getAct1Ev) second extra argument for activation function.


-
void setMode(

### GemmInputs[#](#gemminputs)

-
class GemmInputs
[#](#_CPPv4N13hipblaslt_ext10GemmInputsE) hipblasLt extension Inputs for gemm problems.

This class sets the input pointers of a gemm problem.

Public Functions

-
void setA(const void *a)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs4setAEPKv) Set the a matrix input pointer.


-
void setB(const void *b)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs4setBEPKv) Set the b matrix input pointer.


-
void setC(const void *c)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs4setCEPKv) Set the c matrix input pointer.


-
void setD(const void *d)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs4setDEPKv) Set the d matrix input pointer.


-
void setAlpha(const void *alpha)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs8setAlphaEPKv) Set the alpha value.


-
void setBeta(const void *beta)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs7setBetaEPKv) Set the beta value.


-
void setBias(const void *bias)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs7setBiasEPKv) Set the bias input pointer.


-
void setScaleA(const void *scaleA)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs9setScaleAEPKv) Set the Scale A input pointer.


-
void setScaleB(const void *scaleB)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs9setScaleBEPKv) Set the Scale B input pointer.


-
void setScaleC(const void *scaleC)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs9setScaleCEPKv) Set the Scale C input pointer.


-
void setScaleD(const void *scaleD)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs9setScaleDEPKv) Set the Scale D input pointer.


-
void setScaleAux(const void *scaleAux)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs11setScaleAuxEPKv) Set the Scale AUX input pointer.


-
void setScaleAlphaVec(const void *scaleAlphaVec)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs16setScaleAlphaVecEPKv) Set the scaleAlpha vector input pointer.


-
void setAux(const void *aux)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs6setAuxEPKv) Set the aux input pointer.


-
void setAmaxD(const void *amaxD)
[#](#_CPPv4N13hipblaslt_ext10GemmInputs8setAmaxDEPKv) Set the AmaxD input pointer.


-
const void *getA() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs4getAEv) The a matrix input pointer.


-
const void *getB() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs4getBEv) The b matrix input pointer.


-
const void *getC() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs4getCEv) The c matrix input pointer.


-
const void *getD() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs4getDEv) The d matrix input pointer.


-
const void *getAlpha() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs8getAlphaEv) The alpha value.


-
const void *getBeta() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs7getBetaEv) The beta value.


-
const void *getBias() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs7getBiasEv) The bias input pointer.


-
const void *getScaleA() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs9getScaleAEv) The Scale A input pointer.


-
const void *getScaleB() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs9getScaleBEv) The Scale B input pointer.


-
const void *getScaleC() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs9getScaleCEv) The Scale C input pointer.


-
const void *getScaleD() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs9getScaleDEv) The Scale D input pointer.


-
const void *getScaleAux() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs11getScaleAuxEv) The Scale AUX input pointer.


-
const void *getScaleAlphaVec() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs16getScaleAlphaVecEv) The scaleAlpha vector input pointer.


-
const void *getAux() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs6getAuxEv) The aux input pointer.


-
const void *getAmaxD() const
[#](#_CPPv4NK13hipblaslt_ext10GemmInputs8getAmaxDEv) The AmaxD input pointer.


-
void setA(const void *a)

## hipBLASLtExt GEMM class reference[#](#hipblasltext-gemm-class-reference)

### GemmPreference[#](#gemmpreference)

-
class GemmPreference
[#](#_CPPv4N13hipblaslt_ext14GemmPreferenceE) hipblasLt extension preference for gemm problems.

Currently only supports setting max workspace size.

Public Functions

-
void setMaxWorkspaceBytes(size_t workspaceBytes)
[#](#_CPPv4N13hipblaslt_ext14GemmPreference20setMaxWorkspaceBytesE6size_t) This function sets the max workspace size.

- Parameters:
**workspaceBytes**–**[in]**Set the max workspace size in bytes.


-
const size_t getMaxWorkspaceBytes() const
[#](#_CPPv4NK13hipblaslt_ext14GemmPreference20getMaxWorkspaceBytesEv) This function returns the set max workspace size.

- Return values:
**size_t**– Returns the set max workspace size.


-
void setMaxWorkspaceBytes(size_t workspaceBytes)

### GemmInstance[#](#gemminstance)

-
class GemmInstance
[#](#_CPPv4N13hipblaslt_ext12GemmInstanceE) hipblasLt extension instance for gemm problems.

Subclassed by

[hipblaslt_ext::Gemm](#classhipblaslt__ext_1_1_gemm),[hipblaslt_ext::GroupedGemm](#classhipblaslt__ext_1_1_grouped_gemm)Public Functions

-
hipblasStatus_t algoGetHeuristic(const int requestedAlgoCount, const
[GemmPreference](#_CPPv4N13hipblaslt_ext14GemmPreferenceE)&pref, std::vector<[hipblasLtMatmulHeuristicResult_t](datatypes.html#_CPPv432hipblasLtMatmulHeuristicResult_t)> &heuristicResults)[#](#_CPPv4N13hipblaslt_ext12GemmInstance16algoGetHeuristicEKiRK14GemmPreferenceRNSt6vectorI32hipblasLtMatmulHeuristicResult_tEE) Retrieve the possible algorithms.

This function retrieves the possible algorithms for the matrix multiply operation

[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d)function with the given data and compute tpye. The output is placed in heuristicResult in the order of increasing estimated compute time.- Parameters:
**requestedAlgoCount**–**[in]**number of requested algorithms.**pref**–**[in]**hipblasLt extension preference for gemm problems.**heuristicResults**–**[out]**The algorithm heuristic vector.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. Inspect heuristicResults.size > 0, but may heuristicResults.size < requestedAlgoCount state for the status of the results.**HIPBLAS_STATUS_NOT_SUPPORTED**– If no heuristic function available for current configuration.**HIPBLAS_STATUS_INVALID_VALUE**– If no solution is found.



-
hipblasStatus_t isAlgoSupported(
[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)&algo, size_t &workspaceSizeInBytes)[#](#_CPPv4N13hipblaslt_ext12GemmInstance15isAlgoSupportedER21hipblasLtMatmulAlgo_tR6size_t) Check if the algorithm supports the problem. (For hipblaslt extension API)

This function updates the problem saved inside the algorithm if the problem is supported. The required workspaceSizeInBytes is also returned.

- Parameters:
**algo**–**[in]**The algorithm heuristic.**workspaceSizeInBytes**–**[out]**Return the required workspace size.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. The problem is supported by the algorithm. results.**HIPBLAS_STATUS_INVALID_VALUE**– The problem is not supported.



-
hipblasStatus_t isAlgoSupported(
[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)&algo, GemmTuning &tuning, size_t &workspaceSizeInBytes)[#](#_CPPv4N13hipblaslt_ext12GemmInstance15isAlgoSupportedER21hipblasLtMatmulAlgo_tR10GemmTuningR6size_t) Check if the algorithm supports the problem. (For hipblaslt extension API)

This function updates the problem saved inside the algorithm if the problem is supported. The required workspaceSizeInBytes is also returned.

- Parameters:
**algo**–**[in]**The algorithm heuristic.**tuning**–**[in]**The tuning parameters.**workspaceSizeInBytes**–**[out]**Return the required workspace size.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. The problem is supported by the algorithm. results.**HIPBLAS_STATUS_INVALID_VALUE**– The problem is not supported.



-
void setMaxWorkspaceBytes(size_t workspaceBytes)
[#](#_CPPv4N13hipblaslt_ext12GemmInstance20setMaxWorkspaceBytesE6size_t) This function sets the max workspace size.

- Parameters:
**workspaceBytes**–**[in]**Set the max workspace size in bytes.


-
const size_t getMaxWorkspaceBytes() const
[#](#_CPPv4NK13hipblaslt_ext12GemmInstance20getMaxWorkspaceBytesEv) This function returns the set max workspace size.

- Return values:
**size_t**– Returns the set max workspace size.


-
hipblasStatus_t initialize(const
[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)&algo, void *workspace, bool useUserArgs = true, hipStream_t stream = 0)[#](#_CPPv4N13hipblaslt_ext12GemmInstance10initializeERK21hipblasLtMatmulAlgo_tPvb11hipStream_t) Create kernel arguments from a given

[hipblaslt_ext::GemmInstance](#classhipblaslt__ext_1_1_gemm_instance).This function creates kernel arguments from a given

[hipblaslt_ext::GemmInstance](#classhipblaslt__ext_1_1_gemm_instance)then saves the arguments inside the instance.- Parameters:
**algo**–**[in]**Handle for matrix multiplication algorithm to be used. See hipblaslt.h::hipblasLtMatmulAlgo_t . When NULL, an implicit heuristics query with default search preferences will be performed to determine actual algorithm to use.**workspace**–**[in]**Pointer to the workspace buffer allocated in the GPU memory. Pointer must be 16B aligned (that is, lowest 4 bits of address must be 0).**useUserArgs**–**[in]**Use user args, this does not affect vanilla gemm. (May be deprecated in the future)**stream**–**[in]**The HIP stream where all the GPU work will be submitted. (May be deprecated in the future)

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_INVALID_VALUE**– If the gemm_count = 0 or workspace is null but workspaceBytes is greater than zero. Note that workspaceBytes should be set with setMaxWorkspaceBytes.



-
hipblasStatus_t initialize(const
[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)&algo, GemmTuning &tuning, void *workspace, bool useUserArgs = true, hipStream_t stream = 0)[#](#_CPPv4N13hipblaslt_ext12GemmInstance10initializeERK21hipblasLtMatmulAlgo_tR10GemmTuningPvb11hipStream_t) Create kernel arguments from a given

[hipblaslt_ext::GemmInstance](#classhipblaslt__ext_1_1_gemm_instance).This function creates kernel arguments from a given

[hipblaslt_ext::GemmInstance](#classhipblaslt__ext_1_1_gemm_instance)then saves the arguments inside the instance.- Parameters:
**algo**–**[in]**Handle for matrix multiplication algorithm to be used. See hipblaslt.h::hipblasLtMatmulAlgo_t . When NULL, an implicit heuristics query with default search preferences will be performed to determine actual algorithm to use.**tuning**–**[in]**Structure with user tuning parameters. Note that not every algo supports user tuning parameters. Will return HIPBLAS_STATUS_INVALID_VALUE if not supported. be 0).**workspace**–**[in]**Pointer to the workspace buffer allocated in the GPU memory. Pointer must be 16B aligned (that is, lowest 4 bits of address must be 0).**useUserArgs**–**[in]**Use user args, this does not affect vanilla gemm. (May be deprecated in the future)**stream**–**[in]**The HIP stream where all the GPU work will be submitted. (May be deprecated in the future)

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_INVALID_VALUE**– If the gemm_count = 0 or workspace is null but workspaceBytes is greater than zero. Note that workspaceBytes should be set with setMaxWorkspaceBytes.



-
hipblasStatus_t run(hipStream_t stream, hipEvent_t start = nullptr, hipEvent_t stop = nullptr)
[#](#_CPPv4N13hipblaslt_ext12GemmInstance3runE11hipStream_t10hipEvent_t10hipEvent_t) Execute the kernel arguments stored inside the

[hipblaslt_ext::GemmInstance](#classhipblaslt__ext_1_1_gemm_instance).- Parameters:
**stream**–**[in]**The HIP stream where all the GPU work will be**start**–**[in]**The HIP event which will record the start of the kernel**stop**–**[in]**The HIP event which will record the end of the kernel submitted.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.


-
hipblasStatus_t algoGetHeuristic(const int requestedAlgoCount, const

### Gemm[#](#gemm)

-
class Gemm : public hipblaslt_ext::
[GemmInstance](#_CPPv4N13hipblaslt_ext12GemmInstanceE)[#](#_CPPv4N13hipblaslt_ext4GemmE) hipblasLt extension instance for gemm.

The instance can be used to create arguments to compute the matrix multiplication of matrices A and B to produce the output matrix D, according to the following operation:

`D`

=`alpha*`

(`A`

*`B`

) +`beta*`

(`C`

), where`A`

,`B`

, and`C`

are input matrices, and`alpha`

and`beta`

are input scalars.Public Functions

-
explicit Gemm(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)opA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)opB, hipDataType typeA, hipDataType typeB, hipDataType typeC, hipDataType typeD, hipblasComputeType_t typeCompute)[#](#_CPPv4N13hipblaslt_ext4Gemm4GemmE17hipblasLtHandle_t18hipblasOperation_t18hipblasOperation_t11hipDataType11hipDataType11hipDataType11hipDataType20hipblasComputeType_t) Constructor.

This function set the problem from hipblasLt structures. For more information about the structures, see hipblasLtMatmul for more information.

- Parameters:
**handle**–**[in]**The handle from hipBLASLt.**opA, opB**–**[in]**The transpose type of matrix A, B**typeA, typeB, typeC, typeD**–**[in]**The data type of matrix A, B, C, D**typeCompute**–**[in]**The compute type of the gemm problem



-
explicit Gemm(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmul_descr, const void *alpha, const void *A,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matA, const void *B,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matB, const void *beta, const void *C,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matC, void *D,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matD)[#](#_CPPv4N13hipblaslt_ext4Gemm4GemmE17hipblasLtHandle_t21hipblasLtMatmulDesc_tPKvPKv23hipblasLtMatrixLayout_tPKv23hipblasLtMatrixLayout_tPKvPKv23hipblasLtMatrixLayout_tPv23hipblasLtMatrixLayout_t) Constructor that sets the gemm problem from hipblasLt structures.

This constructor sets the problem from hipblasLt structures. For more information about the structures, see hipblasLtMatmul for more information.

- Parameters:
**handle**–**[in]**The handle from hipBLASLt.**matmul_descr**–**[in]**Handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**alpha, beta**–**[in]**Pointers to the scalars used in the multiplication.**matA, matB, matC, matD**–**[in]**Handles to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**A, B, C**–**[in]**Pointers to the GPU memory associated with the corresponding descriptors`matA`

,`matB`

and`matC`

.**D**–**[out]**Pointer to the GPU memory associated with the descriptor`matD`

.



-
hipblasStatus_t setProblem(int64_t m, int64_t n, int64_t k, int64_t batch_count,
[GemmEpilogue](#_CPPv4N13hipblaslt_ext12GemmEpilogueE)&epilogue,[GemmInputs](#_CPPv4N13hipblaslt_ext10GemmInputsE)&inputs)[#](#_CPPv4N13hipblaslt_ext4Gemm10setProblemE7int64_t7int64_t7int64_t7int64_tR12GemmEpilogueR10GemmInputs) Sets the problem for a gemm problem.

This function sets the problem with m, n, k, batch_count. It uses the problem type sets from the constructor.

- Parameters:
**m, n, k**–**[in]**The problem size.**batch_count**–**[in]**The batch count.**epilogue**–**[in]**The class that controls the epilogue.**inputs**–**[in]**The inputs of the problem.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



-
hipblasStatus_t setProblem(int64_t m, int64_t n, int64_t k, int64_t batch_count, int64_t lda, int64_t ldb, int64_t ldc, int64_t ldd, int64_t strideA, int64_t strideB, int64_t strideC, int64_t strideD,
[GemmEpilogue](#_CPPv4N13hipblaslt_ext12GemmEpilogueE)&epilogue,[GemmInputs](#_CPPv4N13hipblaslt_ext10GemmInputsE)&inputs,[GemmProblemType](#_CPPv4N13hipblaslt_ext15GemmProblemTypeE)&problemtype)[#](#_CPPv4N13hipblaslt_ext4Gemm10setProblemE7int64_t7int64_t7int64_t7int64_t7int64_t7int64_t7int64_t7int64_t7int64_t7int64_t7int64_t7int64_tR12GemmEpilogueR10GemmInputsR15GemmProblemType) Sets the problem for a gemm problem.

This function sets the problem with m, n, k, batch_count. It uses the problem type sets from the constructor.

- Parameters:
**m, n, k**–**[in]**The problem size.**batch_count**–**[in]**The batch count.**lda, ldb, ldc, ldd**–**[in]**The leading dimensions of the matrix.**strideA, strideB, strideC, strideD**–**[in]**The batch stride of the matrix.**epilogue**–**[in]**The structure that controls the epilogue.**inputs**–**[in]**The inputs of the problem.**problemtype**–**[in]**The structure that sets the problem type of a gemm problem.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



-
hipblasStatus_t setProblem(
[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmul_descr, const void *alpha, const void *A,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matA, const void *B,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matB, const void *beta, const void *C,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matC, void *D,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matD)[#](#_CPPv4N13hipblaslt_ext4Gemm10setProblemE21hipblasLtMatmulDesc_tPKvPKv23hipblasLtMatrixLayout_tPKv23hipblasLtMatrixLayout_tPKvPKv23hipblasLtMatrixLayout_tPv23hipblasLtMatrixLayout_t) Sets the gemm problem from hipblasLt structures.

This function sets the problem from hipblasLt structures. For more information about the structures, see hipblasLtMatmul for more information.

- Parameters:
**matmul_descr**–**[in]**Handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**alpha, beta**–**[in]**Pointers to the scalars used in the multiplication.**matA, matB, matC, matD**–**[in]**Handles to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**A, B, C**–**[in]**Pointers to the GPU memory associated with the corresponding descriptors`matA`

,`matB`

and`matC`

.**D**–**[out]**Pointer to the GPU memory associated with the descriptor`matD`

.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



-
explicit Gemm(

### GroupedGemm[#](#groupedgemm)

-
class GroupedGemm : public hipblaslt_ext::
[GemmInstance](#_CPPv4N13hipblaslt_ext12GemmInstanceE)[#](#_CPPv4N13hipblaslt_ext11GroupedGemmE) hipblasLt extension instance for grouped gemm.

The instance can be used to create arguments to compute the matrix multiplication of matrices A and B to produce the output matrix D, according to the following operation:

`D`

=`alpha*`

(`A`

*`B`

) +`beta*`

(`C`

), where`A`

,`B`

, and`C`

are input matrices, and`alpha`

and`beta`

are input scalars.Public Functions

-
explicit GroupedGemm(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)opA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)opB, hipDataType typeA, hipDataType typeB, hipDataType typeC, hipDataType typeD, hipblasComputeType_t typeCompute)[#](#_CPPv4N13hipblaslt_ext11GroupedGemm11GroupedGemmE17hipblasLtHandle_t18hipblasOperation_t18hipblasOperation_t11hipDataType11hipDataType11hipDataType11hipDataType20hipblasComputeType_t) Constructor.

This function set the problem from hipblasLt structures. For more information about the structures, see hipblasLtMatmul for more information.

- Parameters:
**handle**–**[in]**The handle from hipBLASLt.**opA, opB**–**[in]**The transpose type of matrix A, B**typeA, typeB, typeC, typeD**–**[in]**The data type of matrix A, B, C, D**typeCompute**–**[in]**The compute type of the gemm problem



-
explicit GroupedGemm(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle, std::vector<[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)> &matmul_descr, std::vector<void*> &alpha, std::vector<void*> &A, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matA, std::vector<void*> &B, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matB, std::vector<void*> &beta, std::vector<void*> &C, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matC, std::vector<void*> &D, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matD)[#](#_CPPv4N13hipblaslt_ext11GroupedGemm11GroupedGemmE17hipblasLtHandle_tRNSt6vectorI21hipblasLtMatmulDesc_tEERNSt6vectorIPvEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEERNSt6vectorIPvEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEE) Constructor that sets the grouped gemm problem from hipblasLt structures.

This constructor sets the problem from hipblasLt structures. For more information about the structures, see hipblasLtMatmul for more information.

- Parameters:
**handle**–**[in]**The handle from hipBLASLt.**matmul_descr**–**[in]**Vectors of handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**alpha, beta**–**[in]**Vectors of float used in the multiplication.**matA, matB, matC, matD**–**[in]**Vectors of handle to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**A, B, C**–**[in]**Vectors of pointer to the GPU memory associated with the corresponding descriptors`matA`

,`matB`

and`matC`

.**D**–**[out]**Vector of pointer to the GPU memory associated with the descriptor`matD`

.



-
hipblasStatus_t setProblem(std::vector<int64_t> &m, std::vector<int64_t> &n, std::vector<int64_t> &k, std::vector<int64_t> &batch_count, std::vector<
[GemmEpilogue](#_CPPv4N13hipblaslt_ext12GemmEpilogueE)> &epilogue, std::vector<[GemmInputs](#_CPPv4N13hipblaslt_ext10GemmInputsE)> &inputs)[#](#_CPPv4N13hipblaslt_ext11GroupedGemm10setProblemERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI12GemmEpilogueEERNSt6vectorI10GemmInputsEE) Sets the problem for a gemm problem.

This function sets the problem with m, n, k, batch_count. It uses the problem type sets from the constructor.

- Parameters:
**m, n, k**–**[in]**The problem size in vector.**batch_count**–**[in]**The batch count in vector.**epilogue**–**[in]**The structure in vector that controls the epilogue.**inputs**–**[in]**The inputs in vector of the problem.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



-
hipblasStatus_t setProblem(std::vector<int64_t> &m, std::vector<int64_t> &n, std::vector<int64_t> &k, std::vector<int64_t> &batch_count, std::vector<int64_t> &lda, std::vector<int64_t> &ldb, std::vector<int64_t> &ldc, std::vector<int64_t> &ldd, std::vector<int64_t> &strideA, std::vector<int64_t> &strideB, std::vector<int64_t> &strideC, std::vector<int64_t> &strideD, std::vector<
[GemmEpilogue](#_CPPv4N13hipblaslt_ext12GemmEpilogueE)> &epilogue, std::vector<[GemmInputs](#_CPPv4N13hipblaslt_ext10GemmInputsE)> &inputs,[GemmProblemType](#_CPPv4N13hipblaslt_ext15GemmProblemTypeE)&problemtype)[#](#_CPPv4N13hipblaslt_ext11GroupedGemm10setProblemERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI7int64_tEERNSt6vectorI12GemmEpilogueEERNSt6vectorI10GemmInputsEER15GemmProblemType) Sets the problem for a gemm problem.

This function sets the problem with m, n, k, batch_count. It uses the problem type sets from the constructor.

- Parameters:
**m, n, k**–**[in]**The problem size in vector.**batch_count**–**[in]**The batch count in vector.**lda, ldb, ldc, ldd**–**[in]**The leading dimensions in vector of the matrix.**strideA, strideB, strideC, strideD**–**[in]**The batch stride in vector of the matrix.**epilogue**–**[in]**The structure in vector that controls the epilogue.**inputs**–**[in]**The inputs in vector of the problem.**problemtype**–**[in]**The structure that sets the problem type of a gemm problem.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



-
hipblasStatus_t setProblem(std::vector<
[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)> &matmul_descr, std::vector<void*> &alpha, std::vector<void*> &A, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matA, std::vector<void*> &B, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matB, std::vector<void*> &beta, std::vector<void*> &C, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matC, std::vector<void*> &D, std::vector<[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)> &matD)[#](#_CPPv4N13hipblaslt_ext11GroupedGemm10setProblemERNSt6vectorI21hipblasLtMatmulDesc_tEERNSt6vectorIPvEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEERNSt6vectorIPvEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEERNSt6vectorIPvEERNSt6vectorI23hipblasLtMatrixLayout_tEE) Sets the grouped gemm problem from hipblasLt structures.

This function sets the problem from hipblasLt structures. For more information about the structures, see hipblasLtMatmul for more information.

- Parameters:
**matmul_descr**–**[in]**Vectors of handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**alpha, beta**–**[in]**Vectors of float used in the multiplication.**matA, matB, matC, matD**–**[in]**Vectors of handle to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**A, B, C**–**[in]**Vectors of pointer to the GPU memory associated with the corresponding descriptors`matA`

,`matB`

and`matC`

.**D**–**[out]**Vector of pointer to the GPU memory associated with the descriptor`matD`

.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



-
hipblasStatus_t getDefaultValueForDeviceUserArguments(void *hostDeviceUserArgs)
[#](#_CPPv4N13hipblaslt_ext11GroupedGemm37getDefaultValueForDeviceUserArgumentsEPv) A helper function to initialize DeviceUserArguments using the set problem(s) saved in the gemm object.

- Parameters:
**hostDeviceUserArgs**–**[in]**The DeviceUserArguments struture allocated in host. Note that the user must put the correct type of the DeviceUserArguments.- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.


-
hipblasStatus_t run(void *deviceUserArgs, hipStream_t stream)
[#](#_CPPv4N13hipblaslt_ext11GroupedGemm3runEPv11hipStream_t) Run the kernel using DeviceUserArguments.

- Parameters:
**deviceUserArgs**–**[in]**Pointer to the DeviceUserArguments buffer allocated in the GPU memory. Pointer must be 16B aligned (that is, lowest 4 bits of**stream**–**[in]**The HIP stream where all the GPU work will be submitted.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_INVALID_VALUE**– If the gemm_count = 0.



-
hipblasStatus_t run(hipStream_t stream, hipEvent_t start = nullptr, hipEvent_t stop = nullptr)
[#](#_CPPv4N13hipblaslt_ext11GroupedGemm3runE11hipStream_t10hipEvent_t10hipEvent_t) Execute the kernel arguments stored inside the

[hipblaslt_ext::GemmInstance](#classhipblaslt__ext_1_1_gemm_instance).- Parameters:
**stream**–**[in]**The HIP stream where all the GPU work will be**start**–**[in]**The HIP event which will record the start of the kernel**stop**–**[in]**The HIP event which will record the end of the kernel submitted.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.


-
explicit GroupedGemm(

## hipBLASLtExt API reference[#](#id1)

### getAllAlgos()[#](#getallalgos)

-
hipblasStatus_t hipblaslt_ext::getAllAlgos(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[GemmType](#_CPPv4N13hipblaslt_ext8GemmTypeE)typeGemm,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)opA,[hipblasOperation_t](https://rocm.docs.amd.com/projects/hipSOLVER/en/latest/reference/api/types.html#_CPPv418hipblasOperation_t)opB, hipDataType typeA, hipDataType typeB, hipDataType typeC, hipDataType typeD, hipblasComputeType_t typeCompute, std::vector<[hipblasLtMatmulHeuristicResult_t](datatypes.html#_CPPv432hipblasLtMatmulHeuristicResult_t)> &heuristicResults)[#](#_CPPv4N13hipblaslt_ext11getAllAlgosE17hipblasLtHandle_t8GemmType18hipblasOperation_t18hipblasOperation_t11hipDataType11hipDataType11hipDataType11hipDataType20hipblasComputeType_tRNSt6vectorI32hipblasLtMatmulHeuristicResult_tEE) Retrieve the possible algorithms.

This function retrieves the possible algorithms for the matrix multiply operation

[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d)function with the given data and compute tpye. The output is placed in heuristicResults in the order of increasing estimated compute time. It should use[matmulIsAlgoSupported()](#group__library__module_1gaf76d02eda797350ed29af996596ddcaf)to check if the algorithm support the problem before execute[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d).- Parameters:
**handle**–**[in]**Pointer to the allocated hipBLASLt handle for the hipBLASLt context. See[hipblasLtHandle_t](datatypes.html#group__types__module_1ga7eadd4c418242a4d98a617cfd44fa12e).**typeGemm**–**[in]**[Gemm](#classhipblaslt__ext_1_1_gemm)type. ex. GEMM, GROUPED_GEMM.**opA, opB**–**[in]**Transpose settings of A, B.**typeA, typeB, typeC, typeD**–**[in]**The data type of matrix A, B, C, D.**typeCompute**–**[in]**The compute type.**heuristicResults**–**[out]**The algorithm heuristic vector.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. Inspect returnedAlgoCount > 0.state for the status of the results.**HIPBLAS_STATUS_NOT_SUPPORTED**– If no heuristic function available for current configuration.**HIPBLAS_STATUS_INVALID_VALUE**– If no solution is found.



### getIndexFromAlgo()[#](#getindexfromalgo)

-
int hipblaslt_ext::getIndexFromAlgo(
[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)&algo)[#](#_CPPv4N13hipblaslt_ext16getIndexFromAlgoER21hipblasLtMatmulAlgo_t) Retrieve the algorithm index.

- Parameters:
**algo**–**[in]**The algorithm.- Return values:
**int**– The index of the algorithm, can be used to get heuristic results from[getAlgosFromIndex](#group__library__module_1ga507d9a1b79db999952a4f5bce0992b73). Returns -1 if the index stored in algo < 0. Note that the index may not be valid if the algo struct is not initialized properly.


### getAlgosFromIndex()[#](#getalgosfromindex)

-
hipblasStatus_t hipblaslt_ext::getAlgosFromIndex(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle, std::vector<int> &algoIndex, std::vector<[hipblasLtMatmulHeuristicResult_t](datatypes.html#_CPPv432hipblasLtMatmulHeuristicResult_t)> &heuristicResults)[#](#_CPPv4N13hipblaslt_ext17getAlgosFromIndexE17hipblasLtHandle_tRNSt6vectorIiEERNSt6vectorI32hipblasLtMatmulHeuristicResult_tEE) Retrieve the possible algorithms.

This function retrieves the possible algorithms for the matrix multiply operation

[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d)function with the given index. The output is placed in heuristicResult in the order of increasing estimated compute time. A recorded solution index cannot be used across different verison of library. It should use[matmulIsAlgoSupported()](#group__library__module_1gaf76d02eda797350ed29af996596ddcaf)to check if the algorithm support the problem before execute[hipblasLtMatmul()](api-reference.html#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d).- Parameters:
**handle**–**[in]**Pointer to the allocated hipBLASLt handle for the hipBLASLt context. See[hipblasLtHandle_t](datatypes.html#group__types__module_1ga7eadd4c418242a4d98a617cfd44fa12e).**algoIndex**–**[in]**The algorithm index vector.**heuristicResults**–**[out]**The algorithm heuristic vector.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. Inspect heuristicResults.size() > 0.state for the status of the results.**HIPBLAS_STATUS_NOT_SUPPORTED**– If no heuristic function available for current configuration.**HIPBLAS_STATUS_INVALID_VALUE**– If query indexes are all out of bound of solution map.



### matmulIsAlgoSupported()[#](#matmulisalgosupported)

-
hipblasStatus_t hipblaslt_ext::matmulIsAlgoSupported(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmulDesc, const void *alpha,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Adesc,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Bdesc, const void *beta,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Cdesc,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Ddesc,[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)&algo, size_t &workspaceSizeInBytes)[#](#_CPPv4N13hipblaslt_ext21matmulIsAlgoSupportedE17hipblasLtHandle_t21hipblasLtMatmulDesc_tPKv23hipblasLtMatrixLayout_t23hipblasLtMatrixLayout_tPKv23hipblasLtMatrixLayout_t23hipblasLtMatrixLayout_tR21hipblasLtMatmulAlgo_tR6size_t) Check if the algorithm supports the problem. (For hipblasLt API)

This function updates the problem saved inside the algorithm if the problem is supported. The required workspaceSizeInBytes is also returned.

- Parameters:
**handle**–**[in]**Pointer to the allocated hipBLASLt handle for the hipBLASLt context. See[hipblasLtHandle_t](datatypes.html#group__types__module_1ga7eadd4c418242a4d98a617cfd44fa12e).**matmulDesc**–**[in]**Handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**alpha, beta**–**[in]**Pointers to the scalars used in the multiplication.**Adesc, Bdesc, Cdesc, Ddesc**–**[in]**Handles to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**algo**–**[in]**The algorithm heuristic.**workspaceSizeInBytes**–**[out]**Return the required workspace size.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. The problem is supported by the algorithm. results.**HIPBLAS_STATUS_INVALID_VALUE**– The problem is not supported.



## hipblasLtExt usage[#](#hipblasltext-usage)

Here are the three use cases supported by the hipBLASLtExt APIs.

### GEMM[#](#id2)

hipblasLt has its own instance. You must assign the problem type when constructing or importing the problem from the hipBLAS API.

```
HIPBLASLT_EXPORT explicit Gemm(hipblasLtHandle_t handle,
hipblasOperation_t opA,
hipblasOperation_t opB,
hipDataType typeA,
hipDataType typeB,
hipDataType typeC,
hipDataType typeD,
hipblasComputeType_t typeCompute);
HIPBLASLT_EXPORT explicit Gemm(hipblasLtHandle_t handle,
hipblasLtMatmulDesc_t matmul_descr,
const void* alpha,
const void* A,
hipblasLtMatrixLayout_t matA,
const void* B,
hipblasLtMatrixLayout_t matB,
const void* beta,
const void* C,
hipblasLtMatrixLayout_t matC,
void* D,
hipblasLtMatrixLayout_t matD);
```

After the instance is created, you can set the problem using the API. The API might require the following structures:

struct GemmEpilogue { hipblasLtEpilogue_t mode = HIPBLASLT_EPILOGUE_DEFAULT; hipDataType bias_data_type; int aux_ld; int aux_stride; };

`setProblem`

APIs:HIPBLASLT_EXPORT hipblasStatus_t setProblem( int64_t m, int64_t n, int64_t k, int64_t batch_count, GemmEpilogue& epilogue, GemmInputs& inputs);


You can set the leading dimensions and strides and reassign the data type using the following API:

```
HIPBLASLT_EXPORT hipblasStatus_t setProblem(int64_t m,
int64_t n,
int64_t k,
int64_t batch_count,
int64_t lda,
int64_t ldb,
int64_t ldc,
int64_t ldd,
int64_t strideA,
int64_t strideB,
int64_t strideC,
int64_t strideD,
GemmEpilogue& epilogue,
GemmInputs& inputs,
GemmProblemType& problemtype);
```

You can import problems from the hipblasLt APIs after the instance is created.

Note

This can overwrite the problem type of the instance.

```
HIPBLASLT_EXPORT hipblasStatus_t setProblem(hipblasLtMatmulDesc_t matmul_descr,
const void* alpha,
const void* A,
hipblasLtMatrixLayout_t matA,
const void* B,
hipblasLtMatrixLayout_t matB,
const void* beta,
const void* C,
hipblasLtMatrixLayout_t matC,
void* D,
hipblasLtMatrixLayout_t matD);
```

You can retrieve heuristics and set kernel arguments with the instance. If the properties of the GEMM and the inputs don’t change, you can call the run API to launch the kernel directly.

```
// Pseudo code
hipblaslt_ext::GemmPreference pref;
pref.setMaxWorkspaceBytes(1000000);
// Default epilogue mode is HIPBLASLT_EPILOGUE_DEFAULT
hipblaslt_ext::GemmEpilogue epilogue;
hipblaslt_ext::GemmInputs inputs;
inputs.setA(d_a);
inputs.setB(d_b);
inputs.setC(d_c);
inputs.setD(d_d);
inputs.setAlpha(&alpha);
inputs.setBeta(&beta);
hipblaslt_ext::Gemm gemm(handle,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIPBLAS_COMPUTE_32F);
std::vector<hipblasLtMatmulHeuristicResult_t> heuristic;
gemm.setProblem(1, 1, 1, 1, epilogue, inputs); // m, n, k, batch
gemm.algoGetHeuristic(gemm, pref, heuristic);
gemm.initialize(heuristic[0].algo, d_workspace, stream);
for(int i = 0; i < 10; i++)
{
gemm.run(stream);
}
```

### Grouped GEMM[#](#grouped-gemm)

`hipblasLtExt`

supports grouped GEMM. It shares the same class with normal GEMM.

After the problem is set, you can check the problem type using the function `getGemmType()`

.

```
enum class GemmType
{
HIPBLASLT_GEMM = 1,
HIPBLASLT_GROUPED_GEMM = 2
};
```

The grouped GEMM class also includes the `setProblem`

APIs.

```
HIPBLASLT_EXPORT hipblasStatus_t setProblem(
int64_t m, int64_t n, int64_t k, int64_t batch_count, GemmEpilogue& epilogue, GemmInputs& inputs);
HIPBLASLT_EXPORT hipblasStatus_t setProblem(std::vector<int64_t>& m,
std::vector<int64_t>& n,
std::vector<int64_t>& k,
std::vector<int64_t>& batch_count,
std::vector<GemmEpilogue>& epilogue,
std::vector<GemmInputs>& inputs);
HIPBLASLT_EXPORT hipblasStatus_t setProblem(std::vector<int64_t>& m,
std::vector<int64_t>& n,
std::vector<int64_t>& k,
std::vector<int64_t>& batch_count,
std::vector<int64_t>& lda,
std::vector<int64_t>& ldb,
std::vector<int64_t>& ldc,
std::vector<int64_t>& ldd,
std::vector<int64_t>& strideA,
std::vector<int64_t>& strideB,
std::vector<int64_t>& strideC,
std::vector<int64_t>& strideD,
std::vector<GemmEpilogue>& epilogue,
std::vector<GemmInputs>& inputs,
GemmProblemType& problemtype);
HIPBLASLT_EXPORT hipblasStatus_t setProblem(std::vector<hipblasLtMatmulDesc_t>& matmul_descr,
std::vector<void*>& alpha,
std::vector<void*>& A,
std::vector<hipblasLtMatrixLayout_t>& matA,
std::vector<void*>& B,
std::vector<hipblasLtMatrixLayout_t>& matB,
std::vector<void*>& beta,
std::vector<void*>& C,
std::vector<hipblasLtMatrixLayout_t>& matC,
std::vector<void*>& D,
std::vector<hipblasLtMatrixLayout_t>& matD);
```

For the following API, the `epilogue`

argument supports broadcasting to the length of the problem size
by duplicating the last element.

```
HIPBLASLT_EXPORT hipblasStatus_t setProblem(std::vector<int64_t>& m,
std::vector<int64_t>& n,
std::vector<int64_t>& k,
std::vector<int64_t>& batch_count,
std::vector<int64_t>& lda,
std::vector<int64_t>& ldb,
std::vector<int64_t>& ldc,
std::vector<int64_t>& ldd,
std::vector<int64_t>& strideA,
std::vector<int64_t>& strideB,
std::vector<int64_t>& strideC,
std::vector<int64_t>& strideD,
std::vector<GemmEpilogue>& epilogue,
std::vector<GemmInputs>& inputs,
GemmProblemType& problemtype);
```

Note

Only a `problemtype`

size equal to 1 is currently supported. (This means only one `GemmProblemType`

for all problems.)

```
// Pseudo code
std::vector<int64_t> m, n, k;
// ...
for(size_t i = 0; i < problem_size, i++)
{
// ...
}
std::vector<GemmProblemType> problemtypes;
problemtypes.push_back(problemtype);
groupedgemm.setProblem(m, n, k, batch_count, lda, ldb, ldc, ldd, strideA, strideB, strideC, strideD, epilogue, inputs, problemtypes);
```

#### The UserArguments structure[#](#the-userarguments-structure)

Grouped GEMM supports the use of external device memory to run the kernel.
This is helpful if some of the arguments are from the output of the pervious kernel.
To change the size-related arguments `m`

, `n`

, `k`

, and `batch`

, see [Fixed MK](#fixed-mk).

```
struct UserArguments
{
uint32_t m; //!< size m
uint32_t n; //!< size n
uint32_t batch; //!< size batch
uint32_t k; //!< size k
void* d; //!< The d matrix input pointer.
void* c; //!< The c matrix input pointer.
void* a; //!< The a matrix input pointer.
void* b; //!< The b matrix input pointer.
uint32_t strideD1; //!< The d leading dimension.
uint32_t strideD2; //!< The d batch stride
uint32_t strideC1; //!< The c leading dimension.
uint32_t strideC2; //!< The c batch stride
uint32_t strideA1; //!< The a leading dimension.
uint32_t strideA2; //!< The a batch stride
uint32_t strideB1; //!< The b leading dimension.
uint32_t strideB2; //!< The b batch stride
int8_t alpha[16]; //!< The alpha value.
int8_t beta[16]; //!< The beta value.
// Epilogue inputs
void* bias; //!< The bias input pointer.
int biasType; //!< The bias datatype. Only works if mode is set to bias related epilogues.
uint32_t reserved;
void* e; //!< The aux input pointer. Only works if mode is set to aux related epilogues.
uint32_t strideE1; //!< The aux leading dimension. Only works if mode is set to aux related epilogues.
uint32_t strideE2; //!< The aux batch stride. Only works if mode is set to aux related epilogues.
float act0; //!< The activation value 1. Some activations might use it.
float act1; //!< The activation value 2.
int activationType; //!< The activation type. Only works if mode is set to activation related epilogues.
} __attribute__((packed));
```

hipBLASLt adds two functions to the `UserArguments`

-related API. The first API is a helper function that helps you initialize
the `UserArguments`

structure from the saved problems inside the grouped GEMM object.
The second API is an overload function with an additional `UserArguments`

device pointer input.

```
HIPBLASLT_EXPORT hipblasStatus_t getDefaultValueForDeviceUserArguments(void* hostDeviceUserArgs);
HIPBLASLT_EXPORT hipblasStatus_t run(void* deviceUserArgs, hipStream_t stream);
```

Here is a simple example that shows how this API works.

```
// Pseudo code
// Step 1: Get all algorithms
std::vector<hipblasLtMatmulHeuristicResult_t> heuristicResult;
CHECK_HIPBLASLT_ERROR(hipblaslt_ext::getAllAlgos(handle,
HIPBLASLT_GEMM,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
in_out_datatype,
in_out_datatype,
in_out_datatype,
in_out_datatype,
HIPBLAS_COMPUTE_32F,
heuristicResult));
hipblaslt_ext::GemmPreference pref;
pref.setMaxWorkspaceBytes(1000000);
// Step 2: Setup problem
std::vector<int64_t> m(gemm_count);
std::vector<int64_t> n(gemm_count);
std::vector<int64_t> k(gemm_count);
std::vector<int64_t> batch_count(gemm_count);
std::vector<hipblaslt_ext::GemmEpilogue> epilogue(gemm_count);
std::vector<hipblaslt_ext::GemmInputs> inputs(gemm_count);
for(int i = 0; i < gemm_count; i++)
{
m[i] = 1;
n[i] = 1;
k[i] = 1;
batch_count[i] = 1;
epilogue[i].setMode(HIPBLASLT_EPILOGUE_GELU);
inputs[i].setA(d_a[i]);
inputs[i].setB(d_b[i]);
inputs[i].setC(d_c[i]);
inputs[i].setD(d_d[i]);
inputs[i].setAlpha(&alpha[i]);
inputs[i].setBeta(&beta[i]);
}
// Step 3: Create grouped gemm instance
hipblaslt_ext::GroupedGemm groupedGemm(handle,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIPBLAS_COMPUTE_32F);
// Step 4: Set problem
groupedGemm.setProblem(m, n, k, batch_count, epilogue, inputs); // m, n, k, batch
// Step 5: Get default value from the instance
hipblaslt_ext::UserArguments* dUAFloat = new hipblaslt_ext::UserArguments[gemm_count];
groupedGemm.getDefaultValueForDeviceUserArguments((void*)dUAFloat);
// Once you get the default value here, you can make several copies and change the values
// from the host
// Next copy them to the device memory
hipblaslt_ext::UserArguments* d_dUAFloat = nullptr;
hipMalloc(&d_dUAFloat, sizeof(hipblaslt_ext::UserArguments) * gemm_count);
hipMemcpy(d_dUAFloat, dUAFloat, sizeof(hipblaslt_ext::UserArguments) * gemm_count, hipMemcpyHostToDevice);
validIdx.clear();
for(int j = 0; j < heuristicResult.size(); j++)
{
size_t workspace_size = 0;
if(groupedGemm.isAlgoSupported(heuristicResult[j].algo, workspace_size)
== HIPBLAS_STATUS_SUCCESS)
{
validIdx.push_back(j);
}
}
// Step 6: Initialize and run
if(validIdx.size() > 1)
{
groupedGemm.initialize(heuristicResult[validIdx[0]].algo, d_workspace, stream);
for(int i = 0; i < 10; i++)
{
groupedGemm.run(userArgs, stream);
}
}
```

### The base class (GemmInstance)[#](#the-base-class-gemminstance)

This is the base class for `Gemm`

and `GroupedGemm`

.

```
// Gets heuristic from the instance.
HIPBLASLT_EXPORT hipblasStatus_t algoGetHeuristic(const int requestedAlgoCount,
const GemmPreference& pref,
std::vector<hipblasLtMatmulHeuristicResult_t>& heuristicResults);
// Returns SUCCESS if the algo is supported, also returns the required workspace size in bytes.
HIPBLASLT_EXPORT hipblasStatus_t isAlgoSupported(hipblasLtMatmulAlgo_t& algo, size_t& workspaceSizeInBytes);
// Initializes the instance before calling run. Requires every time the problem is set.
HIPBLASLT_EXPORT hipblasStatus_t initialize(const hipblasLtMatmulAlgo_t& algo, void* workspace, bool useUserArgs = true, hipStream_t stream = 0);
// Run the problem.
HIPBLASLT_EXPORT hipblasStatus_t run(hipStream_t stream);
```

### Get all algorithms[#](#get-all-algorithms)

Get all algorithms allows you to get all the algorithms for a specific problem type. It requires the transpose of A, B, the data type of the inputs, and the compute type.

```
HIPBLASLT_EXPORT
hipblasStatus_t hipblaslt_ext::getAllAlgos(hipblasLtHandle_t handle,
hipblasLtExtGemmTypeEnum_t typeGemm,
hipblasOperation_t opA,
hipblasOperation_t opB,
hipDataType typeA,
hipDataType typeB,
hipDataType typeC,
hipDataType typeD,
hipblasComputeType_t typeCompute,
std::vector<hipblasLtMatmulHeuristicResult_t>& heuristicResults);
```

This API doesn’t require a problem size or epilogue as input. It uses another API named `isAlgoSupported`

to check
if the algorithm supports a problem.

```
hipblaslt_ext::matmulIsAlgoSupported()
gemm.isAlgoSupported()
```

The API returns the required workspace size in bytes upon successful completion.

```
// Get all algorithms
CHECK_HIPBLASLT_ERROR(hipblaslt_ext::getAllAlgos(handle,
HIPBLASLT_GEMM,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
in_out_datatype,
in_out_datatype,
in_out_datatype,
in_out_datatype,
HIPBLAS_COMPUTE_32F,
heuristicResult));
validIdx.clear();
for(int j = 0; j < heuristicResult.size(); j++)
{
size_t workspace_size = 0;
if(hipblaslt_ext::matmulIsAlgoSupported(handle,
matmul,
&(alpha),
matA,
matB,
&(beta),
matC,
matD,
heuristicResult[j].algo,
workspace_size)
== HIPBLAS_STATUS_SUCCESS)
{
validIdx.push_back(j);
heuristicResult[j].workspaceSize = workspace_size;
}
else
{
heuristicResult[j].workspaceSize = 0;
}
}
```

### Algorithm index[#](#algorithm-index)

This extension API lets you to get the algorithm index using `hipblasLtMatmulAlgo_t`

.

```
HIPBLASLT_EXPORT int getIndexFromAlgo(hipblasLtMatmulAlgo_t& algo);
```

You can use an index vector to retrieve the heuristic results.

```
HIPBLASLT_EXPORT
hipblasStatus_t
getAlgosFromIndex(hipblasLtHandle_t handle,
std::vector<int>& algoIndex,
std::vector<hipblasLtMatmulHeuristicResult_t>& heuristicResults);
```

## Sample code[#](#sample-code)

This section contains some code samples that demonstrate the use cases of the extension APIs.

### GEMM[#](#id5)

```
// Pseudo code for gemm problem
// Get all algorithms
std::vector<hipblasLtMatmulHeuristicResult_t> heuristicResult;
CHECK_HIPBLASLT_ERROR(hipblaslt_ext::getAllAlgos(handle,
HIPBLASLT_GEMM,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
in_out_datatype,
in_out_datatype,
in_out_datatype,
in_out_datatype,
HIPBLAS_COMPUTE_32F,
heuristicResult));
hipblaslt_ext::GemmPreference pref;
pref.setMaxWorkspaceBytes(1000000);
hipblaslt_ext::GemmEpilogue epilogue;
epilogue.setMode(HIPBLASLT_EPILOGUE_GELU);
hipblaslt_ext::GemmInputs inputs;
inputs.setA(d_a);
inputs.setB(d_b);
inputs.setC(d_c);
inputs.setD(d_d);
inputs.setAlpha(&alpha);
inputs.setBeta(&beta);
hipblaslt_ext::Gemm gemm(handle,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIPBLAS_COMPUTE_32F);
gemm.setProblem(1, 1, 1, 1, epilogue, inputs); // m, n, k, batch
validIdx.clear();
for(int j = 0; j < heuristicResult.size(); j++)
{
size_t workspace_size = 0;
if(gemm.isAlgoSupported(heuristicResult[j].algo, workspace_size)
== HIPBLAS_STATUS_SUCCESS)
{
validIdx.push_back(j);
heuristicResult[j].workspaceSize = workspace_size;
}
else
{
heuristicResult[j].workspaceSize = 0;
}
}
if(validIdx.size() > 1)
{
gemm.initialize(heuristicResult[validIdx[0]].algo, d_workspace, stream);
for(int i = 0; i < 10; i++)
{
gemm.run(stream);
}
}
```

### Grouped GEMM[#](#id6)

```
// Pseudo code for grouped gemm problem
// Get all algorithms
std::vector<hipblasLtMatmulHeuristicResult_t> heuristicResult;
CHECK_HIPBLASLT_ERROR(hipblaslt_ext::getAllAlgos(handle,
HIPBLASLT_GEMM,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
in_out_datatype,
in_out_datatype,
in_out_datatype,
in_out_datatype,
HIPBLAS_COMPUTE_32F,
heuristicResult));
hipblaslt_ext::GemmPreference pref;
pref.setMaxWorkspaceBytes(1000000);
std::vector<int64_t> m(gemm_count);
std::vector<int64_t> n(gemm_count);
std::vector<int64_t> k(gemm_count);
std::vector<int64_t> batch_count(gemm_count);
std::vector<hipblaslt_ext::GemmEpilogue> epilogue(gemm_count);
std::vector<hipblaslt_ext::GemmInputs> inputs(gemm_count);
for(int i = 0; i < gemm_count; i++)
{
m[i] = 1;
n[i] = 1;
k[i] = 1;
batch_count[i] = 1;
epilogue[i].setMode(HIPBLASLT_EPILOGUE_GELU);
inputs[i].setA(d_a[i]);
inputs[i].setB(d_b[i]);
inputs[i].setC(d_c[i]);
inputs[i].setD(d_d[i]);
inputs[i].setAlpha(&alpha[i]);
inputs[i].setBeta(&beta[i]);
}
hipblaslt_ext::GroupedGemm groupedGemm(handle,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIPBLAS_COMPUTE_32F);
groupedGemm.setProblem(m, n, k, batch_count, epilogue, inputs); // m, n, k, batch
validIdx.clear();
for(int j = 0; j < heuristicResult.size(); j++)
{
size_t workspace_size = 0;
if(groupedGemm.isAlgoSupported(heuristicResult[j].algo, workspace_size)
== HIPBLAS_STATUS_SUCCESS)
{
validIdx.push_back(j);
}
}
if(validIdx.size() > 1)
{
groupedGemm.initialize(heuristicResult[validIdx[0]].algo, d_workspace, stream);
for(int i = 0; i < 10; i++)
{
groupedGemm.run(stream);
}
}
```

### Algorithm index[#](#id7)

```
int index = hipblaslt_ext::getIndexFromAlgo(testResults[i].algo);
// Save the index to disk or somewhere else for later use.
// Get the index from previous state.
std::vector<int> algoIndex{index};
std::vector<hipblasLtMatmulHeuristicResult_t> heuristicResults;
// If the index is out of the bound of solutions, getAlgosFromIndex will return HIPBLAS_STATUS_INVALID_VALUE
if(HIPBLAS_STATUS_INVALID_VALUE
== hipblaslt_ext::getAlgosFromIndex(handle, algoIndex, heuristicResults))
{
std::cout << "Indexes are all out of bound." << std::endl;
break;
}
```

### [Grouped Gemm] Fixed MK[#](#grouped-gemm-fixed-mk)

The hipBLASLt extension supports changing the sizes (`m`

, `n`

, `k`

, and `batch`

) from the device memory `UserArguments`

.
However, the setup is a bit different from the normal routing.

#### Sum of N[#](#sum-of-n)

A sum of N needs to be used as an input for the grouped GEMM instance.

```
{1000, 1, 1, 1}; // The array of N, the first element is the sum of N
// Below is the values stored in "UserArguments"
{256, 256, 1, 1}; // This is a valid configuration cause 256 + 256 + 1 + 1 < 1000
{512, 512, 1, 1}; // This is NOT a valid configuration cause 512 + 512 + 1 + 1 > 1000
```

For example, consider a grouped GEMM with `gemm_count = 4`

. The sum of N must not exceed the “sum of N” set in the `setProblem`

API.
In this mode, the first element is the “sum of N” in the array of Ns.

```
// Pseudo code
// Step 1: Get all algorithms
std::vector<hipblasLtMatmulHeuristicResult_t> heuristicResult;
CHECK_HIPBLASLT_ERROR(hipblaslt_ext::getAllAlgos(handle,
HIPBLASLT_GEMM,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
in_out_datatype,
in_out_datatype,
in_out_datatype,
in_out_datatype,
HIPBLAS_COMPUTE_32F,
heuristicResult));
hipblaslt_ext::GemmPreference pref;
pref.setMaxWorkspaceBytes(1000000);
// Step 2: Setup problem
std::vector<int64_t> m(gemm_count);
std::vector<int64_t> n(gemm_count);
std::vector<int64_t> k(gemm_count);
std::vector<int64_t> batch_count(gemm_count);
std::vector<hipblaslt_ext::GemmEpilogue> epilogue(gemm_count);
std::vector<hipblaslt_ext::GemmInputs> inputs(gemm_count);
// Step 2.1: Calculate sum of n
int64_t sum_of_n = 0;
for(int i = 0; i < gemm_count; i++)
{
sum_of_n += n_arr[i];
}
// {sum_of_n, 1, 1, 1, ...}; // The array of N, the first element is the sum of N
for(int i = 0; i < gemm_count; i++)
{
m[i] = m_arr[i];
if(i == 0)
n[i] = sum_of_n;
else
n[i] = 1;
k[i] = k_arr[i];
batch_count[i] = 1;
inputs[i].setA(d_a[i]);
inputs[i].setB(d_b[i]);
inputs[i].setC(d_c[i]);
inputs[i].setD(d_d[i]);
inputs[i].setAlpha(&alpha[i]);
inputs[i].setBeta(&beta[i]);
}
// Step 3: Create grouped gemm instance
hipblaslt_ext::GroupedGemm groupedGemm(handle,
HIPBLAS_OP_N,
HIPBLAS_OP_N,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIP_R_16F,
HIPBLAS_COMPUTE_32F);
// Step 4: Set problem
groupedGemm.setProblem(m, n, k, batch_count, epilogue, inputs); // m, n, k, batch
// Step 5: Get default value from the instance
hipblaslt_ext::UserArguments* dUAFloat = new hipblaslt_ext::UserArguments[gemm_count];
groupedGemm.getDefaultValueForDeviceUserArguments((void*)dUAFloat);
// Once you get the default value here, you can make several copies and change the values
// from the host
// Next Copy them to the device memory
hipblaslt_ext::UserArguments* d_dUAFloat = nullptr;
hipMalloc(&d_dUAFloat, sizeof(hipblaslt_ext::UserArguments) * gemm_count);
hipMemcpy(d_dUAFloat, dUAFloat, sizeof(hipblaslt_ext::UserArguments) * gemm_count, hipMemcpyHostToDevice);
validIdx.clear();
for(int j = 0; j < heuristicResult.size(); j++)
{
size_t workspace_size = 0;
if(groupedGemm.isAlgoSupported(heuristicResult[j].algo, workspace_size)
== HIPBLAS_STATUS_SUCCESS)
{
validIdx.push_back(j);
}
}
int threads = 256;
int blocks = ceil((double)gemm_count / threads);
// Step 6: Initialize and run
if(validIdx.size() > 1)
{
groupedGemm.initialize(heuristicResult[validIdx[0]].algo, d_workspace);
for(int i = 0; i < 10; i++)
{
hipLaunchKernelGGL(kernelUpdateN,
dim3(blocks),
dim3(threads),
0,
stream,
gemm_count,
d_dUAFloat,
d_n_vec); // d_n_vec is a device pointer with Ns
groupedGemm.run(userArgs, stream);
}
}
// .....
__global__ void kernelUpdateN(uint32_t gemm_count, void* userArgs, int32_t* sizes_n)
{
uint64_t id = hipBlockIdx_x * 256 + hipThreadIdx_x;
if(id >= gemm_count)
return;
hipblaslt_ext::UserArguments* dUAFloat = static_cast<hipblaslt_ext::UserArguments*>(userArgs);
dUAFloat[id].n = sizes_n[id];
}
```
