---
title: "Custom type traits in rocPRIM &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/rocPRIM-type-traits.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:28:28.556830+00:00
content_hash: "f25de2f1c5548eaa"
---

# Custom type traits in rocPRIM[#](#custom-type-traits-in-rocprim)

This interface is designed to enable users to provide additional type trait information to rocPRIM, facilitating better compatibility with custom types.

Accurately describing custom types is important for performance optimization and computational correctness.

Custom types that implement arithmetic operators can behave like built-in arithmetic types but might still be interpreted by rocPRIM algorithms as generic `struct`

or `class`

types.

The rocPRIM type traits interface lets users add custom trait information for their types, improving compatibility between these types and rocPRIM algorithms.

This interface is similar to operator overloading.

Traits should be implemented as required by specific algorithms. Some traits can’t be defined if they can be inferred from others.

## Interface[#](#interface)

-
template<class T>

struct define[#](#_CPPv4I0EN7rocprim6traits6defineE) **Overview**This template struct provides an interface for downstream libraries to implement type traits for their custom types. Users can utilize this template struct to define traits for these types. Users should only implement traits as required by specific algorithms, and some traits cannot be defined if they can be inferred from others. This API is not static because of ODR.

**Example**The example below demonstrates how to implement traits for a custom floating-point type.

The example below demonstrates how to implement traits for a custom integral type.// Your type definition struct custom_float_type {}; // Implement the traits template<> struct rocprim::traits::define<custom_float_type> { using is_arithmetic = rocprim::traits::is_arithmetic::values<true>; using number_format = rocprim::traits::number_format::values<traits::number_format::kind::floating_point_type>; using float_bit_mask = rocprim::traits::float_bit_mask::values<uint32_t, 10, 10, 10>; };

// Your type definition struct custom_int_type {}; // Implement the traits template<> struct rocprim::traits::define<custom_int_type> { using is_arithmetic = rocprim::traits::is_arithmetic::values<true>; using number_format = rocprim::traits::number_format::values<traits::number_format::kind::integral_type>; using integral_sign = rocprim::traits::integral_sign::values<traits::integral_sign::kind::signed_type>; };


- Template Parameters:
**T**– The type for which you want to define traits.


-
template<class T>

struct get[#](#_CPPv4I0EN7rocprim6traits3getE) **Overview**This template struct is designed to allow rocPRIM algorithms to retrieve trait information from C++ build-in arithmetic types, rocPRIM types, and custom types. This API is not static because of ODR.

All member functions are

`compiled only when invoked`

.Different algorithms require different traits.


**Example**The following code demonstrates how to retrieve the traits of type

`T`

.// Get the trait in a template parameter template<class T, std::enable_if<rocprim::traits::get<T>().is_integral()>::type* = nullptr> void get_traits_in_template_parameter(){} // Get the trait in a function body template<class T> void get_traits_in_function_body(){ constexpr auto input_traits = rocprim::traits::get<InputType>(); // Then you can use the member functinos constexpr bool is_arithmetic = input_traits.is_arithmetic(); }


- Template Parameters:
**T**– The type from which you want to retrieve the traits.

Public Functions

-
inline constexpr bool is_arithmetic() const
[#](#_CPPv4NK7rocprim6traits3get13is_arithmeticEv) Get the value of trait


.[is_arithmetic](#structrocprim_1_1traits_1_1is__arithmetic)- Returns:
`true`

if`std::is_arithmetic_v<T>`

is`true`

, or if type`T`

is a rocPRIM arithmetic type, or if the

trait has been defined as[is_arithmetic](#structrocprim_1_1traits_1_1is__arithmetic)`true`

; otherwise, returns`false`

.


-
inline constexpr bool is_fundamental() const
[#](#_CPPv4NK7rocprim6traits3get14is_fundamentalEv) Get trait

`is_fundamental`

.- Returns:
`true`

if`T`

is a fundamental type (that is, rocPRIM arithmetic type, void, or nullptr_t); otherwise, returns`false`

.


-
inline constexpr bool is_build_in() const
[#](#_CPPv4NK7rocprim6traits3get11is_build_inEv) Check if the type is a

`build_in`

type, this function is different from`is_fundamental`

, because, by implementing traits, downstream code can “hack” into rocprim to let a type be`arithmetic`

, and by following the rules of`std::is_fundamental`

,`rocprim::is_fundamental`

returns a union set of`std::is_fundamental`

and`rocprim::is_arithmetic`

. So, to check wether a type is a build-in type, please use this function.- Returns:
`true`

if`T`

is a`build_in`

type (that is, char, unsigned char, short, unsigned short, int unsigned int, long long, unsigned long long, rocprim::int128_t, rocprim::uint128_t, rocprim::half, float, double);


-
inline constexpr bool is_compound() const
[#](#_CPPv4NK7rocprim6traits3get11is_compoundEv) If

`T`

is fundamental type, then returns`false`

.- Returns:
`false`

if`T`

is a fundamental type (that is, rocPRIM arithmetic type, void, or nullptr_t); otherwise, returns`true`

.


-
inline constexpr bool is_floating_point() const
[#](#_CPPv4NK7rocprim6traits3get17is_floating_pointEv) To check if

`T`

is floating-point type.

-
inline constexpr bool is_integral() const
[#](#_CPPv4NK7rocprim6traits3get11is_integralEv) To check if

`T`

is integral type.

-
inline constexpr bool is_signed() const
[#](#_CPPv4NK7rocprim6traits3get9is_signedEv) To check if

`T`

is signed integral type.

-
inline constexpr bool is_unsigned() const
[#](#_CPPv4NK7rocprim6traits3get11is_unsignedEv) To check if

`T`

is unsigned integral type.

-
inline constexpr bool is_scalar() const
[#](#_CPPv4NK7rocprim6traits3get9is_scalarEv) Get trait


.[is_scalar](#structrocprim_1_1traits_1_1is__scalar)- Returns:
`true`

if`std::is_scalar_v<T>`

is`true`

, or if type`T`

is a rocPRIM arithmetic type, or if the

trait has been defined as[is_scalar](#structrocprim_1_1traits_1_1is__scalar)`true`

; otherwise, returns`false`

.


-
inline constexpr auto float_bit_mask() const
[#](#_CPPv4NK7rocprim6traits3get14float_bit_maskEv) Get trait


.[float_bit_mask](#structrocprim_1_1traits_1_1float__bit__mask)Warning

You cannot call this function when


returns[is_floating_point()](#structrocprim_1_1traits_1_1get_1a308415b9a3f98de5bb8efa304c815db2)`false`

; doing so will result in a compile-time error.- Returns:
A constexpr instance of the specialization of


as provided in the traits definition of type T. If the[rocprim::traits::float_bit_mask::values](#structrocprim_1_1traits_1_1float__bit__mask_1_1values)

is not defined, it returns the rocprim::detail::float_bit_mask values, provided a specialization of[float_bit_mask](#structrocprim_1_1traits_1_1float__bit__mask)trait`rocprim::detail::float_bit_mask<T>`

exists.


-
template<bool Descending = false>

inline constexpr auto radix_key_codec() const[#](#_CPPv4I_bENK7rocprim6traits3get15radix_key_codecEDav) Get trait


.[radix_key_codec](#structrocprim_1_1traits_1_1radix__key__codec)- Returns:
A constexpr instance of the specialization of


as provided in the traits definition of type T.[rocprim::traits::radix_key_codec::codec](#classrocprim_1_1traits_1_1radix__key__codec_1_1codec)



## Available traits[#](#available-traits)

-
struct is_arithmetic
[#](#_CPPv4N7rocprim6traits13is_arithmeticE) **Definability****Undefinable**: For types with`predefined traits`

.**Optional**: For other types.

**How to define**using is_arithmetic = rocprim::traits::is_arithmetic::values<true>;


**How to use**rocprim::traits::get<InputType>().is_arithmetic();


-
template<bool Val>

struct values[#](#_CPPv4I_bEN7rocprim6traits13is_arithmetic6valuesE) Value of this trait.



-
struct is_scalar
[#](#_CPPv4N7rocprim6traits9is_scalarE) Arithmetic types, pointers, member pointers, and null pointers are considered scalar types.

**Definability****Undefinable**: For types with`predefined traits`

.**Optional**: For other types. If both

and[is_arithmetic](#structrocprim_1_1traits_1_1is__arithmetic)

are defined, their values must be consistent; otherwise, a compile-time error will occur.[is_scalar](#structrocprim_1_1traits_1_1is__scalar)

**How to define**using is_scalar = rocprim::traits::is_scalar::values<true>;


**How to use**rocprim::traits::get<InputType>().is_scalar();


-
template<bool Val>

struct values[#](#_CPPv4I_bEN7rocprim6traits9is_scalar6valuesE) Value of this trait.



-
struct number_format
[#](#_CPPv4N7rocprim6traits13number_formatE) **Definability****Undefinable**: For types with`predefined traits`

and non-arithmetic types.**Required**: If you define

as[is_arithmetic](#structrocprim_1_1traits_1_1is__arithmetic)`true`

, you must also define this trait; otherwise, a compile-time error will occur.

**How to define**using number_format = rocprim::traits::number_format::values<number_format::kind::integral_type>;


**How to use**rocprim::traits::get<InputType>().is_integral(); rocprim::traits::get<InputType>().is_floating_point();


Public Types


-
struct integral_sign
[#](#_CPPv4N7rocprim6traits13integral_signE) **Definability****Undefinable**: For types with`predefined traits`

, non-arithmetic types and floating-point types.**Required**: If you define

as[number_format](#structrocprim_1_1traits_1_1number__format)`number_format::kind::floating_point_type`

, you must also define this trait; otherwise, a compile-time error will occur.

**How to define**using integral_sign = rocprim::traits::integral_sign::values<traits::integral_sign::kind::signed_type>;


**How to use**rocprim::traits::get<InputType>().is_signed(); rocprim::traits::get<InputType>().is_unsigned();


Public Types


-
struct float_bit_mask
[#](#_CPPv4N7rocprim6traits14float_bit_maskE) **Definability****Undefinable**: For types with`predefined traits`

, non-arithmetic types and integral types.**Required**: If you define

as[number_format](#structrocprim_1_1traits_1_1number__format)`number_format::kind::unknown_type`

, you must also define this trait; otherwise, a compile-time error will occur.

**How to define**using float_bit_mask = rocprim::traits::float_bit_mask::values<int,1,1,1>;


**How to use**rocprim::traits::get<InputType>().float_bit_mask();



-
struct radix_key_codec
[#](#_CPPv4N7rocprim6traits15radix_key_codecE) **Definability****Undefinable**: For all types.

**Overview This trait is automatically generated.****How to use**constexpr auto codec = rocprim::traits::get<InputType>().radix_key_codec(); using codec_t = decltype(codec);


Public Types

Public Static Functions

-
template<class Key, bool Descending>

static inline constexpr auto get()[#](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec3getEDav) The getter of this trait.

- Template Parameters:
**Key**– type of the radix key- Returns:
The specialization of


.[rocprim::traits::radix_key_codec::codec](#classrocprim_1_1traits_1_1radix__key__codec_1_1codec)


-
template<class Key, bool Descending = false, bool is_fundamental =
[radix_key_fundamental](#_CPPv4I0EN7rocprim6traits15radix_key_codec21radix_key_fundamentalE)<[Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)>::value>

class codec : protected codec_base<[Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)>[#](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE) codec_base wrapper for fundamental radix key types

Public Static Functions

-
template<class Decomposer = ::rocprim::identity_decomposer>

__host__ __device__ static inline[bit_key_type](#_CPPv4N7rocprim6traits15radix_key_codec5codec12bit_key_typeE)encode([Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec6encodeE12bit_key_type3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec6encodeE12bit_key_type3Key10Decomposer) Encodes a key of type

`Key`

into`bit_key_type`

.- Template Parameters:
**Decomposer**– Being`Key`

a fundamental type,`Decomposer`

should be`identity_decomposer`

. This is also the type by default.- Parameters:
**key**–**[in]**Key to encode.**decomposer**–**[in]**[optional] Decomposer functor.

- Returns:
A

`bit_key_type`

encoded key.


-
template<class Decomposer = ::rocprim::identity_decomposer>

__host__ __device__ static inline void encode_inplace([Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)&key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec14encode_inplaceEvR3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec14encode_inplaceEvR3Key10Decomposer) Encodes in-place a key of type

`Key`

.- Template Parameters:
**Decomposer**– Being`Key`

a fundamental type,`Decomposer`

should be`identity_decomposer`

. This is also the type by default.- Parameters:
**key**–**[inout]**Key to encode.**decomposer**–**[in]**[optional] Decomposer functor.



-
template<class Decomposer = ::rocprim::identity_decomposer>

__host__ __device__ static inline[Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)decode([bit_key_type](#_CPPv4N7rocprim6traits15radix_key_codec5codec12bit_key_typeE)bit_key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec6decodeE3Key12bit_key_type10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec6decodeE3Key12bit_key_type10Decomposer) Decodes an encoded key of type

`bit_key_type`

back into`Key`

.- Template Parameters:
**Decomposer**– Being`Key`

a fundamental type,`Decomposer`

should be`identity_decomposer`

. This is also the type by default.- Parameters:
**bit_key**–**[in]**Key to decode.**decomposer**–**[in]**[optional] Decomposer functor.

- Returns:
A

`Key`

decoded key.


-
template<class Decomposer = ::rocprim::identity_decomposer>

__host__ __device__ static inline void decode_inplace([Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)&key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec14decode_inplaceEvR3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec14decode_inplaceEvR3Key10Decomposer) Decodes in-place an encoded key of type

`Key`

.- Template Parameters:
**Decomposer**– Being`Key`

a fundamental type,`Decomposer`

should be`identity_decomposer`

. This is also the type by default.- Parameters:
**key**–**[inout]**Key to decode.**decomposer**–**[in]**[optional] Decomposer functor.



-
__host__ __device__ static inline unsigned int extract_digit(
[bit_key_type](#_CPPv4N7rocprim6traits15radix_key_codec5codec12bit_key_typeE)bit_key, unsigned int start, unsigned int radix_bits)[#](#_CPPv4N7rocprim6traits15radix_key_codec5codec13extract_digitE12bit_key_typejj) Extracts the specified bits from a given encoded key.

- Parameters:
**bit_key**–**[in]**Encoded key.**start**–**[in]**Start bit of the sequence of bits to extract.**radix_bits**–**[in]**How many bits to extract.

- Returns:
Requested bits from the key.



-
template<class Decomposer = ::rocprim::identity_decomposer>

__host__ __device__ static inline unsigned int extract_digit([Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)key, unsigned int start, unsigned int radix_bits,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec13extract_digitEj3Keyjj10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec13extract_digitEj3Keyjj10Decomposer) Extracts the specified bits from a given in-place encoded key.

- Template Parameters:
**Decomposer**– Being`Key`

a fundamental type,`Decomposer`

should be`identity_decomposer`

. This is also the type by default.- Parameters:
**key**–**[in]**Key.**start**–**[in]**Start bit of the sequence of bits to extract.**radix_bits**–**[in]**How many bits to extract.**decomposer**–**[in]**[optional] Decomposer functor.

- Returns:
Requested bits from the key.



-
template<class Decomposer = ::rocprim::identity_decomposer>

__host__ __device__ static inline[Key](#_CPPv4I0_b_bEN7rocprim6traits15radix_key_codec5codecE)get_out_of_bounds_key([Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec21get_out_of_bounds_keyE3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codec21get_out_of_bounds_keyE3Key10Decomposer) Gives the default value for out-of-bound keys of type

`Key`

.- Template Parameters:
**Decomposer**– Being`Key`

a fundamental type,`Decomposer`

should be`identity_decomposer`

. This is also the type by default.- Parameters:
**decomposer**–**[in]**[optional] Decomposer functor.- Returns:
Out-of-bound keys’ value.



-
template<class Decomposer = ::rocprim::identity_decomposer>

-
template<class Key, bool Descending>

class codec<[Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE),[Descending](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE), false>[#](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE) Specialization of

`class codec`

for non-fundamental radix key types.Public Types

Public Static Functions

-
template<class Decomposer>

__host__ __device__ static inline[bit_key_type](#_CPPv4N7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE12bit_key_typeE)encode([Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE)key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE6encodeE12bit_key_type3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE6encodeE12bit_key_type3Key10Decomposer) Encodes a key of type

`Key`

into`bit_key_type`

.- Template Parameters:
**Decomposer**– Decomposer functor type. Being`Key`

a custom key type, the decomposer type must be other than the`identity_decomposer`

.- Parameters:
**key**–**[in]**Key to encode.**decomposer**–**[in]**[optional]`Key`

is a custom key type, so a custom decomposer functor that returns a

of references to fundamental types from a[rocprim::tuple](types.html#classrocprim_1_1tuple)`Key`

key is needed.

- Returns:
A

`bit_key_type`

encoded key.


-
template<class Decomposer>

__host__ __device__ static inline void encode_inplace([Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE)&key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE14encode_inplaceEvR3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE14encode_inplaceEvR3Key10Decomposer) Encodes in-place a key of type

`Key`

.- Template Parameters:
**Decomposer**– Decomposer functor type. Being`Key`

a custom key type, the decomposer type must be other than the`identity_decomposer`

.- Parameters:
**key**–**[inout]**Key to encode.**decomposer**–**[in]**[optional]`Key`

is a custom key type, so a custom decomposer functor that returns a

of references to fundamental types from a[rocprim::tuple](types.html#classrocprim_1_1tuple)`Key`

key is needed.



-
template<class Decomposer>

__host__ __device__ static inline[Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE)decode([bit_key_type](#_CPPv4N7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE12bit_key_typeE)bit_key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE6decodeE3Key12bit_key_type10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE6decodeE3Key12bit_key_type10Decomposer) Decodes an encoded key of type

`bit_key_type`

back into`Key`

.- Template Parameters:
**Decomposer**– Decomposer functor type. Being`Key`

a custom key type, the decomposer type must be other than the`identity_decomposer`

.- Parameters:
**bit_key**–**[in]**Key to decode.**decomposer**–**[in]**[optional]`Key`

is a custom key type, so a custom decomposer functor that returns a

of references to fundamental types from a[rocprim::tuple](types.html#classrocprim_1_1tuple)`Key`

key is needed.

- Returns:
A

`Key`

decoded key.


-
template<class Decomposer>

__host__ __device__ static inline void decode_inplace([Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE)&key,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE14decode_inplaceEvR3Key10Decomposer)decomposer = {})[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE14decode_inplaceEvR3Key10Decomposer) Decodes in-place an encoded key of type

`Key`

.- Template Parameters:
**Decomposer**– Decomposer functor type. Being`Key`

a custom key type, the decomposer type must be other than the`identity_decomposer`

.- Parameters:
**key**–**[inout]**Key to decode.**decomposer**–**[in]**[optional] Decomposer functor.



-
__host__ __device__ static inline unsigned int extract_digit(
[bit_key_type](#_CPPv4N7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE12bit_key_typeE), unsigned int, unsigned int)[#](#_CPPv4N7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE13extract_digitE12bit_key_typejj) Extracts the specified bits from a given encoded key.

- Returns:
Requested bits from the key.



-
template<class Decomposer>

__host__ __device__ static inline unsigned int extract_digit([Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE)key, unsigned int start, unsigned int radix_bits,[Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE13extract_digitEj3Keyjj10Decomposer)decomposer)[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE13extract_digitEj3Keyjj10Decomposer) Extracts the specified bits from a given in-place encoded key.

- Template Parameters:
**Decomposer**– Decomposer functor type. Being`Key`

a custom key type, the decomposer type must be other than the`identity_decomposer`

.- Parameters:
**key**–**[in]**Key.**start**–**[in]**Start bit of the sequence of bits to extract.**radix_bits**–**[in]**How many bits to extract.**decomposer**–**[in]**`Key`

is a custom key type, so a custom decomposer functor that returns a

of references to fundamental types from a[rocprim::tuple](types.html#classrocprim_1_1tuple)`Key`

key is needed.

- Returns:
Requested bits from the key.



-
template<class Decomposer>

__host__ __device__ static inline[Key](#_CPPv4I0_bEN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEEE)get_out_of_bounds_key([Decomposer](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE21get_out_of_bounds_keyE3Key10Decomposer)decomposer)[#](#_CPPv4I0EN7rocprim6traits15radix_key_codec5codecI3Key10DescendingXL0EEE21get_out_of_bounds_keyE3Key10Decomposer) Gives the default value for out-of-bound keys of type

`Key`

.- Template Parameters:
**Decomposer**– Decomposer functor type. Being`Key`

a custom key type, the decomposer type must be other than the`identity_decomposer`

.- Parameters:
**decomposer**–**[in]**`Key`

is a custom key type, so a custom decomposer functor that returns a

of references to fundamental types from a[rocprim::tuple](types.html#classrocprim_1_1tuple)`Key`

key is needed.- Returns:
Out-of-bound keys’ value.



-
template<class Decomposer>


## Type traits wrappers[#](#type-traits-wrappers)

-
template<class T>

struct is_floating_point : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim17is_floating_pointE)>().is_floating_point()> An extension of

`std::is_floating_point`

that supports additional arithmetic types, including`rocprim::half`

,`rocprim::bfloat16`

, and any types with trait

implemented.[rocprim::traits::number_format::values](#structrocprim_1_1traits_1_1number__format_1_1values)<number_format::kind::floating_point_type>

-
template<class T>

struct is_integral : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim11is_integralE)>().is_integral()> An extension of

`std::is_integral`

that supports additional arithmetic types, including`rocprim::int128_t`

,`rocprim::uint128_t`

, and any types with trait

implemented.[rocprim::traits::number_format::values](#structrocprim_1_1traits_1_1number__format_1_1values)<number_format::kind::integral_type>

-
template<class T>

struct is_arithmetic : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim13is_arithmeticE)>().is_arithmetic()> An extension of

`std::is_arithmetic`

that supports additional arithmetic types, including any types with trait

implemented.[rocprim::traits::is_arithmetic::values](#structrocprim_1_1traits_1_1is__arithmetic_1_1values)<true>

-
template<class T>

struct is_fundamental : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim14is_fundamentalE)>().is_fundamental()> An extension of

`std::is_fundamental`

that supports additional arithmetic types, including any types with trait

implemented.[rocprim::traits::is_arithmetic::values](#structrocprim_1_1traits_1_1is__arithmetic_1_1values)<true>

-
template<class T>

struct is_unsigned : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim11is_unsignedE)>().is_unsigned()> An extension of

`std::is_unsigned`

that supports additional arithmetic types, including`rocprim::uint128_t`

, and any types with trait

implemented.[rocprim::traits::integral_sign::values](#structrocprim_1_1traits_1_1integral__sign_1_1values)<integral_sign::kind::unsigned_type>

-
template<class T>

struct is_signed : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim9is_signedE)>().is_signed()> An extension of

`std::is_signed`

that supports additional arithmetic types, including`rocprim::int128_t`

, and any types with trait

implemented.[rocprim::traits::integral_sign::values](#structrocprim_1_1traits_1_1integral__sign_1_1values)<integral_sign::kind::signed_type>

-
template<class T>

struct is_scalar : public std::integral_constant<bool, ::rocprim::traits::[get](#_CPPv4I0EN7rocprim6traits3getE)<[T](#_CPPv4I0EN7rocprim9is_scalarE)>().is_scalar()> An extension of

`std::is_scalar`

that supports additional arithmetic types, including any types with trait

implemented.[rocprim::traits::is_scalar::values](#structrocprim_1_1traits_1_1is__scalar_1_1values)<true>

## Types with predefined traits[#](#types-with-predefined-traits)

-
template<>

struct define<float>

-
template<>

struct define<double>

-
template<>

struct define<rocprim::bfloat16> Public Types

-
using is_arithmetic = traits::
[is_arithmetic](#_CPPv4N7rocprim6traits13is_arithmeticE)::[values](#_CPPv4I_bEN7rocprim6traits13is_arithmetic6valuesE)<true>

-
using number_format = traits::
[number_format](#_CPPv4N7rocprim6traits13number_formatE)::[values](#_CPPv4I_4kindEN7rocprim6traits13number_format6valuesE)<traits::[number_format](#_CPPv4N7rocprim6traits13number_formatE)::[kind](#_CPPv4N7rocprim6traits13number_format4kindE)::[floating_point_type](#_CPPv4N7rocprim6traits13number_format4kind19floating_point_typeE)>

-
using float_bit_mask = traits::
[float_bit_mask](#_CPPv4N7rocprim6traits14float_bit_maskE)::[values](#_CPPv4I0_7BitType_7BitType_7BitTypeEN7rocprim6traits14float_bit_mask6valuesE)<uint16_t, 0x8000, 0x7F80, 0x007F>

-
using is_arithmetic = traits::

-
template<>

struct define<rocprim::half> Public Types

-
using is_arithmetic = traits::
[is_arithmetic](#_CPPv4N7rocprim6traits13is_arithmeticE)::[values](#_CPPv4I_bEN7rocprim6traits13is_arithmetic6valuesE)<true>

-
using number_format = traits::
[number_format](#_CPPv4N7rocprim6traits13number_formatE)::[values](#_CPPv4I_4kindEN7rocprim6traits13number_format6valuesE)<traits::[number_format](#_CPPv4N7rocprim6traits13number_formatE)::[kind](#_CPPv4N7rocprim6traits13number_format4kindE)::[floating_point_type](#_CPPv4N7rocprim6traits13number_format4kind19floating_point_typeE)>

-
using float_bit_mask = traits::
[float_bit_mask](#_CPPv4N7rocprim6traits14float_bit_maskE)::[values](#_CPPv4I0_7BitType_7BitType_7BitTypeEN7rocprim6traits14float_bit_mask6valuesE)<uint16_t, 0x8000, 0x7C00, 0x03FF>

-
using is_arithmetic = traits::

-
template<>

struct define<rocprim::int128_t> : public std::conditional_t<std::is_arithmetic<rocprim::int128_t>::value, traits::[define](#_CPPv4I0EN7rocprim6traits6defineE)<void>, detail::define_int128_t>

-
template<>

struct define<rocprim::uint128_t> : public std::conditional_t<std::is_arithmetic<rocprim::uint128_t>::value, traits::[define](#_CPPv4I0EN7rocprim6traits6defineE)<void>, detail::define_uint128_t>
