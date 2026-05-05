---
title: "rocSPARSE storage formats &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/conceptual/storage-formats-sparse.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:42.195424+00:00
content_hash: "c2cdbd6025524595"
---

# rocSPARSE storage formats[#](#rocsparse-storage-formats)

A sparse matrix is a matrix in which most of the items are zero,
although there is no strict criteria for the number of non-zero items. The
*sparsity* of a matrix refers to the number of non-zero elements divided by the total
number of elements. For example, if an 8 x 8 matrix with 64 elements has 16 non-zero elements,
it has a sparsity value of 0.25.

The main reason for storing and processing sparse matrices differently is to take advantage of lower memory requirements and potentially faster processing times. It is inefficient or impractical to store every element of a sparse matrix in memory (as a dense matrix) because most of the elements are zero. Instead, sparse matrices are compressed in storage using multiple vectors that map the individual non-zero values to their position in the original matrix. However, more complex algorithms are required to store the values in, and retrieve them from, these compound data structures.

rocSPARSE offers several storage formats for sparse matrices, each with specialized algorithms for
matrix storage, retrieval, and manipulation. For additional information about the
storage formats and their associated algorithms, see the
[Sparse matrix vector multiplication blog post](https://rocm.blogs.amd.com/high-performance-computing/spmv/part-1/README.html).

## Storage formats[#](#storage-formats)

This section describes the supported matrix storage formats.

Note

The different storage formats support indexing from a base of 0 or 1 as described in [Storage schemes and indexing base](#index-base).

### COO storage format[#](#coo-storage-format)

The Coordinate (COO) storage format represents an \(m \times n\) matrix by:

m |
Number of rows (integer). |
n |
Number of columns (integer). |
nnz |
Number of non-zero elements (integer). |
coo_val |
Array of |
coo_row_ind |
Array of |
coo_col_ind |
Array of |

The COO matrix is sorted by row indices and column indices per row. Furthermore, each pair of indices should appear only once. The following \(3 \times 5\) matrix and corresponding COO structures, with \(m = 3\), \(n = 5\), and \(\text{nnz} = 8\), use zero-based indexing:

where

### COO (AoS) storage format[#](#coo-aos-storage-format)

The Coordinate (COO) Array of Structure (AoS) storage format represents an \(m \times n\) matrix by:

m |
Number of rows (integer). |
n |
Number of columns (integer). |
nnz |
Number of non-zero elements (integer). |
coo_val |
Array of |
coo_ind |
Array of |

The COO (AoS) matrix is sorted by row indices and column indices per row. Each pair of indices should appear only once. The following \(3 \times 5\) matrix and corresponding COO (AoS) structures, with \(m = 3\), \(n = 5\), and \(\text{nnz} = 8\), use zero-based indexing:

where

### CSR storage format[#](#csr-storage-format)

The Compressed Sparse Row (CSR) storage format represents an \(m \times n\) matrix by:

m |
Number of rows (integer). |
n |
Number of columns (integer). |
nnz |
Number of non-zero elements (integer). |
csr_val |
Array of |
csr_row_ptr |
Array of |
csr_col_ind |
Array of |

The CSR matrix is sorted by column indices within each row. Each pair of indices should appear only once. The following \(3 \times 5\) matrix and corresponding CSR structures, with \(m = 3\), \(n = 5\), and \(\text{nnz} = 8\), use one-based indexing:

where

### CSC storage format[#](#csc-storage-format)

The Compressed Sparse Column (CSC) storage format represents an \(m \times n\) matrix by:

m |
Number of rows (integer). |
n |
Number of columns (integer). |
nnz |
Number of non-zero elements (integer). |
csc_val |
Array of |
csc_col_ptr |
Array of |
csc_row_ind |
Array of |

The CSC matrix is sorted by row indices within each column. Each pair of indices should appear only once. The following \(3 \times 5\) matrix and corresponding CSC structures, with \(m = 3\), \(n = 5\), and \(\text{nnz} = 8\), use one-based indexing:

where

### BSR storage format[#](#bsr-storage-format)

The Block Compressed Sparse Row (BSR) storage format represents an \((mb \cdot \text{bsr_dim}) \times (nb \cdot \text{bsr_dim})\) matrix by:

mb |
Number of block rows (integer). |
nb |
Number of block columns (integer). |
nnzb |
Number of non-zero blocks (integer). |
bsr_val |
Array of |
bsr_row_ptr |
Array of |
bsr_col_ind |
Array of |
bsr_dim |
Dimension of each block (integer). |

The BSR matrix is sorted by column indices within each row. This matrix is defined as having a number of rows equivalent to \(\text{block_dim} \times \text{number_of_row_blocks}\). The following \(4 \times 3\) matrix and corresponding BSR structures, with \(\text{bsr_dim} = 2\), \(mb = 2\), \(nb = 2\), and \(\text{nnzb} = 4\), use zero-based indexing and column-major storage:

with the blocks \(A_{ij}\)

such that

with arrays represented as

### GEBSR storage format[#](#gebsr-storage-format)

The General Block Compressed Sparse Row (GEBSR) storage format represents an \((mb \cdot \text{bsr_row_dim}) \times (nb \cdot \text{bsr_col_dim})\) matrix by:

mb |
Number of block rows (integer). |
nb |
Number of block columns (integer). |
nnzb |
Number of non-zero blocks (integer). |
bsr_val |
Array of |
bsr_row_ptr |
Array of |
bsr_col_ind |
Array of |
bsr_row_dim |
Row dimension of each block (integer). |
bsr_col_dim |
Column dimension of each block (integer). |

The GEBSR matrix is sorted by column indices within each row. If \(m\) is not evenly divisible by the row block dimension or \(n\) is not evenly divisible by the column block dimension, then zeros are padded to the matrix, such that \(mb = (m + \text{bsr_row_dim} - 1) / \text{bsr_row_dim}\) and \(nb = (n + \text{bsr_col_dim} - 1) / \text{bsr_col_dim}\). The following \(4 \times 5\) matrix and corresponding GEBSR structures, with \(\text{bsr_row_dim} = 2\), \(\text{bsr_col_dim} = 3\), \(mb = 2\), \(nb = 2\), and \(\text{nnzb} = 4\), use zero-based indexing and column-major storage:

with the blocks \(A_{ij}\)

such that

with arrays represented as

### ELL storage format[#](#ell-storage-format)

The Ellpack-Itpack (ELL) storage format represents an \(m \times n\) matrix by:

m |
Number of rows (integer). |
n |
Number of columns (integer). |
ell_width |
Maximum number of non-zero elements per row (integer). |
ell_val |
Array of |
ell_col_ind |
Array of |

The ELL matrix is assumed to be stored in column-major format. Rows with less
than `ell_width`

non-zero elements are padded with zeros (`ell_val`

) and \(-1\) (`ell_col_ind`

).
The following \(3 \times 5\) matrix and corresponding ELL structures,
with \(m = 3\), \(n = 5\), and \(\text{ell_width} = 3\), use zero-based indexing:

where

### Blocked ELL storage format[#](#blocked-ell-storage-format)

The Blocked Ellpack (ELL) storage format represents an \((mb \cdot \text{block_dim}) \times (nb \cdot \text{block_dim})\) matrix by:

mb |
Number of block rows (integer). |
nb |
Number of block columns (integer). |
ell_width |
Maximum number of non-zero block elements per row (integer). |
ell_val |
Array of |
ell_col_ind |
Array of |
block_dim |
Dimension of each block (integer). |

The Blocked ELL is similar to the ELL format except that column entries now indicate the location of two dimensional blocks of size
`block_dim * block_dim`

instead of single matrix entries. The block values can be stored in either row or column ordering.
Rows with less than `ell_width`

non-zero blocks are padded with zero blocks (`ell_val`

) and \(-1\) (`ell_col_ind`

).
The following \(6 \times 6\) matrix and corresponding Blocked ELL structures,
with \(mb = 3\), \(nb = 3\), \(block_dim = 2\), and \(\text{ell_width} = 2\), use zero-based indexing and row ordering for the blocks:

with the blocks \(A_{ij}\)

such that

where

### HYB storage format[#](#hyb-storage-format)

The Hybrid (HYB) storage format represents an \(m \times n\) matrix by:

m |
Number of rows (integer). |
n |
Number of columns (integer). |
nnz |
Number of non-zero elements of the COO part (integer). |
ell_width |
Maximum number of non-zero elements per row of the ELL part (integer). |
ell_val |
Array of |
ell_col_ind |
Array of |
coo_val |
Array of |
coo_row_ind |
Array of |
coo_col_ind |
Array of |

The HYB format is a combination of the ELL and COO sparse matrix formats.
Typically, the regular part of the matrix is stored in
ELL storage format, and the irregular part of the matrix is stored
in COO storage format. Three different partitioning schemes can
be applied when converting a CSR matrix to a matrix in
HYB storage format. For further details on the partitioning schemes,
see [rocsparse_hyb_partition](../reference/enumerations.html#rocsparse-hyb-partition).

## Storage schemes and indexing base[#](#storage-schemes-and-indexing-base)

rocSPARSE supports zero-based and one-based indexing.
The index base is selected by the [ rocsparse_index_base](../reference/enumerations.html#_CPPv420rocsparse_index_base) type,
which is either passed as a standalone parameter or as part of the

[type.](../reference/types.html#_CPPv419rocsparse_mat_descr)

`rocsparse_mat_descr`

Dense vectors are represented with a 1D array, stored linearly in memory. Sparse vectors are represented by a 1D data array that holds all non-zero elements and a 1D indexing array that holds the positions of the corresponding non-zero elements, both stored linearly in memory.
