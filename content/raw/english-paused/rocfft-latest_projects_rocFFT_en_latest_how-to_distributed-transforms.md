---
title: "Distributed transforms &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/how-to/distributed-transforms.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:07:09.795350+00:00
content_hash: "19c07ddc3fee1b30"
---

# Distributed transforms[#](#distributed-transforms)

rocFFT can optionally distribute FFTs across multiple devices in a
single process or across multiple Message Passing Interface (MPI) ranks. To perform distributed
transforms, describe the input and output data layouts
as [fields](working-with-rocfft.html#input-output-fields).

## Multiple devices in a single process[#](#multiple-devices-in-a-single-process)

A transform can be distributed across multiple devices in a single
process by passing distinct device IDs to
[ rocfft_brick_create()](../reference/allapi.html#_CPPv419rocfft_brick_createP12rocfft_brickPK6size_tPK6size_tPK6size_t6size_ti) to create bricks in the input and output
fields.

Support for single-process multi-device transforms was introduced in ROCm 6.0 with rocFFT 1.0.25.

## Message Passing Interface[#](#message-passing-interface)

MPI lets you distribute the transform across multiple processes, organized into MPI ranks.

To turn on rocFFT MPI support, enable the `ROCFFT_MPI_ENABLE`

CMake option
when building the library. By default, this option
is off. To use Cray MPI, enable the `ROCFFT_CRAY_MPI_ENABLE`

CMake option.

Additionally, rocFFT MPI support requires a GPU-aware MPI library that supports transferring data to and from HIP devices.

Support for MPI transforms was introduced in ROCm 6.3 with rocFFT 1.0.29.

Note

rocFFT API calls made on different ranks might return different values. Application developers must ensure that all ranks have successfully created their plans before attempting to execute a distributed transform. One rank can fail to create or execute a plan while the others succeed.

To distribute a transform across multiple MPI ranks, the following additional steps are required:

Each rank calls

to add an MPI communicator to an allocated plan description. rocFFT distributes the computation across all ranks in the communicator.`rocfft_plan_description_set_comm()`

Each rank allocates the same fields and calls

and`rocfft_plan_description_add_infield()`

on the plan description. However, each rank must only call`rocfft_plan_description_add_outfield()`

and`rocfft_brick_create()`

for bricks that reside on that rank. A brick resides on exactly one rank. Each rank can have zero or more bricks associated to it.`rocfft_field_add_brick()`

Each rank in the communicator calls

. rocFFT then uses this information to distribute the supplied brick information between all of the ranks.`rocfft_plan_create()`

Each rank in the communicator calls

. This function accepts arrays of pointers for input and output. The arrays contain pointers to each brick in the input or output of the current rank.`rocfft_execute()`

The pointers must be provided in the same order in which the bricks were added to the field (using calls to

) and must point to the memory on the device that was specified at that time.`rocfft_field_add_brick()`

For in-place transforms, only pass the input pointers and use an empty array of output pointers.
