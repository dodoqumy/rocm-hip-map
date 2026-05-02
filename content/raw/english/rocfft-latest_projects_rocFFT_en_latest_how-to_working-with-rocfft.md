---
title: "Working with rocFFT &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/how-to/working-with-rocfft.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:53.862178+00:00
content_hash: "d12988f4d2acd17e"
---

# Working with rocFFT[#](#working-with-rocfft)

This topic describes how to use rocFFT, including how to structure the workflow, set up and clean up the library, and use plans, buffers, and batches.

## Workflow[#](#workflow)

To compute an FFT with rocFFT, first create a plan. A plan is a handle to an internal data structure that holds the details about the transform. After creating the plan, execute it with the specified data buffers using a separate API call. The execution step can be repeated with the same plan on different input/output buffers as needed. The plan is destroyed when it is no longer needed.

To perform a transform, follow these steps:

Initialize the library by calling

.`rocfft_setup()`

Create a plan for each distinct type of FFT that is required:

If the plan specification is simple, call

and specify the value of the fundamental parameters.`rocfft_plan_create()`

If the plan includes more details, first create a plan description using

. Call additional APIs, such as`rocfft_plan_description_create()`

, to specify the plan details. Then call`rocfft_plan_description_set_data_layout()`

, passing the description handle to it along with the other details.`rocfft_plan_create()`


Optionally, allocate a work buffer for the plan:

Call

to check the size of the work buffer required by the plan.`rocfft_plan_get_work_buffer_size()`

If a non-zero size is required:

Create an execution info object using

.`rocfft_execution_info_create()`

Allocate a buffer using

`hipMalloc`

and pass the allocated buffer to.`rocfft_execution_info_set_work_buffer()`



Execute the plan:

Use the execution API

to execute the actual computation on the data buffers specified.`rocfft_execute()`

Pass the extra execution information such as work buffers and compute streams to

in the`rocfft_execute()`

object.`rocfft_execution_info`

can be called repeatedly as needed for different data with the same plan.`rocfft_execute()`

If the plan requires a work buffer but one wasn’t provided,

automatically allocates a work buffer and frees it when execution is finished.`rocfft_execute()`


If a work buffer was allocated:

Call

`hipFree`

to free the work buffer.Call

to destroy the execution info object.`rocfft_execution_info_destroy()`


Destroy the plan by calling

.`rocfft_plan_destroy()`

Terminate the library by calling

.`rocfft_cleanup()`


### Example[#](#example)

```
#include <iostream>
#include <vector>
#include "hip/hip_runtime_api.h"
#include "hip/hip_vector_types.h"
#include "rocfft/rocfft.h"
int main()
{
// rocFFT gpu compute
// ========================================
rocfft_setup();
size_t N = 16;
size_t Nbytes = N * sizeof(float2);
// Create HIP device buffer
float2 *x;
hipMalloc(&x, Nbytes);
// Initialize data
std::vector<float2> cx(N);
for (size_t i = 0; i < N; i++)
{
cx[i].x = 1;
cx[i].y = -1;
}
// Copy data to device
hipMemcpy(x, cx.data(), Nbytes, hipMemcpyHostToDevice);
// Create rocFFT plan
rocfft_plan plan = nullptr;
size_t length = N;
rocfft_plan_create(&plan, rocfft_placement_inplace,
rocfft_transform_type_complex_forward, rocfft_precision_single,
1, &length, 1, nullptr);
// Check if the plan requires a work buffer
size_t work_buf_size = 0;
rocfft_plan_get_work_buffer_size(plan, &work_buf_size);
void* work_buf = nullptr;
rocfft_execution_info info = nullptr;
if(work_buf_size)
{
rocfft_execution_info_create(&info);
hipMalloc(&work_buf, work_buf_size);
rocfft_execution_info_set_work_buffer(info, work_buf, work_buf_size);
}
// Execute plan
rocfft_execute(plan, (void**) &x, nullptr, info);
// Wait for execution to finish
hipDeviceSynchronize();
// Clean up work buffer
if(work_buf_size)
{
hipFree(work_buf);
rocfft_execution_info_destroy(info);
}
// Destroy plan
rocfft_plan_destroy(plan);
// Copy result back to host
std::vector<float2> y(N);
hipMemcpy(y.data(), x, Nbytes, hipMemcpyDeviceToHost);
// Print results
for (size_t i = 0; i < N; i++)
{
std::cout << y[i].x << ", " << y[i].y << std::endl;
}
// Free device buffer
hipFree(x);
rocfft_cleanup();
return 0;
}
```

## Library setup and cleanup[#](#library-setup-and-cleanup)

At the beginning of the program, the function [ rocfft_setup()](../reference/allapi.html#_CPPv412rocfft_setupv) must be called before any of the library APIs. Similarly,
the function

[must be called at the end of the program. These APIs properly allocate and free the resources.](../reference/allapi.html#_CPPv414rocfft_cleanupv)

`rocfft_cleanup()`

## Plans[#](#plans)

A plan is a collection of most of the parameters needed to specify an FFT computation. A rocFFT plan includes the following information:

The type of transform (complex or real)

The dimension of the transform (1D, 2D, or 3D)

The length or extent of data in each dimension

The number of datasets that are transformed (batch size)

The floating-point precision of the data

Whether the transform is in-place or not in-place

The format (array type) of the input/output buffer

The layout of data in the input/output buffer

The scaling factor to apply to the output of the transform


A rocFFT plan does not include the following parameters:

The handles to the input and output data buffers.

The handle to a temporary work buffer (if needed).

Other information to control execution on the device.


These parameters are specified when the plan is executed.

## Data[#](#data)

You must allocate, initialize, and specify the input/output buffers that hold the data for the transform.
For larger transforms, temporary work buffers might be needed. Because the library tries to minimize its own allocation of
memory regions on the device, it expects you to manage the work buffers. The size of the buffer that is needed can be queried using
[ rocfft_plan_get_work_buffer_size()](../reference/allapi.html#_CPPv432rocfft_plan_get_work_buffer_sizeK11rocfft_planP6size_t). After allocation, it can be passed to the library using

[. The](../reference/allapi.html#_CPPv437rocfft_execution_info_set_work_buffer21rocfft_execution_infoPvK6size_t)

`rocfft_execution_info_set_work_buffer()`

[GitHub repository](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocfft/clients/samples)provide some samples and examples.

## Transform and array types[#](#transform-and-array-types)

There are two main types of FFTs in the library:

**Complex FFT**: Transformation of complex data (forward or backward). The library supports the following two array types to store complex numbers:Planar format: The real and imaginary components are kept in two separate arrays:

Buffer 1:

`RRRRR...`

Buffer 2:

`IIIII...`


Interleaved format: The real and imaginary components are stored as contiguous pairs in the same array:

Buffer:

`RIRIRIRIRIRI...`



**Real FFT**: Transformation of real data. For transforms involving real data, there are two possibilities:Real data being subject to a forward FFT that results in complex data (Hermitian).

Complex data (Hermitian) being subject to a backward FFT that results in real data.



Note

Real backward FFTs require Hermitian-symmetric input data, which would naturally happen in the output of a real forward FFT. rocFFT produces undefined results if this requirement is not met.

The library provides the [ rocfft_transform_type](../reference/allapi.html#_CPPv421rocfft_transform_type) and

[enumerations to specify transform and array types, respectively.](../reference/allapi.html#_CPPv417rocfft_array_type)

`rocfft_array_type`

## Batches[#](#batches)

The efficiency of the library is improved by batching the transforms. Sending as much data as possible in a single
transform call leverages the parallel compute capabilities of the GPU devices and minimizes the control transfer
penalty. It’s best to think of the GPU as a high-throughput, high-latency device, similar to a
high-bandwidth networking pipe with high ping response times. If the client
is ready to send data to the device to compute, it should send it using as few API calls as possible,
which can be accomplished by batching.
rocFFT plans can use the `number_of_transforms`

parameter (also referred to as the batch size)
in [ rocfft_plan_create()](../reference/allapi.html#_CPPv418rocfft_plan_createP11rocfft_plan23rocfft_result_placement21rocfft_transform_type16rocfft_precision6size_tPK6size_t6size_tK23rocfft_plan_description) to describe the number of transforms being requested.
All 1D, 2D, and 3D transforms can be batched.

## Result placement[#](#result-placement)

The API supports both in-place and not in-place transforms through the [ rocfft_result_placement](../reference/allapi.html#_CPPv423rocfft_result_placement) enumeration.
With in-place transforms, only the input buffers are provided to the
execution API. The resulting data is written to the same buffer, overwriting the input data.
With not in-place transforms, distinct
output buffers are provided, and the results are written into the output buffer.

Note

rocFFT can often overwrite the input buffers on real inverse (complex-to-real) transforms, even if they are requested as not in-place. By doing this, rocFFT is better able to optimize the FFT.

## Strides and distances[#](#strides-and-distances)

Strides and distances enable users to specify a custom layout for the data using [ rocfft_plan_description_set_data_layout()](../reference/allapi.html#_CPPv439rocfft_plan_description_set_data_layout23rocfft_plan_descriptionK17rocfft_array_typeK17rocfft_array_typePK6size_tPK6size_tK6size_tPK6size_tK6size_tK6size_tPK6size_tK6size_t).

For 1D data, if `strides[0] == strideX == 1`

, successive elements in the first dimension (dimension index `0`

) are stored
contiguously in memory. If `strideX`

is a value greater than `1`

, gaps in memory exist between each element of the vector.
For multidimensional cases, if `strides[1] == strideY == LenX`

for 2D data and `strides[2] == strideZ == LenX * LenY`

for 3D data,
no gaps exist in memory between each element, and all vectors are stored tightly packed in memory. Here, `LenX`

, `LenY`

, and `LenZ`

denote the
transform lengths `lengths[0]`

, `lengths[1]`

, and `lengths[2]`

, respectively, which are used to set up the plan.

Distance is the stride between corresponding elements of successive FFT data instances (primitives) in a batch.
Distance is measured in units of the memory type.
Complex data is measured in complex units and real data in real units. For tightly packed data,
the distance between FFT primitives is the size of the FFT primitive,
such that `dist == LenX`

for 1D data, `dist == LenX * LenY`

for 2D data, and `dist == LenX * LenY * LenZ`

for
3D data. It is possible to set the distance of a plan to be less than the size
of the FFT vector, which is typically `1`

when doing column (strided) access on packed data.

When computing
a batch of 1D FFT vectors, if `distance == 1`

and `strideX == length(vector)`

,
it means the data for each logical FFT is read along columns, in this case, along the batch. You must
verify that the distance and strides are valid and confirm that each logical
FFT instance does not overlap with any other in the output data. If this is not the case, undefined results
can occur. Overlapping on input data is generally allowed.

A simple example of a column data access pattern would be a 1D transform of length 4096 on
each row of an array of 1024 rows by 4096 columns of values stored in a column-major array,
for example, from a Fortran program. (This would be equivalent to a C or C++ program that
has an array of 4096 rows by 1024 columns stored in row-major format, where you
execute a 1D transform of length 4096 on each column.) In this case, specify the strides as `1024`

and the distance as `1`

.

## Overwriting non-contiguous buffers[#](#overwriting-non-contiguous-buffers)

rocFFT guarantees that both the reading of FFT input and the writing of FFT output respects the specified strides. However, temporary results can be written to these buffers contiguously, which might be unexpected if the strides are designed to avoid certain memory locations completely for reading and writing.

For example, a 1D FFT of length \(N\) with an input and output stride of 2 only transforms the even-indexed elements in the input and output buffers. But if temporary data needs to be written to the buffers, the odd-indexed elements might be overwritten.

However, rocFFT is guaranteed to respect the size of buffers. In the above example, the input/output buffers are \(2N\) elements long, even if only \(N\) even-indexed elements are being transformed. No more than \(2N\) elements of temporary data are written to the buffers during the transform.

These policies apply to both input and output buffers, because not in-place transforms might overwrite input data.
See [Result placement](#resultplacement) for more information.

## Input and output fields[#](#input-and-output-fields)

By default, the rocFFT inputs and outputs are on the same device and the layouts of
each are described using a set of strides passed to
[ rocfft_plan_description_set_data_layout()](../reference/allapi.html#_CPPv439rocfft_plan_description_set_data_layout23rocfft_plan_descriptionK17rocfft_array_typeK17rocfft_array_typePK6size_tPK6size_tK6size_tPK6size_tK6size_tK6size_tPK6size_tK6size_t).

rocFFT optionally allows for inputs and outputs to be described as **fields**,
each of which is decomposed into multiple **bricks**. Each brick can
reside on a different device and have its own layout parameters.

Note

The rocFFT APIs for declaring fields and bricks are currently experimental and
subject to change in future releases. To submit feedback, questions, and comments
about these interfaces, use the [rocm-libraries issue tracker](https://github.com/ROCm/rocm-libraries/issues).

The workflow for using fields is as follows:

Allocate a

struct by calling`rocfft_field`

.`rocfft_field_create()`

Add one or more bricks to the field:

Allocate a

by calling`rocfft_brick`

. Define the brick dimensions in terms of the lower and upper coordinates in the field’s index space.`rocfft_brick_create()`

Note that the lower coordinate is inclusive (contained within the brick) and the upper coordinate is exclusive (the first index past the end of the brick).

Specify the device on which the brick resides, along with the strides of the brick in device memory.

The coordinates and strides provided here include the batch dimensions unless the batch is

`1`

.Add the brick to the field by calling

.`rocfft_field_add_brick()`

Deallocate the brick by calling

.`rocfft_brick_destroy()`


Set the field as an input or output for the transform by calling either

or`rocfft_plan_description_add_infield()`

on a plan description that has already been allocated. The plan description must then be provided to`rocfft_plan_description_add_outfield()`

.`rocfft_plan_create()`

The offsets, strides, and distances specified by

for input or output are ignored when a field is set for the corresponding input or output.`rocfft_plan_description_set_data_layout()`

If the same field layout is used for both input and output, the same

struct can be passed to both`rocfft_field`

and`rocfft_plan_description_add_infield()`

.`rocfft_plan_description_add_outfield()`

For in-place transforms, only call

. Do not call`rocfft_plan_description_add_infield()`

.`rocfft_plan_description_add_outfield()`

Deallocate the field by calling

.`rocfft_field_destroy()`

Create the plan by calling

. Pass the plan description that has already been allocated.`rocfft_plan_create()`

Execute the plan by calling

. This function takes arrays of pointers for input and output. If fields have been set for input or output, then the arrays must contain pointers to each brick in the input or output.`rocfft_execute()`

The pointers must be provided in the same order in which the bricks were added to the field (using calls to

) and must point to memory on the device that was specified at that time.`rocfft_field_add_brick()`


Important

For in-place transforms, pass a non-empty array of input pointers and an empty array of output pointers.

## Transforms of real data[#](#transforms-of-real-data)

See [Real data](real-data.html) for more information.

## Reproducibility of results[#](#reproducibility-of-results)

The results of an FFT computation generated by rocFFT are bitwise reproducible. For example, deterministic behavior is expected between runs and every run generates the exact same results. Bitwise reproducibility is achieved provided the following attributes are kept constant between runs:

FFT parameters

rocFFT library version

GPU model


A valid FFT plan is a requirement for reproducibility. In particular, the
[rules for overlapping of FFT data](#stridesdistances) must be followed.

## Result scaling[#](#result-scaling)

The output of a forward or backward FFT often needs to be multiplied
by a scaling factor before the data can be passed to the next step of
a computation. While you can launch a separate GPU
kernel to do this work, rocFFT provides a
[ rocfft_plan_description_set_scale_factor()](../reference/allapi.html#_CPPv440rocfft_plan_description_set_scale_factor23rocfft_plan_descriptionKd) function to more
efficiently combine this scaling multiplication with the FFT work.

The scaling factor is set as part of the plan description before plan creation.

## Loading and storing callbacks[#](#loading-and-storing-callbacks)

See [Loading and storing callbacks](load-store-callbacks.html) for more information.

## Runtime compilation[#](#runtime-compilation)

See [Runtime compilation](runtime-compilation.html) for more information.
