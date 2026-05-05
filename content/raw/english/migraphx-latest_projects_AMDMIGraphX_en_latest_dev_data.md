---
title: "Data types"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/data.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:16.852000+00:00
content_hash: "f5c1cf8142644776"
---

# Data types[#](#data-types)

2025-10-14

19 min read time

## shape[#](#shape)

-
struct shape
[#](#_CPPv4N8migraphx8internal5shapeE) Public Types

-
enum type_t
[#](#_CPPv4N8migraphx8internal5shape6type_tE) *Values:*-
enumerator bool_type
[#](#_CPPv4N8migraphx8internal5shape6type_t9bool_typeE)

-
enumerator half_type
[#](#_CPPv4N8migraphx8internal5shape6type_t9half_typeE)

-
enumerator float_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10float_typeE)

-
enumerator double_type
[#](#_CPPv4N8migraphx8internal5shape6type_t11double_typeE)

-
enumerator uint8_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10uint8_typeE)

-
enumerator int8_type
[#](#_CPPv4N8migraphx8internal5shape6type_t9int8_typeE)

-
enumerator uint16_type
[#](#_CPPv4N8migraphx8internal5shape6type_t11uint16_typeE)

-
enumerator int16_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10int16_typeE)

-
enumerator int32_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10int32_typeE)

-
enumerator int64_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10int64_typeE)

-
enumerator uint32_type
[#](#_CPPv4N8migraphx8internal5shape6type_t11uint32_typeE)

-
enumerator uint64_type
[#](#_CPPv4N8migraphx8internal5shape6type_t11uint64_typeE)

-
enumerator fp8e4m3fnuz_type
[#](#_CPPv4N8migraphx8internal5shape6type_t16fp8e4m3fnuz_typeE)

-
enumerator fp8e4m3fn_type
[#](#_CPPv4N8migraphx8internal5shape6type_t14fp8e4m3fn_typeE)

-
enumerator fp8e5m2_type
[#](#_CPPv4N8migraphx8internal5shape6type_t12fp8e5m2_typeE)

-
enumerator bf16_type
[#](#_CPPv4N8migraphx8internal5shape6type_t9bf16_typeE)

-
enumerator fp8e5m2fnuz_type
[#](#_CPPv4N8migraphx8internal5shape6type_t16fp8e5m2fnuz_typeE)

-
enumerator tuple_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10tuple_typeE)

-
enumerator fp4x2_type
[#](#_CPPv4N8migraphx8internal5shape6type_t10fp4x2_typeE)

-
enumerator bool_type

Public Functions

-
shape()
[#](#_CPPv4N8migraphx8internal5shape5shapeEv)

-
shape(
[type_t](#_CPPv4N8migraphx8internal5shape6type_tE)t, std::vector<[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)> dims)[#](#_CPPv4N8migraphx8internal5shape5shapeE6type_tNSt6vectorI17dynamic_dimensionEE)

-
shape(
[type_t](#_CPPv4N8migraphx8internal5shape6type_tE)t, std::vector<std::size_t> mins, std::vector<std::size_t> maxes, std::vector<std::set<std::size_t>> optimals_list)[#](#_CPPv4N8migraphx8internal5shape5shapeE6type_tNSt6vectorINSt6size_tEEENSt6vectorINSt6size_tEEENSt6vectorINSt3setINSt6size_tEEEEE)

-
const std::vector<std::size_t> &lens() const
[#](#_CPPv4NK8migraphx8internal5shape4lensEv)

-
const std::vector<std::size_t> &strides() const
[#](#_CPPv4NK8migraphx8internal5shape7stridesEv)

-
std::size_t ndim() const
[#](#_CPPv4NK8migraphx8internal5shape4ndimEv) The number of dimensions in the shape, either static or dynamic. Same as the number of indices required to get a data value.


-
std::size_t elements() const
[#](#_CPPv4NK8migraphx8internal5shape8elementsEv) Return the number of elements in the tensor.


-
std::size_t bytes() const
[#](#_CPPv4NK8migraphx8internal5shape5bytesEv) Return the number of total bytes used for storage of the tensor data; includes subshapes. For dynamic shape, returns the maximum number of bytes presuming a packed shape.


-
std::size_t type_size() const
[#](#_CPPv4NK8migraphx8internal5shape9type_sizeEv) Return the size of the type of the main shape. Returns 0 if there are subshapes.


-
const std::vector<
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)> &dyn_dims() const[#](#_CPPv4NK8migraphx8internal5shape8dyn_dimsEv)

-
std::vector<std::size_t> min_lens() const
[#](#_CPPv4NK8migraphx8internal5shape8min_lensEv) Minimum lengths for dynamic shape.

[lens()](#structmigraphx_1_1internal_1_1shape_1a85455e6b71648c2c34805e81d8705e1c)for static shape.

-
std::vector<std::size_t> max_lens() const
[#](#_CPPv4NK8migraphx8internal5shape8max_lensEv) Maximum lengths for dynamic shape.

[lens()](#structmigraphx_1_1internal_1_1shape_1a85455e6b71648c2c34805e81d8705e1c)for static shape.

-
std::vector<std::set<std::size_t>> opt_lens() const
[#](#_CPPv4NK8migraphx8internal5shape8opt_lensEv) Optimum lengths for dynamic shape. Empty for static shape.


-
std::size_t index(std::initializer_list<std::size_t> l) const
[#](#_CPPv4NK8migraphx8internal5shape5indexENSt16initializer_listINSt6size_tEEE) Map multiple indices to space index.


-
std::size_t index(const std::vector<std::size_t> &l) const
[#](#_CPPv4NK8migraphx8internal5shape5indexERKNSt6vectorINSt6size_tEEE) Map multiple indices to space index.


-
template<class Iterator>

inline std::size_t index([Iterator](#_CPPv4I0ENK8migraphx8internal5shape5indexENSt6size_tE8Iterator8Iterator)start,[Iterator](#_CPPv4I0ENK8migraphx8internal5shape5indexENSt6size_tE8Iterator8Iterator)last) const[#](#_CPPv4I0ENK8migraphx8internal5shape5indexENSt6size_tE8Iterator8Iterator) Map multiple indices from a range of iterator to a space index.


-
std::size_t index(std::size_t i) const
[#](#_CPPv4NK8migraphx8internal5shape5indexENSt6size_tE) Map element index to space index.


-
std::vector<std::size_t> multi(std::size_t idx) const
[#](#_CPPv4NK8migraphx8internal5shape5multiENSt6size_tE) Map element index to multi-dimensional index.


-
void multi_copy(std::size_t idx, std::size_t *start, const std::size_t *end) const
[#](#_CPPv4NK8migraphx8internal5shape10multi_copyENSt6size_tEPNSt6size_tEPKNSt6size_tE) Map element index to multi-dimensional index and put them them into location provided by pointers


-
bool multi_within_bounds(std::vector<std::size_t> multi) const
[#](#_CPPv4NK8migraphx8internal5shape19multi_within_boundsENSt6vectorINSt6size_tEEE) Check if a multi-dimensional index is within bounds for the shape.


-
template<class Iterator>

inline std::size_t single([Iterator](#_CPPv4I0ENK8migraphx8internal5shape6singleENSt6size_tE8Iterator8Iterator)start,[Iterator](#_CPPv4I0ENK8migraphx8internal5shape6singleENSt6size_tE8Iterator8Iterator)last) const[#](#_CPPv4I0ENK8migraphx8internal5shape6singleENSt6size_tE8Iterator8Iterator) Convert multi-dimensional index into a single element index.


-
std::size_t single(const std::vector<std::size_t> &idx) const
[#](#_CPPv4NK8migraphx8internal5shape6singleERKNSt6vectorINSt6size_tEEE) Convert multi-dimensional index into a single element index.


-
bool packed() const
[#](#_CPPv4NK8migraphx8internal5shape6packedEv) Returns true if the shape is packed (number of elements and buffer size the same) with no padding


-
bool transposed() const
[#](#_CPPv4NK8migraphx8internal5shape10transposedEv) Returns true if the shape has been transposed. That is the strides are not in descending order


-
bool broadcasted() const
[#](#_CPPv4NK8migraphx8internal5shape11broadcastedEv) Returns true if the shape is broadcasting a dimension. That is, one of the strides are zero.


-
bool standard() const
[#](#_CPPv4NK8migraphx8internal5shape8standardEv) Returns true if the shape is in its standard format. That is, the shape is both packed and not transposed.


-
bool scalar() const
[#](#_CPPv4NK8migraphx8internal5shape6scalarEv) Returns true if all strides are equal to 0 (scalar tensor)


-
bool dynamic() const
[#](#_CPPv4NK8migraphx8internal5shape7dynamicEv) Return true if the shape is dynamic.


-
bool any_of_dynamic() const
[#](#_CPPv4NK8migraphx8internal5shape14any_of_dynamicEv) Return true if this shape or any of the sub_shapes are dynamic.


-
bool computable() const
[#](#_CPPv4NK8migraphx8internal5shape10computableEv) If type is computable (can do math ops like add or divide) and has a visitor function.


-
std::string type_string() const
[#](#_CPPv4NK8migraphx8internal5shape11type_stringEv)

-
std::size_t tuple_size() const
[#](#_CPPv4NK8migraphx8internal5shape10tuple_sizeEv)

-
std::size_t element_space() const
[#](#_CPPv4NK8migraphx8internal5shape13element_spaceEv) Returns the number of elements in the data buffer. For a dynamic shape, returns the maximum number of elements of the data buffer and assumes it is packed. Will clip to the maximum of size_t if overflows for dynamic shapes.


Public Static Functions

-
static
[shape](#_CPPv4N8migraphx8internal5shapeE)from_permutation([type_t](#_CPPv4N8migraphx8internal5shape6type_tE)t, const std::vector<std::size_t> &l, const std::vector<int64_t> &perm)[#](#_CPPv4N8migraphx8internal5shape16from_permutationE6type_tRKNSt6vectorINSt6size_tEEERKNSt6vectorI7int64_tEE) Creates an output shape with dimensions

`l`

and strides computed to fulfill the given permutation.`t`

= shape type`l`

= output dimensions`perm`

= order dimensions from slowest dimension to fastest dimensionExample:

`t`

= float_type,`l`

= [2, 3, 4],`perm`

= [1, 2, 0] axis=1 to slowest dimension, axis=2 to second slowest, axis=0 to fastest returns shape{type = float, lens = [2, 3, 4], strides = [1, 8 ,2]}

-
template<class Visitor, class TupleVisitor>

static inline void visit([type_t](#_CPPv4N8migraphx8internal5shape6type_tE)t,[Visitor](#_CPPv4I00EN8migraphx8internal5shape5visitEv6type_t7Visitor12TupleVisitor)v,[TupleVisitor](#_CPPv4I00EN8migraphx8internal5shape5visitEv6type_t7Visitor12TupleVisitor)tv)[#](#_CPPv4I00EN8migraphx8internal5shape5visitEv6type_t7Visitor12TupleVisitor)

Friends

-
template<class T>

struct as[#](#_CPPv4I0EN8migraphx8internal5shape2asE)

-
struct dynamic_dimension
[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE) Public Functions

-
bool is_fixed() const
[#](#_CPPv4NK8migraphx8internal5shape17dynamic_dimension8is_fixedEv)

-
bool has_optimal() const
[#](#_CPPv4NK8migraphx8internal5shape17dynamic_dimension11has_optimalEv)

-
inline std::optional<
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)> intersection(const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&other) const[#](#_CPPv4NK8migraphx8internal5shape17dynamic_dimension12intersectionERK17dynamic_dimension) Return a

[dynamic_dimension](#structmigraphx_1_1internal_1_1shape_1_1dynamic__dimension)with the intersection of two[dynamic_dimension](#structmigraphx_1_1internal_1_1shape_1_1dynamic__dimension)ranges if possible.

-
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&operator+=(const std::size_t &x)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionpLERKNSt6size_tE)

-
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&operator-=(const std::size_t &x)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionmIERKNSt6size_tE)

-
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&operator*=(const std::size_t &x)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionmLERKNSt6size_tE)

Friends

-
friend bool operator==(const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensioneqERK17dynamic_dimensionRK17dynamic_dimension)

-
friend bool operator!=(const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionneERK17dynamic_dimensionRK17dynamic_dimension)

-
friend std::ostream &operator<<(std::ostream &os, const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionlsERNSt7ostreamERK17dynamic_dimension)

-
friend bool operator==(const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const std::size_t &y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensioneqERK17dynamic_dimensionRKNSt6size_tE)

-
friend bool operator==(const std::size_t &x, const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensioneqERKNSt6size_tERK17dynamic_dimension)

-
friend bool operator!=(const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const std::size_t &y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionneERK17dynamic_dimensionRKNSt6size_tE)

-
friend bool operator!=(const std::size_t &x, const
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionneERKNSt6size_tERK17dynamic_dimension)

-
friend
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)operator+(const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const std::size_t &y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionplERK17dynamic_dimensionRKNSt6size_tE)

-
friend
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)operator+(const std::size_t &x, const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionplERKNSt6size_tERK17dynamic_dimension)

-
friend
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)operator-(const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const std::size_t &y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionmiERK17dynamic_dimensionRKNSt6size_tE)

-
friend
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)operator*(const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&x, const std::size_t &y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionmlERK17dynamic_dimensionRKNSt6size_tE)

-
friend
[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)operator*(const std::size_t &x, const[dynamic_dimension](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionE)&y)[#](#_CPPv4N8migraphx8internal5shape17dynamic_dimensionmlERKNSt6size_tERK17dynamic_dimension)

-
bool is_fixed() const

-
template<class T, class = void>

struct get_type[#](#_CPPv4I00EN8migraphx8internal5shape8get_typeE) Subclassed by

[migraphx::internal::shape::get_type< const T >](#structmigraphx_1_1internal_1_1shape_1_1get__type_3_01const_01T_01_4)

-
template<class T>

struct get_type<double,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeId1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[double_type](#_CPPv4N8migraphx8internal5shape6type_t11double_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeId1TEE)

-
template<class T>

struct get_type<float,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeIf1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[float_type](#_CPPv4N8migraphx8internal5shape6type_t10float_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeIf1TEE)

-
template<class T>

struct get_type<int16_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7int16_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[int16_type](#_CPPv4N8migraphx8internal5shape6type_t10int16_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7int16_t1TEE)

-
template<class T>

struct get_type<int32_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7int32_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[int32_type](#_CPPv4N8migraphx8internal5shape6type_t10int32_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7int32_t1TEE)

-
template<class T>

struct get_type<int64_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7int64_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[int64_type](#_CPPv4N8migraphx8internal5shape6type_t10int64_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7int64_t1TEE)

- template<class T> fp8e4m3fn, T > : public std::integral_constant< type_t, fp8e4m3fn_type >

- template<class T> fp8e4m3fnuz, T > : public std::integral_constant< type_t, fp8e4m3fnuz_type >

- template<class T> fp8e5m2, T > : public std::integral_constant< type_t, fp8e5m2_type >

- template<class T> fp8e5m2fnuz, T > : public std::integral_constant< type_t, fp8e5m2fnuz_type >

-
template<class T>

struct get_type<uint16_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI8uint16_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[uint16_type](#_CPPv4N8migraphx8internal5shape6type_t11uint16_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI8uint16_t1TEE)

-
template<class T>

struct get_type<uint32_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI8uint32_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[uint32_type](#_CPPv4N8migraphx8internal5shape6type_t11uint32_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI8uint32_t1TEE)

-
template<class T>

struct get_type<uint64_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI8uint64_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[uint64_type](#_CPPv4N8migraphx8internal5shape6type_t11uint64_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI8uint64_t1TEE)

-
template<class T>

struct get_type<uint8_t,[T](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7uint8_t1TEE)> : public std::integral_constant<[type_t](#_CPPv4N8migraphx8internal5shape6type_tE),[uint8_type](#_CPPv4N8migraphx8internal5shape6type_t10uint8_typeE)>[#](#_CPPv4I0EN8migraphx8internal5shape8get_typeI7uint8_t1TEE)

-
enum type_t

## literal[#](#literal)

-
struct literal : public migraphx::internal::raw_data<
[literal](#_CPPv4N8migraphx7literalE)>[#](#_CPPv4N8migraphx7literalE) Represents a raw literal.

This stores the literal has a raw buffer that is owned by this class

Public Functions

-
inline literal()
[#](#_CPPv4N8migraphx7literal7literalEv)

-
template<class U, class T = deduce<
[U](#_CPPv4I00_N5shape6type_tEEN8migraphx7literal7literalE1U)>,[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)::type_t ShapeType =[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)::get_type<[T](#_CPPv4I00_N5shape6type_tEEN8migraphx7literal7literalE1U)>{}>

inline literal([U](#_CPPv4I00_N5shape6type_tEEN8migraphx7literal7literalE1U)x)[#](#_CPPv4I00_N5shape6type_tEEN8migraphx7literal7literalE1U)

-
template<class T, long PrivateRequires__LINE__ = __LINE__, typename std::enable_if<(
[PrivateRequires__LINE__](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXeqst1TL1EEEEEEiE4typeEEN8migraphx7literal7literalERK5shapeP1T)== __LINE__ and (migraphx::and_<sizeof([T](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXeqst1TL1EEEEEEiE4typeEEN8migraphx7literal7literalERK5shapeP1T)) == 1>{})), int>::type = 0>

inline literal(const[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&s,[T](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXeqst1TL1EEEEEEiE4typeEEN8migraphx7literal7literalERK5shapeP1T)*x)[#](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXeqst1TL1EEEEEEiE4typeEEN8migraphx7literal7literalERK5shapeP1T)

-
inline bool empty() const
[#](#_CPPv4NK8migraphx7literal5emptyEv) Whether data is available.


-
inline const char *data() const
[#](#_CPPv4NK8migraphx7literal4dataEv) Provides a raw pointer to the data.


-
inline literal()

## argument[#](#argument)

-
struct argument : public migraphx::internal::raw_data<
[argument](#_CPPv4N8migraphx8internal8argumentE)>[#](#_CPPv4N8migraphx8internal8argumentE) Arguments passed to instructions.

An

`argument`

can represent a raw buffer of data that either be referenced from another element or it can be owned by the argument.Public Functions

-
argument() = default
[#](#_CPPv4N8migraphx8internal8argument8argumentEv)

-
template<class F, long PrivateRequires__LINE__ = __LINE__, typename std::enable_if<(
[PrivateRequires__LINE__](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXclNSt10is_pointerIDTclclNSt7declvalI1FEEEEEEEEEEEEEiE4typeEEN8migraphx8internal8argument8argumentE5shape1F)== __LINE__ and (migraphx::and_<std::is_pointer<decltype(std::declval<[F](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXclNSt10is_pointerIDTclclNSt7declvalI1FEEEEEEEEEEEEEiE4typeEEN8migraphx8internal8argument8argumentE5shape1F)>()())>{}>{})), int>::type = 0>

inline argument([shape](#_CPPv4N8migraphx8internal5shapeE)s,[F](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXclNSt10is_pointerIDTclclNSt7declvalI1FEEEEEEEEEEEEEiE4typeEEN8migraphx8internal8argument8argumentE5shape1F)d)[#](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXclNSt10is_pointerIDTclclNSt7declvalI1FEEEEEEEEEEEEEiE4typeEEN8migraphx8internal8argument8argumentE5shape1F)

-
char *data() const
[#](#_CPPv4NK8migraphx8internal8argument4dataEv) Provides a raw pointer to the data.


-
bool empty() const
[#](#_CPPv4NK8migraphx8internal8argument5emptyEv) Whether data is available.


Make copy of the argument that is always sharing the data.


-
argument() = default

## raw_data[#](#raw-data)

-
template<class Derived>

struct raw_data : public migraphx::internal::raw_data_base[#](#_CPPv4I0EN8migraphx8raw_dataE) Provides a base class for common operations with raw buffer.

For classes that handle a raw buffer of data, this will provide common operations such as equals, printing, and visitors. To use this class the derived class needs to provide a

`data()`

method to retrieve a raw pointer to the data, and`get_shape`

method that provides the shape of the data.Public Functions

-
template<class Visitor, class Index = std::size_t>

inline void visit_at([Visitor](#_CPPv4I00ENK8migraphx8raw_data8visit_atEv7Visitor5Index)v,[Index](#_CPPv4I00ENK8migraphx8raw_data8visit_atEv7Visitor5Index)n = 0) const[#](#_CPPv4I00ENK8migraphx8raw_data8visit_atEv7Visitor5Index) Visits a single data element at a certain index.

- Parameters:
**v**– A function which will be called with the type of data**n**– The index to read from



-
template<class Visitor, class TupleVisitor>

inline void visit([Visitor](#_CPPv4I00ENK8migraphx8raw_data5visitEv7Visitor12TupleVisitor)v,[TupleVisitor](#_CPPv4I00ENK8migraphx8raw_data5visitEv7Visitor12TupleVisitor)tv) const[#](#_CPPv4I00ENK8migraphx8raw_data5visitEv7Visitor12TupleVisitor)

-
template<class Visitor>

inline void visit([Visitor](#_CPPv4I0ENK8migraphx8raw_data5visitEv7Visitor)v) const[#](#_CPPv4I0ENK8migraphx8raw_data5visitEv7Visitor) Visits the data.

This will call the visitor function with a


based on the shape of the data.[tensor_view](#structmigraphx_1_1internal_1_1tensor__view)<T>- Parameters:
**v**– A function to be called with[tensor_view](#structmigraphx_1_1internal_1_1tensor__view)<T>


-
template<class Visitor, class TupleVisitor>

inline void fallback_visit([Visitor](#_CPPv4I00ENK8migraphx8raw_data14fallback_visitEv7Visitor12TupleVisitor)v,[TupleVisitor](#_CPPv4I00ENK8migraphx8raw_data14fallback_visitEv7Visitor12TupleVisitor)tv) const[#](#_CPPv4I00ENK8migraphx8raw_data14fallback_visitEv7Visitor12TupleVisitor) Visit the data using the normal visit function for computable types. For non-computable types, use a tensor_view<byte> with shape = {type = uint8_type, lens = {num bytes}};


-
inline bool single() const
[#](#_CPPv4NK8migraphx8raw_data6singleEv) Returns true if the raw data is only one element.


-
template<class T, class Index = std::size_t>

inline[T](#_CPPv4I00ENK8migraphx8raw_data2atE1T5Index)at([Index](#_CPPv4I00ENK8migraphx8raw_data2atE1T5Index)n = 0) const[#](#_CPPv4I00ENK8migraphx8raw_data2atE1T5Index) Retrieves a single element of data.

- Parameters:
**n**– The index to retrieve the data from- Template Parameters:
**T**– The type of data to be retrieved- Returns:
The element as

`T`



-
template<class T>

inline tensor_view<[T](#_CPPv4I0ENK8migraphx8raw_data3getE11tensor_viewI1TEv)> get() const[#](#_CPPv4I0ENK8migraphx8raw_data3getE11tensor_viewI1TEv) Get a

[tensor_view](#structmigraphx_1_1internal_1_1tensor__view)to the data. For[get<byte>()](#structmigraphx_1_1internal_1_1raw__data_1a60fa6e2ca7f0a62d13e6f229e856775f)returns a 1D tensor_view<const byte*>.

-
inline std::string to_string() const
[#](#_CPPv4NK8migraphx8raw_data9to_stringEv)

-
template<class Visitor, class Index = std::size_t>

-
template<class T, class ...Ts>

auto migraphx::internal::visit_all([T](#_CPPv4I0DpEN8migraphx8internal9visit_allEDaRR1TDpRR2Ts)&&x,[Ts](#_CPPv4I0DpEN8migraphx8internal9visit_allEDaRR1TDpRR2Ts)&&... xs)[#](#_CPPv4I0DpEN8migraphx8internal9visit_allEDaRR1TDpRR2Ts) Visits every object together.

This will visit every object, but assumes each object is the same type. This can reduce the deeply nested visit calls. Returns a function that takes the visitor callback. Calling syntax is

`visit_all(xs...)([](auto... ys) {})`

where`xs...`

and`ys...`

are the same number of parameters.- Parameters:
**x**– A raw data object**xs**– Many raw data objects.

- Returns:
A function to be called with the visitor



-
template<class T>

auto migraphx::internal::visit_all(const std::vector<[T](#_CPPv4I0EN8migraphx8internal9visit_allEDaRKNSt6vectorI1TEE)> &x)[#](#_CPPv4I0EN8migraphx8internal9visit_allEDaRKNSt6vectorI1TEE) Visits every object together.

This will visit every object, but assumes each object is the same type. This can reduce the deeply nested visit calls. Returns a function that takes the visitor callback.

- Parameters:
**x**– A vector of raw data objects. Types must all be the same.- Returns:
A function to be called with the visitor



## tensor_view[#](#tensor-view)

-
template<class T>

struct tensor_view[#](#_CPPv4I0EN8migraphx8internal11tensor_viewE) Public Types

-
using iterator = basic_iota_iterator<tensor_view_iterator_read<
[tensor_view](#_CPPv4I0EN8migraphx8internal11tensor_viewE)<[T](#_CPPv4I0EN8migraphx8internal11tensor_viewE)>>, std::size_t>[#](#_CPPv4N8migraphx8internal11tensor_view8iteratorE)

-
using const_iterator = basic_iota_iterator<tensor_view_iterator_read<const
[tensor_view](#_CPPv4I0EN8migraphx8internal11tensor_viewE)<[T](#_CPPv4I0EN8migraphx8internal11tensor_viewE)>>, std::size_t>[#](#_CPPv4N8migraphx8internal11tensor_view14const_iteratorE)

Public Functions

-
inline tensor_view()
[#](#_CPPv4N8migraphx8internal11tensor_view11tensor_viewEv)

-
inline bool empty() const
[#](#_CPPv4NK8migraphx8internal11tensor_view5emptyEv)

-
inline std::size_t size() const
[#](#_CPPv4NK8migraphx8internal11tensor_view4sizeEv)

-
template<class ...Ts, long PrivateRequires__LINE__ = __LINE__, typename std::enable_if<(
[PrivateRequires__LINE__](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1TDp2Ts)== __LINE__ and (migraphx::and_<std::is_integral<[Ts](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1TDp2Ts)>{}...>{})), int>::type = 0>

inline const[T](#_CPPv4I0EN8migraphx8internal11tensor_viewE)&operator()([Ts](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1TDp2Ts)... xs) const[#](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1TDp2Ts)

-
template<class ...Ts, long PrivateRequires__LINE__ = __LINE__, typename std::enable_if<(
[PrivateRequires__LINE__](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1TDp2Ts)== __LINE__ and (migraphx::and_<std::is_integral<[Ts](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1TDp2Ts)>{}...>{})), int>::type = 0>

inline[T](#_CPPv4I0EN8migraphx8internal11tensor_viewE)&operator()([Ts](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1TDp2Ts)... xs)[#](#_CPPv4IDp_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IJXclNSt11is_integralI2TsEEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1TDp2Ts)

-
template<class Iterator, long PrivateRequires__LINE__ = __LINE__, typename std::enable_if<(
[PrivateRequires__LINE__](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1T8Iterator8Iterator)== __LINE__ and (migraphx::and_<not std::is_integral<[Iterator](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1T8Iterator8Iterator)>{}>{})), int>::type = 0>

inline const[T](#_CPPv4I0EN8migraphx8internal11tensor_viewE)&operator()([Iterator](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1T8Iterator8Iterator)start,[Iterator](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1T8Iterator8Iterator)last) const[#](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEENK8migraphx8internal11tensor_viewclERK1T8Iterator8Iterator)

-
template<class Iterator, long PrivateRequires__LINE__ = __LINE__, typename std::enable_if<(
[PrivateRequires__LINE__](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1T8Iterator8Iterator)== __LINE__ and (migraphx::and_<not std::is_integral<[Iterator](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1T8Iterator8Iterator)>{}>{})), int>::type = 0>

inline[T](#_CPPv4I0EN8migraphx8internal11tensor_viewE)&operator()([Iterator](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1T8Iterator8Iterator)start,[Iterator](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1T8Iterator8Iterator)last)[#](#_CPPv4I0_l_NSt9enable_ifIXaaeq23PrivateRequires__LINE__8__LINE__clN8migraphx4and_IXntclNSt11is_integralI8IteratorEEEEEEEEiE4typeEEN8migraphx8internal11tensor_viewclER1T8Iterator8Iterator)

-
template<class Range>

inline auto operator[](const[Range](#_CPPv4I0EN8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range)&r) -> decltype((*this)([r](#_CPPv4I0EN8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range).begin(),[r](#_CPPv4I0EN8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range).end()))[#](#_CPPv4I0EN8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range)

-
template<class Range>

inline auto operator[](const[Range](#_CPPv4I0ENK8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range)&r) const -> decltype((*this)([r](#_CPPv4I0ENK8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range).begin(),[r](#_CPPv4I0ENK8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range).end()))[#](#_CPPv4I0ENK8migraphx8internal11tensor_viewixEDTcldefpTcldt1r5beginEcldt1r3endEEERK5Range)

-
inline
[const_iterator](#_CPPv4N8migraphx8internal11tensor_view14const_iteratorE)begin() const[#](#_CPPv4NK8migraphx8internal11tensor_view5beginEv)

-
template<class Range>

inline[const_iterator](#_CPPv4N8migraphx8internal11tensor_view14const_iteratorE)begin_at(const[Range](#_CPPv4I0ENK8migraphx8internal11tensor_view8begin_atE14const_iteratorRK5Range)&r) const[#](#_CPPv4I0ENK8migraphx8internal11tensor_view8begin_atE14const_iteratorRK5Range)

-
inline
[const_iterator](#_CPPv4N8migraphx8internal11tensor_view14const_iteratorE)end() const[#](#_CPPv4NK8migraphx8internal11tensor_view3endEv)

-
template<class Range>

inline[tensor_view](#_CPPv4I0EN8migraphx8internal11tensor_viewE)slice_at(std::initializer_list<std::int64_t> axes,[Range](#_CPPv4I0EN8migraphx8internal11tensor_view8slice_atE11tensor_viewNSt16initializer_listINSt7int64_tEEERR5Range)&&r)[#](#_CPPv4I0EN8migraphx8internal11tensor_view8slice_atE11tensor_viewNSt16initializer_listINSt7int64_tEEERR5Range)

-
using iterator = basic_iota_iterator<tensor_view_iterator_read<
