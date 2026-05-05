---
title: "hipFFTW API usage &#8212; hipFFT 1.0.22 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipFFT/en/latest/reference/hipfftw-api-usage.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T15:07:20.774295+00:00
content_hash: "696f05c725584374"
---

# hipFFTW API usage[#](#hipfftw-api-usage)

This section describes how to use the hipFFTW library API. The hipFFTW
API is a partial reproduction of the [FFTW](https://www.fftw.org/) API.

## Data types[#](#data-types)

Similarly to [FFTW](https://www.fftw.org/), hipFFTW uses the following specific types.

-
typedef double fftw_complex[2]
[#](#_CPPv412fftw_complex) Type for double-precision complex floating-point values.

Note

`fftw_complex`

is defined equivalent to`double complex`

in applications that include the standard`complex.h`

prior to`hipfft/hipfftw.h`

.

-
typedef float fftwf_complex[2]
[#](#_CPPv413fftwf_complex) Single-precision equivalent of

[fftw_complex](#hipfftw_8h_1ae1609d659a2dd36b5fa2184246b1743a).

-
typedef struct fftw_plan_s *fftw_plan
[#](#_CPPv49fftw_plan) Type for double-precision hipFFTW plans.


## Constant values[#](#constant-values)

### Flag values[#](#flag-values)

All the hipFFTW [plan creation functions](#hipfftw-plan-creation) request an `unsigned flags`

argument.
The value of that argument conditions what hipFFTW will consider when creating the requested plan. Valid
values are bitwise OR of zero of more of the following constant values.

-
FFTW_MEASURE
[#](#c.FFTW_MEASURE) Flag value allowing hipFFTW to compute (possibly many) FFTs at plan creation to find the optimal configuration, using the input and output data buffers set at plan creation (hence possibly overwriting data therein).


-
FFTW_DESTROY_INPUT
[#](#c.FFTW_DESTROY_INPUT) Flag value allowing an out-of-place hipFFTW plan to overwrite its input buffer data at execution.


-
FFTW_UNALIGNED
[#](#c.FFTW_UNALIGNED) Flag value ruling out any alignment assumption for the input and output buffers to be used at plan execution.


-
FFTW_CONSERVE_MEMORY
[#](#c.FFTW_CONSERVE_MEMORY) Flag value instructing plans to prefer configurations minimizing their memory footprint.


-
FFTW_EXHAUSTIVE
[#](#c.FFTW_EXHAUSTIVE) Flag value equivalent to

[FFTW_PATIENT](#hipfftw_8h_1a98f8ab33cff17c40865428f652b7ea8e), enabling the largest possible set of plan configurations to be considered in the measurements.

-
FFTW_PRESERVE_INPUT
[#](#c.FFTW_PRESERVE_INPUT) Flag value forbidding an out-of-place hipFFTW plan to overwrite its input buffer data at execution.

Note

This flag value is not supported for out-of-place multidimensional real inverse tranforms.


-
FFTW_PATIENT
[#](#c.FFTW_PATIENT) Flag value equivalent to

[FFTW_MEASURE](#hipfftw_8h_1a74838abba9d888010289fc8039b188bd), enabling a larger-than-default set of plan configurations to be considered in the measurements.

-
FFTW_ESTIMATE
[#](#c.FFTW_ESTIMATE) Flag value enforcing hipFFTW to use a heuristric when selecting the plan configuration, thereby ruling out measurements and leaving input and output buffers untouched.


-
FFTW_WISDOM_ONLY
[#](#c.FFTW_WISDOM_ONLY) Flag instructing hipFFTW to query the requested plan from an on-disk database file (“wisdom”). If not found therein, no plan is created.

Note

This flag value is not supported by hipFFTW.


Note

Even if seemingly accepted, flag values are currently ignored by hipFFTW. In particular, note that:

no measurement is ever done at plan creation (plan configurations are chosen based on heuristics);

preservation of input data is never guaranteed;

requests for a minimized memory footprint are ignored;


with the current status of hipFFTW.

### Sign values[#](#sign-values)

The hipFFTW [plan creation functions](#hipfftw-plan-creation) for complex transforms request an `int sign`

argument. This argument determines whether the plan being created is meant to compute forward or backward (inverse)
discrete Fourier transforms. Valid values of that argument are either of the following constant values.

-
FFTW_FORWARD
[#](#c.FFTW_FORWARD) Exponent

`sign`

value to be used for forward discrete Fourier transforms.

-
FFTW_BACKWARD
[#](#c.FFTW_BACKWARD) Exponent

`sign`

value to be used for backward (inverse) discrete Fourier transforms.

## Buffer management[#](#buffer-management)

hipFFTW supports the following buffer-management functions.

-
void *fftw_malloc(size_t n)
[#](#_CPPv411fftw_malloc6size_t) Allocates a data buffer accessible by the host.

Remark

The returned base address is at least 64-bit aligned.

- Parameters:
**n**–**[in]**number of bytes desired for the buffer.- Returns:
a pointer to the base address of the allocated memory block upon success (

`nullptr`

otherwise).


-
void *fftwf_malloc(size_t n)
[#](#_CPPv412fftwf_malloc6size_t) This function is strictly equivalent to

[fftw_malloc](#hipfftw_8h_1a04673fa22a7c6986e22576d58de7dec2).

-
double *fftw_alloc_real(size_t n)
[#](#_CPPv415fftw_alloc_real6size_t) This function is strictly equivalent to

`(double*) fftw_malloc(n * sizeof(double))`


-
float *fftwf_alloc_real(size_t n)
[#](#_CPPv416fftwf_alloc_real6size_t) This function is strictly equivalent to

`(float*) fftw_malloc(n * sizeof(float))`


-
[fftw_complex](#_CPPv412fftw_complex)*fftw_alloc_complex(size_t n)[#](#_CPPv418fftw_alloc_complex6size_t) This function is strictly equivalent to

`(fftw_complex*) fftw_malloc(n * sizeof(fftw_complex))`


-
[fftwf_complex](#_CPPv413fftwf_complex)*fftwf_alloc_complex(size_t n)[#](#_CPPv419fftwf_alloc_complex6size_t) This function is strictly equivalent to

`(fftwf_complex*) fftw_malloc(n * sizeof(fftwf_complex))`


-
void fftw_free(void *p)
[#](#_CPPv49fftw_freePv) Frees a buffer previously allocated by any of the allocation functions above.

- Parameters:
**p**–**[in]**pointer to the base address of the buffer to be freed.


The memory blocks allocated by any of the above `{fftw,fftwf}_{malloc,alloc_real,alloc_complex}`

are always directly accessible to the host, but not necessarily to the GPU. hipFFTW decides on the
type of memory being allocated following a ranked-choice strategy. It attempts to allocate:

pinned host memory (first);

pageable host memory (if the latter failed or if the request exceeds a

[user-defined threshold](#hipfftw-env-byte-size-host-alloc)).

Important

Every buffer allocated via `fftw_malloc`

, `fftwf_malloc`

, `fftw_alloc_real`

, `fftwf_alloc_real`

,
`fftw_alloc_complex`

, or `fftwf_alloc_complex`

**must** be freed using `fftw_free`

or `fftwf_free`

.

## Plan creation[#](#plan-creation)

hipFFTW supports the creation of [basic](#hipfftw-basic-plan-creation), [advanced](#hipfftw-advanced-plan-creation),
and [general](#hipfftw-general-plan-creation) plans, using interleaved formats for complex floating-point data.
Plans capture:

the type of transform, namely, complex or real, forward or backward (inverse) discrete Fourier transform;

the length(s) and batch size(s) of the transform;

layout information for input and output data, for example, stride(s), distance(s);

pointers to buffers that it should consider as input and output data buffers when computing a transform via a

[generic execution function](#hipfftw-execute-with-creation-io);the flag value(s) to use at creation.


A plan of interest can be created using more than one plan creation function. For instance, any plan created
by `fftw_plan_dft`

(or `fftwf_plan_dft`

) could be created by `fftw_plan_many_dft`

(or `fftwf_plan_many_dft`

) without any difference.

For all plan creation functions, the requested plan is said to be configured for in-place operations if identical input and output buffers are used when the plan is created. The plan is configured for out-of-place operations otherwise.

Note

hipFFTW does not support split complex formats, real-to-real transforms, nor distributed transforms;

hipFFTW does not support transforms of more than 3 dimensions, that is,

`rank > 3`

is not supported;hipFFTW does not support transforms of more than 1 batch dimension, that is,

`batch_rank > 1`

is not supported.

### Basic plans[#](#basic-plans)

Basic plans are implicitly configured for unbatched transforms with compact, default data layouts. For \(d\)-dimensional (\(d > 0\)) transforms of lengths \(n_0 \times n_1 \times \ldots \times n_{d-1}\) (\(n_{i} > 0\, \forall i \in \lbrace 0, 1, \ldots, d-1\rbrace\)), default data layouts use strides \(s_i\) along dimension \(i\) where

\(s_{d-1} = 1\);

- if \(d > 1\),
\(s_{d-2} = 2 \lfloor n_{d-1} / 2 + 1 \rfloor\) on input (resp. output) and \(s_{d-2} = \lfloor n_{d-1} / 2 + 1 \rfloor\) on output (resp. input) for forward (resp. backward) real in-place transforms;

\(s_{d-2} = n_{d-1}\) on input (resp. output) and \(s_{d-2} = \lfloor n_{d-1} / 2 + 1 \rfloor\) on output (resp. input) for forward (resp. backward) real out-of-place transforms;

\(n_{d-1}\) otherwise.



if \(d > 2\), \(s_{i} = n_{i+1}s_{i+1}\) for \(0 \leq i < d-2\).


The following functions can be used for creating basic hipFFTW plans.

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_1d(int n,[fftw_complex](#_CPPv412fftw_complex)*in,[fftw_complex](#_CPPv412fftw_complex)*out, int sign, unsigned flags)[#](#_CPPv416fftw_plan_dft_1diP12fftw_complexP12fftw_complexij) Creates a basic plan for a one-dimensional, double-precision, complex discrete Fourier transform of length

`n`

.- Parameters:
**n**–**[in]**strictly positive length of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**sign**–**[in]**exponent sign defining the desired complex transform (`FFTW_FORWARD`

or`FFTW_BACKWARD`

);**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_1d(int n,[fftwf_complex](#_CPPv413fftwf_complex)*in,[fftwf_complex](#_CPPv413fftwf_complex)*out, int sign, unsigned flags)[#](#_CPPv417fftwf_plan_dft_1diP13fftwf_complexP13fftwf_complexij) Single-precision equivalent of

[fftw_plan_dft_1d](#hipfftw_8h_1a9dba60517daf9f1a8187d3d7f386a78d).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_2d(int n0, int n1,[fftw_complex](#_CPPv412fftw_complex)*in,[fftw_complex](#_CPPv412fftw_complex)*out, int sign, unsigned flags)[#](#_CPPv416fftw_plan_dft_2diiP12fftw_complexP12fftw_complexij) Creates a basic plan for a two-dimensional, double-precision, complex discrete Fourier transform of lengths

`n0 x n1`

.- Parameters:
**n0, n1**–**[in]**strictly positive lengths of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**sign**–**[in]**exponent sign defining the desired complex transform (`FFTW_FORWARD`

or`FFTW_BACKWARD`

);**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_2d(int n0, int n1,[fftwf_complex](#_CPPv413fftwf_complex)*in,[fftwf_complex](#_CPPv413fftwf_complex)*out, int sign, unsigned flags)[#](#_CPPv417fftwf_plan_dft_2diiP13fftwf_complexP13fftwf_complexij) Single-precision equivalent of

[fftw_plan_dft_2d](#hipfftw_8h_1a472c49a39060f660733057cb1f85263e).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_3d(int n0, int n1, int n2,[fftw_complex](#_CPPv412fftw_complex)*in,[fftw_complex](#_CPPv412fftw_complex)*out, int sign, unsigned flags)[#](#_CPPv416fftw_plan_dft_3diiiP12fftw_complexP12fftw_complexij) Creates a basic plan for a three-dimensional, double-precision, complex discrete Fourier transform of lengths

`n0 x n1 x n2`

.- Parameters:
**n0, n1, n2**–**[in]**strictly positive lengths of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**sign**–**[in]**exponent sign defining the desired complex transform (`FFTW_FORWARD`

or`FFTW_BACKWARD`

);**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_3d(int n0, int n1, int n2,[fftwf_complex](#_CPPv413fftwf_complex)*in,[fftwf_complex](#_CPPv413fftwf_complex)*out, int sign, unsigned flags)[#](#_CPPv417fftwf_plan_dft_3diiiP13fftwf_complexP13fftwf_complexij) Single-precision equivalent of

[fftw_plan_dft_3d](#hipfftw_8h_1a40e7ee551602affd0ce7ba89c4e8f570).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft(int rank, const int *n,[fftw_complex](#_CPPv412fftw_complex)*in,[fftw_complex](#_CPPv412fftw_complex)*out, int sign, unsigned flags)[#](#_CPPv413fftw_plan_dftiPKiP12fftw_complexP12fftw_complexij) Creates a basic plan for a multidimensional, double-precision, complex discrete Fourier transform of lengths

`n[0] x n[1] x ... x n[rank-1]`

.- Parameters:
**rank**–**[in]**strictly positive rank of the transform;**n**–**[in]**array of strictly positive lengths of the transform (must be of size`rank`

);**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**sign**–**[in]**exponent sign defining the desired complex transform (`FFTW_FORWARD`

or`FFTW_BACKWARD`

);**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft(int rank, const int *n,[fftwf_complex](#_CPPv413fftwf_complex)*in,[fftwf_complex](#_CPPv413fftwf_complex)*out, int sign, unsigned flags)[#](#_CPPv414fftwf_plan_dftiPKiP13fftwf_complexP13fftwf_complexij) Single-precision equivalent of

[fftw_plan_dft](#hipfftw_8h_1ab09c1f487162eac5de0f5b1a313bd90b).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_r2c_1d(int n, double *in,[fftw_complex](#_CPPv412fftw_complex)*out, unsigned flags)[#](#_CPPv420fftw_plan_dft_r2c_1diPdP12fftw_complexj) Creates a basic plan for a one-dimensional, double-precision, real forward discrete Fourier transform of length

`n`

.- Parameters:
**n**–**[in]**strictly positive length of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_r2c_1d(int n, float *in,[fftwf_complex](#_CPPv413fftwf_complex)*out, unsigned flags)[#](#_CPPv421fftwf_plan_dft_r2c_1diPfP13fftwf_complexj) Single-precision equivalent of

[fftw_plan_dft_r2c_1d](#hipfftw_8h_1a7ac1f6b6cc905cd71af39b2fa8949b60).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_r2c_2d(int n0, int n1, double *in,[fftw_complex](#_CPPv412fftw_complex)*out, unsigned flags)[#](#_CPPv420fftw_plan_dft_r2c_2diiPdP12fftw_complexj) Creates a basic plan for a two-dimensional, double-precision, real forward discrete Fourier transform of lengths

`n0 x n1`

.- Parameters:
**n0, n1**–**[in]**strictly positive lengths of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_r2c_2d(int n0, int n1, float *in,[fftwf_complex](#_CPPv413fftwf_complex)*out, unsigned flags)[#](#_CPPv421fftwf_plan_dft_r2c_2diiPfP13fftwf_complexj) Single-precision equivalent of

[fftw_plan_dft_r2c_2d](#hipfftw_8h_1a99c3059c8041350ce9ce75f8b0f55b19).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_r2c_3d(int n0, int n1, int n2, double *in,[fftw_complex](#_CPPv412fftw_complex)*out, unsigned flags)[#](#_CPPv420fftw_plan_dft_r2c_3diiiPdP12fftw_complexj) Creates a basic plan for a three-dimensional, double-precision, real forward discrete Fourier transform of lengths

`n0 x n1 x n2`

.- Parameters:
**n0, n1, n2**–**[in]**strictly positive lengths of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_r2c_3d(int n0, int n1, int n2, float *in,[fftwf_complex](#_CPPv413fftwf_complex)*out, unsigned flags)[#](#_CPPv421fftwf_plan_dft_r2c_3diiiPfP13fftwf_complexj) Single-precision equivalent of

[fftw_plan_dft_r2c_3d](#hipfftw_8h_1a4e2de67bb16d4c45a283dfc8a18fa6cb).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_r2c(int rank, const int *n, double *in,[fftw_complex](#_CPPv412fftw_complex)*out, unsigned flags)[#](#_CPPv417fftw_plan_dft_r2ciPKiPdP12fftw_complexj) Creates a basic plan for a multidimensional, double-precision, real forward discrete Fourier transform of lengths

`n[0] x n[1] x ... x n[rank-1]`

.- Parameters:
**rank**–**[in]**strictly positive rank of the transform;**n**–**[in]**array of strictly positive lengths of the transform (must be of size`rank`

);**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_r2c(int rank, const int *n, float *in,[fftwf_complex](#_CPPv413fftwf_complex)*out, unsigned flags)[#](#_CPPv418fftwf_plan_dft_r2ciPKiPfP13fftwf_complexj) Single-precision equivalent of

[fftw_plan_dft_r2c](#hipfftw_8h_1a34510ae2ad763598078a21ad7f3589c2).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_c2r_1d(int n,[fftw_complex](#_CPPv412fftw_complex)*in, double *out, unsigned flags)[#](#_CPPv420fftw_plan_dft_c2r_1diP12fftw_complexPdj) Creates a basic plan for a one-dimensional, double-precision, real backward (inverse) discrete Fourier transform of length

`n`

.- Parameters:
**n**–**[in]**strictly positive length of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_c2r_1d(int n,[fftwf_complex](#_CPPv413fftwf_complex)*in, float *out, unsigned flags)[#](#_CPPv421fftwf_plan_dft_c2r_1diP13fftwf_complexPfj) Single-precision equivalent of

[fftw_plan_dft_c2r_1d](#hipfftw_8h_1ae4352dc9c1966189add268a51260085f).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_c2r_2d(int n0, int n1,[fftw_complex](#_CPPv412fftw_complex)*in, double *out, unsigned flags)[#](#_CPPv420fftw_plan_dft_c2r_2diiP12fftw_complexPdj) Creates a basic plan for a two-dimensional, double-precision, real backward (inverse) discrete Fourier transform of lengths

`n0 x n1`

.- Parameters:
**n0, n1**–**[in]**strictly positive lengths of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_c2r_2d(int n0, int n1,[fftwf_complex](#_CPPv413fftwf_complex)*in, float *out, unsigned flags)[#](#_CPPv421fftwf_plan_dft_c2r_2diiP13fftwf_complexPfj) Single-precision equivalent of

[fftw_plan_dft_c2r_2d](#hipfftw_8h_1a0d96128c2773fe100a931b102836ece7).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_c2r_3d(int n0, int n1, int n2,[fftw_complex](#_CPPv412fftw_complex)*in, double *out, unsigned flags)[#](#_CPPv420fftw_plan_dft_c2r_3diiiP12fftw_complexPdj) Creates a basic plan for a three-dimensional, double-precision, real backward (inverse) discrete Fourier transform of lengths

`n0 x n1 x n2`

.- Parameters:
**n0, n1, n2**–**[in]**strictly positive lengths of the transform;**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_c2r_3d(int n0, int n1, int n2,[fftwf_complex](#_CPPv413fftwf_complex)*in, float *out, unsigned flags)[#](#_CPPv421fftwf_plan_dft_c2r_3diiiP13fftwf_complexPfj) Single-precision equivalent of

[fftw_plan_dft_c2r_3d](#hipfftw_8h_1a5889bde22de66d19fc29bf9d0b91dff0).

-
[fftw_plan](#_CPPv49fftw_plan)fftw_plan_dft_c2r(int rank, const int *n,[fftw_complex](#_CPPv412fftw_complex)*in, double *out, unsigned flags)[#](#_CPPv417fftw_plan_dft_c2riPKiP12fftw_complexPdj) Creates a basic plan for a multidimensional, double-precision, real backward (inverse) discrete Fourier transform of lengths

`n[0] x n[1] x ... x n[rank-1]`

.- Parameters:
**rank**–**[in]**strictly positive rank of the transform;**n**–**[in]**array of strictly positive lengths of the transform (must be of size`rank`

);**in**–**[in]**pointer to the input buffer for the transform;**out**–**[in]**pointer to the output buffer for the transform;**flags**–**[in]**bitwise OR (`|`

) combination of zero or more constant flag values.

- Returns:
a valid double-precision hipFFTW plan ready for execution upon success (

`nullptr`

otherwise).


-
[fftwf_plan](#_CPPv410fftwf_plan)fftwf_plan_dft_c2r(int rank, const int *n,[fftwf_complex](#_CPPv413fftwf_complex)*in, float *out, unsigned flags)[#](#_CPPv418fftwf_plan_dft_c2riPKiP13fftwf_complexPfj) Single-precision equivalent of

[fftw_plan_dft_c2r](#hipfftw_8h_1a5da0a69d2bb6b641740c42faee06a709).

### Advanced plans[#](#advanced-plans)

### Arbitrary plans[#](#arbitrary-plans)

## Plan execution[#](#plan-execution)

After they are successfully created, hipFFTW plans can be executed, that is, used for computing the discrete Fourier transform that they capture.
The [generic execution functions](#hipfftw-execute-with-creation-io) implicitly reuse the input and output buffers that were set
at [plan creation](#hipfftw-plan-creation). If that is not possible or impractical, new input and output buffers can be communicated
instead by using the [new-arrays execution functions](#hipfftw-execute-with-new-io).

### Using buffers set at plan creation for computation[#](#using-buffers-set-at-plan-creation-for-computation)

-
void fftw_execute(const
[fftw_plan](#_CPPv49fftw_plan)plan)[#](#_CPPv412fftw_executeK9fftw_plan) Computes the discrete Fourier transform that a double-precision plan captures using the input and output data buffers that were communicated at plan’s creation.

- Parameters:
**plan**–**[in]**the double-precision plan capturing the transform to compute.


-
void fftwf_execute(const
[fftwf_plan](#_CPPv410fftwf_plan)plan)[#](#_CPPv413fftwf_executeK10fftwf_plan) Single-precision equivalent of

[fftw_execute](#hipfftw_8h_1a7e26a150d4454f82fb89d30c307238eb).

### Using new buffers for computation[#](#using-new-buffers-for-computation)

-
void fftw_execute_dft(const
[fftw_plan](#_CPPv49fftw_plan)plan,[fftw_complex](#_CPPv412fftw_complex)*in,[fftw_complex](#_CPPv412fftw_complex)*out)[#](#_CPPv416fftw_execute_dftK9fftw_planP12fftw_complexP12fftw_complex) Computes the discrete Fourier transform that a double-precision plan captures using new input and output data buffers. The plan must have been created for a complex transform.

- Parameters:
**plan**–**[in]**the double-precision plan capturing the complex transform to compute;**in**–**[in]**pointer to a new input buffer for the transform;**out**–**[out]**pointer to a new output buffer for the transform.



-
void fftwf_execute_dft(const
[fftwf_plan](#_CPPv410fftwf_plan)plan,[fftwf_complex](#_CPPv413fftwf_complex)*in,[fftwf_complex](#_CPPv413fftwf_complex)*out)[#](#_CPPv417fftwf_execute_dftK10fftwf_planP13fftwf_complexP13fftwf_complex) Single-precision equivalent of

[fftw_execute_dft](#hipfftw_8h_1a2bd8f8e711a499573cfd0cd6b1ef3509).

-
void fftw_execute_dft_r2c(const
[fftw_plan](#_CPPv49fftw_plan)plan, double *in,[fftw_complex](#_CPPv412fftw_complex)*out)[#](#_CPPv420fftw_execute_dft_r2cK9fftw_planPdP12fftw_complex) Computes the discrete Fourier transform that a double-precision plan captures using new input and output data buffers. The plan must have been created for a real forward transform.

- Parameters:
**plan**–**[in]**the double-precision plan capturing the real forward transform to compute;**in**–**[in]**pointer to a new input buffer for the transform;**out**–**[out]**pointer to a new output buffer for the transform.



-
void fftwf_execute_dft_r2c(const
[fftwf_plan](#_CPPv410fftwf_plan)plan, float *in,[fftwf_complex](#_CPPv413fftwf_complex)*out)[#](#_CPPv421fftwf_execute_dft_r2cK10fftwf_planPfP13fftwf_complex) Single-precision equivalent of

[fftw_execute_dft_r2c](#hipfftw_8h_1aab988b70e68240116a2a2095b5645e5f).

-
void fftw_execute_dft_c2r(const
[fftw_plan](#_CPPv49fftw_plan)plan,[fftw_complex](#_CPPv412fftw_complex)*in, double *out)[#](#_CPPv420fftw_execute_dft_c2rK9fftw_planP12fftw_complexPd) Computes the discrete Fourier transform that a double-precision plan captures using new input and output data buffers. The plan must have been created for a real backward (inverse) transform.

- Parameters:
**plan**–**[in]**the double-precision plan capturing the real backward (inverse) transform to compute;**in**–**[in]**pointer to a new input buffer for the transform;**out**–**[out]**pointer to a new output buffer for the transform.



-
void fftwf_execute_dft_c2r(const
[fftwf_plan](#_CPPv410fftwf_plan)plan,[fftwf_complex](#_CPPv413fftwf_complex)*in, float *out)[#](#_CPPv421fftwf_execute_dft_c2rK10fftwf_planP13fftwf_complexPf) Single-precision equivalent of

[fftw_execute_dft_c2r](#hipfftw_8h_1a2ef43d5c1f09aa4e8fa397866e01eb3f).

Note

When new input and output buffers are used for execution, they must honor the placement that was set at plan creation.
In other words, the result of `(void*)in == (void*)out`

must be unchanged between plan creation and plan execution.

Note

If the type of memory for the output buffer is directly accessible by the host, hipFFTW enforces synchronization before
returning from any of the above [execution functions](#hipfftw-execution) to guarantee that the results are readily
available to the host upon completion of the execution function.

## Plan destruction[#](#plan-destruction)

When no longer needed or going out of scope, hipFFTW plans must be destructed using either of the following functions matching the plan’s precision.

-
void fftw_destroy_plan(
[fftw_plan](#_CPPv49fftw_plan)plan)[#](#_CPPv417fftw_destroy_plan9fftw_plan) Deallocates a double-precision plan and frees all its resources.

- Parameters:
**plan**–**[in]**plan to be destroyed.


-
void fftwf_destroy_plan(
[fftwf_plan](#_CPPv410fftwf_plan)plan)[#](#_CPPv418fftwf_destroy_plan10fftwf_plan) Single-precision equivalent of

[fftw_destroy_plan](#hipfftw_8h_1ab97128dc45abeb1de51bcda327e2d52c).

## Other utility functions (existing yet non-functional)[#](#other-utility-functions-existing-yet-non-functional)

The following functions exist in hipFFTW but are **not** functional in any way. They effectively ignore all
arguments and systematically return `0.0`

when a `double`

value needs to be returned.

`fftw_print_plan`

and`fftwf_print_plan`

;`fftw_set_timelimit`

and`fftwf_set_timelimit`

;`fftw_cost`

and`fftwf_cost`

;`fftw_flops`

and`fftwf_flops`

;`fftw_cleanup`

and`fftwf_cleanup`

.

## Environment variables specific to hipFFTW[#](#environment-variables-specific-to-hipfftw)

### Enforcing size limits on types of memory for user-managed buffers[#](#enforcing-size-limits-on-types-of-memory-for-user-managed-buffers)

By setting any of the environment variables

`HIPFFTW_BYTE_SIZE_LIMIT_PINNED_HOST_ALLOC`

;`HIPFFTW_BYTE_SIZE_LIMIT_PAGEABLE_HOST_ALLOC`

;

to a non-negative integer value, users can instruct hipFFTW to observe the value set for the maximal
byte size that can be considered for the corresponding kind of host-accessible memory for any individual
allocation requested via the [buffer allocation functions](#hipfftw-buffer-management). Setting
any of the above variables to `0`

effectively prevents the corresponding kind of memory to be
considered in user-requested buffer allocations altogether.

### Making hipFFTW verbose[#](#making-hipfftw-verbose)

Debugging failures or errors suspected to be triggered by hipFFTW can be challenging, particularly
if the root cause lies in any of the [execution functions](#hipfftw-execution), given
that these functions’ signatures make such errors silent by design. Setting the environment variable
`HIPFFTW_LOG_EXCEPTIONS`

to a strictly positive integer value effectively instructs hipFFTW to become
verbose about internal exceptions it might encounter by reporting them to the standard error stream.

Note

The hipFFTW interface is C-compatible, even when `HIPFFTW_LOG_EXCEPTIONS`

is set as
described above.
