---
title: "hipFFT API usage &#8212; hipFFT 1.0.22 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipFFT/en/latest/reference/hipfft-api-usage.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:07:17.749680+00:00
content_hash: "adc8df89df3da7bf"
---

# hipFFT API usage[#](#hipfft-api-usage)

This section describes how to use the hipFFT library API. The hipFFT
API follows the NVIDIA CUDA [cuFFT](https://docs.nvidia.com/cuda/cufft/) API.

## Data types[#](#data-types)

There are a few data structures that are internal to the library. The pointer types to these structures are listed below. Use these types to create handles and pass them between different library functions.

-
HIPFFT_FORWARD
[#](#c.HIPFFT_FORWARD) Perform a forward FFT.


-
HIPFFT_BACKWARD
[#](#c.HIPFFT_BACKWARD) Perform a backward/inverse FFT.


-
enum hipfftType
[#](#_CPPv410hipfftType) Transform type.

This type is used to declare the Fourier transform type that will be executed.

*Values:*-
enumerator HIPFFT_R2C
[#](#_CPPv4N10hipfftType10HIPFFT_R2CE) Real to complex (interleaved)


-
enumerator HIPFFT_C2R
[#](#_CPPv4N10hipfftType10HIPFFT_C2RE) Complex (interleaved) to real


-
enumerator HIPFFT_C2C
[#](#_CPPv4N10hipfftType10HIPFFT_C2CE) Complex to complex (interleaved)


-
enumerator HIPFFT_D2Z
[#](#_CPPv4N10hipfftType10HIPFFT_D2ZE) Double to double-complex (interleaved)


-
enumerator HIPFFT_Z2D
[#](#_CPPv4N10hipfftType10HIPFFT_Z2DE) Double-complex (interleaved) to double


-
enumerator HIPFFT_Z2Z
[#](#_CPPv4N10hipfftType10HIPFFT_Z2ZE) Double-complex to double-complex (interleaved)


-
enumerator HIPFFT_R2C

-
typedef struct hipfftHandle_t *hipfftHandle
[#](#_CPPv412hipfftHandle)

-
enum hipfftResult
[#](#_CPPv412hipfftResult) Result/status/error codes.

*Values:*-
enumerator HIPFFT_SUCCESS
[#](#_CPPv4N12hipfftResult14HIPFFT_SUCCESSE) hipFFT operation was successful


-
enumerator HIPFFT_INVALID_PLAN
[#](#_CPPv4N12hipfftResult19HIPFFT_INVALID_PLANE) hipFFT was passed an invalid plan handle


-
enumerator HIPFFT_ALLOC_FAILED
[#](#_CPPv4N12hipfftResult19HIPFFT_ALLOC_FAILEDE) hipFFT failed to allocate GPU or CPU memory


-
enumerator HIPFFT_INVALID_TYPE
[#](#_CPPv4N12hipfftResult19HIPFFT_INVALID_TYPEE) No longer used


-
enumerator HIPFFT_INVALID_VALUE
[#](#_CPPv4N12hipfftResult20HIPFFT_INVALID_VALUEE) User specified an invalid pointer or parameter


-
enumerator HIPFFT_INTERNAL_ERROR
[#](#_CPPv4N12hipfftResult21HIPFFT_INTERNAL_ERRORE) Driver or internal hipFFT library error


-
enumerator HIPFFT_EXEC_FAILED
[#](#_CPPv4N12hipfftResult18HIPFFT_EXEC_FAILEDE) Failed to execute an FFT on the GPU


-
enumerator HIPFFT_SETUP_FAILED
[#](#_CPPv4N12hipfftResult19HIPFFT_SETUP_FAILEDE) hipFFT failed to initialize


-
enumerator HIPFFT_INVALID_SIZE
[#](#_CPPv4N12hipfftResult19HIPFFT_INVALID_SIZEE) User specified an invalid transform size


-
enumerator HIPFFT_UNALIGNED_DATA
[#](#_CPPv4N12hipfftResult21HIPFFT_UNALIGNED_DATAE) No longer used


-
enumerator HIPFFT_INCOMPLETE_PARAMETER_LIST
[#](#_CPPv4N12hipfftResult32HIPFFT_INCOMPLETE_PARAMETER_LISTE) Missing parameters in call


-
enumerator HIPFFT_INVALID_DEVICE
[#](#_CPPv4N12hipfftResult21HIPFFT_INVALID_DEVICEE) Execution of a plan was on different GPU than plan creation


-
enumerator HIPFFT_PARSE_ERROR
[#](#_CPPv4N12hipfftResult18HIPFFT_PARSE_ERRORE) Internal plan database error


-
enumerator HIPFFT_NO_WORKSPACE
[#](#_CPPv4N12hipfftResult19HIPFFT_NO_WORKSPACEE) No workspace has been provided prior to plan execution


-
enumerator HIPFFT_NOT_IMPLEMENTED
[#](#_CPPv4N12hipfftResult22HIPFFT_NOT_IMPLEMENTEDE) Function does not implement functionality for parameters given.


-
enumerator HIPFFT_NOT_SUPPORTED
[#](#_CPPv4N12hipfftResult20HIPFFT_NOT_SUPPORTEDE) Operation is not supported for parameters given.


-
enumerator HIPFFT_SUCCESS

### Precision types[#](#precision-types)

This section describes the precision types that are supported as inputs and outputs in hipFFT.

-
typedef hipComplex hipfftComplex
[#](#_CPPv413hipfftComplex) Single-precision floating point complex type.


-
typedef hipDoubleComplex hipfftDoubleComplex
[#](#_CPPv419hipfftDoubleComplex) Double-precision floating point complex type.


-
typedef float hipfftReal
[#](#_CPPv410hipfftReal) Single-precision floating point type.


-
typedef double hipfftDoubleReal
[#](#_CPPv416hipfftDoubleReal) Double-precision floating point type.


## Simple plans[#](#simple-plans)

These planning routines allocate a plan for you. If execution of the plan requires a work buffer, it will be created and destroyed automatically.

-
[hipfftResult](#_CPPv412hipfftResult)hipfftPlan1d([hipfftHandle](#_CPPv412hipfftHandle)*plan, int nx,[hipfftType](#_CPPv410hipfftType)type, int batch)[#](#_CPPv412hipfftPlan1dP12hipfftHandlei10hipfftTypei) Create a new one-dimensional FFT plan.

Allocate and initialize a new one-dimensional FFT plan.

- Parameters:
**plan**–**[out]**Pointer to the FFT plan handle.**nx**–**[in]**FFT length.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to compute.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftPlan2d([hipfftHandle](#_CPPv412hipfftHandle)*plan, int nx, int ny,[hipfftType](#_CPPv410hipfftType)type)[#](#_CPPv412hipfftPlan2dP12hipfftHandleii10hipfftType) Create a new two-dimensional FFT plan.

Allocate and initialize a new two-dimensional FFT plan. Two-dimensional data should be stored in C ordering (row-major format), so that indexes in y-direction (j index) vary the fastest.

- Parameters:
**plan**–**[out]**Pointer to the FFT plan handle.**nx**–**[in]**Number of elements in the x-direction (slow index).**ny**–**[in]**Number of elements in the y-direction (fast index).**type**–**[in]**FFT type.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftPlan3d([hipfftHandle](#_CPPv412hipfftHandle)*plan, int nx, int ny, int nz,[hipfftType](#_CPPv410hipfftType)type)[#](#_CPPv412hipfftPlan3dP12hipfftHandleiii10hipfftType) Create a new three-dimensional FFT plan.

Allocate and initialize a new three-dimensional FFT plan. Three-dimensional data should be stored in C ordering (row-major format), so that indexes in z-direction (k index) vary the fastest.

- Parameters:
**plan**–**[out]**Pointer to the FFT plan handle.**nx**–**[in]**Number of elements in the x-direction (slowest index).**ny**–**[in]**Number of elements in the y-direction.**nz**–**[in]**Number of elements in the z-direction (fastest index).**type**–**[in]**FFT type.



### User managed simple plans[#](#user-managed-simple-plans)

These planning routines assume that you have allocated a plan
(`hipfftHandle`

) yourself and that you will manage a work area.

-
[hipfftResult](#_CPPv412hipfftResult)hipfftCreate([hipfftHandle](#_CPPv412hipfftHandle)*plan)[#](#_CPPv412hipfftCreateP12hipfftHandle) Allocate a new plan.

- Parameters:
**plan**–**[out]**Pointer to the FFT plan handle to be allocated.


-
[hipfftResult](#_CPPv412hipfftResult)hipfftDestroy([hipfftHandle](#_CPPv412hipfftHandle)plan)[#](#_CPPv413hipfftDestroy12hipfftHandle) Destroy and deallocate an existing plan.

- Parameters:
**plan**–**[in]**Handle of the FFT plan to be destroyed.


-
[hipfftResult](#_CPPv412hipfftResult)hipfftSetAutoAllocation([hipfftHandle](#_CPPv412hipfftHandle)plan, int autoAllocate)[#](#_CPPv423hipfftSetAutoAllocation12hipfftHandlei) Set the plan’s auto-allocation flag. The plan will allocate its own workarea.

- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**autoAllocate**–**[in]**0 to disable auto-allocation, non-zero to enable.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftMakePlan1d([hipfftHandle](#_CPPv412hipfftHandle)plan, int nx,[hipfftType](#_CPPv410hipfftType)type, int batch, size_t *workSize)[#](#_CPPv416hipfftMakePlan1d12hipfftHandlei10hipfftTypeiP6size_t) Initialize a new one-dimensional FFT plan.

Assumes that the plan has been created already, and modifies the plan associated with the plan handle.

- Parameters:
**plan**–**[in]**Handle of the FFT plan.**nx**–**[in]**FFT length.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to compute.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftMakePlan2d([hipfftHandle](#_CPPv412hipfftHandle)plan, int nx, int ny,[hipfftType](#_CPPv410hipfftType)type, size_t *workSize)[#](#_CPPv416hipfftMakePlan2d12hipfftHandleii10hipfftTypeP6size_t) Initialize a new two-dimensional FFT plan.

Assumes that the plan has been created already, and modifies the plan associated with the plan handle. Two-dimensional data should be stored in C ordering (row-major format), so that indexes in y-direction (j index) vary the fastest.

- Parameters:
**plan**–**[in]**Handle of the FFT plan.**nx**–**[in]**Number of elements in the x-direction (slow index).**ny**–**[in]**Number of elements in the y-direction (fast index).**type**–**[in]**FFT type.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftMakePlan3d([hipfftHandle](#_CPPv412hipfftHandle)plan, int nx, int ny, int nz,[hipfftType](#_CPPv410hipfftType)type, size_t *workSize)[#](#_CPPv416hipfftMakePlan3d12hipfftHandleiii10hipfftTypeP6size_t) Initialize a new two-dimensional FFT plan.

Assumes that the plan has been created already, and modifies the plan associated with the plan handle. Three-dimensional data should be stored in C ordering (row-major format), so that indexes in z-direction (k index) vary the fastest.

- Parameters:
**plan**–**[in]**Handle of the FFT plan.**nx**–**[in]**Number of elements in the x-direction (slowest index).**ny**–**[in]**Number of elements in the y-direction.**nz**–**[in]**Number of elements in the z-direction (fastest index).**type**–**[in]**FFT type.**workSize**–**[out]**Pointer to work area size (returned value).



## Advanced plans[#](#advanced-plans)

-
[hipfftResult](#_CPPv412hipfftResult)hipfftMakePlanMany([hipfftHandle](#_CPPv412hipfftHandle)plan, int rank, int *n, int *inembed, int istride, int idist, int *onembed, int ostride, int odist,[hipfftType](#_CPPv410hipfftType)type, int batch, size_t *workSize)[#](#_CPPv418hipfftMakePlanMany12hipfftHandleiPiPiiiPiii10hipfftTypeiP6size_t) Initialize a new batched rank-dimensional FFT plan with advanced data layout.

Assumes that the plan has been created already, and modifies the plan associated with the plan handle. The number of elements to transform in each direction of the input data in the FFT plan is specified in n.

The batch parameter tells hipFFT how many transforms to perform. The distance between the first elements of two consecutive batches of the input and output data are specified with the idist and odist parameters.

The inembed and onembed parameters define the input and output data layouts. The number of elements in the data is assumed to be larger than the number of elements in the transform. Strided data layouts are also supported. Strides along the fastest direction in the input and output data are specified via the istride and ostride parameters.

If both inembed and onembed parameters are set to NULL, all the advanced data layout parameters are ignored and reverted to default values, i.e., the batched transform is performed with non-strided data access and the number of data/transform elements are assumed to be equivalent.

- Parameters:
**plan**–**[out]**Pointer to the FFT plan handle.**rank**–**[in]**Dimension of transform (1, 2, or 3).**n**–**[in]**Number of elements to transform in the x/y/z directions.**inembed**–**[in]**Number of elements in the input data in the x/y/z directions.**istride**–**[in]**Distance between two successive elements in the input data.**idist**–**[in]**Distance between input batches.**onembed**–**[in]**Number of elements in the output data in the x/y/z directions.**ostride**–**[in]**Distance between two successive elements in the output data.**odist**–**[in]**Distance between output batches.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtMakePlanMany([hipfftHandle](#_CPPv412hipfftHandle)plan, int rank, long long int *n, long long int *inembed, long long int istride, long long int idist, hipDataType inputType, long long int *onembed, long long int ostride, long long int odist, hipDataType outputType, long long int batch, size_t *workSize, hipDataType executionType)[#](#_CPPv420hipfftXtMakePlanMany12hipfftHandleiPxPxxx11hipDataTypePxxx11hipDataTypexP6size_t11hipDataType) Initialize a batched rank-dimensional FFT plan with advanced data layout and specified input, output, execution data types.

Assumes that the plan has been created already, and modifies the plan associated with the plan handle. The number of elements to transform in each direction of the input data in the FFT plan is specified in n.

The batch parameter tells hipFFT how many transforms to perform. The distance between the first elements of two consecutive batches of the input and output data are specified with the idist and odist parameters.

The inembed and onembed parameters define the input and output data layouts. The number of elements in the data is assumed to be larger than the number of elements in the transform. Strided data layouts are also supported. Strides along the fastest direction in the input and output data are specified via the istride and ostride parameters.

If both inembed and onembed parameters are set to NULL, all the advanced data layout parameters are ignored and reverted to default values, i.e., the batched transform is performed with non-strided data access and the number of data/transform elements are assumed to be

equivalent.

The inputType, outputType, executionType parameters specify the data types (precision, and whether the data is real-valued or complex-valued) of the transform input, output, and internal representation respectively. Currently, the precision of all three parameters must match, and the execution type must always be complex-valued. At least one of inputType and outputType must be complex. A half-precision transform can be requested by using either the HIP_R_16F or HIP_C_16F types.

- Parameters:
**plan**–**[out]**Pointer to the FFT plan handle.**rank**–**[in]**Dimension of transform (1, 2, or 3).**n**–**[in]**Number of elements to transform in the x/y/z directions.**inembed**–**[in]**Number of elements in the input data in the x/y/z directions.**istride**–**[in]**Distance between two successive elements in the input data.**idist**–**[in]**Distance between input batches.**inputType**–**[in]**Format of FFT input.**onembed**–**[in]**Number of elements in the output data in the x/y/z directions.**ostride**–**[in]**Distance between two successive elements in the output data.**odist**–**[in]**Distance between output batches.**outputType**–**[in]**Format of FFT output.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).**executionType**–**[in]**Internal data format used by the library during computation.



## Estimating work area sizes[#](#estimating-work-area-sizes)

These calls return estimates of the work area required to support a
plan generated with the same parameters (either with the simple or
extensible API). Applications that manage the work area allocation
themselves must use this call after plan generation and
after any `hipfftSet*()`

calls subsequent to the plan generation if those
calls can alter the required work space size.

-
[hipfftResult](#_CPPv412hipfftResult)hipfftEstimate1d(int nx,[hipfftType](#_CPPv410hipfftType)type, int batch, size_t *workSize)[#](#_CPPv416hipfftEstimate1di10hipfftTypeiP6size_t) Return an estimate of the work area size required for a 1D plan.

- Parameters:
**nx**–**[in]**Number of elements in the x-direction.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftEstimate2d(int nx, int ny,[hipfftType](#_CPPv410hipfftType)type, size_t *workSize)[#](#_CPPv416hipfftEstimate2dii10hipfftTypeP6size_t) Return an estimate of the work area size required for a 2D plan.

- Parameters:
**nx**–**[in]**Number of elements in the x-direction.**ny**–**[in]**Number of elements in the y-direction.**type**–**[in]**FFT type.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftEstimate3d(int nx, int ny, int nz,[hipfftType](#_CPPv410hipfftType)type, size_t *workSize)[#](#_CPPv416hipfftEstimate3diii10hipfftTypeP6size_t) Return an estimate of the work area size required for a 3D plan.

- Parameters:
**nx**–**[in]**Number of elements in the x-direction.**ny**–**[in]**Number of elements in the y-direction.**nz**–**[in]**Number of elements in the z-direction.**type**–**[in]**FFT type.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftEstimateMany(int rank, int *n, int *inembed, int istride, int idist, int *onembed, int ostride, int odist,[hipfftType](#_CPPv410hipfftType)type, int batch, size_t *workSize)[#](#_CPPv418hipfftEstimateManyiPiPiiiPiii10hipfftTypeiP6size_t) Return an estimate of the work area size required for a rank-dimensional plan.

- Parameters:
**rank**–**[in]**Dimension of FFT transform (1, 2, or 3).**n**–**[in]**Number of elements in the x/y/z directions.**inembed**–**[in]****istride**–**[in]****idist**–**[in]**Distance between input batches.**onembed**–**[in]****ostride**–**[in]****odist**–**[in]**Distance between output batches.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).



### Accurate work area sizes[#](#accurate-work-area-sizes)

After plan generation is complete, an accurate work area size can be obtained using these routines.

-
[hipfftResult](#_CPPv412hipfftResult)hipfftGetSize1d([hipfftHandle](#_CPPv412hipfftHandle)plan, int nx,[hipfftType](#_CPPv410hipfftType)type, int batch, size_t *workSize)[#](#_CPPv415hipfftGetSize1d12hipfftHandlei10hipfftTypeiP6size_t) Return size of the work area size required for a 1D plan.

- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**nx**–**[in]**Number of elements in the x-direction.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftGetSize2d([hipfftHandle](#_CPPv412hipfftHandle)plan, int nx, int ny,[hipfftType](#_CPPv410hipfftType)type, size_t *workSize)[#](#_CPPv415hipfftGetSize2d12hipfftHandleii10hipfftTypeP6size_t) Return size of the work area size required for a 2D plan.

- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**nx**–**[in]**Number of elements in the x-direction.**ny**–**[in]**Number of elements in the y-direction.**type**–**[in]**FFT type.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftGetSize3d([hipfftHandle](#_CPPv412hipfftHandle)plan, int nx, int ny, int nz,[hipfftType](#_CPPv410hipfftType)type, size_t *workSize)[#](#_CPPv415hipfftGetSize3d12hipfftHandleiii10hipfftTypeP6size_t) Return size of the work area size required for a 3D plan.

- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**nx**–**[in]**Number of elements in the x-direction.**ny**–**[in]**Number of elements in the y-direction.**nz**–**[in]**Number of elements in the z-direction.**type**–**[in]**FFT type.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftGetSizeMany([hipfftHandle](#_CPPv412hipfftHandle)plan, int rank, int *n, int *inembed, int istride, int idist, int *onembed, int ostride, int odist,[hipfftType](#_CPPv410hipfftType)type, int batch, size_t *workSize)[#](#_CPPv417hipfftGetSizeMany12hipfftHandleiPiPiiiPiii10hipfftTypeiP6size_t) Return size of the work area size required for a rank-dimensional plan.

- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**rank**–**[in]**Dimension of FFT transform (1, 2, or 3).**n**–**[in]**Number of elements in the x/y/z directions.**inembed**–**[in]****istride**–**[in]****idist**–**[in]**Distance between input batches.**onembed**–**[in]****ostride**–**[in]****odist**–**[in]**Distance between output batches.**type**–**[in]**FFT type.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtGetSizeMany([hipfftHandle](#_CPPv412hipfftHandle)plan, int rank, long long int *n, long long int *inembed, long long int istride, long long int idist, hipDataType inputType, long long int *onembed, long long int ostride, long long int odist, hipDataType outputType, long long int batch, size_t *workSize, hipDataType executionType)[#](#_CPPv419hipfftXtGetSizeMany12hipfftHandleiPxPxxx11hipDataTypePxxx11hipDataTypexP6size_t11hipDataType) Return size of the work area size required for a rank-dimensional plan, with specified input, output, execution data types.

See

[hipfftXtMakePlanMany](#hipfft_xt_8h_1a8635fab320bc65b26477471df45fee8f)for restrictions on inputType, outputType, executionType parameters.- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**rank**–**[in]**Dimension of FFT transform (1, 2, or 3).**n**–**[in]**Number of elements in the x/y/z directions.**inembed**–**[in]**Number of elements in the input data in the x/y/z directions.**istride**–**[in]**Distance between two successive elements in the input data.**idist**–**[in]**Distance between input batches.**inputType**–**[in]**Format of FFT input.**onembed**–**[in]**Number of elements in the output data in the x/y/z directions.**ostride**–**[in]**Distance between two successive elements in the output data.**odist**–**[in]**Distance between output batches.**outputType**–**[in]**Format of FFT output.**batch**–**[in]**Number of batched transforms to perform.**workSize**–**[out]**Pointer to work area size (returned value).**executionType**–**[in]**Internal data format used by the library during computation.



## Executing plans[#](#executing-plans)

After you have created an FFT plan, you can execute it using one of the
`hipfftExec*`

functions.

-
[hipfftResult](#_CPPv412hipfftResult)hipfftExecC2C([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipfftComplex](#_CPPv413hipfftComplex)*idata,[hipfftComplex](#_CPPv413hipfftComplex)*odata, int direction)[#](#_CPPv413hipfftExecC2C12hipfftHandleP13hipfftComplexP13hipfftComplexi) Execute a (float) complex-to-complex FFT.

If the input and output buffers are equal, an in-place transform is performed.

- Parameters:
**plan**–**[in]**The FFT plan.**idata**–**[in]**Input data (on device).**odata**–**[out]**Output data (on device).**direction**–**[in]**Either`HIPFFT_FORWARD`

or`HIPFFT_BACKWARD`

.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftExecR2C([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipfftReal](#_CPPv410hipfftReal)*idata,[hipfftComplex](#_CPPv413hipfftComplex)*odata)[#](#_CPPv413hipfftExecR2C12hipfftHandleP10hipfftRealP13hipfftComplex) Execute a (float) real-to-complex FFT.

If the input and output buffers are equal, an in-place transform is performed.

- Parameters:
**plan**–**[in]**The FFT plan.**idata**–**[in]**Input data (on device).**odata**–**[out]**Output data (on device).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftExecC2R([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipfftComplex](#_CPPv413hipfftComplex)*idata,[hipfftReal](#_CPPv410hipfftReal)*odata)[#](#_CPPv413hipfftExecC2R12hipfftHandleP13hipfftComplexP10hipfftReal) Execute a (float) complex-to-real FFT.

If the input and output buffers are equal, an in-place transform is performed.

- Parameters:
**plan**–**[in]**The FFT plan.**idata**–**[in]**Input data (on device).**odata**–**[out]**Output data (on device).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftExecZ2Z([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipfftDoubleComplex](#_CPPv419hipfftDoubleComplex)*idata,[hipfftDoubleComplex](#_CPPv419hipfftDoubleComplex)*odata, int direction)[#](#_CPPv413hipfftExecZ2Z12hipfftHandleP19hipfftDoubleComplexP19hipfftDoubleComplexi) Execute a (double) complex-to-complex FFT.

If the input and output buffers are equal, an in-place transform is performed.

- Parameters:
**plan**–**[in]**The FFT plan.**idata**–**[in]**Input data (on device).**odata**–**[out]**Output data (on device).**direction**–**[in]**Either`HIPFFT_FORWARD`

or`HIPFFT_BACKWARD`

.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftExecD2Z([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipfftDoubleReal](#_CPPv416hipfftDoubleReal)*idata,[hipfftDoubleComplex](#_CPPv419hipfftDoubleComplex)*odata)[#](#_CPPv413hipfftExecD2Z12hipfftHandleP16hipfftDoubleRealP19hipfftDoubleComplex) Execute a (double) real-to-complex FFT.

If the input and output buffers are equal, an in-place transform is performed.

- Parameters:
**plan**–**[in]**The FFT plan.**idata**–**[in]**Input data (on device).**odata**–**[out]**Output data (on device).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftExecZ2D([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipfftDoubleComplex](#_CPPv419hipfftDoubleComplex)*idata,[hipfftDoubleReal](#_CPPv416hipfftDoubleReal)*odata)[#](#_CPPv413hipfftExecZ2D12hipfftHandleP19hipfftDoubleComplexP16hipfftDoubleReal) Execute a (double) complex-to-real FFT.

If the input and output buffers are equal, an in-place transform is performed.

- Parameters:
**plan**–**[in]**The FFT plan.**idata**–**[in]**Input data (on device).**odata**–**[out]**Output data (on device).



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExec([hipfftHandle](#_CPPv412hipfftHandle)plan, void *input, void *output, int direction)[#](#_CPPv412hipfftXtExec12hipfftHandlePvPvi) Execute an FFT plan for any precision and type.

An in-place transform is performed if the input and output pointers have the same value.

The direction parameter is ignored if for real-to-complex and complex-to-real transforms, as the direction is already implied by the data types.

- Parameters:
**plan**–**[in]**Pointer to the FFT plan.**input**–**[in]**Pointer to input data for the transform.**output**–**[in]**Pointer to output data for the transform.**direction**–**[in]**Either`HIPFFT_FORWARD`

or`HIPFFT_BACKWARD`

.



## HIP graph support for hipFFT[#](#hip-graph-support-for-hipfft)

hipFFT supports capturing kernels launched during FFT execution into HIP graph nodes. This way, you can capture the FFT execution and other work into a HIP graph and launch the work in the graph multiple times.

The following hipFFT APIs can be used with graph capture:

Note

Each launch of a HIP graph provides the same arguments to the kernels in the graph. This implies that all of the parameters to the above APIs remain valid while the HIP graph is in use, including:

The hipFFT plan

The input and output buffers


hipFFT does not support capturing work performed by other API functions other than those listed above.

## Callbacks[#](#callbacks)

-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtSetCallback([hipfftHandle](#_CPPv412hipfftHandle)plan, void **callbacks, hipfftXtCallbackType cbtype, void **callbackData)[#](#_CPPv419hipfftXtSetCallback12hipfftHandlePPv20hipfftXtCallbackTypePPv) Set a callback on a plan.

Set either a load or store callback to run with a plan. The type of callback is specified with the ‘cbtype’ parameter. An array ofcallback and callback data pointers must be given - one per device executing the plan.

- Parameters:
**plan**–**[in]**The FFT plan.**callbacks**–**[in]**Array of callback function pointers.**cbtype**–**[in]**Type of callback being set.**callbackData**–**[in]**Array of callback function data pointers



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtClearCallback([hipfftHandle](#_CPPv412hipfftHandle)plan, hipfftXtCallbackType cbtype)[#](#_CPPv421hipfftXtClearCallback12hipfftHandle20hipfftXtCallbackType) Remove a callback from a plan.

Remove a previously-set callback from a plan.

- Parameters:
**plan**–**[in]**The FFT plan.**cbtype**–**[in]**Type of callback being removed.



Set shared memory size for callback.

Set shared memory required for a callback. The callback of the specified type must have already been set on the plan.

- Parameters:
**plan**–**[in]**The FFT plan.**cbtype**–**[in]**Type of callback being modified.**sharedSize**–**[in]**Amount of shared memory required, in bytes.



## Single-process multi-GPU transforms[#](#single-process-multi-gpu-transforms)

hipFFT offers experimental support for distributing a transform across multiple GPUs in a single process.

To implement this functionality, use the API as follows:

Create a hipFFT plan handle using

.`hipfftCreate()`

Associate a set of GPU devices to the plan by calling

.`hipfftXtSetGPUs()`

Make the plan by calling one of:

`hipfftMakePlanMany64()`


Allocate memory for the data on the devices with

, which returns the allocated memory as a`hipfftXtMalloc()`

descriptor.`hipLibXtDesc`

Copy data from the host to the descriptor with

.`hipfftXtMemcpy()`

Execute the plan by calling one of:

Pass the descriptor as input and output.

Copy the output from the descriptor back to the host with

.`hipfftXtMemcpy()`

Free the descriptor using

.`hipfftXtFree()`

Clean up the plan by calling

.`hipfftDestroy()`


-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtSetGPUs([hipfftHandle](#_CPPv412hipfftHandle)plan, int count, int *gpus)[#](#_CPPv415hipfftXtSetGPUs12hipfftHandleiPi) Set multiple GPUs on a plan.

Instructs hipFFT to use multiple GPUs for a plan.

This function must be called after the plan is allocated using

[hipfftCreate](#hipfft_8h_1ac29ff23b8787a79ed3aeb7b9a4a96411), but before the plan is initialized by any of the “MakePlan” functions. Therefore, API functions that combine creation and initialization ([hipfftPlan1d](#hipfft_8h_1a161c62bdc08dcfa8ca37c220a82a8a8c),[hipfftPlan2d](#hipfft_8h_1a48f69945bde62d42c003f5dfd42d4c45),[hipfftPlan3d](#hipfft_8h_1aec4cf36f90582ece527d4633faca4693), and hipfftPlanMany) cannot use multiple GPUs.Warning

Experimental

- Parameters:
**plan**–**[inout]****count**–**[in]**length gpus array**gpus**–**[in]**array of ints specifying deviceIDs



-
struct hipXtDesc
[#](#_CPPv49hipXtDesc)

-
struct hipLibXtDesc
[#](#_CPPv412hipLibXtDesc)

-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtMalloc([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)**desc, hipfftXtSubFormat format)[#](#_CPPv414hipfftXtMalloc12hipfftHandlePP12hipLibXtDesc17hipfftXtSubFormat) Allocate memory on multiple devices.

Allocate memory on multiple devices for the specified plan. Returns a hipLibXtDesc_t descriptor which includes pointers to the allocated memory, devices that memory resides on, and sizes allocated.

The subformat indicates whether the memory will be used for FFT input or output.

The memory must be freed by calling

[hipfftXtFree](#hipfft_xt_8h_1a69db1daa9a85fb326a6b2b70c3f64dd9).Warning

Experimental

- Parameters:
**plan**–**[in]**FFT plan to allocate descriptor memory for.**desc**–**[out]**Pointer to descriptors for allocated memory, the devices used, and sizes.**format**–**[in]**Subformat determines whether memory is used for FFT input or output.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtFree([hipLibXtDesc](#_CPPv412hipLibXtDesc)*desc)[#](#_CPPv412hipfftXtFreeP12hipLibXtDesc) Free memory allocated by

[hipfftXtMalloc](#hipfft_xt_8h_1a56270d18a1e5709044f71849fe8cb1a4).Warning

Experimental

- Parameters:
**desc**–**[in]**Descriptor whose memory will be freed.


-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtMemcpy([hipfftHandle](#_CPPv412hipfftHandle)plan, void *dest, void *src, hipfftXtCopyType type)[#](#_CPPv414hipfftXtMemcpy12hipfftHandlePvPv16hipfftXtCopyType) Copy data to/from hipLibXtDesc_t descriptors.

Copy data according to the hipfftXtCopyType_t

HIPFFT_COPY_HOST_TO_DEVICE: dest points to a hipLibXtDesc_t structure that describes multi-device memory layout. src points to a host memory buffer.

HIPFFT_COPY_DEVICE_TO_HOST: src points to a hipLibXtDesc_t structure that describes multi-device memory layout. dest points to a host memory buffer.

HIPFFT_COPY_DEVICE_TO_DEVICE: Both dest and src point to a hipLibXtDesc_t structure that describes multi-device memory layout. The two structures must describe memory with the same number of devices and memory sizes.


Warning

Experimental

- Parameters:
**plan**–**[in]**Plan which has the descriptor.**dest**–**[out]**Buffer that will be populated.**src**–**[in]**Buffer that will be copied from.**type**–**[in]**Type of copy operation to perform.



-
*group*hipfftXtExecDescriptor Execute FFTs using hipLibXtDesc_t descriptors. Inputs and outputs are pointers to hipLibXtDesc_t descriptors. In-place transforms are performed by passing the same pointer for input and output.

Warning

Experimental

Functions

-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptorC2C([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output, int direction)[#](#_CPPv425hipfftXtExecDescriptorC2C12hipfftHandleP12hipLibXtDescP12hipLibXtDesci) Execute single-precision complex-to-complex transform.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.**direction**–**[in]**Either`HIPFFT_FORWARD`

or`HIPFFT_BACKWARD`

.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptorR2C([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output)[#](#_CPPv425hipfftXtExecDescriptorR2C12hipfftHandleP12hipLibXtDescP12hipLibXtDesc) Execute single-precision real forward transform.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptorC2R([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output)[#](#_CPPv425hipfftXtExecDescriptorC2R12hipfftHandleP12hipLibXtDescP12hipLibXtDesc) Execute single-precision real backward transform.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptorZ2Z([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output, int direction)[#](#_CPPv425hipfftXtExecDescriptorZ2Z12hipfftHandleP12hipLibXtDescP12hipLibXtDesci) Execute double-precision complex-to-complex transform.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.**direction**–**[in]**Either`HIPFFT_FORWARD`

or`HIPFFT_BACKWARD`

.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptorD2Z([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output)[#](#_CPPv425hipfftXtExecDescriptorD2Z12hipfftHandleP12hipLibXtDescP12hipLibXtDesc) Execute double-precision real forward transform.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptorZ2D([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output)[#](#_CPPv425hipfftXtExecDescriptorZ2D12hipfftHandleP12hipLibXtDescP12hipLibXtDesc) Execute double-precision real backward transform.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtExecDescriptor([hipfftHandle](#_CPPv412hipfftHandle)plan,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*input,[hipLibXtDesc](#_CPPv412hipLibXtDesc)*output, int direction)[#](#_CPPv422hipfftXtExecDescriptor12hipfftHandleP12hipLibXtDescP12hipLibXtDesci) Execute general transform - types of the descriptors must match the plan.

- Parameters:
**plan**–**[in]**The FFT plan.**input**–**[in]**Input data.**output**–**[out]**Output data.**direction**–**[in]**Either`HIPFFT_FORWARD`

or`HIPFFT_BACKWARD`

.



-

## Multi-process transforms[#](#multi-process-transforms)

hipFFT has experimental support for transforms that are distributed across MPI (Message Passing Interface) processes.

Support for MPI transforms was introduced in ROCm 6.4 as part of hipFFT 1.0.18.

MPI must be initialized before creating a multi-process hipFFT plan.

Note

hipFFT MPI support is only available when the library is built
with the `HIPFFT_MPI_ENABLE`

CMake option enabled. By default, MPI support
is off.

In addition, hipFFT MPI support requires the backend FFT library to also support MPI. This means that either an MPI-enabled rocFFT library or cuFFTMp must be used.

Finally, hipFFT API calls made on different ranks might return different values. You must take care to ensure that all ranks have successfully created their plans before attempting to execute a distributed transform. It’s possible for one rank to fail to create and execute a plan while the others succeed.

### Built-in decomposition[#](#built-in-decomposition)

hipFFT can automatically decide on the data decomposition for distributed transforms. The API usage is similar to the single-process, multi-GPU case described above.

On all ranks in the MPI communicator:

Create a hipFFT plan handle with

.`hipfftCreate()`

Attach the MPI communicator to the plan with

.`hipfftMpAttachComm()`

Make the plan by calling one of:

`hipfftMakePlanMany64()`



Note

Not all backend FFT libraries support distributing all transforms. Check the documentation for the backend FFT library for any restrictions on distributed transform types, placement, sizes, or data layouts.

Copy data from the host to the descriptor using

.`hipfftXtMemcpy()`

Execute the plan by calling one of:

Copy the output from the descriptor back to the host with

.`hipfftXtMemcpy()`

Free the descriptor with

.`hipfftXtFree()`

On all ranks in the MPI communicator, clean up the plan by calling

.`hipfftDestroy()`


### Custom decomposition[#](#custom-decomposition)

hipFFT also allows an arbitrary decomposition of the FFT into 1D, 2D, or
3D bricks. Each MPI rank calls [ hipfftXtSetDistribution()](#_CPPv423hipfftXtSetDistribution12hipfftHandleiPKxPKxPKxPKxPKxPKx)
during plan creation to declare which input and output brick resides
on that rank.

The same API calls are made on each rank in the MPI communicator as follows:

Create a hipFFT plan handle with

.`hipfftCreate()`

Attach the MPI communicator to the plan with

.`hipfftMpAttachComm()`

Call

to specify the input and output brick for the current rank.`hipfftXtSetDistribution()`

Bricks are specified by their lower and upper coordinates in the input/output index space. The lower coordinate is inclusive (contained within the brick) and the upper coordinate is exclusive (first index past the end of the brick).

Strides for the input/output data are also provided, to describe how the bricks are laid out in physical memory.

Each coordinate and stride contain the same number of elements as the number of dimensions in the FFT. This also implies that batched FFTs are not supported when using MPI, because the coordinates and strides do not contain information about the batch dimension.

Make the plan by calling one of:

The “PlanMany” APIs enable batched FFTs and are not usable with MPI.

Note

Not all backend FFT libraries support distributing all transforms. Consult the documentation for the backend FFT library for any restrictions on distributed transform types, placement, sizes, or data layouts.

Call

with`hipfftXtMalloc()`

`HIPFFT_XT_FORMAT_DISTRIBUTED_INPUT`

to allocate the input brick on the current rank. The allocated memory is returned as adescriptor.`hipLibXtDesc`

Call

with`hipfftXtMalloc()`

`HIPFFT_XT_FORMAT_DISTRIBUTED_OUTPUT`

to allocate the output brick on the current rank. The allocated memory is returned as adescriptor.`hipLibXtDesc`

Initialize the memory pointed to by the descriptor.

Execute the plan by calling one of:

Pass the input descriptor as input and the output descriptor as output.

Use the transformed data pointed to by the output descriptor.

Free the descriptors with

.`hipfftXtFree()`

Clean up the plan by calling

.`hipfftDestroy()`


-
[hipfftResult](#_CPPv412hipfftResult)hipfftMpAttachComm([hipfftHandle](#_CPPv412hipfftHandle)plan, hipfftMpCommType comm_type, void *comm_handle)[#](#_CPPv418hipfftMpAttachComm12hipfftHandle16hipfftMpCommTypePv) Set a multi-processing communicator on a plan.

Attach a multi-processing communication handle to a hipFFT plan. ‘comm_handle’ points to the handle, whose type depends on the multi-processing library being used. With MPI (Message Passing Interface) for example, ‘comm_handle’ points to an MPI communicator.

This function must only be called on a plan that has already been allocated by

[hipfftCreate](#hipfft_8h_1ac29ff23b8787a79ed3aeb7b9a4a96411), but before the plan is initialized with any of the ‘hipfftMakePlan’ functions.Warning

Experimental

- Parameters:
**plan**–**[in]**The FFT plan.**comm_type**–**[in]**Type of communication handle.**comm_handle**–**[in]**Pointer to the communication handle.



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtSetDistribution([hipfftHandle](#_CPPv412hipfftHandle)plan, int rank, const long long int *input_lower, const long long int *input_upper, const long long int *output_lower, const long long int *output_upper, const long long int *input_stride, const long long int *output_stride)[#](#_CPPv423hipfftXtSetDistribution12hipfftHandleiPKxPKxPKxPKxPKxPKx) Describe the partial input and output for a distributed transform in the current process.

For the given plan, describe the ‘brick’ of input and output that is distributed to the current process. A brick is defined with the lower and upper coordinates of the that brick in the global index space of the transform.

Strides for both the input and output bricks are also provided, to describe how the brick is laid out in memory.

All coordinates and strides are in row-major order, with the slowest-moving dimension specified first.

This function must only be called on a plan that has already been allocated by

[hipfftCreate](#hipfft_8h_1ac29ff23b8787a79ed3aeb7b9a4a96411), but before the plan is initialized with any of the ‘hipfftMakePlan’ functions.Warning

Experimental

- Parameters:
**plan**–**[in]**The FFT plan.**rank**–**[in]**Dimension of the transform**input_lower**–**[in]**Array of length rank, specifying the lower index (inclusive) for the brick in the FFT input.**input_upper**–**[in]**Array of length rank, specifying the upper index (exclusive) for the brick in the FFT input.**output_lower**–**[in]**Array of length rank, specifying the lower index (inclusive) for the brick in the FFT output.**output_upper**–**[in]**Array of length rank, specifying the upper index (exclusive) for the brick in the FFT output.**input_stride**–**[in]**Array of length rank specifying the input brick’s stride in memory**output_stride**–**[in]**Array of length rank specifying the output brick’s stride in memory



-
[hipfftResult](#_CPPv412hipfftResult)hipfftXtSetSubformatDefault([hipfftHandle](#_CPPv412hipfftHandle)plan, hipfftXtSubFormat subformat_forward, hipfftXtSubFormat subformat_inverse)[#](#_CPPv427hipfftXtSetSubformatDefault12hipfftHandle17hipfftXtSubFormat17hipfftXtSubFormat) Set the input and output formats for a distributed transform.

Specifies the distribution of data for each side of a distributed transform. Forward transforms use ‘subformat_forward’ to describe input and ‘subformat_inverse’ to describe output. Inverse transforms use ‘subformat_inverse’ to describe input and ‘subformat_forward’ to describe output.

‘subformat_forward’ and ‘subformat_inverse’ must be set to matching values. One may be HIPFFT_XT_FORMAT_INPLACE and the other HIPFFT_XT_FORMAT_INPLACE_SHUFFLED; Alternatively, one may be HIPFFT_XT_FORMAT_DISTRIBUTED_INPUT and the other HIPFFT_XT_FORMAT_DISTRIBUTED_OUTPUT.

This function must only be called on a plan that has already been allocated by

[hipfftCreate](#hipfft_8h_1ac29ff23b8787a79ed3aeb7b9a4a96411), but before the plan is initialized with any of the ‘hipfftMakePlan’ functions.Warning

Experimental

- Parameters:
**plan**–**[in]**The FFT plan.**subformat_forward**–**[in]**Format of the input for a forward transform.**subformat_inverse**–**[in]**Format of the input for an inverse transform.
