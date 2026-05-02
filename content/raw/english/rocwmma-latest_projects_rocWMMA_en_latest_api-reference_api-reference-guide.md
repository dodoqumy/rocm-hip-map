---
title: "API reference guide &#8212; rocWMMA 2.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocWMMA/en/latest/api-reference/api-reference-guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:46.852485+00:00
content_hash: "ab11372e44dd9c05"
---

# API reference guide[#](#api-reference-guide)

This document provides information about rocWMMA functions, data types, and other programming constructs.

## Synchronous API[#](#synchronous-api)

rocWMMA API functions such as `load_matrix_sync`

, `store_matrix_sync`

, and `mma_sync`

are synchronous when
used with global memory. However, when you use these functions with shared memory, for example, LDS memory,
explicit workgroup synchronization (`synchronize_workgroup`

) might be required.

## Supported GPU architectures[#](#supported-gpu-architectures)

Supported CDNA architectures (wave64):

gfx908

gfx90a

gfx942

gfx950


Note

gfx9 refers to gfx908, gfx90a, gfx942, and gfx950.

Supported RDNA architectures (wave32):

gfx1100

gfx1101

gfx1102

gfx1200

gfx1201


Note

gfx11 refers to gfx1100, gfx1101, and gfx1102. gfx12 refers to gfx1200 and gfx1201.

## Supported data types[#](#supported-data-types)

rocWMMA mixed precision multiply-accumulate operations support the following data type combinations.

Data Types **<Ti / To / Tc>** = <Input type / Output Type / Compute Type>, where:

Input Type = Matrix A / B

Output Type = Matrix C / D

Compute Type = Math / Accumulation type


Supported data types:

i8: 8-bit precision integer

f8: 8-bit precision floating point

bf8: 8-bit precision brain floating point

f16: half-precision floating point

bf16: half-precision brain floating point

f32: single-precision floating point

i32: 32-bit precision integer

xf32: single-precision tensor floating point

f64: double-precision floating point


Note

f16 includes support for both _Float16 and __half types.

f8 NANOO (optimized) format is only supported on gfx942, otherwise f8 OCP is assumed on targets that support f8 datatypes.

Ti / To / Tc |
BlockM |
BlockN |
BlockK Range* (Powers of 2) |
CDNA Support |
RDNA Support |
|---|---|---|---|---|---|
bf8 / f32 / f32 |
16 |
16 |
32+ |
gfx940, gfx950 |
gfx12 |
32 |
32 |
16+ |
- |
||
f8 / f32 / f32 |
16 |
16 |
32+ |
gfx940, gfx950 |
gfx12 |
32 |
32 |
16+ |
- |
||
i8 / i32 / i32 |
16 |
16 |
16 |
gfx908, gfx90a |
gfx11, gfx12 |
32 |
gfx940, gfx950 |
- |
|||
64+ |
gfx950 |
- |
|||
32 |
32 |
8 |
gfx908, gfx90a |
- |
|
16 |
gfx940, gfx950 |
- |
|||
32+ |
gfx950 |
- |
|||
i8 / i8 / i32 |
16 |
16 |
16 |
gfx908, gfx90a |
gfx11, gfx12 |
32 |
gfx940, gfx950 |
- |
|||
64+ |
gfx950 |
- |
|||
32 |
32 |
8 |
gfx908, gfx90a |
- |
|
16 |
gfx940, gfx950 |
- |
|||
32+ |
gfx950 |
- |
|||
f16 / f32 / f32 |
16 |
16 |
16 |
gfx9 |
gfx11, gfx12 |
32+ |
gfx950 |
- |
|||
32 |
32 |
8 |
gfx9 |
- |
|
16+ |
gfx950 |
- |
|||
f16 / f16 / f32 |
16 |
16 |
16 |
gfx9 |
gfx11, gfx12 |
32+ |
gfx950 |
- |
|||
32 |
32 |
8 |
gfx9 |
- |
|
16+ |
gfx950 |
- |
|||
f16 / f16 / f16** |
16 |
16 |
16 |
gfx9 |
gfx11, gfx12 |
32+ |
gfx950 |
- |
|||
32 |
32 |
8 |
gfx9 |
- |
|
16+ |
gfx950 |
- |
|||
bf16 / f32 / f32 |
16 |
16 |
8 |
gfx908 |
- |
16 |
gfx90a, gfx942, gfx950 |
gfx11, gfx12 |
|||
32+ |
gfx950 |
- |
|||
32 |
32 |
4+ |
gfx908 |
- |
|
8 |
gfx90a, gfx942, gfx950 |
- |
|||
16+ |
gfx950 |
- |
|||
bf16 / bf16 / f32 |
16 |
16 |
8 |
gfx908 |
- |
16 |
gfx90a, gfx942, gfx950 |
gfx11, gfx12 |
|||
32+ |
gfx950 |
- |
|||
32 |
32 |
4+ |
gfx908 |
- |
|
8 |
gfx90a, gfx942, gfx950 |
- |
|||
16+ |
gfx950 |
- |
|||
bf16 / bf16 / bf16** |
16 |
16 |
8 |
gfx908 |
- |
16 |
gfx90a, gfx942, gfx950 |
gfx11, gfx12 |
|||
32+ |
gfx950 |
- |
|||
32 |
32 |
4+ |
gfx908 |
- |
|
8 |
gfx90a, gfx942, gfx950 |
- |
|||
16+ |
gfx950 |
- |
|||
f32 / f32 / f32 |
16 |
16 |
4+ |
gfx9 |
- |
32 |
32 |
2+ |
gfx9 |
- |
|
xf32 / xf32 / xf32 |
16 |
16 |
8+ |
gfx942 |
- |
32 |
32 |
4+ |
|||
f64 / f64 / f64 |
16 |
16 |
4+ |
gfx90a, gfx942, gfx950 |
- |

Note

BlockM/N values are minimum recommended values. Below these values padding is used which may impact performance. Above this value powers of 2 are acceptable.

* BlockK range specifies the minimum recommended value. Below this value padding is used which may impact performance. Above this value powers of 2 are acceptable. In practice, BlockK values are typically 32 or less.

** On CDNA architectures, matrix unit accumulation is performed in natively 32-bit precision and then converted to the target data type.

Note

rocWMMA supports partial fragment sizes where `FragMNK`

may be smaller than the `BlockMNK`

sizes listed in the table above. These fragments are internally padded to nearest supported `BlockMNK`

sizes.

## Supported matrix layouts[#](#supported-matrix-layouts)

(N = col major, T = row major)

LayoutA |
LayoutB |
Layout C |
LayoutD |
|---|---|---|---|
N |
N |
N |
N |
N |
N |
T |
T |
N |
T |
N |
N |
N |
T |
T |
T |
T |
N |
N |
N |
T |
N |
T |
T |
T |
T |
N |
N |
T |
T |
T |
T |

## Supported thread block sizes[#](#supported-thread-block-sizes)

rocWMMA supports up to four wavefronts per thread block. The X dimension should be a multiple of the wave size and is scaled accordingly.

TBlock_X |
TBlock_Y |
|---|---|
WaveSize |
1 |
WaveSize |
2 |
WaveSize |
4 |
WaveSize*2 |
1 |
WaveSize*2 |
2 |
WaveSize*4 |
1 |

Note

WaveSize (RDNA) = 32

WaveSize (CDNA) = 64

## Using rocWMMA API[#](#using-rocwmma-api)

This section describes how to use the rocWMMA library API.

## rocWMMA datatypes[#](#rocwmma-datatypes)

### matrix_a[#](#matrix-a)

-
struct matrix_a
[#](#_CPPv4N7rocwmma8matrix_aE) Meta-tag indicating data context is input Matrix A.


### matrix_b[#](#matrix-b)

-
struct matrix_b
[#](#_CPPv4N7rocwmma8matrix_bE) Meta-tag indicating data context is input Matrix B.


### accumulator[#](#accumulator)

-
struct accumulator
[#](#_CPPv4N7rocwmma11accumulatorE) Meta-tag indicating data context is Accumulator (also used as Matrix C / D).


### row_major[#](#row-major)

-
struct row_major
[#](#_CPPv4N7rocwmma9row_majorE) Meta-tag indicating 2D in-memory data layout as row major.


### col_major[#](#col-major)

-
struct col_major
[#](#_CPPv4N7rocwmma9col_majorE) Meta-tag indicating 2D in-memory data layout as column major.


### default_schedule[#](#default-schedule)

-
typedef IOScheduler::Default rocwmma::fragment_scheduler::default_schedule
[#](#_CPPv4N7rocwmma18fragment_scheduler16default_scheduleE) The default fragment scheduler; each wave operates independently.


### coop_row_major_2d[#](#coop-row-major-2d)

-
typedef IOScheduler::RowMajor2d<TBlockX, TBlockY> rocwmma::fragment_scheduler::coop_row_major_2d
[#](#_CPPv4N7rocwmma18fragment_scheduler17coop_row_major_2dE) A cooperative scheduling strategy where each wave in the 2d threadblock will contribute to the fragment operation in

[row_major](#structrocwmma_1_1row__major)grid order. All waves are scheduled in[row_major](#structrocwmma_1_1row__major)order. E.g. (TBlockX, TBlockY) => 2x2 waves w0 = (0, 0), w1 = (0, 1), w2 = (1, 0), w3 = (1, 1)- Template Parameters:
**TBlockX**– the size of the thread-block in the X dimension**TBlockY**– the size of the thread-block in the Y dimension



### coop_col_major_2d[#](#coop-col-major-2d)

-
typedef IOScheduler::ColMajor2d<TBlockX, TBlockY> rocwmma::fragment_scheduler::coop_col_major_2d
[#](#_CPPv4N7rocwmma18fragment_scheduler17coop_col_major_2dE) A cooperative scheduling strategy where each wave in the 2d threadblock will contribute to the fragment operation in

[col_major](#structrocwmma_1_1col__major)grid order. All waves are scheduled in[row_major](#structrocwmma_1_1row__major)order. E.g. (TBlockX, TBlockY) => 2x2 waves w0 = (0, 0), w2 = (0, 1), w1 = (1, 0), w3 = (1, 1)- Template Parameters:
**TBlockX**– the size of the thread-block in the X dimension**TBlockY**– the size of the thread-block in the Y dimension



### coop_row_slice_2d[#](#coop-row-slice-2d)

-
typedef IOScheduler::RowSlice2d<TBlockX, TBlockY> rocwmma::fragment_scheduler::coop_row_slice_2d
[#](#_CPPv4N7rocwmma18fragment_scheduler17coop_row_slice_2dE) A cooperative scheduling strategy where each row of waves in the 2d threadblock will contribute to the fragment operation. Waves are partitioned into rows. Only waves in the same row participate together. E.g. (TBlockX, TBlockY) = 2x2 waves RowSlice0: w0 = (0, 0), w1 = (0, 1) RowSlice1: w0 = (1, 0), w1 = (1, 1)

- Template Parameters:
**TBlockX**– the size of the thread-block in the X dimension**TBlockY**– the size of the thread-block in the Y dimension



### coop_col_slice_2d[#](#coop-col-slice-2d)

-
typedef IOScheduler::ColSlice2d<TBlockX, TBlockY> rocwmma::fragment_scheduler::coop_col_slice_2d
[#](#_CPPv4N7rocwmma18fragment_scheduler17coop_col_slice_2dE) A cooperative scheduling strategy where each col of waves in the 2d threadblock will contribute to the fragment operation. Waves are partitioned into cols. Only waves in the same col participate together. E.g. (TBlockX, TBlockY) = 2x2 waves ColSlice0: ColSlice1: w0 = (0, 0), w0 = (0, 1), w1 = (1, 0) w1 = (1, 1)

- Template Parameters:
**TBlockX**– the size of the thread-block in the X dimension**TBlockY**– the size of the thread-block in the Y dimension



### single[#](#single)

-
typedef IOScheduler::Single<TBlockX, TBlockY, WaveIdx> rocwmma::fragment_scheduler::single
[#](#_CPPv4N7rocwmma18fragment_scheduler6singleE) A cooperative scheduling strategy where only one wave in the thread block will participate.

- Template Parameters:
**TBlockX**– the size of the thread-block in the X dimension**TBlockY**– the size of the thread-block in the Y dimension**WaveIdx**– the index of the wave which will participate



### fragment[#](#fragment)

-
template<typename MatrixT, uint32_t FragM, uint32_t FragN, uint32_t FragK, typename DataT, typename DataLayoutT = void, typename Scheduler = fragment_scheduler::
[default_schedule](#_CPPv4N7rocwmma18fragment_scheduler16default_scheduleE)>

class fragment[#](#_CPPv4I0_8uint32_t_8uint32_t_8uint32_t000EN7rocwmma8fragmentE) rocWMMA fragment class. This is the primary object used in block-wise decomposition of the matrix multiply-accumulate (mma) problem space. In general, fragment data is associated with a matrix context (

[matrix_a](#structrocwmma_1_1matrix__a),[matrix_b](#structrocwmma_1_1matrix__b)or accumulator), a block size (BlockM/N/K), a datatype (e.g. single-precision float, etc.) and an in-memory 2D layout (e.g.[row_major](#structrocwmma_1_1row__major)or[col_major](#structrocwmma_1_1col__major)). These fragment properties are used to define how data is handled and stored locally, and to drive API implementations for loading / storing, mma and transforms. Fragment abstractions are designed to promote a simple wavefront programming model, which can accelerate development time. Internal thread-level details are handled by rocWMMA which frees the user to focus on wavefront block-wise decomposition. Written purely in device code, the programmer can use this object in their own device kernels.Note

Fragments are stored in packed registers, however vector elements have no guaranteed order or locality.

- Template Parameters:

Public Types

Public Functions

-
inline
[DataT](#_CPPv4I0_8uint32_t_8uint32_t_8uint32_t000EN7rocwmma8fragmentE)&operator[](uint32_t index)[#](#_CPPv4N7rocwmma8fragmentixE8uint32_t) - Parameters:
**index**– Element index- Returns:
Mutable unpacked element accessor at given index



Public Members

Public Static Functions

-
static inline constexpr uint32_t height()
[#](#_CPPv4N7rocwmma8fragment6heightEv) - Returns:
The geometric height of fragment



-
static inline constexpr uint32_t width()
[#](#_CPPv4N7rocwmma8fragment5widthEv) - Returns:
The geometric width of fragment



-
static inline constexpr uint32_t blockDim()
[#](#_CPPv4N7rocwmma8fragment8blockDimEv) - Returns:
The leading block dimension (non-K)



-
static inline constexpr uint32_t kDim()
[#](#_CPPv4N7rocwmma8fragment4kDimEv) - Returns:
The k dimension



-
static inline constexpr uint32_t size()
[#](#_CPPv4N7rocwmma8fragment4sizeEv) - Returns:
The size of the unpacked elements vector




## rocWMMA enumeration[#](#rocwmma-enumeration)

### layout_t[#](#layout-t)

## rocWMMA API functions[#](#rocwmma-api-functions)

-
template<typename FragT, typename DataT>

void rocwmma::fill_fragment([FragT](#_CPPv4I00EN7rocwmma13fill_fragmentEvR5FragT5DataT)&frag,[DataT](#_CPPv4I00EN7rocwmma13fill_fragmentEvR5FragT5DataT)value)[#](#_CPPv4I00EN7rocwmma13fill_fragmentEvR5FragT5DataT) Fills the entire fragment with the desired value.

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout**value**– Fill value of type DataT

- Template Parameters:
**FragT**– Opaque fragment type**DataT**– Datatype



-
template<typename FragT, typename DataT>

void rocwmma::load_matrix_sync([FragT](#_CPPv4I00EN7rocwmma16load_matrix_syncEvR5FragTPK5DataT8uint32_t)&frag, const[DataT](#_CPPv4I00EN7rocwmma16load_matrix_syncEvR5FragTPK5DataT8uint32_t)*data, uint32_t ldm)[#](#_CPPv4I00EN7rocwmma16load_matrix_syncEvR5FragTPK5DataT8uint32_t) Loads the entire fragment from the data pointer according to its matrix and data layout contexts. Data pointer may point to either local or global memory.

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout**data**– Data pointer to global or local memory**ldm**– Leading dimension size

- Template Parameters:
**FragT**– Opaque fragment type**DataT**– Datatype



-
template<typename FragT, typename DataT>

void rocwmma::load_matrix_sync([FragT](#_CPPv4I00EN7rocwmma16load_matrix_syncEvR5FragTPK5DataT8uint32_t8layout_t)&frag, const[DataT](#_CPPv4I00EN7rocwmma16load_matrix_syncEvR5FragTPK5DataT8uint32_t8layout_t)*data, uint32_t ldm,[layout_t](#_CPPv4N7rocwmma8layout_tE)layout)[#](#_CPPv4I00EN7rocwmma16load_matrix_syncEvR5FragTPK5DataT8uint32_t8layout_t) Loads the entire fragment from the data pointer according to its matrix layout and data layout contexts. Data pointer may point to either local or global memory. This overload provides manual selection of data layout of the incoming memory pointer, which will be transformed to conform to the data layout of the fragment.

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout**data**– Data pointer to global/local memory**ldm**– Leading dimension size**layout**– Data layout

- Template Parameters:
**FragT**– Opaque fragment type**DataT**– Datatype



-
template<typename FragT, typename DataT>

void rocwmma::store_matrix_sync([DataT](#_CPPv4I00EN7rocwmma17store_matrix_syncEvP5DataTRK5FragT8uint32_t)*data,[FragT](#_CPPv4I00EN7rocwmma17store_matrix_syncEvP5DataTRK5FragT8uint32_t)const &frag, uint32_t ldm)[#](#_CPPv4I00EN7rocwmma17store_matrix_syncEvP5DataTRK5FragT8uint32_t) Stores the entire fragment to the data pointer according to its matrix and data layouts. Data pointer may point to either local or global memory.

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout**data**– Data pointer to global/local memory**ldm**– Leading dimension size

- Template Parameters:
**FragT**– Opaque fragment type**DataT**– Datatype



-
template<typename FragT, typename DataT>

void rocwmma::store_matrix_sync([DataT](#_CPPv4I00EN7rocwmma17store_matrix_syncEvP5DataTRK5FragT8uint32_t8layout_t)*data,[FragT](#_CPPv4I00EN7rocwmma17store_matrix_syncEvP5DataTRK5FragT8uint32_t8layout_t)const &frag, uint32_t ldm,[layout_t](#_CPPv4N7rocwmma8layout_tE)layout)[#](#_CPPv4I00EN7rocwmma17store_matrix_syncEvP5DataTRK5FragT8uint32_t8layout_t) Stores the entire fragment to the data pointer according to its matrix layout and data layout contexts. Data pointer may point to either local or global memory. This overload provides manual selection of data layout of the outgoing memory pointer, which the data layout of the fragment will be transformed to.

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout**data**– Data pointer to global/local memory**ldm**– Leading dimension size**layout**– Data layout

- Template Parameters:
**FragT**– Opaque fragment type**DataT**– Datatype



-
template<typename FragA, typename FragB, typename FragAccumIn, typename FragAccumOut>

void rocwmma::mma_sync([FragAccumOut](#_CPPv4I0000EN7rocwmma8mma_syncEvR12FragAccumOutRK5FragARK5FragBR11FragAccumIn)&d,[FragA](#_CPPv4I0000EN7rocwmma8mma_syncEvR12FragAccumOutRK5FragARK5FragBR11FragAccumIn)const &a,[FragB](#_CPPv4I0000EN7rocwmma8mma_syncEvR12FragAccumOutRK5FragARK5FragBR11FragAccumIn)const &b,[FragAccumIn](#_CPPv4I0000EN7rocwmma8mma_syncEvR12FragAccumOutRK5FragARK5FragBR11FragAccumIn)&c)[#](#_CPPv4I0000EN7rocwmma8mma_syncEvR12FragAccumOutRK5FragARK5FragBR11FragAccumIn) Performs the Multiply-Accumulate operation on the fragments A, B, C and D (D = A * B + C)

Note

Frag c = d is valid

- Parameters:
**d**– Accumulator output D**a**– Input fragment A**b**– Input fragment B**c**– Input accumulator fragment C

- Template Parameters:
**FragA**– Opaque fragment type for matrix A data**FragB**– Opaque fragment type for matrix A data**FragAccumIn**– Opaque fragment type for input accumulation data**FragAccumOut**– Opaque fragment type for output accumulation data



-
void rocwmma::synchronize_workgroup()
[#](#_CPPv4N7rocwmma21synchronize_workgroupEv) Synchronization point for all wavefronts in a workgroup. Guarantees pending reads / writes to LDS are flushed.


### rocWMMA transforms API functions[#](#rocwmma-transforms-api-functions)

-
template<typename FragT>

static inline T rocwmma::apply_transpose([FragT](#_CPPv4I0EN7rocwmma15apply_transposeE1TRR5FragT)&&frag)[#](#_CPPv4I0EN7rocwmma15apply_transposeE1TRR5FragT) Applies the transpose transform the input fragment. Transpose is defined as orthogonal matrix and data layout. E.g. T(fragment<matrix_a, BlockM, BlockN, BlockK, DataT, row_major>) = fragment<matrix_b, BlockN, BlockM, BlockK, DataT, col_major>

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout- Template Parameters:
**FragT**– The incoming fragment type- Returns:
Transposed (orthogonal) fragment



-
template<typename DataLayoutT, typename FragT>

static inline T rocwmma::apply_data_layout([FragT](#_CPPv4I00EN7rocwmma17apply_data_layoutE1TRR5FragT)&&frag)[#](#_CPPv4I00EN7rocwmma17apply_data_layoutE1TRR5FragT) Transforms the input fragment to have the desired data layout.

- Parameters:
**frag**– Fragment of type MatrixT with its associated block sizes, data type and layout- Template Parameters:
**DataLayoutT**– The desired fragment data layout to apply**FragT**– The incoming fragment type

- Returns:
Fragment with transformed data layout



-
template<typename DstFragT, typename FragT>

static inline T rocwmma::apply_fragment([FragT](#_CPPv4I00EN7rocwmma14apply_fragmentE1TRR5FragT)&&frag)[#](#_CPPv4I00EN7rocwmma14apply_fragmentE1TRR5FragT) Transforms the input fragment to the target fragment type. This could include changing matrix context and/or changing data layout, as long as there is a path from the source register layout to the destination register layout.

- Parameters:
**frag**– Source fragment of type MatrixT with its associated block sizes, data type and layout- Template Parameters:
**DstFragT**– The target fragment type to transform to**FragT**– The source incoming fragment type

- Returns:
Target fragment after transformation



-
template<typename FragT>

static inline T rocwmma::to_register_file([FragT](#_CPPv4I0EN7rocwmma16to_register_fileE1TRR5FragT)&&frag)[#](#_CPPv4I0EN7rocwmma16to_register_fileE1TRR5FragT) Transforms the input fragment to a “register file” fragment type. Register contents are directly mapped to a 2D matrix space represented by [RegCount x WaveSize]. This transform is a geometry reinterpretation.

- Parameters:
**frag**– Source fragment of type MatrixT with its associated block sizes, data type and layout- Template Parameters:
**FragT**– The source incoming fragment type- Returns:
Target fragment after transformation



-
template<typename DstFragT, typename FragT>

static inline T rocwmma::from_register_file([FragT](#_CPPv4I00EN7rocwmma18from_register_fileE1TRR5FragT)&&frag)[#](#_CPPv4I00EN7rocwmma18from_register_fileE1TRR5FragT) Transforms the “register file” fragment type to a target fragment type. Register contents are directly mapped to a 2D matrix space represented by [RegCount x WaveSize]. This transform is a geometry reinterpretation.

- Parameters:
**frag**– Source fragment of type MatrixT with its associated block sizes, data type and layout- Template Parameters:
**DstFragT**– The target frag to transform to**FragT**– The source incoming fragment type as register file

- Returns:
Fragment after transformation



## Sample programs[#](#sample-programs)

A sample demonstrating the use of rocWMMA functions `load_matrix_sync`

, `store_matrix_sync`

, `fill_fragment`

, and `mma_sync`

is available [here](https://github.com/ROCm/rocm-libraries/blob/develop/projects/rocwmma/samples/simple_hgemm.cpp).
For more sample programs, refer to the [samples directory](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocwmma/samples).

## Emulation tests[#](#emulation-tests)

The emulation test is a smaller test suite designed for emulators. It includes a subset of ROCWMMA test cases for faster execution on emulated platforms. It supports `smoke`

, `regression`

, and `extended`

modes.

For example, to run a smoke test:

```
--install_dir <build_dir> --emulation smoke
```
