---
title: "Two-dimensional kernels: Matrix multiplication tutorial &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/tutorial/programming-patterns/matrix_multiplication.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:57.653185+00:00
content_hash: "ff86c76cab14adf2"
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# Two-dimensional kernels: Matrix multiplication tutorial

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::::::::::::::::
{#two-dimensional-kernels-matrix-multiplication-tutorial .section}
# Two-dimensional kernels: Matrix multiplication tutorial[\#](#two-dimensional-kernels-matrix-multiplication-tutorial "Link to this heading"){.headerlink}

GPUs provide a massively parallel architecture consisting of thousands of cores, making them exceptionally well-suited for data-parallel computations. Two-dimensional kernel patterns are commonly data-parallel, enabling us to leverage GPU capabilities to exploit this inherent parallelism.

Tasks involving large matrices, which are common in image processing and machine learning applications, can be significantly accelerated by distributing computations across GPU cores. This tutorial explores how to implement matrix multiplication using two-dimensional GPU kernels with [[HIP]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html "(in HIP Documentation v7.2.53211)"){.reference .external}.

{#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

To follow this tutorial, you'll need installed drivers and a HIP compiler toolchain to compile your code. HIP supports compiling and running on Linux and Windows with AMD GPUs, the combination of install instructions is more than worth covering as part of this tutorial. For more information about installing HIP development packages, see [[Install HIP]{.doc}](../../install/install.html){.reference .internal}.

{#characteristics-of-2d-computational-problems .section}
## Characteristics of 2D computational problems[\#](#characteristics-of-2d-computational-problems "Link to this heading"){.headerlink}

- Spatial locality and data dependencies: Adjacent elements in the grid often exhibit strong spatial correlations, making memory access patterns and cache utilization critical for performance.

- Natural 2D data representation: Many datasets---such as images, numerical matrices, and discretized physical fields---map directly onto a two-dimensional coordinate space.

- Prevalence in simulation and modeling: Numerous scientific and engineering workloads such as finite difference methods, fluid dynamics, heat transfer, and image processing, are inherently two-dimensional.

Modern GPU architectures are engineered to exploit the parallelism of 2D computational grids. By designing kernels that operate on two-dimensional thread blocks and memory layouts, developers can optimize global memory access, minimize latency, and maximize throughput. Leveraging 2D kernel configurations not only aligns the computation with the GPU's hardware topology but also enables substantial performance improvements for domain-specific applications.

:
{#matrix-multiplication .section}
## Matrix multiplication[\#](#matrix-multiplication "Link to this heading"){.headerlink}

Let **A** and **B** be two matrices defined as follows, [\\(A \\in \\mathbb{R}\^{m \\times n}\\)]{.math .notranslate .nohighlight} and [\\(B \\in \\mathbb{R}\^{n \\times k}\\)]{.math .notranslate .nohighlight}. The matrix product [\\(C = A \\cdot B\\)]{.math .notranslate .nohighlight} is defined only when the number of columns of [\\(A\\)]{.math .notranslate .nohighlight} equals the number of rows of [\\(B\\)]{.math .notranslate .nohighlight}. The resulting matrix [\\(C \\in \\mathbb{R}\^{m \\times k}\\)]{.math .notranslate .nohighlight} has elements given by:

{.math .notranslate .nohighlight}
\\\[C\_{ij} = \\sum\_{r=1}\^{n} A\_{ir} B\_{rj}\\\]

for all [\\(i = 1, \\dots, m\\)]{.math .notranslate .nohighlight} and [\\(j = 1, \\dots, k\\)]{.math .notranslate .nohighlight}.

In other words, each element [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is computed as the dot product of the [\\(i\\)]{.math .notranslate .nohighlight}-th row vector of [\\(A\\)]{.math .notranslate .nohighlight} and the *j*-th column vector of [\\(B\\)]{.math .notranslate .nohighlight}. This operation is repeated for all valid pairs of [\\((i, j)\\)]{.math .notranslate .nohighlight} to construct the complete matrix [\\(C\\)]{.math .notranslate .nohighlight}.

For two square matrices of size [\\(N \\times N\\)]{.math .notranslate .nohighlight}, the computational cost of classical matrix multiplication is [\\(O(N\^3)\\)]{.math .notranslate .nohighlight}. As an example, consider [\\(N = 32\\)]{.math .notranslate .nohighlight}:

- **Multiplication operations**: [\\(32\^3 = 32{,}768\\)]{.math .notranslate .nohighlight}

- **Addition operations**: [\\(32\^2 \\times (32 - 1) = 31{,}744\\)]{.math .notranslate .nohighlight}

Each element in the resulting matrix [\\(C\\)]{.math .notranslate .nohighlight} is computed independently of the others, since it depends only on a single row of [\\(A\\)]{.math .notranslate .nohighlight} and a single column of [\\(B\\)]{.math .notranslate .nohighlight}. This property makes matrix multiplication **highly parallelizable** and well-suited for execution on GPUs, multi-core CPUs, or distributed computing architectures.
:

::
{#cpu-implementation .section}
## CPU implementation[\#](#cpu-implementation "Link to this heading"){.headerlink}

A baseline CPU implementation provides a clear understanding of the classical matrix multiplication algorithm before exploring parallel GPU execution.

:
{.highlight-c++ .notranslate}

highlight
    #include <iostream>
    #include <cstdlib>
    #define N 32

    void cpu_matrix_multiplication(float *a, float *b, float *c, int n) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                float sum = 0.0f;
                for (int k = 0; k < n; ++k) {
                    sum += a[i * n + k] * b[k * n + j];
                }
                c[i * n + j] = sum;
            }
        }
    }

    int main() {
        float *a, *b, *c;
        a = (float*)malloc(sizeof(float) * N * N);
        b = (float*)malloc(sizeof(float) * N * N);
        c = (float*)malloc(sizeof(float) * N * N);

        // Initialize matrix A
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                a[i * N + j] = static_cast<float>(rand()) / RAND_MAX;
            }
        }

        // Initialize matrix B
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                b[i * N + j] = static_cast<float>(rand()) / RAND_MAX;
            }
        }

        cpu_matrix_multiplication(a, b, c, N);
        free(a);
        free(b);
        free(c);
        return 0;
    }

:

The [`cpu_matrix_multiplication`{.docutils .literal .notranslate}]{.pre} function performs the classical [\\(O(N\^3)\\)]{.math .notranslate .nohighlight} matrix multiplication algorithm using three nested loops. The implementation proceeds as follows:

- **Input parameters:** Three pointers to contiguous memory blocks representing matrices [\\(A\\)]{.math .notranslate .nohighlight}, [\\(B\\)]{.math .notranslate .nohighlight}, and the output matrix [\\(C\\)]{.math .notranslate .nohighlight}.

- **Outer and middle loops:** The indices [\\(i\\)]{.math .notranslate .nohighlight} and [\\(j\\)]{.math .notranslate .nohighlight} iterate over the rows and columns of the output matrix [\\(C\\)]{.math .notranslate .nohighlight}, respectively.

- **Innermost loop:** For each element [\\(C\_{ij}\\)]{.math .notranslate .nohighlight}, the loop over [\\(k\\)]{.math .notranslate .nohighlight} performs a dot product between the *i*-th row of [\\(A\\)]{.math .notranslate .nohighlight} and the [\\(j\\)]{.math .notranslate .nohighlight}-th column of [\\(B\\)]{.math .notranslate .nohighlight}:

  
{.math .notranslate .nohighlight}
  \\\[C\_{ij} = \\sum\_{k=0}\^{n-1} A\_{ik} \\cdot B\_{kj}\\\]
  

- **Temporary accumulation:** A local scalar [`sum`{.code .docutils .literal .notranslate}]{.pre} accumulates the intermediate sum before being written to [`c[i`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`*`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`n`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`+`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`j]`{.code .docutils .literal .notranslate}]{.pre}.

This implementation has a computational complexity of [\\(O(N\^3)\\)]{.math .notranslate .nohighlight} and poor cache locality for large matrices, but it serves as a reference for understanding sequential computation before introducing GPU parallelization.
::

::::::::::::::::::::::::::
{#gpu-implementation .section}
## GPU implementation[\#](#gpu-implementation "Link to this heading"){.headerlink}

The following example demonstrates a complete HIP implementation of matrix multiplication, including host and device memory management, kernel implementation, configuration, and synchronization.

:::::::::
{#gpu-kernel .section}
### GPU kernel[\#](#gpu-kernel "Link to this heading"){.headerlink}

The core computation is performed by the GPU kernel, where each thread computes one element of the output matrix. For comparison, the CPU implementation is also provided.

pst-scrollable-table-container
+--------------------------------------------------------------------------------------+
| **GPU version**                                                                      |
+======================================================================================+
| :
{.highlight-c++ .notranslate}                                                   |
| 
highlight                                                                        |
|     __global__ void gpu_matrix_multiplication(float *a, float *b, float *c, int n) { |
|                                                                                      |
|         int row = blockIdx.y * blockDim.y + threadIdx.y;                             |
|         int col = blockIdx.x * blockDim.x + threadIdx.x;                             |
|         float sum = 0.0f;                                                            |
|                                                                                      |
|         if (row < n && col < n) {                                                    |
|             for (int k = 0; k < n; ++k) {                                            |
|                 sum += a[row * n + k] * b[k * n + col];                              |
|             }                                                                        |
|             c[row * n + col] = sum;                                                  |
|         }                                                                            |
|     }                                                                                |
| 
                                                                                 |
| :
                                                                                |
+--------------------------------------------------------------------------------------+

pst-scrollable-table-container
+---------------------------------------------------------------------------+
| **CPU version**                                                           |
+===========================================================================+
| :
{.highlight-c++ .notranslate}                                        |
| 
highlight                                                             |
|     void cpu_matrix_multiplication(float *a, float *b, float *c, int n) { |
|                                                                           |
|         for (int i = 0; i < n; ++i) {                                     |
|             for (int j = 0; j < n; ++j) {                                 |
|                 float sum = 0.0f;                                         |
|                 for (int k = 0; k < n; ++k) {                             |
|                     sum += a[i * n + k] * b[k * n + j];                   |
|                 }                                                         |
|                 c[i * n + j] = sum;                                       |
|             }                                                             |
|         }                                                                 |
|     }                                                                     |
| 
                                                                      |
| :
                                                                     |
+---------------------------------------------------------------------------+

The outer and middle loops of the CPU implementation are replaced by the parallel execution of the GPU implementation. Each GPU thread computes the **single element** [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} of the output matrix corresponding to one dot product between a row of [\\(A\\)]{.math .notranslate .nohighlight} and a column of [\\(B\\)]{.math .notranslate .nohighlight}. This decomposition exposes massive parallelism, as all elements of [\\(C\\)]{.math .notranslate .nohighlight} can be computed independently and concurrently.

::
{#thread-and-block-identification .section}
#### Thread and block identification[\#](#thread-and-block-identification "Link to this heading"){.headerlink}

Each thread's global position within the grid is determined by:

:
{.highlight-c++ .notranslate}

highlight
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

:

Here:

- [`threadIdx.(x|y)`{.docutils .literal .notranslate}]{.pre}: Local thread indices within a block.

- [`blockIdx.(x|y)`{.docutils .literal .notranslate}]{.pre}: Block indices within the grid.

- [`blockDim.(x|y)`{.docutils .literal .notranslate}]{.pre}: Dimensions of each block (used to scale offsets).
::

::
{#boundary-checking .section}
#### Boundary checking[\#](#boundary-checking "Link to this heading"){.headerlink}

Since the total number of threads launched may exceed [\\(N\^2\\)]{.math .notranslate .nohighlight}, boundary checking ensures that threads outside the matrix domain do not perform invalid memory accesses:

:
{.highlight-c++ .notranslate}

highlight
    if (row < n && col < n) {
        // Safe computation region
    }

:
::

{#dot-product-computation .section}
#### Dot product computation[\#](#dot-product-computation "Link to this heading"){.headerlink}

Within the valid region, each thread executes a dot product over [\\(k\\)]{.math .notranslate .nohighlight}:

- Loads one element from row [`row`{.code .docutils .literal .notranslate}]{.pre} of matrix [\\(A\\)]{.math .notranslate .nohighlight}.

- Loads one element from column [`col`{.code .docutils .literal .notranslate}]{.pre} of matrix [\\(B\\)]{.math .notranslate .nohighlight}.

- Multiplies and accumulates these values into [`sum`{.code .docutils .literal .notranslate}]{.pre}.

- Writes the final scalar result to [`c[row`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`*`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`n`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`+`{.code .docutils .literal .notranslate}]{.pre}` `{.code .docutils .literal .notranslate}[`col]`{.code .docutils .literal .notranslate}]{.pre}.

This kernel performs the same [\\(O(N\^3)\\)]{.math .notranslate .nohighlight} arithmetic operations as the CPU version but distributes them across thousands of concurrent GPU threads, achieving significant acceleration through parallel execution and memory throughput optimization.

:::::::::

::
{#step-1-host-memory-allocation-and-initialization .section}
### Step 1: Host memory allocation and initialization[\#](#step-1-host-memory-allocation-and-initialization "Link to this heading"){.headerlink}

Host memory is allocated for matrices and initialized with random floating-point values.

:
{.highlight-c++ .notranslate}

highlight
    int main() {
        float *h_a, *h_b, *h_c;
        h_a = (float*)malloc(sizeof(float) * N * N);
        h_b = (float*)malloc(sizeof(float) * N * N);
        h_c = (float*)malloc(sizeof(float) * N * N);

        // Initialize matrix A
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                h_a[i * N + j] = static_cast<float>(rand()) / RAND_MAX;
            }
        }

        // Initialize matrix B
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                h_b[i * N + j] = static_cast<float>(rand()) / RAND_MAX;
            }
        }

:

**Description:**

- Declare host (CPU) pointers [`h_a`{.docutils .literal .notranslate}]{.pre}, [`h_b`{.docutils .literal .notranslate}]{.pre}, and [`h_c`{.docutils .literal .notranslate}]{.pre}.

- Allocate contiguous memory for each [\\(N \\times N\\)]{.math .notranslate .nohighlight} matrix.

- Initialize input matrices [\\(A\\)]{.math .notranslate .nohighlight} and [\\(B\\)]{.math .notranslate .nohighlight} with pseudo-random floating-point values in the range \[0, 1).
::

::
{#step-2-device-memory-allocation-and-data-transfer .section}
### Step 2: Device memory allocation and data transfer[\#](#step-2-device-memory-allocation-and-data-transfer "Link to this heading"){.headerlink}

Memory is allocated on the GPU, and input matrices are transferred from host to device.

:
{.highlight-c++ .notranslate}

highlight
    float *d_a, *d_b, *d_c;
    hipMalloc((void**)&d_a, sizeof(float) * N * N);
    hipMalloc((void**)&d_b, sizeof(float) * N * N);
    hipMalloc((void**)&d_c, sizeof(float) * N * N);

    hipMemcpy(d_a, h_a, sizeof(float) * N * N, hipMemcpyHostToDevice);
    hipMemcpy(d_b, h_b, sizeof(float) * N * N, hipMemcpyHostToDevice);

:

**Operations:**

1.  Allocate GPU (device) memory for matrices [`d_a`{.docutils .literal .notranslate}]{.pre}, [`d_b`{.docutils .literal .notranslate}]{.pre}, and [`d_c`{.docutils .literal .notranslate}]{.pre}.

2.  Transfer data from host to device using [[`hipMemcpy()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/memory_management.html#_CPPv49hipMemcpyPvPKv6size_t13hipMemcpyKind "hipMemcpy"){.reference .internal} with direction [`hipMemcpyHostToDevice`{.xref .cpp .cpp-enum .docutils .literal .notranslate}]{.pre}.
::

::::::
{#step-3-configure-and-launch-kernel .section}
### Step 3: Configure and launch kernel[\#](#step-3-configure-and-launch-kernel "Link to this heading"){.headerlink}

Kernel launch parameters define how threads are organized across blocks and the grid.

:
{.highlight-c++ .notranslate}

highlight
    dim3 threadsPerBlock(BLOCK_SIZE, BLOCK_SIZE);
    int n_blocks = static_cast<int>(ceil(static_cast<float>(N) / BLOCK_SIZE));
    dim3 blocksPerGrid(n_blocks, n_blocks);

    hipLaunchKernelGGL(gpu_matrix_multiplication,
                       blocksPerGrid,
                       threadsPerBlock,
                       0, 0,
                       d_a, d_b, d_c, N);

    hipDeviceSynchronize();

:

::
{#configuration-details .section}
#### Configuration details[\#](#configuration-details "Link to this heading"){.headerlink}

The [`dim3`{.code .docutils .literal .notranslate}]{.pre} type defines thread and block dimensions:

- [`threadsPerBlock`{.code .docutils .literal .notranslate}]{.pre}: Number of threads per block. A 16 × 16 block (256 threads total).

- [`n_blocks`{.code .docutils .literal .notranslate}]{.pre}: Number of blocks per dimension. Computed as [\\(\\lceil N / \\mathrm{BLOCK\\\_SIZE} \\rceil\\)]{.math .notranslate .nohighlight}.

- [`blocksPerGrid`{.code .docutils .literal .notranslate}]{.pre}: A grid of blocks covering the entire [\\(N \\times N\\)]{.math .notranslate .nohighlight} matrix.

For example [\\(N = 256\\)]{.math .notranslate .nohighlight} and [`BLOCK_SIZE`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`16`{.docutils .literal .notranslate}]{.pre}:

- [`n_blocks`{.code .docutils .literal .notranslate}]{.pre}: [\\(\\lceil 256 / 16 \\rceil = 16\\)]{.math .notranslate .nohighlight}

- [`blocksPerGrid`{.code .docutils .literal .notranslate}]{.pre}: [\\(16 \\times 16 = 256\\)]{.math .notranslate .nohighlight}

- Total threads: [\\(256 \\text{ blocks} \\times 256 \\text{ threads/block} = 65{,}536\\)]{.math .notranslate .nohighlight} threads.

Rounding up ensures full coverage of the matrix even when [\\(N\\)]{.math .notranslate .nohighlight} is not an exact multiple of [`BLOCK_SIZE`{.docutils .literal .notranslate}]{.pre}. The boundary check in the kernel

:
{.highlight-c++ .notranslate}

highlight
    if (row < n && col < n)

:

prevents out-of-bounds memory access for extra threads.
::

{#synchronization .section}
#### Synchronization[\#](#synchronization "Link to this heading"){.headerlink}

The call to [[`hipDeviceSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev "hipDeviceSynchronize"){.reference .internal} ensures that all GPU computations complete before the CPU accesses results or proceeds to subsequent operations. This is essential for correctness and debugging.

::::::

::
{#step-4-copy-results-back-and-cleanup .section}
### Step 4: Copy results back and cleanup[\#](#step-4-copy-results-back-and-cleanup "Link to this heading"){.headerlink}

After the kernel execution, results are transferred back to host memory, and all allocated resources are released.

:
{.highlight-c++ .notranslate}

highlight
    hipMemcpy(h_c, d_c, sizeof(float) * N * N, hipMemcpyDeviceToHost);

    hipFree(d_a);
    hipFree(d_b);
    hipFree(d_c);
    free(h_a);
    free(h_b);
    free(h_c);
    return 0;
    }

:

**Summary of final steps:**

1.  Copy the result matrix from device to host using [`hipMemcpy`{.docutils .literal .notranslate}]{.pre}.

2.  Free all device memory allocations with [`hipFree`{.docutils .literal .notranslate}]{.pre}.

3.  Release host memory with [`free`{.docutils .literal .notranslate}]{.pre}.

4.  Return control to the operating system, indicating successful program termination.
::
::::::::::::::::::::::::::

{#parallelization-benefits .section}
## Parallelization benefits[\#](#parallelization-benefits "Link to this heading"){.headerlink}

For a 256 × 256 matrix multiplication:

- **Sequential CPU version:** Computes 65,536 output elements serially.

- **Parallel GPU version:** Executes up to 65,536 independent threads concurrently.

This results in a theoretical performance gain proportional to the number of active GPU threads and the device's compute throughput.

Each output element [\\(C\_{ij}\\)]{.math .notranslate .nohighlight} is computed independently from others, since it depends solely on row [\\(i\\)]{.math .notranslate .nohighlight} of matrix [\\(A\\)]{.math .notranslate .nohighlight} and column [\\(j\\)]{.math .notranslate .nohighlight} of matrix [\\(B\\)]{.math .notranslate .nohighlight}. This independence allows full utilization of GPU streaming multiprocessors and makes the algorithm highly scalable.

{#best-practices .section}
## Best practices[\#](#best-practices "Link to this heading"){.headerlink}

1.  **Choose optimal block sizes**

    Powers of two (e.g., 16 or 32) often yield better occupancy and memory alignment.

2.  **Handle boundary conditions**

    Always include thread boundary checks.

3.  **Synchronize appropriately**

    Use [[`hipDeviceSynchronize()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../reference/hip_runtime_api/modules/device_management.html#_CPPv420hipDeviceSynchronizev "hipDeviceSynchronize"){.reference .internal} after kernel launches to ensure data consistency.

4.  **Memory coalescing**

    Arrange data access patterns so consecutive threads access contiguous memory locations, maximizing bandwidth utilization.

5.  **Use shared memory**

    Use shared memory to cache sub-blocks of matrices, significantly reducing global memory latency.

6.  **Profile and tune**

    Use tools such as [[rocprofv3]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3.html "(in Rocprofiler SDK v1.1.0)"){.reference .external} or [[ROCm compute profiler]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/how-to/profile/mode.html "(in ROCm Compute Profiler v3.4.0)"){.reference .external} to identify bottlenecks and fine-tune kernel launch configurations.

{#conclusion .section}
## Conclusion[\#](#conclusion "Link to this heading"){.headerlink}

Two-dimensional GPU kernels provide an efficient mechanism to accelerate dense linear algebra computations such as matrix multiplication by exploiting fine-grained data parallelism. This example demonstrates:

- Structuring GPU kernels for 2D problems.

- Managing memory transfers between host and device.

- Configuring thread and block hierarchies.

- Achieving substantial speedups via massive parallel execution.

Understanding these concepts enables developers to implement optimized GPU solutions for computationally intensive workloads, including scientific simulations, numerical linear algebra, and machine learning. Because each output element is computed independently, matrix multiplication serves as an ideal introductory example for mastering GPU programming paradigms applicable to a wide range of data-parallel applications.

:::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
