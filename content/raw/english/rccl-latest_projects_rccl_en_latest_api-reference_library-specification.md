---
title: "RCCL library specification &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/api-reference/library-specification.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:45.141081+00:00
content_hash: "f0fd6c0deb5cabf8"
---

# RCCL library specification[#](#rccl-library-specification)

This document provides details of the API library.

## Communicator functions[#](#communicator-functions)

-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclGetUniqueId([ncclUniqueId](api-library.html#_CPPv412ncclUniqueId)*uniqueId) Generates an ID for ncclCommInitRank.

Generates an ID to be used in ncclCommInitRank. ncclGetUniqueId should be called once by a single rank and the ID should be distributed to all ranks in the communicator before using it as a parameter for ncclCommInitRank.

- Parameters:
**uniqueId**–**[out]**Pointer to where uniqueId will be stored- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommInitRank([ncclComm_t](api-library.html#_CPPv410ncclComm_t)*comm, int nranks,[ncclUniqueId](api-library.html#_CPPv412ncclUniqueId)commId, int rank) Creates a new communicator (multi thread/process version).

Rank must be between 0 and nranks-1 and unique within a communicator clique. Each rank is associated to a CUDA device, which has to be set before calling ncclCommInitRank. ncclCommInitRank implicitly syncronizes with other ranks, so it must be called by different threads/processes or use ncclGroupStart/ncclGroupEnd.

- Parameters:
**comm**–**[out]**Pointer to created communicator**nranks**–**[in]**Total number of ranks participating in this communicator**commId**–**[in]**UniqueId required for initialization**rank**–**[in]**Current rank to create communicator for

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommInitAll([ncclComm_t](api-library.html#_CPPv410ncclComm_t)*comm, int ndev, const int *devlist) Creates a clique of communicators (single process version).

This is a convenience function to create a single-process communicator clique. Returns an array of ndev newly initialized communicators in comm. comm should be pre-allocated with size at least ndev*sizeof(ncclComm_t). If devlist is NULL, the first ndev HIP devices are used. Order of devlist defines user-order of processors within the communicator.

- Parameters:
**comm**–**[out]**Pointer to array of created communicators**ndev**–**[in]**Total number of ranks participating in this communicator**devlist**–**[in]**Array of GPU device indices to create for

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommDestroy([ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm) Frees local resources associated with communicator object.

Destroy all local resources associated with the passed in communicator object

- Parameters:
**comm**–**[in]**Communicator to destroy- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommAbort([ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm) Abort any in-progress calls and destroy the communicator object.

Frees resources associated with communicator object and aborts any operations that might still be running on the device.

- Parameters:
**comm**–**[in]**Communicator to abort and destroy- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommCount(const[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, int *count) Gets the number of ranks in the communicator clique.

Returns the number of ranks in the communicator clique (as set during initialization)

- Parameters:
**comm**–**[in]**Communicator to query**count**–**[out]**Pointer to where number of ranks will be stored

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommCuDevice(const[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, int *device) Get the ROCm device index associated with a communicator.

Returns the ROCm device number associated with the provided communicator.

- Parameters:
**comm**–**[in]**Communicator to query**device**–**[out]**Pointer to where the associated ROCm device index will be stored

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclCommUserRank(const[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, int *rank) Get the rank associated with a communicator.

Returns the user-ordered “rank” associated with the provided communicator.

- Parameters:
**comm**–**[in]**Communicator to query**rank**–**[out]**Pointer to where the associated rank will be stored

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


## Collective communication operations[#](#collective-communication-operations)

Collective communication operations must be called separately for each communicator in a communicator clique.

They return when operations have been enqueued on the hipstream.

Since they may perform inter-CPU synchronization, each call has to be done from a different thread or process, or need to use Group Semantics (see below).

-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclReduce(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](api-library.html#_CPPv411ncclRedOp_t)op, int root,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Reduce.

Reduces data arrays of length

*count*in*sendbuff*into*recvbuff*using*op*operation. recvbuff* may be NULL on all calls except for root device. root* is the rank (not the HIP device) where data will reside after the operation is complete. In-place operation will happen if sendbuff == recvbuff.- Parameters:
**sendbuff**–**[in]**Local device data buffer to be reduced**recvbuff**–**[out]**Data buffer where result is stored (only for*root*rank). May be null for other ranks.**count**–**[in]**Number of elements in every send buffer**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator type**root**–**[in]**Rank where result data array will be stored**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclBcast(void *buff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) (Deprecated) Broadcast (in-place)

Copies

*count*values from*root*to all other devices. root is the rank (not the CUDA device) where data resides before the operation is started. This operation is implicitly in-place.- Parameters:
**buff**–**[inout]**Input array on*root*to be copied to other ranks. Output array for all ranks.**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank owning buffer to be copied to others**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclBroadcast(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Broadcast.

Copies

*count*values from*sendbuff*on*root*to*recvbuff*on all devices. root* is the rank (not the HIP device) where data resides before the operation is started. sendbuff* may be NULL on ranks other than*root*. In-place operation will happen if*sendbuff*==*recvbuff*.- Parameters:
**sendbuff**–**[in]**Data array to copy (if*root*). May be NULL for other ranks**recvbuff**–**[in]**Data array to store received array**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank of broadcast root**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclAllReduce(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](api-library.html#_CPPv411ncclRedOp_t)op,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) All-Reduce.

Reduces data arrays of length

*count*in*sendbuff*using*op*operation, and leaves identical copies of result on each*recvbuff*. In-place operation will happen if sendbuff == recvbuff.- Parameters:
**sendbuff**–**[in]**Input data array to reduce**recvbuff**–**[out]**Data array to store reduced result array**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclReduceScatter(const void *sendbuff, void *recvbuff, size_t recvcount,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](api-library.html#_CPPv411ncclRedOp_t)op,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Reduce-Scatter.

Reduces data in

*sendbuff*using*op*operation and leaves reduced result scattered over the devices so that*recvbuff*on rank i will contain the i-th block of the result. Assumes sendcount is equal to nranks*recvcount, which means that*sendbuff*should have a size of at least nranks*recvcount elements. In-place operations will happen if recvbuff == sendbuff + rank * recvcount.- Parameters:
**sendbuff**–**[in]**Input data array to reduce**recvbuff**–**[out]**Data array to store reduced result subarray**recvcount**–**[in]**Number of elements each rank receives**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclAllGather(const void *sendbuff, void *recvbuff, size_t sendcount,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) All-Gather.

Each device gathers

*sendcount*values from other GPUs into*recvbuff*, receiving data from rank i at offset i*sendcount. Assumes recvcount is equal to nranks*sendcount, which means that recvbuff should have a size of at least nranks*sendcount elements. In-place operations will happen if sendbuff == recvbuff + rank * sendcount.- Parameters:
**sendbuff**–**[in]**Input data array to send**recvbuff**–**[out]**Data array to store the gathered result**sendcount**–**[in]**Number of elements each rank sends**datatype**–**[in]**Data buffer element datatype**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclSend(const void *sendbuff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype, int peer,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Send.

Send data from

*sendbuff*to rank*peer*. Rank*peer*needs to call ncclRecv with the same*datatype*and the same*count*as this rank. This operation is blocking for the GPU. If multiple ncclSend and ncclRecv operations need to progress concurrently to complete, they must be fused within a ncclGroupStart / ncclGroupEnd section.- Parameters:
**sendbuff**–**[in]**Data array to send**count**–**[in]**Number of elements to send**datatype**–**[in]**Data buffer element datatype**peer**–**[in]**Peer rank to send to**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclRecv(void *recvbuff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype, int peer,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Receive.

Receive data from rank

*peer*into*recvbuff*. Rank*peer*needs to call ncclSend with the same datatype and the same count as this rank. This operation is blocking for the GPU. If multiple ncclSend and ncclRecv operations need to progress concurrently to complete, they must be fused within a ncclGroupStart/ ncclGroupEnd section.- Parameters:
**recvbuff**–**[out]**Data array to receive**count**–**[in]**Number of elements to receive**datatype**–**[in]**Data buffer element datatype**peer**–**[in]**Peer rank to send to**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclGather(const void *sendbuff, void *recvbuff, size_t sendcount,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Gather.

Root device gathers

*sendcount*values from other GPUs into*recvbuff*, receiving data from rank i at offset i*sendcount. Assumes recvcount is equal to nranks*sendcount, which means that*recvbuff*should have a size of at least nranks*sendcount elements. In-place operations will happen if sendbuff == recvbuff + rank * sendcount. recvbuff* may be NULL on ranks other than*root*.- Parameters:
**sendbuff**–**[in]**Data array to send**recvbuff**–**[out]**Data array to receive into on*root*.**sendcount**–**[in]**Number of elements to send per rank**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank that receives data from all other ranks**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclScatter(const void *sendbuff, void *recvbuff, size_t recvcount,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) Scatter.

Scattered over the devices so that recvbuff on rank i will contain the i-th block of the data on root. Assumes sendcount is equal to nranks*recvcount, which means that

*sendbuff*should have a size of at least nranks*recvcount elements. In-place operations will happen if recvbuff == sendbuff + rank * recvcount.- Parameters:
**sendbuff**–**[in]**Data array to send (on*root*rank). May be NULL on other ranks.**recvbuff**–**[out]**Data array to receive partial subarray into**recvcount**–**[in]**Number of elements to receive per rank**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank that scatters data to all other ranks**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclAllToAll(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](api-library.html#_CPPv414ncclDataType_t)datatype,[ncclComm_t](api-library.html#_CPPv410ncclComm_t)comm, hipStream_t stream) All-To-All.

Device (i) send (j)th block of data to device (j) and be placed as (i)th block. Each block for sending/receiving has

*count*elements, which means that*recvbuff*and*sendbuff*should have a size of nranks*count elements. In-place operation is NOT supported. It is the user’s responsibility to ensure that sendbuff and recvbuff are distinct.- Parameters:
**sendbuff**–**[in]**Data array to send (contains blocks for each other rank)**recvbuff**–**[out]**Data array to receive (contains blocks from each other rank)**count**–**[in]**Number of elements to send between each pair of ranks**datatype**–**[in]**Data buffer element datatype**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


## Group semantics[#](#group-semantics)

When managing multiple GPUs from a single thread, and since NCCL collective calls may perform inter-CPU synchronization, we need to “group” calls for different ranks/devices into a single call.

Grouping NCCL calls as being part of the same collective operation is done using ncclGroupStart and ncclGroupEnd. ncclGroupStart will enqueue all collective calls until the ncclGroupEnd call, which will wait for all calls to be complete. Note that for collective communication, ncclGroupEnd only guarantees that the operations are enqueued on the streams, not that the operation is effectively done.

Both collective communication and ncclCommInitRank can be used in conjunction of ncclGroupStart/ncclGroupEnd.

-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclGroupStart() Group Start.

Start a group call. All calls to RCCL until ncclGroupEnd will be fused into a single RCCL operation. Nothing will be started on the HIP stream until ncclGroupEnd.

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclGroupEnd() Group End.

End a group call. Start a fused RCCL operation consisting of all calls since ncclGroupStart. Operations on the HIP stream depending on the RCCL operations need to be called after ncclGroupEnd.

- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


## Library functions[#](#library-functions)

-
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)ncclGetVersion(int *version) Return the RCCL_VERSION_CODE of RCCL in the supplied integer.

This integer is coded with the MAJOR, MINOR and PATCH level of RCCL.

- Parameters:
**version**–**[out]**Pointer to where version will be stored- Returns:
Result code. See

[Result Codes](api-library.html#group__rccl__result__code)for more details.


-
const char *ncclGetErrorString(
[ncclResult_t](api-library.html#_CPPv412ncclResult_t)result) Returns a string for each result code.

Returns a human-readable string describing the given result code.

- Parameters:
**result**–**[in]**Result code to get description for- Returns:
String containing description of result code.



## Types[#](#types)

There are few data structures that are internal to the library. The pointer types to these structures are given below. The user would need to use these types to create handles and pass them between different library functions.

-
typedef struct ncclComm *ncclComm_t
Opaque handle to communicator.

A communicator contains information required to facilitate collective communications calls


-
struct ncclUniqueId
Opaque unique id used to initialize communicators.

The

[ncclUniqueId](#structnccl_unique_id)must be passed to all participating ranks

## Enumerations[#](#enumerations)

This section provides all the enumerations used.

-
enum ncclResult_t
Result type.

Return codes aside from ncclSuccess indicate that a call has failed

*Values:*-
enumerator ncclSuccess
No error


-
enumerator ncclUnhandledCudaError
Unhandled HIP error


-
enumerator ncclSystemError
Unhandled system error


-
enumerator ncclInternalError
Internal Error - Please report to RCCL developers


-
enumerator ncclInvalidArgument
Invalid argument


-
enumerator ncclInvalidUsage
Invalid usage


-
enumerator ncclRemoteError
Remote process exited or there was a network error


-
enumerator ncclInProgress
RCCL operation in progress


-
enumerator ncclNumResults
Number of result types


-
enumerator ncclSuccess

-
enum ncclRedOp_t
Reduction operation selector.

Enumeration used to specify the various reduction operations ncclNumOps is the number of built-in ncclRedOp_t values and serves as the least possible value for dynamic ncclRedOp_t values constructed by ncclRedOpCreate functions.

ncclMaxRedOp is the largest valid value for ncclRedOp_t and is defined to be the largest signed value (since compilers are permitted to use signed enums) that won’t grow sizeof(ncclRedOp_t) when compared to previous RCCL versions to maintain ABI compatibility.

*Values:*-
enumerator ncclSum
Sum


-
enumerator ncclProd
Product


-
enumerator ncclMax
Max


-
enumerator ncclMin
Min


-
enumerator ncclAvg
Average


-
enumerator ncclNumOps
Number of built-in reduction ops


-
enumerator ncclMaxRedOp
Largest value for ncclRedOp_t


-
enumerator ncclSum

-
enum ncclDataType_t
Data types.

Enumeration of the various supported datatype

*Values:*-
enumerator ncclInt8

-
enumerator ncclChar

-
enumerator ncclUint8

-
enumerator ncclInt32

-
enumerator ncclInt

-
enumerator ncclUint32

-
enumerator ncclInt64

-
enumerator ncclUint64

-
enumerator ncclFloat16

-
enumerator ncclHalf

-
enumerator ncclFloat32

-
enumerator ncclFloat

-
enumerator ncclFloat64

-
enumerator ncclDouble

-
enumerator ncclBfloat16

-
enumerator ncclFloat8e4m3

-
enumerator ncclFloat8e5m2

-
enumerator ncclNumTypes

-
enumerator ncclInt8
