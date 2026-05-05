---
title: "rocPRIM data movement functions &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/block_ops/data_mov_funcs.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:17:20.261814+00:00
content_hash: "387f761726e09fa8"
---

# rocPRIM data movement functions[#](#rocprim-data-movement-functions)

API reference for rocPRIM data movement functions.

## Direct Blocked[#](#direct-blocked)

### Load[#](#load)

-
template<class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_load_direct_blocked(unsigned int flat_id,[InputIterator](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1T)block_input,[T](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1T) Loads data from continuous memory into a blocked arrangement of items across the thread block.

The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to



-
template<class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_load_direct_blocked(unsigned int flat_id,[InputIterator](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj)block_input,[T](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I00_jEN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj) Loads data from continuous memory into a blocked arrangement of items across the thread block, which is guarded by range

`valid`

.The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load



-
template<class InputIterator, class T, unsigned int ItemsPerThread, class Default>

__device__ inline void rocprim::block_load_direct_blocked(unsigned int flat_id,[InputIterator](#_CPPv4I00_j0EN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)block_input,[T](#_CPPv4I00_j0EN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)(&items)[[ItemsPerThread](#_CPPv4I00_j0EN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)], unsigned int valid,[Default](#_CPPv4I00_j0EN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)out_of_bounds)[#](#_CPPv4I00_j0EN7rocprim25block_load_direct_blockedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default) Loads data from continuous memory into a blocked arrangement of items across the thread block, which is guarded by range with a fall-back value for out-of-bound elements.

The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread**Default**– [inferred] The data type of the default value

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load**out_of_bounds**– default value assigned to out-of-bound items



### Store[#](#store)

-
template<class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_store_direct_blocked(unsigned int flat_id,[OutputIterator](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1T)block_output,[T](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1T) Stores a blocked arrangement of items from across the thread block into a blocked arrangement on continuous memory.

The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.- Template Parameters:
**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block



-
template<class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_store_direct_blocked(unsigned int flat_id,[OutputIterator](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1Tj)block_output,[T](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I00_jEN7rocprim26block_store_direct_blockedEvj14OutputIteratorRA14ItemsPerThread_1Tj) Stores a blocked arrangement of items from across the thread block into a blocked arrangement on continuous memory, which is guarded by range

`valid`

.The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.- Template Parameters:
**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block**valid**– maximum range of valid numbers to store



## Direct Blocked Vectorized[#](#direct-blocked-vectorized)

### Load[#](#id1)

-
template<class T, class U, unsigned int ItemsPerThread>

__device__ inline auto rocprim::block_load_direct_blocked_vectorized(unsigned int flat_id,[T](#_CPPv4I00_jEN7rocprim36block_load_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)*block_input,[U](#_CPPv4I00_jEN7rocprim36block_load_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)(&items)[[ItemsPerThread](#_CPPv4I00_jEN7rocprim36block_load_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)]) -> typename std::enable_if<detail::is_vectorizable<[T](#_CPPv4I00_jEN7rocprim36block_load_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U),[ItemsPerThread](#_CPPv4I00_jEN7rocprim36block_load_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)>::value>::type[#](#_CPPv4I00_jEN7rocprim36block_load_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U) Loads data from continuous memory into a blocked arrangement of items across the thread block.

The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.The input offset (

`block_input`

+ offset) must be quad-item aligned.The following conditions will prevent vectorization and switch to default block_load_direct_blocked:

`ItemsPerThread`

is odd.The datatype

`T`

is not a primitive or a HIP vector type (e.g. int2, int4, etc.)

The type

`T`

must be such that it can be implicitly converted to`U`

.- Template Parameters:
**T**– [inferred] the input data type**U**– [inferred] the output data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to



### Store[#](#id2)

-
template<class T, class U, unsigned int ItemsPerThread>

__device__ inline auto rocprim::block_store_direct_blocked_vectorized(unsigned int flat_id,[T](#_CPPv4I00_jEN7rocprim37block_store_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)*block_output,[U](#_CPPv4I00_jEN7rocprim37block_store_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)(&items)[[ItemsPerThread](#_CPPv4I00_jEN7rocprim37block_store_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)]) -> typename std::enable_if<detail::is_vectorizable<[T](#_CPPv4I00_jEN7rocprim37block_store_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U),[ItemsPerThread](#_CPPv4I00_jEN7rocprim37block_store_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U)>::value>::type[#](#_CPPv4I00_jEN7rocprim37block_store_direct_blocked_vectorizedENSt9enable_ifIN6detail15is_vectorizableI1T14ItemsPerThreadE5valueEE4typeEjP1TRA14ItemsPerThread_1U) Stores a blocked arrangement of items from across the thread block into a blocked arrangement on continuous memory.

The block arrangement is assumed to be (block-threads *

`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.The input offset (

`block_output`

+ offset) must be quad-item aligned.The following conditions will prevent vectorization and switch to default block_load_direct_blocked:

`ItemsPerThread`

is odd.The datatype

`T`

is not a primitive or a HIP vector type (e.g. int2, int4, etc.)

The type

`U`

must be such that it can be implicitly converted to`T`

.- Template Parameters:
**T**– [inferred] the output data type**U**– [inferred] the input data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to load from**items**– array that data is loaded to



## Direct Striped[#](#direct-striped)

### Load[#](#id3)

-
template<unsigned int BlockSize, class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_load_direct_striped(unsigned int flat_id,[InputIterator](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1T)block_input,[T](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1T) Loads data from continuous memory into a striped arrangement of items across the thread block.

The striped arrangement is assumed to be (

`BlockSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**BlockSize**– the number of threads in a block**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to



-
template<unsigned int BlockSize, class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_load_direct_striped(unsigned int flat_id,[InputIterator](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj)block_input,[T](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I_j00_jEN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj) Loads data from continuous memory into a striped arrangement of items across the thread block, which is guarded by range

`valid`

.The striped arrangement is assumed to be (

`BlockSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**BlockSize**– the number of threads in a block**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load



-
template<unsigned int BlockSize, class InputIterator, class T, unsigned int ItemsPerThread, class Default>

__device__ inline void rocprim::block_load_direct_striped(unsigned int flat_id,[InputIterator](#_CPPv4I_j00_j0EN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)block_input,[T](#_CPPv4I_j00_j0EN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)(&items)[[ItemsPerThread](#_CPPv4I_j00_j0EN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)], unsigned int valid,[Default](#_CPPv4I_j00_j0EN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default)out_of_bounds)[#](#_CPPv4I_j00_j0EN7rocprim25block_load_direct_stripedEvj13InputIteratorRA14ItemsPerThread_1Tj7Default) Loads data from continuous memory into a striped arrangement of items across the thread block, which is guarded by range with a fall-back value for out-of-bound elements.

The striped arrangement is assumed to be (

`BlockSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**BlockSize**– the number of threads in a block**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread**Default**– [inferred] The data type of the default value

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load**out_of_bounds**– default value assigned to out-of-bound items



### Store[#](#id4)

-
template<unsigned int BlockSize, class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_store_direct_striped(unsigned int flat_id,[OutputIterator](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1T)block_output,[T](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1T) Stores a striped arrangement of items from across the thread block into a blocked arrangement on continuous memory.

The striped arrangement is assumed to be (

`BlockSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.- Template Parameters:
**BlockSize**– the number of threads in a block**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block



-
template<unsigned int BlockSize, class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void rocprim::block_store_direct_striped(unsigned int flat_id,[OutputIterator](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1Tj)block_output,[T](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I_j00_jEN7rocprim26block_store_direct_stripedEvj14OutputIteratorRA14ItemsPerThread_1Tj) Stores a striped arrangement of items from across the thread block into a blocked arrangement on continuous memory, which is guarded by range

`valid`

.The striped arrangement is assumed to be (

`BlockSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.- Template Parameters:
**BlockSize**– the number of threads in a block**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block**valid**– maximum range of valid numbers to store



## Direct Warp Striped[#](#direct-warp-striped)

### Load[#](#id5)

-
template<unsigned int VirtualWaveSize, class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_load_direct_warp_striped(unsigned int flat_id,[InputIterator](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T)block_input,[T](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T) Loads data from continuous memory into a warp-striped arrangement of items across the thread block.

The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.The number of threads in the block must be a multiple of

`VirtualWaveSize`

.`VirtualWaveSize`

must be a power of two and equal or less than the size of hardware warp.Using

`VirtualWaveSize`

smaller than hardware warpsize could result in lower performance.

- Template Parameters:
**VirtualWaveSize**– [optional] the number of threads in a warp**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to



-
template<class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_load_direct_warp_striped(unsigned int flat_id,[InputIterator](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T)block_input,[T](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1T) Loads data from continuous memory into a warp-striped arrangement of items across the thread block, using the hardware warp size.

The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to



-
template<unsigned int VirtualWaveSize, class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_load_direct_warp_striped(unsigned int flat_id,[InputIterator](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj)block_input,[T](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I_j00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj) Loads data from continuous memory into a warp-striped arrangement of items across the thread block, which is guarded by range

`valid`

.The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.The number of threads in the block must be a multiple of

`VirtualWaveSize`

.`VirtualWaveSize`

must be a power of two and equal or less than the size of hardware warp.Using

`VirtualWaveSize`

smaller than hardware warpsize could result in lower performance.

- Template Parameters:
**VirtualWaveSize**– [optional] the number of threads in a warp**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load



-
template<class InputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_load_direct_warp_striped(unsigned int flat_id,[InputIterator](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj)block_input,[T](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I00_jE30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj) Loads data from continuous memory into a warp-striped arrangement of items across the thread block, which is guarded by range

`valid`

, using the hardware warp size.The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load



-
template<unsigned int VirtualWaveSize, class InputIterator, class T, unsigned int ItemsPerThread, class Default>

__device__ inline void block_load_direct_warp_striped(unsigned int flat_id,[InputIterator](#_CPPv4I_j00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)block_input,[T](#_CPPv4I_j00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)(&items)[[ItemsPerThread](#_CPPv4I_j00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)], unsigned int valid,[Default](#_CPPv4I_j00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)out_of_bounds)[#](#_CPPv4I_j00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default) Loads data from continuous memory into a warp-striped arrangement of items across the thread block, which is guarded by range with a fall-back value for out-of-bound elements.

The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.The number of threads in the block must be a multiple of

`VirtualWaveSize`

.`VirtualWaveSize`

must be a power of two and equal or less than the size of hardware warp.Using

`VirtualWaveSize`

smaller than hardware warpsize could result in lower performance.

- Template Parameters:
**VirtualWaveSize**– [optional] the number of threads in a warp**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread**Default**– [inferred] The data type of the default value

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load**out_of_bounds**– default value assigned to out-of-bound items



-
template<class InputIterator, class T, unsigned int ItemsPerThread, class Default>

__device__ inline void block_load_direct_warp_striped(unsigned int flat_id,[InputIterator](#_CPPv4I00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)block_input,[T](#_CPPv4I00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)(&items)[[ItemsPerThread](#_CPPv4I00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)], unsigned int valid,[Default](#_CPPv4I00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default)out_of_bounds)[#](#_CPPv4I00_j0E30block_load_direct_warp_stripedvj13InputIteratorRA14ItemsPerThread_1Tj7Default) Loads data from continuous memory into a warp-striped arrangement of items across the thread block, which is guarded by range with a fall-back value for out-of-bound elements, using the hardware warp size.

The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to load a range of`ItemsPerThread`

into`items`

.- Template Parameters:
**InputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread**Default**– [inferred] The data type of the default value

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_input**– the input iterator from the thread block to load from**items**– array that data is loaded to**valid**– maximum range of valid numbers to load**out_of_bounds**– default value assigned to out-of-bound items



### Store[#](#id6)

-
template<unsigned int VirtualWaveSize, class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_store_direct_warp_striped(unsigned int flat_id,[OutputIterator](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T)block_output,[T](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T) Stores a warp-striped arrangement of items from across the thread block into a blocked arrangement on continuous memory.

The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.The number of threads in the block must be a multiple of

`VirtualWaveSize`

.`VirtualWaveSize`

must be a power of two and equal or less than the size of hardware warp.Using

`VirtualWaveSize`

smaller than hardware warpsize could result in lower performance.

- Template Parameters:
**VirtualWaveSize**– [optional] the number of threads in a warp**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block



-
template<class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_store_direct_warp_striped(unsigned int flat_id,[OutputIterator](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T)block_output,[T](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T)(&items)[[ItemsPerThread](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T)])[#](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1T) Stores a warp-striped arrangement of items from across the thread block into a blocked arrangement on continuous memory, using the hardware warp size.

The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.- Template Parameters:
**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block



-
template<unsigned int VirtualWaveSize, class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_store_direct_warp_striped(unsigned int flat_id,[OutputIterator](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj)block_output,[T](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I_j00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj) Stores a warp-striped arrangement of items from across the thread block into a blocked arrangement on continuous memory, which is guarded by range

`valid`

.The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.The number of threads in the block must be a multiple of

`VirtualWaveSize`

.`VirtualWaveSize`

must be a power of two and equal or less than the size of hardware warp.Using

`VirtualWaveSize`

smaller than hardware warpsize could result in lower performance.

- Template Parameters:
**VirtualWaveSize**– [optional] the number of threads in a warp**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block**valid**– maximum range of valid numbers to store



-
template<class OutputIterator, class T, unsigned int ItemsPerThread>

__device__ inline void block_store_direct_warp_striped(unsigned int flat_id,[OutputIterator](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj)block_output,[T](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj)(&items)[[ItemsPerThread](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj)], unsigned int valid)[#](#_CPPv4I00_jE31block_store_direct_warp_stripedvj14OutputIteratorRA14ItemsPerThread_1Tj) Stores a warp-striped arrangement of items from across the thread block into a blocked arrangement on continuous memory, which is guarded by range

`valid`

, using the hardware warp size.The warp-striped arrangement is assumed to be (

`VirtualWaveSize`

*`ItemsPerThread`

) items across a thread block. Each thread uses a`flat_id`

to store a range of`ItemsPerThread`

`items`

to the thread block.- Template Parameters:
**OutputIterator**– [inferred] an iterator type for input (can be a simple pointer)**T**– [inferred] the data type**ItemsPerThread**– [inferred] the number of items to be processed by each thread

- Parameters:
**flat_id**– a local flat 1D thread id in a block (tile) for the calling thread**block_output**– the input iterator from the thread block to store to**items**– array that data is stored to thread block**valid**– maximum range of valid numbers to store
