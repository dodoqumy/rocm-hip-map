---
title: "rocPRIM utility types &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/types.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:17:34.930928+00:00
content_hash: "66afb9d9aee57448"
---

# rocPRIM utility types[#](#rocprim-utility-types)

## Double buffer[#](#double-buffer)

-
template<class T>

class double_buffer[#](#_CPPv4I0EN7rocprim13double_bufferE) This class provides an convenient way to do double buffering.

It tracks two versions of the buffer (“current” and “alternate”), which can be accessed with functions of the same name. You can also swap the buffers.

Public Functions

-
__host__ __device__ inline double_buffer()
[#](#_CPPv4N7rocprim13double_buffer13double_bufferEv) Constructs an empty double buffer object, initializing the buffer pointers to nullptr.


-
__host__ __device__ inline double_buffer(
[T](#_CPPv4I0EN7rocprim13double_bufferE)*current,[T](#_CPPv4I0EN7rocprim13double_bufferE)*alternate)[#](#_CPPv4N7rocprim13double_buffer13double_bufferEP1TP1T) Contructs a double buffer object using the supplied buffer pointers.

- Parameters:
**current**– Pointer to the buffer to designate as “current” (in use).**alternate**– Pointer to the buffer to designate as “alternate” (not in use)



-
__host__ __device__ inline void swap()
[#](#_CPPv4N7rocprim13double_buffer4swapEv) Swaps the current and alternate buffers.


-
__host__ __device__ inline double_buffer()

## Future value[#](#future-value)

-
template<typename T, typename Iter =
[T](#_CPPv4I00EN7rocprim12future_valueE)*>

class future_value[#](#_CPPv4I00EN7rocprim12future_valueE) Allows passing values that are not yet known at launch time as parameters to device algorithms.

Note

It is the users responsibility to ensure that value is available when the algorithm executes. This can be guaranteed with stream dependencies or explicit external synchronization.

int* intermediate_result = nullptr; hipMalloc(reinterpret_cast<void**>(&intermediate_result), sizeof(intermediate_result)); hipLaunchKernelGGL(compute_intermediate, blocks, threads, 0, stream, arg1, arg2, intermediate_result); const auto initial_value = rocprim::future_value<int>{intermediate_result}; rocprim::exclusive_scan(temporary_storage, storage_size, input, output, initial_value, size); hipFree(intermediate_result)

- Template Parameters:
**T**–**Iter**–


Public Types

Public Functions

-
__host__ __device__ inline explicit future_value(const
[Iter](#_CPPv4I00EN7rocprim12future_valueE)iter)[#](#_CPPv4N7rocprim12future_value12future_valueEK4Iter) Constructs a future value.

- Parameters:
**iter**– An iterator that will point to the value when it becomes available.



## Key-value pair[#](#key-value-pair)

-
template<class Key_, class Value_>

struct key_value_pair[#](#_CPPv4I00EN7rocprim14key_value_pairE) Convenience struct that allows you to store key-value pairs as a composite entity.

Public Functions

-
__host__ __device__ inline key_value_pair(const
[key_type](#_CPPv4N7rocprim14key_value_pair8key_typeE)key, const[value_type](#_CPPv4N7rocprim14key_value_pair10value_typeE)value)[#](#_CPPv4N7rocprim14key_value_pair14key_value_pairEK8key_typeK10value_type) Constructs a key-value pair using the supplied values.


-
__host__ __device__ inline bool operator!=(const
[key_value_pair](#_CPPv4I00EN7rocprim14key_value_pairE)&kvb) const[#](#_CPPv4NK7rocprim14key_value_pairneERK14key_value_pair) Returns true if the given key-value pair is not equal to this one. Otherwise returns false.


-
__host__ __device__ inline bool operator==(const
[key_value_pair](#_CPPv4I00EN7rocprim14key_value_pairE)&kvb) const[#](#_CPPv4NK7rocprim14key_value_paireqERK14key_value_pair) Returns true if the given key-value pair is equal to this one. Otherwise returns false.


-
__host__ __device__ inline key_value_pair(const

## Tuple[#](#tuple)

-
template<class ...Types>

class tuple[#](#_CPPv4IDpEN7rocprim5tupleE) Fixed-size collection of heterogeneous values.

See also

std::tuple

- Template Parameters:
**Types...**– the types (zero or more) of the elements that the tuple stores.- Pre:
For all types in

`Types`

… following operations should not throw exceptions: construction, copy and move assignment, and swapping.


Public Functions

-
__host__ __device__ inline constexpr tuple() noexcept
[#](#_CPPv4N7rocprim5tuple5tupleEv) Default constructor. Performs value-initialization of all elements.

This overload only participates in overload resolution if:

`std::is_default_constructible<Ti>::value`

is`true`

for all`i`

.


-
__host__ __device__ inline explicit tuple(const
[Types](#_CPPv4IDpEN7rocprim5tupleE)&... values)[#](#_CPPv4N7rocprim5tuple5tupleEDpRK5Types) Direct constructor. Initializes each element of the tuple with the corresponding input value.

This overload only participates in overload resolution if:

`std::is_copy_constructible<Ti>::value`

is`true`

for all`i`

.


-
template<class ...UTypes>

__host__ __device__ inline explicit tuple([UTypes](#_CPPv4IDpEN7rocprim5tuple5tupleEDpRR6UTypes)&&... values) noexcept[#](#_CPPv4IDpEN7rocprim5tuple5tupleEDpRR6UTypes) Converting constructor. Initializes each element of the tuple with the corresponding value in

`rocprim::detail::custom_forward<UTypes>(values)`

.This overload only participates in overload resolution if:

`sizeof...(Types) == sizeof...(UTypes)`

,`sizeof...(Types) >= 1`

, and`std::is_constructible<Ti, Ui&&>::value`

is`true`

for all`i`

.


-
template<class ...UTypes>

__host__ __device__ inline tuple(const[tuple](#_CPPv4IDpEN7rocprim5tuple5tupleERK5tupleIDp6UTypesE)<[UTypes](#_CPPv4IDpEN7rocprim5tuple5tupleERK5tupleIDp6UTypesE)...> &other) noexcept[#](#_CPPv4IDpEN7rocprim5tuple5tupleERK5tupleIDp6UTypesE) Converting copy constructor. Initializes each element of the tuple with the corresponding value from

`other`

.This overload only participates in overload resolution if:

`sizeof...(Types) == sizeof...(UTypes)`

,`sizeof...(Types) >= 1`

, and`std::is_constructible<Ti, Ui&&>::value`

is`true`

for all`i`

.


-
template<class ...UTypes>

__host__ __device__ inline tuple([tuple](#_CPPv4IDpEN7rocprim5tuple5tupleERR5tupleIDp6UTypesE)<[UTypes](#_CPPv4IDpEN7rocprim5tuple5tupleERR5tupleIDp6UTypesE)...> &&other) noexcept[#](#_CPPv4IDpEN7rocprim5tuple5tupleERR5tupleIDp6UTypesE) Converting move constructor. Initializes each element of the tuple with the corresponding value from

`other`

.This overload only participates in overload resolution if:

`sizeof...(Types) == sizeof...(UTypes)`

,`sizeof...(Types) >= 1`

, and`std::is_constructible<Ti, Ui&&>::value`

is`true`

for all`i`

.


-
__host__ __device__ inline ~tuple() noexcept = default
[#](#_CPPv4N7rocprim5tupleD0Ev) Implicitly-defined destructor.


-
[tuple](#_CPPv4IDpEN7rocprim5tupleE)&operator=(const[tuple](#_CPPv4IDpEN7rocprim5tupleE)&other) noexcept[#](#_CPPv4N7rocprim5tupleaSERK5tuple) Copy assignment operator.

- Parameters:
**other**– tuple to replace the contents of this tuple


-
[tuple](#_CPPv4IDpEN7rocprim5tupleE)&operator=([tuple](#_CPPv4IDpEN7rocprim5tupleE)&&other) noexcept[#](#_CPPv4N7rocprim5tupleaSERR5tuple) Move assignment operator.

- Parameters:
**other**– tuple to replace the contents of this tuple


-
template<class ...UTypes>
[tuple](#_CPPv4IDpEN7rocprim5tupleE)&operator=(const[tuple](#_CPPv4IDpEN7rocprim5tupleE)<[UTypes](#_CPPv4IDpEN7rocprim5tupleaSER5tupleRK5tupleIDp6UTypesE)...> &other) noexcept[#](#_CPPv4IDpEN7rocprim5tupleaSER5tupleRK5tupleIDp6UTypesE) For all

`i`

, assigns`rocprim::get<i>(other)`

to`rocprim::get<i>(*this)`

.- Parameters:
**other**– tuple to replace the contents of this tuple



-
template<class T>

class tuple_size[#](#_CPPv4I0EN7rocprim10tuple_sizeE) Provides access to the number of elements in a tuple as a compile-time constant expression.

`tuple_size<T>`

is undefined for types`T`

that are not tuples.

-
template<size_t I, class T>

struct tuple_element[#](#_CPPv4I_6size_t0EN7rocprim13tuple_elementE) Provides compile-time indexed access to the types of the elements of the tuple.

`tuple_element<I, T>`

is undefined for types`T`

that are not tuples.

## Uninitialized Array[#](#uninitialized-array)

-
template<typename T, unsigned int Count, size_t Alignment = alignof(
[T](#_CPPv4I0_j_6size_tEN7rocprim19uninitialized_arrayE))>

class uninitialized_array[#](#_CPPv4I0_j_6size_tEN7rocprim19uninitialized_arrayE) Provides indexed & typed access to uninitialized memory. To be used with

`ROCPRIM_SHARED_MEMORY`

Note

This class should be used to ensure that writes to the uninitialized memory block occur only via placement new.

Note

This class is non-copyable.

Note

The recommended pattern for usage is to first fill the array via calls to

`emplace`

, then read-only via

. Writing to the array reference returned by[get_unsafe_array()](#classrocprim_1_1uninitialized__array_1ad58ef9506f374500431085dd88ce282e)

should be avoided, if possible.[get_unsafe_array()](#classrocprim_1_1uninitialized__array_1ad58ef9506f374500431085dd88ce282e)Note

The value of

`Alignment`

MUST be a valid alignment for`T`

.- Template Parameters:
**T**– The item type which is provided via the accessors.**Count**– The number of T items to store.**Alignment**– The alignment of the backing storage, in bytes.


Public Functions

-
__host__ __device__ uninitialized_array(
[uninitialized_array](#_CPPv4N7rocprim19uninitialized_array19uninitialized_arrayERR19uninitialized_array)&&) = default[#](#_CPPv4N7rocprim19uninitialized_array19uninitialized_arrayERR19uninitialized_array) Default move constructor.


-
__host__ __device__
[uninitialized_array](#_CPPv4I0_j_6size_tEN7rocprim19uninitialized_arrayE)&operator=([uninitialized_array](#_CPPv4I0_j_6size_tEN7rocprim19uninitialized_arrayE)&&) = default[#](#_CPPv4N7rocprim19uninitialized_arrayaSERR19uninitialized_array) Default move assignment.


-
template<typename ...Args>

__host__ __device__ inline[T](#_CPPv4I0_j_6size_tEN7rocprim19uninitialized_arrayE)&emplace(const unsigned int index,[Args](#_CPPv4IDpEN7rocprim19uninitialized_array7emplaceER1TKjDpRR4Args)&&... args)[#](#_CPPv4IDpEN7rocprim19uninitialized_array7emplaceER1TKjDpRR4Args) Constructs a value in-place at the specified array index.

Note

This function calls the constructor of

`T`

with the specified arguments. If an instance of`T&`

is passed, the copy constructor is called, whereas in the case of a`T&&`

, the move constructor is called.Note

If an object is created at the same index more than once, the old object’s destructor is

**not**called. If`T`

is not trivially destructible, the behaviour is undefined.- Template Parameters:
**Args**– The types of the argument values.- Parameters:
**index**– The index in the array where the new object is constructed.**args**– The arguments to call the constructor with.

- Returns:
A reference to the newly constructed element.
