---
title: "Using the rocSOLVER library &#8212; rocSOLVER 3.32.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/howto/using.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:10:47.754128+00:00
content_hash: "06df01b8deeecbaa"
---

# Using the rocSOLVER library[#](#using-the-rocsolver-library)

After rocSOLVER is installed, it can be used like any other library with a C API. To use rocSOLVER, include the header file in the user code. This means that the rocBLAS and rocSOLVER shared libraries become link-time and runtime dependencies for the user application.

Here are some examples that show how to use the rocSOLVER and rocSOLVER batched APIs.

## QR factorization of a single matrix[#](#qr-factorization-of-a-single-matrix)

The following code snippet uses rocSOLVER to compute the QR factorization of a general m-by-n real matrix in double precision.
For a full description of the rocSOLVER routine shown here, see the API documentation for [rocsolver_dgeqrf()](../reference/lapack.html#geqrf).

```
#include <hip/hip_runtime_api.h> // for hip functions
#include <rocsolver/rocsolver.h> // for all the rocsolver C interfaces and type declarations
#include <stdio.h> // for printf
#include <stdlib.h> // for malloc
// Example: Compute the QR Factorization of a matrix on the GPU
double *create_example_matrix(rocblas_int *M_out,
rocblas_int *N_out,
rocblas_int *lda_out) {
// a *very* small example input; not a very efficient use of the API
const double A[3][3] = { { 12, -51, 4},
{ 6, 167, -68},
{ -4, 24, -41} };
const rocblas_int M = 3;
const rocblas_int N = 3;
const rocblas_int lda = 3;
*M_out = M;
*N_out = N;
*lda_out = lda;
// note: rocsolver matrices must be stored in column major format,
// i.e. entry (i,j) should be accessed by hA[i + j*lda]
double *hA = (double*)malloc(sizeof(double)*lda*N);
for (size_t i = 0; i < M; ++i) {
for (size_t j = 0; j < N; ++j) {
// copy A (2D array) into hA (1D array, column-major)
hA[i + j*lda] = A[i][j];
}
}
return hA;
}
// We use rocsolver_dgeqrf to factor a real M-by-N matrix, A.
// See https://rocm.docs.amd.com/projects/rocSOLVER/en/latest/api/lapack.html#rocsolver-type-geqrf
int main() {
rocblas_int M; // rows
rocblas_int N; // cols
rocblas_int lda; // leading dimension
double *hA = create_example_matrix(&M, &N, &lda); // input matrix on CPU
// let's print the input matrix, just to see it
printf("A = [\n");
for (size_t i = 0; i < M; ++i) {
printf(" ");
for (size_t j = 0; j < N; ++j) {
printf("% .3f ", hA[i + j*lda]);
}
printf(";\n");
}
printf("]\n");
// initialization
rocblas_handle handle;
rocblas_create_handle(&handle);
// Some rocsolver functions may trigger rocblas to load its GEMM kernels.
// You can preload the kernels by explicitly invoking rocblas_initialize
// (e.g., to exclude one-time initialization overhead from benchmarking).
// preload rocBLAS GEMM kernels (optional)
// rocblas_initialize();
// calculate the sizes of our arrays
size_t size_A = lda * (size_t)N; // count of elements in matrix A
size_t size_piv = (M < N) ? M : N; // count of Householder scalars
// allocate memory on GPU
double *dA, *dIpiv;
hipMalloc((void**)&dA, sizeof(double)*size_A);
hipMalloc((void**)&dIpiv, sizeof(double)*size_piv);
// copy data to GPU
hipMemcpy(dA, hA, sizeof(double)*size_A, hipMemcpyHostToDevice);
// compute the QR factorization on the GPU
rocsolver_dgeqrf(handle, M, N, dA, lda, dIpiv);
// copy the results back to CPU
double *hIpiv = (double*)malloc(sizeof(double)*size_piv); // householder scalars on CPU
hipMemcpy(hA, dA, sizeof(double)*size_A, hipMemcpyDeviceToHost);
hipMemcpy(hIpiv, dIpiv, sizeof(double)*size_piv, hipMemcpyDeviceToHost);
// the results are now in hA and hIpiv
// we can print some of the results if we want to see them
printf("R = [\n");
for (size_t i = 0; i < M; ++i) {
printf(" ");
for (size_t j = 0; j < N; ++j) {
printf("% .3f ", (i <= j) ? hA[i + j*lda] : 0);
}
printf(";\n");
}
printf("]\n");
// clean up
free(hIpiv);
hipFree(dA);
hipFree(dIpiv);
free(hA);
rocblas_destroy_handle(handle);
}
```

The exact command required to compile the example above might vary depending on the system environment, but here is a typical example:

```
-I/opt/rocm/include -c example.c
/opt/rocm/bin/hipcc -o example -L/opt/rocm/lib -lrocsolver -lrocblas example.o
```

## QR factorization of a batch of matrices[#](#qr-factorization-of-a-batch-of-matrices)

One advantage of using GPUs is the ability to execute many operations of the same type in parallel on different data sets.
Based on this idea, rocSOLVER and rocBLAS provide a `batch`

version for most routines. These batch versions let you execute
the same operation on a set of different matrices, vectors, or both with a single library call.

### Strided_batched version[#](#strided-batched-version)

The following code snippet uses rocSOLVER to compute the QR factorization of a series of general m-by-n real matrices in double precision.
The matrices must be stored in contiguous memory locations on the GPU and accessed by a pointer to the first matrix and a
stride value that gives the separation between one matrix and the next, as shown in this example.
For a full description of the rocSOLVER routine that is used here, see the API documentation for [rocsolver_dgeqrf_strided_batched()](../reference/lapack.html#geqrf-strided-batched).

```
#include <hip/hip_runtime_api.h> // for hip functions
#include <rocsolver/rocsolver.h> // for all the rocsolver C interfaces and type declarations
#include <stdio.h> // for printf
#include <stdlib.h> // for malloc
// Example: Compute the QR Factorizations of an array of matrices on the GPU
double *create_example_matrices(rocblas_int *M_out,
rocblas_int *N_out,
rocblas_int *lda_out,
rocblas_stride *strideA_out,
rocblas_int *batch_count_out) {
const double A[2][3][3] = {
// First input matrix
{ { 12, -51, 4},
{ 6, 167, -68},
{ -4, 24, -41} },
// Second input matrix
{ { 3, -12, 11},
{ 4, -46, -2},
{ 0, 5, 15} } };
const rocblas_int M = 3;
const rocblas_int N = 3;
const rocblas_int lda = 3;
const rocblas_stride strideA = lda * N;
const rocblas_int batch_count = 2;
*M_out = M;
*N_out = N;
*lda_out = lda;
*strideA_out = strideA;
*batch_count_out = batch_count;
// allocate space for input matrix data on CPU
double *hA = (double*)malloc(sizeof(double)*strideA*batch_count);
// copy A (3D array) into hA (1D array, column-major)
for (size_t b = 0; b < batch_count; ++b)
for (size_t i = 0; i < M; ++i)
for (size_t j = 0; j < N; ++j)
hA[i + j*lda + b*strideA] = A[b][i][j];
return hA;
}
// Use rocsolver_dgeqrf_strided_batched to factor an array of real M-by-N matrices.
int main() {
rocblas_int M; // rows
rocblas_int N; // cols
rocblas_int lda; // leading dimension
rocblas_stride strideA; // stride from start of one matrix to the next
rocblas_int batch_count; // number of matricies
double *hA = create_example_matrices(&M, &N, &lda, &strideA, &batch_count);
// print the input matrices
for (size_t b = 0; b < batch_count; ++b) {
printf("A[%zu] = [\n", b);
for (size_t i = 0; i < M; ++i) {
printf(" ");
for (size_t j = 0; j < N; ++j) {
printf("% 4.f ", hA[i + j*lda + strideA*b]);
}
printf(";\n");
}
printf("]\n");
}
// initialization
rocblas_handle handle;
rocblas_create_handle(&handle);
// preload rocBLAS GEMM kernels (optional)
// rocblas_initialize();
// calculate the sizes of our arrays
size_t size_A = strideA * (size_t)batch_count; // elements in array for matrices
rocblas_stride strideP = (M < N) ? M : N; // stride of Householder scalar sets
size_t size_piv = strideP * (size_t)batch_count; // elements in array for Householder scalars
// allocate memory on GPU
double *dA, *dIpiv;
hipMalloc((void**)&dA, sizeof(double)*size_A);
hipMalloc((void**)&dIpiv, sizeof(double)*size_piv);
// copy data to GPU
hipMemcpy(dA, hA, sizeof(double)*size_A, hipMemcpyHostToDevice);
// compute the QR factorizations on the GPU
rocsolver_dgeqrf_strided_batched(handle, M, N, dA, lda, strideA, dIpiv, strideP, batch_count);
// copy the results back to CPU
double *hIpiv = (double*)malloc(sizeof(double)*size_piv); // householder scalars on CPU
hipMemcpy(hA, dA, sizeof(double)*size_A, hipMemcpyDeviceToHost);
hipMemcpy(hIpiv, dIpiv, sizeof(double)*size_piv, hipMemcpyDeviceToHost);
// the results are now in hA and hIpiv
// print some of the results
for (size_t b = 0; b < batch_count; ++b) {
printf("R[%zu] = [\n", b);
for (size_t i = 0; i < M; ++i) {
printf(" ");
for (size_t j = 0; j < N; ++j) {
printf("% 4.f ", (i <= j) ? hA[i + j*lda + strideA*b] : 0);
}
printf(";\n");
}
printf("]\n");
}
// clean up
free(hIpiv);
hipFree(dA);
hipFree(dIpiv);
free(hA);
rocblas_destroy_handle(handle);
}
```

### Batched version[#](#batched-version)

The following code snippet uses rocSOLVER to compute the QR factorization of a series of general m-by-n real matrices in double precision.
In this case, the matrices do not need to be in contiguous memory locations on the GPU and can be accessed by an array of pointers.
For a full description of this rocSOLVER routine, see the API documentation for [rocsolver_dgeqrf_batched](../reference/lapack.html#geqrf-batched).

```
#include <hip/hip_runtime_api.h> // for hip functions
#include <rocsolver/rocsolver.h> // for all the rocsolver C interfaces and type declarations
#include <stdio.h> // for printf
#include <stdlib.h> // for malloc
// Example: Compute the QR Factorizations of a batch of matrices on the GPU
double **create_example_matrices(rocblas_int *M_out,
rocblas_int *N_out,
rocblas_int *lda_out,
rocblas_int *batch_count_out) {
// a small example input
const double A[2][3][3] = {
// First input matrix
{ { 12, -51, 4},
{ 6, 167, -68},
{ -4, 24, -41} },
// Second input matrix
{ { 3, -12, 11},
{ 4, -46, -2},
{ 0, 5, 15} } };
const rocblas_int M = 3;
const rocblas_int N = 3;
const rocblas_int lda = 3;
const rocblas_int batch_count = 2;
*M_out = M;
*N_out = N;
*lda_out = lda;
*batch_count_out = batch_count;
// allocate space for input matrix data on CPU
double **hA = (double**)malloc(sizeof(double*)*batch_count);
hA[0] = (double*)malloc(sizeof(double)*lda*N);
hA[1] = (double*)malloc(sizeof(double)*lda*N);
for (size_t b = 0; b < batch_count; ++b)
for (size_t i = 0; i < M; ++i)
for (size_t j = 0; j < N; ++j)
hA[b][i + j*lda] = A[b][i][j];
return hA;
}
// Use rocsolver_dgeqrf_batched to factor a batch of real M-by-N matrices.
int main() {
rocblas_int M; // rows
rocblas_int N; // cols
rocblas_int lda; // leading dimension
rocblas_int batch_count; // number of matricies
double **hA = create_example_matrices(&M, &N, &lda, &batch_count);
// print the input matrices
for (size_t b = 0; b < batch_count; ++b) {
printf("A[%zu] = [\n", b);
for (size_t i = 0; i < M; ++i) {
printf(" ");
for (size_t j = 0; j < N; ++j) {
printf("% 4.f ", hA[b][i + j*lda]);
}
printf(";\n");
}
printf("]\n");
}
// initialization
rocblas_handle handle;
rocblas_create_handle(&handle);
// preload rocBLAS GEMM kernels (optional)
// rocblas_initialize();
// calculate the sizes of the arrays
size_t size_A = lda * (size_t)N; // count of elements in each matrix A
rocblas_stride strideP = (M < N) ? M : N; // stride of Householder scalar sets
size_t size_piv = strideP * (size_t)batch_count; // elements in array for Householder scalars
// allocate memory on the CPU for an array of pointers,
// then allocate memory for each matrix on the GPU.
double **A = (double**)malloc(sizeof(double*)*batch_count);
for (rocblas_int b = 0; b < batch_count; ++b)
hipMalloc((void**)&A[b], sizeof(double)*size_A);
// allocate memory on GPU for the array of pointers and Householder scalars
double **dA, *dIpiv;
hipMalloc((void**)&dA, sizeof(double*)*batch_count);
hipMalloc((void**)&dIpiv, sizeof(double)*size_piv);
// copy each matrix to the GPU
for (rocblas_int b = 0; b < batch_count; ++b)
hipMemcpy(A[b], hA[b], sizeof(double)*size_A, hipMemcpyHostToDevice);
// copy the array of pointers to the GPU
hipMemcpy(dA, A, sizeof(double*)*batch_count, hipMemcpyHostToDevice);
// compute the QR factorizations on the GPU
rocsolver_dgeqrf_batched(handle, M, N, dA, lda, dIpiv, strideP, batch_count);
// copy the results back to CPU
double *hIpiv = (double*)malloc(sizeof(double)*size_piv); // householder scalars on CPU
hipMemcpy(hIpiv, dIpiv, sizeof(double)*size_piv, hipMemcpyDeviceToHost);
for (rocblas_int b = 0; b < batch_count; ++b)
hipMemcpy(hA[b], A[b], sizeof(double)*size_A, hipMemcpyDeviceToHost);
// the results are now in hA and hIpiv
// print some of the results
for (size_t b = 0; b < batch_count; ++b) {
printf("R[%zu] = [\n", b);
for (size_t i = 0; i < M; ++i) {
printf(" ");
for (size_t j = 0; j < N; ++j) {
printf("% 4.f ", (i <= j) ? hA[b][i + j*lda] : 0);
}
printf(";\n");
}
printf("]\n");
}
// clean up
free(hIpiv);
for (rocblas_int b = 0; b < batch_count; ++b)
free(hA[b]);
free(hA);
for (rocblas_int b = 0; b < batch_count; ++b)
hipFree(A[b]);
free(A);
hipFree(dA);
hipFree(dIpiv);
rocblas_destroy_handle(handle);
}
```
