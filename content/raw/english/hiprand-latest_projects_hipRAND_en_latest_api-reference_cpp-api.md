---
title: "C/C++ API reference &#8212; hipRAND 3.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipRAND/en/latest/api-reference/cpp-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:09:34.233488+00:00
content_hash: "7b4fd569db9b1871"
---

# C/C++ API reference[#](#c-c-api-reference)

This document describes the hipRAND APIs available in C and C++.

## Device functions[#](#device-functions)

-
*group*hipranddevice Defines

-
HIPRAND_PHILOX4x32_DEFAULT_SEED
[#](#c.HIPRAND_PHILOX4x32_DEFAULT_SEED) Default seed for PHILOX4x32 PRNG.


-
HIPRAND_XORWOW_DEFAULT_SEED
[#](#c.HIPRAND_XORWOW_DEFAULT_SEED) Default seed for XORWOW PRNG.


-
HIPRAND_MRG32K3A_DEFAULT_SEED
[#](#c.HIPRAND_MRG32K3A_DEFAULT_SEED) Default seed for MRG32K3A PRNG.


-
HIPRAND_MTGP32_DEFAULT_SEED
[#](#c.HIPRAND_MTGP32_DEFAULT_SEED) Default seed for MTGP32 PRNG.


-
HIPRAND_MT19937_DEFAULT_SEED
[#](#c.HIPRAND_MT19937_DEFAULT_SEED) Default seed for MT19937 PRNG.


Typedefs

-
typedef struct hiprandStateXORWOW hiprandStateXORWOW_t
[#](#_CPPv420hiprandStateXORWOW_t) XORWOW PRNG state type.


-
typedef
[hiprandStateXORWOW_t](#_CPPv420hiprandStateXORWOW_t)hipRandState_t[#](#_CPPv414hipRandState_t) Deprecated alias of hiprandStateXORWOW_t.

-
*Deprecated:* Please use hiprandStateXORWOW_t directly.


-

-
typedef struct hiprandStatePhilox4_32_10 hiprandStatePhilox4_32_10_t
[#](#_CPPv427hiprandStatePhilox4_32_10_t) PHILOX PRNG state type.


-
typedef struct hiprandStateMRG32k3a hiprandStateMRG32k3a_t
[#](#_CPPv422hiprandStateMRG32k3a_t) MRG32k3a PRNG state type.


-
typedef struct hiprandStateMtgp32 hiprandStateMtgp32_t
[#](#_CPPv420hiprandStateMtgp32_t) MTGP32 PRNG state type.


-
typedef struct hiprandStateScrambledSobol32 hiprandStateScrambledSobol32_t
[#](#_CPPv430hiprandStateScrambledSobol32_t) Scrambled SOBOL32 QRNG state type.


-
typedef struct hiprandStateScrambledSobol64 hiprandStateScrambledSobol64_t
[#](#_CPPv430hiprandStateScrambledSobol64_t) Scrambled SOBOL64 QRNG state type.


-
typedef struct hiprandStateSobol32 hiprandStateSobol32_t
[#](#_CPPv421hiprandStateSobol32_t) SOBOL32 QRNG state type.


-
typedef struct hiprandStateSobol64 hiprandStateSobol64_t
[#](#_CPPv421hiprandStateSobol64_t) SOBOL64 QRNG state type.


-
typedef mtgp32_params mtgp32_kernel_params_t
[#](#_CPPv422mtgp32_kernel_params_t) Opaque MTGP32 PRNG state parameters in the device format.


-
typedef struct mtgp32_params_fast mtgp32_params_fast_t
[#](#_CPPv420mtgp32_params_fast_t) Opaque MTGP32 PRNG state parameters in the host format.


-
typedef mtgp32_fast_params mtgp32_fast_param_t
[#](#_CPPv419mtgp32_fast_param_t) Deprecated alias of mtgp32_params_fast_t.

-
*Deprecated:* please use mtgp32_params_fast_t directly.


-

-
typedef unsigned int hiprandDirectionVectors32_t[32]
[#](#_CPPv427hiprandDirectionVectors32_t) Convenience typedef for Sobol 32 direction vector array.


-
typedef unsigned long long hiprandDirectionVectors64_t[64]
[#](#_CPPv427hiprandDirectionVectors64_t) Convenience typedef for Sobol 64 direction vector array.


Functions

-
void hiprand_mtgp32_block_copy(
[hiprandStateMtgp32_t](#_CPPv420hiprandStateMtgp32_t)*src,[hiprandStateMtgp32_t](#_CPPv420hiprandStateMtgp32_t)*dest)[#](#_CPPv425hiprand_mtgp32_block_copyP20hiprandStateMtgp32_tP20hiprandStateMtgp32_t) Copy MTGP32 state to another state using block of threads.

Copies a MTGP32 state

`src`

to`dest`

using a block of threads efficiently. Example usage would be:__global__ void generate_kernel(hiprandStateMtgp32_t * states, unsigned int * output, const size_t size) { const unsigned int state_id = hipBlockIdx_x; unsigned int index = hipBlockIdx_x * hipBlockDim_x + hipThreadIdx_x; unsigned int stride = hipGridDim_x * hipBlockDim_x; __shared__ GeneratorState state; hiprand_mtgp32_block_copy(&states[state_id], &state); while(index < size) { output[index] = rocrand(&state); index += stride; } hiprand_mtgp32_block_copy(&state, &states[state_id]); }

- Parameters:
**src**– Pointer to a state to copy from**dest**– Pointer to a state to copy to



-
void hiprand_mtgp32_set_params(
[hiprandStateMtgp32_t](#_CPPv420hiprandStateMtgp32_t)*state,[mtgp32_kernel_params_t](#_CPPv422mtgp32_kernel_params_t)*params)[#](#_CPPv425hiprand_mtgp32_set_paramsP20hiprandStateMtgp32_tP22mtgp32_kernel_params_t) Changes parameters of a MTGP32 state.

- Parameters:
**state**– Pointer to a MTGP32 state**params**– Pointer to new parameters



-
template<class StateType>

void hiprand_init(const unsigned long long seed, const unsigned long long subsequence, const unsigned long long offset,[StateType](#_CPPv4I0E12hiprand_initvKyKyKyP9StateType)*state)[#](#_CPPv4I0E12hiprand_initvKyKyKyP9StateType) Initializes a PRNG state.

- Template Parameters:
**StateType**– Pseudorandom number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66)or[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)- Parameters:
**seed**– Pseudorandom number generator’s seed**subsequence**– Number of subsequence to skipahead**offset**– Absolute subsequence offset, i.e. how many states from current subsequence should be skipped**state**– Pointer to a state to initialize



-
void hiprand_init(
[hiprandDirectionVectors32_t](#_CPPv427hiprandDirectionVectors32_t)direction_vectors, unsigned int offset,[hiprandStateSobol32_t](#_CPPv421hiprandStateSobol32_t)*state)[#](#_CPPv412hiprand_init27hiprandDirectionVectors32_tjP21hiprandStateSobol32_t) Initializes a Sobol32 state.

- Parameters:
**direction_vectors**– Pointer to array of 32`unsigned int`

s that represent the direction numbers.**offset**– Absolute subsequence offset, i.e. how many states should be skipped.**state**– Pointer to a state to initialize.



-
void hiprand_init(
[hiprandDirectionVectors32_t](#_CPPv427hiprandDirectionVectors32_t)direction_vectors, unsigned int scramble_constant, unsigned int offset,[hiprandStateScrambledSobol32_t](#_CPPv430hiprandStateScrambledSobol32_t)*state)[#](#_CPPv412hiprand_init27hiprandDirectionVectors32_tjjP30hiprandStateScrambledSobol32_t) Initializes a ScrambledSobol32 state.

- Parameters:
**direction_vectors**– Pointer to array of 32`unsigned int`

s that represent the direction numbers.**scramble_constant**– Constant used for scrambling the sequence.**offset**– Absolute subsequence offset, i.e. how many states should be skipped.**state**– Pointer to a state to initialize.



-
void hiprand_init(
[hiprandDirectionVectors64_t](#_CPPv427hiprandDirectionVectors64_t)direction_vectors, unsigned int offset,[hiprandStateSobol64_t](#_CPPv421hiprandStateSobol64_t)*state)[#](#_CPPv412hiprand_init27hiprandDirectionVectors64_tjP21hiprandStateSobol64_t) Initializes a Sobol64 state.

- Parameters:
**direction_vectors**– Pointer to array of 64`unsigned long long int`

s that represent the direction numbers.**offset**– Absolute subsequence offset, i.e. how many states should be skipped.**state**– Pointer to a state to initialize.



-
void hiprand_init(
[hiprandDirectionVectors64_t](#_CPPv427hiprandDirectionVectors64_t)direction_vectors, unsigned long long int scramble_constant, unsigned int offset,[hiprandStateScrambledSobol64_t](#_CPPv430hiprandStateScrambledSobol64_t)*state)[#](#_CPPv412hiprand_init27hiprandDirectionVectors64_tyjP30hiprandStateScrambledSobol64_t) Initializes a ScrambledSobol64 state.

- Parameters:
**direction_vectors**– Pointer to array of 64`unsigned long long int`

s that represent the direction numbers.**scramble_constant**– Constant used for scrambling the sequence.**offset**– Absolute subsequence offset, i.e. how many states should be skipped.**state**– Pointer to a state to initialize.



-
template<class StateType>

void skipahead(unsigned long long n,[StateType](#_CPPv4I0E9skipaheadvyP9StateType)*state)[#](#_CPPv4I0E9skipaheadvyP9StateType) Updates RNG state skipping

`n`

states ahead.- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66),[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011),[hiprandStateSobol32_t](#group__hipranddevice_1gade7ead2e63fdf92114564e25608d22d9),[hiprandStateScrambledSobol32_t](#group__hipranddevice_1gac043b9426d83395100f1f1ae122f5fe5),[hiprandStateSobol64_t](#group__hipranddevice_1gaa684476ee02d7b27327da4d5d142c654)or[hiprandStateScrambledSobol64_t](#group__hipranddevice_1gadeebda951ec4100bf0a97302243f4930).- Parameters:
**n**– Number of states to skipahead**state**– Pointer to a state to modify



-
template<class StateType>

void skipahead_sequence(unsigned long long n,[StateType](#_CPPv4I0E18skipahead_sequencevyP9StateType)*state)[#](#_CPPv4I0E18skipahead_sequencevyP9StateType) Updates PRNG state skipping

`n`

sequences ahead.PRNG

Sequence size [Number of elements]

XORWOW

\( 2^{67} \)

Philox

\( 4 \times 2^{64} \)

MRG32k3a

\( 2^{67} \)

- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66), or[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)- Parameters:
**n**– Number of subsequences to skipahead**state**– Pointer to a state to update



-
template<class StateType>

void skipahead_subsequence(unsigned long long n,[StateType](#_CPPv4I0E21skipahead_subsequencevyP9StateType)*state)[#](#_CPPv4I0E21skipahead_subsequencevyP9StateType) Updates PRNG state skipping

`n`

subsequences ahead.PRNG

Subsequence size [Number of elements]

XORWOW

\( 2^{67} \)

Philox

\( 4 \times 2^{64} \)

MRG32k3a

\( 2^{127} \)

- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66)or[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)- Parameters:
**n**– Number of subsequences to skipahead**state**– Pointer to a state to update



-
template<class StateType>

unsigned int hiprand([StateType](#_CPPv4I0E7hiprandjP9StateType)*state)[#](#_CPPv4I0E7hiprandjP9StateType) Generates uniformly distributed random

`unsigned int`

from [0; 2^32 - 1] range.- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66),[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011),[hiprandStateMtgp32_t](#group__hipranddevice_1ga2afca2f9af43d868b2feb082db0f9268),[hiprandStateSobol32_t](#group__hipranddevice_1gade7ead2e63fdf92114564e25608d22d9),[hiprandStateScrambledSobol32_t](#group__hipranddevice_1gac043b9426d83395100f1f1ae122f5fe5).- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Uniformly distributed random 32-bit

`unsigned int`



-
uint4 hiprand4(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state)[#](#_CPPv48hiprand4P27hiprandStatePhilox4_32_10_t) Generates four uniformly distributed random

`unsigned int`

s from [0; 2^32 - 1] range.- Parameters:
**state**– Pointer to a Philox state to use- Returns:
Four uniformly distributed random 32-bit

`unsigned int`

s as`uint4`



-
template<class StateType>

unsigned long long int hiprand_long_long([StateType](#_CPPv4I0E17hiprand_long_longyP9StateType)*state)[#](#_CPPv4I0E17hiprand_long_longyP9StateType) Generates uniformly distributed random

`unsigned long long int`

from [0; 2^64 - 1] range.- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of the following types:[hiprandStateSobol64_t](#group__hipranddevice_1gaa684476ee02d7b27327da4d5d142c654)or[hiprandStateScrambledSobol64_t](#group__hipranddevice_1gadeebda951ec4100bf0a97302243f4930).- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Uniformly distributed random 64-bit

`unsigned long long int`



-
template<class StateType>

float hiprand_uniform([StateType](#_CPPv4I0E15hiprand_uniformfP9StateType)*state)[#](#_CPPv4I0E15hiprand_uniformfP9StateType) Generates uniformly distributed random

`float`

value from (0; 1] range.- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Uniformly distributed random

`float`

value


-
float4 hiprand_uniform4(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state)[#](#_CPPv416hiprand_uniform4P27hiprandStatePhilox4_32_10_t) Generates four uniformly distributed random

`float`

value from (0; 1] range.- Parameters:
**state**– Pointer to a Philox state to use- Returns:
Four uniformly distributed random

`float`

values as`float4`



-
template<class StateType>

double hiprand_uniform_double([StateType](#_CPPv4I0E22hiprand_uniform_doubledP9StateType)*state)[#](#_CPPv4I0E22hiprand_uniform_doubledP9StateType) Generates uniformly distributed random

`double`

value from (0; 1] range.Note

When

`state`

is of type:[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011),[hiprandStateMtgp32_t](#group__hipranddevice_1ga2afca2f9af43d868b2feb082db0f9268),[hiprandStateSobol32_t](#group__hipranddevice_1gade7ead2e63fdf92114564e25608d22d9)or[hiprandStateScrambledSobol32_t](#group__hipranddevice_1gac043b9426d83395100f1f1ae122f5fe5)then the returned`double`

value is generated using only 32 random bits (one`unsigned int`

value). In case of the Sobol types, this is done to guarantee the quasi-random properties.- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Uniformly distributed random

`double`

value


-
double2 hiprand_uniform2_double(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state)[#](#_CPPv423hiprand_uniform2_doubleP27hiprandStatePhilox4_32_10_t) Generates two uniformly distributed random

`double`

values from (0; 1] range.- Parameters:
**state**– Pointer to a Philox state to use- Returns:
Two uniformly distributed random

`double`

values as`double2`



-
double4 hiprand_uniform4_double(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state)[#](#_CPPv423hiprand_uniform4_doubleP27hiprandStatePhilox4_32_10_t) Generates four uniformly distributed random

`double`

values from (0; 1] range.- Parameters:
**state**– Pointer to a Philox state to use- Returns:
Four uniformly distributed random

`double`

values as`double4`



-
template<class StateType>

float hiprand_normal([StateType](#_CPPv4I0E14hiprand_normalfP9StateType)*state)[#](#_CPPv4I0E14hiprand_normalfP9StateType) Generates normally distributed random

`float`

value.Mean value of normal distribution is equal to 0.0, and standard deviation equals 1.0.

- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Normally distributed random

`float`

value


-
template<class StateType>

float2 hiprand_normal2([StateType](#_CPPv4I0E15hiprand_normal26float2P9StateType)*state)[#](#_CPPv4I0E15hiprand_normal26float2P9StateType) Generates two normally distributed random

`float`

values.Mean value of normal distribution is equal to 0.0, and standard deviation equals 1.0.

- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66), or[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Two normally distributed random

`float`

values as`float2`



-
float4 hiprand_normal4(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state)[#](#_CPPv415hiprand_normal4P27hiprandStatePhilox4_32_10_t) Generates four normally distributed random

`float`

values.Mean value of normal distribution is equal to 0.0, and standard deviation equals 1.0.

- Parameters:
**state**– Pointer to a Philox state to use- Returns:
Four normally distributed random

`float`

values as`float4`



-
template<class StateType>

double hiprand_normal_double([StateType](#_CPPv4I0E21hiprand_normal_doubledP9StateType)*state)[#](#_CPPv4I0E21hiprand_normal_doubledP9StateType) Generates normally distributed random

`double`

value.Mean value of normal distribution is equal to 0.0, and standard deviation equals 1.0.

- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Normally distributed random

`double`

value


-
template<class StateType>

double2 hiprand_normal2_double([StateType](#_CPPv4I0E22hiprand_normal2_double7double2P9StateType)*state)[#](#_CPPv4I0E22hiprand_normal2_double7double2P9StateType) Generates two normally distributed random

`double`

values.Mean value of normal distribution is equal to 0.0, and standard deviation equals 1.0.

- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66), or[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)- Parameters:
**state**– Pointer to a RNG state to use- Returns:
Two normally distributed random

`double`

values as`double2`



-
double4 hiprand_normal4_double(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state)[#](#_CPPv422hiprand_normal4_doubleP27hiprandStatePhilox4_32_10_t) Generates four normally distributed random

`double`

values.Mean value of normal distribution is equal to 0.0, and standard deviation equals 1.0.

- Parameters:
**state**– Pointer to a Philox state to use- Returns:
Four normally distributed random

`double`

values as`double4`



-
template<class StateType>

float hiprand_log_normal([StateType](#_CPPv4I0E18hiprand_log_normalfP9StateTypeff)*state, float mean, float stddev)[#](#_CPPv4I0E18hiprand_log_normalfP9StateTypeff) Generates log-normally distributed random

`float`

value.- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use**mean**– Mean value of log-normal distribution**stddev**– Standard deviation value of log-normal distribution

- Returns:
Log-normally distributed random

`float`

value


-
template<class StateType>

float2 hiprand_log_normal2([StateType](#_CPPv4I0E19hiprand_log_normal26float2P9StateTypeff)*state, float mean, float stddev)[#](#_CPPv4I0E19hiprand_log_normal26float2P9StateTypeff) Generates two log-normally distributed random

`float`

values.- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66), or[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)- Parameters:
**state**– Pointer to a RNG state to use**mean**– Mean value of log-normal distribution**stddev**– Standard deviation value of log-normal distribution

- Returns:
Two log-normally distributed random

`float`

values as`float2`



-
float4 hiprand_log_normal4(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state, float mean, float stddev)[#](#_CPPv419hiprand_log_normal4P27hiprandStatePhilox4_32_10_tff) Generates four log-normally distributed random

`float`

values.- Parameters:
**state**– Pointer to a Philox state to use**mean**– Mean value of log-normal distribution**stddev**– Standard deviation value of log-normal distribution

- Returns:
Four log-normally distributed random

`float`

values as`float4`



-
template<class StateType>

double hiprand_log_normal_double([StateType](#_CPPv4I0E25hiprand_log_normal_doubledP9StateTypedd)*state, double mean, double stddev)[#](#_CPPv4I0E25hiprand_log_normal_doubledP9StateTypedd) Generates log-normally distributed random

`double`

value.- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use**mean**– Mean value of log-normal distribution**stddev**– Standard deviation value of log-normal distribution

- Returns:
Log-normally distributed random

`double`

value


-
template<class StateType>

double2 hiprand_log_normal2_double([StateType](#_CPPv4I0E26hiprand_log_normal2_double7double2P9StateTypedd)*state, double mean, double stddev)[#](#_CPPv4I0E26hiprand_log_normal2_double7double2P9StateTypedd) Generates two log-normally distributed random

`double`

values.- Template Parameters:
**StateType**– Random number generator state type.`StateType`

type must be one of following types:[hiprandStateXORWOW_t](#group__hipranddevice_1ga8c0c8986ae9aab357f4935eb1b1f9d72),[hiprandStatePhilox4_32_10_t](#group__hipranddevice_1gaef89fa57654876bd370fbafebbce8e66),[hiprandStateMRG32k3a_t](#group__hipranddevice_1ga0e257c07e70c08795ad3af2893ecc011)or hiprandStateMtgp32_t.- Parameters:
**state**– Pointer to a RNG state to use**mean**– Mean value of log-normal distribution**stddev**– Standard deviation value of log-normal distribution

- Returns:
Two log-normally distributed random

`double`

values as`double2`



-
double4 hiprand_log_normal4_double(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state, double mean, double stddev)[#](#_CPPv426hiprand_log_normal4_doubleP27hiprandStatePhilox4_32_10_tdd) Generates four log-normally distributed random

`double`

values.- Parameters:
**state**– Pointer to a Philox state to use**mean**– Mean value of log-normal distribution**stddev**– Standard deviation value of log-normal distribution

- Returns:
Four log-normally distributed random

`double`

values as`double4`



-
template<class StateType>

unsigned int hiprand_poisson([StateType](#_CPPv4I0E15hiprand_poissonjP9StateTyped)*state, double lambda)[#](#_CPPv4I0E15hiprand_poissonjP9StateTyped) Generates Poisson-distributed random

`unsigned int`

value.- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use**lambda**– Lambda (mean) parameter of Poisson distribution

- Returns:
Poisson-distributed random

`unsigned int`

value


-
uint4 hiprand_poisson4(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state, double lambda)[#](#_CPPv416hiprand_poisson4P27hiprandStatePhilox4_32_10_td) Generates four Poisson-distributed random

`unsigned int`

values.- Parameters:
**state**– Pointer to a Philox state to use**lambda**– Lambda (mean) parameter of Poisson distribution

- Returns:
Four Poisson-distributed random

`unsigned int`

values as`uint4`



-
template<class StateType>

unsigned int hiprand_discrete([StateType](#_CPPv4I0E16hiprand_discretejP9StateType29hiprandDiscreteDistribution_t)*state, hiprandDiscreteDistribution_t discrete_distribution)[#](#_CPPv4I0E16hiprand_discretejP9StateType29hiprandDiscreteDistribution_t) Generates random

`unsigned int`

value according to given discrete distribution.See also:

[hiprandCreatePoissonDistribution()](#group__hiprandhost_1ga82c3a994afd78ba0631cfd8c1b9a5a6a)- Template Parameters:
**StateType**– Random number generator state type.- Parameters:
**state**– Pointer to a RNG state to use**discrete_distribution**– Discrete distribution

- Returns:
Random

`unsigned int`

value


-
uint4 hiprand_discrete4(
[hiprandStatePhilox4_32_10_t](#_CPPv427hiprandStatePhilox4_32_10_t)*state, hiprandDiscreteDistribution_t discrete_distribution)[#](#_CPPv417hiprand_discrete4P27hiprandStatePhilox4_32_10_t29hiprandDiscreteDistribution_t) Generates four random

`unsigned int`

values according to given discrete distribution.See also:

[hiprandCreatePoissonDistribution()](#group__hiprandhost_1ga82c3a994afd78ba0631cfd8c1b9a5a6a)- Parameters:
**state**– Pointer to a Philox state to use**discrete_distribution**– Discrete distribution

- Returns:
Four random

`unsigned int`

values as`uint4`



-
inline
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandMakeMTGP32Constants(const[mtgp32_params_fast_t](#_CPPv420mtgp32_params_fast_t)params[],[mtgp32_kernel_params_t](#_CPPv422mtgp32_kernel_params_t)*p)[#](#_CPPv426hiprandMakeMTGP32ConstantsA_K20mtgp32_params_fast_tP22mtgp32_kernel_params_t) Loads parameters for MTGP32.

Loads parameters for use by kernel functions on the host-side and copies the results to the specified location in device memory.

- Parameters:
**params**–**[in]**Pointer to an array of type mtgp32_params_fast_t allocated in host memory**p**–**[out]**Pointer to a mtgp32_kernel_params_t structure allocated in device memory

- Returns:
HIPRAND_STATUS_ALLOCATION_FAILED if parameters could not be loaded

HIPRAND_STATUS_SUCCESS if parameters are loaded




-
inline
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandMakeMTGP32KernelState([hiprandStateMtgp32_t](#_CPPv420hiprandStateMtgp32_t)*s,[mtgp32_params_fast_t](#_CPPv420mtgp32_params_fast_t)params[], [[maybe_unused]][mtgp32_kernel_params_t](#_CPPv422mtgp32_kernel_params_t)*k, int n, unsigned long long seed)[#](#_CPPv428hiprandMakeMTGP32KernelStateP20hiprandStateMtgp32_tA_20mtgp32_params_fast_tP22mtgp32_kernel_params_tiy) Initializes MTGP32 states.

Initializes MTGP32 states on the host-side by allocating a state array in host memory, initializes that array, and copies the result to device memory.

On the cuRAND backend

`k`

must be initialized by calling[hiprandMakeMTGP32Constants()](#group__hipranddevice_1gae8611b506bf8323289abb2ecdcf936d9)with the the same`params`

On the rocRAND backend

`k`

is ignored

For maximum portability application should initialize

`k`

as required by cuRAND, but when only targeting the rocRAND backend it may be left uninitialized.- Parameters:
**s**–**[out]**Pointer to an array of states in device memory**params**–**[in]**Pointer to an array of type mtgp32_params_fast_t in host memory**k**–**[in]**Pointer to a mtgp32_kernel_params_t structure allocated in device memory**n**– Number of states to initialize**seed**– Seed value

- Returns:
HIPRAND_STATUS_ALLOCATION_FAILED if states could not be initialized

HIPRAND_STATUS_SUCCESS if states are initialized




-
HIPRAND_PHILOX4x32_DEFAULT_SEED

## C host API[#](#c-host-api)

-
*group*hiprandhost Defines

-
HIPRAND_VERSION
[#](#c.HIPRAND_VERSION) hipRAND library version

Version number may not be visible in the documentation.

`HIPRAND_VERSION % 100`

is the patch level,`HIPRAND_VERSION / 100 % 1000`

is the minor version,`HIPRAND_VERSION / 100000`

is the major version.For example, if

`HIPRAND_VERSION`

is`100500`

, then the major version is`1`

, the minor version is`5`

, and the patch level is`0`

.

-
HIPRAND_DEFAULT_MAX_BLOCK_SIZE
[#](#c.HIPRAND_DEFAULT_MAX_BLOCK_SIZE) Legacy macro for default maximum block size.

-
*Deprecated:* May be removed in a future version.


-

-
HIPRAND_DEFAULT_MIN_WARPS_PER_EU
[#](#c.HIPRAND_DEFAULT_MIN_WARPS_PER_EU) Default minimum number of warps per execution unit for kernel launches.


Typedefs

-
typedef enum
[hiprandStatus](#_CPPv413hiprandStatus)hiprandStatus_t[#](#_CPPv415hiprandStatus_t) hipRAND function call status type


-
typedef enum
[hiprandRngType](#_CPPv414hiprandRngType)hiprandRngType_t[#](#_CPPv416hiprandRngType_t) hipRAND generator type


-
typedef enum
[hiprandOrdering](#_CPPv415hiprandOrdering)hiprandOrdering_t[#](#_CPPv417hiprandOrdering_t) hipRAND generator ordering


-
typedef enum
[hiprandDirectionVectorSet](#_CPPv425hiprandDirectionVectorSet)hiprandDirectionVectorSet_t[#](#_CPPv427hiprandDirectionVectorSet_t) hipRAND vector set for quasirandom generators.


Enums

-
enum hiprandStatus
[#](#_CPPv413hiprandStatus) hipRAND function call status type

*Values:*-
enumerator HIPRAND_STATUS_SUCCESS
[#](#_CPPv4N13hiprandStatus22HIPRAND_STATUS_SUCCESSE) Success.


-
enumerator HIPRAND_STATUS_VERSION_MISMATCH
[#](#_CPPv4N13hiprandStatus31HIPRAND_STATUS_VERSION_MISMATCHE) Header file and linked library version do not match.


-
enumerator HIPRAND_STATUS_NOT_INITIALIZED
[#](#_CPPv4N13hiprandStatus30HIPRAND_STATUS_NOT_INITIALIZEDE) Generator not created.


-
enumerator HIPRAND_STATUS_ALLOCATION_FAILED
[#](#_CPPv4N13hiprandStatus32HIPRAND_STATUS_ALLOCATION_FAILEDE) Memory allocation failed.


-
enumerator HIPRAND_STATUS_TYPE_ERROR
[#](#_CPPv4N13hiprandStatus25HIPRAND_STATUS_TYPE_ERRORE) Generator type is wrong.


-
enumerator HIPRAND_STATUS_OUT_OF_RANGE
[#](#_CPPv4N13hiprandStatus27HIPRAND_STATUS_OUT_OF_RANGEE) Argument out of range.


-
enumerator HIPRAND_STATUS_LENGTH_NOT_MULTIPLE
[#](#_CPPv4N13hiprandStatus34HIPRAND_STATUS_LENGTH_NOT_MULTIPLEE) Requested size is not a multiple of quasirandom generator’s dimension, or requested size is not even (see

[hiprandGenerateNormal()](#group__hiprandhost_1gac2560fd9f148ecc860cb4b81a52362e0)), or pointer is misaligned (see[hiprandGenerateNormal()](#group__hiprandhost_1gac2560fd9f148ecc860cb4b81a52362e0))

-
enumerator HIPRAND_STATUS_DOUBLE_PRECISION_REQUIRED
[#](#_CPPv4N13hiprandStatus40HIPRAND_STATUS_DOUBLE_PRECISION_REQUIREDE) GPU does not have double precision.


-
enumerator HIPRAND_STATUS_LAUNCH_FAILURE
[#](#_CPPv4N13hiprandStatus29HIPRAND_STATUS_LAUNCH_FAILUREE) Kernel launch failure.


-
enumerator HIPRAND_STATUS_PREEXISTING_FAILURE
[#](#_CPPv4N13hiprandStatus34HIPRAND_STATUS_PREEXISTING_FAILUREE) Preexisting failure on library entry.


-
enumerator HIPRAND_STATUS_INITIALIZATION_FAILED
[#](#_CPPv4N13hiprandStatus36HIPRAND_STATUS_INITIALIZATION_FAILEDE) Initialization of HIP failed.


-
enumerator HIPRAND_STATUS_ARCH_MISMATCH
[#](#_CPPv4N13hiprandStatus28HIPRAND_STATUS_ARCH_MISMATCHE) Architecture mismatch, GPU does not support requested feature.


-
enumerator HIPRAND_STATUS_INTERNAL_ERROR
[#](#_CPPv4N13hiprandStatus29HIPRAND_STATUS_INTERNAL_ERRORE) Internal library error.


-
enumerator HIPRAND_STATUS_NOT_IMPLEMENTED
[#](#_CPPv4N13hiprandStatus30HIPRAND_STATUS_NOT_IMPLEMENTEDE) Feature not implemented yet.


-
enumerator HIPRAND_STATUS_SUCCESS

-
enum hiprandRngType
[#](#_CPPv414hiprandRngType) hipRAND generator type

*Values:*-
enumerator HIPRAND_RNG_PSEUDO_DEFAULT
[#](#_CPPv4N14hiprandRngType26HIPRAND_RNG_PSEUDO_DEFAULTE) Default pseudorandom generator.


-
enumerator HIPRAND_RNG_PSEUDO_XORWOW
[#](#_CPPv4N14hiprandRngType25HIPRAND_RNG_PSEUDO_XORWOWE) XORWOW pseudorandom generator.


-
enumerator HIPRAND_RNG_PSEUDO_MRG32K3A
[#](#_CPPv4N14hiprandRngType27HIPRAND_RNG_PSEUDO_MRG32K3AE) MRG32k3a pseudorandom generator.


-
enumerator HIPRAND_RNG_PSEUDO_MTGP32
[#](#_CPPv4N14hiprandRngType25HIPRAND_RNG_PSEUDO_MTGP32E) Mersenne Twister MTGP32 pseudorandom generator.


-
enumerator HIPRAND_RNG_PSEUDO_MT19937
[#](#_CPPv4N14hiprandRngType26HIPRAND_RNG_PSEUDO_MT19937E) Mersenne Twister 19937.


-
enumerator HIPRAND_RNG_PSEUDO_PHILOX4_32_10
[#](#_CPPv4N14hiprandRngType32HIPRAND_RNG_PSEUDO_PHILOX4_32_10E) PHILOX_4x32 (10 rounds) pseudorandom generator.


-
enumerator HIPRAND_RNG_QUASI_DEFAULT
[#](#_CPPv4N14hiprandRngType25HIPRAND_RNG_QUASI_DEFAULTE) Default quasirandom generator.


-
enumerator HIPRAND_RNG_QUASI_SOBOL32
[#](#_CPPv4N14hiprandRngType25HIPRAND_RNG_QUASI_SOBOL32E) Sobol32 quasirandom generator.


-
enumerator HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL32
[#](#_CPPv4N14hiprandRngType35HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL32E) Scrambled Sobol32 quasirandom generator.


-
enumerator HIPRAND_RNG_QUASI_SOBOL64
[#](#_CPPv4N14hiprandRngType25HIPRAND_RNG_QUASI_SOBOL64E) Sobol64 quasirandom generator.


-
enumerator HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL64
[#](#_CPPv4N14hiprandRngType35HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL64E) Scrambled Sobol64 quasirandom generator.


-
enumerator HIPRAND_RNG_PSEUDO_DEFAULT

-
enum hiprandOrdering
[#](#_CPPv415hiprandOrdering) hipRAND generator ordering

*Values:*-
enumerator HIPRAND_ORDERING_PSEUDO_BEST
[#](#_CPPv4N15hiprandOrdering28HIPRAND_ORDERING_PSEUDO_BESTE) Best ordering for pseudorandom results.


-
enumerator HIPRAND_ORDERING_PSEUDO_DEFAULT
[#](#_CPPv4N15hiprandOrdering31HIPRAND_ORDERING_PSEUDO_DEFAULTE) Specific default thread sequence for pseudorandom results, same as HIPRAND_ORDERING_PSEUDO_BEST.


-
enumerator HIPRAND_ORDERING_PSEUDO_SEEDED
[#](#_CPPv4N15hiprandOrdering30HIPRAND_ORDERING_PSEUDO_SEEDEDE) Specific seeding pattern for fast lower quality pseudorandom results.


-
enumerator HIPRAND_ORDERING_PSEUDO_LEGACY
[#](#_CPPv4N15hiprandOrdering30HIPRAND_ORDERING_PSEUDO_LEGACYE) Specific legacy sequence for pseudorandom results. This remains the same across releases, but not across backends.


-
enumerator HIPRAND_ORDERING_PSEUDO_DYNAMIC
[#](#_CPPv4N15hiprandOrdering31HIPRAND_ORDERING_PSEUDO_DYNAMICE) Specific ordering adjusted to the device it is being executed on, provides the best performance.


-
enumerator HIPRAND_ORDERING_QUASI_DEFAULT
[#](#_CPPv4N15hiprandOrdering30HIPRAND_ORDERING_QUASI_DEFAULTE) Specific n-dimensional ordering for quasirandom results.


-
enumerator HIPRAND_ORDERING_PSEUDO_BEST

-
enum hiprandDirectionVectorSet
[#](#_CPPv425hiprandDirectionVectorSet) hipRAND vector set for quasirandom generators.

*Values:*-
enumerator HIPRAND_DIRECTION_VECTORS_32_JOEKUO6
[#](#_CPPv4N25hiprandDirectionVectorSet36HIPRAND_DIRECTION_VECTORS_32_JOEKUO6E)

-
enumerator HIPRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6
[#](#_CPPv4N25hiprandDirectionVectorSet46HIPRAND_SCRAMBLED_DIRECTION_VECTORS_32_JOEKUO6E)

-
enumerator HIPRAND_DIRECTION_VECTORS_64_JOEKUO6
[#](#_CPPv4N25hiprandDirectionVectorSet36HIPRAND_DIRECTION_VECTORS_64_JOEKUO6E)

-
enumerator HIPRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6
[#](#_CPPv4N25hiprandDirectionVectorSet46HIPRAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6E)

-
enumerator HIPRAND_DIRECTION_VECTORS_32_JOEKUO6

Functions

-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandCreateGenerator(hiprandGenerator_t *generator,[hiprandRngType_t](#_CPPv416hiprandRngType_t)rng_type)[#](#_CPPv422hiprandCreateGeneratorP18hiprandGenerator_t16hiprandRngType_t) Creates a new random number generator.

Creates a new random number generator of type

`rng_type`

, and returns it in`generator`

. That generator will use GPU to create random numbers.Values for

`rng_type`

are:HIPRAND_RNG_PSEUDO_DEFAULT

HIPRAND_RNG_PSEUDO_XORWOW

HIPRAND_RNG_PSEUDO_MRG32K3A

HIPRAND_RNG_PSEUDO_MTGP32

HIPRAND_RNG_PSEUDO_MT19937

HIPRAND_RNG_PSEUDO_PHILOX4_32_10

HIPRAND_RNG_QUASI_DEFAULT

HIPRAND_RNG_QUASI_SOBOL32

HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL32

HIPRAND_RNG_QUASI_SOBOL64

HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL64


- Parameters:
**generator**– Pointer to generator**rng_type**– Type of random number generator to create

- Returns:
HIPRAND_STATUS_ALLOCATION_FAILED, if memory allocation failed

HIPRAND_STATUS_INITIALIZATION_FAILED if there was a problem setting up the GPU

HIPRAND_STATUS_VERSION_MISMATCH if the header file version does not match the dynamically linked library version

HIPRAND_STATUS_TYPE_ERROR if the value for

`rng_type`

is invalidHIPRAND_STATUS_NOT_IMPLEMENTED if generator of type

`rng_type`

is not implemented yetHIPRAND_STATUS_SUCCESS if generator was created successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandCreateGeneratorHost(hiprandGenerator_t *generator,[hiprandRngType_t](#_CPPv416hiprandRngType_t)rng_type)[#](#_CPPv426hiprandCreateGeneratorHostP18hiprandGenerator_t16hiprandRngType_t) Creates a new random number generator on host.

Creates a new host random number generator of type

`rng_type`

and returns it in`generator`

. Created generator will use host CPU to generate random numbers.Values for

`rng_type`

are:HIPRAND_RNG_PSEUDO_DEFAULT

HIPRAND_RNG_PSEUDO_XORWOW

HIPRAND_RNG_PSEUDO_MRG32K3A

HIPRAND_RNG_PSEUDO_MTGP32

HIPRAND_RNG_PSEUDO_MT19937

HIPRAND_RNG_PSEUDO_PHILOX4_32_10

HIPRAND_RNG_QUASI_DEFAULT

HIPRAND_RNG_QUASI_SOBOL32

HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL32

HIPRAND_RNG_QUASI_SOBOL64

HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL64


- Parameters:
**generator**– Pointer to generator**rng_type**– Type of random number generator to create

- Returns:
HIPRAND_STATUS_ALLOCATION_FAILED, if memory allocation failed

HIPRAND_STATUS_VERSION_MISMATCH if the header file version does not match the dynamically linked library version

HIPRAND_STATUS_TYPE_ERROR if the value for

`rng_type`

is invalidHIPRAND_STATUS_NOT_IMPLEMENTED if host generator of type

`rng_type`

is not implemented yetHIPRAND_STATUS_SUCCESS if generator was created successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandDestroyGenerator(hiprandGenerator_t generator)[#](#_CPPv423hiprandDestroyGenerator18hiprandGenerator_t) Destroys random number generator.

Destroys random number generator and frees related memory.

- Parameters:
**generator**– Generator to be destroyed- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_SUCCESS if generator was destroyed successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerate(hiprandGenerator_t generator, unsigned int *output_data, size_t n)[#](#_CPPv415hiprandGenerate18hiprandGenerator_tPj6size_t) Generates uniformly distributed 32-bit unsigned integers.

Generates

`n`

uniformly distributed 32-bit unsigned integers and saves them to`output_data`

.Generated numbers are between

`0`

and`2^32`

, including`0`

and excluding`2^32`

.Note:

`generator`

must be not be of type`HIPRAND_RNG_QUASI_SOBOL64`

or`HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL64`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of 32-bit unsigned integers to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateChar(hiprandGenerator_t generator, unsigned char *output_data, size_t n)[#](#_CPPv419hiprandGenerateChar18hiprandGenerator_tPh6size_t) Generates uniformly distributed 8-bit unsigned integers.

Generates

`n`

uniformly distributed 8-bit unsigned integers and saves them to`output_data`

.Generated numbers are between

`0`

and`2^8`

, including`0`

and excluding`2^8`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of 8-bit unsigned integers to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateShort(hiprandGenerator_t generator, unsigned short *output_data, size_t n)[#](#_CPPv420hiprandGenerateShort18hiprandGenerator_tPt6size_t) Generates uniformly distributed 16-bit unsigned integers.

Generates

`n`

uniformly distributed 16-bit unsigned integers and saves them to`output_data`

.Generated numbers are between

`0`

and`2^16`

, including`0`

and excluding`2^16`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of 16-bit unsigned integers to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateLongLong(hiprandGenerator_t generator, unsigned long long *output_data, size_t n)[#](#_CPPv423hiprandGenerateLongLong18hiprandGenerator_tPy6size_t) Generates uniformly distributed 64-bit unsigned integers.

Generates

`n`

uniformly distributed 64-bit unsigned integers and saves them to`output_data`

.Generated numbers are between

`0`

and`2^64`

, including`0`

and excluding`2^64`

.Note:

`generator`

must be of type`HIPRAND_RNG_QUASI_SOBOL64`

or`HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL64`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of 64-bit unsigned integers to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateUniform(hiprandGenerator_t generator, float *output_data, size_t n)[#](#_CPPv422hiprandGenerateUniform18hiprandGenerator_tPf6size_t) Generates uniformly distributed floats.

Generates

`n`

uniformly distributed 32-bit floating-point values and saves them to`output_data`

.Generated numbers are between

`0.0f`

and`1.0f`

, excluding`0.0f`

and including`1.0f`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of floats to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateUniformDouble(hiprandGenerator_t generator, double *output_data, size_t n)[#](#_CPPv428hiprandGenerateUniformDouble18hiprandGenerator_tPd6size_t) Generates uniformly distributed double-precision floating-point values.

Generates

`n`

uniformly distributed 64-bit double-precision floating-point values and saves them to`output_data`

.Generated numbers are between

`0.0`

and`1.0`

, excluding`0.0`

and including`1.0`

.Note: When

`generator`

is of type:`HIPRAND_RNG_PSEUDO_MRG32K3A`

,`HIPRAND_RNG_PSEUDO_MTGP32`

,`HIPRAND_RNG_QUASI_SOBOL32`

, or`HIPRAND_RNG_QUASI_SCRAMBLED_SOBOL32`

then the returned`double`

values are generated from only 32 random bits each (one`unsigned int`

value per one generated`double`

).- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of floats to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateUniformHalf(hiprandGenerator_t generator, half *output_data, size_t n)[#](#_CPPv426hiprandGenerateUniformHalf18hiprandGenerator_tP4half6size_t) Generates uniformly distributed half-precision floating-point values.

Generates

`n`

uniformly distributed 16-bit half-precision floating-point values and saves them to`output_data`

.Generated numbers are between

`0.0`

and`1.0`

, excluding`0.0`

and including`1.0`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of halfs to generate

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateNormal(hiprandGenerator_t generator, float *output_data, size_t n, float mean, float stddev)[#](#_CPPv421hiprandGenerateNormal18hiprandGenerator_tPf6size_tff) Generates normally distributed floats.

Generates

`n`

normally distributed 32-bit floating-point values and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of floats to generate**mean**– Mean value of normal distribution**stddev**– Standard deviation value of normal distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not even,`output_data`

is not aligned to`sizeof(float2)`

bytes, or`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateNormalDouble(hiprandGenerator_t generator, double *output_data, size_t n, double mean, double stddev)[#](#_CPPv427hiprandGenerateNormalDouble18hiprandGenerator_tPd6size_tdd) Generates normally distributed doubles.

Generates

`n`

normally distributed 64-bit double-precision floating-point numbers and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of doubles to generate**mean**– Mean value of normal distribution**stddev**– Standard deviation value of normal distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not even,`output_data`

is not aligned to`sizeof(double2)`

bytes, or`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateNormalHalf(hiprandGenerator_t generator, half *output_data, size_t n, half mean, half stddev)[#](#_CPPv425hiprandGenerateNormalHalf18hiprandGenerator_tP4half6size_t4half4half) Generates normally distributed halfs.

Generates

`n`

normally distributed 16-bit half-precision floating-point numbers and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of halfs to generate**mean**– Mean value of normal distribution**stddev**– Standard deviation value of normal distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not even,`output_data`

is not aligned to`sizeof(half2)`

bytes, or`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateLogNormal(hiprandGenerator_t generator, float *output_data, size_t n, float mean, float stddev)[#](#_CPPv424hiprandGenerateLogNormal18hiprandGenerator_tPf6size_tff) Generates log-normally distributed floats.

Generates

`n`

log-normally distributed 32-bit floating-point values and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of floats to generate**mean**– Mean value of log normal distribution**stddev**– Standard deviation value of log normal distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not even,`output_data`

is not aligned to`sizeof(float2)`

bytes, or`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateLogNormalDouble(hiprandGenerator_t generator, double *output_data, size_t n, double mean, double stddev)[#](#_CPPv430hiprandGenerateLogNormalDouble18hiprandGenerator_tPd6size_tdd) Generates log-normally distributed doubles.

Generates

`n`

log-normally distributed 64-bit double-precision floating-point values and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of doubles to generate**mean**– Mean value of log normal distribution**stddev**– Standard deviation value of log normal distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not even,`output_data`

is not aligned to`sizeof(double2)`

bytes, or`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateLogNormalHalf(hiprandGenerator_t generator, half *output_data, size_t n, half mean, half stddev)[#](#_CPPv428hiprandGenerateLogNormalHalf18hiprandGenerator_tP4half6size_t4half4half) Generates log-normally distributed halfs.

Generates

`n`

log-normally distributed 16-bit half-precision floating-point values and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of halfs to generate**mean**– Mean value of log normal distribution**stddev**– Standard deviation value of log normal distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not even,`output_data`

is not aligned to`sizeof(half2)`

bytes, or`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGeneratePoisson(hiprandGenerator_t generator, unsigned int *output_data, size_t n, double lambda)[#](#_CPPv422hiprandGeneratePoisson18hiprandGenerator_tPj6size_td) Generates Poisson-distributed 32-bit unsigned integers.

Generates

`n`

Poisson-distributed 32-bit unsigned integers and saves them to`output_data`

.- Parameters:
**generator**– Generator to use**output_data**– Pointer to memory to store generated numbers**n**– Number of 32-bit unsigned integers to generate**lambda**– lambda for the Poisson distribution

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_LAUNCH_FAILURE if generator failed to launch kernel

HIPRAND_STATUS_OUT_OF_RANGE if lambda is non-positive

HIPRAND_STATUS_LENGTH_NOT_MULTIPLE if

`n`

is not a multiple of the dimension of used quasi-random generatorHIPRAND_STATUS_SUCCESS if random numbers were successfully generated




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGenerateSeeds(hiprandGenerator_t generator)[#](#_CPPv420hiprandGenerateSeeds18hiprandGenerator_t) Initializes the generator’s state on GPU or host.

Initializes the generator’s state on GPU or host.

If

[hiprandGenerateSeeds()](#group__hiprandhost_1ga0fa18f793ad80b753be53f4a95a94f2b)was not called for a generator, it will be automatically called by functions which generates random numbers like[hiprandGenerate()](#group__hiprandhost_1ga9ed176ab4295d6d2c19b0b976941b124),[hiprandGenerateUniform()](#group__hiprandhost_1ga041797e2c1b813ab558015f07647534a),[hiprandGenerateNormal()](#group__hiprandhost_1gac2560fd9f148ecc860cb4b81a52362e0)etc.- Parameters:
**generator**– Generator to initialize- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was never created

HIPRAND_STATUS_PREEXISTING_FAILURE if there was an existing error from a previous kernel launch

HIPRAND_STATUS_LAUNCH_FAILURE if the kernel launch failed for any reason

HIPRAND_STATUS_SUCCESS if the seeds were generated successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandSetStream(hiprandGenerator_t generator, hipStream_t stream)[#](#_CPPv416hiprandSetStream18hiprandGenerator_t11hipStream_t) Sets the current stream for kernel launches.

Sets the current stream for all kernel launches of the generator. All functions will use this stream.

- Parameters:
**generator**– Generator to modify**stream**– Stream to use or NULL for default stream

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_SUCCESS if stream was set successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandSetPseudoRandomGeneratorSeed(hiprandGenerator_t generator, unsigned long long seed)[#](#_CPPv435hiprandSetPseudoRandomGeneratorSeed18hiprandGenerator_ty) Sets the seed of a pseudo-random number generator.

Sets the seed of the pseudo-random number generator.

This operation resets the generator’s internal state.

This operation does not change the generator’s offset.


- Parameters:
**generator**– Pseudo-random number generator**seed**– New seed value

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_TYPE_ERROR if the generator is a quasi random number generator

HIPRAND_STATUS_SUCCESS if seed was set successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandSetGeneratorOffset(hiprandGenerator_t generator, unsigned long long offset)[#](#_CPPv425hiprandSetGeneratorOffset18hiprandGenerator_ty) Sets the offset of a random number generator.

Sets the absolute offset of the random number generator.

This operation resets the generator’s internal state.

This operation does not change the generator’s seed.


Absolute offset cannot be set if generator’s type is HIPRAND_RNG_PSEUDO_MTGP32 or HIPRAND_RNG_PSEUDO_MT19937.

- Parameters:
**generator**– Random number generator**offset**– New absolute offset

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_SUCCESS if offset was successfully set

HIPRAND_STATUS_TYPE_ERROR if generator’s type is HIPRAND_RNG_PSEUDO_MTGP32 or HIPRAND_RNG_PSEUDO_MT19937




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandSetGeneratorOrdering(hiprandGenerator_t generator,[hiprandOrdering_t](#_CPPv417hiprandOrdering_t)order)[#](#_CPPv427hiprandSetGeneratorOrdering18hiprandGenerator_t17hiprandOrdering_t) Sets the ordering of a random number generator.

Sets the ordering of the results of a random number generator.

This operation resets the generator’s internal state.

This operation does not change the generator’s seed.


The ordering choices for pseudorandom sequences are HIPRAND_ORDERING_PSEUDO_DEFAULT and HIPRAND_ORDERING_PSEUDO_LEGACY. The default ordering is HIPRAND_ORDERING_PSEUDO_DEFAULT, which is equal to HIPRAND_ORDERING_PSEUDO_LEGACY for now.

For quasirandom sequences there is only one ordering, HIPRAND_ORDERING_QUASI_DEFAULT.

- Parameters:
**generator**– Random number generator**order**– New ordering of results

- Returns:
HIPRAND_STATUS_NOT_INITIALIZED if the generator was not initialized

HIPRAND_STATUS_OUT_OF_RANGE if the ordering is not valid

HIPRAND_STATUS_SUCCESS if the ordering was successfully set

HIPRAND_STATUS_TYPE_ERROR if generator’s type is not valid




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandSetQuasiRandomGeneratorDimensions(hiprandGenerator_t generator, unsigned int dimensions)[#](#_CPPv440hiprandSetQuasiRandomGeneratorDimensions18hiprandGenerator_tj) Set the number of dimensions of a quasi-random number generator.

Set the number of dimensions of a quasi-random number generator. Supported values of

`dimensions`

are 1 to 20000.This operation resets the generator’s internal state.

This operation does not change the generator’s offset.


- Parameters:
**generator**– Quasi-random number generator**dimensions**– Number of dimensions

- Returns:
HIPRAND_STATUS_NOT_CREATED if the generator wasn’t created

HIPRAND_STATUS_TYPE_ERROR if the generator is not a quasi-random number generator

HIPRAND_STATUS_OUT_OF_RANGE if

`dimensions`

is out of rangeHIPRAND_STATUS_SUCCESS if the number of dimensions was set successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGetVersion(int *version)[#](#_CPPv417hiprandGetVersionPi) Returns the version number of the cuRAND or rocRAND library.

Returns in

`version`

the version number of the underlying cuRAND or rocRAND library.- Parameters:
**version**– Version of the library- Returns:
HIPRAND_STATUS_OUT_OF_RANGE if

`version`

is NULLHIPRAND_STATUS_SUCCESS if the version number was successfully returned




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandCreatePoissonDistribution(double lambda, hiprandDiscreteDistribution_t *discrete_distribution)[#](#_CPPv432hiprandCreatePoissonDistributiondP29hiprandDiscreteDistribution_t) Construct the histogram for a Poisson distribution.

Construct the histogram for the Poisson distribution with lambda

`lambda`

.- Parameters:
**lambda**– lambda for the Poisson distribution**discrete_distribution**– pointer to the histogram in device memory

- Returns:
HIPRAND_STATUS_ALLOCATION_FAILED if memory could not be allocated

HIPRAND_STATUS_OUT_OF_RANGE if

`discrete_distribution`

pointer was nullHIPRAND_STATUS_OUT_OF_RANGE if lambda is non-positive

HIPRAND_STATUS_SUCCESS if the histogram was constructed successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandDestroyDistribution(hiprandDiscreteDistribution_t discrete_distribution)[#](#_CPPv426hiprandDestroyDistribution29hiprandDiscreteDistribution_t) Destroy the histogram array for a discrete distribution.

Destroy the histogram array for a discrete distribution created by hiprandCreatePoissonDistribution.

- Parameters:
**discrete_distribution**– pointer to the histogram in device memory- Returns:
HIPRAND_STATUS_OUT_OF_RANGE if

`discrete_distribution`

was nullHIPRAND_STATUS_SUCCESS if the histogram was destroyed successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGetDirectionVectors32([hiprandDirectionVectors32_t](#_CPPv427hiprandDirectionVectors32_t)**vectors,[hiprandDirectionVectorSet_t](#_CPPv427hiprandDirectionVectorSet_t)set)[#](#_CPPv428hiprandGetDirectionVectors32PP27hiprandDirectionVectors32_t27hiprandDirectionVectorSet_t) Retrieves the Sobol 32 direction vector array specified by

`set`

.- Parameters:
**vectors**– Pointer to the Sobol 32 direction vector array.**set**– Specifies which hipRAND vector set for quasirandom generators to retrieve.

- Returns:
HIPRAND_STATUS_OUT_OF_RANGE if

`set`

is invalidHIPRAND_STATUS_SUCCESS if

`vectors`

was set successfully



-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGetDirectionVectors64([hiprandDirectionVectors64_t](#_CPPv427hiprandDirectionVectors64_t)**vectors,[hiprandDirectionVectorSet_t](#_CPPv427hiprandDirectionVectorSet_t)set)[#](#_CPPv428hiprandGetDirectionVectors64PP27hiprandDirectionVectors64_t27hiprandDirectionVectorSet_t) Retrieves the Sobol 64 direction vector array specified by

`set`

.- Parameters:
**vectors**– Pointer to the Sobol 64 direction vector array.**set**– Specifies which hipRAND vector set for quasirandom generators to retrieve.

- Returns:
HIPRAND_STATUS_OUT_OF_RANGE if

`set`

is invalidHIPRAND_STATUS_SUCCESS if

`vectors`

was set successfully



-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGetScrambleConstants32(const unsigned int **constants)[#](#_CPPv429hiprandGetScrambleConstants32PPKj) Retrieves the scramble constants for 32-bit scrambled Sobol generation.

- Parameters:
**constants**– Pointer to the constants pointer.- Returns:
HIPRAND_STATUS_SUCCESS if the pointer was set successfully




-
[hiprandStatus_t](#_CPPv415hiprandStatus_t)hiprandGetScrambleConstants64(const unsigned long long **constants)[#](#_CPPv429hiprandGetScrambleConstants64PPKy) Retrieves the scramble constants for 64-bit scrambled Sobol generation.

- Parameters:
**constants**– Pointer to the constants pointer.- Returns:
HIPRAND_STATUS_SUCCESS if the pointer was set successfully




-
HIPRAND_VERSION

## C++ host API wrapper[#](#c-host-api-wrapper)

-
*group*hiprandhostcpp Typedefs

-
typedef philox4x32_10_engine philox4x32_10
[#](#_CPPv413philox4x32_10) Typedef of

[hiprand_cpp::philox4x32_10_engine](#classhiprand__cpp_1_1philox4x32__10__engine)PRNG engine with default seed ([HIPRAND_PHILOX4x32_DEFAULT_SEED](#group__hipranddevice_1gaffe282ce91ff23e56e033fe1014bde39)).

-
typedef xorwow_engine xorwow
[#](#_CPPv46xorwow) Typedef of

[hiprand_cpp::xorwow_engine](#classhiprand__cpp_1_1xorwow__engine)PRNG engine with default seed ([HIPRAND_XORWOW_DEFAULT_SEED](#group__hipranddevice_1ga77b588f7a94fc7f1d7822b81ac945acb)).

-
typedef mrg32k3a_engine mrg32k3a
[#](#_CPPv48mrg32k3a) Typedef of

[hiprand_cpp::mrg32k3a_engine](#classhiprand__cpp_1_1mrg32k3a__engine)PRNG engine with default seed ([HIPRAND_MRG32K3A_DEFAULT_SEED](#group__hipranddevice_1gafeb5d0737ded8005bf8a1f93782ca754)).

-
typedef mtgp32_engine mtgp32
[#](#_CPPv46mtgp32) Typedef of

[hiprand_cpp::mtgp32_engine](#classhiprand__cpp_1_1mtgp32__engine)PRNG engine with default seed ([HIPRAND_MTGP32_DEFAULT_SEED](#group__hipranddevice_1gaca104632d34f05d6a7243a98d4036462)).

-
typedef mt19937_engine mt19937
[#](#_CPPv47mt19937) Typedef of

[hiprand_cpp::mt19937_engine](#classhiprand__cpp_1_1mt19937__engine)PRNG engine with default seed ([HIPRAND_MT19937_DEFAULT_SEED](#group__hipranddevice_1gaaafd87b238238db36b195e6464ccb9fd)).

-
typedef sobol32_engine sobol32
[#](#_CPPv47sobol32) Typedef of

[hiprand_cpp::sobol32_engine](#classhiprand__cpp_1_1sobol32__engine)QRNG engine with default number of dimensions (1).

-
typedef scrambled_sobol32_engine scrambled_sobol32
[#](#_CPPv417scrambled_sobol32) Typedef of

[hiprand_cpp::scrambled_sobol32_engine](#classhiprand__cpp_1_1scrambled__sobol32__engine)QRNG engine with default number of dimensions (1).

-
typedef sobol64_engine sobol64
[#](#_CPPv47sobol64) Typedef of

[hiprand_cpp::sobol64_engine](#classhiprand__cpp_1_1sobol64__engine)QRNG engine with default number of dimensions (1).

-
typedef scrambled_sobol64_engine scrambled_sobol64
[#](#_CPPv417scrambled_sobol64) Typedef of

[hiprand_cpp::scrambled_sobol64_engine](#classhiprand__cpp_1_1scrambled__sobol64__engine)QRNG engine with default number of dimensions (1).

-
typedef std::random_device random_device
[#](#_CPPv413random_device) A non-deterministic uniform random number generator.

hiprand_cpp::random_device is non-deterministic uniform random number generator, or a pseudo-random number engine if there is no support for non-deterministic random number generation. It’s implemented as a typedef of std::random_device.

For practical use hiprand_cpp::random_device is generally only used to seed a PRNG such as

[hiprand_cpp::mtgp32_engine](#classhiprand__cpp_1_1mtgp32__engine).Example:

#include <hiprand/hiprand.hpp> int main() { const size_t size = 8192; unsigned int * output; hipMalloc(&output, size * sizeof(unsigned int)); hiprand_cpp::random_device rd; hiprand_cpp::mtgp32 engine(rd()); // seed engine with a real random value, if available hiprand_cpp::normal_distribution<float> dist(0.0, 1.5); dist(engine, output, size); }


Functions

-
inline int version()
[#](#_CPPv47versionv) Returns hipRAND version.

- Returns:
hipRAND version number as an

`int`

value.


-
class error : public std::exception
[#](#_CPPv4N11hiprand_cpp5errorE) *#include <hiprand.hpp>*A run-time hipRAND error.

The error class represents an error returned by a hipRAND function.


-
template<class IntType = unsigned int>

class uniform_int_distribution[#](#_CPPv4I0EN11hiprand_cpp24uniform_int_distributionE) *#include <hiprand.hpp>*Produces random integer values uniformly distributed on the interval [0, 2^(sizeof(IntType)*8) - 1].

- Template Parameters:
**IntType**– type of generated values. Only`unsigned char`

,`unsigned short`

,`unsigned int`

,`unsigned long long int`

are supported.


-
template<class RealType = float>

class uniform_real_distribution[#](#_CPPv4I0EN11hiprand_cpp25uniform_real_distributionE) *#include <hiprand.hpp>*Produces random floating-point values uniformly distributed on the interval (0, 1].

- Template Parameters:
**RealType**– type of generated values. Only`float`

,`double`

and`half`

types are supported.


-
template<class RealType = float>

class normal_distribution[#](#_CPPv4I0EN11hiprand_cpp19normal_distributionE) *#include <hiprand.hpp>*Produces random numbers according to a normal distribution.

- Template Parameters:
**RealType**– type of generated values. Only`float`

,`double`

and`half`

types are supported.


-
template<class RealType = float>

class lognormal_distribution[#](#_CPPv4I0EN11hiprand_cpp22lognormal_distributionE) *#include <hiprand.hpp>*Produces positive random numbers according to a log-normal distribution.

- Template Parameters:
**RealType**– type of generated values. Only`float`

,`double`

and`half`

types are supported.


-
template<class IntType = unsigned int>

class poisson_distribution[#](#_CPPv4I0EN11hiprand_cpp20poisson_distributionE) *#include <hiprand.hpp>*Produces random non-negative integer values distributed according to Poisson distribution.

- Template Parameters:
**IntType**– type of generated values. Only`unsinged`

`int`

type is supported.


-
template<unsigned long long DefaultSeed = HIPRAND_PHILOX4x32_DEFAULT_SEED>

class philox4x32_10_engine[#](#_CPPv4I_yEN11hiprand_cpp20philox4x32_10_engineE) *#include <hiprand.hpp>*Pseudorandom number engine based Philox algorithm.

[philox4x32_10_engine](#classhiprand__cpp_1_1philox4x32__10__engine)implements a Counter-based random number generator called Philox, which was developed by a group at D. E. Shaw Research. It generates random numbers of type`unsigned`

`int`

on the interval [0; 2^32 - 1]. Random numbers are generated in sets of four.

-
template<unsigned long long DefaultSeed = HIPRAND_XORWOW_DEFAULT_SEED>

class xorwow_engine[#](#_CPPv4I_yEN11hiprand_cpp13xorwow_engineE) *#include <hiprand.hpp>*Pseudorandom number engine based XORWOW algorithm.

[xorwow_engine](#classhiprand__cpp_1_1xorwow__engine)is a xorshift pseudorandom number engine based on XORWOW algorithm, which was presented by George Marsaglia in “Xorshift RNGs” paper published in Journal of Statistical Software. It produces random numbers of type`unsigned`

`int`

on the interval [0; 2^32 - 1].

-
template<unsigned long long DefaultSeed = HIPRAND_MRG32K3A_DEFAULT_SEED>

class mrg32k3a_engine[#](#_CPPv4I_yEN11hiprand_cpp15mrg32k3a_engineE) *#include <hiprand.hpp>*Pseudorandom number engine based MRG32k3a CMRG.

[mrg32k3a_engine](#classhiprand__cpp_1_1mrg32k3a__engine)is an implementation of MRG32k3a pseudorandom number generator, which is a Combined Multiple Recursive Generator (CMRG) created by Pierre L’Ecuyer. It produces random 32-bit`unsigned`

`int`

values on the interval [0; 2^32 - 1].

-
template<unsigned long long DefaultSeed = HIPRAND_MTGP32_DEFAULT_SEED>

class mtgp32_engine[#](#_CPPv4I_yEN11hiprand_cpp13mtgp32_engineE) *#include <hiprand.hpp>*Pseudorandom number engine based on Mersenne Twister for Graphic Processors algorithm.

[mtgp32_engine](#classhiprand__cpp_1_1mtgp32__engine)is a random number engine based on Mersenne Twister for Graphic Processors algorithm, which is a version of well-known Mersenne Twister algorithm. It produces high quality random numbers of type`unsigned`

`int`

on the interval [0; 2^32 - 1].

-
template<unsigned long long DefaultSeed = HIPRAND_MT19937_DEFAULT_SEED>

class mt19937_engine[#](#_CPPv4I_yEN11hiprand_cpp14mt19937_engineE) *#include <hiprand.hpp>*Pseudorandom number engine based on Mersenne Twister.

[mt19937_engine](#classhiprand__cpp_1_1mt19937__engine)is a random number engine based on the well-known Mersenne Twister algorithm. It produces high quality random numbers of type`unsigned`

`int`

on the interval [0; 2^32 - 1].

-
template<unsigned int DefaultNumDimensions = 1>

class sobol32_engine[#](#_CPPv4I_jEN11hiprand_cpp14sobol32_engineE) *#include <hiprand.hpp>*Sobol’s quasi-random sequence generator.

[sobol32_engine](#classhiprand__cpp_1_1sobol32__engine)is quasi-random number engine which produced Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0; 2^32 - 1].

-
template<unsigned int DefaultNumDimensions = 1>

class scrambled_sobol32_engine[#](#_CPPv4I_jEN11hiprand_cpp24scrambled_sobol32_engineE) *#include <hiprand.hpp>*Sobol’s quasi-random sequence generator.

[scrambled_sobol32_engine](#classhiprand__cpp_1_1scrambled__sobol32__engine)is a quasi-random number engine which produces scrambled Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0; 2^32 - 1].

-
template<unsigned int DefaultNumDimensions = 1>

class sobol64_engine[#](#_CPPv4I_jEN11hiprand_cpp14sobol64_engineE) *#include <hiprand.hpp>*Sobol’s quasi-random sequence generator.

[sobol64_engine](#classhiprand__cpp_1_1sobol64__engine)is a quasi-random number engine which produced Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0; 2^64 - 1].

-
template<unsigned int DefaultNumDimensions = 1>

class scrambled_sobol64_engine[#](#_CPPv4I_jEN11hiprand_cpp24scrambled_sobol64_engineE) *#include <hiprand.hpp>*Sobol’s quasi-random sequence generator.

[scrambled_sobol64_engine](#classhiprand__cpp_1_1scrambled__sobol64__engine)is a quasi-random number engine which produces scrambled Sobol sequences. This implementation supports generating sequences in up to 20,000 dimensions. The engine produces random unsigned integers on the interval [0; 2^64 - 1].

-
typedef philox4x32_10_engine philox4x32_10
