---
title: "API usage &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/reference/api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:26.200556+00:00
content_hash: "b8a7e2988c28e6ec"
---

# API usage[#](#api-usage)

This section describes how to use the rocFFT library API.

## Types[#](#types)

There are a few data structures that are internal to the library. The pointer types to these structures are listed below. Use these types to create handles and pass them between different library functions.

-
typedef struct rocfft_plan_t *rocfft_plan
Pointer type to plan structure.

This type is used to declare a plan handle that can be initialized with

[rocfft_plan_create](#rocfft_8h_1ae1c36eca302a0d6fdf2ff02f819ce9e1).

-
typedef struct rocfft_plan_description_t *rocfft_plan_description
Pointer type to plan description structure.

This type is used to declare a plan description handle that can be initialized with

[rocfft_plan_description_create](#rocfft_8h_1a3c38da7775a4e0425a589c5486c6ffc4).

-
typedef struct rocfft_execution_info_t *rocfft_execution_info
Pointer type to execution info structure.

This type is used to declare an execution info handle that can be initialized with

[rocfft_execution_info_create](#rocfft_8h_1aafb626ad7f63900a68fc913bf8c45e5b).

## Library setup and cleanup[#](#library-setup-and-cleanup)

The following functions handle initialization and cleanup of the library.

-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_setup() Library setup function, called once in program before start of library use.


-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_cleanup() Library cleanup function, called once in program after end of library use.


## Plan[#](#plan)

The following functions are used to create and destroy plan objects.

-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_create([rocfft_plan](allapi.html#_CPPv411rocfft_plan)*plan,[rocfft_result_placement](allapi.html#_CPPv423rocfft_result_placement)placement,[rocfft_transform_type](allapi.html#_CPPv421rocfft_transform_type)transform_type,[rocfft_precision](allapi.html#_CPPv416rocfft_precision)precision, size_t dimensions, const size_t *lengths, size_t number_of_transforms, const[rocfft_plan_description](allapi.html#_CPPv423rocfft_plan_description)description) Create an FFT plan.

This API creates a plan, which the user can execute subsequently. This function takes many of the fundamental parameters needed to specify a transform.

The dimensions parameter can take a value of 1, 2, or 3. The ‘lengths’ array specifies the size of data in each dimension. Note that lengths[0] is the size of the innermost dimension, lengths[1] is the next higher dimension and so on (column-major ordering).

The ‘number_of_transforms’ parameter specifies how many transforms (of the same kind) needs to be computed. By specifying a value greater than 1, a batch of transforms can be computed with a single API call.

Additionally, a handle to a plan description can be passed for more detailed transforms. For simple transforms, this parameter can be set to NULL.

The plan must be destroyed with a call to

[rocfft_plan_destroy](#rocfft_8h_1a2338317b1790f96b4db891e45a2581c2).- Parameters:
**plan**–**[out]**plan handle**placement**–**[in]**placement of result**transform_type**–**[in]**type of transform**precision**–**[in]**precision**dimensions**–**[in]**dimensions**lengths**–**[in]**dimensions-sized array of transform lengths**number_of_transforms**–**[in]**number of transforms**description**–**[in]**description handle created by rocfft_plan_description_create; can be NULL for simple transforms



-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_destroy([rocfft_plan](allapi.html#_CPPv411rocfft_plan)plan) Destroy an FFT plan.

This API frees the plan after it is no longer needed.

- Parameters:
**plan**–**[in]**plan handle


The following functions are used to query for information after a plan is created.

-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_get_work_buffer_size(const[rocfft_plan](allapi.html#_CPPv411rocfft_plan)plan, size_t *size_in_bytes) Get work buffer size.

Get the work buffer size required for a plan.

- Parameters:
**plan**–**[in]**plan handle**size_in_bytes**–**[out]**size of needed work buffer in bytes



-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_get_print(const[rocfft_plan](allapi.html#_CPPv411rocfft_plan)plan) Print all plan information.

Prints plan details to stdout, to aid debugging

- Parameters:
**plan**–**[in]**plan handle


## Plan description[#](#plan-description)

Most of the time, [ rocfft_plan_create()](allapi.html#_CPPv418rocfft_plan_createP11rocfft_plan23rocfft_result_placement21rocfft_transform_type16rocfft_precision6size_tPK6size_t6size_tK23rocfft_plan_description) is able to fully
specify a transform. However, advanced plan details such as strides and
offsets require the creation of a plan description object, which is
configured and passed to the

[function.](allapi.html#_CPPv418rocfft_plan_createP11rocfft_plan23rocfft_result_placement21rocfft_transform_type16rocfft_precision6size_tPK6size_t6size_tK23rocfft_plan_description)

`rocfft_plan_create()`

The plan description object can be safely destroyed after it is passed
to the [ rocfft_plan_create()](allapi.html#_CPPv418rocfft_plan_createP11rocfft_plan23rocfft_result_placement21rocfft_transform_type16rocfft_precision6size_tPK6size_t6size_tK23rocfft_plan_description) function.

-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_description_create([rocfft_plan_description](allapi.html#_CPPv423rocfft_plan_description)*description) Create plan description.

This API creates a plan description with which the user can set extra plan properties. The plan description must be freed with a call to

[rocfft_plan_description_destroy](#rocfft_8h_1a9e5f32c5eb787b7c8c3f96402a017f3f).- Parameters:
**description**–**[out]**plan description handle


-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_description_destroy([rocfft_plan_description](allapi.html#_CPPv423rocfft_plan_description)description) Destroy a plan description.

This API frees the plan description. A plan description can be freed any time after it is passed to

[rocfft_plan_create](#rocfft_8h_1ae1c36eca302a0d6fdf2ff02f819ce9e1).- Parameters:
**description**–**[in]**plan description handle


-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_description_set_scale_factor([rocfft_plan_description](allapi.html#_CPPv423rocfft_plan_description)description, const double scale_factor) Set scaling factor.

rocFFT multiplies each element of the result by the given factor at the end of the transform.

The supplied factor must be a finite number. That is, it must neither be infinity nor NaN.

- Parameters:
**description**–**[in]**description handle**scale_factor**–**[in]**scaling factor



-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_plan_description_set_data_layout([rocfft_plan_description](allapi.html#_CPPv423rocfft_plan_description)description, const[rocfft_array_type](allapi.html#_CPPv417rocfft_array_type)in_array_type, const[rocfft_array_type](allapi.html#_CPPv417rocfft_array_type)out_array_type, const size_t *in_offsets, const size_t *out_offsets, const size_t in_strides_size, const size_t *in_strides, const size_t in_distance, const size_t out_strides_size, const size_t *out_strides, const size_t out_distance) Set advanced data layout parameters on a plan description.

This API specifies advanced layout of input/output buffers for a plan description.

The following parameters are supported for inputs and outputs:

Array type (real, hermitian, or complex data, in either interleaved or planar format).

Real forward transforms require real input and hermitian output.

Real inverse transforms require hermitian input and real output.

Complex transforms require complex input and output.

Hermitian and complex data defaults to interleaved if a specific format is not specified.


Offset of first data element in the data buffer. Defaults to 0 if unspecified.

Stride between consecutive elements in each dimension. Defaults to contiguous data in all dimensions if unspecified.

Distance between consecutive batches. Defaults to contiguous batches if unspecified.


Not all combinations of array types are supported and error codes will be returned for unsupported cases.

Offset, stride, and distance for either input or output provided here is ignored if a field is set for the corresponding input or output.

- Parameters:
**description**–**[inout]**description handle**in_array_type**–**[in]**array type of input buffer**out_array_type**–**[in]**array type of output buffer**in_offsets**–**[in]**offsets, in element units, to start of data in input buffer**out_offsets**–**[in]**offsets, in element units, to start of data in output buffer**in_strides_size**–**[in]**size of in_strides array (must be equal to transform dimensions)**in_strides**–**[in]**array of strides, in each dimension, of input buffer; if set to null ptr library chooses defaults**in_distance**–**[in]**distance between start of each data instance in input buffer**out_strides_size**–**[in]**size of out_strides array (must be equal to transform dimensions)**out_strides**–**[in]**array of strides, in each dimension, of output buffer; if set to null ptr library chooses defaults**out_distance**–**[in]**distance between start of each data instance in output buffer



## Execution[#](#execution)

After creating a plan, execute it using the
[ rocfft_execute()](allapi.html#_CPPv414rocfft_executeK11rocfft_planA_PvA_Pv21rocfft_execution_info) function.
This function computes a transform on the specified data. It provides control over the execution and returns useful
information.

-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_execute(const[rocfft_plan](allapi.html#_CPPv411rocfft_plan)plan, void *in_buffer[], void *out_buffer[],[rocfft_execution_info](allapi.html#_CPPv421rocfft_execution_info)info) Execute an FFT plan.

This API executes an FFT plan on buffers given by the user.

If the transform is in-place, only the input buffer is needed and the output buffer parameter can be set to NULL. For not in-place transforms, output buffers have to be specified.

Input and output buffers are arrays of pointers. Interleaved array formats are the default, and require just one pointer per input or output buffer. Planar array formats require two pointers per input or output buffer - real and imaginary pointers, in that order.

If fields have been set for transform input or output, these arrays have one pointer per brick in the input or output field, provided in the order that the bricks were added to the field.

Note that input buffers may still be overwritten during execution of a transform, even if the transform is not in-place.

The final parameter in this function is a rocfft_execution_info handle. This optional parameter serves as a way for the user to control execution streams and work buffers.

- Parameters:
**plan**–**[in]**plan handle**in_buffer**–**[inout]**array (of size 1 for interleaved data, of size 2 for planar data, or one per brick if an input field is set) of input buffers**out_buffer**–**[inout]**array (of size 1 for interleaved data, of size 2 for planar data, or one per brick if an output field is set) of output buffers, ignored for in-place transforms**info**–**[in]**execution info handle created by rocfft_execution_info_create



Execution info -=============

[ rocfft_execute()](allapi.html#_CPPv414rocfft_executeK11rocfft_planA_PvA_Pv21rocfft_execution_info) takes an optional

[parameter. This parameter encapsulates information such as the work buffer and compute stream for the transform.](allapi.html#_CPPv421rocfft_execution_info)

`rocfft_execution_info`

-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_execution_info_create([rocfft_execution_info](allapi.html#_CPPv421rocfft_execution_info)*info) Create execution info.

This API creates an execution info with which the user can control plan execution and work buffers. The execution info must be freed with a call to

[rocfft_execution_info_destroy](#rocfft_8h_1a2c636a589cf9b2356dc94a4042017862).- Parameters:
**info**–**[out]**execution info handle


-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_execution_info_destroy([rocfft_execution_info](allapi.html#_CPPv421rocfft_execution_info)info) Destroy an execution info.

This API frees the execution info. An execution info object can be freed any time after it is passed to

[rocfft_execute](#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71).- Parameters:
**info**–**[in]**execution info handle


-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_execution_info_set_work_buffer([rocfft_execution_info](allapi.html#_CPPv421rocfft_execution_info)info, void *work_buffer, const size_t size_in_bytes) Set work buffer in execution info.

This is one of the execution info functions to specify optional additional information to control execution. This API provides a work buffer for the transform. It must be called before

[rocfft_execute](#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71).When a non-zero value is obtained from

[rocfft_plan_get_work_buffer_size](#rocfft_8h_1a2b8d6a49fbb5204023776715f971e055), that means the library needs a work buffer to compute the transform. In this case, the user should allocate the work buffer and pass it to the library via this API.If a work buffer is required for the transform but is not specified using this function,

[rocfft_execute](#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71)will automatically allocate the required buffer and free it when execution is finished.Users should allocate their own work buffers if they need precise control over the lifetimes of those buffers, or if multiple plans need to share the same buffer.

- Parameters:
**info**–**[in]**execution info handle**work_buffer**–**[in]**work buffer**size_in_bytes**–**[in]**size of work buffer in bytes



-
[rocfft_status](allapi.html#_CPPv413rocfft_status)rocfft_execution_info_set_stream([rocfft_execution_info](allapi.html#_CPPv421rocfft_execution_info)info, void *stream) Set stream in execution info.

Associates an existing compute stream to a plan. This must be called before the call to

[rocfft_execute](#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71).Once the association is made, execution of the FFT will run the computation through the specified stream.

The stream must be of type hipStream_t. It is an error to pass the address of a hipStream_t object.

- Parameters:
**info**–**[in]**execution info handle**stream**–**[in]**underlying compute stream



## HIP graph support for rocFFT[#](#hip-graph-support-for-rocfft)

rocFFT supports capturing kernels launched by
[ rocfft_execute()](allapi.html#_CPPv414rocfft_executeK11rocfft_planA_PvA_Pv21rocfft_execution_info) into HIP graph nodes. This approach
captures the FFT execution and other work into a HIP graph and
launches the work in the graph multiple times.

Graph capture is only supported for single-process transforms. Multi-process transforms, such as those that use Message Passing Interface, cannot use graph capture because rocFFT performs inter-process communication in addition to launching kernels.

Each launch of a HIP graph provides the same arguments
to the kernels in the graph. In particular, this implies that all of
the parameters to [ rocfft_execute()](allapi.html#_CPPv414rocfft_executeK11rocfft_planA_PvA_Pv21rocfft_execution_info) remain valid while the
HIP graph is in use, including the following:

The rocFFT plan

The input and output buffers

The

object, if provided`rocfft_execution_info`


rocFFT does not support capturing work performed by other API
functions, aside from [ rocfft_execute()](allapi.html#_CPPv414rocfft_executeK11rocfft_planA_PvA_Pv21rocfft_execution_info), into HIP graphs.

## Enumerations[#](#enumerations)

This section lists all the enumerations that are used.

-
enum rocfft_status
rocFFT status/error codes

*Values:*-
enumerator rocfft_status_success

-
enumerator rocfft_status_failure

-
enumerator rocfft_status_invalid_arg_value

-
enumerator rocfft_status_invalid_dimensions

-
enumerator rocfft_status_invalid_array_type

-
enumerator rocfft_status_invalid_strides

-
enumerator rocfft_status_invalid_distance

-
enumerator rocfft_status_invalid_offset

-
enumerator rocfft_status_invalid_work_buffer

-
enumerator rocfft_status_success

-
enum rocfft_transform_type
Type of transform.

*Values:*-
enumerator rocfft_transform_type_complex_forward

-
enumerator rocfft_transform_type_complex_inverse

-
enumerator rocfft_transform_type_real_forward

-
enumerator rocfft_transform_type_real_inverse

-
enumerator rocfft_transform_type_complex_forward

-
enum rocfft_precision
Precision.

*Values:*-
enumerator rocfft_precision_single

-
enumerator rocfft_precision_double

-
enumerator rocfft_precision_half

-
enumerator rocfft_precision_single

-
enum rocfft_result_placement
Result placement.

Declares where the output of the transform should be placed. Note that input buffers may still be overwritten during execution of a transform, even if the transform is not in-place.

*Values:*-
enumerator rocfft_placement_inplace

-
enumerator rocfft_placement_notinplace

-
enumerator rocfft_placement_inplace

-
enum rocfft_array_type
Array type.

*Values:*-
enumerator rocfft_array_type_complex_interleaved

-
enumerator rocfft_array_type_complex_planar

-
enumerator rocfft_array_type_real

-
enumerator rocfft_array_type_hermitian_interleaved

-
enumerator rocfft_array_type_hermitian_planar

-
enumerator rocfft_array_type_unset

-
enumerator rocfft_array_type_complex_interleaved
