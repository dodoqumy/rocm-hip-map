---
title: "Tuning rocSOLVER performance &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/tuning.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:11:07.572561+00:00
content_hash: "fea19802d51a7130"
---

# Tuning rocSOLVER performance[#](#tuning-rocsolver-performance)

Some compile-time parameters in rocSOLVER can be modified to tune the performance of the library functions in a given context, such as for a particular matrix size or shape. A description of these tunable constants is presented in this section.

To facilitate the description, the constants are grouped by the family of functions they affect. Some aspects of the algorithms involved are also depicted here for the sake of clarity. However, this section is not intended to be a review of the well-known methods for different matrix computations. These constants are specific to the rocSOLVER implementation and are only described within that context.

All described constants can be found in `library/src/include/ideal_sizes.hpp`

.
These are not run-time arguments for the associated API functions. The library must be
[rebuilt from source](../installation/installlinux.html#linux-install-source) for any change to take effect.

Warning

The effect of changing a tunable constant on the performance of the library is difficult to predict and such analysis is beyond the scope of this document. Advanced users and developers tuning these values should proceed with caution. New values might (or might not) improve or worsen the performance of the associated functions.

## geqr2/geqrf and geql2/geqlf functions[#](#geqr2-geqrf-and-geql2-geqlf-functions)

The orthogonal factorizations from the left (QR or QL factorizations) are separated into two versions: blocked and unblocked. The unblocked routines GEQR2 and GEQL2 are based on BLAS Level 2 operations and work by applying Householder reflectors one column at a time. The blocked routines GEQRF and GEQLF factorize a block of columns at each step using the unblocked functions, provided the matrix is large enough, and apply the resulting block reflectors to update the rest of the matrix. The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which, in general, can give better performance on the GPU.

### GEQxF_BLOCKSIZE[#](#geqxf-blocksize)

-
GEQxF_BLOCKSIZE
[#](#c.GEQxF_BLOCKSIZE) Determines the size of the block column factorized at each step in the blocked QR or QL algorithm (GEQRF or GEQLF). It also applies to the corresponding batched and strided-batched routines.


### GEQxF_GEQx2_SWITCHSIZE[#](#geqxf-geqx2-switchsize)

-
GEQxF_GEQx2_SWITCHSIZE
[#](#c.GEQxF_GEQx2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing GEQRF or GEQLF. It also applies to the corresponding batched and strided-batched routines.

GEQRF or GEQLF will factorize blocks of GEQxF_BLOCKSIZE columns at a time until the rest of the matrix has no more than GEQxF_GEQx2_SWITCHSIZE rows or columns; at this point the last block, if any, will be factorized with the unblocked algorithm (GEQR2 or GEQL2).


Note

These constants have not been tuned for any specific cases.

## gerq2/gerqf and gelq2/gelqf functions[#](#gerq2-gerqf-and-gelq2-gelqf-functions)

The orthogonal factorizations from the right (RQ or LQ factorizations) are separated into two versions: blocked and unblocked. The unblocked routines GERQ2 and GELQ2 are based on BLAS Level 2 operations and work by applying Householder reflectors one row at a time. The blocked routines GERQF and GELQF factorize a block of rows at each step using the unblocked functions, provided the matrix is large enough, and apply the resulting block reflectors to update the rest of the matrix. The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which, in general, can give better performance on the GPU.

### GExQF_BLOCKSIZE[#](#gexqf-blocksize)

-
GExQF_BLOCKSIZE
[#](#c.GExQF_BLOCKSIZE) Determines the size of the block row factorized at each step in the blocked RQ or LQ algorithm (GERQF or GELQF). It also applies to the corresponding batched and strided-batched routines.


### GExQF_GExQ2_SWITCHSIZE[#](#gexqf-gexq2-switchsize)

-
GExQF_GExQ2_SWITCHSIZE
[#](#c.GExQF_GExQ2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing GERQF or GELQF. It also applies to the corresponding batched and strided-batched routines.

GERQF or GELQF will factorize blocks of GExQF_BLOCKSIZE rows at a time until the rest of the matrix has no more than GExQF_GExQ2_SWITCHSIZE rows or columns; at this point the last block, if any, will be factorized with the unblocked algorithm (GERQ2 or GELQ2).


Note

These constants have not been tuned for any specific cases.

## org2r/orgqr, org2l/orgql, ung2r/ungqr, and ung2l/ungql functions[#](#org2r-orgqr-org2l-orgql-ung2r-ungqr-and-ung2l-ungql-functions)

The generators of a matrix `Q`

with orthonormal columns (as products of Householder reflectors derived
from the QR or QL factorizations) are also separated into blocked and unblocked versions. The unblocked
routines ORG2R/UNG2R and ORG2L/UNG2L, based on BLAS Level 2 operations, work by accumulating one Householder reflector at a time.
The blocked routines ORGQR/UNGQR and ORGQL/UNGQL multiply a set of reflectors at each step using the unblocked
functions, provided there are enough reflectors to accumulate, and apply the resulting block reflector to update `Q`

.
The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which,
in general, can give better performance on the GPU.

### xxGQx_BLOCKSIZE[#](#xxgqx-blocksize)

-
xxGQx_BLOCKSIZE
[#](#c.xxGQx_BLOCKSIZE) Determines the size of the block reflector that is applied at each step when generating a matrix Q with orthonormal columns with the blocked algorithm (ORGQR/UNGQR or ORGQL/UNGQL).


### xxGQx_xxGQx2_SWITCHSIZE[#](#xxgqx-xxgqx2-switchsize)

-
xxGQx_xxGQx2_SWITCHSIZE
[#](#c.xxGQx_xxGQx2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing ORGQR/UNGQR or ORGQL/UNGQL.

ORGQR/UNGQR or ORGQL/UNGQL will accumulate xxGQx_BLOCKSIZE reflectors at a time until there are no more than xxGQx_xxGQx2_SWITCHSIZE reflectors left; the remaining reflectors, if any, are applied one by one using the unblocked algorithm (ORG2R/UNG2R or ORG2L/UNG2L).


Note

These constants have not been tuned for any specific cases.

## orgr2/orgrq, orgl2/orglq, ungr2/ungrq, and ungl2/unglq functions[#](#orgr2-orgrq-orgl2-orglq-ungr2-ungrq-and-ungl2-unglq-functions)

The generators of a matrix `Q`

with orthonormal rows (as products of Householder reflectors derived
from the RQ or LQ factorizations) are also separated into blocked and unblocked versions. The unblocked
routines ORGR2/UNGR2 and ORGL2/UNGL2, based on BLAS Level 2 operations, work by accumulating one Householder reflector at a time.
The blocked routines ORGRQ/UNGRQ and ORGLQ/UNGLQ multiply a set of reflectors at each step using the unblocked
functions, provided there are enough reflectors to accumulate, and apply the resulting block reflector to update `Q`

.
The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which,
in general, can give better performance on the GPU.

### xxGxQ_BLOCKSIZE[#](#xxgxq-blocksize)

-
xxGxQ_BLOCKSIZE
[#](#c.xxGxQ_BLOCKSIZE) Determines the size of the block reflector that is applied at each step when generating a matrix Q with orthonormal rows with the blocked algorithm (ORGRQ/UNGRQ or ORGLQ/UNGLQ).


### xxGxQ_xxGxQ2_SWITCHSIZE[#](#xxgxq-xxgxq2-switchsize)

-
xxGxQ_xxGxQ2_SWITCHSIZE
[#](#c.xxGxQ_xxGxQ2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing ORGRQ/UNGRQ or ORGLQ/UNGLQ.

ORGRQ/UNGRQ or ORGLQ/UNGLQ will accumulate xxGxQ_BLOCKSIZE reflectors at a time until there are no more than xxGxQ_xxGxQ2_SWITCHSIZE reflectors left; the remaining reflectors, if any, are applied one by one using the unblocked algorithm (ORGR2/UNGR2 or ORGL2/UNGL2).


Note

These constants have not been tuned for any specific cases.

## orm2r/ormqr, orm2l/ormql, unm2r/unmqr, and unm2l/unmql functions[#](#orm2r-ormqr-orm2l-ormql-unm2r-unmqr-and-unm2l-unmql-functions)

As with the generators of orthonormal or unitary matrices, the routines to multiply a general
matrix `C`

by a matrix `Q`

with orthonormal columns are separated into blocked and unblocked versions.
The unblocked routines ORM2R/UNM2R and ORM2L/UNM2L, based on BLAS Level 2 operations, work by multiplying one Householder
reflector at a time, while the blocked routines ORMQR/UNMQR and ORMQL/UNMQL apply a set of reflectors at each step,
provided there are enough reflectors to start with.
The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which,
in general, can give better performance on the GPU.

### xxMQx_BLOCKSIZE[#](#xxmqx-blocksize)

-
xxMQx_BLOCKSIZE
[#](#c.xxMQx_BLOCKSIZE) Determines the size of the block reflector that multiplies the matrix C at each step with the blocked algorithm (ORMQR/UNMQR or ORMQL/UNMQL).

xxMQx_BLOCKSIZE also acts as a switch size; if the total number of reflectors is not greater than xxMQx_BLOCKSIZE (k <= xxMQx_BLOCKSIZE), ORMQR/UNMQR or ORMQL/UNMQL will directly call the unblocked routines (ORM2R/UNM2R or ORM2L/UNM2L). However, when k is not a multiple of xxMQx_BLOCKSIZE, the last block that updates C in the blocked process is allowed to be smaller than xxMQx_BLOCKSIZE.


Note

This constant has not been tuned for any specific cases

## ormr2/ormrq, orml2/ormlq, unmr2/unmrq, and unml2/unmlq functions[#](#ormr2-ormrq-orml2-ormlq-unmr2-unmrq-and-unml2-unmlq-functions)

As with the generators of orthonormal or unitary matrices, the routines to multiply a general
matrix `C`

by a matrix `Q`

with orthonormal rows are separated into blocked and unblocked versions.
The unblocked routines ORMR2/UNMR2 and ORML2/UNML2, based on BLAS Level 2 operations, work by multiplying one Householder
reflector at a time, while the blocked routines ORMRQ/UNMRQ and ORMLQ/UNMLQ apply a set of reflectors at each step,
provided there are enough reflectors to start with.
The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which,
in general, can give better performance on the GPU.

### xxMxQ_BLOCKSIZE[#](#xxmxq-blocksize)

-
xxMxQ_BLOCKSIZE
[#](#c.xxMxQ_BLOCKSIZE) Determines the size of the block reflector that multiplies the matrix C at each step with the blocked algorithm (ORMRQ/UNMRQ or ORMLQ/UNMLQ).

xxMxQ_BLOCKSIZE also acts as a switch size; if the total number of reflectors is not greater than xxMxQ_BLOCKSIZE (k <= xxMxQ_BLOCKSIZE), ORMRQ/UNMRQ or ORMLQ/UNMLQ will directly call the unblocked routines (ORMR2/UNMR2 or ORML2/UNML2). However, when k is not a multiple of xxMxQ_BLOCKSIZE, the last block that updates C in the blocked process is allowed to be smaller than xxMxQ_BLOCKSIZE.


Note

This constant has not been tuned for any specific cases

## gebd2/gebrd and labrd functions[#](#gebd2-gebrd-and-labrd-functions)

The computation of the bidiagonal form of a matrix is separated into blocked and unblocked versions. The unblocked routine GEBD2 (and the auxiliary LABRD), based on BLAS Level 2 operations, apply Householder reflections to one column and row at a time. The blocked routine GEBRD reduces a leading block of rows and columns at each step using the unblocked function LABRD, provided the matrix is large enough, and applies the resulting block reflectors to update the trailing submatrix. The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which, in general, can give better performance on the GPU.

### GEBRD_BLOCKSIZE[#](#gebrd-blocksize)

-
GEBRD_BLOCKSIZE
[#](#c.GEBRD_BLOCKSIZE) Determines the size of the leading block that is reduced to bidiagonal form at each step when using the blocked algorithm (GEBRD). It also applies to the corresponding batched and strided-batched routines.


### GEBRD_GEBD2_SWITCHSIZE[#](#gebrd-gebd2-switchsize)

-
GEBRD_GEBD2_SWITCHSIZE
[#](#c.GEBRD_GEBD2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing GEBRD. It also applies to the corresponding batched and strided-batched routines.

GEBRD will use LABRD to reduce blocks of GEBRD_BLOCKSIZE rows and columns at a time until the trailing submatrix has no more than GEBRD_GEBD2_SWITCHSIZE rows or columns; at this point the last block, if any, will be reduced with the unblocked algorithm (GEBD2).


Note

These constants have not been tuned for any specific cases.

## bdsqr function[#](#bdsqr-function)

The singular value decomposition (SVD) of a bidiagonal matrix can be executed with one or multiple thread blocks. It is a blocking API that requires synchronization with the host.

### BDSQR_SWITCH_SIZE[#](#bdsqr-switch-size)

-
BDSQR_SWITCH_SIZE
[#](#c.BDSQR_SWITCH_SIZE) Determines the size at which rocSOLVER switches from updating singular vectors in a single thread group, to using multiple thread groups. It also applies to the corresponding batched and strided-batched routines.

When nv, nu, and nc are less than or equal to BDSQR_SWITCH_SIZE, BDSQR will update the singular vectors in a single thread group. Otherwise, BDSQR will launch a dedicated kernel with multiple thread groups.


### BDSQR_ITERS_PER_SYNC[#](#bdsqr-iters-per-sync)

-
BDSQR_ITERS_PER_SYNC
[#](#c.BDSQR_ITERS_PER_SYNC) Determines the number of iterations that BDSQR will execute between device synchronizations in the multi-kernel algorithm.

BDSQR will run an inner loop BDSQR_ITERS_PER_SYNC at a time, before synchronizing with the device to check if the stopping criterion has been met.


Note

These constants have not been tuned for any specific cases.

## gesvd function[#](#gesvd-function)

The singular value decomposition of a matrix `A`

can be sped up for matrices with sufficiently many more rows than
columns (or columns than rows) by starting with a QR factorization (or LQ factorization) of `A`

and working with the
triangular factor afterwards.

### THIN_SVD_SWITCH[#](#thin-svd-switch)

-
THIN_SVD_SWITCH
[#](#c.THIN_SVD_SWITCH) Determines the factor by which one dimension of a matrix should exceed the other dimension for the thin SVD to be computed when executing GESVD. It also applies to the corresponding batched and strided-batched routines.

When a m-by-n matrix A is passed to GESVD, if m >= THIN_SVD_SWITCH*n or n >= THIN_SVD_SWITCH*m, then the thin SVD is computed.


Note

This constant has not been tuned for any specific cases

## sytd2/sytrd, hetd2/hetrd, and latrd functions[#](#sytd2-sytrd-hetd2-hetrd-and-latrd-functions)

The computation of the tridiagonal form of a symmetric or Hermitian matrix is separated into blocked and unblocked versions. The unblocked routines SYTD2/HETD2 (and the auxiliary LATRD), based on BLAS Level 2 operations, apply Householder reflections to one column or row at a time. The blocked routine SYTRD reduces a block of rows and columns at each step using the unblocked function LATRD, provided the matrix is large enough, and applies the resulting block reflector to update the rest of the matrix. The application of the block reflectors is based on matrix-matrix operations (BLAS Level 3), which, in general, can give better performance on the GPU.

### xxTRD_BLOCKSIZE[#](#xxtrd-blocksize)

-
xxTRD_BLOCKSIZE
[#](#c.xxTRD_BLOCKSIZE) Determines the size of the leading block that is reduced to tridiagonal form at each step when using the blocked algorithm (SYTRD/HETRD). It also applies to the corresponding batched and strided-batched routines.


### xxTRD_xxTD2_SWITCHSIZE[#](#xxtrd-xxtd2-switchsize)

-
xxTRD_xxTD2_SWITCHSIZE
[#](#c.xxTRD_xxTD2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing SYTRD/HETRD. It also applies to the corresponding batched and strided-batched routines.

SYTRD/HETRD will use LATRD to reduce blocks of xxTRD_BLOCKSIZE rows and columns at a time until the rest of the matrix has no more than xxTRD_xxTD2_SWITCHSIZE rows or columns; at this point the last block, if any, will be reduced with the unblocked algorithm (SYTD2/HETD2).


Note

These constants have not been tuned for any specific cases.

## sygs2/sygst and hegs2/hegst functions[#](#sygs2-sygst-and-hegs2-hegst-functions)

The reduction of a symmetric or Hermitian-definite generalized eigenproblem to standard form is separated into
blocked and unblocked versions. The unblocked routines SYGS2/HEGS2 reduce the matrix `A`

one column or row at a time with vector operations and rank-2 updates (BLAS Level 2). The blocked
routines SYGST/HEGST reduce a leading block of `A`

at each step using the unblocked methods, provided `A`

is large enough,
and update the trailing matrix with BLAS Level 3 operations (matrix products
and rank-2k updates), which, in general, can give better performance on the GPU.

### xxGST_BLOCKSIZE[#](#xxgst-blocksize)

-
xxGST_BLOCKSIZE
[#](#c.xxGST_BLOCKSIZE) Determines the size of the leading block that is reduced to standard form at each step when using the blocked algorithm (SYGST/HEGST). It also applies to the corresponding batched and strided-batched routines.

xxGST_BLOCKSIZE also acts as a switch size; if the original size of the problem is not larger than xxGST_BLOCKSIZE (n <= xxGST_BLOCKSIZE), SYGST/HEGST will directly call the unblocked routines (SYGS2/HEGS2). However, when n is not a multiple of xxGST_BLOCKSIZE, the last block reduced in the blocked process is allowed to be smaller than xxGST_BLOCKSIZE.


Note

This constant has not been tuned for any specific cases

## syevd, heevd, and stedc functions[#](#syevd-heevd-and-stedc-functions)

When running SYEVD/HEEVD (or the corresponding batched and strided-batched routines), the computation of the eigenvectors of the associated tridiagonal matrix can be sped up using a divide-and-conquer approach (implemented in STEDC), provided the size of the independent block is large enough.

### STEDC_MIN_DC_SIZE[#](#stedc-min-dc-size)

-
STEDC_MIN_DC_SIZE
[#](#c.STEDC_MIN_DC_SIZE) Determines the minimum size required for the eigenvectors of an independent block of a tridiagonal matrix to be computed using the divide-and-conquer algorithm (STEDC).

If the size of the block is smaller than STEDC_MIN_DC_SIZE (bs < STEDC_MIN_DC_SIZE), the eigenvectors are computed with the normal QR algorithm.


### STEDC_NUM_SPLIT_BLKS[#](#stedc-num-split-blks)

-
STEDC_NUM_SPLIT_BLKS
[#](#c.STEDC_NUM_SPLIT_BLKS) Determines the number of split blocks (independent blocks) of a tridiagonal matrix that are analyzed in parallel with the divide & conquer method.


Note

These constants have not been tuned for any specific cases.

## syevj, heevj, syevdj, and heevdj functions[#](#syevj-heevj-syevdj-and-heevdj-functions)

The Jacobi eigensolver routines SYEVJ/HEEVJ (or the corresponding batched and strided-batched routines) can be executed with a single kernel call (for small-size matrices) or with multiple kernel calls (for large-size matrices). In the former case, the matrix is considered unblocked, Jacobi rotations are applied directly using the computed cosine and sine values, and the number of iterations or sweeps is controlled on the GPU. In the latter case, the matrix is partitioned into blocks, Jacobi rotations are accumulated per block to be applied in separate kernel calls, and the number of iterations or sweeps is controlled by the CPU, requiring synchronization of the handle stream.

When running SYEVDJ/HEEVDJ (or the corresponding batched and strided-batched routines), the computation of the eigenvectors of the associated tridiagonal matrix can be sped up using a divide-and-conquer approach, provided the size of the independent block is large enough.

### SYEVJ_BLOCKED_SWITCH[#](#syevj-blocked-switch)

-
SYEVJ_BLOCKED_SWITCH
[#](#c.SYEVJ_BLOCKED_SWITCH) Determines the size at which rocSOLVER switches from the small-size kernel to the blocked algorithm when executing SYEVJ. It also applies to the corresponding batched and strided-batched routines. Must be <= 64.

If the size of the matrix is not greater than SYEVJ_BLOCKED_SWITCH, the eigenvalues and eigenvectors will be computed with a single kernel call.


### SYEVDJ_MIN_DC_SIZE[#](#syevdj-min-dc-size)

-
SYEVDJ_MIN_DC_SIZE
[#](#c.SYEVDJ_MIN_DC_SIZE) Determines the minimum size required for the Jacobi divide and conquer to be used.

If the size of the block is smaller than SYEVDJ_MIN_DC_SIZE, the eigenvectors are computed with the normal Jacobi algorithm.


Note

These constants have not been tuned for any specific cases.

## potf2/potrf functions[#](#potf2-potrf-functions)

The Cholesky factorization is separated into blocked (right-looking) and unblocked versions. The unblocked routine POTF2, based on BLAS Level 2 operations, computes one diagonal element at a time and scales the corresponding row/column. The blocked routine POTRF factorizes a leading block of rows/columns at each step using the unblocked algorithm, provided the matrix is large enough, and updates the trailing matrix with BLAS Level 3 operations (symmetric rank-k updates), which, in general, can give better performance on the GPU.

### POTRF_BLOCKSIZE[#](#potrf-blocksize)

-
POTRF_BLOCKSIZE(T)
[#](#c.POTRF_BLOCKSIZE) Determines the size of the leading block that is factorized at each step when using the blocked algorithm (POTRF). It also applies to the corresponding batched and strided-batched routines.


### POTRF_POTF2_SWITCHSIZE[#](#potrf-potf2-switchsize)

-
POTRF_POTF2_SWITCHSIZE(T)
[#](#c.POTRF_POTF2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing POTRF. It also applies to the corresponding batched and strided-batched routines.

POTRF will factorize blocks of POTRF_BLOCKSIZE columns at a time until the rest of the matrix has no more than POTRF_POTF2_SWITCHSIZE columns; at this point the last block, if any, will be factorized with the unblocked algorithm (POTF2).


Note

These constants have not been tuned for any specific cases.

## sytf2/sytrf and lasyf functions[#](#sytf2-sytrf-and-lasyf-functions)

The Bunch-Kaufman factorization is separated into blocked and unblocked versions. The unblocked routine SYTF2 generates one 1-by-1 or 2-by-2 diagonal block at a time and applies a rank-1 update. The blocked routine SYTRF executes a partial factorization of a given maximum number of diagonal elements (LASYF) at each step, provided the matrix is large enough, and updates the rest of the matrix with matrix-matrix operations (BLAS Level 3), which, in general, can give better performance on the GPU.

### SYTRF_BLOCKSIZE[#](#sytrf-blocksize)

-
SYTRF_BLOCKSIZE
[#](#c.SYTRF_BLOCKSIZE) Determines the maximum size of the partial factorization executed at each step when using the blocked algorithm (SYTRF). It also applies to the corresponding batched and strided-batched routines.


### SYTRF_SYTF2_SWITCHSIZE[#](#sytrf-sytf2-switchsize)

-
SYTRF_SYTF2_SWITCHSIZE
[#](#c.SYTRF_SYTF2_SWITCHSIZE) Determines the size at which rocSOLVER switches from the unblocked to the blocked algorithm when executing SYTRF. It also applies to the corresponding batched and strided-batched routines.

SYTRF will use LASYF to factorize a submatrix of at most SYTRF_BLOCKSIZE columns at a time until the rest of the matrix has no more than SYTRF_SYTF2_SWITCHSIZE columns; at this point the last block, if any, will be factorized with the unblocked algorithm (SYTF2).


Note

These constants have not been tuned for any specific cases.
