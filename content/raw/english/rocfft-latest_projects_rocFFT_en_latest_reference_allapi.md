---
title: "API reference &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/reference/allapi.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:06:46.834459+00:00
content_hash: "6dcc29c85ce111f9"
---

# API reference[#](#api-reference)

This topic includes a comprehensive listing of the classes and methods in the rocFFT library.

-
*file*rocfft.h [rocfft.h](#rocfft_8h)defines all the public interfaces and typesTypedefs

-
typedef struct rocfft_plan_t *rocfft_plan
[#](#_CPPv411rocfft_plan) Pointer type to plan structure.

This type is used to declare a plan handle that can be initialized with

[rocfft_plan_create](api.html#rocfft_8h_1ae1c36eca302a0d6fdf2ff02f819ce9e1).

-
typedef struct rocfft_plan_description_t *rocfft_plan_description
[#](#_CPPv423rocfft_plan_description) Pointer type to plan description structure.

This type is used to declare a plan description handle that can be initialized with

[rocfft_plan_description_create](api.html#rocfft_8h_1a3c38da7775a4e0425a589c5486c6ffc4).

-
typedef struct rocfft_execution_info_t *rocfft_execution_info
[#](#_CPPv421rocfft_execution_info) Pointer type to execution info structure.

This type is used to declare an execution info handle that can be initialized with

[rocfft_execution_info_create](api.html#rocfft_8h_1aafb626ad7f63900a68fc913bf8c45e5b).

-
typedef struct rocfft_field_t *rocfft_field
[#](#_CPPv412rocfft_field) Pointer type to a rocFFT field structure.

rocFFT fields are used to hold data decomposition information which is then passed to a

[rocfft_plan](api.html#rocfft_8h_1aecca10c6ee20e6710a6fb7e39d69aeae)via a[rocfft_plan_description](api.html#rocfft_8h_1ad25e39e540dd29040edf589b2ef503c2)Warning

Experimental! This feature is part of an experimental API preview.


-
typedef struct rocfft_brick_t *rocfft_brick
[#](#_CPPv412rocfft_brick) Pointer type to a rocFFT brick structure.

rocFFT bricks are used to describe the data decomposition of fields.

Warning

Experimental! This feature is part of an experimental API preview.


Enums

-
enum rocfft_status
[#](#_CPPv413rocfft_status) rocFFT status/error codes

*Values:*-
enumerator rocfft_status_success
[#](#_CPPv4N13rocfft_status21rocfft_status_successE)

-
enumerator rocfft_status_failure
[#](#_CPPv4N13rocfft_status21rocfft_status_failureE)

-
enumerator rocfft_status_invalid_arg_value
[#](#_CPPv4N13rocfft_status31rocfft_status_invalid_arg_valueE)

-
enumerator rocfft_status_invalid_dimensions
[#](#_CPPv4N13rocfft_status32rocfft_status_invalid_dimensionsE)

-
enumerator rocfft_status_invalid_array_type
[#](#_CPPv4N13rocfft_status32rocfft_status_invalid_array_typeE)

-
enumerator rocfft_status_invalid_strides
[#](#_CPPv4N13rocfft_status29rocfft_status_invalid_stridesE)

-
enumerator rocfft_status_invalid_distance
[#](#_CPPv4N13rocfft_status30rocfft_status_invalid_distanceE)

-
enumerator rocfft_status_invalid_offset
[#](#_CPPv4N13rocfft_status28rocfft_status_invalid_offsetE)

-
enumerator rocfft_status_invalid_work_buffer
[#](#_CPPv4N13rocfft_status33rocfft_status_invalid_work_bufferE)

-
enumerator rocfft_status_success

-
enum rocfft_transform_type
[#](#_CPPv421rocfft_transform_type) Type of transform.

*Values:*-
enumerator rocfft_transform_type_complex_forward
[#](#_CPPv4N21rocfft_transform_type37rocfft_transform_type_complex_forwardE)

-
enumerator rocfft_transform_type_complex_inverse
[#](#_CPPv4N21rocfft_transform_type37rocfft_transform_type_complex_inverseE)

-
enumerator rocfft_transform_type_real_forward
[#](#_CPPv4N21rocfft_transform_type34rocfft_transform_type_real_forwardE)

-
enumerator rocfft_transform_type_real_inverse
[#](#_CPPv4N21rocfft_transform_type34rocfft_transform_type_real_inverseE)

-
enumerator rocfft_transform_type_complex_forward

-
enum rocfft_precision
[#](#_CPPv416rocfft_precision) Precision.

*Values:*-
enumerator rocfft_precision_single
[#](#_CPPv4N16rocfft_precision23rocfft_precision_singleE)

-
enumerator rocfft_precision_double
[#](#_CPPv4N16rocfft_precision23rocfft_precision_doubleE)

-
enumerator rocfft_precision_half
[#](#_CPPv4N16rocfft_precision21rocfft_precision_halfE)

-
enumerator rocfft_precision_single

-
enum rocfft_result_placement
[#](#_CPPv423rocfft_result_placement) Result placement.

Declares where the output of the transform should be placed. Note that input buffers may still be overwritten during execution of a transform, even if the transform is not in-place.

*Values:*-
enumerator rocfft_placement_inplace
[#](#_CPPv4N23rocfft_result_placement24rocfft_placement_inplaceE)

-
enumerator rocfft_placement_notinplace
[#](#_CPPv4N23rocfft_result_placement27rocfft_placement_notinplaceE)

-
enumerator rocfft_placement_inplace

-
enum rocfft_array_type
[#](#_CPPv417rocfft_array_type) Array type.

*Values:*-
enumerator rocfft_array_type_complex_interleaved
[#](#_CPPv4N17rocfft_array_type37rocfft_array_type_complex_interleavedE)

-
enumerator rocfft_array_type_complex_planar
[#](#_CPPv4N17rocfft_array_type32rocfft_array_type_complex_planarE)

-
enumerator rocfft_array_type_real
[#](#_CPPv4N17rocfft_array_type22rocfft_array_type_realE)

-
enumerator rocfft_array_type_hermitian_interleaved
[#](#_CPPv4N17rocfft_array_type39rocfft_array_type_hermitian_interleavedE)

-
enumerator rocfft_array_type_hermitian_planar
[#](#_CPPv4N17rocfft_array_type34rocfft_array_type_hermitian_planarE)

-
enumerator rocfft_array_type_unset
[#](#_CPPv4N17rocfft_array_type23rocfft_array_type_unsetE)

-
enumerator rocfft_array_type_complex_interleaved

Functions

-
[rocfft_status](#_CPPv413rocfft_status)rocfft_setup()[#](#_CPPv412rocfft_setupv) Library setup function, called once in program before start of library use.


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_cleanup()[#](#_CPPv414rocfft_cleanupv) Library cleanup function, called once in program after end of library use.


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_create([rocfft_plan](#_CPPv411rocfft_plan)*plan,[rocfft_result_placement](#_CPPv423rocfft_result_placement)placement,[rocfft_transform_type](#_CPPv421rocfft_transform_type)transform_type,[rocfft_precision](#_CPPv416rocfft_precision)precision, size_t dimensions, const size_t *lengths, size_t number_of_transforms, const[rocfft_plan_description](#_CPPv423rocfft_plan_description)description)[#](#_CPPv418rocfft_plan_createP11rocfft_plan23rocfft_result_placement21rocfft_transform_type16rocfft_precision6size_tPK6size_t6size_tK23rocfft_plan_description) Create an FFT plan.

This API creates a plan, which the user can execute subsequently. This function takes many of the fundamental parameters needed to specify a transform.

The dimensions parameter can take a value of 1, 2, or 3. The ‘lengths’ array specifies the size of data in each dimension. Note that lengths[0] is the size of the innermost dimension, lengths[1] is the next higher dimension and so on (column-major ordering).

The ‘number_of_transforms’ parameter specifies how many transforms (of the same kind) needs to be computed. By specifying a value greater than 1, a batch of transforms can be computed with a single API call.

Additionally, a handle to a plan description can be passed for more detailed transforms. For simple transforms, this parameter can be set to NULL.

The plan must be destroyed with a call to

[rocfft_plan_destroy](api.html#rocfft_8h_1a2338317b1790f96b4db891e45a2581c2).- Parameters:
**plan**–**[out]**plan handle**placement**–**[in]**placement of result**transform_type**–**[in]**type of transform**precision**–**[in]**precision**dimensions**–**[in]**dimensions**lengths**–**[in]**dimensions-sized array of transform lengths**number_of_transforms**–**[in]**number of transforms**description**–**[in]**description handle created by rocfft_plan_description_create; can be NULL for simple transforms



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execute(const[rocfft_plan](#_CPPv411rocfft_plan)plan, void *in_buffer[], void *out_buffer[],[rocfft_execution_info](#_CPPv421rocfft_execution_info)info)[#](#_CPPv414rocfft_executeK11rocfft_planA_PvA_Pv21rocfft_execution_info) Execute an FFT plan.

This API executes an FFT plan on buffers given by the user.

If the transform is in-place, only the input buffer is needed and the output buffer parameter can be set to NULL. For not in-place transforms, output buffers have to be specified.

Input and output buffers are arrays of pointers. Interleaved array formats are the default, and require just one pointer per input or output buffer. Planar array formats require two pointers per input or output buffer - real and imaginary pointers, in that order.

If fields have been set for transform input or output, these arrays have one pointer per brick in the input or output field, provided in the order that the bricks were added to the field.

Note that input buffers may still be overwritten during execution of a transform, even if the transform is not in-place.

The final parameter in this function is a rocfft_execution_info handle. This optional parameter serves as a way for the user to control execution streams and work buffers.

- Parameters:
**plan**–**[in]**plan handle**in_buffer**–**[inout]**array (of size 1 for interleaved data, of size 2 for planar data, or one per brick if an input field is set) of input buffers**out_buffer**–**[inout]**array (of size 1 for interleaved data, of size 2 for planar data, or one per brick if an output field is set) of output buffers, ignored for in-place transforms**info**–**[in]**execution info handle created by rocfft_execution_info_create



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_destroy([rocfft_plan](#_CPPv411rocfft_plan)plan)[#](#_CPPv419rocfft_plan_destroy11rocfft_plan) Destroy an FFT plan.

This API frees the plan after it is no longer needed.

- Parameters:
**plan**–**[in]**plan handle


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_set_scale_factor([rocfft_plan_description](#_CPPv423rocfft_plan_description)description, const double scale_factor)[#](#_CPPv440rocfft_plan_description_set_scale_factor23rocfft_plan_descriptionKd) Set scaling factor.

rocFFT multiplies each element of the result by the given factor at the end of the transform.

The supplied factor must be a finite number. That is, it must neither be infinity nor NaN.

- Parameters:
**description**–**[in]**description handle**scale_factor**–**[in]**scaling factor



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_set_data_layout([rocfft_plan_description](#_CPPv423rocfft_plan_description)description, const[rocfft_array_type](#_CPPv417rocfft_array_type)in_array_type, const[rocfft_array_type](#_CPPv417rocfft_array_type)out_array_type, const size_t *in_offsets, const size_t *out_offsets, const size_t in_strides_size, const size_t *in_strides, const size_t in_distance, const size_t out_strides_size, const size_t *out_strides, const size_t out_distance)[#](#_CPPv439rocfft_plan_description_set_data_layout23rocfft_plan_descriptionK17rocfft_array_typeK17rocfft_array_typePK6size_tPK6size_tK6size_tPK6size_tK6size_tK6size_tPK6size_tK6size_t) Set advanced data layout parameters on a plan description.

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



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_field_create([rocfft_field](#_CPPv412rocfft_field)*field)[#](#_CPPv419rocfft_field_createP12rocfft_field) Create a rocfft field struct.

Warning

Experimental! This feature is part of an experimental API preview.


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_field_destroy([rocfft_field](#_CPPv412rocfft_field)field)[#](#_CPPv420rocfft_field_destroy12rocfft_field) Destroy a rocfft field struct.

The field struct can be destroyed after being added to the plan description; it is not used for plan execution.

Warning

Experimental! This feature is part of an experimental API preview.


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_get_version_string(char *buf, size_t len)[#](#_CPPv425rocfft_get_version_stringPc6size_t) Get library version string.

- Parameters:
**buf**–**[inout]**buffer that receives the version string**len**–**[in]**length of buf, minimum 30 characters



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_set_comm([rocfft_plan_description](#_CPPv423rocfft_plan_description)description,[rocfft_comm_type](#_CPPv416rocfft_comm_type)comm_type, void *comm_handle)[#](#_CPPv432rocfft_plan_description_set_comm23rocfft_plan_description16rocfft_comm_typePv) Set the communication library for distributed transforms.

Set the multi-processing communication library for a plan.

Multi-processing communication libraries require library-specific handle to also be specified. For MPI libraries, this is a pointer to an MPI communicator.

- Parameters:
**description**–**[in]**description handle**comm_type**–**[in]**communicator type**comm_handle**–**[in]**handle to communication-library-specific state



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_brick_create([rocfft_brick](#_CPPv412rocfft_brick)*brick, const size_t *field_lower, const size_t *field_upper, const size_t *brick_stride, size_t dim_with_batch, int deviceID)[#](#_CPPv419rocfft_brick_createP12rocfft_brickPK6size_tPK6size_tPK6size_t6size_ti) Define a brick as part of a decomposition of a field.

Fields can contain a full-dimensional data distribution. The decomposition is specified by providing a lower coordinate and an upper coordinate in the field’s index space. The lower coordinate is inclusive (contained within the brick) and the upper coordinate is exclusive (first index past the end of the brick).

One must also provide a stride for the brick data which specifies how the brick’s data is arranged in memory.

All coordinates and strides must include batch dimensions, and are in column-major order (fastest-moving dimension first).

A HIP device ID is also provided - each brick may reside on a different device.

All arrays may be re-used or freed immediately after the function returns.

Warning

Experimental! This feature is part of an experimental API preview.

- Parameters:
**brick**–**[out]**brick structure**field_lower**–**[in]**array of length dim specifying the lower index (inclusive) for the brick in the field’s index space.**field_upper**–**[in]**array of length dim specifying the upper index (exclusive) for the brick in the field’s index space.**brick_stride**–**[in]**array of length dim specifying the brick’s stride in memory**dim_with_batch**–**[in]**length of the arrays; this must match the dimension of the FFT plus one for the batch dimension.**deviceID**–**[in]**HIP device ID for the device on which the brick’s data is resident.



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_brick_destroy([rocfft_brick](#_CPPv412rocfft_brick)brick)[#](#_CPPv420rocfft_brick_destroy12rocfft_brick) Deallocate a brick created with rocfft_brick_create.

Warning

Experimental! This feature is part of an experimental API preview.


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_field_add_brick([rocfft_field](#_CPPv412rocfft_field)field,[rocfft_brick](#_CPPv412rocfft_brick)brick)[#](#_CPPv422rocfft_field_add_brick12rocfft_field12rocfft_brick) Add a brick to a field.

Note that the order in which the bricks are added is significant; the pointers provided for each brick to

[rocfft_execute](api.html#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71)are in the same order that the bricks were added to the field.The brick may be added to another field or destroyed any time after this function returns.

Warning

Experimental! This feature is part of an experimental API preview.

- Parameters:
**field**–**[inout]**[rocfft_field](#rocfft_8h_1a22ec11504d81008b36adb670192a51b8)struct which holds the brick decomposition.**brick**–**[in]**[rocfft_brick](#rocfft_8h_1aa32dbe9bd6bc689a410c368f6b22acc0)struct to add to the field.



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_add_infield([rocfft_plan_description](#_CPPv423rocfft_plan_description)description,[rocfft_field](#_CPPv412rocfft_field)field)[#](#_CPPv435rocfft_plan_description_add_infield23rocfft_plan_description12rocfft_field) Add a

[rocfft_field](#rocfft_8h_1a22ec11504d81008b36adb670192a51b8)to a[rocfft_plan_description](api.html#rocfft_8h_1ad25e39e540dd29040edf589b2ef503c2)as an input.The field may be reused or freed immediately after the function returns.

Warning

Experimental! This feature is part of an experimental API preview.

- Parameters:
**description**–**[inout]**[rocfft_plan_description](api.html#rocfft_8h_1ad25e39e540dd29040edf589b2ef503c2)that will pass the field information to plan creation**field**–**[in]**[rocfft_field](#rocfft_8h_1a22ec11504d81008b36adb670192a51b8)struct added as an input field



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_add_outfield([rocfft_plan_description](#_CPPv423rocfft_plan_description)description,[rocfft_field](#_CPPv412rocfft_field)field)[#](#_CPPv436rocfft_plan_description_add_outfield23rocfft_plan_description12rocfft_field) Add a

[rocfft_field](#rocfft_8h_1a22ec11504d81008b36adb670192a51b8)to a[rocfft_plan_description](api.html#rocfft_8h_1ad25e39e540dd29040edf589b2ef503c2)as an output.The field may be reused or freed immediately after the function returns.

Warning

Experimental! This feature is part of an experimental API preview.

- Parameters:
**description**–**[inout]**[rocfft_plan_description](api.html#rocfft_8h_1ad25e39e540dd29040edf589b2ef503c2)that will pass the field information to plan creation**field**–**[in]**[rocfft_field](#rocfft_8h_1a22ec11504d81008b36adb670192a51b8)struct added as an output field



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_get_work_buffer_size(const[rocfft_plan](#_CPPv411rocfft_plan)plan, size_t *size_in_bytes)[#](#_CPPv432rocfft_plan_get_work_buffer_sizeK11rocfft_planP6size_t) Get work buffer size.

Get the work buffer size required for a plan.

- Parameters:
**plan**–**[in]**plan handle**size_in_bytes**–**[out]**size of needed work buffer in bytes



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_get_print(const[rocfft_plan](#_CPPv411rocfft_plan)plan)[#](#_CPPv421rocfft_plan_get_printK11rocfft_plan) Print all plan information.

Prints plan details to stdout, to aid debugging

- Parameters:
**plan**–**[in]**plan handle


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_create([rocfft_plan_description](#_CPPv423rocfft_plan_description)*description)[#](#_CPPv430rocfft_plan_description_createP23rocfft_plan_description) Create plan description.

This API creates a plan description with which the user can set extra plan properties. The plan description must be freed with a call to

[rocfft_plan_description_destroy](api.html#rocfft_8h_1a9e5f32c5eb787b7c8c3f96402a017f3f).- Parameters:
**description**–**[out]**plan description handle


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_plan_description_destroy([rocfft_plan_description](#_CPPv423rocfft_plan_description)description)[#](#_CPPv431rocfft_plan_description_destroy23rocfft_plan_description) Destroy a plan description.

This API frees the plan description. A plan description can be freed any time after it is passed to

[rocfft_plan_create](api.html#rocfft_8h_1ae1c36eca302a0d6fdf2ff02f819ce9e1).- Parameters:
**description**–**[in]**plan description handle


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execution_info_create([rocfft_execution_info](#_CPPv421rocfft_execution_info)*info)[#](#_CPPv428rocfft_execution_info_createP21rocfft_execution_info) Create execution info.

This API creates an execution info with which the user can control plan execution and work buffers. The execution info must be freed with a call to

[rocfft_execution_info_destroy](api.html#rocfft_8h_1a2c636a589cf9b2356dc94a4042017862).- Parameters:
**info**–**[out]**execution info handle


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execution_info_destroy([rocfft_execution_info](#_CPPv421rocfft_execution_info)info)[#](#_CPPv429rocfft_execution_info_destroy21rocfft_execution_info) Destroy an execution info.

This API frees the execution info. An execution info object can be freed any time after it is passed to

[rocfft_execute](api.html#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71).- Parameters:
**info**–**[in]**execution info handle


-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execution_info_set_work_buffer([rocfft_execution_info](#_CPPv421rocfft_execution_info)info, void *work_buffer, const size_t size_in_bytes)[#](#_CPPv437rocfft_execution_info_set_work_buffer21rocfft_execution_infoPvK6size_t) Set work buffer in execution info.

This is one of the execution info functions to specify optional additional information to control execution. This API provides a work buffer for the transform. It must be called before

[rocfft_execute](api.html#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71).When a non-zero value is obtained from

[rocfft_plan_get_work_buffer_size](api.html#rocfft_8h_1a2b8d6a49fbb5204023776715f971e055), that means the library needs a work buffer to compute the transform. In this case, the user should allocate the work buffer and pass it to the library via this API.If a work buffer is required for the transform but is not specified using this function,

[rocfft_execute](api.html#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71)will automatically allocate the required buffer and free it when execution is finished.Users should allocate their own work buffers if they need precise control over the lifetimes of those buffers, or if multiple plans need to share the same buffer.

- Parameters:
**info**–**[in]**execution info handle**work_buffer**–**[in]**work buffer**size_in_bytes**–**[in]**size of work buffer in bytes



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execution_info_set_stream([rocfft_execution_info](#_CPPv421rocfft_execution_info)info, void *stream)[#](#_CPPv432rocfft_execution_info_set_stream21rocfft_execution_infoPv) Set stream in execution info.

Associates an existing compute stream to a plan. This must be called before the call to

[rocfft_execute](api.html#rocfft_8h_1a0f306349a116698ac30ccdb3a1201d71).Once the association is made, execution of the FFT will run the computation through the specified stream.

The stream must be of type hipStream_t. It is an error to pass the address of a hipStream_t object.

- Parameters:
**info**–**[in]**execution info handle**stream**–**[in]**underlying compute stream



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execution_info_set_load_callback([rocfft_execution_info](#_CPPv421rocfft_execution_info)info, void **cb_functions, void **cb_data, size_t shared_mem_bytes)[#](#_CPPv439rocfft_execution_info_set_load_callback21rocfft_execution_infoPPvPPv6size_t) Set a load callback for a plan execution (experimental)

This function specifies a user-defined callback function that is run to load input from global memory at the start of the transform. Callbacks are an experimental feature in rocFFT.

Callback function pointers/data are given as arrays, with one function/data pointer per brick in the input field of the plan. A plan with no input field specified is considered to have one brick.

All functions in the array must perform the same logical operation. That is, any function in the array must be substitutable for any other function in the array if the data being loaded were moved to another brick.

The provided function pointers replace any previously-specified load callback for this execution info handle.

Load callbacks have the following signature:

Tdata load_cb(Tdata* data, size_t offset, void* cbdata, void* sharedMem);

‘Tdata’ is the type of a single element of the input buffer. It is the caller’s responsibility to ensure that the function type is appropriate for the plan (for example, a single-precision real-to-complex transform would load single-precision real elements).

A null value for ‘cb_functions’ may be specified to clear any previously registered load callback. ‘cb_data’ may be null if the functions require no additional pointer to be passed to them.

Currently, ‘shared_mem_bytes’ must be 0. Callbacks are not supported on transforms that use planar formats for either input or output.

- Parameters:
**info**–**[in]**execution info handle**cb_functions**–**[in]**callback function pointers**cb_data**–**[in]**callback function data, passed to the function pointer when it is called**shared_mem_bytes**–**[in]**amount of shared memory to allocate for the callback function to use



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_execution_info_set_store_callback([rocfft_execution_info](#_CPPv421rocfft_execution_info)info, void **cb_functions, void **cb_data, size_t shared_mem_bytes)[#](#_CPPv440rocfft_execution_info_set_store_callback21rocfft_execution_infoPPvPPv6size_t) Set a store callback for a plan execution (experimental)

This function specifies a user-defined callback function that is run to store output to global memory at the end of the transform. Callbacks are an experimental feature in rocFFT.

Callback function pointers/data are given as arrays, with one function/data pointer per device executing this plan. Currently, plans can only use one device.

Callback function pointers/data are given as arrays, with one function/data pointer per brick in the output field of the plan. A plan with no output field specified is considered to have one brick.

All functions in the array must perform the same logical operation. That is, any function in the array must be substitutable for any other function in the array if the data being stored were moved to another brick.

The provided function pointers replace any previously-specified store callback for this execution info handle.

Store callbacks have the following signature:

void store_cb(Tdata* data, size_t offset, Tdata element, void* cbdata, void* sharedMem);

‘Tdata’ is the type of a single element of the output buffer. It is the caller’s responsibility to ensure that the function type is appropriate for the plan (for example, a single-precision real-to-complex transform would store single-precision complex elements).

A null value for ‘cb_functions’ may be specified to clear any previously registered load callback. ‘cb_data’ may be null if the functions require no additional pointer to be passed to them.

Currently, ‘shared_mem_bytes’ must be 0. Callbacks are not supported on transforms that use planar formats for either input or output.

- Parameters:
**info**–**[in]**execution info handle**cb_functions**–**[in]**callback function pointers**cb_data**–**[in]**callback function data, passed to the function pointer when it is called**shared_mem_bytes**–**[in]**amount of shared memory to allocate for the callback function to use



-
[rocfft_status](#_CPPv413rocfft_status)rocfft_cache_serialize(void **buffer, size_t *buffer_len_bytes)[#](#_CPPv422rocfft_cache_serializePPvP6size_t) Serialize compiled kernel cache.

Serialize rocFFT’s cache of compiled kernels into a buffer. This buffer is allocated by rocFFT and must be freed with a call to

[rocfft_cache_buffer_free](#rocfft_8h_1a7f519646d5e39e250e9979adebe1cb24). The length of the buffer in bytes is written to ‘buffer_len_bytes’.

-
[rocfft_status](#_CPPv413rocfft_status)rocfft_cache_buffer_free(void *buffer)[#](#_CPPv424rocfft_cache_buffer_freePv) Free cache serialization buffer.

Deallocate a buffer allocated by

[rocfft_cache_serialize](#rocfft_8h_1a17523664254ddf451db89e8e9d21f25a).

-
[rocfft_status](#_CPPv413rocfft_status)rocfft_cache_deserialize(const void *buffer, size_t buffer_len_bytes)[#](#_CPPv424rocfft_cache_deserializePKv6size_t) Deserialize a buffer into the compiled kernel cache.

Kernels in the buffer that match already-cached kernels will replace those kernels that are in the cache. Already-cached kernels that do not match those in the buffer are unmodified by this operation. The cache is unmodified if either a null buffer pointer or a zero length is passed.


-
typedef struct rocfft_plan_t *rocfft_plan

-
*file*README.md

-
*page*index [ROCm](https://github.com/ROCm/ROCm). The rocFFT library can be used with AMD GPUs.## Documentation

[#](#index_1autotoc_md1)

To build our documentation locally, use the following code:[!NOTE] The published rocFFT documentation is available at

[rocFFT](https://rocm.docs.amd.com/projects/rocFFT/en/latest/index.html)in an organized, easy-to-read format, with search and a table of contents. The documentation source files reside in the projects/rocfft/docs folder of the rocm-libraries repository. As with all ROCm projects, the documentation is open source. For more information, see[Contribute to ROCm documentation](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).cd projects/rocfft/docs pip3 install -r sphinx/requirements.txt python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html

## Build and install

[#](#index_1autotoc_md2)You can install rocFFT using pre-built packages or building from source.

Installing pre-built packages:

Download the pre-built packages from the

[ROCm package servers](https://rocm.docs.amd.com/en/latest/deploy/linux/index.html)or use the GitHub releases tab to download the source (this may give you a more recent version than the pre-built packages).Run:

`sudo apt update && sudo apt install rocfft`


Building from source:

rocFFT is compiled with AMD’s clang++ and uses CMake. You can specify several options to customize your build. The following commands build a shared library for supported AMD GPUs. Run these commands from the

`rocm-libraries/projects/rocfft`

directory:build && cd build cmake -DCMAKE_CXX_COMPILER=amdclang++ -DCMAKE_C_COMPILER=amdclang .. make -j

You can compile a static library using the

`-DBUILD_SHARED_LIBS=off`

option.With rocFFT, you can use indirect function calls by default; this requires ROCm 4.3 or higher. You can use

`-DROCFFT_CALLBACKS_ENABLED=off`

with CMake to prevent these calls on older ROCm compilers. Note that with this configuration, callbacks won’t work correctly.rocFFT includes the following clients:

`rocfft-bench`

: Runs general transforms and is useful for performance analysis`rocfft-test`

: Runs various regression testsVarious small samples



Client

CMake option

Dependencies

`rocfft-bench`

`-DBUILD_CLIENTS_BENCH=on`

hipRAND

`rocfft-test`

`-DBUILD_CLIENTS_TESTS=on`

hipRAND, FFTW, GoogleTest

samples

`-DBUILD_CLIENTS_SAMPLES=on`

None

coverage

`-DBUILD_CODE_COVERAGE=ON`

clang, llvm-cov

Clients are not built by default. To build them, use

`-DBUILD_CLIENTS=on`

. The build process downloads and builds GoogleTest and FFTW if they are not already installed.Clients can be built separately from the main library. For example, you can build all the clients with an existing rocFFT library by invoking CMake from within the

`rocFFT-src/clients`

folder:build && cd build cmake -DCMAKE_CXX_COMPILER=amdclang++ -DCMAKE_PREFIX_PATH=/path/to/rocFFT-lib .. make -j

To install client dependencies on Ubuntu, run:

`bash sudo apt install libgtest-dev libfftw3-dev libboost-dev`

rocFFT uses version 1.11 of GoogleTest.

You can generate a test coverage report with the following:

`bash cmake -DCMAKE_CXX_COMPILER=amdclang++ -DBUILD_CLIENTS_SAMPLES=ON -DBUILD_CLIENTS_TESTS=ON -DBUILD_CODE_COVERAGE=ON <optional: -DCOVERAGE_TEST_OPTIONS="cmdline args to pass to rocfft-test (default: --smoketest)"> .. make -j coverage`

The above will output the coverage report to the terminal and also save an html coverage report to`$PWD/coverage-report`

.## Examples

[#](#index_1autotoc_md3)A summary of the latest functionality and workflow to compute an FFT with rocFFT is available on the

[rocFFT documentation portal](https://rocm.docs.amd.com/projects/rocFFT/en/latest/).You can find additional examples in the

`clients/samples`

subdirectory.## Support

[#](#index_1autotoc_md4)You can report bugs and feature requests through the rocm-libraries GitHub

[issue tracker](https://github.com/ROCm/rocm-libraries/issues).## Contribute

[#](#index_1autotoc_md5)If you want to contribute to rocFFT, you must follow the

[contribution guidelines](https://github.com/ROCm/rocm-libraries/blob/develop/projects/rocfft/.github/CONTRIBUTING.md).
