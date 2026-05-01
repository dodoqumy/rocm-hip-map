---
title: "rocSOLVER refactorization and direct solvers &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/reference/refact.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:39.568875+00:00
content_hash: "2b0949282f3ba5cc"
---

# rocSOLVER refactorization and direct solvers[#](#rocsolver-refactorization-and-direct-solvers)

These functions implement direct solvers for sparse systems with different coefficient matrices that share the same sparsity pattern. The refactorization functions are divided into the following categories:

[Initialization and meta data](#rfinit): Basic functions to initialize and destroy meta data.[Triangular refactorization](#rfrefact): Refactorization of new matrices given a known sparsity pattern.[Direct sparse solvers](#rfsolver): Based on triangular refactorization.

Note

The API descriptions use the following notations:

`i`

,`j`

, and`k`

are used as general purpose indices. In some legacy LAPACK APIs,`k`

can be a parameter indicating some problem or matrix dimension.Depending on the context, when it is necessary to index rows, columns, and blocks or submatrices,

`i`

is assigned to rows,`j`

to columns, and`k`

to blocks.`l`

is always used to index matrices or problems in a batch.`x[i]`

stands for the i-th element of vector x, while`A[i,j]`

represents the element in the i-th row and j-th column of matrix`A`

. Indices are 1-based, for instance,`x[1]`

is the first element of`x`

.To identify a block in a matrix or a matrix in the batch,

`k`

and`l`

are used as sub-indices`x_i`

\(=x_i\). Both notations are used, \(x_i\) when displaying mathematical equations and`x_i`

in the text describing the function parameters.If

`X`

is a real vector or matrix, \(X^T\) indicates its transpose. If`X`

is complex, then \(X^H\) represents its conjugate transpose. When`X`

could be real or complex, the descriptions use`X'`

to indicate`X`

transposed or`X`

conjugate transposed, accordingly.When a matrix

`A`

is formed as the product of several matrices, the following notation is used:`A=M(1)M(2)...M(t)`

.

## Initialization and meta data[#](#initialization-and-meta-data)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_create_rfinfo([rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)*rfinfo,[rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle)[#](#_CPPv423rocsolver_create_rfinfoP16rocsolver_rfinfo14rocblas_handle) CREATE_RFINFO initializes the structure rfinfo that contains the meta data and descriptors of the involved matrices required by the re-factorization functions

[CSRRF_REFACTLU](#rocsolver-functions_8h_1a84c4539b95f2f76eae8e42c0d5e0ab9a)and[CSRRF_REFACTCHOL](#rocsolver-functions_8h_1ae2729f52382e1ee539a5542428e29e6d), and by the direct solver[CSRRF_SOLVE](#rocsolver-functions_8h_1a5122e171f18b91d64dbc13513a54e668).- Parameters:
**rfinfo**–**[out]**[rocsolver_rfinfo](types.html#rocsolver-extra-types_8h_1ac4dba41ced3c23c0f29e72dd7d53fd59). The pointer to the rfinfo struct to be initialized.**handle**–**[in]**rocblas_handle.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_destroy_rfinfo([rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv424rocsolver_destroy_rfinfo16rocsolver_rfinfo) DESTROY_RFINFO destroys the structure rfinfo used by the re-factorization functions

[CSRRF_REFACTLU](#rocsolver-functions_8h_1a84c4539b95f2f76eae8e42c0d5e0ab9a)and[CSRRF_REFACTCHOL](#rocsolver-functions_8h_1ae2729f52382e1ee539a5542428e29e6d), and by the direct solver[CSRRF_SOLVE](#rocsolver-functions_8h_1a5122e171f18b91d64dbc13513a54e668).- Parameters:
**rfinfo**–**[in]**[rocsolver_rfinfo](types.html#rocsolver-extra-types_8h_1ac4dba41ced3c23c0f29e72dd7d53fd59). The rfinfo struct to be destroyed.


-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_set_rfinfo_mode([rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo,[rocsolver_rfinfo_mode](types.html#_CPPv421rocsolver_rfinfo_mode)mode)[#](#_CPPv425rocsolver_set_rfinfo_mode16rocsolver_rfinfo21rocsolver_rfinfo_mode) SET_RFINFO_MODE sets the mode of the structure rfinfo required by the re-factorization functions

[CSRRF_REFACTLU](#rocsolver-functions_8h_1a84c4539b95f2f76eae8e42c0d5e0ab9a)and[CSRRF_REFACTCHOL](#rocsolver-functions_8h_1ae2729f52382e1ee539a5542428e29e6d), and by the direct solver[CSRRF_SOLVE](#rocsolver-functions_8h_1a5122e171f18b91d64dbc13513a54e668).- Parameters:
**rfinfo**–**[in]**[rocsolver_rfinfo](types.html#rocsolver-extra-types_8h_1ac4dba41ced3c23c0f29e72dd7d53fd59). The rfinfo struct to be set up.**mode**–**[in]**[rocsolver_rfinfo_mode](types.html#rocsolver-extra-types_8h_1a6225659a6a7253a51e6bfbeff65f5733). Use rocsolver_rfinfo_mode_cholesky when the Cholesky factorization is required.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_get_rfinfo_mode([rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo,[rocsolver_rfinfo_mode](types.html#_CPPv421rocsolver_rfinfo_mode)*mode)[#](#_CPPv425rocsolver_get_rfinfo_mode16rocsolver_rfinfoP21rocsolver_rfinfo_mode) GET_RFINFO_MODE gets the mode of the structure rfinfo required by the re-factorization functions

[CSRRF_REFACTLU](#rocsolver-functions_8h_1a84c4539b95f2f76eae8e42c0d5e0ab9a)and[CSRRF_REFACTCHOL](#rocsolver-functions_8h_1ae2729f52382e1ee539a5542428e29e6d), and by the direct solver[CSRRF_SOLVE](#rocsolver-functions_8h_1a5122e171f18b91d64dbc13513a54e668).- Parameters:
**rfinfo**–**[in]**[rocsolver_rfinfo](types.html#rocsolver-extra-types_8h_1ac4dba41ced3c23c0f29e72dd7d53fd59). The referenced rfinfo struct.**mode**–**[out]**[rocsolver_rfinfo_mode](types.html#rocsolver-extra-types_8h_1a6225659a6a7253a51e6bfbeff65f5733). The queried mode.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_dcsrrf_analysis([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nrhs, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzM,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrM,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indM, double *valM, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, double *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivP,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ, double *B, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)ldb,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv425rocsolver_dcsrrf_analysis14rocblas_handleK11rocblas_intK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPdK11rocblas_intP11rocblas_intP11rocblas_intPdP11rocblas_intP11rocblas_intPdK11rocblas_int16rocsolver_rfinfo)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_scsrrf_analysis([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nrhs, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzM,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrM,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indM, float *valM, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, float *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivP,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ, float *B, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)ldb,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv425rocsolver_scsrrf_analysis14rocblas_handleK11rocblas_intK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPfK11rocblas_intP11rocblas_intP11rocblas_intPfP11rocblas_intP11rocblas_intPfK11rocblas_int16rocsolver_rfinfo) CSRRF_ANALYSIS performs the analysis phase required by the re-factorization functions

[CSRRF_REFACTLU](#rocsolver-functions_8h_1a84c4539b95f2f76eae8e42c0d5e0ab9a)and[CSRRF_REFACTCHOL](#rocsolver-functions_8h_1ae2729f52382e1ee539a5542428e29e6d), and by the direct solver[CSRRF_SOLVE](#rocsolver-functions_8h_1a5122e171f18b91d64dbc13513a54e668).Consider a sparse matrix \(M\) previously factorized as

\[ Q^TMQ = L_ML_M^T \](Cholesky factorization for the symmetric positive definite case), or

\[ PMQ = L_MU_M \](LU factorization for the general case)

where \(L_M\) is lower triangular (with unit diagonal in the general case), \(U_M\) is upper triangular, and \(P\) and \(Q\) are permutation matrices associated with pivoting and re-ordering (to minimize fill-in), respectively. The meta data generated by this routine is collected in the output parameter rfinfo. This information will allow the fast re-factorization of another sparse matrix \(A\) as

\[ Q^TAQ = L_AL_A^T, \quad \text{or} \]\[ PAQ = L_AU_A, \]and, eventually, the computation of the solution vector \(X\) of any linear system of the form

\[ AX = B \]as long as \(A\) has the same sparsity pattern as the previous matrix \(M\).

This function supposes that the rfinfo struct has been initialized by

[RFINFO_CREATE](#rocsolver-functions_8h_1a1e7e4fe0fc97abeb4b270ac2f3bf3ab2). By default, rfinfo is set up to work with the LU factorization (general matrices). If the matrix is symmetric positive definite, and the Cholesky factorization is desired, then the corresponding mode must be manually set up by[SET_RFINFO_MODE](#rocsolver-functions_8h_1a0307df5be336f33630ecb3e4345cb5b4). This function does not automatically detect symmetry.For the LU factorization mode, the LU factors \(L_M\) and \(U_M\) must be passed in a bundle matrix \(T=(L_M-I)+U_M\) as returned by

[CSRRF_SUMLU](#rocsolver-functions_8h_1a743f72a89d342ed59866ebf078e08587). For the Cholesky mode, the lower triangular part of \(T\) must contain the Cholesky factor \(L_M\); the strictly upper triangular part of \(T\) will be ignored. Similarly, the strictly upper triangular part of \(M\) is ignored when working in Cholesky mode.Note

If only a re-factorization will be executed (i.e. no solver phase), then nrhs can be set to zero and B can be null.

- Parameters:
**handle**–**[in]**rocblas_handle.**n**–**[in]**rocblas_int. n >= 0. The number of rows (and columns) of matrix M.**nrhs**–**[in]**rocblas_int. nrhs >= 0. The number of right-hand-sides (columns of matrix B). Set nrhs to zero when only the re-factorization is needed.**nnzM**–**[in]**rocblas_int. nnzM >= 0. The number of non-zero elements in M.**ptrM**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indM and valM. The last element of ptrM is equal to nnzM.**indM**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzM. It contains the column indices of the non-zero elements of M. Indices are sorted by row and by column within each row.**valM**–**[in]**pointer to type. Array on the GPU of dimension nnzM. The values of the non-zero elements of M. The strictly upper triangular entries are not referenced when working in Cholesky mode.**nnzT**–**[in]**rocblas_int. nnzT >= 0. The number of non-zero elements in T.**ptrT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indT and valT. The last element of ptrT is equal to nnzT.**indT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzT. It contains the column indices of the non-zero elements of T. Indices are sorted by row and by column within each row.**valT**–**[in]**pointer to type. Array on the GPU of dimension nnzT. The values of the non-zero elements of T. The strictly upper triangular entries are not referenced when working in Cholesky mode.**pivP**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix P, i.e. the order in which the rows of matrix M were re-arranged. When working in Cholesky mode, this array is not referenced and can be null.**pivQ**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix Q, i.e. the order in which the columns of matrix M were re-arranged.**B**–**[in]**pointer to type. Array on the GPU of dimension ldb*nrhs. The right hand side matrix B. It can be null if only the re-factorization is needed.**ldb**–**[in]**rocblas_int. ldb >= n. The leading dimension of B.**rfinfo**–**[out]**rocsolver_rfinfo. Structure that holds the meta data generated in the analysis phase.



## Triangular refactorization[#](#triangular-refactorization)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_dcsrrf_sumlu([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indL, double *valL, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indU, double *valU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, double *valT)[#](#_CPPv422rocsolver_dcsrrf_sumlu14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPdK11rocblas_intP11rocblas_intP11rocblas_intPdP11rocblas_intP11rocblas_intPd)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_scsrrf_sumlu([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indL, float *valL, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indU, float *valU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, float *valT)[#](#_CPPv422rocsolver_scsrrf_sumlu14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPfK11rocblas_intP11rocblas_intP11rocblas_intPfP11rocblas_intP11rocblas_intPf) CSRRF_SUMLU bundles the factors \(L\) and \(U\), associated with the LU factorization of a sparse matrix \(A\), into a single sparse matrix \(T=(L-I)+U\).

Factor \(L\) is a sparse lower triangular matrix with unit diagonal elements, and \(U\) is a sparse upper triangular matrix. The resulting sparse matrix \(T\) combines both sparse factors without storing the unit diagonal; in other words, the number of non-zero elements of T, nnzT, is given by nnzT = nnzL - n + nnzU.

- Parameters:
**handle**–**[in]**rocblas_handle.**n**–**[in]**rocblas_int. n >= 0. The number of rows (and columns) of matrix A.**nnzL**–**[in]**rocblas_int. nnzL >= n. The number of non-zero elements in L.**ptrL**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indL and valL. The last element of ptrL is equal to nnzL.**indL**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzL. It contains the column indices of the non-zero elements of L. Indices are sorted by row and by column within each row.**valL**–**[in]**pointer to type. Array on the GPU of dimension nnzL. The values of the non-zero elements of L.**nnzU**–**[in]**rocblas_int. nnzU >= 0. The number of non-zero elements in U.**ptrU**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indU and valU. The last element of ptrU is equal to nnzU.**indU**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzU. It contains the column indices of the non-zero elements of U. Indices are sorted by row and by column within each row.**valU**–**[in]**pointer to type. Array on the GPU of dimension nnzU. The values of the non-zero elements of U.**ptrT**–**[out]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indT and valT. The last element of ptrT is equal to nnzT.**indT**–**[out]**pointer to rocblas_int. Array on the GPU of dimension nnzT. It contains the column indices of the non-zero elements of T. Indices are sorted by row and by column within each row.**valT**–**[out]**pointer to type. Array on the GPU of dimension nnzT. The values of the non-zero elements of T.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_dcsrrf_splitlu([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, double *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indL, double *valL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indU, double *valU)[#](#_CPPv424rocsolver_dcsrrf_splitlu14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPdP11rocblas_intP11rocblas_intPdP11rocblas_intP11rocblas_intPd)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_scsrrf_splitlu([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, float *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indL, float *valL,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrU,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indU, float *valU)[#](#_CPPv424rocsolver_scsrrf_splitlu14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPfP11rocblas_intP11rocblas_intPfP11rocblas_intP11rocblas_intPf) CSRRF_SPLITLU splits the factors \(L\) and \(U\), associated with the LU factorization of a sparse matrix \(A\), from a bundled matrix \(T=(L-I)+U\).

Factor \(L\) is a sparse lower triangular matrix with unit diagonal elements, and \(U\) is a sparse upper triangular matrix. Conceptually, on input, U is stored on the diagonal and upper part of \(T\), while the non diagonal elements of \(L\) are stored on the strictly lower part of \(T\).

- Parameters:
**handle**–**[in]**rocblas_handle.**n**–**[in]**rocblas_int. n >= 0. The number of rows (and columns) of matrix A.**nnzT**–**[in]**rocblas_int. nnzT >= 0. The number of non-zero elements in T.**ptrT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indT and valT. The last element of ptrT is equal to nnzT.**indT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzT. It contains the column indices of the non-zero elements of T. Indices are sorted by row and by column within each row.**valT**–**[in]**pointer to type. Array on the GPU of dimension nnzT. The values of the non-zero elements of T.**ptrL**–**[out]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indL and valL. The last element of ptrL is equal to nnzL.**indL**–**[out]**pointer to rocblas_int. Array on the GPU of dimension nnzL. It contains the column indices of the non-zero elements of L. Indices are sorted by row and by column within each row. (If nnzL is not known in advance, the size of this array could be set to nnzT + n as an upper bound).**valL**–**[out]**pointer to type. Array on the GPU of dimension nnzL. The values of the non-zero elements of L. (If nnzL is not known in advance, the size of this array could be set to nnzT + n as an upper bound).**ptrU**–**[out]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indU and valU. The last element of ptrU is equal to nnzU.**indU**–**[out]**pointer to rocblas_int. Array on the GPU of dimension nnzU. It contains the column indices of the non-zero elements of U. Indices are sorted by row and by column within each row. (If nnzU is not known in advance, the size of this array could be set to nnzT as an upper bound).**valU**–**[out]**pointer to type. Array on the GPU of dimension nnzU. The values of the non-zero elements of U. (If nnzU is not known in advance, the size of this array could be set to nnzT as an upper bound).



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_dcsrrf_refactlu([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indA, double *valA, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, double *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivP,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv425rocsolver_dcsrrf_refactlu14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPdK11rocblas_intP11rocblas_intP11rocblas_intPdP11rocblas_intP11rocblas_int16rocsolver_rfinfo)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_scsrrf_refactlu([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indA, float *valA, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, float *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivP,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv425rocsolver_scsrrf_refactlu14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPfK11rocblas_intP11rocblas_intP11rocblas_intPfP11rocblas_intP11rocblas_int16rocsolver_rfinfo) CSRRF_REFACTLU performs a fast LU factorization of a sparse matrix \(A\) based on the information from the factorization of a previous matrix \(M\) with the same sparsity pattern (re-factorization).

Consider a sparse matrix \(M\) previously factorized as

\[ PMQ = L_MU_M \]where \(L_M\) is lower triangular with unit diagonal, \(U_M\) is upper triangular, and \(P\) and \(Q\) are permutation matrices associated with pivoting and re-ordering (to minimize fill-in), respectively. If \(A\) has the same sparsity pattern as \(M\), then the re-factorization

\[ PAQ = L_AU_A \]can be computed numerically without a symbolic analysis phase.

This function supposes that rfinfo has been updated, by function

[CSRRF_ANALYSIS](#rocsolver-functions_8h_1a413d5dbb0fe4d02f9245beafead4e804), after the analysis phase of the previous matrix M and its initial factorization. Both functions, CSRRF_ANALYSIS and CSRRF_REFACTLU must be run with the same rfinfo mode (LU factorization, the default mode), otherwise the workflow will result in an error.- Parameters:
**handle**–**[in]**rocblas_handle.**n**–**[in]**rocblas_int. n >= 0. The number of rows (and columns) of matrix A.**nnzA**–**[in]**rocblas_int. nnzA >= 0. The number of non-zero elements in A.**ptrA**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indA and valA. The last element of ptrM is equal to nnzA.**indA**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzA. It contains the column indices of the non-zero elements of M. Indices are sorted by row and by column within each row.**valA**–**[in]**pointer to type. Array on the GPU of dimension nnzA. The values of the non-zero elements of A.**nnzT**–**[in]**rocblas_int. nnzT >= 0. The number of non-zero elements in T.**ptrT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indT and valT. The last element of ptrT is equal to nnzT.**indT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzT. It contains the column indices of the non-zero elements of T. Indices are sorted by row and by column within each row.**valT**–**[out]**pointer to type. Array on the GPU of dimension nnzT. The values of the non-zero elements of the new bundle matrix (L_A - I) + U_A.**pivP**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix P, i.e. the order in which the rows of matrix M were re-arranged.**pivQ**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix Q, i.e. the order in which the columns of matrix M were re-arranged.**rfinfo**–**[in]**rocsolver_rfinfo. Structure that holds the meta data generated in the analysis phase.



-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_dcsrrf_refactchol([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indA, double *valA, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, double *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv427rocsolver_dcsrrf_refactchol14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPdK11rocblas_intP11rocblas_intP11rocblas_intPdP11rocblas_int16rocsolver_rfinfo)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_scsrrf_refactchol([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrA,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indA, float *valA, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, float *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv427rocsolver_scsrrf_refactchol14rocblas_handleK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPfK11rocblas_intP11rocblas_intP11rocblas_intPfP11rocblas_int16rocsolver_rfinfo) CSRRF_REFACTCHOL performs a fast Cholesky factorization of a sparse symmetric positive definite matrix \(A\) based on the information from the factorization of a previous matrix \(M\) with the same sparsity pattern (re-factorization).

Consider a sparse matrix \(M\) previously factorized as

\[ Q^TMQ = L_ML_M^T \]where \(L_M\) is lower triangular, and \(Q\) is a permutation matrices associated with re-ordering to minimize fill-in. If \(A\) has the same sparsity pattern as \(M\), then the re-factorization

\[ Q^TAQ = L_AL_A^T \]can be computed numerically without a symbolic analysis phase.

This function supposes that rfinfo has been updated by function

[CSRRF_ANALYSIS](#rocsolver-functions_8h_1a413d5dbb0fe4d02f9245beafead4e804), after the analysis phase of the previous matrix M and its initial factorization. Both functions, CSRRF_ANALYSIS and CSRRF_REFACTCHOL must be run with the same rfinfo mode (Cholesky factorization), otherwise the workflow will result in an error.- Parameters:
**handle**–**[in]**rocblas_handle.**n**–**[in]**rocblas_int. n >= 0. The number of rows (and columns) of matrix A.**nnzA**–**[in]**rocblas_int. nnzA >= 0. The number of non-zero elements in A.**ptrA**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indA and valA. The last element of ptrM is equal to nnzA.**indA**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzA. It contains the column indices of the non-zero elements of M. Indices are sorted by row and by column within each row.**valA**–**[in]**pointer to type. Array on the GPU of dimension nnzA. The values of the non-zero elements of A. The strictly upper triangular entries are not referenced.**nnzT**–**[in]**rocblas_int. nnzT >= 0. The number of non-zero elements in T.**ptrT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indT and valT. The last element of ptrT is equal to nnzT.**indT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzT. It contains the column indices of the non-zero elements of T. Indices are sorted by row and by column within each row.**valT**–**[out]**pointer to type. Array on the GPU of dimension nnzT. The values of the non-zero elements of the new Cholesky factor L_A. The strictly upper triangular entries of this array are not referenced.**pivQ**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix Q, i.e. the order in which the columns of matrix M were re-arranged.**rfinfo**–**[in]**[rocsolver_rfinfo](types.html#rocsolver-extra-types_8h_1ac4dba41ced3c23c0f29e72dd7d53fd59). Structure that holds the meta data generated in the analysis phase.



## Direct sparse solvers[#](#direct-sparse-solvers)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_dcsrrf_solve([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nrhs, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, double *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivP,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ, double *B, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)ldb,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv422rocsolver_dcsrrf_solve14rocblas_handleK11rocblas_intK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPdP11rocblas_intP11rocblas_intPdK11rocblas_int16rocsolver_rfinfo)

-
[rocblas_status](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/enumerations.html#_CPPv414rocblas_status)rocsolver_scsrrf_solve([rocblas_handle](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv414rocblas_handle)handle, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)n, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nrhs, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)nnzT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*ptrT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*indT, float *valT,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivP,[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)*pivQ, float *B, const[rocblas_int](https://rocm.docs.amd.com/projects/rocBLAS/en/latest/reference/datatypes.html#_CPPv411rocblas_int)ldb,[rocsolver_rfinfo](types.html#_CPPv416rocsolver_rfinfo)rfinfo)[#](#_CPPv422rocsolver_scsrrf_solve14rocblas_handleK11rocblas_intK11rocblas_intK11rocblas_intP11rocblas_intP11rocblas_intPfP11rocblas_intP11rocblas_intPfK11rocblas_int16rocsolver_rfinfo) CSRRF_SOLVE solves a linear system with sparse coefficient matrix \(A\) in its factorized form.

The linear system is of the form

\[ AX = B \]where the sparse matrix \(A\) is factorized as

\[ Q^TAQ = L_AL_A^T \](Cholesky factorization for the symmetric positive definite case), or

\[ PAQ = L_AU_A \](LU factorization for the general case),

and \(B\) is a dense matrix of right hand sides.

This function supposes that rfinfo has been updated by function

[CSRRF_ANALYSIS](#rocsolver-functions_8h_1a413d5dbb0fe4d02f9245beafead4e804), after the analysis phase. Both functions, CSRRF_ANALYSIS and CSRRF_SOLVE must be run with the same rfinfo mode (LU or Cholesky factorization), otherwise the workflow will result in an error.For the LU factorization mode, the LU factors \(L_A\) and \(U_A\) must be passed in a bundle matrix \(T=(L_A-I)+U_A\) as returned by

[CSRRF_REFACTLU](#rocsolver-functions_8h_1a84c4539b95f2f76eae8e42c0d5e0ab9a)or[CSRRF_SUMLU](#rocsolver-functions_8h_1a743f72a89d342ed59866ebf078e08587). For the Cholesky mode, the lower triangular part of \(T\) must contain the Cholesky factor \(L_A\); the strictly upper triangular part of \(T\) will be ignored.- Parameters:
**handle**–**[in]**rocblas_handle.**n**–**[in]**rocblas_int. n >= 0. The number of rows (and columns) of matrix A.**nrhs**–**[in]**rocblas_int. nrhs >= 0. The number of right hand sides, i.e. the number of columns of matrix B.**nnzT**–**[in]**rocblas_int. nnzT >= 0. The number of non-zero elements in T.**ptrT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n+1. It contains the positions of the beginning of each row in indT and valT. The last element of ptrT is equal to nnzT.**indT**–**[in]**pointer to rocblas_int. Array on the GPU of dimension nnzT. It contains the column indices of the non-zero elements of T. Indices are sorted by row and by column within each row.**valT**–**[in]**pointer to type. Array on the GPU of dimension nnzT. The values of the non-zero elements of T. The strictly upper triangular entries are not referenced when working in Cholesky mode.**pivP**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix P, i.e. the order in which the rows of matrix A were re-arranged. When working in Cholesky mode, this array is not referenced and can be null.**pivQ**–**[in]**pointer to rocblas_int. Array on the GPU of dimension n. Contains the pivot indices representing the permutation matrix Q, i.e. the order in which the columns of matrix A were re-arranged.**B**–**[inout]**pointer to type. Array on the GPU of dimension ldb*nrhs. On entry the right hand side matrix B. On exit, the solution matrix X.**ldb**–**[in]**rocblas_int. ldb >= n. The leading dimension of B.**rfinfo**–**[in]**rocsolver_rfinfo. Structure that holds the meta data generated in the analysis phase.
