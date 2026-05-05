---
title: "rocPRIM iterators &#8212; rocPRIM 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocPRIM/en/latest/reference/iterators.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:17:57.057082+00:00
content_hash: "0abe12ad15e0006c"
---

# rocPRIM iterators[#](#rocprim-iterators)

## Constant[#](#constant)

-
template<class ValueType, class Difference = std::ptrdiff_t>

class constant_iterator[#](#_CPPv4I00EN7rocprim17constant_iteratorE) A random-access input (read-only) iterator which generates a sequence of homogeneous values.

**Overview**A

[constant_iterator](#classrocprim_1_1constant__iterator)represents a pointer into a range of same values.Using it for simulating a range filled with a sequence of same values saves memory capacity and bandwidth.



- Template Parameters:
**ValueType**– type of value that can be obtained by dereferencing the iterator.**Difference**– a type used for identify distance between iterators


Public Types

-
using value_type = typename std::remove_const<
[ValueType](#_CPPv4I00EN7rocprim17constant_iteratorE)>::type[#](#_CPPv4N7rocprim17constant_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference =
[value_type](#_CPPv4N7rocprim17constant_iterator10value_typeE)[#](#_CPPv4N7rocprim17constant_iterator9referenceE) A reference type of the type iterated over (

`value_type`

). It’s same as`value_type`

since[constant_iterator](#classrocprim_1_1constant__iterator)is a read-only iterator and does not have underlying buffer.

-
using pointer = const
[value_type](#_CPPv4N7rocprim17constant_iterator10value_typeE)*[#](#_CPPv4N7rocprim17constant_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

). It’s`const`

since[constant_iterator](#classrocprim_1_1constant__iterator)is a read-only iterator.

-
using difference_type =
[Difference](#_CPPv4I00EN7rocprim17constant_iteratorE)[#](#_CPPv4N7rocprim17constant_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim17constant_iterator17iterator_categoryE) The category of the iterator.


Public Functions

-
__host__ __device__ inline explicit constant_iterator(const
[value_type](#_CPPv4N7rocprim17constant_iterator10value_typeE)value, const size_t index = 0)[#](#_CPPv4N7rocprim17constant_iterator17constant_iteratorEK10value_typeK6size_t) Creates

[constant_iterator](#classrocprim_1_1constant__iterator)and sets its initial value to`value`

.- Parameters:
**value**– initial value**index**– optional index for[constant_iterator](#classrocprim_1_1constant__iterator)



-
__host__ __device__ inline
[value_type](#_CPPv4N7rocprim17constant_iterator10value_typeE)operator[]([difference_type](#_CPPv4N7rocprim17constant_iterator15difference_typeE)) const[#](#_CPPv4NK7rocprim17constant_iteratorixE15difference_type) Constant_iterator is not writable, so we don’t return reference, just something convertible to reference. That matches requirement of RandomAccessIterator concept



Note

For example, `constant_iterator(20)`

generates the infinite sequence:

```
20
20
20
...
```

## Counting[#](#counting)

-
template<class Incrementable, class Difference = std::ptrdiff_t>

class counting_iterator[#](#_CPPv4I00EN7rocprim17counting_iteratorE) A random-access input (read-only) iterator over a sequence of consecutive integer values.

**Overview**A

[counting_iterator](#classrocprim_1_1counting__iterator)represents a pointer into a range of sequentially increasing values.Using it for simulating a range filled with a sequence of consecutive values saves memory capacity and bandwidth.



- Template Parameters:
**Incrementable**– type of value that can be obtained by dereferencing the iterator.**Difference**– a type used for identify distance between iterators


Public Types

-
using value_type = typename std::remove_const<
[Incrementable](#_CPPv4I00EN7rocprim17counting_iteratorE)>::type[#](#_CPPv4N7rocprim17counting_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference =
[value_type](#_CPPv4N7rocprim17counting_iterator10value_typeE)[#](#_CPPv4N7rocprim17counting_iterator9referenceE) A reference type of the type iterated over (

`value_type`

). It’s same as`value_type`

since[constant_iterator](#classrocprim_1_1constant__iterator)is a read-only iterator and does not have underlying buffer.

-
using pointer = const
[value_type](#_CPPv4N7rocprim17counting_iterator10value_typeE)*[#](#_CPPv4N7rocprim17counting_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

). It’s`const`

since[counting_iterator](#classrocprim_1_1counting__iterator)is a read-only iterator.

-
using difference_type =
[Difference](#_CPPv4I00EN7rocprim17counting_iteratorE)[#](#_CPPv4N7rocprim17counting_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim17counting_iterator17iterator_categoryE) The category of the iterator.


Public Functions

-
__host__ __device__ inline ~counting_iterator() = default
[#](#_CPPv4N7rocprim17counting_iteratorD0Ev) Creates

[counting_iterator](#classrocprim_1_1counting__iterator)with its initial value initialized to its default value (usually 0).

-
__host__ __device__ inline explicit counting_iterator(const
[value_type](#_CPPv4N7rocprim17counting_iterator10value_typeE)value)[#](#_CPPv4N7rocprim17counting_iterator17counting_iteratorEK10value_type) Creates

[counting_iterator](#classrocprim_1_1counting__iterator)and sets its initial value to`value_`

.- Parameters:
**value**– initial value



Note

For example, `counting_iterator(20)`

generates the infinite sequence:

```
20
21
22
23
...
```

## Transform[#](#transform)

-
template<class InputIterator, class UnaryFunction, class ValueType = typename ::rocprim::invoke_result<
[UnaryFunction](#_CPPv4I000EN7rocprim18transform_iteratorE), typename std::iterator_traits<[InputIterator](#_CPPv4I000EN7rocprim18transform_iteratorE)>::value_type>::type>

class transform_iterator[#](#_CPPv4I000EN7rocprim18transform_iteratorE) A random-access input (read-only) iterator adaptor for transforming dereferenced values.

**Overview**A

[transform_iterator](#classrocprim_1_1transform__iterator)uses functor of type UnaryFunction to transform value obtained by dereferencing underlying iterator.Using it for simulating a range filled with results of applying functor of type

`UnaryFunction`

to another range saves memory capacity and/or bandwidth.


- Template Parameters:
**InputIterator**– type of the underlying random-access input iterator. Must be a random-access iterator.**UnaryFunction**– type of the transform functor.**ValueType**– type of value that can be obtained by dereferencing the iterator. By default it is the return type of`UnaryFunction`

.


Public Types

-
using value_type =
[ValueType](#_CPPv4I000EN7rocprim18transform_iteratorE)[#](#_CPPv4N7rocprim18transform_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference = const std::remove_reference_t<
[value_type](#_CPPv4N7rocprim18transform_iterator10value_typeE)>&[#](#_CPPv4N7rocprim18transform_iterator9referenceE) A reference type of the type iterated over (

`value_type`

). It’s`const`

since[transform_iterator](#classrocprim_1_1transform__iterator)is a read-only iterator.

-
using pointer = const detail::proxy_pointer<std::remove_reference_t<
[value_type](#_CPPv4N7rocprim18transform_iterator10value_typeE)>>[#](#_CPPv4N7rocprim18transform_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

). It’s`const`

since[transform_iterator](#classrocprim_1_1transform__iterator)is a read-only iterator.

-
using difference_type = typename std::iterator_traits<
[InputIterator](#_CPPv4I000EN7rocprim18transform_iteratorE)>::difference_type[#](#_CPPv4N7rocprim18transform_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim18transform_iterator17iterator_categoryE) The category of the iterator.


-
using unary_function =
[UnaryFunction](#_CPPv4I000EN7rocprim18transform_iteratorE)[#](#_CPPv4N7rocprim18transform_iterator14unary_functionE) The type of unary function used to transform input range.


Public Functions

-
__host__ __device__ inline transform_iterator(
[InputIterator](#_CPPv4I000EN7rocprim18transform_iteratorE)iterator,[UnaryFunction](#_CPPv4I000EN7rocprim18transform_iteratorE)transform)[#](#_CPPv4N7rocprim18transform_iterator18transform_iteratorE13InputIterator13UnaryFunction) Creates a new

[transform_iterator](#classrocprim_1_1transform__iterator).- Parameters:
**iterator**– input iterator to iterate over and transform.**transform**– unary function used to transform values obtained from range pointed by`iterator`

.




Note

`transform_iterator(sequence, transform)`

should generate the sequence:

```
transform(sequence(0))
transform(sequence(1))
...
```

### Predicate[#](#predicate)

-
template<class DataIterator, class PredicateDataIterator, class UnaryPredicate>

class predicate_iterator[#](#_CPPv4I000EN7rocprim18predicate_iteratorE) A random-access iterator which can discard values assigned to it upon dereference based on a predicate.

**Overview**

can be used to ignore certain input or output of algorithms.[predicate_iterator](#classrocprim_1_1predicate__iterator)When writing to


, it will only write to the underlying iterator if the predicate holds. Otherwise it will discard the value.[predicate_iterator](#classrocprim_1_1predicate__iterator)When reading from


, it will only read from the underlying iterator if the predicate holds. Otherwise it will return the default constructed value.[predicate_iterator](#classrocprim_1_1predicate__iterator)


- Template Parameters:
**DataIterator**– Type of the data iterator that will be forwarded upon dereference.**PredicateDataIterator**– Type of the test iterator used to test the predicate function.**UnaryPredicate**– Type of the predicate function that tests the test.


Public Types

-
using value_type = typename std::iterator_traits<
[DataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)>::value_type[#](#_CPPv4N7rocprim18predicate_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference = typename std::iterator_traits<
[DataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)>::reference[#](#_CPPv4N7rocprim18predicate_iterator9referenceE) A reference type of the type iterated over (

`value_type`

).

-
using pointer = typename std::iterator_traits<
[DataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)>::pointer[#](#_CPPv4N7rocprim18predicate_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

).

-
using difference_type = typename std::iterator_traits<
[DataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)>::difference_type[#](#_CPPv4N7rocprim18predicate_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim18predicate_iterator17iterator_categoryE) The category of the iterator.


Public Functions

-
__host__ __device__ inline predicate_iterator(
[DataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)data_iterator,[PredicateDataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)predicate_iterator,[UnaryPredicate](#_CPPv4I000EN7rocprim18predicate_iteratorE)predicate)[#](#_CPPv4N7rocprim18predicate_iterator18predicate_iteratorE12DataIterator21PredicateDataIterator14UnaryPredicate) Creates a new

[predicate_iterator](#classrocprim_1_1predicate__iterator).- Parameters:
**data_iterator**– The data iterator that will be forwarded whenever the predicate is true.**predicate_iterator**– The test iterator that is used to test the predicate on.**predicate**– Unary function used to select values obtained. from range pointed by`iterator`

.



-
struct proxy
[#](#_CPPv4N7rocprim18predicate_iterator5proxyE) Assignable proxy for values in

`DataIterator`

.Public Types

-
using capture_t = decltype(*std::declval<
[DataIterator](#_CPPv4I000EN7rocprim18predicate_iteratorE)>())[#](#_CPPv4N7rocprim18predicate_iterator5proxy9capture_tE) The return type on the dereference operator. This may be different than

`reference`

.

Public Functions

-
__host__ __device__ inline proxy(
[capture_t](#_CPPv4N7rocprim18predicate_iterator5proxy9capture_tE)val, const bool keep)[#](#_CPPv4N7rocprim18predicate_iterator5proxy5proxyE9capture_tKb) Constructs a

`proxy`

object with the given reference and keep flag.- Parameters:
**val**– The value or reference to be captured.**keep**– Boolean flag that indicates whether to keep the reference.



-
__host__ __device__ inline
[proxy](#_CPPv4N7rocprim18predicate_iterator5proxyE)&operator=(const[value_type](#_CPPv4N7rocprim18predicate_iterator10value_typeE)&value)[#](#_CPPv4N7rocprim18predicate_iterator5proxyaSERK10value_type) Assigns a value to the held reference if the keep flag is

`true`

.- Parameters:
**value**– The value to assign to the captured value.- Returns:
A reference to the (possibly) modified

`proxy`

object.


-
__host__ __device__ inline operator
[value_type](#_CPPv4N7rocprim18predicate_iterator10value_typeE)() const[#](#_CPPv4NK7rocprim18predicate_iterator5proxycv10value_typeEv) Converts the

`proxy`

to the underlying value type.- Returns:
The referenced value or the default-constructed value.



-
using capture_t = decltype(*std::declval<


Note

`predicate_iterator(sequence, test, predicate)`

generates the sequence:


## Pairing Values with Indices[#](#pairing-values-with-indices)

-
template<class InputIterator, class Difference = std::ptrdiff_t, class InputValueType = typename std::iterator_traits<
[InputIterator](#_CPPv4I000EN7rocprim18arg_index_iteratorE)>::value_type>

class arg_index_iterator[#](#_CPPv4I000EN7rocprim18arg_index_iteratorE) A random-access input (read-only) iterator adaptor for pairing dereferenced values with their indices.

**Overview**Dereferencing

[arg_index_iterator](#classrocprim_1_1arg__index__iterator)return a value of`key_value_pair<Difference, InputValueType>`

type, which includes value from the underlying range and its index in that range.`std::iterator_traits<InputIterator>::value_type`

should be convertible to`InputValueType`

.


- Template Parameters:
**InputIterator**– type of the underlying random-access input iterator. Must be a random-access iterator.**Difference**– type used for identify distance between iterators and as the index type in the output pair type (see`value_type`

).**InputValueType**– value type used in the output pair type (see`value_type`

).


Public Types

-
using value_type = ::rocprim::
[key_value_pair](types.html#_CPPv4I00EN7rocprim14key_value_pairE)<[Difference](#_CPPv4I000EN7rocprim18arg_index_iteratorE),[InputValueType](#_CPPv4I000EN7rocprim18arg_index_iteratorE)>[#](#_CPPv4N7rocprim18arg_index_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference = const
[value_type](#_CPPv4N7rocprim18arg_index_iterator10value_typeE)&[#](#_CPPv4N7rocprim18arg_index_iterator9referenceE) A reference type of the type iterated over (

`value_type`

). It’s`const`

since[arg_index_iterator](#classrocprim_1_1arg__index__iterator)is a read-only iterator.

-
using pointer = const detail::proxy_pointer<
[InputValueType](#_CPPv4I000EN7rocprim18arg_index_iteratorE)>[#](#_CPPv4N7rocprim18arg_index_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

). It’s`const`

since[arg_index_iterator](#classrocprim_1_1arg__index__iterator)is a read-only iterator.

-
using difference_type =
[Difference](#_CPPv4I000EN7rocprim18arg_index_iteratorE)[#](#_CPPv4N7rocprim18arg_index_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim18arg_index_iterator17iterator_categoryE) The category of the iterator.


Public Functions

-
__host__ __device__ inline arg_index_iterator(
[InputIterator](#_CPPv4I000EN7rocprim18arg_index_iteratorE)iterator,[difference_type](#_CPPv4N7rocprim18arg_index_iterator15difference_typeE)offset = 0)[#](#_CPPv4N7rocprim18arg_index_iterator18arg_index_iteratorE13InputIterator15difference_type) Creates a new

[arg_index_iterator](#classrocprim_1_1arg__index__iterator).- Parameters:
**iterator**– input iterator pointing to the input range.**offset**– index of the`iterator`

in the input range.




Note

`arg_index_iterator(sequence)`

generates the sequence of tuples:

```
(0, sequence[0])
(1, sequence[1])
...
```

## Zip[#](#zip)

-
template<class IteratorTuple>

class zip_iterator[#](#_CPPv4I0EN7rocprim12zip_iteratorE) TBD.

**Overview**TBD



- Template Parameters:
**IteratorTuple**– -

Public Types

-
using reference = typename detail::tuple_of_references<
[IteratorTuple](#_CPPv4I0EN7rocprim12zip_iteratorE)>::type[#](#_CPPv4N7rocprim12zip_iterator9referenceE) A reference type of the type iterated over.

The type of the tuple made of the reference types of the iterator types in the IteratorTuple argument.


-
using value_type = typename detail::tuple_of_values<
[IteratorTuple](#_CPPv4I0EN7rocprim12zip_iteratorE)>::type[#](#_CPPv4N7rocprim12zip_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using pointer =
[value_type](#_CPPv4N7rocprim12zip_iterator10value_typeE)*[#](#_CPPv4N7rocprim12zip_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

).

-
using difference_type = typename std::iterator_traits<typename ::rocprim::
[tuple_element](types.html#_CPPv4I_6size_t0EN7rocprim13tuple_elementE)<0,[IteratorTuple](#_CPPv4I0EN7rocprim12zip_iteratorE)>::type>::difference_type[#](#_CPPv4N7rocprim12zip_iterator15difference_typeE) A type used for identify distance between iterators.

The difference_type member of

[zip_iterator](#classrocprim_1_1zip__iterator)is the difference_type of the first of the iterator types in the IteratorTuple argument.

-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim12zip_iterator17iterator_categoryE) The category of the iterator.



Note

`zip_iterator(sequence_X, sequence_Y)`

generates the sequence of tuples:

```
(sequence_X[0], sequence_Y[0])
(sequence_X[1], sequence_Y[1])
...
```

## Discard[#](#discard)

-
class discard_iterator
[#](#_CPPv4N7rocprim16discard_iteratorE) A random-access iterator which discards values assigned to it upon dereference.

**Overview**[discard_iterator](#classrocprim_1_1discard__iterator)does not have any underlying array (memory) and does not save values written to it upon dereference.[discard_iterator](#classrocprim_1_1discard__iterator)can be used to safely ignore certain output of algorithms, which saves memory capacity and/or bandwidth.


Public Types

-
using value_type = discard_value
[#](#_CPPv4N7rocprim16discard_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference = discard_value
[#](#_CPPv4N7rocprim16discard_iterator9referenceE) A reference type of the type iterated over (

`value_type`

).

-
using pointer = discard_value*
[#](#_CPPv4N7rocprim16discard_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

).

-
using difference_type = std::ptrdiff_t
[#](#_CPPv4N7rocprim16discard_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim16discard_iterator17iterator_categoryE) The category of the iterator.



## Texture Cache[#](#texture-cache)

-
template<class T, class Difference = std::ptrdiff_t>

class texture_cache_iterator[#](#_CPPv4I00EN7rocprim22texture_cache_iteratorE) A random-access input (read-only) iterator adaptor for dereferencing array values through texture cache. This iterator is not functional on gfx94x architectures.

**Overview**A

[texture_cache_iterator](#classrocprim_1_1texture__cache__iterator)wraps a device pointer of type T, where values are obtained by dereferencing through texture cache.Can be exchanged and manipulated within and between host and device functions.

Can only be constructed within host functions, and can only be dereferenced within device functions.

Accepts any data type from memory, and loads through texture cache.

This iterator is not functional on gfx94x architectures, as native texture fetch functions are not supported in gfx94x.



- Template Parameters:
**T**– type of value that can be obtained by dereferencing the iterator.**Difference**– a type used for identify distance between iterators.


Public Types

-
using value_type = typename std::remove_const<
[T](#_CPPv4I00EN7rocprim22texture_cache_iteratorE)>::type[#](#_CPPv4N7rocprim22texture_cache_iterator10value_typeE) The type of the value that can be obtained by dereferencing the iterator.


-
using reference = const
[value_type](#_CPPv4N7rocprim22texture_cache_iterator10value_typeE)&[#](#_CPPv4N7rocprim22texture_cache_iterator9referenceE) A reference type of the type iterated over (

`value_type`

).

-
using pointer = detail::proxy_pointer<
[value_type](#_CPPv4N7rocprim22texture_cache_iterator10value_typeE)>[#](#_CPPv4N7rocprim22texture_cache_iterator7pointerE) A pointer type of the type iterated over (

`value_type`

).

-
using difference_type =
[Difference](#_CPPv4I00EN7rocprim22texture_cache_iteratorE)[#](#_CPPv4N7rocprim22texture_cache_iterator15difference_typeE) A type used for identify distance between iterators.


-
using iterator_category = std::random_access_iterator_tag
[#](#_CPPv4N7rocprim22texture_cache_iterator17iterator_categoryE) The category of the iterator.


Public Functions

-
template<class Qualified>

inline hipError_t bind_texture([Qualified](#_CPPv4I0EN7rocprim22texture_cache_iterator12bind_textureE10hipError_tP9Qualified6size_t6size_t)*ptr, size_t bytes = size_t(-1), size_t texture_offset = 0)[#](#_CPPv4I0EN7rocprim22texture_cache_iterator12bind_textureE10hipError_tP9Qualified6size_t6size_t) Creates a

`hipTextureObject_t`

and binds this iterator to it.- Template Parameters:
**Texture**– data pointer type- Parameters:
**ptr**– pointer to the texture data on the device**bytes**– size of the texture data (in bytes)**texture_offset**– an offset from ptr to load texture data from (Defaults to 0)



-
inline hipError_t unbind_texture()
[#](#_CPPv4N7rocprim22texture_cache_iterator14unbind_textureEv) Destroys the texture object that this iterator points at.
