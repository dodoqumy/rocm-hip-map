---
title: "Sparse auxiliary functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/auxiliary.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:28.871816+00:00
content_hash: "77fc900d6629c0ed"
---

# Sparse auxiliary functions[#](#sparse-auxiliary-functions)

This module contains all sparse auxiliary functions.

The functions that are contained in the auxiliary module describe all available helper functions that are required for subsequent library calls.
These functions do not support execution in a `hipGraph`

context.

## rocsparse_create_handle()[#](#rocsparse-create-handle)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_handle([rocsparse_handle](types.html#_CPPv416rocsparse_handle)*handle)[#](#_CPPv423rocsparse_create_handleP16rocsparse_handle) Create a rocsparse handle.

`rocsparse_create_handle`

creates the rocSPARSE library context. It must be initialized before any other rocSPARSE API function is invoked and must be passed to all subsequent library function calls. The handle should be destroyed at the end using[rocsparse_destroy_handle()](#rocsparse-auxiliary_8h_1a87c65c7bbcdb98852704ac2a65478241).- Parameters:
**handle**–**[out]**the pointer to the handle to the rocSPARSE library context.- Return values:
**rocsparse_status_success**– the initialization succeeded.**rocsparse_status_invalid_handle**–`handle`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_destroy_handle()[#](#rocsparse-destroy-handle)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_handle([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle)[#](#_CPPv424rocsparse_destroy_handle16rocsparse_handle) Destroy a rocsparse handle.

`rocsparse_destroy_handle`

destroys the rocSPARSE library context and releases all resources used by the rocSPARSE library.- Parameters:
**handle**–**[in]**the handle to the rocSPARSE library context.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_set_stream()[#](#rocsparse-set-stream)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_stream([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, hipStream_t stream)[#](#_CPPv420rocsparse_set_stream16rocsparse_handle11hipStream_t) Specify user defined HIP stream.

`rocsparse_set_stream`

specifies the stream to be used by the rocSPARSE library context and all subsequent function calls.**Example**This example illustrates, how a user defined stream can be used in rocSPARSE.

// Create rocSPARSE handle rocsparse_handle handle; rocsparse_create_handle(&handle); // Create stream hipStream_t stream; hipStreamCreate(&stream); // Set stream to rocSPARSE handle rocsparse_set_stream(handle, stream); // Do some work // ... // Clean up rocsparse_destroy_handle(handle); hipStreamDestroy(stream);


- Parameters:
**handle**–**[inout]**the handle to the rocSPARSE library context.**stream**–**[in]**the stream to be used by the rocSPARSE library context.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.



## rocsparse_get_stream()[#](#rocsparse-get-stream)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_get_stream([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, hipStream_t *stream)[#](#_CPPv420rocsparse_get_stream16rocsparse_handleP11hipStream_t) Get current stream from library context.

`rocsparse_get_stream`

gets the rocSPARSE library context stream which is currently used for all subsequent function calls.- Parameters:
**handle**–**[in]**the handle to the rocSPARSE library context.**stream**–**[out]**the stream currently used by the rocSPARSE library context.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.



## rocsparse_set_pointer_mode()[#](#rocsparse-set-pointer-mode)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_pointer_mode([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_pointer_mode](enumerations.html#_CPPv422rocsparse_pointer_mode)pointer_mode)[#](#_CPPv426rocsparse_set_pointer_mode16rocsparse_handle22rocsparse_pointer_mode) Specify pointer mode.

`rocsparse_set_pointer_mode`

specifies the pointer mode to be used by the rocSPARSE library context and all subsequent function calls. For example, many rocSPARSE routines take \(\alpha\) and \(\beta\) pointers as parameters. These can be either host memory pointers or device memory pointers depending on what the pointer mode is set to. By default, all values are passed using host pointer mode. Valid pointer modes are[rocsparse_pointer_mode_host](enumerations.html#rocsparse-types_8h_1a154fe9812f99d1f2c3db94c1ce561a15ab69d8b65b07ce81f2a28a03da361c698)or[rocsparse_pointer_mode_device](enumerations.html#rocsparse-types_8h_1a154fe9812f99d1f2c3db94c1ce561a15a8e76bc462cef4e84dc4c15f53006ac5e).- Parameters:
**handle**–**[in]**the handle to the rocSPARSE library context.**pointer_mode**–**[in]**the pointer mode to be used by the rocSPARSE library context.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.



## rocsparse_get_pointer_mode()[#](#rocsparse-get-pointer-mode)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_get_pointer_mode([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle,[rocsparse_pointer_mode](enumerations.html#_CPPv422rocsparse_pointer_mode)*pointer_mode)[#](#_CPPv426rocsparse_get_pointer_mode16rocsparse_handleP22rocsparse_pointer_mode) Get current pointer mode from library context.

`rocsparse_get_pointer_mode`

gets the rocSPARSE library context pointer mode which is currently used for all subsequent function calls.- Parameters:
**handle**–**[in]**the handle to the rocSPARSE library context.**pointer_mode**–**[out]**the pointer mode that is currently used by the rocSPARSE library context.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.



## rocsparse_get_version()[#](#rocsparse-get-version)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_get_version([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, int *version)[#](#_CPPv421rocsparse_get_version16rocsparse_handlePi) Get rocSPARSE version.

`rocsparse_get_version`

gets the rocSPARSE library version number.patch = version % 100

minor = version / 100 % 1000

major = version / 100000


**Example**rocsparse_handle handle; rocsparse_create_handle(&handle); rocsparse_get_version(handle, &rocsparse_ver); rocsparse_destroy_handle(handle);


- Parameters:
**handle**–**[in]**the handle to the rocSPARSE library context.**version**–**[out]**the version number of the rocSPARSE library.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.



## rocsparse_get_git_rev()[#](#rocsparse-get-git-rev)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_get_git_rev([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, char *rev)[#](#_CPPv421rocsparse_get_git_rev16rocsparse_handlePc) Get rocSPARSE git revision.

`rocsparse_get_git_rev`

gets the rocSPARSE library git commit revision (SHA-1).**Example**rocsparse_handle handle; rocsparse_create_handle(&handle); rocsparse_get_git_rev(handle, rocsparse_rev); rocsparse_destroy_handle(handle);


- Parameters:
**handle**–**[in]**the handle to the rocSPARSE library context.**rev**–**[out]**the git commit revision (SHA-1).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_handle**–`handle`

is invalid.



## rocsparse_destroy_error()[#](#rocsparse-destroy-error)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_error([rocsparse_error](types.html#_CPPv415rocsparse_error)error)[#](#_CPPv423rocsparse_destroy_error15rocsparse_error) Destroy a rocsparse error descriptor.

`rocsparse_destroy_error`

destroys the rocSPARSE error descriptor.- Parameters:
**error**–**[in]**the pointer to the rocSPARSE error descriptor, it can be a null pointer.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_error_get_message()[#](#rocsparse-error-get-message)

-
const char *rocsparse_error_get_message(
[rocsparse_error](types.html#_CPPv415rocsparse_error)error)[#](#_CPPv427rocsparse_error_get_message15rocsparse_error) Eerror message from a rocsparse error descriptor.

`rocsparse_error_message`

returns a C-style string that provides detail for the error.- Parameters:
**error**–**[in]**the error to the rocSPARSE error descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_internal_error**– an internal error occurred.

- Returns:
an error message from a rocsparse error descriptor.



## rocsparse_create_mat_descr()[#](#rocsparse-create-mat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_mat_descr([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)*descr)[#](#_CPPv426rocsparse_create_mat_descrP19rocsparse_mat_descr) Create a matrix descriptor.

`rocsparse_create_mat_descr`

creates a matrix descriptor. It initializes[rocsparse_matrix_type](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75)to[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_fill_mode](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1)to[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e),[rocsparse_diag_type](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5)to[rocsparse_diag_type_non_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5a4f6d3d25237d1b2520659c9ec7635cf1),[rocsparse_index_base](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060d)to[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d), and[rocsparse_storage_mode](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13e)to[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff). It should be destroyed at the end using[rocsparse_destroy_mat_descr()](#rocsparse-auxiliary_8h_1a014b60f1fd861c0043fed4b03f068b6b).The matrix type, fill mode, diag type, index base, and storage mode can be set using the

[rocsparse_set_mat_type](#rocsparse-auxiliary_8h_1aee1ac5812c3291dce837a3d4e0847973),[rocsparse_set_mat_fill_mode](#rocsparse-auxiliary_8h_1aa1a9f7ba86427f6b56ea878fbee04db9),[rocsparse_set_mat_diag_type](#rocsparse-auxiliary_8h_1a61f894d80e4da74c7e8cd43f61f9215c),[rocsparse_set_mat_index_base](#rocsparse-auxiliary_8h_1a590fbadaeab2d0edebbf14e2a82a3a8c), and[rocsparse_set_mat_storage_mode](#rocsparse-auxiliary_8h_1a56de830362b6785ff367658ebe31fea7)APIs respectively.- Parameters:
**descr**–**[out]**the pointer to the matrix descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.



## rocsparse_destroy_mat_descr()[#](#rocsparse-destroy-mat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_mat_descr([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr)[#](#_CPPv427rocsparse_destroy_mat_descr19rocsparse_mat_descr) Destroy a matrix descriptor.

`rocsparse_destroy_mat_descr`

destroys a matrix descriptor and releases all resources used by the descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

is invalid.



## rocsparse_copy_mat_descr()[#](#rocsparse-copy-mat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_copy_mat_descr([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)dest, const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)src)[#](#_CPPv424rocsparse_copy_mat_descr19rocsparse_mat_descrK19rocsparse_mat_descr) Copy a matrix descriptor.

`rocsparse_copy_mat_descr`

copies a matrix descriptor. Both, source and destination matrix descriptors must be initialized prior to calling`rocsparse_copy_mat_descr`

.- Parameters:
**dest**–**[out]**the pointer to the destination matrix descriptor.**src**–**[in]**the pointer to the source matrix descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`src`

or`dest`

pointer is invalid.



## rocsparse_set_mat_index_base()[#](#rocsparse-set-mat-index-base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_mat_index_base([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)base)[#](#_CPPv428rocsparse_set_mat_index_base19rocsparse_mat_descr20rocsparse_index_base) Specify the index base of a matrix descriptor.

`rocsparse_set_mat_index_base`

sets the index base of a matrix descriptor. Valid options are[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).- Parameters:
**descr**–**[inout]**the matrix descriptor.**base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.**rocsparse_status_invalid_value**–`base`

is invalid.



## rocsparse_get_mat_index_base()[#](#rocsparse-get-mat-index-base)

-
[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)rocsparse_get_mat_index_base(const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr)[#](#_CPPv428rocsparse_get_mat_index_baseK19rocsparse_mat_descr) Get the index base of a matrix descriptor.

`rocsparse_get_mat_index_base`

returns the index base of a matrix descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Returns:


## rocsparse_set_mat_type()[#](#rocsparse-set-mat-type)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_mat_type([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)type)[#](#_CPPv422rocsparse_set_mat_type19rocsparse_mat_descr21rocsparse_matrix_type) Specify the matrix type of a matrix descriptor.

`rocsparse_set_mat_type`

sets the matrix type of a matrix descriptor. Valid matrix types are[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).- Parameters:
**descr**–**[inout]**the matrix descriptor.**type**–**[in]**[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.**rocsparse_status_invalid_value**–`type`

is invalid.



## rocsparse_get_mat_type()[#](#rocsparse-get-mat-type)

-
[rocsparse_matrix_type](enumerations.html#_CPPv421rocsparse_matrix_type)rocsparse_get_mat_type(const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr)[#](#_CPPv422rocsparse_get_mat_typeK19rocsparse_mat_descr) Get the matrix type of a matrix descriptor.

`rocsparse_get_mat_type`

returns the matrix type of a matrix descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Returns:
[rocsparse_matrix_type_general](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8374056a76ce56d1392e6b35f8ddde03),[rocsparse_matrix_type_symmetric](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a8340a3909d43b5b6bedd8ecc928605a5),[rocsparse_matrix_type_hermitian](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75aa30592e2cccfda6e1d66dc3a484fc7a8)or[rocsparse_matrix_type_triangular](enumerations.html#rocsparse-types_8h_1aa7d5259898cb2181f3fb785246962d75a73d9ef5e5e18209f9f10a5885d3e15ba).


## rocsparse_set_mat_fill_mode()[#](#rocsparse-set-mat-fill-mode)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_mat_fill_mode([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)fill_mode)[#](#_CPPv427rocsparse_set_mat_fill_mode19rocsparse_mat_descr19rocsparse_fill_mode) Specify the matrix fill mode of a matrix descriptor.

`rocsparse_set_mat_fill_mode`

sets the matrix fill mode of a matrix descriptor. Valid fill modes are[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).- Parameters:
**descr**–**[inout]**the matrix descriptor.**fill_mode**–**[in]**[rocsparse_fill_mode_lower](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a1eb644f6f2701329635e07d91919d37e)or[rocsparse_fill_mode_upper](enumerations.html#rocsparse-types_8h_1ae3a66441e40bb7caa1861df90aae01d1a905f490c7fc5a59e8a635938cec0d004).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.**rocsparse_status_invalid_value**–`fill_mode`

is invalid.



## rocsparse_get_mat_fill_mode()[#](#rocsparse-get-mat-fill-mode)

-
[rocsparse_fill_mode](enumerations.html#_CPPv419rocsparse_fill_mode)rocsparse_get_mat_fill_mode(const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr)[#](#_CPPv427rocsparse_get_mat_fill_modeK19rocsparse_mat_descr) Get the matrix fill mode of a matrix descriptor.

`rocsparse_get_mat_fill_mode`

returns the matrix fill mode of a matrix descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Returns:


## rocsparse_set_mat_diag_type()[#](#rocsparse-set-mat-diag-type)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_mat_diag_type([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_diag_type](enumerations.html#_CPPv419rocsparse_diag_type)diag_type)[#](#_CPPv427rocsparse_set_mat_diag_type19rocsparse_mat_descr19rocsparse_diag_type) Specify the matrix diagonal type of a matrix descriptor.

`rocsparse_set_mat_diag_type`

sets the matrix diagonal type of a matrix descriptor. Valid diagonal types are[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)or[rocsparse_diag_type_non_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5a4f6d3d25237d1b2520659c9ec7635cf1).- Parameters:
**descr**–**[inout]**the matrix descriptor.**diag_type**–**[in]**[rocsparse_diag_type_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5ac14545fb3bf8773d5f6b8e258c9576f4)or[rocsparse_diag_type_non_unit](enumerations.html#rocsparse-types_8h_1a6e8e038adcd3fa03168a1cb4a7da1bc5a4f6d3d25237d1b2520659c9ec7635cf1).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.**rocsparse_status_invalid_value**–`diag_type`

is invalid.



## rocsparse_get_mat_diag_type()[#](#rocsparse-get-mat-diag-type)

-
[rocsparse_diag_type](enumerations.html#_CPPv419rocsparse_diag_type)rocsparse_get_mat_diag_type(const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr)[#](#_CPPv427rocsparse_get_mat_diag_typeK19rocsparse_mat_descr) Get the matrix diagonal type of a matrix descriptor.

`rocsparse_get_mat_diag_type`

returns the matrix diagonal type of a matrix descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Returns:


## rocsparse_set_mat_storage_mode()[#](#rocsparse-set-mat-storage-mode)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_set_mat_storage_mode([rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr,[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)storage_mode)[#](#_CPPv430rocsparse_set_mat_storage_mode19rocsparse_mat_descr22rocsparse_storage_mode) Specify the matrix storage mode of a matrix descriptor.

`rocsparse_set_mat_storage_mode`

sets the matrix storage mode of a matrix descriptor. Valid fill modes are[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_unsorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13eafebdc12265a5dbd242288a4e664fcc64).- Parameters:
**descr**–**[inout]**the matrix descriptor.**storage_mode**–**[in]**[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_unsorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13eafebdc12265a5dbd242288a4e664fcc64).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.**rocsparse_status_invalid_value**–`storage_mode`

is invalid.



## rocsparse_get_mat_storage_mode()[#](#rocsparse-get-mat-storage-mode)

-
[rocsparse_storage_mode](enumerations.html#_CPPv422rocsparse_storage_mode)rocsparse_get_mat_storage_mode(const[rocsparse_mat_descr](types.html#_CPPv419rocsparse_mat_descr)descr)[#](#_CPPv430rocsparse_get_mat_storage_modeK19rocsparse_mat_descr) Get the matrix storage mode of a matrix descriptor.

`rocsparse_get_mat_storage_mode`

returns the matrix storage mode of a matrix descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Returns:
[rocsparse_storage_mode_sorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13ea73d28ef281d17b58cf46a846fd515fff)or[rocsparse_storage_mode_unsorted](enumerations.html#rocsparse-types_8h_1ad159dca3bdce1ba175f67e59ed17d13eafebdc12265a5dbd242288a4e664fcc64).


## rocsparse_create_hyb_mat()[#](#rocsparse-create-hyb-mat)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_hyb_mat([rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)*hyb)[#](#_CPPv424rocsparse_create_hyb_matP17rocsparse_hyb_mat) Create a

`HYB`

matrix structure.`rocsparse_create_hyb_mat`

creates a structure that holds the matrix in`HYB`

storage format. It should be destroyed at the end using[rocsparse_destroy_hyb_mat()](#rocsparse-auxiliary_8h_1aa4425f19d565953d9309538d1a3bcc74).- Parameters:
**hyb**–**[inout]**the pointer to the hybrid matrix.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`hyb`

pointer is invalid.



## rocsparse_destroy_hyb_mat()[#](#rocsparse-destroy-hyb-mat)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_hyb_mat([rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)hyb)[#](#_CPPv425rocsparse_destroy_hyb_mat17rocsparse_hyb_mat) Destroy a

`HYB`

matrix structure.`rocsparse_destroy_hyb_mat`

destroys a`HYB`

structure.- Parameters:
**hyb**–**[in]**the hybrid matrix structure.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`hyb`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_copy_hyb_mat()[#](#rocsparse-copy-hyb-mat)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_copy_hyb_mat([rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)dest, const[rocsparse_hyb_mat](types.html#_CPPv417rocsparse_hyb_mat)src)[#](#_CPPv422rocsparse_copy_hyb_mat17rocsparse_hyb_matK17rocsparse_hyb_mat) Copy a

`HYB`

matrix structure.`rocsparse_copy_hyb_mat`

copies a matrix info structure. Both, source and destination matrix info structure must be initialized prior to calling`rocsparse_copy_hyb_mat`

.- Parameters:
**dest**–**[out]**the pointer to the destination matrix info structure.**src**–**[in]**the pointer to the source matrix info structure.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`hyb`

pointer is invalid.



## rocsparse_create_mat_info()[#](#rocsparse-create-mat-info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_mat_info([rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)*info)[#](#_CPPv425rocsparse_create_mat_infoP18rocsparse_mat_info) Create a matrix info structure.

`rocsparse_create_mat_info`

creates a structure that holds the matrix info data that is gathered during the analysis routines available. It should be destroyed at the end using[rocsparse_destroy_mat_info()](#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).- Parameters:
**info**–**[inout]**the pointer to the info structure.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.



## rocsparse_copy_mat_info()[#](#rocsparse-copy-mat-info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_copy_mat_info([rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)dest, const[rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)src)[#](#_CPPv423rocsparse_copy_mat_info18rocsparse_mat_infoK18rocsparse_mat_info) Copy a matrix info structure.

`rocsparse_copy_mat_info`

copies a matrix info structure. Both, source and destination matrix info structure must be initialized prior to calling`rocsparse_copy_mat_info`

.- Parameters:
**dest**–**[out]**the pointer to the destination matrix info structure.**src**–**[in]**the pointer to the source matrix info structure.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`src`

or`dest`

pointer is invalid.



## rocsparse_destroy_mat_info()[#](#rocsparse-destroy-mat-info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_mat_info([rocsparse_mat_info](types.html#_CPPv418rocsparse_mat_info)info)[#](#_CPPv426rocsparse_destroy_mat_info18rocsparse_mat_info) Destroy a matrix info structure.

`rocsparse_destroy_mat_info`

destroys a matrix info structure.- Parameters:
**info**–**[in]**the info structure.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_create_color_info()[#](#rocsparse-create-color-info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_color_info([rocsparse_color_info](types.html#_CPPv420rocsparse_color_info)*info)[#](#_CPPv427rocsparse_create_color_infoP20rocsparse_color_info) Create a color info structure.

`rocsparse_create_color_info`

creates a structure that holds the color info data that is gathered during the analysis routines available. It should be destroyed at the end using[rocsparse_destroy_color_info()](#rocsparse-auxiliary_8h_1a56e7e0ef6b6408b84b82ac42e1e4f020).- Parameters:
**info**–**[inout]**the pointer to the info structure.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.



## rocsparse_destroy_color_info()[#](#rocsparse-destroy-color-info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_color_info([rocsparse_color_info](types.html#_CPPv420rocsparse_color_info)info)[#](#_CPPv428rocsparse_destroy_color_info20rocsparse_color_info) Destroy a color info structure.

`rocsparse_destroy_color_info`

destroys a color info structure.- Parameters:
**info**–**[in]**the info structure.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`info`

pointer is invalid.**rocsparse_status_internal_error**– an internal error occurred.



## rocsparse_copy_color_info()[#](#rocsparse-copy-color-info)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_copy_color_info([rocsparse_color_info](types.html#_CPPv420rocsparse_color_info)dest, const[rocsparse_color_info](types.html#_CPPv420rocsparse_color_info)src)[#](#_CPPv425rocsparse_copy_color_info20rocsparse_color_infoK20rocsparse_color_info) Copy a color info structure.

`rocsparse_copy_color_info`

copies a color info structure. Both, source and destination color info structure must be initialized prior to calling`rocsparse_copy_color_info`

.- Parameters:
**dest**–**[out]**the pointer to the destination color info structure.**src**–**[in]**the pointer to the source color info structure.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`src`

or`dest`

pointer is invalid.



## rocsparse_create_spvec_descr()[#](#rocsparse-create-spvec-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_spvec_descr([rocsparse_spvec_descr](types.html#_CPPv421rocsparse_spvec_descr)*descr, int64_t size, int64_t nnz, void *indices, void *values,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv428rocsparse_create_spvec_descrP21rocsparse_spvec_descr7int64_t7int64_tPvPv19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse vector descriptor.

`rocsparse_create_spvec_descr`

creates a sparse vector descriptor. It should be destroyed at the end using[rocsparse_destroy_mat_descr()](#rocsparse-auxiliary_8h_1a014b60f1fd861c0043fed4b03f068b6b).- Parameters:
**descr**–**[out]**the pointer to the sparse vector descriptor.**size**–**[in]**size of the sparse vector.**nnz**–**[in]**number of non-zeros in sparse vector.**indices**–**[in]**indices of the sparse vector where non-zeros occur (must be array of length`nnz`

).**values**–**[in]**non-zero values in the sparse vector (must be array of length`nnz`

).**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`indices`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`size`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_destroy_spvec_descr()[#](#rocsparse-destroy-spvec-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_spvec_descr([rocsparse_const_spvec_descr](types.html#_CPPv427rocsparse_const_spvec_descr)descr)[#](#_CPPv429rocsparse_destroy_spvec_descr27rocsparse_const_spvec_descr) Destroy a sparse vector descriptor.

`rocsparse_destroy_spvec_descr`

destroys a sparse vector descriptor and releases all resources used by the descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

is invalid.



## rocsparse_spvec_get()[#](#rocsparse-spvec-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spvec_get(const[rocsparse_spvec_descr](types.html#_CPPv421rocsparse_spvec_descr)descr, int64_t *size, int64_t *nnz, void **indices, void **values,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv419rocsparse_spvec_getK21rocsparse_spvec_descrP7int64_tP7int64_tPPvPPvP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse vector descriptor.

`rocsparse_spvec_get`

gets the fields of the sparse vector descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse vector descriptor.**size**–**[out]**size of the sparse vector.**nnz**–**[out]**number of non-zeros in sparse vector.**indices**–**[out]**indices of the sparse vector where non-zeros occur (must be array of length`nnz`

).**values**–**[out]**non-zero values in the sparse vector (must be array of length`nnz`

).**idx_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`indices`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`size`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_spvec_get_index_base()[#](#rocsparse-spvec-get-index-base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spvec_get_index_base([rocsparse_const_spvec_descr](types.html#_CPPv427rocsparse_const_spvec_descr)descr,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base)[#](#_CPPv430rocsparse_spvec_get_index_base27rocsparse_const_spvec_descrP20rocsparse_index_base) Get the index base stored in the sparse vector descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse vector descriptor.**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_value**– if`idx_base`

is invalid.



## rocsparse_spvec_get_values()[#](#rocsparse-spvec-get-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spvec_get_values(const[rocsparse_spvec_descr](types.html#_CPPv421rocsparse_spvec_descr)descr, void **values)[#](#_CPPv426rocsparse_spvec_get_valuesK21rocsparse_spvec_descrPPv) Get the values array stored in the sparse vector descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse vector descriptor.**values**–**[out]**non-zero values in the sparse vector (must be array of length`nnz`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.



## rocsparse_spvec_set_values()[#](#rocsparse-spvec-set-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spvec_set_values([rocsparse_spvec_descr](types.html#_CPPv421rocsparse_spvec_descr)descr, void *values)[#](#_CPPv426rocsparse_spvec_set_values21rocsparse_spvec_descrPv) Set the values array in the sparse vector descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**values**–**[in]**non-zero values in the sparse vector (must be array of length`nnz`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.



## rocsparse_create_coo_descr[#](#rocsparse-create-coo-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_coo_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, void *coo_row_ind, void *coo_col_ind, void *coo_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv426rocsparse_create_coo_descrP21rocsparse_spmat_descr7int64_t7int64_t7int64_tPvPvPv19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse COO matrix descriptor.

`rocsparse_create_coo_descr`

creates a sparse COO matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse COO matrix descriptor.**rows**–**[in]**number of rows in the COO matrix.**cols**–**[in]**number of columns in the COO matrix**nnz**–**[in]**number of non-zeros in the COO matrix.**coo_row_ind**–**[in]**row indices of the COO matrix (must be array of length`nnz`

).**coo_col_ind**–**[in]**column indices of the COO matrix (must be array of length`nnz`

).**coo_val**–**[in]**values of the COO matrix (must be array of length`nnz`

).**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_row_ind`

or`coo_col_ind`

or`coo_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_coo_aos_descr[#](#rocsparse-create-coo-aos-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_coo_aos_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, void *coo_ind, void *coo_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv430rocsparse_create_coo_aos_descrP21rocsparse_spmat_descr7int64_t7int64_t7int64_tPvPv19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse COO AoS matrix descriptor.

`rocsparse_create_coo_aos_descr`

creates a sparse COO AoS matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse COO AoS matrix descriptor.**rows**–**[in]**number of rows in the COO AoS matrix.**cols**–**[in]**number of columns in the COO AoS matrix**nnz**–**[in]**number of non-zeros in the COO AoS matrix.**coo_ind**–**[in]**<row, column> indices of the COO AoS matrix (must be array of length`nnz`

).**coo_val**–**[in]**values of the COO AoS matrix (must be array of length`nnz`

).**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_ind`

or`coo_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_csr_descr[#](#rocsparse-create-csr-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_csr_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, void *csr_row_ptr, void *csr_col_ind, void *csr_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)row_ptr_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv426rocsparse_create_csr_descrP21rocsparse_spmat_descr7int64_t7int64_t7int64_tPvPvPv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse CSR matrix descriptor.

`rocsparse_create_csr_descr`

creates a sparse CSR matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse CSR matrix descriptor.**rows**–**[in]**number of rows in the CSR matrix.**cols**–**[in]**number of columns in the CSR matrix**nnz**–**[in]**number of non-zeros in the CSR matrix.**csr_row_ptr**–**[in]**row offsets of the CSR matrix (must be array of length`rows+1`

).**csr_col_ind**–**[in]**column indices of the CSR matrix (must be array of length`nnz`

).**csr_val**–**[in]**values of the CSR matrix (must be array of length`nnz`

).**row_ptr_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**col_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`csr_row_ptr`

or`csr_col_ind`

or`csr_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`row_ptr_type`

or`col_ind_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_csc_descr[#](#rocsparse-create-csc-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_csc_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, void *csc_col_ptr, void *csc_row_ind, void *csc_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)col_ptr_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)row_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv426rocsparse_create_csc_descrP21rocsparse_spmat_descr7int64_t7int64_t7int64_tPvPvPv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse CSC matrix descriptor.

`rocsparse_create_csc_descr`

creates a sparse CSC matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse CSC matrix descriptor.**rows**–**[in]**number of rows in the CSC matrix.**cols**–**[in]**number of columns in the CSC matrix**nnz**–**[in]**number of non-zeros in the CSC matrix.**csc_col_ptr**–**[in]**column offsets of the CSC matrix (must be array of length`cols+1`

).**csc_row_ind**–**[in]**row indices of the CSC matrix (must be array of length`nnz`

).**csc_val**–**[in]**values of the CSC matrix (must be array of length`nnz`

).**col_ptr_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**row_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`csc_col_ptr`

or`csc_row_ind`

or`csc_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`col_ptr_type`

or`row_ind_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_bsr_descr[#](#rocsparse-create-bsr-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_bsr_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t mb, int64_t nb, int64_t nnzb,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)block_dir, int64_t block_dim, void *bsr_row_ptr, void *bsr_col_ind, void *bsr_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)row_ptr_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv426rocsparse_create_bsr_descrP21rocsparse_spmat_descr7int64_t7int64_t7int64_t19rocsparse_direction7int64_tPvPvPv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse BSR matrix descriptor.

`rocsparse_create_bsr_descr`

creates a sparse BSR matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse BSR matrix descriptor.**mb**–**[in]**number of rows in the BSR matrix.**nb**–**[in]**number of columns in the BSR matrix**nnzb**–**[in]**number of non-zeros in the BSR matrix.**block_dir**–**[in]**direction of the internal block storage.**block_dim**–**[in]**dimension of the blocks.**bsr_row_ptr**–**[in]**row offsets of the BSR matrix (must be array of length`mb+1`

).**bsr_col_ind**–**[in]**column indices of the BSR matrix (must be array of length`nnzb`

).**bsr_val**–**[in]**values of the BSR matrix (must be array of length`nnzb`

*`block_dim`

*`block_dim`

).**row_ptr_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**col_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`bsr_row_ptr`

or`bsr_col_ind`

or`bsr_val`

is invalid.**rocsparse_status_invalid_size**– if`mb`

or`nb`

or`nnzb`

`block_dim`

is invalid.**rocsparse_status_invalid_value**– if`row_ptr_type`

or`col_ind_type`

or`idx_base`

or`data_type`

or`block_dir`

is invalid.



## rocsparse_create_ell_descr[#](#rocsparse-create-ell-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_ell_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols, void *ell_col_ind, void *ell_val, int64_t ell_width,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv426rocsparse_create_ell_descrP21rocsparse_spmat_descr7int64_t7int64_tPvPv7int64_t19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse ELL matrix descriptor.

`rocsparse_create_ell_descr`

creates a sparse ELL matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse ELL matrix descriptor.**rows**–**[in]**number of rows in the ELL matrix.**cols**–**[in]**number of columns in the ELL matrix**ell_col_ind**–**[in]**column indices of the ELL matrix (must be array of length`rows*ell_width`

).**ell_val**–**[in]**values of the ELL matrix (must be array of length`rows*ell_width`

).**ell_width**–**[in]**width of the ELL matrix.**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`ell_col_ind`

or`ell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`ell_width`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_bell_descr[#](#rocsparse-create-bell-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_bell_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)ell_block_dir, int64_t ell_block_dim, int64_t ell_cols, void *ell_col_ind, void *ell_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv427rocsparse_create_bell_descrP21rocsparse_spmat_descr7int64_t7int64_t19rocsparse_direction7int64_t7int64_tPvPv19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse blocked ELL matrix descriptor.

`rocsparse_create_bell_descr`

creates a sparse blocked ELL matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.Currently the only routine that supports the Blocked ELL format is

[rocsparse_spmm](generic.html#rocsparse__spmm_8h_1a0e65f540947b2c9e172ab7cbfa2d5f8a).- Parameters:
**descr**–**[out]**the pointer to the sparse blocked ELL matrix descriptor.**rows**–**[in]**number of rows in the blocked ELL matrix.**cols**–**[in]**number of columns in the blocked ELL matrix**ell_block_dir**–**[in]**[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**ell_block_dim**–**[in]**block dimension of the sparse blocked ELL matrix.**ell_cols**–**[in]**column indices of the blocked ELL matrix (must be array of length`rows*ell_width`

).**ell_col_ind**–**[in]**column indices of the blocked ELL matrix (must be array of length`rows*ell_width`

).**ell_val**–**[in]**values of the blocked ELL matrix (must be array of length`rows*ell_width`

).**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`ell_cols`

or`ell_col_ind`

or`ell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_sell_descr[#](#rocsparse-create-sell-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_sell_descr([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, int64_t sell_slice_size, int64_t sell_colval_size, void *sell_slice_offsets, void *sell_col_ind, void *sell_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)sell_slice_offsets_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)sell_col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv427rocsparse_create_sell_descrP21rocsparse_spmat_descr7int64_t7int64_t7int64_t7int64_t7int64_tPvPvPv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse sliced ELL matrix descriptor.

`rocsparse_create_sell_descr`

creates a sparse slice ELL matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.Currently the only routine that supports the sliced ELL format is

[rocsparse_spmv](generic.html#rocsparse__spmv_8h_1aa4c929b4f9449cf10df016f7c1a17dea).- Parameters:
**descr**–**[out]**the pointer to the sparse sliced ELL matrix descriptor.**rows**–**[in]**number of rows in the sliced ELL matrix.**cols**–**[in]**number of columns in the sliced ELL matrix**nnz**–**[in]**number of non-zeros in the sliced ELL matrix.**sell_slice_size**–**[in]**slice size in the sliced ELL matrix.**sell_colval_size**–**[in]**size of the column and value arrays in the sliced ELL matrix.**sell_slice_offsets**–**[in]**slice offsets into column and value arrays (must be array of length`nslices+1`

where`nslice=m/sell_slice_size`

).**sell_col_ind**–**[in]**column indices of the sliced ELL matrix (must be array of length`sell_colval_size`

).**sell_val**–**[in]**values of the sliced ELL matrix (must be array of length`sell_colval_size`

).**sell_slice_offsets_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**sell_col_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`sell_slice_offsets`

or`sell_col_ind`

or`sell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

pr`sell_slice_size`

or`sell_colval_size`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_const_coo_descr[#](#rocsparse-create-const-coo-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_coo_descr([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, const void *coo_row_ind, const void *coo_col_ind, const void *coo_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv432rocsparse_create_const_coo_descrP27rocsparse_const_spmat_descr7int64_t7int64_t7int64_tPKvPKvPKv19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse COO matrix descriptor.

`rocsparse_create_coo_descr`

creates a sparse COO matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse COO matrix descriptor.**rows**–**[in]**number of rows in the COO matrix.**cols**–**[in]**number of columns in the COO matrix**nnz**–**[in]**number of non-zeros in the COO matrix.**coo_row_ind**–**[in]**row indices of the COO matrix (must be array of length`nnz`

).**coo_col_ind**–**[in]**column indices of the COO matrix (must be array of length`nnz`

).**coo_val**–**[in]**values of the COO matrix (must be array of length`nnz`

).**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_row_ind`

or`coo_col_ind`

or`coo_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_const_csr_descr[#](#rocsparse-create-const-csr-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_csr_descr([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, const void *csr_row_ptr, const void *csr_col_ind, const void *csr_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)row_ptr_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv432rocsparse_create_const_csr_descrP27rocsparse_const_spmat_descr7int64_t7int64_t7int64_tPKvPKvPKv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse CSR matrix descriptor.

`rocsparse_create_csr_descr`

creates a sparse CSR matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse CSR matrix descriptor.**rows**–**[in]**number of rows in the CSR matrix.**cols**–**[in]**number of columns in the CSR matrix**nnz**–**[in]**number of non-zeros in the CSR matrix.**csr_row_ptr**–**[in]**row offsets of the CSR matrix (must be array of length`rows+1`

).**csr_col_ind**–**[in]**column indices of the CSR matrix (must be array of length`nnz`

).**csr_val**–**[in]**values of the CSR matrix (must be array of length`nnz`

).**row_ptr_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**col_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`csr_row_ptr`

or`csr_col_ind`

or`csr_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`row_ptr_type`

or`col_ind_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_const_csc_descr[#](#rocsparse-create-const-csc-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_csc_descr([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, const void *csc_col_ptr, const void *csc_row_ind, const void *csc_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)col_ptr_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)row_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv432rocsparse_create_const_csc_descrP27rocsparse_const_spmat_descr7int64_t7int64_t7int64_tPKvPKvPKv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse CSC matrix descriptor.

`rocsparse_create_csc_descr`

creates a sparse CSC matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.- Parameters:
**descr**–**[out]**the pointer to the sparse CSC matrix descriptor.**rows**–**[in]**number of rows in the CSC matrix.**cols**–**[in]**number of columns in the CSC matrix**nnz**–**[in]**number of non-zeros in the CSC matrix.**csc_col_ptr**–**[in]**column offsets of the CSC matrix (must be array of length`cols+1`

).**csc_row_ind**–**[in]**row indices of the CSC matrix (must be array of length`nnz`

).**csc_val**–**[in]**values of the CSC matrix (must be array of length`nnz`

).**col_ptr_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**row_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`csc_col_ptr`

or`csc_row_ind`

or`csc_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`col_ptr_type`

or`row_ind_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_const_bell_descr[#](#rocsparse-create-const-bell-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_bell_descr([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)*descr, int64_t rows, int64_t cols,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)ell_block_dir, int64_t ell_block_dim, int64_t ell_cols, const void *ell_col_ind, const void *ell_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv433rocsparse_create_const_bell_descrP27rocsparse_const_spmat_descr7int64_t7int64_t19rocsparse_direction7int64_t7int64_tPKvPKv19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse blocked ELL matrix descriptor.

`rocsparse_create_bell_descr`

creates a sparse blocked ELL matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.Currently the only routine that supports the Blocked ELL format is

[rocsparse_spmm](generic.html#rocsparse__spmm_8h_1a0e65f540947b2c9e172ab7cbfa2d5f8a).- Parameters:
**descr**–**[out]**the pointer to the sparse blocked ELL matrix descriptor.**rows**–**[in]**number of rows in the blocked ELL matrix.**cols**–**[in]**number of columns in the blocked ELL matrix**ell_block_dir**–**[in]**[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**ell_block_dim**–**[in]**block dimension of the sparse blocked ELL matrix.**ell_cols**–**[in]**column indices of the blocked ELL matrix (must be array of length`rows*ell_width`

).**ell_col_ind**–**[in]**column indices of the blocked ELL matrix (must be array of length`rows*ell_width`

).**ell_val**–**[in]**values of the blocked ELL matrix (must be array of length`rows*ell_width`

).**idx_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`ell_cols`

or`ell_col_ind`

or`ell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_create_const_sell_descr[#](#rocsparse-create-const-sell-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_sell_descr([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)*descr, int64_t rows, int64_t cols, int64_t nnz, int64_t sell_slice_size, int64_t sell_colval_size, const void *sell_slice_offsets, const void *sell_col_ind, const void *sell_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)sell_slice_offsets_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)sell_col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv433rocsparse_create_const_sell_descrP27rocsparse_const_spmat_descr7int64_t7int64_t7int64_t7int64_t7int64_tPKvPKvPKv19rocsparse_indextype19rocsparse_indextype20rocsparse_index_base18rocsparse_datatype) Create a sparse sliced ELL matrix descriptor.

`rocsparse_create_sell_descr`

creates a sparse slice ELL matrix descriptor. It should be destroyed at the end using`rocsparse_destroy_spmat_descr`

.Currently the only routine that supports the sliced ELL format is

[rocsparse_spmv](generic.html#rocsparse__spmv_8h_1aa4c929b4f9449cf10df016f7c1a17dea).- Parameters:
**descr**–**[out]**the pointer to the sparse sliced ELL matrix descriptor.**rows**–**[in]**number of rows in the sliced ELL matrix.**cols**–**[in]**number of columns in the sliced ELL matrix**nnz**–**[in]**number of non-zeros in the sliced ELL matrix.**sell_slice_size**–**[in]**slice size in the sliced ELL matrix.**sell_colval_size**–**[in]**size of the column and value arrays in the sliced ELL matrix.**sell_slice_offsets**–**[in]**slice offsets into column and value arrays (must be array of length`nslices+1`

where`nslice=m/sell_slice_size`

).**sell_col_ind**–**[in]**column indices of the sliced ELL matrix (must be array of length`sell_colval_size`

).**sell_val**–**[in]**values of the sliced ELL matrix (must be array of length`sell_colval_size`

).**sell_slice_offsets_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**sell_col_ind_type**–**[in]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[in]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`sell_slice_offsets`

or`sell_col_ind`

or`sell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

pr`sell_slice_size`

or`sell_colval_size`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_destroy_spmat_descr[#](#rocsparse-destroy-spmat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_spmat_descr([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr)[#](#_CPPv429rocsparse_destroy_spmat_descr27rocsparse_const_spmat_descr) Destroy a sparse matrix descriptor.

`rocsparse_destroy_spmat_descr`

destroys a sparse matrix descriptor and releases all resources used by the descriptor.Currently the only routine that supports the Blocked ELL format is

[rocsparse_spmm](generic.html#rocsparse__spmm_8h_1a0e65f540947b2c9e172ab7cbfa2d5f8a).- Parameters:
**descr**–**[in]**the matrix descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

is invalid.



## rocsparse_create_sparse_to_sparse_descr[#](#rocsparse-create-sparse-to-sparse-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_sparse_to_sparse_descr([rocsparse_sparse_to_sparse_descr](types.html#_CPPv432rocsparse_sparse_to_sparse_descr)*descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)source,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)target,[rocsparse_sparse_to_sparse_alg](enumerations.html#_CPPv430rocsparse_sparse_to_sparse_alg)alg)[#](#_CPPv439rocsparse_create_sparse_to_sparse_descrP32rocsparse_sparse_to_sparse_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr30rocsparse_sparse_to_sparse_alg) Sparse matrix to sparse matrix conversion.

`rocsparse_create_sparse_to_sparse_descr`

creates the descriptor of the sparse_to_sparse algorithm.- Parameters:
**descr**–**[out]**pointer to the descriptor of the sparse_to_sparse algorithm.**source**–**[in]**source sparse matrix descriptor.**target**–**[in]**target sparse matrix descriptor.**alg**–**[in]**algorithm for the sparse_to_sparse computation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**– if any required enumeration is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`source`

, or`target`

pointer is invalid.



## rocsparse_destroy_sparse_to_sparse_descr[#](#rocsparse-destroy-sparse-to-sparse-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_sparse_to_sparse_descr([rocsparse_sparse_to_sparse_descr](types.html#_CPPv432rocsparse_sparse_to_sparse_descr)descr)[#](#_CPPv440rocsparse_destroy_sparse_to_sparse_descr32rocsparse_sparse_to_sparse_descr) Sparse matrix to sparse matrix conversion.

`rocsparse_destroy_sparse_to_sparse_descr`

destroys the descriptor of the sparse_to_sparse algorithm.- Parameters:
**descr**–**[in]**descriptor of the sparse_to_sparse algorithm.- Return values:
**rocsparse_status_success**– the operation completed successfully.


## rocsparse_sparse_to_sparse_permissive[#](#rocsparse-sparse-to-sparse-permissive)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sparse_to_sparse_permissive([rocsparse_sparse_to_sparse_descr](types.html#_CPPv432rocsparse_sparse_to_sparse_descr)descr)[#](#_CPPv437rocsparse_sparse_to_sparse_permissive32rocsparse_sparse_to_sparse_descr) Sparse matrix to sparse matrix conversion.

`rocsparse_sparse_to_sparse_permissive`

allows the routine to allocate an intermediate sparse matrix in order to perform the conversion. By default, the routine is not permissive.- Parameters:
**descr**–**[in]**descriptor of the sparse_to_sparse algorithm.- Return values:
**rocsparse_status_success**– the operation completed successfully.


## rocsparse_create_extract_descr[#](#rocsparse-create-extract-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_extract_descr([rocsparse_extract_descr](types.html#_CPPv423rocsparse_extract_descr)*descr,[rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)source,[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)target,[rocsparse_extract_alg](enumerations.html#_CPPv421rocsparse_extract_alg)alg)[#](#_CPPv430rocsparse_create_extract_descrP23rocsparse_extract_descr27rocsparse_const_spmat_descr21rocsparse_spmat_descr21rocsparse_extract_alg) Sparse matrix extraction.

`rocsparse_create_extract_descr`

creates the descriptor of the extract algorithm.- Parameters:
**descr**–**[out]**pointer to the descriptor of the extract algorithm.**source**–**[in]**source sparse matrix descriptor.**target**–**[in]**target sparse matrix descriptor.**alg**–**[in]**algorithm for the extract computation.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_value**– if any required enumeration is invalid.**rocsparse_status_invalid_pointer**–`descr`

,`source`

, or`target`

pointer is invalid.



## rocsparse_destroy_extract_descr[#](#rocsparse-destroy-extract-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_extract_descr([rocsparse_extract_descr](types.html#_CPPv423rocsparse_extract_descr)descr)[#](#_CPPv431rocsparse_destroy_extract_descr23rocsparse_extract_descr) Sparse matrix extraction.

`rocsparse_destroy_extract_descr`

destroys the descriptor of the[rocsparse_extract](generic.html#rocsparse__extract_8h_1ad9110cab48a4ebbc6e04dc4e22b1f0f3)routine.- Parameters:
**descr**–**[in]**descriptor of the extract routine.- Return values:
**rocsparse_status_success**– the operation completed successfully.


## rocsparse_create_spgeam_descr[#](#rocsparse-create-spgeam-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_spgeam_descr(rocsparse_spgeam_descr *descr)[#](#_CPPv429rocsparse_create_spgeam_descrP22rocsparse_spgeam_descr) Sparse matrix spgeam.

`rocsparse_create_spgeam_descr`

creates the descriptor of the[rocsparse_spgeam_buffer_size](generic.html#rocsparse__spgeam_8h_1aefc21d68d17849c7efef71b3347a0427)and[rocsparse_spgeam](generic.html#rocsparse__spgeam_8h_1ac6994d8e5bbf8af3b275d193de933f92)routines.- Parameters:
**descr**–**[out]**pointer to the descriptor of the SpGEAM routine.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.



## rocsparse_destroy_spgeam_descr[#](#rocsparse-destroy-spgeam-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_spgeam_descr(rocsparse_spgeam_descr descr)[#](#_CPPv430rocsparse_destroy_spgeam_descr22rocsparse_spgeam_descr) Sparse matrix spgeam.

`rocsparse_destroy_spgeam_descr`

destroys the descriptor of the[rocsparse_spgeam_buffer_size](generic.html#rocsparse__spgeam_8h_1aefc21d68d17849c7efef71b3347a0427)and[rocsparse_spgeam](generic.html#rocsparse__spgeam_8h_1ac6994d8e5bbf8af3b275d193de933f92)routines.- Parameters:
**descr**–**[in]**descriptor of the spgeam routine.- Return values:
**rocsparse_status_success**– the operation completed successfully.


## rocsparse_spgeam_set_input[#](#rocsparse-spgeam-set-input)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spgeam_set_input([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spgeam_descr descr,[rocsparse_spgeam_input](enumerations.html#_CPPv422rocsparse_spgeam_input)input, const void *data, size_t data_size_in_bytes,[rocsparse_error](types.html#_CPPv415rocsparse_error)*p_error)[#](#_CPPv426rocsparse_spgeam_set_input16rocsparse_handle22rocsparse_spgeam_descr22rocsparse_spgeam_inputPKv6size_tP15rocsparse_error) Set the requested

[rocsparse_spgeam_input](enumerations.html#rocsparse-types_8h_1a14aad71f5468fe647ba3ea4770ac111b)data in the SpGEAM descriptor.- Parameters:
**handle**–**[in]**the pointer to the handle to the rocSPARSE library context.**descr**–**[inout]**the pointer to the SpGEAM descriptor.**input**–**[in]**one of the values from[rocsparse_spgeam_input](enumerations.html#rocsparse-types_8h_1a14aad71f5468fe647ba3ea4770ac111b)**data**–**[in]**input data**data_size_in_bytes**–**[in]**input data size.**p_error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`data`

is invalid.**rocsparse_status_invalid_value**– if`input`

is invalid.**rocsparse_status_invalid_size**– if`data_size_in_bytes`

is invalid.



## rocsparse_spgeam_get_output[#](#rocsparse-spgeam-get-output)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spgeam_get_output([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spgeam_descr descr,[rocsparse_spgeam_output](enumerations.html#_CPPv423rocsparse_spgeam_output)output, void *data, size_t data_size_in_bytes,[rocsparse_error](types.html#_CPPv415rocsparse_error)*error)[#](#_CPPv427rocsparse_spgeam_get_output16rocsparse_handle22rocsparse_spgeam_descr23rocsparse_spgeam_outputPv6size_tP15rocsparse_error) Get the requested

[rocsparse_spgeam_output](enumerations.html#rocsparse-types_8h_1a78cf02e5f35dd98ccfd635397169fa8b)data from the SpGEAM descriptor.- Parameters:
**handle**–**[in]**the pointer to the handle to the rocSPARSE library context.**descr**–**[inout]**the pointer to the SpGEAM descriptor.**output**–**[in]**[rocsparse_spgeam_output_nnz](enumerations.html#rocsparse-types_8h_1a78cf02e5f35dd98ccfd635397169fa8ba3677a9158b8c97873ce09598cf69b75a)**data**–**[in]**output data**data_size_in_bytes**–**[in]**output data size.**error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`data`

is invalid.**rocsparse_status_invalid_value**– if`output`

is invalid.**rocsparse_status_invalid_size**– if`data_size_in_bytes`

is invalid.



## rocsparse_create_spmv_descr[#](#rocsparse-create-spmv-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_spmv_descr(rocsparse_spmv_descr *descr)[#](#_CPPv427rocsparse_create_spmv_descrP20rocsparse_spmv_descr) Sparse matrix spmv.

`rocsparse_create_spmv_descr`

creates the descriptor of the[rocsparse_v2_spmv_buffer_size](generic.html#rocsparse__v2__spmv_8h_1ac9b01de6fbc79a5a98e1c69dd9708ccd)and[rocsparse_v2_spmv](generic.html#rocsparse__v2__spmv_8h_1a82054ad1c5ba87b41b757948d23d30fc)routines.- Parameters:
**descr**–**[out]**pointer to the descriptor of the SpMV routine.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

pointer is invalid.



## rocsparse_destroy_spmv_descr[#](#rocsparse-destroy-spmv-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_spmv_descr(rocsparse_spmv_descr descr)[#](#_CPPv428rocsparse_destroy_spmv_descr20rocsparse_spmv_descr) Sparse matrix spmv.

`rocsparse_destroy_spmv_descr`

destroys the descriptor of the[rocsparse_v2_spmv_buffer_size](generic.html#rocsparse__v2__spmv_8h_1ac9b01de6fbc79a5a98e1c69dd9708ccd)and[rocsparse_v2_spmv](generic.html#rocsparse__v2__spmv_8h_1a82054ad1c5ba87b41b757948d23d30fc)routines.- Parameters:
**descr**–**[in]**descriptor of the v2_spmv routine.- Return values:
**rocsparse_status_success**– the operation completed successfully.


## rocsparse_spmv_set_input[#](#rocsparse-spmv-set-input)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmv_set_input([rocsparse_handle](types.html#_CPPv416rocsparse_handle)handle, rocsparse_spmv_descr descr,[rocsparse_spmv_input](enumerations.html#_CPPv420rocsparse_spmv_input)input, const void *in, size_t size_in_bytes,[rocsparse_error](types.html#_CPPv415rocsparse_error)*error)[#](#_CPPv424rocsparse_spmv_set_input16rocsparse_handle20rocsparse_spmv_descr20rocsparse_spmv_inputPKv6size_tP15rocsparse_error) Set the requested

[rocsparse_spmv_input](enumerations.html#rocsparse-types_8h_1a7cf3074b95bdd0d961330be4515d3903)data in the SpMV descriptor.- Parameters:
**handle**–**[in]**the pointer to the handle to the rocSPARSE library context.**descr**–**[inout]**the pointer to the SpMV descriptor.**input**–**[in]**one possible value of[rocsparse_spmv_input](enumerations.html#rocsparse-types_8h_1a7cf3074b95bdd0d961330be4515d3903)**in**–**[in]**input value**size_in_bytes**–**[in]**input value size in bytes.**error**–**[out]**error descriptor created if the returned status is not[rocsparse_status_success](enumerations.html#rocsparse-types_8h_1a578f8c5c1b08f358bf4605b0031006a8a96462a9361cfceb6cf9354e10fdc671b). A null pointer can be passed if the user is not interested in obtaining an error descriptor.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`in`

is invalid.**rocsparse_status_invalid_value**– if`input`

is invalid.**rocsparse_status_invalid_size**– if`size_in_bytes`

is zero.



## rocsparse_coo_get[#](#rocsparse-coo-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coo_get(const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, int64_t *rows, int64_t *cols, int64_t *nnz, void **coo_row_ind, void **coo_col_ind, void **coo_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv417rocsparse_coo_getK21rocsparse_spmat_descrP7int64_tP7int64_tP7int64_tPPvPPvPPvP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse COO matrix descriptor.

`rocsparse_coo_get`

gets the fields of the sparse COO matrix descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse COO matrix descriptor.**rows**–**[out]**number of rows in the sparse COO matrix.**cols**–**[out]**number of columns in the sparse COO matrix.**nnz**–**[out]**number of non-zeros in sparse COO matrix.**coo_row_ind**–**[out]**row indices of the COO matrix (must be array of length`nnz`

).**coo_col_ind**–**[out]**column indices of the COO matrix (must be array of length`nnz`

).**coo_val**–**[out]**values of the COO matrix (must be array of length`nnz`

).**idx_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_row_ind`

or`coo_col_ind`

or`coo_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_coo_aos_get[#](#rocsparse-coo-aos-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coo_aos_get(const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, int64_t *rows, int64_t *cols, int64_t *nnz, void **coo_ind, void **coo_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv421rocsparse_coo_aos_getK21rocsparse_spmat_descrP7int64_tP7int64_tP7int64_tPPvPPvP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse COO AoS matrix descriptor.

`rocsparse_coo_aos_get`

gets the fields of the sparse COO AoS matrix descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse COO AoS matrix descriptor.**rows**–**[out]**number of rows in the sparse COO AoS matrix.**cols**–**[out]**number of columns in the sparse COO AoS matrix.**nnz**–**[out]**number of non-zeros in sparse COO AoS matrix.**coo_ind**–**[out]**<row, columns> indices of the COO AoS matrix (must be array of length`nnz`

).**coo_val**–**[out]**values of the COO AoS matrix (must be array of length`nnz`

).**idx_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_ind`

or`coo_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_csr_get[#](#rocsparse-csr-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr_get(const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, int64_t *rows, int64_t *cols, int64_t *nnz, void **csr_row_ptr, void **csr_col_ind, void **csr_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*row_ptr_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv417rocsparse_csr_getK21rocsparse_spmat_descrP7int64_tP7int64_tP7int64_tPPvPPvPPvP19rocsparse_indextypeP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse CSR matrix descriptor.

`rocsparse_csr_get`

gets the fields of the sparse CSR matrix descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse CSR matrix descriptor.**rows**–**[out]**number of rows in the CSR matrix.**cols**–**[out]**number of columns in the CSR matrix**nnz**–**[out]**number of non-zeros in the CSR matrix.**csr_row_ptr**–**[out]**row offsets of the CSR matrix (must be array of length`rows+1`

).**csr_col_ind**–**[out]**column indices of the CSR matrix (must be array of length`nnz`

).**csr_val**–**[out]**values of the CSR matrix (must be array of length`nnz`

).**row_ptr_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**col_ind_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`csr_row_ptr`

or`csr_col_ind`

or`csr_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.**rocsparse_status_invalid_value**– if`row_ptr_type`

or`col_ind_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_ell_get[#](#rocsparse-ell-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ell_get(const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, int64_t *rows, int64_t *cols, void **ell_col_ind, void **ell_val, int64_t *ell_width,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv417rocsparse_ell_getK21rocsparse_spmat_descrP7int64_tP7int64_tPPvPPvP7int64_tP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse ELL matrix descriptor.

`rocsparse_ell_get`

gets the fields of the sparse ELL matrix descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse ELL matrix descriptor.**rows**–**[out]**number of rows in the ELL matrix.**cols**–**[out]**number of columns in the ELL matrix**ell_col_ind**–**[out]**column indices of the ELL matrix (must be array of length`rows*ell_width`

).**ell_val**–**[out]**values of the ELL matrix (must be array of length`rows*ell_width`

).**ell_width**–**[out]**width of the ELL matrix.**idx_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`ell_col_ind`

or`ell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`ell_width`

is invalid.**rocsparse_status_invalid_value**– if`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_bell_get[#](#rocsparse-bell-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bell_get(const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, int64_t *rows, int64_t *cols,[rocsparse_direction](enumerations.html#_CPPv419rocsparse_direction)*ell_block_dir, int64_t *ell_block_dim, int64_t *ell_cols, void **ell_col_ind, void **ell_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*idx_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv418rocsparse_bell_getK21rocsparse_spmat_descrP7int64_tP7int64_tP19rocsparse_directionP7int64_tP7int64_tPPvPPvP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse blocked ELL matrix descriptor.

`rocsparse_bell_get`

gets the fields of the sparse blocked ELL matrix descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse blocked ELL matrix descriptor.**rows**–**[out]**number of rows in the blocked ELL matrix.**cols**–**[out]**number of columns in the blocked ELL matrix**ell_block_dir**–**[out]**[rocsparse_direction_row](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca40d95f05d0cd4ad3c89465959c58943e)or[rocsparse_direction_column](enumerations.html#rocsparse-types_8h_1a1975ceac5a0aae162dca78582ee2a56ca23355bb7b606c550ba61c781bcecfc5b).**ell_block_dim**–**[out]**block dimension of the sparse blocked ELL matrix.**ell_cols**–**[out]**column indices of the blocked ELL matrix (must be array of length`rows*ell_width`

).**ell_col_ind**–**[out]**column indices of the blocked ELL matrix (must be array of length`rows*ell_width`

).**ell_val**–**[out]**values of the blocked ELL matrix (must be array of length`rows*ell_width`

).**idx_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`ell_cols`

or`ell_col_ind`

or`ell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`ell_block_dim`

is invalid.**rocsparse_status_invalid_value**– if`ell_block_dir`

or`idx_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_sell_get[#](#rocsparse-sell-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_sell_get(const[rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, int64_t *rows, int64_t *cols, int64_t *nnz, int64_t *sell_slice_size, int64_t *sell_colval_size, void **sell_slice_offsets, void **sell_col_ind, void **sell_val,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*sell_slice_offsets_type,[rocsparse_indextype](enumerations.html#_CPPv419rocsparse_indextype)*sell_col_ind_type,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv418rocsparse_sell_getK21rocsparse_spmat_descrP7int64_tP7int64_tP7int64_tP7int64_tP7int64_tPPvPPvPPvP19rocsparse_indextypeP19rocsparse_indextypeP20rocsparse_index_baseP18rocsparse_datatype) Get the fields of the sparse sliced ELL matrix descriptor.

`rocsparse_sell_get`

gets the fields of the sparse sliced ELL matrix descriptor- Parameters:
**descr**–**[in]**the pointer to the sparse sliced ELL matrix descriptor.**rows**–**[out]**number of rows in the sliced ELL matrix.**cols**–**[out]**number of columns in the sliced ELL matrix**nnz**–**[out]**number of non-zeros in the sliced ELL matix.**sell_slice_size**–**[out]**slice size in the sliced ELL matrix.**sell_colval_size**–**[out]**actual number of elements stored in the sliced ELL matrix.**sell_slice_offsets**–**[out]**slice offsets array in the sliced ELL matrix (must be array of length`nslices`

+ 1 where`nslices=`

(rows-1)/sell_slice_size+1 ).**sell_col_ind**–**[out]**column indices of the sliced ELL matrix (must be array of length`sell_colval_size`

).**sell_val**–**[out]**values of the sliced ELL matrix (must be array of length`sell_colval_size`

).**sell_slice_offsets_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**sell_col_ind_type**–**[out]**[rocsparse_indextype_i32](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666afeb5495f2a20e642311223c1035fa92a)or[rocsparse_indextype_i64](enumerations.html#rocsparse-types_8h_1aeea59369d310397d0f995b7d54502666ae077f4d43a04ad38399d32b4abfe9cc4).**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`sell_slice_offsets`

or`sell_col_ind`

or`sell_val`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

or`sell_colval_size`

or`sell_slice_size`

is invalid.**rocsparse_status_invalid_value**– if`sell_slice_offsets_type`

or`sell_col_ind_type`

or`idx_base`

or`data_type`

is invalid.



## rocsparse_coo_set_pointers[#](#rocsparse-coo-set-pointers)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coo_set_pointers([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *coo_row_ind, void *coo_col_ind, void *coo_val)[#](#_CPPv426rocsparse_coo_set_pointers21rocsparse_spmat_descrPvPvPv) Set the row indices, column indices and values array in the sparse COO matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**coo_row_ind**–**[in]**row indices of the COO matrix (must be array of length`nnz`

).**coo_col_ind**–**[in]**column indices of the COO matrix (must be array of length`nnz`

).**coo_val**–**[in]**values of the COO matrix (must be array of length`nnz`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_row_ind`

or`coo_col_ind`

or`coo_val`

is invalid.



## rocsparse_coo_aos_set_pointers[#](#rocsparse-coo-aos-set-pointers)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coo_aos_set_pointers([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *coo_ind, void *coo_val)[#](#_CPPv430rocsparse_coo_aos_set_pointers21rocsparse_spmat_descrPvPv) Set the <row, column> indices and values array in the sparse COO AoS matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**coo_ind**–**[in]**<row, column> indices of the COO matrix (must be array of length`nnz`

).**coo_val**–**[in]**values of the COO matrix (must be array of length`nnz`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_ind`

or`coo_val`

is invalid.



## rocsparse_csr_set_pointers[#](#rocsparse-csr-set-pointers)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr_set_pointers([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *csr_row_ptr, void *csr_col_ind, void *csr_val)[#](#_CPPv426rocsparse_csr_set_pointers21rocsparse_spmat_descrPvPvPv) Set the row offsets, column indices and values array in the sparse CSR matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**csr_row_ptr**–**[in]**row offsets of the CSR matrix (must be array of length`rows+1`

).**csr_col_ind**–**[in]**column indices of the CSR matrix (must be array of length`nnz`

).**csr_val**–**[in]**values of the CSR matrix (must be array of length`nnz`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`coo_ind`

or`coo_val`

is invalid.



## rocsparse_csc_set_pointers[#](#rocsparse-csc-set-pointers)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csc_set_pointers([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *csc_col_ptr, void *csc_row_ind, void *csc_val)[#](#_CPPv426rocsparse_csc_set_pointers21rocsparse_spmat_descrPvPvPv) Set the column offsets, row indices and values array in the sparse CSC matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**csc_col_ptr**–**[in]**column offsets of the CSC matrix (must be array of length`cols+1`

).**csc_row_ind**–**[in]**row indices of the CSC matrix (must be array of length`nnz`

).**csc_val**–**[in]**values of the CSC matrix (must be array of length`nnz`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`csc_col_ptr`

or`csc_row_ind`

or`csc_val`

is invalid.



## rocsparse_ell_set_pointers[#](#rocsparse-ell-set-pointers)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_ell_set_pointers([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *ell_col_ind, void *ell_val)[#](#_CPPv426rocsparse_ell_set_pointers21rocsparse_spmat_descrPvPv) Set the column indices and values array in the sparse ELL matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**ell_col_ind**–**[in]**column indices of the ELL matrix (must be array of length`rows*ell_width`

).**ell_val**–**[in]**values of the ELL matrix (must be array of length`rows*ell_width`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`ell_col_ind`

or`ell_val`

is invalid.



## rocsparse_bsr_set_pointers[#](#rocsparse-bsr-set-pointers)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_bsr_set_pointers([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *bsr_row_ptr, void *bsr_col_ind, void *bsr_val)[#](#_CPPv426rocsparse_bsr_set_pointers21rocsparse_spmat_descrPvPvPv) Set the row offsets, column indices and values array in the sparse BSR matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse vector descriptor.**bsr_row_ptr**–**[in]**row offsets of the BSR matrix (must be array of length`rows+1`

).**bsr_col_ind**–**[in]**column indices of the BSR matrix (must be array of length`nnzb`

).**bsr_val**–**[in]**values of the BSR matrix (must be array of length`nnzb*block_dim*block_dim`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`bsr_row_ptr`

or`bsr_col_ind`

or`bsr_val`

is invalid.



## rocsparse_spmat_get_size[#](#rocsparse-spmat-get-size)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_size([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr, int64_t *rows, int64_t *cols, int64_t *nnz)[#](#_CPPv424rocsparse_spmat_get_size27rocsparse_const_spmat_descrP7int64_tP7int64_tP7int64_t) Get the number of rows, columns and non-zeros from the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**rows**–**[out]**number of rows in the sparse matrix.**cols**–**[out]**number of columns in the sparse matrix.**nnz**–**[out]**number of non-zeros in sparse matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`nnz`

is invalid.



## rocsparse_spmat_get_nnz[#](#rocsparse-spmat-get-nnz)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_nnz([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr, int64_t *nnz)[#](#_CPPv423rocsparse_spmat_get_nnz27rocsparse_const_spmat_descrP7int64_t) Get the number of non-zeros from the sparse matrix descriptor.

Note

The returned number of non-zeros is the number of elements of the array of values of the sparse matrix.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**nnz**–**[out]**the number of non-zeros of the sparse matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`nnz`

is invalid.



## rocsparse_spmat_get_format[#](#rocsparse-spmat-get-format)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_format([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr,[rocsparse_format](enumerations.html#_CPPv416rocsparse_format)*format)[#](#_CPPv426rocsparse_spmat_get_format27rocsparse_const_spmat_descrP16rocsparse_format) Get the sparse matrix format from the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**format**–**[out]**[rocsparse_format_coo](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a11b2282b2de9242f0b9a8607cf835423)or[rocsparse_format_coo_aos](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378affaa78f83b090b976f77765f259e0981)or[rocsparse_format_csr](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a26160296ec3d447960cf2f5958a2f84d)or[rocsparse_format_csc](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378af8fdd82ccbbc7b2f7386eae16f284e08)or[rocsparse_format_ell](enumerations.html#rocsparse-types_8h_1ae1c0b9de06f3772ed14403400320b378a37a77201d206121094dacef57666d80b)

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_value**– if`format`

is invalid.



## rocsparse_spmat_get_index_base[#](#rocsparse-spmat-get-index-base)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_index_base([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr,[rocsparse_index_base](enumerations.html#_CPPv420rocsparse_index_base)*idx_base)[#](#_CPPv430rocsparse_spmat_get_index_base27rocsparse_const_spmat_descrP20rocsparse_index_base) Get the sparse matrix index base from the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**idx_base**–**[out]**[rocsparse_index_base_zero](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da71f5a4d652495d496d1b049fbfd4074d)or[rocsparse_index_base_one](enumerations.html#rocsparse-types_8h_1a170a3a8edd9e1d990e1321a0367d060da7ebbfb972c7bb96f4960a3c80d8b0625)

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_value**– if`idx_base`

is invalid.



## rocsparse_spmat_get_values[#](#rocsparse-spmat-get-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_values([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void **values)[#](#_CPPv426rocsparse_spmat_get_values21rocsparse_spmat_descrPPv) Get the values array from the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**values**–**[out]**values array of the sparse matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.



## rocsparse_spmat_set_values[#](#rocsparse-spmat-set-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_set_values([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr, void *values)[#](#_CPPv426rocsparse_spmat_set_values21rocsparse_spmat_descrPv) Set the values array in the sparse matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse matrix descriptor.**values**–**[in]**values array of the sparse matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.



## rocsparse_spmat_get_strided_batch[#](#rocsparse-spmat-get-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_strided_batch([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*batch_count)[#](#_CPPv433rocsparse_spmat_get_strided_batch27rocsparse_const_spmat_descrP13rocsparse_int) Get the strided batch count from the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**batch_count**–**[out]**batch_count of the sparse matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

is invalid.



## rocsparse_spmat_set_strided_batch[#](#rocsparse-spmat-set-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_set_strided_batch([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count)[#](#_CPPv433rocsparse_spmat_set_strided_batch21rocsparse_spmat_descr13rocsparse_int) Set the strided batch count in the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**batch_count**–**[in]**batch_count of the sparse matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

is invalid.



## rocsparse_coo_set_strided_batch[#](#rocsparse-coo-set-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_coo_set_strided_batch([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count, int64_t batch_stride)[#](#_CPPv431rocsparse_coo_set_strided_batch21rocsparse_spmat_descr13rocsparse_int7int64_t) Set the batch count and batch stride in the sparse COO matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse COO matrix descriptor.**batch_count**–**[in]**batch_count of the sparse COO matrix.**batch_stride**–**[in]**batch stride of the sparse COO matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

or`batch_stride`

is invalid.



## rocsparse_csr_set_strided_batch[#](#rocsparse-csr-set-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csr_set_strided_batch([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count, int64_t offsets_batch_stride, int64_t columns_values_batch_stride)[#](#_CPPv431rocsparse_csr_set_strided_batch21rocsparse_spmat_descr13rocsparse_int7int64_t7int64_t) Set the batch count, row offset batch stride and the column indices batch stride in the sparse CSR matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse CSR matrix descriptor.**batch_count**–**[in]**batch_count of the sparse CSR matrix.**offsets_batch_stride**–**[in]**row offset batch stride of the sparse CSR matrix.**columns_values_batch_stride**–**[in]**column indices batch stride of the sparse CSR matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

or`offsets_batch_stride`

or`columns_values_batch_stride`

is invalid.



## rocsparse_csc_set_strided_batch[#](#rocsparse-csc-set-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_csc_set_strided_batch([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count, int64_t offsets_batch_stride, int64_t rows_values_batch_stride)[#](#_CPPv431rocsparse_csc_set_strided_batch21rocsparse_spmat_descr13rocsparse_int7int64_t7int64_t) Set the batch count, column offset batch stride and the row indices batch stride in the sparse CSC matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse CSC matrix descriptor.**batch_count**–**[in]**batch_count of the sparse CSC matrix.**offsets_batch_stride**–**[in]**column offset batch stride of the sparse CSC matrix.**rows_values_batch_stride**–**[in]**row indices batch stride of the sparse CSC matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

or`offsets_batch_stride`

or`rows_values_batch_stride`

is invalid.



## rocsparse_spmat_get_attribute[#](#rocsparse-spmat-get-attribute)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_get_attribute([rocsparse_const_spmat_descr](types.html#_CPPv427rocsparse_const_spmat_descr)descr,[rocsparse_spmat_attribute](enumerations.html#_CPPv425rocsparse_spmat_attribute)attribute, void *data, size_t data_size)[#](#_CPPv429rocsparse_spmat_get_attribute27rocsparse_const_spmat_descr25rocsparse_spmat_attributePv6size_t) Get the requested attribute data from the sparse matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the sparse matrix descriptor.**attribute**–**[in]**[rocsparse_spmat_fill_mode](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07a82fc7516bbe52e3f44d3f796dc509253)or[rocsparse_spmat_diag_type](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07a7d33b080f3fbfc774d389e41ff52ae5c)or[rocsparse_spmat_matrix_type](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07ae04bb3c1ca0f2c2752f140d54cfbe995)or[rocsparse_spmat_storage_mode](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07a8180d2295fe0f56ec4ec2397addd85c9)**data**–**[out]**attribute data**data_size**–**[in]**attribute data size.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`data`

is invalid.**rocsparse_status_invalid_value**– if`attribute`

is invalid.**rocsparse_status_invalid_size**– if`data_size`

is invalid.



## rocsparse_spmat_set_attribute[#](#rocsparse-spmat-set-attribute)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_spmat_set_attribute([rocsparse_spmat_descr](types.html#_CPPv421rocsparse_spmat_descr)descr,[rocsparse_spmat_attribute](enumerations.html#_CPPv425rocsparse_spmat_attribute)attribute, const void *data, size_t data_size)[#](#_CPPv429rocsparse_spmat_set_attribute21rocsparse_spmat_descr25rocsparse_spmat_attributePKv6size_t) Set the requested attribute data in the sparse matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the sparse matrix descriptor.**attribute**–**[in]**[rocsparse_spmat_fill_mode](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07a82fc7516bbe52e3f44d3f796dc509253)or[rocsparse_spmat_diag_type](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07a7d33b080f3fbfc774d389e41ff52ae5c)or[rocsparse_spmat_matrix_type](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07ae04bb3c1ca0f2c2752f140d54cfbe995)or[rocsparse_spmat_storage_mode](enumerations.html#rocsparse-types_8h_1ad84e79592aecad930b96561ced224b07a8180d2295fe0f56ec4ec2397addd85c9)**data**–**[in]**attribute data**data_size**–**[in]**attribute data size.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`data`

is invalid.**rocsparse_status_invalid_value**– if`attribute`

is invalid.**rocsparse_status_invalid_size**– if`data_size`

is invalid.



## rocsparse_create_dnvec_descr[#](#rocsparse-create-dnvec-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_dnvec_descr([rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)*descr, int64_t size, void *values,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv428rocsparse_create_dnvec_descrP21rocsparse_dnvec_descr7int64_tPv18rocsparse_datatype) Create a dense vector descriptor.

`rocsparse_create_dnvec_descr`

creates a dense vector descriptor. It should be destroyed at the end using[rocsparse_destroy_dnvec_descr()](#rocsparse-auxiliary_8h_1a7bd4cf18649566f7017e84ba7ff2e400).- Parameters:
**descr**–**[out]**the pointer to the dense vector descriptor.**size**–**[in]**size of the dense vector.**values**–**[in]**non-zero values in the dense vector (must be array of length`size`

).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`size`

is invalid.**rocsparse_status_invalid_value**– if`data_type`

is invalid.



## rocsparse_create_const_dnvec_descr[#](#rocsparse-create-const-dnvec-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_dnvec_descr([rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)*descr, int64_t size, const void *values,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type)[#](#_CPPv434rocsparse_create_const_dnvec_descrP27rocsparse_const_dnvec_descr7int64_tPKv18rocsparse_datatype) Create a dense vector descriptor.

`rocsparse_create_dnvec_descr`

creates a dense vector descriptor. It should be destroyed at the end using[rocsparse_destroy_dnvec_descr()](#rocsparse-auxiliary_8h_1a7bd4cf18649566f7017e84ba7ff2e400).- Parameters:
**descr**–**[out]**the pointer to the dense vector descriptor.**size**–**[in]**size of the dense vector.**values**–**[in]**non-zero values in the dense vector (must be array of length`size`

).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`size`

is invalid.**rocsparse_status_invalid_value**– if`data_type`

is invalid.



## rocsparse_destroy_dnvec_descr[#](#rocsparse-destroy-dnvec-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_dnvec_descr([rocsparse_const_dnvec_descr](types.html#_CPPv427rocsparse_const_dnvec_descr)descr)[#](#_CPPv429rocsparse_destroy_dnvec_descr27rocsparse_const_dnvec_descr) Destroy a dense vector descriptor.

`rocsparse_destroy_dnvec_descr`

destroys a dense vector descriptor and releases all resources used by the descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

is invalid.



## rocsparse_dnvec_get[#](#rocsparse-dnvec-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnvec_get(const[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)descr, int64_t *size, void **values,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type)[#](#_CPPv419rocsparse_dnvec_getK21rocsparse_dnvec_descrP7int64_tPPvP18rocsparse_datatype) Get the fields of the dense vector descriptor.

`rocsparse_dnvec_get`

gets the fields of the dense vector descriptor- Parameters:
**descr**–**[in]**the pointer to the dense vector descriptor.**size**–**[out]**size of the dense vector.**values**–**[out]**non-zero values in the dense vector (must be array of length`size`

).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`size`

is invalid.**rocsparse_status_invalid_value**– if`data_type`

is invalid.



## rocsparse_dnvec_get_values[#](#rocsparse-dnvec-get-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnvec_get_values(const[rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)descr, void **values)[#](#_CPPv426rocsparse_dnvec_get_valuesK21rocsparse_dnvec_descrPPv) Get the values array from a dense vector descriptor.

- Parameters:
**descr**–**[in]**the matrix descriptor.**values**–**[out]**non-zero values in the dense vector (must be array of length`size`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

or`values`

is invalid.



## rocsparse_dnvec_set_values[#](#rocsparse-dnvec-set-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnvec_set_values([rocsparse_dnvec_descr](types.html#_CPPv421rocsparse_dnvec_descr)descr, void *values)[#](#_CPPv426rocsparse_dnvec_set_values21rocsparse_dnvec_descrPv) Set the values array in a dense vector descriptor.

- Parameters:
**descr**–**[inout]**the matrix descriptor.**values**–**[in]**non-zero values in the dense vector (must be array of length`size`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

or`values`

is invalid.



## rocsparse_create_dnmat_descr[#](#rocsparse-create-dnmat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_dnmat_descr([rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)*descr, int64_t rows, int64_t cols, int64_t ld, void *values,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type,[rocsparse_order](enumerations.html#_CPPv415rocsparse_order)order)[#](#_CPPv428rocsparse_create_dnmat_descrP21rocsparse_dnmat_descr7int64_t7int64_t7int64_tPv18rocsparse_datatype15rocsparse_order) Create a dense matrix descriptor.

`rocsparse_create_dnmat_descr`

creates a dense matrix descriptor. It should be destroyed at the end using[rocsparse_destroy_dnmat_descr()](#rocsparse-auxiliary_8h_1a0097b585f6f9c5a39ce5526d58e6206a).- Parameters:
**descr**–**[out]**the pointer to the dense matrix descriptor.**rows**–**[in]**number of rows in the dense matrix.**cols**–**[in]**number of columns in the dense matrix.**ld**–**[in]**leading dimension of the dense matrix.**values**–**[in]**non-zero values in the dense vector (must be array of length`ld*rows`

if`order=rocsparse_order_column`

or`ld*cols`

if`order=rocsparse_order_row`

).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).**order**–**[in]**[rocsparse_order_row](enumerations.html#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fdace7cebc3314be9cab0b132298a3ae9fd)or[rocsparse_order_column](enumerations.html#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fdafe684501aaf1d3f437968240c98706f9).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`ld`

is invalid.**rocsparse_status_invalid_value**– if`data_type`

or`order`

is invalid.



## rocsparse_create_const_dnmat_descr[#](#rocsparse-create-const-dnmat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_create_const_dnmat_descr([rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)*descr, int64_t rows, int64_t cols, int64_t ld, const void *values,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)data_type,[rocsparse_order](enumerations.html#_CPPv415rocsparse_order)order)[#](#_CPPv434rocsparse_create_const_dnmat_descrP27rocsparse_const_dnmat_descr7int64_t7int64_t7int64_tPKv18rocsparse_datatype15rocsparse_order) Create a dense matrix descriptor.

`rocsparse_create_dnmat_descr`

creates a dense matrix descriptor. It should be destroyed at the end using[rocsparse_destroy_dnmat_descr()](#rocsparse-auxiliary_8h_1a0097b585f6f9c5a39ce5526d58e6206a).- Parameters:
**descr**–**[out]**the pointer to the dense matrix descriptor.**rows**–**[in]**number of rows in the dense matrix.**cols**–**[in]**number of columns in the dense matrix.**ld**–**[in]**leading dimension of the dense matrix.**values**–**[in]**non-zero values in the dense vector (must be array of length`ld*rows`

if`order=rocsparse_order_column`

or`ld*cols`

if`order=rocsparse_order_row`

).**data_type**–**[in]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).**order**–**[in]**[rocsparse_order_row](enumerations.html#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fdace7cebc3314be9cab0b132298a3ae9fd)or[rocsparse_order_column](enumerations.html#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fdafe684501aaf1d3f437968240c98706f9).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`ld`

is invalid.**rocsparse_status_invalid_value**– if`data_type`

or`order`

is invalid.



## rocsparse_destroy_dnmat_descr[#](#rocsparse-destroy-dnmat-descr)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_destroy_dnmat_descr([rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)descr)[#](#_CPPv429rocsparse_destroy_dnmat_descr27rocsparse_const_dnmat_descr) Destroy a dense matrix descriptor.

`rocsparse_destroy_dnmat_descr`

destroys a dense matrix descriptor and releases all resources used by the descriptor.- Parameters:
**descr**–**[in]**the matrix descriptor.- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

is invalid.



## rocsparse_dnmat_get[#](#rocsparse-dnmat-get)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnmat_get(const[rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)descr, int64_t *rows, int64_t *cols, int64_t *ld, void **values,[rocsparse_datatype](enumerations.html#_CPPv418rocsparse_datatype)*data_type,[rocsparse_order](enumerations.html#_CPPv415rocsparse_order)*order)[#](#_CPPv419rocsparse_dnmat_getK21rocsparse_dnmat_descrP7int64_tP7int64_tP7int64_tPPvP18rocsparse_datatypeP15rocsparse_order) Get the fields of the dense matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the dense matrix descriptor.**rows**–**[out]**number of rows in the dense matrix.**cols**–**[out]**number of columns in the dense matrix.**ld**–**[out]**leading dimension of the dense matrix.**values**–**[out]**non-zero values in the dense matrix (must be array of length`ld*rows`

if`order=rocsparse_order_column`

or`ld*cols`

if`order=rocsparse_order_row`

).**data_type**–**[out]**[rocsparse_datatype_f32_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edaa62d4737b4cdb93a7f60715db0d01520),[rocsparse_datatype_f64_r](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda2ca573746a15c391064033943edcebdb),[rocsparse_datatype_f32_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108eda680bfd1bcdda1c2e2c23a885fef0d86e)or[rocsparse_datatype_f64_c](enumerations.html#rocsparse-types_8h_1a157ea6ff90ad10035edb1e51232108edadd4150f1dee0d44da9568294d6b11aa2).**order**–**[out]**[rocsparse_order_row](enumerations.html#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fdace7cebc3314be9cab0b132298a3ae9fd)or[rocsparse_order_column](enumerations.html#rocsparse-types_8h_1a2c805a5d353c83120ba8b84cbff620fdafe684501aaf1d3f437968240c98706f9).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.**rocsparse_status_invalid_size**– if`rows`

or`cols`

or`ld`

is invalid.**rocsparse_status_invalid_value**– if`data_type`

or`order`

is invalid.



## rocsparse_dnmat_get_values[#](#rocsparse-dnmat-get-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnmat_get_values(const[rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)descr, void **values)[#](#_CPPv426rocsparse_dnmat_get_valuesK21rocsparse_dnmat_descrPPv) Get the values array from the dense matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the dense matrix descriptor.**values**–**[out]**non-zero values in the dense matrix (must be array of length`ld*rows`

if`order=rocsparse_order_column`

or`ld*cols`

if`order=rocsparse_order_row`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

or`values`

is invalid.



## rocsparse_dnmat_set_values[#](#rocsparse-dnmat-set-values)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnmat_set_values([rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)descr, void *values)[#](#_CPPv426rocsparse_dnmat_set_values21rocsparse_dnmat_descrPv) Set the values array in a dense matrix descriptor.

- Parameters:
**descr**–**[inout]**the matrix descriptor.**values**–**[in]**non-zero values in the dense matrix (must be array of length`ld*rows`

if`order=rocsparse_order_column`

or`ld*cols`

if`order=rocsparse_order_row`

).

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**–`descr`

or`values`

is invalid.



## rocsparse_dnmat_get_strided_batch[#](#rocsparse-dnmat-get-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnmat_get_strided_batch([rocsparse_const_dnmat_descr](types.html#_CPPv427rocsparse_const_dnmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)*batch_count, int64_t *batch_stride)[#](#_CPPv433rocsparse_dnmat_get_strided_batch27rocsparse_const_dnmat_descrP13rocsparse_intP7int64_t) Get the batch count and batch stride from the dense matrix descriptor.

- Parameters:
**descr**–**[in]**the pointer to the dense matrix descriptor.**batch_count**–**[out]**the batch count in the dense matrix.**batch_stride**–**[out]**the batch stride in the dense matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

or`batch_stride`

is invalid.



## rocsparse_dnmat_set_strided_batch[#](#rocsparse-dnmat-set-strided-batch)

-
[rocsparse_status](enumerations.html#_CPPv416rocsparse_status)rocsparse_dnmat_set_strided_batch([rocsparse_dnmat_descr](types.html#_CPPv421rocsparse_dnmat_descr)descr,[rocsparse_int](types.html#_CPPv413rocsparse_int)batch_count, int64_t batch_stride)[#](#_CPPv433rocsparse_dnmat_set_strided_batch21rocsparse_dnmat_descr13rocsparse_int7int64_t) Set the batch count and batch stride in the dense matrix descriptor.

- Parameters:
**descr**–**[inout]**the pointer to the dense matrix descriptor.**batch_count**–**[in]**the batch count in the dense matrix.**batch_stride**–**[in]**the batch stride in the dense matrix.

- Return values:
**rocsparse_status_success**– the operation completed successfully.**rocsparse_status_invalid_pointer**– if`descr`

is invalid.**rocsparse_status_invalid_size**– if`batch_count`

or`batch_stride`

is invalid.
