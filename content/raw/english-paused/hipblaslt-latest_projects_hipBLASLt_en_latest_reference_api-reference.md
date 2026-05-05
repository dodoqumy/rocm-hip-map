---
title: "hipBLASLt API reference &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/reference/api-reference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:15.104410+00:00
content_hash: "93fb93bdf5551b16"
---

# hipBLASLt API reference[#](#hipblaslt-api-reference)

## hipblasLtCreate()[#](#hipblasltcreate)

-
hipblasStatus_t hipblasLtCreate(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)*handle)[#](#_CPPv415hipblasLtCreateP17hipblasLtHandle_t) Create a hipblaslt handle.

This function initializes the hipBLASLt library and creates a handle to an opaque structure holding the hipBLASLt library context. It allocates light hardware resources on the host and device, and must be called prior to making any other hipBLASLt library calls. The hipBLASLt library context is tied to the current ROCm device. To use the library on multiple devices, one hipBLASLt handle should be created for each device.

- Parameters:
**handle**–**[out]**Pointer to the allocated hipBLASLt handle for the created hipBLASLt context.- Return values:
**HIPBLAS_STATUS_SUCCESS**– The allocation completed successfully.**HIPBLAS_STATUS_INVALID_VALUE**–`handle`

== NULL.



## hipblasLtDestroy()[#](#hipblasltdestroy)

-
hipblasStatus_t hipblasLtDestroy(const
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle)[#](#_CPPv416hipblasLtDestroyK17hipblasLtHandle_t) Destory a hipblaslt handle.

This function releases hardware resources used by the hipBLASLt library. This function is usually the last call with a particular handle to the hipBLASLt library. Because

[hipblasLtCreate()](#group__library__module_1ga8f48ee6fa147ddc87c2b6278016e8bd7)allocates some internal resources and the release of those resources by calling[hipblasLtDestroy()](#group__library__module_1ga22b16d7255e78eb223d332957b4c6e80)will implicitly call hipDeviceSynchronize(), it is recommended to minimize the number of[hipblasLtCreate()](#group__library__module_1ga8f48ee6fa147ddc87c2b6278016e8bd7)/hipblasLtDestroy() occurrences.- Parameters:
**handle**–**[in]**Pointer to the hipBLASLt handle to be destroyed.- Return values:
**HIPBLAS_STATUS_SUCCESS**– The hipBLASLt context was successfully destroyed.**HIPBLAS_STATUS_NOT_INITIALIZED**– The hipBLASLt library was not initialized.**HIPBLAS_STATUS_INVALID_VALUE**–`handle`

== NULL.



## hipblasLtMatrixLayoutCreate()[#](#hipblasltmatrixlayoutcreate)

-
hipblasStatus_t hipblasLtMatrixLayoutCreate(
[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)*matLayout, hipDataType type, uint64_t rows, uint64_t cols, int64_t ld)[#](#_CPPv427hipblasLtMatrixLayoutCreateP23hipblasLtMatrixLayout_t11hipDataType8uint64_t8uint64_t7int64_t) Create a matrix layout descriptor.

This function creates a matrix layout descriptor by allocating the memory needed to hold its opaque structure.

- Parameters:
**matLayout**–**[out]**Pointer to the structure holding the matrix layout descriptor created by this function. see[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**type**–**[in]**Enumerant that specifies the data precision for the matrix layout descriptor this function creates. See hipDataType.**rows**–**[in]**Number of rows of the matrix.**cols**–**[in]**Number of columns of the matrix.**ld**–**[in]**The leading dimension of the matrix. In column major layout, this is the number of elements to jump to reach the next column. Thus ld >= m (number of rows).

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the descriptor was created successfully.**HIPBLAS_STATUS_ALLOC_FAILED**– If the memory could not be allocated.



## hipblasLtMatrixLayoutDestroy()[#](#hipblasltmatrixlayoutdestroy)

-
hipblasStatus_t hipblasLtMatrixLayoutDestroy(const
[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matLayout)[#](#_CPPv428hipblasLtMatrixLayoutDestroyK23hipblasLtMatrixLayout_t) Destory a matrix layout descriptor.

This function destroys a previously created matrix layout descriptor object.

- Parameters:
**matLayout**–**[in]**Pointer to the structure holding the matrix layout descriptor that should be destroyed by this function. see[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation was successful.


## hipblasLtMatrixLayoutSetAttribute()[#](#hipblasltmatrixlayoutsetattribute)

-
hipblasStatus_t hipblasLtMatrixLayoutSetAttribute(
[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matLayout,[hipblasLtMatrixLayoutAttribute_t](datatypes.html#_CPPv432hipblasLtMatrixLayoutAttribute_t)attr, const void *buf, size_t sizeInBytes)[#](#_CPPv433hipblasLtMatrixLayoutSetAttribute23hipblasLtMatrixLayout_t32hipblasLtMatrixLayoutAttribute_tPKv6size_t) Set attribute to a matrix descriptor.

This function sets the value of the specified attribute belonging to a previously created matrix descriptor.

- Parameters:
**matLayout**–**[in]**Pointer to the previously created structure holding the matrix mdescriptor queried by this function. See[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**attr**–**[in]**The attribute that will be set by this function. See[hipblasLtMatrixLayoutAttribute_t](datatypes.html#group__types__module_1ga9028f2fddc41b1252dd5cd0b734182f5).**buf**–**[in]**The value to which the specified attribute should be set.**sizeInBytes**–**[in]**Size of buf buffer (in bytes) for verification.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the attribute was set successfully..**HIPBLAS_STATUS_INVALID_VALUE**– If`buf`

is NULL or`sizeInBytes`

doesn’t match the size of the internal storage for the selected attribute.



## hipblasLtMatrixLayoutGetAttribute()[#](#hipblasltmatrixlayoutgetattribute)

-
hipblasStatus_t hipblasLtMatrixLayoutGetAttribute(
[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)matLayout,[hipblasLtMatrixLayoutAttribute_t](datatypes.html#_CPPv432hipblasLtMatrixLayoutAttribute_t)attr, void *buf, size_t sizeInBytes, size_t *sizeWritten)[#](#_CPPv433hipblasLtMatrixLayoutGetAttribute23hipblasLtMatrixLayout_t32hipblasLtMatrixLayoutAttribute_tPv6size_tP6size_t) Query attribute from a matrix descriptor.

This function returns the value of the queried attribute belonging to a previously created matrix descriptor.

- Parameters:
**matLayout**–**[in]**Pointer to the previously created structure holding the matrix descriptor queried by this function. See[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**attr**–**[in]**The attribute that will be retrieved by this function. See[hipblasLtMatrixLayoutAttribute_t](datatypes.html#group__types__module_1ga9028f2fddc41b1252dd5cd0b734182f5).**buf**–**[out]**Memory address containing the attribute value retrieved by this function.**sizeInBytes**–**[in]**Size of`buf`

buffer (in bytes) for verification.**sizeWritten**–**[out]**Valid only when the return value is HIPBLAS_STATUS_SUCCESS. If sizeInBytes is non-zero: then sizeWritten is the number of bytes actually written; if sizeInBytes is 0: then sizeWritten is the number of bytes needed to write full contents.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If attribute’s value was successfully written to user memory.**HIPBLAS_STATUS_INVALID_VALUE**– If`sizeInBytes`

is 0 and`sizeWritten`

is NULL, or if`sizeInBytes`

is non-zero and`buf`

is NULL, or`sizeInBytes`

doesn’t match size of internal storage for the selected attribute.



## hipblasLtMatmulDescCreate()[#](#hipblasltmatmuldesccreate)

-
hipblasStatus_t hipblasLtMatmulDescCreate(
[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)*matmulDesc, hipblasComputeType_t computeType, hipDataType scaleType)[#](#_CPPv425hipblasLtMatmulDescCreateP21hipblasLtMatmulDesc_t20hipblasComputeType_t11hipDataType) Create a matrix multiply descriptor.

This function creates a matrix multiply descriptor by allocating the memory needed to hold its opaque structure.

- Parameters:
**matmulDesc**–**[out]**Pointer to the structure holding the matrix multiply descriptor created by this function. See[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**computeType**–**[in]**Enumerant that specifies the data precision for the matrix multiply descriptor this function creates. See hipblasComputeType_t .**scaleType**–**[in]**Enumerant that specifies the data precision for the matrix transform descriptor this function creates. See hipDataType.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the descriptor was created successfully.**HIPBLAS_STATUS_ALLOC_FAILED**– If the memory could not be allocated.



## hipblasLtMatmulDescDestroy()[#](#hipblasltmatmuldescdestroy)

-
hipblasStatus_t hipblasLtMatmulDescDestroy(const
[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmulDesc)[#](#_CPPv426hipblasLtMatmulDescDestroyK21hipblasLtMatmulDesc_t) Destory a matrix multiply descriptor.

This function destroys a previously created matrix multiply descriptor object.

- Parameters:
**matmulDesc**–**[in]**Pointer to the structure holding the matrix multiply descriptor that should be destroyed by this function. See[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).- Return values:
**HIPBLAS_STATUS_SUCCESS**– If operation was successful.


## hipblasLtMatmulDescSetAttribute()[#](#hipblasltmatmuldescsetattribute)

-
hipblasStatus_t hipblasLtMatmulDescSetAttribute(
[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmulDesc,[hipblasLtMatmulDescAttributes_t](datatypes.html#_CPPv431hipblasLtMatmulDescAttributes_t)attr, const void *buf, size_t sizeInBytes)[#](#_CPPv431hipblasLtMatmulDescSetAttribute21hipblasLtMatmulDesc_t31hipblasLtMatmulDescAttributes_tPKv6size_t) Set attribute to a matrix multiply descriptor.

This function sets the value of the specified attribute belonging to a previously created matrix multiply descriptor.

- Parameters:
**matmulDesc**–**[in]**Pointer to the previously created structure holding the matrix multiply descriptor queried by this function. See[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**attr**–**[in]**The attribute that will be set by this function. See[hipblasLtMatmulDescAttributes_t](datatypes.html#group__types__module_1gab818dece34ff0cf597b72b6c4c527b75).**buf**–**[in]**The value to which the specified attribute should be set.**sizeInBytes**–**[in]**Size of buf buffer (in bytes) for verification.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the attribute was set successfully..**HIPBLAS_STATUS_INVALID_VALUE**– If`buf`

is NULL or`sizeInBytes`

doesn’t match the size of the internal storage for the selected attribute.



## hipblasLtMatmulDescGetAttribute()[#](#hipblasltmatmuldescgetattribute)

-
hipblasStatus_t hipblasLtMatmulDescGetAttribute(
[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmulDesc,[hipblasLtMatmulDescAttributes_t](datatypes.html#_CPPv431hipblasLtMatmulDescAttributes_t)attr, void *buf, size_t sizeInBytes, size_t *sizeWritten)[#](#_CPPv431hipblasLtMatmulDescGetAttribute21hipblasLtMatmulDesc_t31hipblasLtMatmulDescAttributes_tPv6size_tP6size_t) Query attribute from a matrix multiply descriptor.

This function returns the value of the queried attribute belonging to a previously created matrix multiply descriptor.

- Parameters:
**matmulDesc**–**[in]**Pointer to the previously created structure holding the matrix multiply descriptor queried by this function. See[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**attr**–**[in]**The attribute that will be retrieved by this function. See[hipblasLtMatmulDescAttributes_t](datatypes.html#group__types__module_1gab818dece34ff0cf597b72b6c4c527b75).**buf**–**[out]**Memory address containing the attribute value retrieved by this function.**sizeInBytes**–**[in]**Size of`buf`

buffer (in bytes) for verification.**sizeWritten**–**[out]**Valid only when the return value is HIPBLAS_STATUS_SUCCESS. If sizeInBytes is non-zero: then sizeWritten is the number of bytes actually written; if sizeInBytes is 0: then sizeWritten is the number of bytes needed to write full contents.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If attribute’s value was successfully written to user memory.**HIPBLAS_STATUS_INVALID_VALUE**– If`sizeInBytes`

is 0 and`sizeWritten`

is NULL, or if`sizeInBytes`

is non-zero and`buf`

is NULL, or`sizeInBytes`

doesn’t match size of internal storage for the selected attribute.



## hipblasLtMatmulPreferenceCreate()[#](#hipblasltmatmulpreferencecreate)

-
hipblasStatus_t hipblasLtMatmulPreferenceCreate(
[hipblasLtMatmulPreference_t](datatypes.html#_CPPv427hipblasLtMatmulPreference_t)*pref)[#](#_CPPv431hipblasLtMatmulPreferenceCreateP27hipblasLtMatmulPreference_t) Create a preference descriptor.

This function creates a matrix multiply heuristic search preferences descriptor by allocating the memory needed to hold its opaque structure.

- Parameters:
**pref**–**[out]**Pointer to the structure holding the matrix multiply preferences descriptor created by this function. see[hipblasLtMatmulPreference_t](datatypes.html#group__types__module_1ga2fc030d19287f2c541a0f7d962b94e3b).- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the descriptor was created successfully.**HIPBLAS_STATUS_ALLOC_FAILED**– If memory could not be allocated.



## hipblasLtMatmulPreferenceDestroy()[#](#hipblasltmatmulpreferencedestroy)

-
hipblasStatus_t hipblasLtMatmulPreferenceDestroy(const
[hipblasLtMatmulPreference_t](datatypes.html#_CPPv427hipblasLtMatmulPreference_t)pref)[#](#_CPPv432hipblasLtMatmulPreferenceDestroyK27hipblasLtMatmulPreference_t) Destory a preferences descriptor.

This function destroys a previously created matrix multiply preferences descriptor object.

- Parameters:
**pref**–**[in]**Pointer to the structure holding the matrix multiply preferences descriptor that should be destroyed by this function. See[hipblasLtMatmulPreference_t](datatypes.html#group__types__module_1ga2fc030d19287f2c541a0f7d962b94e3b).- Return values:
**HIPBLAS_STATUS_SUCCESS**– If operation was successful.


## hipblasLtMatmulPreferenceSetAttribute()[#](#hipblasltmatmulpreferencesetattribute)

-
hipblasStatus_t hipblasLtMatmulPreferenceSetAttribute(
[hipblasLtMatmulPreference_t](datatypes.html#_CPPv427hipblasLtMatmulPreference_t)pref,[hipblasLtMatmulPreferenceAttributes_t](datatypes.html#_CPPv437hipblasLtMatmulPreferenceAttributes_t)attr, const void *buf, size_t sizeInBytes)[#](#_CPPv437hipblasLtMatmulPreferenceSetAttribute27hipblasLtMatmulPreference_t37hipblasLtMatmulPreferenceAttributes_tPKv6size_t) Set attribute to a preference descriptor.

This function sets the value of the specified attribute belonging to a previously created matrix multiply preferences descriptor.

- Parameters:
**pref**–**[in]**Pointer to the previously created structure holding the matrix multiply preferences descriptor queried by this function. See[hipblasLtMatmulPreference_t](datatypes.html#group__types__module_1ga2fc030d19287f2c541a0f7d962b94e3b)**attr**–**[in]**The attribute that will be set by this function. See[hipblasLtMatmulPreferenceAttributes_t](datatypes.html#group__types__module_1ga9592fb75d3077b5d87619f8983ebdd82).**buf**–**[in]**The value to which the specified attribute should be set.**sizeInBytes**–**[in]**Size of`buf`

buffer (in bytes) for verification.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the attribute was set successfully..**HIPBLAS_STATUS_INVALID_VALUE**– If`buf`

is NULL or`sizeInBytes`

doesn’t match the size of the internal storage for the selected attribute.



## hipblasLtMatmulPreferenceGetAttribute()[#](#hipblasltmatmulpreferencegetattribute)

-
hipblasStatus_t hipblasLtMatmulPreferenceGetAttribute(
[hipblasLtMatmulPreference_t](datatypes.html#_CPPv427hipblasLtMatmulPreference_t)pref,[hipblasLtMatmulPreferenceAttributes_t](datatypes.html#_CPPv437hipblasLtMatmulPreferenceAttributes_t)attr, void *buf, size_t sizeInBytes, size_t *sizeWritten)[#](#_CPPv437hipblasLtMatmulPreferenceGetAttribute27hipblasLtMatmulPreference_t37hipblasLtMatmulPreferenceAttributes_tPv6size_tP6size_t) Query attribute from a preference descriptor.

This function returns the value of the queried attribute belonging to a previously created matrix multiply heuristic search preferences descriptor.

- Parameters:
**pref**–**[in]**Pointer to the previously created structure holding the matrix multiply heuristic search preferences descriptor queried by this function. See[hipblasLtMatmulPreference_t](datatypes.html#group__types__module_1ga2fc030d19287f2c541a0f7d962b94e3b).**attr**–**[in]**The attribute that will be retrieved by this function. See[hipblasLtMatmulPreferenceAttributes_t](datatypes.html#group__types__module_1ga9592fb75d3077b5d87619f8983ebdd82).**buf**–**[out]**Memory address containing the attribute value retrieved by this function.**sizeInBytes**–**[in]**Size of`buf`

buffer (in bytes) for verification.**sizeWritten**–**[out]**Valid only when the return value is HIPBLAS_STATUS_SUCCESS. If sizeInBytes is non-zero: then sizeWritten is the number of bytes actually written; if sizeInBytes is 0: then sizeWritten is the number of bytes needed to write full contents.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If attribute’s value was successfully written to user memory.**HIPBLAS_STATUS_INVALID_VALUE**– If`sizeInBytes`

is 0 and`sizeWritten`

is NULL, or if`sizeInBytes`

is non-zero and`buf`

is NULL, or`sizeInBytes`

doesn’t match size of internal storage for the selected attribute.



## hipblasLtMatmulAlgoGetHeuristic()[#](#hipblasltmatmulalgogetheuristic)

-
hipblasStatus_t hipblasLtMatmulAlgoGetHeuristic(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmulDesc,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Adesc,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Bdesc,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Cdesc,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Ddesc,[hipblasLtMatmulPreference_t](datatypes.html#_CPPv427hipblasLtMatmulPreference_t)pref, int requestedAlgoCount,[hipblasLtMatmulHeuristicResult_t](datatypes.html#_CPPv432hipblasLtMatmulHeuristicResult_t)heuristicResultsArray[], int *returnAlgoCount)[#](#_CPPv431hipblasLtMatmulAlgoGetHeuristic17hipblasLtHandle_t21hipblasLtMatmulDesc_t23hipblasLtMatrixLayout_t23hipblasLtMatrixLayout_t23hipblasLtMatrixLayout_t23hipblasLtMatrixLayout_t27hipblasLtMatmulPreference_tiA_32hipblasLtMatmulHeuristicResult_tPi) Retrieve the possible algorithms.

This function retrieves the possible algorithms for the matrix multiply operation

[hipblasLtMatmul()](#group__library__module_1gabb645313f1f5e7839bb63e6f54fad93d)function with the given input matrices A, B and C, and the output matrix D. The output is placed in heuristicResultsArray[] in the order of increasing estimated compute time. Note that the wall duration increases if the requestedAlgoCount increases.- Parameters:
**handle**–**[in]**Pointer to the allocated hipBLASLt handle for the hipBLASLt context. See[hipblasLtHandle_t](datatypes.html#group__types__module_1ga7eadd4c418242a4d98a617cfd44fa12e).**matmulDesc**–**[in]**Handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**Adesc, Bdesc, Cdesc, Ddesc**–**[in]**Handles to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**pref**–**[in]**Pointer to the structure holding the heuristic search preferences descriptor. See[hipblasLtMatmulPreference_t](datatypes.html#group__types__module_1ga2fc030d19287f2c541a0f7d962b94e3b).**requestedAlgoCount**–**[in]**Size of the`heuristicResultsArray`

(in elements). This is the requested maximum number of algorithms to return.**heuristicResultsArray[]**–**[out]**Array containing the algorithm heuristics and associated runtime characteristics, returned by this function, in the order of increasing estimated compute time.**returnAlgoCount**–**[out]**Number of algorithms returned by this function. This is the number of`heuristicResultsArray`

elements written.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If query was successful. Inspect heuristicResultsArray[0 to (returnAlgoCount -1)].state for the status of the results.**HIPBLAS_STATUS_NOT_SUPPORTED**– If no heuristic function available for current configuration.**HIPBLAS_STATUS_INVALID_VALUE**– If`requestedAlgoCount`

is less or equal to zero.



## hipblasLtMatmul()[#](#hipblasltmatmul)

-
hipblasStatus_t hipblasLtMatmul(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)handle,[hipblasLtMatmulDesc_t](datatypes.html#_CPPv421hipblasLtMatmulDesc_t)matmulDesc, const void *alpha, const void *A,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Adesc, const void *B,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Bdesc, const void *beta, const void *C,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Cdesc, void *D,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Ddesc, const[hipblasLtMatmulAlgo_t](datatypes.html#_CPPv421hipblasLtMatmulAlgo_t)*algo, void *workspace, size_t workspaceSizeInBytes, hipStream_t stream)[#](#_CPPv415hipblasLtMatmul17hipblasLtHandle_t21hipblasLtMatmulDesc_tPKvPKv23hipblasLtMatrixLayout_tPKv23hipblasLtMatrixLayout_tPKvPKv23hipblasLtMatrixLayout_tPv23hipblasLtMatrixLayout_tPK21hipblasLtMatmulAlgo_tPv6size_t11hipStream_t) Retrieve the possible algorithms.

This function computes the matrix multiplication of matrices A and B to produce the output matrix D, according to the following operation:

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

are input scalars. Note: This function supports both in-place matrix multiplication (C == D and Cdesc == Ddesc) and out-of-place matrix multiplication (C != D, both matrices must have the same data type, number of rows, number of columns, batch size, and memory order). In the out-of-place case, the leading dimension of C can be different from the leading dimension of D. Specifically the leading dimension of C can be 0 to achieve row or column broadcast. If Cdesc is omitted, this function assumes it to be equal to Ddesc.- Parameters:
**handle**–**[in]**Pointer to the allocated hipBLASLt handle for the hipBLASLt context. See[hipblasLtHandle_t](datatypes.html#group__types__module_1ga7eadd4c418242a4d98a617cfd44fa12e).**matmulDesc**–**[in]**Handle to a previously created matrix multiplication descriptor of type[hipblasLtMatmulDesc_t](datatypes.html#group__types__module_1ga663dbc97c0c9d20c5792e050220f4a1b).**alpha, beta**–**[in]**Pointers to the scalars used in the multiplication.**Adesc, Bdesc, Cdesc, Ddesc**–**[in]**Handles to the previously created matrix layout descriptors of the type[hipblasLtMatrixLayout_t](datatypes.html#group__types__module_1gae0814e91393b7f1bd15b6c9fc4b55da4).**A, B, C**–**[in]**Pointers to the GPU memory associated with the corresponding descriptors`Adesc`

,`Bdesc`

and`Cdesc`

.**D**–**[out]**Pointer to the GPU memory associated with the descriptor`Ddesc`

.**algo**–**[in]**Handle for matrix multiplication algorithm to be used. See[hipblasLtMatmulAlgo_t](datatypes.html#structhipblas_lt_matmul_algo__t). When NULL, an implicit heuristics query with default search preferences will be performed to determine actual algorithm to use.**workspace**–**[in]**Pointer to the workspace buffer allocated in the GPU memory. Pointer must be 16B aligned (that is, lowest 4 bits of address must be 0).**workspaceSizeInBytes**–**[in]**Size of the workspace.**stream**–**[in]**The HIP stream where all the GPU work will be submitted.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– If the operation completed successfully.**HIPBLAS_STATUS_EXECUTION_FAILED**– If HIP reported an execution error from the device.**HIPBLAS_STATUS_ARCH_MISMATCH**– If the configured operation cannot be run using the selected device.**HIPBLAS_STATUS_NOT_SUPPORTED**– If the current implementation on the selected device doesn’t support the configured operation.**HIPBLAS_STATUS_INVALID_VALUE**– If the parameters are unexpectedly NULL, in conflict or in an impossible configuration. For example, when workspaceSizeInBytes is less than workspace required by the configured algo.**HIBLAS_STATUS_NOT_INITIALIZED**– If hipBLASLt handle has not been initialized.



## Supported data types[#](#supported-data-types)

`hipblasLtMatmul`

supports the following computeType, scaleType, Bias type, Atype/Btype, and Ctype/Dtype:

computeType |
scaleType/Bias type |
Atype/Btype |
Ctype/Dtype |
|---|---|---|---|
HIPBLAS_COMPUTE_32F |
HIP_R_32F |
HIP_R_32F |
HIP_R_32F |
HIPBLAS_COMPUTE_32F_FAST_TF32 |
HIP_R_32F |
HIP_R_32F |
HIP_R_32F |
HIPBLAS_COMPUTE_32F |
HIP_R_32F |
HIP_R_16F |
HIP_R_16F |
HIPBLAS_COMPUTE_32F |
HIP_R_32F |
HIP_R_16F |
HIP_R_32F |
HIPBLAS_COMPUTE_32F |
HIP_R_32F |
HIP_R_16BF |
HIP_R_16BF |

For `FP8`

type Matmul, hipBLASLt supports the type combinations shown in the following table:

This table uses simpler abbrieviations:

**FP16**means**HIP_R_16F****BF16**means**HIP_R_16BF****FP32**means**HIP_R_32F****FP8**means**HIP_R_8F_E4M3****BF8**means**HIP_R_8F_E5M2****FP8_FNUZ**means**HIP_R_8F_E4M3_FNUZ**and**BF8_FNUZ**means**HIP_R_8F_E5M2_FNUZ**

The table applies to all transpose types (NN/NT/TT/TN).

**Default bias type**indicates the type when the bias type is not explicitly specified.

Atype |
Btype |
Ctype |
Dtype |
computeType |
scaleA,B |
scaleC,D |
Bias type |
Default bias type |
|
|---|---|---|---|---|---|---|---|---|---|
FP8 |
FP8 |
FP16 |
FP16 |
FP32 |
Yes |
No |
FP32, FP16 |
FP16 |
|
BF16 |
BF16 |
FP32, BF16 |
BF16 |
||||||
FP32 |
FP32 |
FP32, BF16 |
BF16 |
||||||
FP8 |
FP8 |
Yes |
FP32, FP16 |
FP16 |
|||||
BF8 |
BF8 |
FP32, FP16 |
FP16 |
||||||
BF8 |
FP16 |
FP16 |
No |
FP32, FP16 |
FP16 |
||||
BF16 |
BF16 |
FP32, BF16 |
BF16 |
||||||
FP32 |
FP32 |
FP32, BF16 |
BF16 |
||||||
FP8 |
FP8 |
Yes |
FP32, FP16 |
FP16 |
|||||
BF8 |
BF8 |
FP32, FP16 |
FP16 |
||||||
BF8 |
FP8 |
FP16 |
FP16 |
No |
FP32, FP16 |
FP16 |
|||
BF16 |
BF16 |
FP32, BF16 |
BF16 |
||||||
FP32 |
FP32 |
FP32, BF16 |
BF16 |
||||||
FP8 |
FP8 |
Yes |
FP32, FP16 |
FP16 |
|||||
BF8 |
BF8 |
FP32, FP16 |
FP16 |
||||||
BF8 |
FP16 |
FP16 |
No |
FP32, FP16 |
FP16 |
||||
BF16 |
BF16 |
FP32, BF16 |
BF16 |
||||||
FP32 |
FP32 |
FP32, BF16 |
BF16 |
||||||
FP8 |
FP8 |
Yes |
FP32, FP16 |
FP16 |
|||||
BF8 |
BF8 |
FP32, FP16 |
FP16 |

To use special data ordering for `HIPBLASLT_ORDER_COL16_4R8`

and `HIPBLASLT_ORDER_COL16_4R16`

in `hipblasLtMatmul`

for the gfx94x architecture, choose one of these valid combinations of transposes and orders of input and output matrices:

Atype |
Btype |
CType |
DType |
opA |
opB |
orderA |
orderB |
orderC |
orderD |
|---|---|---|---|---|---|---|---|---|---|
FP8 |
FP8 |
FP16 |
FP16 |
T |
N |
HIPBLASLT_ORDER_COL16_4R16 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP8 |
FP8 |
BF16 |
BF16 |
T |
N |
HIPBLASLT_ORDER_COL16_4R16 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP16 |
FP16 |
FP32 |
FP32 |
T |
N |
HIPBLASLT_ORDER_COL16_4R8 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP16 |
FP16 |
FP16 |
FP16 |
T |
N |
HIPBLASLT_ORDER_COL16_4R8 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
BF16 |
BF16 |
BF16 |
BF16 |
T |
N |
HIPBLASLT_ORDER_COL16_4R8 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP8 |
FP8 |
FP16 |
FP16 |
T |
N |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL16_4R16 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP8 |
FP8 |
BF16 |
BF16 |
T |
N |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL16_4R16 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP16 |
FP16 |
FP32 |
FP32 |
T |
N |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL16_4R8 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
FP16 |
FP16 |
FP16 |
FP16 |
T |
N |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL16_4R8 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |
BF16 |
BF16 |
BF16 |
BF16 |
T |
N |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL16_4R8 |
HIPBLASLT_ORDER_COL |
HIPBLASLT_ORDER_COL |

There are restrictions on the supported problem sizes for the `HIP_R_4F_E2M1`

, `HIP_R_6F_E2M3`

, `HIP_R_6F_E3M2`

,
`HIP_R_8F_E4M3`

, and `HIP_R_8F_E5M2`

data types.
When `HIPBLASLT_MATMUL_DESC_A_SCALE_MODE`

and `HIPBLASLT_MATMUL_DESC_B_SCALE_MODE`

are both set
to `HIPBLASLT_MATMUL_MATRIX_SCALE_VEC32_UE8M0`

, the following restrictions apply:

Atype and Btype can be any combination of:

`HIP_R_8F_E4M3`

,`HIP_R_8F_E5M2`

,`HIP_R_6F_E2M3`

,`HIP_R_6F_E3M2`

, and`HIP_R_4F_E2M1`

.Ctype must be the same as Dtype.

Dtype can be any of the following:

`HIP_R_32F`

,`HIP_R_16F`

, or`HIP_R_16BF`

.`m % 16`

must be equal to`0`

.`n % 16`

must be equal to`0`

.`K % 128`

must be equal to`0`

.`B`

must be equal to`1`

.`opA`

must be equal to`T`

.`opB`

must be equal to`N`

.Epilogues are not supported.

The scaling data pointed to by

`HIPBLASLT_MATMUL_DESC_A_SCALE_POINTER`

must be stored in the same order as`A`

.The scaling data pointed to by

`HIPBLASLT_MATMUL_DESC_B_SCALE_POINTER`

must be stored in the same order as`B`

.

## hipblasLtMatrixTransformDescCreate()[#](#hipblasltmatrixtransformdesccreate)

-
hipblasStatus_t hipblasLtMatrixTransformDescCreate(
[hipblasLtMatrixTransformDesc_t](datatypes.html#_CPPv430hipblasLtMatrixTransformDesc_t)*transformDesc, hipDataType scaleType)[#](#_CPPv434hipblasLtMatrixTransformDescCreateP30hipblasLtMatrixTransformDesc_t11hipDataType) Create new matrix transform operation descriptor.

- Return values:
**HIPBLAS_STATUS_ALLOC_FAILED**– if memory could not be allocated**HIPBLAS_STATUS_SUCCESS**– if desciptor was created successfully



## hipblasLtMatrixTransformDescDestroy()[#](#hipblasltmatrixtransformdescdestroy)

-
hipblasStatus_t hipblasLtMatrixTransformDescDestroy(
[hipblasLtMatrixTransformDesc_t](datatypes.html#_CPPv430hipblasLtMatrixTransformDesc_t)transformDesc)[#](#_CPPv435hipblasLtMatrixTransformDescDestroy30hipblasLtMatrixTransformDesc_t) Destroy matrix transform operation descriptor.

- Return values:
**HIPBLAS_STATUS_SUCCESS**– if operation was successful


## hipblasLtMatrixTransformDescSetAttribute()[#](#hipblasltmatrixtransformdescsetattribute)

-
hipblasStatus_t hipblasLtMatrixTransformDescSetAttribute(
[hipblasLtMatrixTransformDesc_t](datatypes.html#_CPPv430hipblasLtMatrixTransformDesc_t)transformDesc, hipblasLtMatrixTransformDescAttributes_t attr, const void *buf, size_t sizeInBytes)[#](#_CPPv440hipblasLtMatrixTransformDescSetAttribute30hipblasLtMatrixTransformDesc_t40hipblasLtMatrixTransformDescAttributes_tPKv6size_t) Set matrix transform operation descriptor attribute.

- Parameters:
**transformDesc**–**[in]**The descriptor**attr**–**[in]**The attribute**buf**–**[in]**memory address containing the new value**sizeInBytes**–**[in]**size of buf buffer for verification (in bytes)

- Return values:
**HIPBLAS_STATUS_INVALID_VALUE**– if buf is NULL or sizeInBytes doesn’t match size of internal storage for selected attribute**HIPBLAS_STATUS_SUCCESS**– if attribute was set successfully



## hipblasLtMatrixTransformDescGetAttribute()[#](#hipblasltmatrixtransformdescgetattribute)

-
hipblasStatus_t hipblasLtMatrixTransformDescGetAttribute(
[hipblasLtMatrixTransformDesc_t](datatypes.html#_CPPv430hipblasLtMatrixTransformDesc_t)transformDesc, hipblasLtMatrixTransformDescAttributes_t attr, void *buf, size_t sizeInBytes, size_t *sizeWritten)[#](#_CPPv440hipblasLtMatrixTransformDescGetAttribute30hipblasLtMatrixTransformDesc_t40hipblasLtMatrixTransformDescAttributes_tPv6size_tP6size_t) Matrix transform operation getter.

Get matrix transform operation descriptor attribute.

- Parameters:
**transformDesc**–**[in]**The descriptor**attr**–**[in]**The attribute**buf**–**[out]**memory address containing the new value**sizeInBytes**–**[in]**size of buf buffer for verification (in bytes)**sizeWritten**–**[out]**only valid when return value is HIPBLAS_STATUS_SUCCESS. If sizeInBytes is non-zero: number of bytes actually written, if sizeInBytes is 0: number of bytes needed to write full contents

- Return values:
**HIPBLAS_STATUS_INVALID_VALUE**– if sizeInBytes is 0 and sizeWritten is NULL, or if sizeInBytes is non-zero and buf is NULL or sizeInBytes doesn’t match size of internal storage for selected attribute**HIPBLAS_STATUS_SUCCESS**– if attribute’s value was successfully written to user memory



## hipblasLtMatrixTransform()[#](#hipblasltmatrixtransform)

-
hipblasStatus_t hipblasLtMatrixTransform(
[hipblasLtHandle_t](datatypes.html#_CPPv417hipblasLtHandle_t)lightHandle,[hipblasLtMatrixTransformDesc_t](datatypes.html#_CPPv430hipblasLtMatrixTransformDesc_t)transformDesc, const void *alpha, const void *A,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Adesc, const void *beta, const void *B,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Bdesc, void *C,[hipblasLtMatrixLayout_t](datatypes.html#_CPPv423hipblasLtMatrixLayout_t)Cdesc, hipStream_t stream)[#](#_CPPv424hipblasLtMatrixTransform17hipblasLtHandle_t30hipblasLtMatrixTransformDesc_tPKvPKv23hipblasLtMatrixLayout_tPKvPKv23hipblasLtMatrixLayout_tPv23hipblasLtMatrixLayout_t11hipStream_t) Matrix layout conversion helper.

Matrix layout conversion helper (C = alpha * op(A) + beta * op(B)), can be used to change memory order of data or to scale and shift the values.

- Parameters:
**lightHandle**–**[in]**Pointer to the allocated hipBLASLt handle for the hipBLASLt context. See[hipblasLtHandle_t](datatypes.html#group__types__module_1ga7eadd4c418242a4d98a617cfd44fa12e).**transformDesc**–**[in]**Pointer to allocated matrix transform descriptor.**alpha**–**[in]**Pointer to scalar alpha, either pointer to host or device address.**A**–**[in]**Pointer to matrix A, must be pointer to device address.**Adesc**–**[in]**Pointer to layout for input matrix A.**beta**–**[in]**Pointer to scalar beta, either pointer to host or device address.**B**–**[in]**Pointer to layout for matrix B, must be pointer to device address**Bdesc**–**[in]**Pointer to layout for inputmatrix B.**C**–**[in]**Pointer to matrix C, must be pointer to device address**Cdesc**–**[out]**Pointer to layout for output matrix C.**stream**–**[in]**The HIP stream where all the GPU work will be submitted.

- Return values:
**HIPBLAS_STATUS_NOT_INITIALIZED**– if hipBLASLt handle has not been initialized**HIPBLAS_STATUS_INVALID_VALUE**– if parameters are in conflict or in an impossible configuration; e.g. when A is not NULL, but Adesc is NULL**HIPBLAS_STATUS_NOT_SUPPORTED**– if current implementation on selected device doesn’t support configured operation**HIPBLAS_STATUS_ARCH_MISMATCH**– if configured operation cannot be run using selected device**HIPBLAS_STATUS_EXECUTION_FAILED**– if HIP reported execution error from the device**HIPBLAS_STATUS_SUCCESS**– if the operation completed successfully



`hipblasLtMatrixTransform`

supports the following Atype/Btype/Ctype and scaleType:

Atype/Btype/Ctype |
scaleType |
|---|---|
HIP_R_32F |
HIP_R_32F |
HIP_R_16F |
HIP_R_32F/HIP_R_16F |
HIP_R_16BF |
HIP_R_32F |
HIP_R_8I |
HIP_R_32F |
HIP_R_32I |
HIP_R_32F |
