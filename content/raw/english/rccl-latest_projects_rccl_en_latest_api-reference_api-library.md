---
title: "API library &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/api-reference/api-library.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:23:06.078310+00:00
content_hash: "3e24589114f4ac8b"
---

# API library[#](#api-library)

-
struct ncclConfig_t
[#](#_CPPv412ncclConfig_t) Communicator configuration.

Users can assign value to attributes to specify the behavior of a communicator

Public Members

-
size_t size
[#](#_CPPv4N12ncclConfig_t4sizeE) Should not be touched


-
unsigned int magic
[#](#_CPPv4N12ncclConfig_t5magicE) Should not be touched


-
unsigned int version
[#](#_CPPv4N12ncclConfig_t7versionE) Should not be touched


-
int blocking
[#](#_CPPv4N12ncclConfig_t8blockingE) Whether or not calls should block or not


-
int cgaClusterSize
[#](#_CPPv4N12ncclConfig_t14cgaClusterSizeE) Cooperative group array cluster size


-
int minCTAs
[#](#_CPPv4N12ncclConfig_t7minCTAsE) Minimum number of cooperative thread arrays (blocks)


-
int maxCTAs
[#](#_CPPv4N12ncclConfig_t7maxCTAsE) Maximum number of cooperative thread arrays (blocks)


-
const char *netName
[#](#_CPPv4N12ncclConfig_t7netNameE) Force NCCL to use a specfic network


Allow communicators to share resources


-
int trafficClass
[#](#_CPPv4N12ncclConfig_t12trafficClassE) Traffic class


-
const char *commName
[#](#_CPPv4N12ncclConfig_t8commNameE) Name of the communicator


-
int collnetEnable
[#](#_CPPv4N12ncclConfig_t13collnetEnableE) Check for collnet enablement


-
int CTAPolicy
[#](#_CPPv4N12ncclConfig_t9CTAPolicyE) CTA Policy


Shrink size


-
int nvlsCTAs
[#](#_CPPv4N12ncclConfig_t8nvlsCTAsE) Number of NVLS cooperative thread arrays (blocks)


-
size_t size

-
struct ncclSimInfo_t
[#](#_CPPv413ncclSimInfo_t)

-
struct ncclUniqueId
[#](#_CPPv412ncclUniqueId) Opaque unique id used to initialize communicators.

The

[ncclUniqueId](library-specification.html#structnccl_unique_id)must be passed to all participating ranks

-
*file*mainpage.txt

-
*file*nccl.h.in *#include <hip/hip_runtime.h>**#include <hip/hip_fp16.h>**#include <limits.h>*Defines

-
NCCL_H_
[#](#c.NCCL_H_)

-
NCCL_MAJOR
[#](#c.NCCL_MAJOR)

-
NCCL_MINOR
[#](#c.NCCL_MINOR)

-
NCCL_PATCH
[#](#c.NCCL_PATCH)

-
NCCL_SUFFIX
[#](#c.NCCL_SUFFIX)

-
NCCL_VERSION_CODE
[#](#c.NCCL_VERSION_CODE)

-
NCCL_VERSION(X, Y, Z)
[#](#c.NCCL_VERSION)

-
RCCL_BFLOAT16
[#](#c.RCCL_BFLOAT16)

-
RCCL_FLOAT8
[#](#c.RCCL_FLOAT8)

-
RCCL_GATHER_SCATTER
[#](#c.RCCL_GATHER_SCATTER)

-
RCCL_ALLTOALLV
[#](#c.RCCL_ALLTOALLV)

-
RCCL_ALLREDUCE_WITH_BIAS
[#](#c.RCCL_ALLREDUCE_WITH_BIAS)

-
NCCL_COMM_NULL
[#](#c.NCCL_COMM_NULL)

-
NCCL_UNIQUE_ID_BYTES
[#](#c.NCCL_UNIQUE_ID_BYTES)

-
NCCL_CONFIG_UNDEF_INT
[#](#c.NCCL_CONFIG_UNDEF_INT)

-
NCCL_CONFIG_UNDEF_PTR
[#](#c.NCCL_CONFIG_UNDEF_PTR)

-
NCCL_SPLIT_NOCOLOR
[#](#c.NCCL_SPLIT_NOCOLOR)

-
NCCL_UNDEF_FLOAT
[#](#c.NCCL_UNDEF_FLOAT)

-
NCCL_WIN_DEFAULT
[#](#c.NCCL_WIN_DEFAULT)

-
NCCL_WIN_COLL_SYMMETRIC
[#](#c.NCCL_WIN_COLL_SYMMETRIC)

-
NCCL_CTA_POLICY_DEFAULT
[#](#c.NCCL_CTA_POLICY_DEFAULT)

-
NCCL_CTA_POLICY_EFFICIENCY
[#](#c.NCCL_CTA_POLICY_EFFICIENCY)

-
NCCL_SHRINK_DEFAULT
[#](#c.NCCL_SHRINK_DEFAULT)

-
NCCL_SHRINK_ABORT
[#](#c.NCCL_SHRINK_ABORT)

-
NCCL_CONFIG_INITIALIZER
[#](#c.NCCL_CONFIG_INITIALIZER)

-
NCCL_SIM_INFO_INITIALIZER
[#](#c.NCCL_SIM_INFO_INITIALIZER)

Typedefs

-
typedef struct ncclComm *ncclComm_t
[#](#_CPPv410ncclComm_t) Opaque handle to communicator.

A communicator contains information required to facilitate collective communications calls


-
typedef struct ncclWindow *ncclWindow_t
[#](#_CPPv412ncclWindow_t)

-
typedef int mscclAlgoHandle_t
[#](#_CPPv417mscclAlgoHandle_t) Opaque handle to MSCCL algorithm.


Enums

-
enum ncclResult_t
[#](#_CPPv412ncclResult_t) Result type.

Return codes aside from ncclSuccess indicate that a call has failed

*Values:*-
enumerator ncclSuccess
[#](#_CPPv4N12ncclResult_t11ncclSuccessE) No error


-
enumerator ncclUnhandledCudaError
[#](#_CPPv4N12ncclResult_t22ncclUnhandledCudaErrorE) Unhandled HIP error


-
enumerator ncclSystemError
[#](#_CPPv4N12ncclResult_t15ncclSystemErrorE) Unhandled system error


-
enumerator ncclInternalError
[#](#_CPPv4N12ncclResult_t17ncclInternalErrorE) Internal Error - Please report to RCCL developers


-
enumerator ncclInvalidArgument
[#](#_CPPv4N12ncclResult_t19ncclInvalidArgumentE) Invalid argument


-
enumerator ncclInvalidUsage
[#](#_CPPv4N12ncclResult_t16ncclInvalidUsageE) Invalid usage


-
enumerator ncclRemoteError
[#](#_CPPv4N12ncclResult_t15ncclRemoteErrorE) Remote process exited or there was a network error


-
enumerator ncclInProgress
[#](#_CPPv4N12ncclResult_t14ncclInProgressE) RCCL operation in progress


-
enumerator ncclNumResults
[#](#_CPPv4N12ncclResult_t14ncclNumResultsE) Number of result types


-
enumerator ncclSuccess

-
enum ncclRedOp_dummy_t
[#](#_CPPv417ncclRedOp_dummy_t) Dummy reduction enumeration.

Dummy reduction enumeration used to determine value for ncclMaxRedOp

*Values:*-
enumerator ncclNumOps_dummy
[#](#_CPPv4N17ncclRedOp_dummy_t16ncclNumOps_dummyE)

-
enumerator ncclNumOps_dummy

-
enum ncclRedOp_t
[#](#_CPPv411ncclRedOp_t) Reduction operation selector.

Enumeration used to specify the various reduction operations ncclNumOps is the number of built-in ncclRedOp_t values and serves as the least possible value for dynamic ncclRedOp_t values constructed by ncclRedOpCreate functions.

ncclMaxRedOp is the largest valid value for ncclRedOp_t and is defined to be the largest signed value (since compilers are permitted to use signed enums) that won’t grow sizeof(ncclRedOp_t) when compared to previous RCCL versions to maintain ABI compatibility.

*Values:*-
enumerator ncclSum
[#](#_CPPv4N11ncclRedOp_t7ncclSumE) Sum


-
enumerator ncclProd
[#](#_CPPv4N11ncclRedOp_t8ncclProdE) Product


-
enumerator ncclMax
[#](#_CPPv4N11ncclRedOp_t7ncclMaxE) Max


-
enumerator ncclMin
[#](#_CPPv4N11ncclRedOp_t7ncclMinE) Min


-
enumerator ncclAvg
[#](#_CPPv4N11ncclRedOp_t7ncclAvgE) Average


-
enumerator ncclNumOps
[#](#_CPPv4N11ncclRedOp_t10ncclNumOpsE) Number of built-in reduction ops


-
enumerator ncclMaxRedOp
[#](#_CPPv4N11ncclRedOp_t12ncclMaxRedOpE) Largest value for ncclRedOp_t


-
enumerator ncclSum

-
enum ncclDataType_t
[#](#_CPPv414ncclDataType_t) Data types.

Enumeration of the various supported datatype

*Values:*-
enumerator ncclInt8
[#](#_CPPv4N14ncclDataType_t8ncclInt8E)

-
enumerator ncclChar
[#](#_CPPv4N14ncclDataType_t8ncclCharE)

-
enumerator ncclUint8
[#](#_CPPv4N14ncclDataType_t9ncclUint8E)

-
enumerator ncclInt32
[#](#_CPPv4N14ncclDataType_t9ncclInt32E)

-
enumerator ncclInt
[#](#_CPPv4N14ncclDataType_t7ncclIntE)

-
enumerator ncclUint32
[#](#_CPPv4N14ncclDataType_t10ncclUint32E)

-
enumerator ncclInt64
[#](#_CPPv4N14ncclDataType_t9ncclInt64E)

-
enumerator ncclUint64
[#](#_CPPv4N14ncclDataType_t10ncclUint64E)

-
enumerator ncclFloat16
[#](#_CPPv4N14ncclDataType_t11ncclFloat16E)

-
enumerator ncclHalf
[#](#_CPPv4N14ncclDataType_t8ncclHalfE)

-
enumerator ncclFloat32
[#](#_CPPv4N14ncclDataType_t11ncclFloat32E)

-
enumerator ncclFloat
[#](#_CPPv4N14ncclDataType_t9ncclFloatE)

-
enumerator ncclFloat64
[#](#_CPPv4N14ncclDataType_t11ncclFloat64E)

-
enumerator ncclDouble
[#](#_CPPv4N14ncclDataType_t10ncclDoubleE)

-
enumerator ncclBfloat16
[#](#_CPPv4N14ncclDataType_t12ncclBfloat16E)

-
enumerator ncclFloat8e4m3
[#](#_CPPv4N14ncclDataType_t14ncclFloat8e4m3E)

-
enumerator ncclFloat8e5m2
[#](#_CPPv4N14ncclDataType_t14ncclFloat8e5m2E)

-
enumerator ncclNumTypes
[#](#_CPPv4N14ncclDataType_t12ncclNumTypesE)

-
enumerator ncclInt8

-
enum ncclScalarResidence_t
[#](#_CPPv421ncclScalarResidence_t) Location and dereferencing logic for scalar arguments.

Enumeration specifying memory location of the scalar argument. Based on where the value is stored, the argument will be dereferenced either while the collective is running (if in device memory), or before the ncclRedOpCreate() function returns (if in host memory).

*Values:*-
enumerator ncclScalarDevice
[#](#_CPPv4N21ncclScalarResidence_t16ncclScalarDeviceE) Scalar is in device-visible memory


-
enumerator ncclScalarHostImmediate
[#](#_CPPv4N21ncclScalarResidence_t23ncclScalarHostImmediateE) Scalar is in host-visible memory


-
enumerator ncclScalarDevice

Functions

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclMemAlloc(void **ptr, size_t size)[#](#_CPPv412ncclMemAllocPPv6size_t)

-
[ncclResult_t](#_CPPv412ncclResult_t)pncclMemAlloc(void **ptr, size_t size)[#](#_CPPv413pncclMemAllocPPv6size_t)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclMemFree(void *ptr)[#](#_CPPv411ncclMemFreePv)

-
[ncclResult_t](#_CPPv412ncclResult_t)pncclMemFree(void *ptr)[#](#_CPPv412pncclMemFreePv)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclGetVersion(int *version)[#](#_CPPv414ncclGetVersionPi) Return the RCCL_VERSION_CODE of RCCL in the supplied integer.

This integer is coded with the MAJOR, MINOR and PATCH level of RCCL.

- Parameters:
**version**–**[out]**Pointer to where version will be stored- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclGetUniqueId([ncclUniqueId](#_CPPv412ncclUniqueId)*uniqueId)[#](#_CPPv415ncclGetUniqueIdP12ncclUniqueId) Generates an ID for ncclCommInitRank.

Generates an ID to be used in ncclCommInitRank. ncclGetUniqueId should be called once by a single rank and the ID should be distributed to all ranks in the communicator before using it as a parameter for ncclCommInitRank.

- Parameters:
**uniqueId**–**[out]**Pointer to where uniqueId will be stored- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommInitRankConfig([ncclComm_t](#_CPPv410ncclComm_t)*comm, int nranks,[ncclUniqueId](#_CPPv412ncclUniqueId)commId, int rank,[ncclConfig_t](#_CPPv412ncclConfig_t)*config)[#](#_CPPv422ncclCommInitRankConfigP10ncclComm_ti12ncclUniqueIdiP12ncclConfig_t) Create a new communicator with config.

Create a new communicator (multi thread/process version) with a configuration set by users. See

[Communicator Configuration](#group__rccl__config__type)for more details. Each rank is associated to a CUDA device, which has to be set before calling ncclCommInitRank.- Parameters:
**comm**–**[out]**Pointer to created communicator**nranks**–**[in]**Total number of ranks participating in this communicator**commId**–**[in]**UniqueId required for initialization**rank**–**[in]**Current rank to create communicator for. [0 to nranks-1]**config**–**[in]**Pointer to communicator configuration

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommInitRank([ncclComm_t](#_CPPv410ncclComm_t)*comm, int nranks,[ncclUniqueId](#_CPPv412ncclUniqueId)commId, int rank)[#](#_CPPv416ncclCommInitRankP10ncclComm_ti12ncclUniqueIdi) Creates a new communicator (multi thread/process version).

Rank must be between 0 and nranks-1 and unique within a communicator clique. Each rank is associated to a CUDA device, which has to be set before calling ncclCommInitRank. ncclCommInitRank implicitly syncronizes with other ranks, so it must be called by different threads/processes or use ncclGroupStart/ncclGroupEnd.

- Parameters:
**comm**–**[out]**Pointer to created communicator**nranks**–**[in]**Total number of ranks participating in this communicator**commId**–**[in]**UniqueId required for initialization**rank**–**[in]**Current rank to create communicator for

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommInitAll([ncclComm_t](#_CPPv410ncclComm_t)*comm, int ndev, const int *devlist)[#](#_CPPv415ncclCommInitAllP10ncclComm_tiPKi) Creates a clique of communicators (single process version).

This is a convenience function to create a single-process communicator clique. Returns an array of ndev newly initialized communicators in comm. comm should be pre-allocated with size at least ndev*sizeof(ncclComm_t). If devlist is NULL, the first ndev HIP devices are used. Order of devlist defines user-order of processors within the communicator.

- Parameters:
**comm**–**[out]**Pointer to array of created communicators**ndev**–**[in]**Total number of ranks participating in this communicator**devlist**–**[in]**Array of GPU device indices to create for

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommFinalize([ncclComm_t](#_CPPv410ncclComm_t)comm)[#](#_CPPv416ncclCommFinalize10ncclComm_t) Finalize a communicator.

ncclCommFinalize flushes all issued communications and marks communicator state as ncclInProgress. The state will change to ncclSuccess when the communicator is globally quiescent and related resources are freed; then, calling ncclCommDestroy can locally free the rest of the resources (e.g. communicator itself) without blocking.

- Parameters:
**comm**–**[in]**Communicator to finalize- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommDestroy([ncclComm_t](#_CPPv410ncclComm_t)comm)[#](#_CPPv415ncclCommDestroy10ncclComm_t) Frees local resources associated with communicator object.

Destroy all local resources associated with the passed in communicator object

- Parameters:
**comm**–**[in]**Communicator to destroy- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommAbort([ncclComm_t](#_CPPv410ncclComm_t)comm)[#](#_CPPv413ncclCommAbort10ncclComm_t) Abort any in-progress calls and destroy the communicator object.

Frees resources associated with communicator object and aborts any operations that might still be running on the device.

- Parameters:
**comm**–**[in]**Communicator to abort and destroy- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommSplit([ncclComm_t](#_CPPv410ncclComm_t)comm, int color, int key,[ncclComm_t](#_CPPv410ncclComm_t)*newcomm,[ncclConfig_t](#_CPPv412ncclConfig_t)*config)[#](#_CPPv413ncclCommSplit10ncclComm_tiiP10ncclComm_tP12ncclConfig_t) Create one or more communicators from an existing one.

Creates one or more communicators from an existing one. Ranks with the same color will end up in the same communicator. Within the new communicator, key will be used to order ranks. NCCL_SPLIT_NOCOLOR as color will indicate the rank will not be part of any group and will therefore return a NULL communicator. If config is NULL, the new communicator will inherit the original communicator’s configuration

- Parameters:
**comm**–**[in]**Original communicator object for this rank**color**–**[in]**Color to assign this rank**key**–**[in]**Key used to order ranks within the same new communicator**newcomm**–**[out]**Pointer to new communicator**config**–**[in]**Config file for new communicator. May be NULL to inherit from comm

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommShrink([ncclComm_t](#_CPPv410ncclComm_t)comm, int *excludeRanksList, int excludeRanksCount,[ncclComm_t](#_CPPv410ncclComm_t)*newcomm,[ncclConfig_t](#_CPPv412ncclConfig_t)*config, int shrinkFlags)[#](#_CPPv414ncclCommShrink10ncclComm_tPiiP10ncclComm_tP12ncclConfig_ti) Shrink existing communicator.

Ranks in excludeRanksList will be removed form the existing communicator. Within the new communicator, ranks will be re-ordered to fill the gap of removed ones. If config is NULL, the new communicator will inherit the original communicator’s configuration. The flag enables NCCL to adapt to various states of the parent communicator, see NCCL_SHRINK flags.

- Parameters:
**comm**–**[in]**Original communicator object for this rank**excludeRanksList**–**[in]**List of ranks to be exluded**excludeRanksCount**–**[in]**Number of ranks to be excluded**newcomm**–**[out]**Pointer to new communicator**config**–**[in]**Config file for new communicator. May be NULL to inherit from comm**shrinkFlags**–**[in]**Flag to adapt to various states of the parent communicator (see NCCL_SHRINK flags)

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)pncclCommShrink([ncclComm_t](#_CPPv410ncclComm_t)comm, int *excludeRanksList, int excludeRanksCount,[ncclComm_t](#_CPPv410ncclComm_t)*newcomm,[ncclConfig_t](#_CPPv412ncclConfig_t)*config, int shrinkFlags)[#](#_CPPv415pncclCommShrink10ncclComm_tPiiP10ncclComm_tP12ncclConfig_ti)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommInitRankScalable([ncclComm_t](#_CPPv410ncclComm_t)*newcomm, int nranks, int myrank, int nId,[ncclUniqueId](#_CPPv412ncclUniqueId)*commIds,[ncclConfig_t](#_CPPv412ncclConfig_t)*config)[#](#_CPPv424ncclCommInitRankScalableP10ncclComm_tiiiP12ncclUniqueIdP12ncclConfig_t) Creates a new communicator (multi thread/process version), similar to ncclCommInitRankConfig.

Allows to use more than one

[ncclUniqueId](library-specification.html#structnccl_unique_id)(up to one per rank), indicated by nId, to accelerate the init operation. The number of ncclUniqueIds and their order must be the same for every rank.- Parameters:
**newcomm**–**[out]**Pointer to new communicator**nranks**–**[in]**Total number of ranks participating in this communicator**myrank**–**[in]**Current rank**nId**–**[in]**Number of unique IDs**commIds**–**[in]**List of unique IDs**config**–**[in]**Config file for new communicator. May be NULL to inherit from comm

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
const char *ncclGetErrorString(
[ncclResult_t](#_CPPv412ncclResult_t)result)[#](#_CPPv418ncclGetErrorString12ncclResult_t) Returns a string for each result code.

Returns a human-readable string describing the given result code.

- Parameters:
**result**–**[in]**Result code to get description for- Returns:
String containing description of result code.



-
const char *ncclGetLastError(
[ncclComm_t](#_CPPv410ncclComm_t)comm)[#](#_CPPv416ncclGetLastError10ncclComm_t)

-
void ncclResetDebugInit()
[#](#_CPPv418ncclResetDebugInitv)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommGetAsyncError([ncclComm_t](#_CPPv410ncclComm_t)comm,[ncclResult_t](#_CPPv412ncclResult_t)*asyncError)[#](#_CPPv421ncclCommGetAsyncError10ncclComm_tP12ncclResult_t) Checks whether the comm has encountered any asynchronous errors.

Query whether the provided communicator has encountered any asynchronous errors

- Parameters:
**comm**–**[in]**Communicator to query**asyncError**–**[out]**Pointer to where result code will be stored

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommCount(const[ncclComm_t](#_CPPv410ncclComm_t)comm, int *count)[#](#_CPPv413ncclCommCountK10ncclComm_tPi) Gets the number of ranks in the communicator clique.

Returns the number of ranks in the communicator clique (as set during initialization)

- Parameters:
**comm**–**[in]**Communicator to query**count**–**[out]**Pointer to where number of ranks will be stored

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommCuDevice(const[ncclComm_t](#_CPPv410ncclComm_t)comm, int *device)[#](#_CPPv416ncclCommCuDeviceK10ncclComm_tPi) Get the ROCm device index associated with a communicator.

Returns the ROCm device number associated with the provided communicator.

- Parameters:
**comm**–**[in]**Communicator to query**device**–**[out]**Pointer to where the associated ROCm device index will be stored

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommUserRank(const[ncclComm_t](#_CPPv410ncclComm_t)comm, int *rank)[#](#_CPPv416ncclCommUserRankK10ncclComm_tPi) Get the rank associated with a communicator.

Returns the user-ordered “rank” associated with the provided communicator.

- Parameters:
**comm**–**[in]**Communicator to query**rank**–**[out]**Pointer to where the associated rank will be stored

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommRegister(const[ncclComm_t](#_CPPv410ncclComm_t)comm, void *buff, size_t size, void **handle)[#](#_CPPv416ncclCommRegisterK10ncclComm_tPv6size_tPPv)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommDeregister(const[ncclComm_t](#_CPPv410ncclComm_t)comm, void *handle)[#](#_CPPv418ncclCommDeregisterK10ncclComm_tPv)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommWindowRegister([ncclComm_t](#_CPPv410ncclComm_t)comm, void *buff, size_t size,[ncclWindow_t](#_CPPv412ncclWindow_t)*win, int winFlags)[#](#_CPPv422ncclCommWindowRegister10ncclComm_tPv6size_tP12ncclWindow_ti)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclCommWindowDeregister([ncclComm_t](#_CPPv410ncclComm_t)comm,[ncclWindow_t](#_CPPv412ncclWindow_t)win)[#](#_CPPv424ncclCommWindowDeregister10ncclComm_t12ncclWindow_t)

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclRedOpCreatePreMulSum([ncclRedOp_t](#_CPPv411ncclRedOp_t)*op, void *scalar,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclScalarResidence_t](#_CPPv421ncclScalarResidence_t)residence,[ncclComm_t](#_CPPv410ncclComm_t)comm)[#](#_CPPv424ncclRedOpCreatePreMulSumP11ncclRedOp_tPv14ncclDataType_t21ncclScalarResidence_t10ncclComm_t) Create a custom pre-multiplier reduction operator.

Creates a new reduction operator which pre-multiplies input values by a given scalar locally before reducing them with peer values via summation. For use only with collectives launched against

*comm*and*datatype*. The residence* argument indicates how/when the memory pointed to by*scalar*will be dereferenced. Upon return, the newly created operator’s handle is stored in*op*.- Parameters:
**op**–**[out]**Pointer to where newly created custom reduction operator is to be stored**scalar**–**[in]**Pointer to scalar value.**datatype**–**[in]**Scalar value datatype**residence**–**[in]**Memory type of the scalar value**comm**–**[in]**Communicator to associate with this custom reduction operator

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclRedOpDestroy([ncclRedOp_t](#_CPPv411ncclRedOp_t)op,[ncclComm_t](#_CPPv410ncclComm_t)comm)[#](#_CPPv416ncclRedOpDestroy11ncclRedOp_t10ncclComm_t) Destroy custom reduction operator.

Destroys the reduction operator

*op*. The operator must have been created by ncclRedOpCreatePreMul with the matching communicator*comm*. An operator may be destroyed as soon as the last RCCL function which is given that operator returns.- Parameters:
**op**–**[in]**Custom reduction operator is to be destroyed**comm**–**[in]**Communicator associated with this reduction operator

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclReduce(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](#_CPPv411ncclRedOp_t)op, int root,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv410ncclReducePKvPv6size_t14ncclDataType_t11ncclRedOp_ti10ncclComm_t11hipStream_t) Reduce.

Reduces data arrays of length

*count*in*sendbuff*into*recvbuff*using*op*operation. recvbuff* may be NULL on all calls except for root device. root* is the rank (not the HIP device) where data will reside after the operation is complete. In-place operation will happen if sendbuff == recvbuff.- Parameters:
**sendbuff**–**[in]**Local device data buffer to be reduced**recvbuff**–**[out]**Data buffer where result is stored (only for*root*rank). May be null for other ranks.**count**–**[in]**Number of elements in every send buffer**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator type**root**–**[in]**Rank where result data array will be stored**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclBcast(void *buff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv49ncclBcastPv6size_t14ncclDataType_ti10ncclComm_t11hipStream_t) (Deprecated) Broadcast (in-place)

Copies

*count*values from*root*to all other devices. root is the rank (not the CUDA device) where data resides before the operation is started. This operation is implicitly in-place.- Parameters:
**buff**–**[inout]**Input array on*root*to be copied to other ranks. Output array for all ranks.**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank owning buffer to be copied to others**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclBroadcast(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv413ncclBroadcastPKvPv6size_t14ncclDataType_ti10ncclComm_t11hipStream_t) Broadcast.

Copies

*count*values from*sendbuff*on*root*to*recvbuff*on all devices. root* is the rank (not the HIP device) where data resides before the operation is started. sendbuff* may be NULL on ranks other than*root*. In-place operation will happen if*sendbuff*==*recvbuff*.- Parameters:
**sendbuff**–**[in]**Data array to copy (if*root*). May be NULL for other ranks**recvbuff**–**[in]**Data array to store received array**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank of broadcast root**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclAllReduce(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](#_CPPv411ncclRedOp_t)op,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv413ncclAllReducePKvPv6size_t14ncclDataType_t11ncclRedOp_t10ncclComm_t11hipStream_t) All-Reduce.

Reduces data arrays of length

*count*in*sendbuff*using*op*operation, and leaves identical copies of result on each*recvbuff*. In-place operation will happen if sendbuff == recvbuff.- Parameters:
**sendbuff**–**[in]**Input data array to reduce**recvbuff**–**[out]**Data array to store reduced result array**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclAllReduceWithBias(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](#_CPPv411ncclRedOp_t)op,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream, const void *acc)[#](#_CPPv421ncclAllReduceWithBiasPKvPv6size_t14ncclDataType_t11ncclRedOp_t10ncclComm_t11hipStream_tPKv) All-Reduce-with-Bias.

Reduces data arrays of length

*count*in*sendbuff*using*op*operation, and leaves identical copies of result on each*recvbuff*. In-place operation will happen if sendbuff == recvbuff.- Parameters:
**sendbuff**–**[in]**Input data array to reduce**recvbuff**–**[out]**Data array to store reduced result array**count**–**[in]**Number of elements in data buffer**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on**acc**–**[in]**Bias data array to reduce

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclReduceScatter(const void *sendbuff, void *recvbuff, size_t recvcount,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclRedOp_t](#_CPPv411ncclRedOp_t)op,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv417ncclReduceScatterPKvPv6size_t14ncclDataType_t11ncclRedOp_t10ncclComm_t11hipStream_t) Reduce-Scatter.

Reduces data in

*sendbuff*using*op*operation and leaves reduced result scattered over the devices so that*recvbuff*on rank i will contain the i-th block of the result. Assumes sendcount is equal to nranks*recvcount, which means that*sendbuff*should have a size of at least nranks*recvcount elements. In-place operations will happen if recvbuff == sendbuff + rank * recvcount.- Parameters:
**sendbuff**–**[in]**Input data array to reduce**recvbuff**–**[out]**Data array to store reduced result subarray**recvcount**–**[in]**Number of elements each rank receives**datatype**–**[in]**Data buffer element datatype**op**–**[in]**Reduction operator**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclAllGather(const void *sendbuff, void *recvbuff, size_t sendcount,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv413ncclAllGatherPKvPv6size_t14ncclDataType_t10ncclComm_t11hipStream_t) All-Gather.

Each device gathers

*sendcount*values from other GPUs into*recvbuff*, receiving data from rank i at offset i*sendcount. Assumes recvcount is equal to nranks*sendcount, which means that recvbuff should have a size of at least nranks*sendcount elements. In-place operations will happen if sendbuff == recvbuff + rank * sendcount.- Parameters:
**sendbuff**–**[in]**Input data array to send**recvbuff**–**[out]**Data array to store the gathered result**sendcount**–**[in]**Number of elements each rank sends**datatype**–**[in]**Data buffer element datatype**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclSend(const void *sendbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype, int peer,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv48ncclSendPKv6size_t14ncclDataType_ti10ncclComm_t11hipStream_t) Send.

Send data from

*sendbuff*to rank*peer*. Rank*peer*needs to call ncclRecv with the same*datatype*and the same*count*as this rank. This operation is blocking for the GPU. If multiple ncclSend and ncclRecv operations need to progress concurrently to complete, they must be fused within a ncclGroupStart / ncclGroupEnd section.- Parameters:
**sendbuff**–**[in]**Data array to send**count**–**[in]**Number of elements to send**datatype**–**[in]**Data buffer element datatype**peer**–**[in]**Peer rank to send to**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclRecv(void *recvbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype, int peer,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv48ncclRecvPv6size_t14ncclDataType_ti10ncclComm_t11hipStream_t) Receive.

Receive data from rank

*peer*into*recvbuff*. Rank*peer*needs to call ncclSend with the same datatype and the same count as this rank. This operation is blocking for the GPU. If multiple ncclSend and ncclRecv operations need to progress concurrently to complete, they must be fused within a ncclGroupStart/ ncclGroupEnd section.- Parameters:
**recvbuff**–**[out]**Data array to receive**count**–**[in]**Number of elements to receive**datatype**–**[in]**Data buffer element datatype**peer**–**[in]**Peer rank to send to**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclGather(const void *sendbuff, void *recvbuff, size_t sendcount,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv410ncclGatherPKvPv6size_t14ncclDataType_ti10ncclComm_t11hipStream_t) Gather.

Root device gathers

*sendcount*values from other GPUs into*recvbuff*, receiving data from rank i at offset i*sendcount. Assumes recvcount is equal to nranks*sendcount, which means that*recvbuff*should have a size of at least nranks*sendcount elements. In-place operations will happen if sendbuff == recvbuff + rank * sendcount. recvbuff* may be NULL on ranks other than*root*.- Parameters:
**sendbuff**–**[in]**Data array to send**recvbuff**–**[out]**Data array to receive into on*root*.**sendcount**–**[in]**Number of elements to send per rank**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank that receives data from all other ranks**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclScatter(const void *sendbuff, void *recvbuff, size_t recvcount,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype, int root,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv411ncclScatterPKvPv6size_t14ncclDataType_ti10ncclComm_t11hipStream_t) Scatter.

Scattered over the devices so that recvbuff on rank i will contain the i-th block of the data on root. Assumes sendcount is equal to nranks*recvcount, which means that

*sendbuff*should have a size of at least nranks*recvcount elements. In-place operations will happen if recvbuff == sendbuff + rank * recvcount.- Parameters:
**sendbuff**–**[in]**Data array to send (on*root*rank). May be NULL on other ranks.**recvbuff**–**[out]**Data array to receive partial subarray into**recvcount**–**[in]**Number of elements to receive per rank**datatype**–**[in]**Data buffer element datatype**root**–**[in]**Rank that scatters data to all other ranks**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclAllToAll(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv412ncclAllToAllPKvPv6size_t14ncclDataType_t10ncclComm_t11hipStream_t) All-To-All.

Device (i) send (j)th block of data to device (j) and be placed as (i)th block. Each block for sending/receiving has

*count*elements, which means that*recvbuff*and*sendbuff*should have a size of nranks*count elements. In-place operation is NOT supported. It is the user’s responsibility to ensure that sendbuff and recvbuff are distinct.- Parameters:
**sendbuff**–**[in]**Data array to send (contains blocks for each other rank)**recvbuff**–**[out]**Data array to receive (contains blocks from each other rank)**count**–**[in]**Number of elements to send between each pair of ranks**datatype**–**[in]**Data buffer element datatype**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclAllToAllv(const void *sendbuff, const size_t sendcounts[], const size_t sdispls[], void *recvbuff, const size_t recvcounts[], const size_t rdispls[],[ncclDataType_t](#_CPPv414ncclDataType_t)datatype,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv413ncclAllToAllvPKvA_K6size_tA_K6size_tPvA_K6size_tA_K6size_t14ncclDataType_t10ncclComm_t11hipStream_t) All-To-Allv.

Device (i) sends sendcounts[j] of data from offset sdispls[j] to device (j). At the same time, device (i) receives recvcounts[j] of data from device (j) to be placed at rdispls[j]. sendcounts, sdispls, recvcounts and rdispls are all measured in the units of datatype, not bytes. In-place operation will happen if sendbuff == recvbuff.

- Parameters:
**sendbuff**–**[in]**Data array to send (contains blocks for each other rank)**sendcounts**–**[in]**Array containing number of elements to send to each participating rank**sdispls**–**[in]**Array of offsets into*sendbuff*for each participating rank**recvbuff**–**[out]**Data array to receive (contains blocks from each other rank)**recvcounts**–**[in]**Array containing number of elements to receive from each participating rank**rdispls**–**[in]**Array of offsets into*recvbuff*for each participating rank**datatype**–**[in]**Data buffer element datatype**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)mscclLoadAlgo(const char *mscclAlgoFilePath,[mscclAlgoHandle_t](#_CPPv417mscclAlgoHandle_t)*mscclAlgoHandle, int rank)[#](#_CPPv413mscclLoadAlgoPKcP17mscclAlgoHandle_ti) MSCCL Load Algorithm.

-
[Deprecated:](#deprecated_1_deprecated000001) This function has been removed from the public API.


Load MSCCL algorithm file specified in mscclAlgoFilePath and return its handle via mscclAlgoHandle. This API is expected to be called by MSCCL scheduler instead of end users.

- Parameters:
**mscclAlgoFilePath**–**[in]**Path to MSCCL algorithm file**mscclAlgoHandle**–**[out]**Returned handle to MSCCL algorithm**rank**–**[in]**Current rank

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.

-

-
[ncclResult_t](#_CPPv412ncclResult_t)mscclRunAlgo(const void *sendBuff, const size_t sendCounts[], const size_t sDisPls[], void *recvBuff, const size_t recvCounts[], const size_t rDisPls[], size_t count,[ncclDataType_t](#_CPPv414ncclDataType_t)dataType, int root, int peer,[ncclRedOp_t](#_CPPv411ncclRedOp_t)op,[mscclAlgoHandle_t](#_CPPv417mscclAlgoHandle_t)mscclAlgoHandle,[ncclComm_t](#_CPPv410ncclComm_t)comm, hipStream_t stream)[#](#_CPPv412mscclRunAlgoPKvA_K6size_tA_K6size_tPvA_K6size_tA_K6size_t6size_t14ncclDataType_tii11ncclRedOp_t17mscclAlgoHandle_t10ncclComm_t11hipStream_t) MSCCL Run Algorithm.

-
[Deprecated:](#deprecated_1_deprecated000002) This function has been removed from the public API.


Run MSCCL algorithm specified by mscclAlgoHandle. The parameter list merges all possible parameters required by different operations as this is a general-purposed API. This API is expected to be called by MSCCL scheduler instead of end users.

- Parameters:
**sendBuff**–**[in]**Data array to send**sendCounts**–**[in]**Array containing number of elements to send to each participating rank**sDisPls**–**[in]**Array of offsets into*sendbuff*for each participating rank**recvBuff**–**[out]**Data array to receive**recvCounts**–**[in]**Array containing number of elements to receive from each participating rank**rDisPls**–**[in]**Array of offsets into*recvbuff*for each participating rank**count**–**[in]**Number of elements**dataType**–**[in]**Data buffer element datatype**root**–**[in]**Root rank index**peer**–**[in]**Peer rank index**op**–**[in]**Reduction operator**mscclAlgoHandle**–**[in]**Handle to MSCCL algorithm**comm**–**[in]**Communicator group object to execute on**stream**–**[in]**HIP stream to execute collective on

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.

-

-
[ncclResult_t](#_CPPv412ncclResult_t)mscclUnloadAlgo([mscclAlgoHandle_t](#_CPPv417mscclAlgoHandle_t)mscclAlgoHandle)[#](#_CPPv415mscclUnloadAlgo17mscclAlgoHandle_t) MSCCL Unload Algorithm.

-
[Deprecated:](#deprecated_1_deprecated000003) This function has been removed from the public API.


Unload MSCCL algorithm previous loaded using its handle. This API is expected to be called by MSCCL scheduler instead of end users.

- Parameters:
**mscclAlgoHandle**–**[in]**Handle to MSCCL algorithm to unload- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.

-

-
[ncclResult_t](#_CPPv412ncclResult_t)ncclGroupStart()[#](#_CPPv414ncclGroupStartv) Group Start.

Start a group call. All calls to RCCL until ncclGroupEnd will be fused into a single RCCL operation. Nothing will be started on the HIP stream until ncclGroupEnd.

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclGroupEnd()[#](#_CPPv412ncclGroupEndv) Group End.

End a group call. Start a fused RCCL operation consisting of all calls since ncclGroupStart. Operations on the HIP stream depending on the RCCL operations need to be called after ncclGroupEnd.

- Returns:
Result code. See

[Result Codes](#group__rccl__result__code)for more details.


-
[ncclResult_t](#_CPPv412ncclResult_t)ncclGroupSimulateEnd([ncclSimInfo_t](#_CPPv413ncclSimInfo_t)*simInfo)[#](#_CPPv420ncclGroupSimulateEndP13ncclSimInfo_t)

-
[ncclResult_t](#_CPPv412ncclResult_t)pncclGroupSimulateEnd([ncclSimInfo_t](#_CPPv413ncclSimInfo_t)*simInfo)[#](#_CPPv421pncclGroupSimulateEndP13ncclSimInfo_t)

-
NCCL_H_

-
*group*rccl_result_code The various result codes that RCCL API calls may return

Enums

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
enum ncclResult_t

-
*group*rccl_config_type Structure that allows for customizing Communicator behavior via ncclCommInitRankConfig

Defines

-
NCCL_CONFIG_INITIALIZER

-
NCCL_CONFIG_INITIALIZER

-
*group*rccl_api_version API call that returns RCCL version


-
*group*rccl_api_communicator API calls that operate on communicators. Communicators objects are used to launch collective communication operations. Unique ranks between 0 and N-1 must be assigned to each HIP device participating in the same Communicator. Using the same HIP device for multiple ranks of the same Communicator is not supported at this time.


-
*group*rccl_api_errcheck API calls that check for errors


-
*group*rccl_api_comminfo API calls that query communicator information


-
*group*rccl_api_enumerations Enumerations used by collective communication calls

Enums

-
enum ncclRedOp_dummy_t
Dummy reduction enumeration.

Dummy reduction enumeration used to determine value for ncclMaxRedOp

*Values:*-
enumerator ncclNumOps_dummy

-
enumerator ncclNumOps_dummy

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

-
enum ncclRedOp_dummy_t

-
*group*rccl_api_custom_redop API calls relating to creation/destroying custom reduction operator that pre-multiplies local source arrays prior to reduction

Enums

-
enum ncclScalarResidence_t
Location and dereferencing logic for scalar arguments.

Enumeration specifying memory location of the scalar argument. Based on where the value is stored, the argument will be dereferenced either while the collective is running (if in device memory), or before the ncclRedOpCreate() function returns (if in host memory).

*Values:*-
enumerator ncclScalarDevice
Scalar is in device-visible memory


-
enumerator ncclScalarHostImmediate
Scalar is in host-visible memory


-
enumerator ncclScalarDevice

-
enum ncclScalarResidence_t

-
*group*rccl_collective_api Collective communication operations must be called separately for each communicator in a communicator clique.

They return when operations have been enqueued on the HIP stream. Since they may perform inter-CPU synchronization, each call has to be done from a different thread or process, or need to use Group Semantics (see below).


-
*group*msccl_api API calls relating to the optional MSCCL algorithm datapath

Typedefs

-
typedef int mscclAlgoHandle_t
Opaque handle to MSCCL algorithm.


-
typedef int mscclAlgoHandle_t

-
*group*rccl_group_api When managing multiple GPUs from a single thread, and since RCCL collective calls may perform inter-CPU synchronization, we need to “group” calls for different ranks/devices into a single call.

Grouping RCCL calls as being part of the same collective operation is done using ncclGroupStart and ncclGroupEnd. ncclGroupStart will enqueue all collective calls until the ncclGroupEnd call, which will wait for all calls to be complete. Note that for collective communication, ncclGroupEnd only guarantees that the operations are enqueued on the streams, not that the operation is effectively done.

Both collective communication and ncclCommInitRank can be used in conjunction of ncclGroupStart/ncclGroupEnd, but not together.

Group semantics also allow to fuse multiple operations on the same device to improve performance (for aggregated collective calls), or to permit concurrent progress of multiple send/receive operations.


-
*page*deprecated -
Global
[mscclLoadAlgo](#group__msccl__api_1gafc8446f6990399459ea17c3844cb53fd)(const char *mscclAlgoFilePath, mscclAlgoHandle_t *mscclAlgoHandle, int rank)

-
Global
[mscclRunAlgo](#group__msccl__api_1ga59c37e39ac3733bef3c84d4b2f1243a4)(const void *sendBuff, const size_t sendCounts[], const size_t sDisPls[], void *recvBuff, const size_t recvCounts[], const size_t rDisPls[], size_t count, ncclDataType_t dataType, int root, int peer, ncclRedOp_t op, mscclAlgoHandle_t mscclAlgoHandle, ncclComm_t comm, hipStream_t stream)

-
Global
[mscclUnloadAlgo](#group__msccl__api_1gafdb450531b5feeb3df5649e6bbef794e)(mscclAlgoHandle_t mscclAlgoHandle)

-
Global

-
*dir*src

-
*page*index ## Introduction

[#](#index_1intro_sec)RCCL (pronounced “Rickle”) is a stand-alone library of standard collective communication routines for GPUs, implementing all-reduce, all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and all-to-all. There is also initial support for direct GPU-to-GPU send and receive operations. It has been optimized to achieve high bandwidth on platforms using PCIe, xGMI as well as networking using InfiniBand Verbs or TCP/IP sockets. RCCL supports an arbitrary number of GPUs installed in a single node or multiple nodes, and can be used in either single- or multi-process (e.g., MPI) applications.

The collective operations are implemented using ring and tree algorithms and have been optimized for throughput and latency. For best performance, small operations can be either batched into larger operations or aggregated through the API.

## RCCL API Contents

[#](#index_1API)## RCCL API File

[#](#index_1Full)
