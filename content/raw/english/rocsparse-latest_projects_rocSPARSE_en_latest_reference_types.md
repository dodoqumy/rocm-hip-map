---
title: "rocSPARSE data types &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:08:52.701982+00:00
content_hash: "c6d8ed64ba49500d"
---

# rocSPARSE data types[#](#rocsparse-data-types)

## rocsparse_handle[#](#rocsparse-handle)

-
typedef struct _rocsparse_handle *rocsparse_handle
[#](#_CPPv416rocsparse_handle) Handle to the rocSPARSE library context queue.

The rocSPARSE handle is a structure holding the rocSPARSE library context. It must be initialized using

[rocsparse_create_handle()](auxiliary.html#rocsparse-auxiliary_8h_1ae89c836b8dee934b84c2d7cd654a0426)and the returned handle must be passed to all subsequent library function calls. It should be destroyed at the end using[rocsparse_destroy_handle()](auxiliary.html#rocsparse-auxiliary_8h_1a87c65c7bbcdb98852704ac2a65478241).

## rocsparse_error[#](#rocsparse-error)

-
typedef struct _rocsparse_error *rocsparse_error
[#](#_CPPv415rocsparse_error) Descriptor of the error.

The rocSPARSE error descriptor is a structure holding the information related to an error that occured during the execution of a rocSPARSE routine. It should be destroyed using

[rocsparse_destroy_error()](auxiliary.html#rocsparse-auxiliary_8h_1a5dc3d115fa882933daeca4de2cae3a26).

## rocsparse_int[#](#rocsparse-int)

-
typedef int32_t rocsparse_int
[#](#_CPPv413rocsparse_int) Specifies rocSPARSE integer type (defaults to int32_t).


## rocsparse_bfloat16[#](#rocsparse-bfloat16)

-
struct rocsparse_bfloat16
[#](#_CPPv418rocsparse_bfloat16) Struct to represent a 16 bit brain floating-point number.


## rocsparse_float_complex[#](#rocsparse-float-complex)

-
struct rocsparse_float_complex
[#](#_CPPv423rocsparse_float_complex) Struct to represent a complex number with float precision real and imaginary parts.


## rocsparse_double_complex[#](#rocsparse-double-complex)

-
struct rocsparse_double_complex
[#](#_CPPv424rocsparse_double_complex) Struct to represent a complex number with double precision real and imaginary parts.


## rocsparse_mat_descr[#](#rocsparse-mat-descr)

-
typedef struct _rocsparse_mat_descr *rocsparse_mat_descr
[#](#_CPPv419rocsparse_mat_descr) Descriptor of the matrix.

The rocSPARSE matrix descriptor is a structure holding all properties of a matrix. It must be initialized using

[rocsparse_create_mat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a936452e9024232518e3b4ebdfdb9ecab)and the returned descriptor must be passed to all subsequent library calls that involve the matrix. It should be destroyed at the end using[rocsparse_destroy_mat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a014b60f1fd861c0043fed4b03f068b6b).

## rocsparse_mat_info[#](#rocsparse-mat-info)

-
typedef struct _rocsparse_mat_info *rocsparse_mat_info
[#](#_CPPv418rocsparse_mat_info) Info structure to hold all matrix meta data.

The rocSPARSE matrix info is a structure holding all matrix information that is gathered during analysis routines. It must be initialized using

[rocsparse_create_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a23eb2202356ebb8506136b4898abdeaf)and the returned info structure must be passed to all subsequent library calls that require additional matrix information. It should be destroyed at the end using[rocsparse_destroy_mat_info()](auxiliary.html#rocsparse-auxiliary_8h_1a9c143f65076a10ebafcffc633ad5d87b).

## rocsparse_hyb_mat[#](#rocsparse-hyb-mat)

-
typedef struct _rocsparse_hyb_mat *rocsparse_hyb_mat
[#](#_CPPv417rocsparse_hyb_mat) HYB matrix storage format.

The rocSPARSE HYB matrix structure holds the HYB matrix. It must be initialized using

[rocsparse_create_hyb_mat()](auxiliary.html#rocsparse-auxiliary_8h_1a0b8464ef21c90b80ad8c870bf0a66ce0)and the returned HYB matrix must be passed to all subsequent library calls that involve the matrix. It should be destroyed at the end using[rocsparse_destroy_hyb_mat()](auxiliary.html#rocsparse-auxiliary_8h_1aa4425f19d565953d9309538d1a3bcc74).

For more details on the HYB format, see [HYB storage format](../conceptual/storage-formats-sparse.html#hyb-storage-format).

## rocsparse_spvec_descr[#](#rocsparse-spvec-descr)

-
typedef struct _rocsparse_spvec_descr *rocsparse_spvec_descr
[#](#_CPPv421rocsparse_spvec_descr) Generic API descriptor of the sparse vector.

The rocSPARSE sparse vector descriptor is a structure holding all properties of a sparse vector. It must be initialized using

[rocsparse_create_spvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a039eb3a72bc740f459f53e13364ed06b)and the returned descriptor must be passed to all subsequent generic API library calls that involve the sparse vector. It should be destroyed at the end using[rocsparse_destroy_spvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a515afec7ea4f7008b4aafa146bb0fdb8).

## rocsparse_const_spvec_descr[#](#rocsparse-const-spvec-descr)

-
typedef struct _rocsparse_spvec_descr const *rocsparse_const_spvec_descr
[#](#_CPPv427rocsparse_const_spvec_descr) Generic API descriptor of the sparse vector.

The rocSPARSE constant sparse vector descriptor is a structure holding all properties of a sparse vector. It must be initialized using rocsparse_create_const_spvec_descr() and the returned descriptor must be passed to all subsequent generic API library calls that involve the sparse vector. It should be destroyed at the end using

[rocsparse_destroy_spvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a515afec7ea4f7008b4aafa146bb0fdb8).

## rocsparse_spmat_descr[#](#rocsparse-spmat-descr)

-
typedef struct _rocsparse_spmat_descr *rocsparse_spmat_descr
[#](#_CPPv421rocsparse_spmat_descr) Generic API descriptor of the sparse matrix.

The rocSPARSE sparse matrix descriptor is a structure holding all properties of a sparse matrix. It must be initialized using

[rocsparse_create_coo_descr()](auxiliary.html#rocsparse-auxiliary_8h_1aa44e306525a860b074a6ecbbbacdae10),[rocsparse_create_coo_aos_descr()](auxiliary.html#rocsparse-auxiliary_8h_1abf82ada697a4dc8e7d5bb8da969468b0),[rocsparse_create_bsr_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a3aa4dc7fb625a292aea4ccf42b41e8c8),[rocsparse_create_csr_descr()](auxiliary.html#rocsparse-auxiliary_8h_1ad50506ca8757c69dc00ffd1bb4867ef2),[rocsparse_create_csc_descr()](auxiliary.html#rocsparse-auxiliary_8h_1aa66a83fe3f2422496f0d8abc9103b87d),[rocsparse_create_ell_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a7b5cc0af1561522d58f35ba019b62bc1), or[rocsparse_create_bell_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a744a5a943d8f4f30e5eaaf4ed0cb9d5e)and the returned descriptor must be passed to all subsequent generic API library calls that involve the sparse matrix. It should be destroyed at the end using[rocsparse_destroy_spmat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a4798c23eb7a64836089261c6003af83c).

## rocsparse_const_spmat_descr[#](#rocsparse-const-spmat-descr)

-
typedef struct _rocsparse_spmat_descr const *rocsparse_const_spmat_descr
[#](#_CPPv427rocsparse_const_spmat_descr) Generic API descriptor of the sparse matrix.

The rocSPARSE constant sparse matrix descriptor is a structure holding all properties of a sparse matrix. It must be initialized using

[rocsparse_create_const_coo_descr()](auxiliary.html#rocsparse-auxiliary_8h_1ae5171da472192327da810fc5926baee6),[rocsparse_create_const_csr_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a93a7a2111ca90edf298fb29e9f7b6587),[rocsparse_create_const_csc_descr()](auxiliary.html#rocsparse-auxiliary_8h_1ab54bb582977b2c72a7e7fbc4048a22f0), or[rocsparse_create_const_bell_descr()](auxiliary.html#rocsparse-auxiliary_8h_1ab66b71602a81221cd2978956107e4aa7)and the returned descriptor must be passed to all subsequent generic API library calls that involve the sparse matrix. It should be destroyed at the end using[rocsparse_destroy_spmat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a4798c23eb7a64836089261c6003af83c).

## rocsparse_dnvec_descr[#](#rocsparse-dnvec-descr)

-
typedef struct _rocsparse_dnvec_descr *rocsparse_dnvec_descr
[#](#_CPPv421rocsparse_dnvec_descr) Generic API descriptor of the dense vector.

The rocSPARSE dense vector descriptor is a structure holding all properties of a dense vector. It must be initialized using

[rocsparse_create_dnvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a4af239f31ca46361e2091c0de350a193)and the returned descriptor must be passed to all subsequent generic API library calls that involve the dense vector. It should be destroyed at the end using[rocsparse_destroy_dnvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a7bd4cf18649566f7017e84ba7ff2e400).

## rocsparse_const_dnvec_descr[#](#rocsparse-const-dnvec-descr)

-
typedef struct _rocsparse_dnvec_descr const *rocsparse_const_dnvec_descr
[#](#_CPPv427rocsparse_const_dnvec_descr) Generic API descriptor of the dense vector.

The rocSPARSE constant dense vector descriptor is a structure holding all properties of a dense vector. It must be initialized using

[rocsparse_create_const_dnvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a206db44772b70e948d9b172c93fa5ec1)and the returned descriptor must be passed to all subsequent generic API library calls that involve the dense vector. It should be destroyed at the end using[rocsparse_destroy_dnvec_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a7bd4cf18649566f7017e84ba7ff2e400).

## rocsparse_dnmat_descr[#](#rocsparse-dnmat-descr)

-
typedef struct _rocsparse_dnmat_descr *rocsparse_dnmat_descr
[#](#_CPPv421rocsparse_dnmat_descr) Generic API descriptor of the dense matrix.

The rocSPARSE dense matrix descriptor is a structure holding all properties of a dense matrix. It must be initialized using

[rocsparse_create_dnmat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a445cf7ce700b36336f6f8d7aafff2da7)and the returned descriptor must be passed to all subsequent generic API library calls that involve the dense matrix. It should be destroyed at the end using[rocsparse_destroy_dnmat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a0097b585f6f9c5a39ce5526d58e6206a).

## rocsparse_const_dnmat_descr[#](#rocsparse-const-dnmat-descr)

-
typedef struct _rocsparse_dnmat_descr const *rocsparse_const_dnmat_descr
[#](#_CPPv427rocsparse_const_dnmat_descr) Generic API descriptor of the dense matrix.

The rocSPARSE constant dense matrix descriptor is a structure holding all properties of a dense matrix. It must be initialized using

[rocsparse_create_const_dnmat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1ade90d766da746ffeac81bcdefcaa1019)and the returned descriptor must be passed to all subsequent generic API library calls that involve the dense matrix. It should be destroyed at the end using[rocsparse_destroy_dnmat_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a0097b585f6f9c5a39ce5526d58e6206a).

## rocsparse_color_info[#](#rocsparse-color-info)

-
typedef struct _rocsparse_color_info *rocsparse_color_info
[#](#_CPPv420rocsparse_color_info) Coloring info structure to hold data gathered during analysis and later used in rocSPARSE sparse matrix coloring routines.

The rocSPARSE color info is a structure holding coloring data that is gathered during analysis routines. It must be initialized using

[rocsparse_create_color_info()](auxiliary.html#rocsparse-auxiliary_8h_1ad9902c131204639eaa7fff944c25ad6d)and the returned info structure must be passed to all subsequent library calls that require coloring information. It should be destroyed at the end using[rocsparse_destroy_color_info()](auxiliary.html#rocsparse-auxiliary_8h_1a56e7e0ef6b6408b84b82ac42e1e4f020).

## rocsparse_sparse_to_sparse_descr[#](#rocsparse-sparse-to-sparse-descr)

-
typedef struct _rocsparse_sparse_to_sparse_descr *rocsparse_sparse_to_sparse_descr
[#](#_CPPv432rocsparse_sparse_to_sparse_descr) rocsparse_sparse_to_sparse_descr is a structure holding the rocsparse sparse_to_sparse descr data. It must be initialized using the

[rocsparse_create_sparse_to_sparse_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a2703bb20d605f5d62e9646e47c82e836)routine. It should be destroyed at the end using[rocsparse_destroy_sparse_to_sparse_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a8b5aec2b4c87bd20b21a547ae8d09c70).

## rocsparse_extract_descr[#](#rocsparse-extract-descr)

-
typedef struct _rocsparse_extract_descr *rocsparse_extract_descr
[#](#_CPPv423rocsparse_extract_descr) rocsparse_extract_descr is a structure holding the rocsparse extract descr data. It must be initialized using the

[rocsparse_create_extract_descr()](auxiliary.html#rocsparse-auxiliary_8h_1af8a98e6c716b0c93d9387142054d3dcc)routine. It should be destroyed at the end using[rocsparse_destroy_extract_descr()](auxiliary.html#rocsparse-auxiliary_8h_1a22248e885bc5c14ef4445bc6e94e92dd).
