---
title: "rocPRIM intrinsics &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/intrinsics.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:28:34.208507+00:00
content_hash: "98bf55ee8d210c7e"
---

# rocPRIM intrinsics[#](#rocprim-intrinsics)

## Bitwise[#](#bitwise)

-
__device__ inline int rocprim::get_bit(int x, int i)
[#](#_CPPv4N7rocprim7get_bitEii) Returns a single bit at ‘i’ from ‘x’.


-
__device__ inline unsigned int rocprim::bit_count(unsigned int x)
[#](#_CPPv4N7rocprim9bit_countEj) Bit count.

Returns the number of bit of

`x`

set.

-
__device__ inline unsigned int rocprim::bit_count(unsigned long long x)
[#](#_CPPv4N7rocprim9bit_countEy) Bit count.

Returns the number of bit of

`x`

set.

-
__host__ __device__ inline unsigned int rocprim::ctz(unsigned int x)
[#](#_CPPv4N7rocprim3ctzEj) Count trailing zeroes.

Count the number of consecutive 0-bits, starting from the least significant bit.

`x`

must be non-zero.

-
__host__ __device__ inline unsigned int rocprim::ctz(unsigned long long x)
[#](#_CPPv4N7rocprim3ctzEy) Count trailing zeroes.

Count the number of consecutive 0-bits, starting from the least significant bit.

`x`

must be non-zero.

## Warp size[#](#warp-size)

-
__host__ inline hipError_t rocprim::host_warp_size(const int device_id, unsigned int &warp_size)
[#](#_CPPv4N7rocprim14host_warp_sizeEKiRj) Returns a number of threads in a hardware warp for the actual device. At host side this constant is available at runtime only.

It is constant for a device.

- Parameters:
**device_id**– the device that should be queried.**warp_size**– out parameter for the warp size.

- Returns:
hipError_t any error that might occur.



-
__host__ inline hipError_t rocprim::host_warp_size(const hipStream_t stream, unsigned int &warp_size)
[#](#_CPPv4N7rocprim14host_warp_sizeEK11hipStream_tRj) Returns the number of threads in a hardware warp for the device associated with the stream. At host side this constant is available at runtime only.

It is constant for a device.

- Parameters:
**stream**– the stream, whose device should be queried.**warp_size**– out parameter for the warp size.

- Returns:
hipError_t any error that might occur.



## Lane and Warp ID[#](#lane-and-warp-id)

-
__device__ inline unsigned int warp_id()
[#](#_CPPv47warp_idv) Returns warp id in a block (tile).


## Flat ID[#](#flat-id)

-
__device__ inline unsigned int flat_block_thread_id()
[#](#_CPPv420flat_block_thread_idv) Returns flat (linear, 1D) thread identifier in a multidimensional block (tile).


-
__device__ inline unsigned int flat_block_id()
[#](#_CPPv413flat_block_idv) Returns flat (linear, 1D) block identifier in a multidimensional grid.


## Flat Size[#](#flat-size)

-
__device__ inline unsigned int rocprim::flat_block_size()
[#](#_CPPv4N7rocprim15flat_block_sizeEv) Returns flat size of a multidimensional block (tile).


-
__device__ inline unsigned int rocprim::flat_tile_size()
[#](#_CPPv4N7rocprim14flat_tile_sizeEv) Returns flat size of a multidimensional tile (block).


## Synchronization[#](#synchronization)

-
__device__ inline void rocprim::syncthreads()
[#](#_CPPv4N7rocprim11syncthreadsEv) Synchronize all threads in a block (tile)


-
__device__ inline void rocprim::wave_barrier()
[#](#_CPPv4N7rocprim12wave_barrierEv) Synchronize all threads in the wavefront.

Wait for all threads in the wavefront before continuing execution. Memory ordering is guaranteed by this function between threads in the same wavefront. Threads can communicate by storing to global / shared memory, executing

[wave_barrier()](#group__intrinsicsmodule_1ga921b41dd37b3b12241a880a40d2afb58)then reading values stored by other threads in the same wavefront.[wave_barrier()](#group__intrinsicsmodule_1ga921b41dd37b3b12241a880a40d2afb58)should be executed by all threads in the wavefront in convergence, this means that if the function is executed in a conditional statement all threads in the wave must enter the conditional statement.Note

On SIMT architectures all lanes come to a convergence point simultaneously, thus no special instruction is needed in the ISA.


## Active threads[#](#active-threads)

-
__device__ inline lane_mask_type rocprim::ballot(int predicate)
[#](#_CPPv4N7rocprim6ballotEi) Evaluate predicate for all active work-items in the warp and return an integer whose

`i`

-th bit is set if and only if`predicate`

is`true`

for the`i`

-th thread of the warp and the`i`

-th thread is active.- Parameters:
**predicate**– input to be evaluated for all active lanes


-
__device__ inline bool rocprim::group_elect(lane_mask_type mask)
[#](#_CPPv4N7rocprim11group_electE14lane_mask_type) Elect a single lane for each group in

`mask`

.- Parameters:
**mask**–**[in]**bit mask of the lanes in the same group as the calling lane. The`i`

-th bit should be set if lane`i`

is in the same group as the calling lane.- Returns:
`true`

for one unspecified lane in the`mask`

, false for everyone else. Returns`false`

for all lanes not in any group, that is lanes passing 0 as`mask`

.- Pre:
The relation specified by

`mask`

must be symmetric and transitive, in other words: the groups should be consistent between threads.


-
__device__ inline unsigned int rocprim::masked_bit_count(lane_mask_type x, unsigned int add = 0)
[#](#_CPPv4N7rocprim16masked_bit_countE14lane_mask_typej) Masked bit count.

For each thread, this function returns the number of active threads which have

`i`

-th bit of`x`

set and come before the current thread.

-
template<unsigned int LabelBits>

__device__ inline lane_mask_type rocprim::match_any(unsigned int label, bool valid = true)[#](#_CPPv4I_jEN7rocprim9match_anyE14lane_mask_typejb) Group active lanes having the same bits of

`label`

.Threads that have the same least significant

`LabelBits`

bits are grouped into the same group. Every lane in the warp receives a mask of all active lanes participating in its group.- Template Parameters:
**LabelBits**– number of bits to compare between labels- Parameters:
**label**–**[in]**the label for the calling lane**valid**–**[in]**lanes passing`false`

will be ignored for comparisons, such lanes will not be part of any group, and will always return an empty mask (0)

- Returns:
A bit mask of lanes sharing the same bits for

`label`

. The bit at index lane`i`

’s result includes bit`j`

in the lane mask if lane`j`

is part of the same group as lane`i`

, i.e. lane`i`

and`j`

called with the same value for label.


-
__device__ inline lane_mask_type rocprim::match_any(unsigned int label, unsigned int label_bits, bool valid = true)
[#](#_CPPv4N7rocprim9match_anyEjjb) Group active lanes having the same bits of

`label`

.This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.

Threads that have the same least significant

`label_bits`

bits are grouped into the same group. Every lane in the warp receives a mask of all active lanes participating in its group.This overload does not accept a template parameter for label bits. It is passed as a function parameter instead.

- Parameters:
**label**–**[in]**the label for the calling lane**label_bits**–**[in]**number of bits to compare between labels**valid**–**[in]**lanes passing`false`

will be ignored for comparisons, such lanes will not be part of any group, and will always return an empty mask (0)

- Returns:
A bit mask of lanes sharing the same bits for

`label`

. The bit at index lane`i`

’s result includes bit`j`

in the lane mask if lane`j`

is part of the same group as lane`i`

, i.e. lane`i`

and`j`

called with the same value for label.
