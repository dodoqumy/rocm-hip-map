---
title: "rocSOLVER types &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:07:43.974720+00:00
content_hash: "f63e2bbd90478574"
---

# rocSOLVER types[#](#rocsolver-types)

rocSOLVER uses most types and enumerations defined in rocBLAS for the general operation and
dense matrix computations along with some defined in rocSPARSE for sparse matrix computations, such as direct solvers.
For more information, see the [rocBLAS types](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html) and
[rocSPARSE types](https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/types.html) documentation.

This topic describes the rocSOLVER types that extend the rocBLAS and rocSPARSE APIs.

## rocblas_direct[#](#rocblas-direct)

-
enum rocblas_direct
[#](#_CPPv414rocblas_direct) Used to specify the order in which multiple Householder matrices or plane rotations are applied together (see the documentation of the specific routines for more details).

*Values:*-
enumerator rocblas_forward_direction
[#](#_CPPv4N14rocblas_direct25rocblas_forward_directionE) Forward ordering.


-
enumerator rocblas_backward_direction
[#](#_CPPv4N14rocblas_direct26rocblas_backward_directionE) Backward ordering.


-
enumerator rocblas_forward_direction

## rocblas_pivot[#](#rocblas-pivot)

-
enum rocblas_pivot
[#](#_CPPv413rocblas_pivot) Used to specify the planes on which a sequence of Givens rotations is applied.

*Values:*-
enumerator rocblas_pivot_variable
[#](#_CPPv4N13rocblas_pivot22rocblas_pivot_variableE) The i-th rotation is applied on plane (i,i+1).


-
enumerator rocblas_pivot_top
[#](#_CPPv4N13rocblas_pivot17rocblas_pivot_topE) The i-th rotation is applied on plane (1,i+1).


-
enumerator rocblas_pivot_bottom
[#](#_CPPv4N13rocblas_pivot20rocblas_pivot_bottomE) The i-th rotation is applied on plane (i,m) or (i,n).


-
enumerator rocblas_pivot_variable

## rocblas_storev[#](#rocblas-storev)

## rocblas_svect[#](#rocblas-svect)

-
enum rocblas_svect
[#](#_CPPv413rocblas_svect) Used to specify how the singular vectors are to be computed and stored.

*Values:*-
enumerator rocblas_svect_all
[#](#_CPPv4N13rocblas_svect17rocblas_svect_allE) The entire associated orthogonal/unitary matrix is computed.


-
enumerator rocblas_svect_singular
[#](#_CPPv4N13rocblas_svect22rocblas_svect_singularE) Only the singular vectors are computed and stored in output array.


-
enumerator rocblas_svect_overwrite
[#](#_CPPv4N13rocblas_svect23rocblas_svect_overwriteE) Only the singular vectors are computed and overwrite the input matrix.


-
enumerator rocblas_svect_none
[#](#_CPPv4N13rocblas_svect18rocblas_svect_noneE) No singular vectors are computed.


-
enumerator rocblas_svect_all

## rocblas_srange[#](#rocblas-srange)

-
enum rocblas_srange
[#](#_CPPv414rocblas_srange) Used to specify the type of range in which singular values will be found in partial singular value decompositions.

*Values:*-
enumerator rocblas_srange_all
[#](#_CPPv4N14rocblas_srange18rocblas_srange_allE) All singular values will be found.


-
enumerator rocblas_srange_value
[#](#_CPPv4N14rocblas_srange20rocblas_srange_valueE) All singular values in the half-open interval \((vl, vu]\) will be found.


-
enumerator rocblas_srange_index
[#](#_CPPv4N14rocblas_srange20rocblas_srange_indexE) The \(il\)-th through \(iu\)-th singular values will be found.


-
enumerator rocblas_srange_all

## rocblas_evect[#](#rocblas-evect)

-
enum rocblas_evect
[#](#_CPPv413rocblas_evect) Used to specify how the eigenvectors are to be computed.

*Values:*-
enumerator rocblas_evect_original
[#](#_CPPv4N13rocblas_evect22rocblas_evect_originalE) Compute eigenvectors for the original symmetric/Hermitian matrix.


-
enumerator rocblas_evect_tridiagonal
[#](#_CPPv4N13rocblas_evect25rocblas_evect_tridiagonalE) Compute eigenvectors for the symmetric tridiagonal matrix.


-
enumerator rocblas_evect_none
[#](#_CPPv4N13rocblas_evect18rocblas_evect_noneE) No eigenvectors are computed.


-
enumerator rocblas_evect_original

## rocblas_workmode[#](#rocblas-workmode)

-
enum rocblas_workmode
[#](#_CPPv416rocblas_workmode) Used to enable the use of fast algorithms (with out-of-place computations) in some of the routines.

*Values:*-
enumerator rocblas_outofplace
[#](#_CPPv4N16rocblas_workmode18rocblas_outofplaceE) Out-of-place computations are allowed; this requires extra device memory for workspace.


-
enumerator rocblas_inplace
[#](#_CPPv4N16rocblas_workmode15rocblas_inplaceE) If not enough memory is available, this forces in-place computations.


-
enumerator rocblas_outofplace

## rocblas_eform[#](#rocblas-eform)

## rocblas_erange[#](#rocblas-erange)

-
enum rocblas_erange
[#](#_CPPv414rocblas_erange) Used to specify the type of range in which eigenvalues will be found in partial eigenvalue decompositions.

*Values:*-
enumerator rocblas_erange_all
[#](#_CPPv4N14rocblas_erange18rocblas_erange_allE) All eigenvalues will be found.


-
enumerator rocblas_erange_value
[#](#_CPPv4N14rocblas_erange20rocblas_erange_valueE) All eigenvalues in the half-open interval \((vl, vu]\) will be found.


-
enumerator rocblas_erange_index
[#](#_CPPv4N14rocblas_erange20rocblas_erange_indexE) The \(il\)-th through \(iu\)-th eigenvalues will be found.


-
enumerator rocblas_erange_all

## rocblas_eorder[#](#rocblas-eorder)

-
enum rocblas_eorder
[#](#_CPPv414rocblas_eorder) Used to specify whether the eigenvalues are grouped and ordered by blocks.

*Values:*-
enumerator rocblas_eorder_blocks
[#](#_CPPv4N14rocblas_eorder21rocblas_eorder_blocksE) The computed eigenvalues will be grouped by split-off blocks and arranged in increasing order within each block.


-
enumerator rocblas_eorder_entire
[#](#_CPPv4N14rocblas_eorder21rocblas_eorder_entireE) All computed eigenvalues of the entire matrix will be ordered from smallest to largest.


-
enumerator rocblas_eorder_blocks

## rocblas_esort[#](#rocblas-esort)

## rocblas_layer_mode_flags[#](#rocblas-layer-mode-flags)

-
typedef uint32_t rocblas_layer_mode_flags
[#](#_CPPv424rocblas_layer_mode_flags) Used to specify the logging layer mode using a bitwise combination of rocblas_layer_mode values.


## rocsolver_rfinfo[#](#rocsolver-rfinfo)

-
typedef struct rocsolver_rfinfo_ *rocsolver_rfinfo
[#](#_CPPv416rocsolver_rfinfo) A handle to a structure containing matrix descriptors and metadata required to interact with rocSPARSE when using the rocSOLVER re-factorization functionality. It needs to be initialized with

[rocsolver_create_rfinfo](refact.html#rocsolver-functions_8h_1a1e7e4fe0fc97abeb4b270ac2f3bf3ab2)and destroyed with[rocsolver_destroy_rfinfo](refact.html#rocsolver-functions_8h_1ae44434a33640f28432ef23ed94860840).

## rocsolver_rfinfo_mode[#](#rocsolver-rfinfo-mode)

-
enum rocsolver_rfinfo_mode
[#](#_CPPv421rocsolver_rfinfo_mode) Used to specify the mode of the rfinfo struct required by the re-factorization functionality.

*Values:*-
enumerator rocsolver_rfinfo_mode_lu
[#](#_CPPv4N21rocsolver_rfinfo_mode24rocsolver_rfinfo_mode_luE) To work with LU factorization (for general sparse matrices). This is the default mode.


-
enumerator rocsolver_rfinfo_mode_cholesky
[#](#_CPPv4N21rocsolver_rfinfo_mode30rocsolver_rfinfo_mode_choleskyE) To work with Cholesky factorization (for symmetric positive definite sparse matrices).


-
enumerator rocsolver_rfinfo_mode_lu

## rocsolver_alg_mode[#](#rocsolver-alg-mode)

-
enum rocsolver_alg_mode
[#](#_CPPv418rocsolver_alg_mode) Used by specific functions to specify the algorithm mode.

*Values:*-
enumerator rocsolver_alg_mode_gpu
[#](#_CPPv4N18rocsolver_alg_mode22rocsolver_alg_mode_gpuE) Computations are all performed on the GPU. This is the default mode.


-
enumerator rocsolver_alg_mode_hybrid
[#](#_CPPv4N18rocsolver_alg_mode25rocsolver_alg_mode_hybridE) Computations are performed on the CPU and GPU.


-
enumerator rocsolver_alg_mode_mixed
[#](#_CPPv4N18rocsolver_alg_mode24rocsolver_alg_mode_mixedE) Nested functions use a mixture of hybrid and GPU-only modes.


-
enumerator rocsolver_alg_mode_gpu

## rocsolver_function[#](#rocsolver-function)

-
enum rocsolver_function
[#](#_CPPv418rocsolver_function) Used to specify a function with multiple supported algorithm modes.

*Values:*-
enumerator rocsolver_function_bdsqr
[#](#_CPPv4N18rocsolver_function24rocsolver_function_bdsqrE)

-
enumerator rocsolver_function_gesvd
[#](#_CPPv4N18rocsolver_function24rocsolver_function_gesvdE) Affected by bdsqr.


-
enumerator rocsolver_function_sterf
[#](#_CPPv4N18rocsolver_function24rocsolver_function_sterfE)

-
enumerator rocsolver_function_steqr
[#](#_CPPv4N18rocsolver_function24rocsolver_function_steqrE)

-
enumerator rocsolver_function_syev_heev
[#](#_CPPv4N18rocsolver_function28rocsolver_function_syev_heevE) Affected by sterf and steqr.


-
enumerator rocsolver_function_bdsqr
