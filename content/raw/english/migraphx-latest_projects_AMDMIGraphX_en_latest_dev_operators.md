---
title: "Operators"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/operators.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:42.185778+00:00
content_hash: "c4517856eb459048"
---

# Operators[#](#operators)

2025-10-14

94 min read time

## operation[#](#operation)

-
struct operation
[#](#_CPPv4N8migraphx8internal9operationE) The operation interface represents an action an instruction will perform. All operation classes must be CopyConstructible.

Public Functions

-
std::string name() const
[#](#_CPPv4NK8migraphx8internal9operation4nameEv) A unique name identifying the operation.


-
void finalize(context &ctx)
[#](#_CPPv4N8migraphx8internal9operation8finalizeER7context) An optional method that can be used to finalize the operator before running.


-
[shape](data.html#_CPPv4N8migraphx8internal5shapeE)compute_shape(const std::vector<[shape](data.html#_CPPv4N8migraphx8internal5shapeE)> &input) const[#](#_CPPv4NK8migraphx8internal9operation13compute_shapeERKNSt6vectorI5shapeEE) This is used to compute the resulting shape from an operation. If an operation cannot be run with input shapes, then it should throw an exception.


-
[argument](data.html#_CPPv4N8migraphx8internal8argumentE)compute(context &ctx, const[shape](data.html#_CPPv4N8migraphx8internal5shapeE)&output, const std::vector<[argument](data.html#_CPPv4N8migraphx8internal8argumentE)> &input) const[#](#_CPPv4NK8migraphx8internal9operation7computeER7contextRK5shapeRKNSt6vectorI8argumentEE) This performs the operation’s computation.

This method can be optional when the operation is only used as a placeholder to be lowered later on.

- Parameters:
**ctx**– This is the context created by the`target`

during compilation. Implementations can use the target’s`context`

class rather than the`context`

interface class.**output**– Equivalent to running`compute_shape`

with each`shape`

of the`argument`

. For a fixed shape, the returned argument will have the same shape as`output`

. For a dynamic shape, the returned`argument`

will be a fixed shape within the bounds set in the dynamic shape`output`

.**input**– This is the`argument`

result from the previous instruction’s computation.

- Returns:
Return an

`argument`

of the result computation. The`shape`

of`argument`

should be the same the`output`

shape.


-
std::string name() const

## operators[#](#id1)

-
namespace op
[#](#_CPPv4N8migraphx2opE) Unpacks fastest dimension of tensor into fp8e4m3fn_type such that the output dimensions are [x_0, …, 2 * x_pack, …]

Enums

-
enum class normalize_attribute
[#](#_CPPv4N8migraphx2op19normalize_attributeE) `normalize_attribute`

settings: Note that default options are not included as enums.`use_input`

(default) vs.`use_output`

: Affects the rank of the attribute.`use_input -> lens.size()`

,`use_output -> lens.size() + vec.size()`

.use_rank (default) vs use_len:

`use_rank`

sets the max value/index of the attribute as the rank of lens.`use_lens`

sets the max value/index as the corresponding value in lens at the axes index. Uses the dynamic_dimension.max value for dynamic shapes. Returns the original vector (no normalization) if any of dynamic_dimension[axes] are not fixed.`clip_min`

vs.`not_clip_min`

(default): Clip values less than the minimum to the minimum or not.`include_min`

vs.`exclude_min`

(default): Include or exclude the minimum value/index for range checking and clipping.`clip_max`

vs.`not_clip_max`

(default): Clip values greater than the maximum or not.`include_max`

vs.`exclude_max`

(default): Include or exclude the maximum value/index for range checking and clipping.`normalize_padding`

: To normalize the padding to`2*(pad ndim)`

dimensions.

*Values:*-
enumerator use_output
[#](#_CPPv4N8migraphx2op19normalize_attribute10use_outputE)

-
enumerator use_len
[#](#_CPPv4N8migraphx2op19normalize_attribute7use_lenE)

-
enumerator clip_max
[#](#_CPPv4N8migraphx2op19normalize_attribute8clip_maxE)

-
enumerator clip_min
[#](#_CPPv4N8migraphx2op19normalize_attribute8clip_minE)

-
enumerator include_max
[#](#_CPPv4N8migraphx2op19normalize_attribute11include_maxE)

-
enumerator include_min
[#](#_CPPv4N8migraphx2op19normalize_attribute11include_minE)

-
enumerator normalize_padding
[#](#_CPPv4N8migraphx2op19normalize_attribute17normalize_paddingE)


Functions

-
std::ostream &operator<<(std::ostream &os,
[pooling_mode](#_CPPv4N8migraphx2op12pooling_modeE)v)[#](#_CPPv4N8migraphx2oplsERNSt7ostreamE12pooling_mode)

-
std::ostream &operator<<(std::ostream &os,
[rnn_direction](#_CPPv4N8migraphx2op13rnn_directionE)v)[#](#_CPPv4N8migraphx2oplsERNSt7ostreamE13rnn_direction)

-
struct allocate
[#](#_CPPv4N8migraphx2op8allocateE) *#include <migraphx/op/allocate.hpp>*Static allocate: No inputs:

`allocate()`

`this.s`

attribute set to the static output shape of the buffer.`this.s`

attribute can be set to a dynamic output shape; however this will allocate the maximum buffer size for that caseDynamic allocate: One input:

`allocate(output_dims)`

`output_dims`

are the output buffer dimensions and has a static shape. Either`this.s`

or`this.buf_type`

(but not both) must be set to calculate the dynamic output shape at compute time. If`this.buf_type`

is set, the[compute_shape()](#structmigraphx_1_1internal_1_1op_1_1allocate_1a595361901fcd490104e67899a2456bb9)of allocate at compile time will have dynamic_dimensions from {0, max_int} with rank = output_dims.ndim(). If`this.s`

is set then the[compute_shape()](#structmigraphx_1_1internal_1_1op_1_1allocate_1a595361901fcd490104e67899a2456bb9)will output`this.s`

;`this.s`

should be a dynamic shape.

-
struct argmax
[#](#_CPPv4N8migraphx2op6argmaxE) *#include <migraphx/op/argmax.hpp>*

-
struct argmin
[#](#_CPPv4N8migraphx2op6argminE) *#include <migraphx/op/argmin.hpp>*

-
struct as_shape
[#](#_CPPv4N8migraphx2op8as_shapeE) *#include <migraphx/op/as_shape.hpp>*

-
template<class Derived>

struct binary : public migraphx::internal::op::op_name<[Derived](#_CPPv4I0EN8migraphx2op6binaryE)>[#](#_CPPv4I0EN8migraphx2op6binaryE) *#include <migraphx/op/binary.hpp>*

-
struct bit_cast : public migraphx::internal::op::unary<
[bit_cast](#_CPPv4N8migraphx2op8bit_castE)>[#](#_CPPv4N8migraphx2op8bit_castE) *#include <migraphx/op/bit_cast.hpp>*Obtain a value of type

`target_type`

by reinterpreting the object represnetaion of the input. Originally used for casting from fp8e4m3fn to fp8e4m3fnuz.

-
struct bitwise_and : public migraphx::internal::op::binary<
[bitwise_and](#_CPPv4N8migraphx2op11bitwise_andE)>[#](#_CPPv4N8migraphx2op11bitwise_andE) *#include <migraphx/op/bitwise_and.hpp>*

-
struct broadcast
[#](#_CPPv4N8migraphx2op9broadcastE) *#include <migraphx/op/broadcast.hpp>*1 input version: Broadcasts a tensor from the original shape to the broadcast_lens by setting the stride of broadcasted dimensions to zero.

`axis`

attribute for a 1D input shape is the output dimension that stays the same. ex: broadcasting shape [1024] -> [4, 1024, 3] has axis = 1.For higher rank input shapes, axis is an offset parameter for the broadcasting. Such that this operator would work in the opposite direction of NumPy broadcasting (left-most to rightwards element-wise comparison) ex: broadcasting shape [2, 2] -> [2, 2, 3] with axis = 0

2 input version: Broadcast the first input 1D shape into the second input shape based on the axis parameter. Handles broadcasting a 1D static shape into a higher rank dynamic shape. broadcast_lens is not used


-
struct broadcast_for_dot
[#](#_CPPv4N8migraphx2op17broadcast_for_dotE) *#include <migraphx/op/broadcast_for_dot.hpp>*Broadcast dimensions between two tensors for the

`dot`

operator. Essentially broadcasts between two shapes for dimensions other than the last two. This operator is only needed if one of the shapes are dynamic. Example: a = shape[{1, 4}, 3, 248, 248] b = shape[248, 365] broadcast_for_dot(a, b) => shape[{1, 4}, 3, 248, 248] (no change) broadcast_for_dot(b, a) => shape[{1, 4}, 3, 248, 365]

-
struct broadcast_with_dims
[#](#_CPPv4N8migraphx2op19broadcast_with_dimsE) *#include <migraphx/op/broadcast_with_dims.hpp>*Broadcast the input tensor to the shape defined by the values of the second input. Used as

`broadcast_with_dims(input_tensor, dims)`

, where dims is a vector of integer dimensions.`input_tensor`

must be broadcastable with`dims`

, otherwise this operator with throw at compute. This operator can be replaced with`multibroadcast(input_tensor)`

if the`dims`

vector is constant.Example: input_tensor shape: lens = {2, 3}, strides = {3, 1} dims = [4, 1, 3] output shape: lens = {4, 2, 3}, strides = {0, 3, 1}


-
struct cache_parameters
[#](#_CPPv4N8migraphx2op16cache_parametersE) *#include <migraphx/op/concat_past_present.hpp>*

-
struct capture
[#](#_CPPv4N8migraphx2op7captureE) *#include <migraphx/op/capture.hpp>*

-
struct clip
[#](#_CPPv4N8migraphx2op4clipE) *#include <migraphx/op/clip.hpp>*

-
struct concat
[#](#_CPPv4N8migraphx2op6concatE) *#include <migraphx/op/concat.hpp>*

-
struct concat_past_present
[#](#_CPPv4N8migraphx2op19concat_past_presentE) *#include <migraphx/op/concat_past_present.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op19concat_past_present4nameEv)

-
template<typename T>

inline[T](#_CPPv4I0ENK8migraphx2op19concat_past_present18concat_state_chunkE1TK1TK1TNSt6size_tENSt6size_tENSt6size_tENSt9ptrdiff_tE)concat_state_chunk(const[T](#_CPPv4I0ENK8migraphx2op19concat_past_present18concat_state_chunkE1TK1TK1TNSt6size_tENSt6size_tENSt6size_tENSt9ptrdiff_tE)chunk, const[T](#_CPPv4I0ENK8migraphx2op19concat_past_present18concat_state_chunkE1TK1TK1TNSt6size_tENSt6size_tENSt6size_tENSt9ptrdiff_tE)present, std::size_t present_buff_chunk_length, std::size_t past_chunk_length, std::size_t new_chunk_length, std::ptrdiff_t i) const[#](#_CPPv4I0ENK8migraphx2op19concat_past_present18concat_state_chunkE1TK1TK1TNSt6size_tENSt6size_tENSt6size_tENSt9ptrdiff_tE)

-
template<class T, class U>

inline void update_cache([T](#_CPPv4I00ENK8migraphx2op19concat_past_present12update_cacheEv1TK1UK1T16cache_parameters)past_key, const[U](#_CPPv4I00ENK8migraphx2op19concat_past_present12update_cacheEv1TK1UK1T16cache_parameters)seqlens_k, const[T](#_CPPv4I00ENK8migraphx2op19concat_past_present12update_cacheEv1TK1UK1T16cache_parameters)present_key,[cache_parameters](#_CPPv4N8migraphx2op16cache_parametersE)params) const[#](#_CPPv4I00ENK8migraphx2op19concat_past_present12update_cacheEv1TK1UK1T16cache_parameters)

-
inline std::string name() const

-
struct contiguous
[#](#_CPPv4N8migraphx2op10contiguousE) *#include <migraphx/op/contiguous.hpp>*The contiguous operator takes a non-standard input tensor and returns the same tensor but in standard form. For example, if input tensor A which has lens = (4,5) is first transposed, i.e. lens = (5,4), this tensor’s data layout remained the same during the transpose operation; only it’s shape lengths and strides were changed. This leaves the tensor in a non-standard form. The contiguous operator copies the underlying data such that resulting tensor is returned to a standard form.


-
struct convolution
[#](#_CPPv4N8migraphx2op11convolutionE) *#include <migraphx/op/convolution.hpp>*Convolution operator. Does not support optimal dimensions for spatial dimensions. Returns empty optimals.

Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op11convolution4nameEv)

-
inline void check_attribute_size() const
[#](#_CPPv4NK8migraphx2op11convolution20check_attribute_sizeEv)

-
inline std::vector<std::size_t> calc_conv_lens(std::vector<std::size_t> x_lens, std::vector<std::size_t> w_lens) const
[#](#_CPPv4NK8migraphx2op11convolution14calc_conv_lensENSt6vectorINSt6size_tEEENSt6vectorINSt6size_tEEE)

-
inline size_t kdims() const
[#](#_CPPv4NK8migraphx2op11convolution5kdimsEv)

-
inline std::string name() const

-
struct convolution_backwards
[#](#_CPPv4N8migraphx2op21convolution_backwardsE) *#include <migraphx/op/convolution_backwards.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op21convolution_backwards4nameEv)

-
inline void check_attribute_size() const
[#](#_CPPv4NK8migraphx2op21convolution_backwards20check_attribute_sizeEv)

-
inline std::vector<std::size_t> calc_spatial_lens(std::vector<std::size_t> x_lens, std::vector<std::size_t> w_lens) const
[#](#_CPPv4NK8migraphx2op21convolution_backwards17calc_spatial_lensENSt6vectorINSt6size_tEEENSt6vectorINSt6size_tEEE)

-
inline size_t kdims() const
[#](#_CPPv4NK8migraphx2op21convolution_backwards5kdimsEv)

-
inline std::string name() const

-
struct dequantizelinear
[#](#_CPPv4N8migraphx2op16dequantizelinearE) *#include <migraphx/op/dequantizelinear.hpp>*

-
struct dimensions_of
[#](#_CPPv4N8migraphx2op13dimensions_ofE) *#include <migraphx/op/dimensions_of.hpp>*Returns the dimensions of the input argument from starting axis to ending axis. Atleast

`end`

must be set to use this operator (set`end`

to ndim for default ONNX behavior of`Shape`

operator) This should only be used for dynamic shapes as this can be simplified to a literal for static shapes.

-
struct dot
[#](#_CPPv4N8migraphx2op3dotE) *#include <migraphx/op/dot.hpp>*Matrix multiplication of two tensors.


-
struct fill
[#](#_CPPv4N8migraphx2op4fillE) *#include <migraphx/op/fill.hpp>*fill(default_value, output_buffer) Fill an output buffer with the given default_value. Note that if the default_value is a literal and the output_buffer has a static shape this operator can be replaced with a literal.


-
struct fixed_pad
[#](#_CPPv4N8migraphx2op9fixed_padE) *#include <migraphx/op/fixed_pad.hpp>*Pads an input with dynamic shape to its maximum dimensions. No-op for a static shape input. The main use for this op versus the standard pad op is that it can accept a dynamic input shape and convert it to a padded static shape.


-
struct flatten
[#](#_CPPv4N8migraphx2op7flattenE) *#include <migraphx/op/flatten.hpp>*

-
struct gather
[#](#_CPPv4N8migraphx2op6gatherE) *#include <migraphx/op/gather.hpp>*

-
struct gathernd
[#](#_CPPv4N8migraphx2op8gatherndE) *#include <migraphx/op/gathernd.hpp>*

-
struct get_tuple_elem
[#](#_CPPv4N8migraphx2op14get_tuple_elemE) *#include <migraphx/op/get_tuple_elem.hpp>*

-
struct gqa_rotary_embedding
[#](#_CPPv4N8migraphx2op20gqa_rotary_embeddingE) *#include <migraphx/op/gqa_rotary_embedding.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op20gqa_rotary_embedding4nameEv)

-
template<class T>

inline void run_rotary_embedding([T](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding20run_rotary_embeddingEv1T1T1T1TPK6size_t17rotary_parameters)input,[T](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding20run_rotary_embeddingEv1T1T1T1TPK6size_t17rotary_parameters)cos_cache,[T](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding20run_rotary_embeddingEv1T1T1T1TPK6size_t17rotary_parameters)sin_cache,[T](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding20run_rotary_embeddingEv1T1T1T1TPK6size_t17rotary_parameters)output, const size_t *pos_ids,[rotary_parameters](#_CPPv4N8migraphx2op20gqa_rotary_embedding17rotary_parametersE)params) const[#](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding20run_rotary_embeddingEv1T1T1T1TPK6size_t17rotary_parameters)

-
template<class T>

inline void pack_v_into_rotary_qkv([rotary_parameters](#_CPPv4N8migraphx2op20gqa_rotary_embedding17rotary_parametersE)params, const[T](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding22pack_v_into_rotary_qkvEv17rotary_parametersK1T1T)input,[T](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding22pack_v_into_rotary_qkvEv17rotary_parametersK1T1T)output) const[#](#_CPPv4I0ENK8migraphx2op20gqa_rotary_embedding22pack_v_into_rotary_qkvEv17rotary_parametersK1T1T)

-
struct rotary_parameters
[#](#_CPPv4N8migraphx2op20gqa_rotary_embedding17rotary_parametersE) *#include <migraphx/op/gqa_rotary_embedding.hpp>*

-
inline std::string name() const

-
struct group
[#](#_CPPv4N8migraphx2op5groupE) *#include <migraphx/op/group.hpp>*

-
struct gru
[#](#_CPPv4N8migraphx2op3gruE) *#include <migraphx/op/gru.hpp>*

-
struct highest
[#](#_CPPv4N8migraphx2op7highestE) *#include <migraphx/op/reduce_op.hpp>*

-
struct identity
[#](#_CPPv4N8migraphx2op8identityE) *#include <migraphx/op/identity.hpp>*

-
struct if_op
[#](#_CPPv4N8migraphx2op5if_opE) *#include <migraphx/op/if_op.hpp>*

-
struct im2col
[#](#_CPPv4N8migraphx2op6im2colE) *#include <migraphx/op/im2col.hpp>*

-
struct layout : public migraphx::internal::op::unary<
[layout](#_CPPv4N8migraphx2op6layoutE)>[#](#_CPPv4N8migraphx2op6layoutE) *#include <migraphx/op/layout.hpp>*Rearrange the memory layout of the input instruction based on the permutation attribute. This operator changes the order of elements in memory,

*not*the order in the tensor. Therefore, regardless of how the memory layout is changed, the order of elements returned by a[tensor_view](data.html#structmigraphx_1_1internal_1_1tensor__view)will be unchanged.`permutation`

: List with how to rearrange the data buffer of the input instruction. This permutation is the transpose from the order in the tensor to the order in memory.

-
struct leaky_relu : public migraphx::internal::op::unary<
[leaky_relu](#_CPPv4N8migraphx2op10leaky_reluE)>[#](#_CPPv4N8migraphx2op10leaky_reluE) *#include <migraphx/op/leaky_relu.hpp>*

-
struct load
[#](#_CPPv4N8migraphx2op4loadE) *#include <migraphx/op/load.hpp>*

-
struct logical_and : public migraphx::internal::op::binary<
[logical_and](#_CPPv4N8migraphx2op11logical_andE)>[#](#_CPPv4N8migraphx2op11logical_andE) *#include <migraphx/op/logical_and.hpp>*

-
struct logical_or : public migraphx::internal::op::binary<
[logical_or](#_CPPv4N8migraphx2op10logical_orE)>[#](#_CPPv4N8migraphx2op10logical_orE) *#include <migraphx/op/logical_or.hpp>*

-
struct logical_xor : public migraphx::internal::op::binary<
[logical_xor](#_CPPv4N8migraphx2op11logical_xorE)>[#](#_CPPv4N8migraphx2op11logical_xorE) *#include <migraphx/op/logical_xor.hpp>*

-
struct logsoftmax
[#](#_CPPv4N8migraphx2op10logsoftmaxE) *#include <migraphx/op/logsoftmax.hpp>*

-
struct loop
[#](#_CPPv4N8migraphx2op4loopE) *#include <migraphx/op/loop.hpp>*-
struct ref_loop
[#](#_CPPv4N8migraphx2op4loop8ref_loopE) *#include <migraphx/op/loop.hpp>*Public Functions

-
inline void append(const std::vector<
[argument](../reference/MIGraphX-cpp.html#_CPPv4N8migraphx8argumentE)> &iter_state, const std::vector<[argument](../reference/MIGraphX-cpp.html#_CPPv4N8migraphx8argumentE)> &concatenated_outputs, const std::vector<int64_t> &scan_output_dirs, int64_t curr_iter, int64_t num_iters) const[#](#_CPPv4NK8migraphx2op4loop8ref_loop6appendERKNSt6vectorI8argumentEERKNSt6vectorI8argumentEERKNSt6vectorI7int64_tEE7int64_t7int64_t)

-
inline std::unordered_map<std::string, int> get_output_params(const module&) const
[#](#_CPPv4NK8migraphx2op4loop8ref_loop17get_output_paramsERK6module)

-
inline void append(const std::vector<

-
struct ref_loop

-
struct lowest
[#](#_CPPv4N8migraphx2op6lowestE) *#include <migraphx/op/reduce_op.hpp>*

-
struct lrn
[#](#_CPPv4N8migraphx2op3lrnE) *#include <migraphx/op/lrn.hpp>*

-
struct lstm
[#](#_CPPv4N8migraphx2op4lstmE) *#include <migraphx/op/lstm.hpp>*

-
struct multibroadcast
[#](#_CPPv4N8migraphx2op14multibroadcastE) *#include <migraphx/op/multibroadcast.hpp>*Broadcast multiple dimensions between two tensors. Two versions of this operator: 1 input and 2+ inputs. One input version uses output_lens attribute and broadcasts to it. 2+ inputs version broadcasts first input to the common shape at evaluation time.


-
struct multinomial
[#](#_CPPv4N8migraphx2op11multinomialE) *#include <migraphx/op/multinomial.hpp>*

-
struct nearbyint : public migraphx::internal::op::unary<
[nearbyint](#_CPPv4N8migraphx2op9nearbyintE)>[#](#_CPPv4N8migraphx2op9nearbyintE) *#include <migraphx/op/nearbyint.hpp>*

-
struct nonmaxsuppression
[#](#_CPPv4N8migraphx2op17nonmaxsuppressionE) *#include <migraphx/op/nonmaxsuppression.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op17nonmaxsuppression4nameEv)

-
template<class T>

inline std::vector<std::pair<double, int64_t>> filter_boxes_by_score([T](#_CPPv4I0ENK8migraphx2op17nonmaxsuppression21filter_boxes_by_scoreENSt6vectorINSt4pairId7int64_tEEEE1TNSt6size_tEd)scores_start, std::size_t num_boxes, double score_threshold) const[#](#_CPPv4I0ENK8migraphx2op17nonmaxsuppression21filter_boxes_by_scoreENSt6vectorINSt4pairId7int64_tEEEE1TNSt6size_tEd)

-
inline std::string name() const

-
struct nonzero
[#](#_CPPv4N8migraphx2op7nonzeroE) *#include <migraphx/op/nonzero.hpp>*

-
struct one
[#](#_CPPv4N8migraphx2op3oneE) *#include <migraphx/op/reduce_op.hpp>*

-
struct onehot
[#](#_CPPv4N8migraphx2op6onehotE) *#include <migraphx/op/onehot.hpp>*Produces a one-hot tensor. Called with

`axis`

attribute that defaults to the last output axis Constant depth:`onehot(indices, values), depth attribute must be set; Variable depth:`

onehot(indices, depth, values)`;`

indicies`as a N rank tensor of indices where value is`

on_value

depth`scalar with the number of classes for the one-hot dimension`

values[off_value, on_value]

axis`which axis to add the one-hot dimension to For axis = 0 and rank(indices) = 2: output is A[indicies[j, k], j, k] = on_value; A[i, j, k] = off_value otherwise Can be simplified to other operators when`

indices`has a static shape and`

depth` is constant at compile-time.

-
template<class Derived>

struct op_name[#](#_CPPv4I0EN8migraphx2op7op_nameE) *#include <migraphx/op/name.hpp>*Create name from class.

Subclassed by

[migraphx::internal::op::binary< add >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< bitwise_and >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< div >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< equal >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< fmod >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< greater >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< less >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< logical_and >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< logical_or >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< logical_xor >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< max >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< min >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< mod >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< mul >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< pow >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< prelu >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< sqdiff >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::binary< sub >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::prefix_scan_op< prefix_scan_sum >](#structmigraphx_1_1internal_1_1op_1_1prefix__scan__op),[migraphx::internal::op::reduce_op< reduce_all >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::reduce_op< reduce_any >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::reduce_op< reduce_max >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::reduce_op< reduce_mean >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::reduce_op< reduce_min >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::reduce_op< reduce_prod >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::reduce_op< reduce_sum >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::scatter_op< scatter_add >](#structmigraphx_1_1internal_1_1op_1_1scatter__op),[migraphx::internal::op::scatter_op< scatter_max >](#structmigraphx_1_1internal_1_1op_1_1scatter__op),[migraphx::internal::op::scatter_op< scatter_min >](#structmigraphx_1_1internal_1_1op_1_1scatter__op),[migraphx::internal::op::scatter_op< scatter_mul >](#structmigraphx_1_1internal_1_1op_1_1scatter__op),[migraphx::internal::op::scatter_op< scatter_none >](#structmigraphx_1_1internal_1_1op_1_1scatter__op),[migraphx::internal::op::scatternd_op< scatternd_add >](#structmigraphx_1_1internal_1_1op_1_1scatternd__op),[migraphx::internal::op::scatternd_op< scatternd_max >](#structmigraphx_1_1internal_1_1op_1_1scatternd__op),[migraphx::internal::op::scatternd_op< scatternd_min >](#structmigraphx_1_1internal_1_1op_1_1scatternd__op),[migraphx::internal::op::scatternd_op< scatternd_mul >](#structmigraphx_1_1internal_1_1op_1_1scatternd__op),[migraphx::internal::op::scatternd_op< scatternd_none >](#structmigraphx_1_1internal_1_1op_1_1scatternd__op),[migraphx::internal::op::unary< abs >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< acos >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< acosh >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< asin >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< asinh >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< atan >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< atanh >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< bit_cast >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< ceil >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< convert >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< cos >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< cosh >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< elu >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< erf >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< exp >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< floor >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< isinf >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< isnan >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< layout >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< leaky_relu >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< log >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< log2 >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< nearbyint >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< neg >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< recip >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< relu >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< rsqrt >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< sigmoid >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< sign >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< sin >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< sinh >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< sqrt >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< tan >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< tanh >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::unary< unary_not >](#structmigraphx_1_1internal_1_1op_1_1unary),[migraphx::internal::op::binary< Derived >](#structmigraphx_1_1internal_1_1op_1_1binary),[migraphx::internal::op::prefix_scan_op< Derived >](#structmigraphx_1_1internal_1_1op_1_1prefix__scan__op),[migraphx::internal::op::reduce_op< Derived >](#structmigraphx_1_1internal_1_1op_1_1reduce__op),[migraphx::internal::op::scatter_op< Derived >](#structmigraphx_1_1internal_1_1op_1_1scatter__op),[migraphx::internal::op::scatternd_op< Derived >](#structmigraphx_1_1internal_1_1op_1_1scatternd__op),[migraphx::internal::op::unary< Derived >](#structmigraphx_1_1internal_1_1op_1_1unary)

-
struct outline
[#](#_CPPv4N8migraphx2op7outlineE) *#include <migraphx/op/outline.hpp>*

-
struct pack_fp4
[#](#_CPPv4N8migraphx2op8pack_fp4E) *#include <migraphx/op/pack_fp4.hpp>*Packs fastest dimension of tensor into fp4x2_type such that the output dimensions are [x_0, …, x_pack/2, …]


-
struct pack_int4
[#](#_CPPv4N8migraphx2op9pack_int4E) *#include <migraphx/op/pack_int4.hpp>*

-
struct pad
[#](#_CPPv4N8migraphx2op3padE) *#include <migraphx/op/pad.hpp>*Public Types


-
struct pointwise
[#](#_CPPv4N8migraphx2op9pointwiseE) *#include <migraphx/op/pointwise.hpp>*

-
struct pooling
[#](#_CPPv4N8migraphx2op7poolingE) *#include <migraphx/op/pooling.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op7pooling4nameEv)

-
inline void check_attribute_size() const
[#](#_CPPv4NK8migraphx2op7pooling20check_attribute_sizeEv)

-
inline size_t kdims() const
[#](#_CPPv4NK8migraphx2op7pooling5kdimsEv)

-
inline std::size_t dilate_dim(std::size_t dim, std::size_t dilation) const
[#](#_CPPv4NK8migraphx2op7pooling10dilate_dimENSt6size_tENSt6size_tE)

-
inline std::vector<std::size_t> calc_spatial_dim_out(const std::vector<std::size_t> &input_lens, std::size_t kdims) const
[#](#_CPPv4NK8migraphx2op7pooling20calc_spatial_dim_outERKNSt6vectorINSt6size_tEEENSt6size_tE)

Public Members

-
[pooling_mode](#_CPPv4N8migraphx2op12pooling_modeE)mode = {[pooling_mode](#_CPPv4N8migraphx2op12pooling_modeE)::[average](#_CPPv4N8migraphx2op12pooling_mode7averageE)}[#](#_CPPv4N8migraphx2op7pooling4modeE)

-
std::vector<std::size_t> padding = {0, 0}
[#](#_CPPv4N8migraphx2op7pooling7paddingE)

-
std::vector<std::size_t> stride = {1, 1}
[#](#_CPPv4N8migraphx2op7pooling6strideE)

-
std::vector<std::size_t> lengths = {1, 1}
[#](#_CPPv4N8migraphx2op7pooling7lengthsE)

-
std::vector<std::size_t> dilations = {1, 1}
[#](#_CPPv4N8migraphx2op7pooling9dilationsE)

-
bool ceil_mode = false
[#](#_CPPv4N8migraphx2op7pooling9ceil_modeE)

-
int lp_order = 2
[#](#_CPPv4N8migraphx2op7pooling8lp_orderE)

-
[padding_mode_t](#_CPPv4N8migraphx2op14padding_mode_tE)padding_mode =[padding_mode_t](#_CPPv4N8migraphx2op14padding_mode_tE)::[default_](#_CPPv4N8migraphx2op14padding_mode_t8default_E)[#](#_CPPv4N8migraphx2op7pooling12padding_modeE)

-
bool dyn_global = false
[#](#_CPPv4N8migraphx2op7pooling10dyn_globalE)

-
bool count_include_pad = false
[#](#_CPPv4N8migraphx2op7pooling17count_include_padE)

-
struct avg_pool
[#](#_CPPv4N8migraphx2op7pooling8avg_poolE) *#include <migraphx/op/pooling.hpp>*

-
struct lpnorm_pool
[#](#_CPPv4N8migraphx2op7pooling11lpnorm_poolE) *#include <migraphx/op/pooling.hpp>*

-
struct max_pool
[#](#_CPPv4N8migraphx2op7pooling8max_poolE) *#include <migraphx/op/pooling.hpp>*

-
inline std::string name() const

-
template<class Derived>

struct prefix_scan_op : public migraphx::internal::op::op_name<[Derived](#_CPPv4I0EN8migraphx2op14prefix_scan_opE)>[#](#_CPPv4I0EN8migraphx2op14prefix_scan_opE) *#include <migraphx/op/prefix_scan_op.hpp>*Parent struct for prefix scan operations. A prefix scan is equivalent to the C++ std::exclusive_scan or std::inclusive_scan. Given a list of numbers, a prefix scan sum op returns an equal size list of running totals of the values. Other operations besides addition can be supported by their own child ops.


-
struct prefix_scan_sum : public migraphx::internal::op::prefix_scan_op<
[prefix_scan_sum](#_CPPv4N8migraphx2op15prefix_scan_sumE)>[#](#_CPPv4N8migraphx2op15prefix_scan_sumE) *#include <migraphx/op/prefix_scan_sum.hpp>*

-
struct quant_convolution
[#](#_CPPv4N8migraphx2op17quant_convolutionE) *#include <migraphx/op/quant_convolution.hpp>*2 input version: Standard quantized convolution operation inputs = {A_mat, W_mat}

4 input version: Quantized convolution with two sets of scales for A and W matricies. inputs = {A_mat, W_mat, scale_A, scale_W}

Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op17quant_convolution4nameEv)

-
inline void check_attribute_size() const
[#](#_CPPv4NK8migraphx2op17quant_convolution20check_attribute_sizeEv)

-
inline size_t kdims() const
[#](#_CPPv4NK8migraphx2op17quant_convolution5kdimsEv)

-
inline std::string name() const

-
struct quant_dot
[#](#_CPPv4N8migraphx2op9quant_dotE) *#include <migraphx/op/quant_dot.hpp>*2 input version: Standard quantized GEMM operation inputs = {A_mat, B_mat}

4 input version: Quantized GEMM with two sets of scales for A and B matricies. inputs = {A_mat, B_mat, scale_A, scale_B}


-
struct quantizelinear
[#](#_CPPv4N8migraphx2op14quantizelinearE) *#include <migraphx/op/quantizelinear.hpp>*

-
struct random_seed
[#](#_CPPv4N8migraphx2op11random_seedE) *#include <migraphx/op/random_seed.hpp>*Generates a random seed for the use of random number generators. Generating the seed at runtime guarantees there will be a different random sequence on every execution. This operation has no inputs or attributes, and outputs an unsigned integer tensor with a single value.


-
struct random_uniform
[#](#_CPPv4N8migraphx2op14random_uniformE) *#include <migraphx/op/random_uniform.hpp>*[random_uniform](#structmigraphx_1_1internal_1_1op_1_1random__uniform)populates the passed shape with random numbers, in a uniform distribution. Range for floating-point data types is (0, 1); for integer types it is [0, <max value for the type>]

-
struct reduce_all : public migraphx::internal::op::reduce_op<
[reduce_all](#_CPPv4N8migraphx2op10reduce_allE)>[#](#_CPPv4N8migraphx2op10reduce_allE) *#include <migraphx/op/reduce_all.hpp>*

-
struct reduce_any : public migraphx::internal::op::reduce_op<
[reduce_any](#_CPPv4N8migraphx2op10reduce_anyE)>[#](#_CPPv4N8migraphx2op10reduce_anyE) *#include <migraphx/op/reduce_any.hpp>*

-
struct reduce_max : public migraphx::internal::op::reduce_op<
[reduce_max](#_CPPv4N8migraphx2op10reduce_maxE)>[#](#_CPPv4N8migraphx2op10reduce_maxE) *#include <migraphx/op/reduce_max.hpp>*

-
struct reduce_mean : public migraphx::internal::op::reduce_op<
[reduce_mean](#_CPPv4N8migraphx2op11reduce_meanE)>[#](#_CPPv4N8migraphx2op11reduce_meanE) *#include <migraphx/op/reduce_mean.hpp>*

-
struct reduce_min : public migraphx::internal::op::reduce_op<
[reduce_min](#_CPPv4N8migraphx2op10reduce_minE)>[#](#_CPPv4N8migraphx2op10reduce_minE) *#include <migraphx/op/reduce_min.hpp>*

-
template<class Derived>

struct reduce_op : public migraphx::internal::op::op_name<[Derived](#_CPPv4I0EN8migraphx2op9reduce_opE)>[#](#_CPPv4I0EN8migraphx2op9reduce_opE) *#include <migraphx/op/reduce_op.hpp>*Public Functions

-
inline
[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)collapse_reduced_axes(const[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&original_shape, const std::vector<int64_t> &reduce_axes) const[#](#_CPPv4NK8migraphx2op9reduce_op21collapse_reduced_axesERK5shapeRKNSt6vectorI7int64_tEE)

-
inline
[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)normalize_compute_shape(std::vector<[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)> inputs) const[#](#_CPPv4NK8migraphx2op9reduce_op23normalize_compute_shapeENSt6vectorI5shapeEE) returns a shape in which the axis or axes named for reduction by this op are set, to size 1.

- Parameters:
**inputs**– list of input shapes- Returns:
shape



-
template<class T>

inline void tune_dims(const std::vector<int64_t> &tuned_axes, const std::vector<[T](#_CPPv4I0ENK8migraphx2op9reduce_op9tune_dimsEvRKNSt6vectorI7int64_tEERKNSt6vectorI1TEERNSt6vectorI1TEE)> &in_lens, std::vector<[T](#_CPPv4I0ENK8migraphx2op9reduce_op9tune_dimsEvRKNSt6vectorI7int64_tEERKNSt6vectorI1TEERNSt6vectorI1TEE)> &out_lens) const[#](#_CPPv4I0ENK8migraphx2op9reduce_op9tune_dimsEvRKNSt6vectorI7int64_tEERKNSt6vectorI1TEERNSt6vectorI1TEE)

-
template<class T>

inline void reduce(const tensor_view<[T](#_CPPv4I0ENK8migraphx2op9reduce_op6reduceEvRK11tensor_viewI1TERK5shapeRKNSt6vectorI7int64_tEERKNSt6vectorINSt6size_tEEER11tensor_viewI1TE)> &input, const[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&batch_shape, const std::vector<int64_t> &tuned_axes, const std::vector<std::size_t> &out_idx, tensor_view<[T](#_CPPv4I0ENK8migraphx2op9reduce_op6reduceEvRK11tensor_viewI1TERK5shapeRKNSt6vectorI7int64_tEERKNSt6vectorINSt6size_tEEER11tensor_viewI1TE)> &output) const[#](#_CPPv4I0ENK8migraphx2op9reduce_op6reduceEvRK11tensor_viewI1TERK5shapeRKNSt6vectorI7int64_tEERKNSt6vectorINSt6size_tEEER11tensor_viewI1TE)

-
inline
[argument](../reference/MIGraphX-cpp.html#_CPPv4N8migraphx8argumentE)reduce(const[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&computed_shape, const std::vector<int64_t> &reduce_axes,[argument](../reference/MIGraphX-cpp.html#_CPPv4N8migraphx8argumentE)&data_arg) const[#](#_CPPv4NK8migraphx2op9reduce_op6reduceERK5shapeRKNSt6vectorI7int64_tEER8argument)

-
inline auto init() const
[#](#_CPPv4NK8migraphx2op9reduce_op4initEv)

-
inline auto input() const
[#](#_CPPv4NK8migraphx2op9reduce_op5inputEv)

-
inline reduce_op()
[#](#_CPPv4N8migraphx2op9reduce_op9reduce_opEv)

-
inline reduce_op(std::vector<int64_t> ax)
[#](#_CPPv4N8migraphx2op9reduce_op9reduce_opENSt6vectorI7int64_tEE)

-
inline

-
struct reduce_prod : public migraphx::internal::op::reduce_op<
[reduce_prod](#_CPPv4N8migraphx2op11reduce_prodE)>[#](#_CPPv4N8migraphx2op11reduce_prodE) *#include <migraphx/op/reduce_prod.hpp>*

-
struct reduce_sum : public migraphx::internal::op::reduce_op<
[reduce_sum](#_CPPv4N8migraphx2op10reduce_sumE)>[#](#_CPPv4N8migraphx2op10reduce_sumE) *#include <migraphx/op/reduce_sum.hpp>*

-
struct reshape
[#](#_CPPv4N8migraphx2op7reshapeE) *#include <migraphx/op/reshape.hpp>*1 input version: reshape(input_data) this.dims = output_dims Makes a copy of input_data to the output shape.

2 input version: reshape(input_data, output_buffer) this.dims = unset Copies input_data to output_buffer; output_buffer already has the output shape. This version will not fail gracefully if the input shape and output_buffer shape are incompatible. There’s a throw that will catch when the number of elements do not match at runtime. This version should only be used for dynamic reshapes (output dimensions only known at runtime). If output_buffer has a static shape during compile/parse, you can use the 1 input version.


-
struct reshape_lazy
[#](#_CPPv4N8migraphx2op12reshape_lazyE) *#include <migraphx/op/reshape_lazy.hpp>*Public Static Functions

-
template<class Iterator>

static inline auto compute_end_dim([Iterator](#_CPPv4I0EN8migraphx2op12reshape_lazy15compute_end_dimEDa8Iterator8IteratorNSt6size_tE)start,[Iterator](#_CPPv4I0EN8migraphx2op12reshape_lazy15compute_end_dimEDa8Iterator8IteratorNSt6size_tE)last, std::size_t dim)[#](#_CPPv4I0EN8migraphx2op12reshape_lazy15compute_end_dimEDa8Iterator8IteratorNSt6size_tE)

-
template<class OptionalPair>

static inline[OptionalPair](#_CPPv4I0EN8migraphx2op12reshape_lazy15try_merge_pairsE12OptionalPair12OptionalPair12OptionalPair)try_merge_pairs([OptionalPair](#_CPPv4I0EN8migraphx2op12reshape_lazy15try_merge_pairsE12OptionalPair12OptionalPair12OptionalPair)p2,[OptionalPair](#_CPPv4I0EN8migraphx2op12reshape_lazy15try_merge_pairsE12OptionalPair12OptionalPair12OptionalPair)p1)[#](#_CPPv4I0EN8migraphx2op12reshape_lazy15try_merge_pairsE12OptionalPair12OptionalPair12OptionalPair)

-
template<class DimIterator, class StrideIterator>

static inline optional<std::size_t> merge_strides([DimIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy13merge_stridesE8optionalINSt6size_tEE11DimIterator11DimIterator14StrideIterator14StrideIterator)dim_start,[DimIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy13merge_stridesE8optionalINSt6size_tEE11DimIterator11DimIterator14StrideIterator14StrideIterator)dim_last,[StrideIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy13merge_stridesE8optionalINSt6size_tEE11DimIterator11DimIterator14StrideIterator14StrideIterator)stride_start,[StrideIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy13merge_stridesE8optionalINSt6size_tEE11DimIterator11DimIterator14StrideIterator14StrideIterator)stride_last)[#](#_CPPv4I00EN8migraphx2op12reshape_lazy13merge_stridesE8optionalINSt6size_tEE11DimIterator11DimIterator14StrideIterator14StrideIterator)

-
template<class DimIterator, class StrideIterator>

static inline auto can_strides_merge([DimIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy17can_strides_mergeEDa11DimIterator11DimIterator14StrideIterator14StrideIterator)dim_start,[DimIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy17can_strides_mergeEDa11DimIterator11DimIterator14StrideIterator14StrideIterator)dim_last,[StrideIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy17can_strides_mergeEDa11DimIterator11DimIterator14StrideIterator14StrideIterator)stride_start,[StrideIterator](#_CPPv4I00EN8migraphx2op12reshape_lazy17can_strides_mergeEDa11DimIterator11DimIterator14StrideIterator14StrideIterator)stride_last)[#](#_CPPv4I00EN8migraphx2op12reshape_lazy17can_strides_mergeEDa11DimIterator11DimIterator14StrideIterator14StrideIterator)

-
template<class Iterator>

-
struct resize
[#](#_CPPv4N8migraphx2op6resizeE) *#include <migraphx/op/resize.hpp>*The Resize operation mirrors the Onnx Resize operation with some differences. Currently, only Nearest mode is supported. “Axes” and “ROI” attributes not recognized.

Accepts either one or two runtime inputs. Input 0 - data to be resized Input 1 - sizes or scales. If data type is uint64, Input 1 is interpreted as output sizes; otherwise as scaling factors.

If the second input is not used, either a “sizes” or “scales” attribute must be provided.


-
struct reverse
[#](#_CPPv4N8migraphx2op7reverseE) *#include <migraphx/op/reverse.hpp>*

-
struct rnn
[#](#_CPPv4N8migraphx2op3rnnE) *#include <migraphx/op/rnn.hpp>*

-
struct rnn_last_cell_output
[#](#_CPPv4N8migraphx2op20rnn_last_cell_outputE) *#include <migraphx/op/rnn_last_cell_output.hpp>*

-
struct rnn_last_hs_output
[#](#_CPPv4N8migraphx2op18rnn_last_hs_outputE) *#include <migraphx/op/rnn_last_hs_output.hpp>*

-
struct rnn_var_sl_last_output
[#](#_CPPv4N8migraphx2op22rnn_var_sl_last_outputE) *#include <migraphx/op/rnn_var_sl_last_output.hpp>*

-
struct rnn_var_sl_shift_output
[#](#_CPPv4N8migraphx2op23rnn_var_sl_shift_outputE) *#include <migraphx/op/rnn_variable_seq_lens.hpp>*

-
struct rnn_var_sl_shift_sequence
[#](#_CPPv4N8migraphx2op25rnn_var_sl_shift_sequenceE) *#include <migraphx/op/rnn_variable_seq_lens.hpp>*

-
struct roialign
[#](#_CPPv4N8migraphx2op8roialignE) *#include <migraphx/op/roialign.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op8roialign4nameEv)

-
inline auto calc_pos_weight(const std::array<std::size_t, 2> &dims, const
[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&comp_s, const std::array<float, 2> &roi_start, const std::array<float, 2> &bin_size, const std::array<std::size_t, 2> &bin_grid_size) const[#](#_CPPv4NK8migraphx2op8roialign15calc_pos_weightERKNSt5arrayINSt6size_tEXL2EEEERK5shapeRKNSt5arrayIfXL2EEEERKNSt5arrayIfXL2EEEERKNSt5arrayINSt6size_tEXL2EEEE)

-
template<class T, class Op>

inline std::tuple<double, int64_t> calc_pooling(const[T](#_CPPv4I00ENK8migraphx2op8roialign12calc_poolingENSt5tupleId7int64_tEERK1TRKNSt5arrayINSt6size_tEXL2EEEERKNSt6vectorI10pos_weightEE7int64_t2Op)&data, const std::array<std::size_t, 2> &bin_grid_size, const std::vector<[pos_weight](#_CPPv4N8migraphx2op8roialign10pos_weightE)> &pos_weights, int64_t index,[Op](#_CPPv4I00ENK8migraphx2op8roialign12calc_poolingENSt5tupleId7int64_tEERK1TRKNSt5arrayINSt6size_tEXL2EEEERKNSt6vectorI10pos_weightEE7int64_t2Op)op) const[#](#_CPPv4I00ENK8migraphx2op8roialign12calc_poolingENSt5tupleId7int64_tEERK1TRKNSt5arrayINSt6size_tEXL2EEEERKNSt6vectorI10pos_weightEE7int64_t2Op)

Public Members

-
std::string coord_trans_mode = "half_pixel"
[#](#_CPPv4N8migraphx2op8roialign16coord_trans_modeE)

-
[pooling_mode](#_CPPv4N8migraphx2op12pooling_modeE)mode = {[pooling_mode](#_CPPv4N8migraphx2op12pooling_modeE)::[average](#_CPPv4N8migraphx2op12pooling_mode7averageE)}[#](#_CPPv4N8migraphx2op8roialign4modeE)

-
int64_t output_height = 1
[#](#_CPPv4N8migraphx2op8roialign13output_heightE)

-
int64_t output_width = 1
[#](#_CPPv4N8migraphx2op8roialign12output_widthE)

-
int64_t sampling_ratio = 0
[#](#_CPPv4N8migraphx2op8roialign14sampling_ratioE)

-
float spatial_scale = 1.0f
[#](#_CPPv4N8migraphx2op8roialign13spatial_scaleE)

-
struct avg_pool
[#](#_CPPv4N8migraphx2op8roialign8avg_poolE) *#include <migraphx/op/roialign.hpp>*

-
struct max_pool
[#](#_CPPv4N8migraphx2op8roialign8max_poolE) *#include <migraphx/op/roialign.hpp>*

-
struct pos_weight
[#](#_CPPv4N8migraphx2op8roialign10pos_weightE) *#include <migraphx/op/roialign.hpp>*

-
inline std::string name() const

-
struct run_on_target
[#](#_CPPv4N8migraphx2op13run_on_targetE) *#include <migraphx/op/run_on_target.hpp>*

-
struct scalar
[#](#_CPPv4N8migraphx2op6scalarE) *#include <migraphx/op/scalar.hpp>*

-
struct scan_slice : public migraphx::internal::op::op_name<
[scan_slice](#_CPPv4N8migraphx2op10scan_sliceE)>[#](#_CPPv4N8migraphx2op10scan_sliceE) *#include <migraphx/op/scan_slice.hpp>*Public Functions


-
struct scatter_add : public migraphx::internal::op::scatter_op<
[scatter_add](#_CPPv4N8migraphx2op11scatter_addE)>[#](#_CPPv4N8migraphx2op11scatter_addE) *#include <migraphx/op/scatter_add.hpp>*

-
struct scatter_max : public migraphx::internal::op::scatter_op<
[scatter_max](#_CPPv4N8migraphx2op11scatter_maxE)>[#](#_CPPv4N8migraphx2op11scatter_maxE) *#include <migraphx/op/scatter_max.hpp>*

-
struct scatter_min : public migraphx::internal::op::scatter_op<
[scatter_min](#_CPPv4N8migraphx2op11scatter_minE)>[#](#_CPPv4N8migraphx2op11scatter_minE) *#include <migraphx/op/scatter_min.hpp>*

-
struct scatter_mul : public migraphx::internal::op::scatter_op<
[scatter_mul](#_CPPv4N8migraphx2op11scatter_mulE)>[#](#_CPPv4N8migraphx2op11scatter_mulE) *#include <migraphx/op/scatter_mul.hpp>*

-
struct scatter_none : public migraphx::internal::op::scatter_op<
[scatter_none](#_CPPv4N8migraphx2op12scatter_noneE)>[#](#_CPPv4N8migraphx2op12scatter_noneE) *#include <migraphx/op/scatter_none.hpp>*

-
template<typename Derived>

struct scatter_op : public migraphx::internal::op::op_name<[Derived](#_CPPv4I0EN8migraphx2op10scatter_opE)>[#](#_CPPv4I0EN8migraphx2op10scatter_opE) *#include <migraphx/op/scatter_op.hpp>*

-
struct scatternd_add : public migraphx::internal::op::scatternd_op<
[scatternd_add](#_CPPv4N8migraphx2op13scatternd_addE)>[#](#_CPPv4N8migraphx2op13scatternd_addE) *#include <migraphx/op/scatternd_add.hpp>*

-
struct scatternd_max : public migraphx::internal::op::scatternd_op<
[scatternd_max](#_CPPv4N8migraphx2op13scatternd_maxE)>[#](#_CPPv4N8migraphx2op13scatternd_maxE) *#include <migraphx/op/scatternd_max.hpp>*

-
struct scatternd_min : public migraphx::internal::op::scatternd_op<
[scatternd_min](#_CPPv4N8migraphx2op13scatternd_minE)>[#](#_CPPv4N8migraphx2op13scatternd_minE) *#include <migraphx/op/scatternd_min.hpp>*

-
struct scatternd_mul : public migraphx::internal::op::scatternd_op<
[scatternd_mul](#_CPPv4N8migraphx2op13scatternd_mulE)>[#](#_CPPv4N8migraphx2op13scatternd_mulE) *#include <migraphx/op/scatternd_mul.hpp>*

-
struct scatternd_none : public migraphx::internal::op::scatternd_op<
[scatternd_none](#_CPPv4N8migraphx2op14scatternd_noneE)>[#](#_CPPv4N8migraphx2op14scatternd_noneE) *#include <migraphx/op/scatternd_none.hpp>*

-
template<class Derived>

struct scatternd_op : public migraphx::internal::op::op_name<[Derived](#_CPPv4I0EN8migraphx2op12scatternd_opE)>[#](#_CPPv4I0EN8migraphx2op12scatternd_opE) *#include <migraphx/op/scatternd_op.hpp>*N-dimensional Scatter operations. This struct is parent class to ops which differ in what formula is used to reduce (combine old and new values of) the scattered value. It was originally based on Onnx ScatterND operation (see

[onnx/onnx](https://github.com/onnx/onnx/blob/main/docs/Operators.md#ScatterND)) and is also similar to Numpy numpy.add.at().- Template Parameters:
**Derived**– a template parameter in the CRTP inheritance idiom, represents one of the child operations.


-
struct select_module
[#](#_CPPv4N8migraphx2op13select_moduleE) *#include <migraphx/op/select_module.hpp>*Public Functions

-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op13select_module4nameEv)

-
inline std::vector<std::string> get_input_parameter_names(module_ref mod) const
[#](#_CPPv4NK8migraphx2op13select_module25get_input_parameter_namesE10module_ref)

-
inline std::vector<std::string> get_output_parameter_names(module_ref mod) const
[#](#_CPPv4NK8migraphx2op13select_module26get_output_parameter_namesE10module_ref)

-
inline std::string name() const

-
struct slice
[#](#_CPPv4N8migraphx2op5sliceE) *#include <migraphx/op/slice.hpp>*Slice operator that accepts variable axes, starts and ends. All of

`starts`

,`ends`

, and`axes`

must be supplied by either their attribute or an input (but not both).Valid calls: slice(input); axes, starts, ends set slice(input, starts); axes, ends set slice(input, ends); starts, axes set slice(input, axes); starts, ends set slice(input, starts, ends); axes set slice(input, starts, axes); ends set slice(input, ends, axes); starts set slice(input, start, ends, axes); none set

Attributes: axes: constant axes to slice over (optional) starts: constant slice starting indices (optional) ends: constant slice ending indices (optional)

Parameters: data: the input tensor to slice (dynamic or static shape) input_starts: starting indices of slice (optional, static shape) input_ends: ending indices of slice (optional, static shape) input_axes: axes to slice over (optional, static shape)

Public Functions

-
inline
[value](https://rocm.docs.amd.com/projects/hipRaft/en/latest/reference/cpp_api/mdspan_representation.html#_CPPv45value)attributes() const[#](#_CPPv4NK8migraphx2op5slice10attributesEv) Ensure that attribute axes is within limits. Will attempt to normalize starts and ends; but will use the dynamic_dimension.max values for dynamic shapes. This makes it so you have to renormalize for non-fixed dynamic_dimensions.


-
inline std::string name() const
[#](#_CPPv4NK8migraphx2op5slice4nameEv)

-
template<class A, class B>

inline std::vector<std::size_t> lens_calc(const std::vector<std::size_t> &lengths,[A](#_CPPv4I00ENK8migraphx2op5slice9lens_calcENSt6vectorINSt6size_tEEERKNSt6vectorINSt6size_tEEE1A1A1B)in_starts,[A](#_CPPv4I00ENK8migraphx2op5slice9lens_calcENSt6vectorINSt6size_tEEERKNSt6vectorINSt6size_tEEE1A1A1B)in_ends,[B](#_CPPv4I00ENK8migraphx2op5slice9lens_calcENSt6vectorINSt6size_tEEERKNSt6vectorINSt6size_tEEE1A1A1B)in_axes) const[#](#_CPPv4I00ENK8migraphx2op5slice9lens_calcENSt6vectorINSt6size_tEEERKNSt6vectorINSt6size_tEEE1A1A1B) Computes the slice output shape dimensions for given starts, ends,and axes. Templated to also handle tensor views. Possibly different type between [in_starts, in_ends] and [in_axes] if in_axes is this object’s axes attribute. Assumes in_starts and in_ends are normalized; in_axes are valid.


-
inline std::array<bool, 3> get_set_attributes() const
[#](#_CPPv4NK8migraphx2op5slice18get_set_attributesEv) Get the attributes that are non-empty.


-
inline
[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)compute_two_or_more(std::vector<[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)> inputs) const[#](#_CPPv4NK8migraphx2op5slice19compute_two_or_moreENSt6vectorI5shapeEE) Helper function for

[normalize_compute_shape()](#structmigraphx_1_1internal_1_1op_1_1slice_1a815c0d81ce7234d61b4a84c2c2755c4b)

-
inline auto compute_offset(const
[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&s) const[#](#_CPPv4NK8migraphx2op5slice14compute_offsetERK5shape) Calculates the starting offset for the sliced tensor. Used in compute when only data input and all other information are in the attributes.

- Parameters:
**s**– static input shape


-
template<class T>

inline auto compute_offset(const[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)&s, const[T](#_CPPv4I0ENK8migraphx2op5slice14compute_offsetEDaRK5shapeRK1TRK1T)&input_starts, const[T](#_CPPv4I0ENK8migraphx2op5slice14compute_offsetEDaRK5shapeRK1TRK1T)&ax_vec) const[#](#_CPPv4I0ENK8migraphx2op5slice14compute_offsetEDaRK5shapeRK1TRK1T) Calculates the starting offset for the sliced tensor (for aliasing). Used for 2-4 inputs to `slice.

- Parameters:
**s**– static input shape**input_starts**– starting indices of slice**ax_vec**– axes to slice on



-
inline std::unordered_map<std::string, std::vector<int64_t>> normalize_starts_ends_axes(
[shape](../reference/MIGraphX-cpp.html#_CPPv4I00EN8migraphx5shapeE)input_shape, const optional<std::vector<int64_t>> &input_starts, const optional<std::vector<int64_t>> &input_ends, const optional<std::vector<int64_t>> &input_axes) const[#](#_CPPv4NK8migraphx2op5slice26normalize_starts_ends_axesE5shapeRK8optionalINSt6vectorI7int64_tEEERK8optionalINSt6vectorI7int64_tEEERK8optionalINSt6vectorI7int64_tEEE) If given, normalize the inputs. Otherwise get from operator attributes. Return the values in a map.

Parameters input_shape: static shape of the input input_starts: optional input_ends: optional input_ends: optional


Public Members

-
std::vector<int64_t> axes = {}
[#](#_CPPv4N8migraphx2op5slice4axesE)

-
std::vector<int64_t> starts = {}
[#](#_CPPv4N8migraphx2op5slice6startsE)

-
std::vector<int64_t> ends = {}
[#](#_CPPv4N8migraphx2op5slice4endsE)

Public Static Attributes

-
static constexpr std::array<bool, 3> all_set = {true, true, true}
[#](#_CPPv4N8migraphx2op5slice7all_setE) Named arrays for the set attribute possibilities.


-
static constexpr std::array<bool, 3> ends_axes = {false, true, true}
[#](#_CPPv4N8migraphx2op5slice9ends_axesE)

-
static constexpr std::array<bool, 3> starts_axes = {true, false, true}
[#](#_CPPv4N8migraphx2op5slice11starts_axesE)

-
static constexpr std::array<bool, 3> starts_ends = {true, true, false}
[#](#_CPPv4N8migraphx2op5slice11starts_endsE)

-
static constexpr std::array<bool, 3> axes_only = {false, false, true}
[#](#_CPPv4N8migraphx2op5slice9axes_onlyE)

-
static constexpr std::array<bool, 3> ends_only = {false, true, false}
[#](#_CPPv4N8migraphx2op5slice9ends_onlyE)

-
static constexpr std::array<bool, 3> starts_only = {true, false, false}
[#](#_CPPv4N8migraphx2op5slice11starts_onlyE)

-
static constexpr std::array<bool, 3> none_set = {false, false, false}
[#](#_CPPv4N8migraphx2op5slice8none_setE)

-
inline

-
struct softmax
[#](#_CPPv4N8migraphx2op7softmaxE) *#include <migraphx/op/softmax.hpp>*

-
struct squeeze
[#](#_CPPv4N8migraphx2op7squeezeE) *#include <migraphx/op/squeeze.hpp>*

-
struct step
[#](#_CPPv4N8migraphx2op4stepE) *#include <migraphx/op/step.hpp>*

-
struct topk
[#](#_CPPv4N8migraphx2op4topkE) *#include <migraphx/op/topk.hpp>*

-
struct transpose
[#](#_CPPv4N8migraphx2op9transposeE) *#include <migraphx/op/transpose.hpp>*

-
template<class Derived>

struct unary : public migraphx::internal::op::op_name<[Derived](#_CPPv4I0EN8migraphx2op5unaryE)>[#](#_CPPv4I0EN8migraphx2op5unaryE) *#include <migraphx/op/unary.hpp>*

-
struct unary_not : public migraphx::internal::op::unary<
[unary_not](#_CPPv4N8migraphx2op9unary_notE)>[#](#_CPPv4N8migraphx2op9unary_notE) *#include <migraphx/op/unary_not.hpp>*

-
struct undefined
[#](#_CPPv4N8migraphx2op9undefinedE) *#include <migraphx/op/undefined.hpp>*

-
struct unique
[#](#_CPPv4N8migraphx2op6uniqueE) *#include <migraphx/op/unique.hpp>*

-
struct unknown
[#](#_CPPv4N8migraphx2op7unknownE) *#include <migraphx/op/unknown.hpp>*

-
struct unpack_fp4
[#](#_CPPv4N8migraphx2op10unpack_fp4E) *#include <migraphx/op/unpack_fp4.hpp>*

-
struct unpack_int4
[#](#_CPPv4N8migraphx2op11unpack_int4E) *#include <migraphx/op/unpack_int4.hpp>*

-
struct unsqueeze
[#](#_CPPv4N8migraphx2op9unsqueezeE) *#include <migraphx/op/unsqueeze.hpp>*Adds dimensions to a tensor based on the axes attribute.

`axes`

are based on the number of output shape dimensions and should not contain duplicates.`steps`

are for modifying dimensions added to the middle of the original shape. Each step must be a factor of the original dimension. ex: unsqueeze(shape = [3, 4, 10], axes = [2, 4, 5], steps = [2]) -> shape = [3, 4, 2, 5, 1, 1] Dynamic shape version does not handle`steps`

.

-
struct where
[#](#_CPPv4N8migraphx2op5whereE) *#include <migraphx/op/where.hpp>*

-
struct zero
[#](#_CPPv4N8migraphx2op4zeroE) *#include <migraphx/op/reduce_op.hpp>*

-
namespace builder
[#](#_CPPv4N8migraphx2op7builderE) Typedefs

Functions

-
std::vector<instruction_ref> insert(const std::string &name, module &m, instruction_ref ins, const std::vector<instruction_ref> &args, const
[value](https://rocm.docs.amd.com/projects/hipRaft/en/latest/reference/cpp_api/mdspan_representation.html#_CPPv45value)&options)[#](#_CPPv4N8migraphx2op7builder6insertERKNSt6stringER6module15instruction_refRKNSt6vectorI15instruction_refEERK5value)

-
std::vector<instruction_ref> insert(const std::string &name, module &m, instruction_ref ins, const std::vector<instruction_ref> &args, const std::vector<module_ref> &module_args, const
[value](https://rocm.docs.amd.com/projects/hipRaft/en/latest/reference/cpp_api/mdspan_representation.html#_CPPv45value)&options)[#](#_CPPv4N8migraphx2op7builder6insertERKNSt6stringER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value)

-
std::vector<instruction_ref> add(const std::string &name, module &m, const std::vector<instruction_ref> &args, const
[value](https://rocm.docs.amd.com/projects/hipRaft/en/latest/reference/cpp_api/mdspan_representation.html#_CPPv45value)&options)[#](#_CPPv4N8migraphx2op7builder3addERKNSt6stringER6moduleRKNSt6vectorI15instruction_refEERK5value)

-
std::vector<instruction_ref> add(const std::string &name, module &m, const std::vector<instruction_ref> &args, const std::vector<module_ref> &module_args, const
[value](https://rocm.docs.amd.com/projects/hipRaft/en/latest/reference/cpp_api/mdspan_representation.html#_CPPv45value)&options)[#](#_CPPv4N8migraphx2op7builder3addERKNSt6stringER6moduleRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value)

-
template<class ...Ins>

instruction_ref insert_common_op(module &m, instruction_ref ins, const std::string &op_name,[Ins](#_CPPv4IDpEN8migraphx2op7builder16insert_common_opE15instruction_refR6module15instruction_refRKNSt6stringEDp3Ins)... args)[#](#_CPPv4IDpEN8migraphx2op7builder16insert_common_opE15instruction_refR6module15instruction_refRKNSt6stringEDp3Ins)

-
void register_builder(const std::string &name,
[builder_func](#_CPPv4N8migraphx2op7builder12builder_funcE)f)[#](#_CPPv4N8migraphx2op7builder16register_builderERKNSt6stringE12builder_func)

-
template<class T>

auto invoke_builder(module &m, instruction_ref ins, const std::vector<instruction_ref> &args, const std::vector<module_ref> &module_args, const[value](https://rocm.docs.amd.com/projects/hipRaft/en/latest/reference/cpp_api/mdspan_representation.html#_CPPv45value)&options) -> decltype([T](#_CPPv4I0EN8migraphx2op7builder14invoke_builderEDTcldtcl1TE6insert1m3ins4args11module_argsEER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value){}.insert([m](#_CPPv4I0EN8migraphx2op7builder14invoke_builderEDTcldtcl1TE6insert1m3ins4args11module_argsEER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value),[ins](#_CPPv4I0EN8migraphx2op7builder14invoke_builderEDTcldtcl1TE6insert1m3ins4args11module_argsEER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value),[args](#_CPPv4I0EN8migraphx2op7builder14invoke_builderEDTcldtcl1TE6insert1m3ins4args11module_argsEER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value),[module_args](#_CPPv4I0EN8migraphx2op7builder14invoke_builderEDTcldtcl1TE6insert1m3ins4args11module_argsEER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value)))[#](#_CPPv4I0EN8migraphx2op7builder14invoke_builderEDTcldtcl1TE6insert1m3ins4args11module_argsEER6module15instruction_refRKNSt6vectorI15instruction_refEERKNSt6vectorI10module_refEERK5value)

-
template<class T>

void register_builder()[#](#_CPPv4I0EN8migraphx2op7builder16register_builderEvv)

-
static std::unordered_map<std::string,
[builder_func](#_CPPv4N8migraphx2op7builder12builder_funcE)> &builder_map()[#](#_CPPv4N8migraphx2op7builder11builder_mapEv)

-
struct convolution : public migraphx::internal::op::builder::convolution_base<
[convolution](#_CPPv4N8migraphx2op7builder11convolutionE)>[#](#_CPPv4N8migraphx2op7builder11convolutionE)

-
template<class Derived>

struct convolution_base : public migraphx::internal::op::builder::op_builder<[Derived](#_CPPv4I0EN8migraphx2op7builder16convolution_baseE)>[#](#_CPPv4I0EN8migraphx2op7builder16convolution_baseE) Public Functions

-
inline void validate_or_init_attributes(size_t kdims, const instruction_ref x, const instruction_ref w)
[#](#_CPPv4N8migraphx2op7builder16convolution_base27validate_or_init_attributesE6size_tK15instruction_refK15instruction_ref)

-
inline operation make_conv_op(const std::string &name) const
[#](#_CPPv4NK8migraphx2op7builder16convolution_base12make_conv_opERKNSt6stringE)

Public Members

-
std::string auto_pad = "NOTSET"
[#](#_CPPv4N8migraphx2op7builder16convolution_base8auto_padE)

-
std::vector<int64_t> paddings
[#](#_CPPv4N8migraphx2op7builder16convolution_base8paddingsE)

-
std::vector<std::size_t> strides
[#](#_CPPv4N8migraphx2op7builder16convolution_base7stridesE)

-
std::vector<std::size_t> dilations
[#](#_CPPv4N8migraphx2op7builder16convolution_base9dilationsE)

-
int group = 1
[#](#_CPPv4N8migraphx2op7builder16convolution_base5groupE)

-
[padding_mode_t](#_CPPv4N8migraphx2op14padding_mode_tE)padding_mode =[padding_mode_t](#_CPPv4N8migraphx2op14padding_mode_tE)::[default_](#_CPPv4N8migraphx2op14padding_mode_t8default_E)[#](#_CPPv4N8migraphx2op7builder16convolution_base12padding_modeE)

-
inline void validate_or_init_attributes(size_t kdims, const instruction_ref x, const instruction_ref w)

-
struct einsum : public migraphx::internal::op::builder::op_builder<
[einsum](#_CPPv4N8migraphx2op7builder6einsumE)>[#](#_CPPv4N8migraphx2op7builder6einsumE) -
Public Functions

-
inline std::vector<instruction_ref> insert(module &m, instruction_ref ins, const std::vector<instruction_ref> &args) const
[#](#_CPPv4NK8migraphx2op7builder6einsum6insertER6module15instruction_refRKNSt6vectorI15instruction_refEE)

-
inline
[equation_info](#_CPPv4N8migraphx2op7builder6einsum13equation_infoE)analyze_equation(const std::vector<instruction_ref> &args) const[#](#_CPPv4NK8migraphx2op7builder6einsum16analyze_equationERKNSt6vectorI15instruction_refEE)

-
inline
[equation_info](#_CPPv4N8migraphx2op7builder6einsum13equation_infoE)parse_equation() const[#](#_CPPv4NK8migraphx2op7builder6einsum14parse_equationEv)

-
inline size_t validate_input_terms(const std::vector<std::string> &input_terms, const std::vector<instruction_ref> &args) const
[#](#_CPPv4NK8migraphx2op7builder6einsum20validate_input_termsERKNSt6vectorINSt6stringEEERKNSt6vectorI15instruction_refEE)

-
inline void validate_output_term(std::string_view output_term, const std::map<char, int> &label_count, size_t ellipsis_ndim) const
[#](#_CPPv4NK8migraphx2op7builder6einsum20validate_output_termENSt11string_viewERKNSt3mapIciEE6size_t)

-
inline std::string generate_output_term(const std::map<char, int> &label_count, size_t ellipsis_ndim) const
[#](#_CPPv4NK8migraphx2op7builder6einsum20generate_output_termERKNSt3mapIciEE6size_t)

-
inline
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)make_mapping_matrix(const std::vector<std::string> &terms, const std::map<char, int> &label_count, size_t ellipsis_ndim) const[#](#_CPPv4NK8migraphx2op7builder6einsum19make_mapping_matrixERKNSt6vectorINSt6stringEEERKNSt3mapIciEE6size_t)

-
inline std::vector<std::map<char, std::vector<int>>> find_duplicates(const std::vector<std::string> &terms) const
[#](#_CPPv4NK8migraphx2op7builder6einsum15find_duplicatesERKNSt6vectorINSt6stringEEE)

-
inline instruction_ref preprocess_input(module &m, instruction_ref ins, instruction_ref op, const std::map<char, std::vector<int>> &duplicates, const
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&map_mat, size_t input_idx,[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair) const[#](#_CPPv4NK8migraphx2op7builder6einsum16preprocess_inputER6module15instruction_ref15instruction_refRKNSt3mapIcNSt6vectorIiEEEERK7int_mat6size_tR7int_mat)

-
inline instruction_ref gather_diagonal(module &m, instruction_ref ins,
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair, instruction_ref op, const[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&diag) const[#](#_CPPv4NK8migraphx2op7builder6einsum15gather_diagonalER6module15instruction_refR7int_mat15instruction_refRK7int_mat)

-
inline instruction_ref process_pair(module &m, instruction_ref ins, instruction_ref op1, instruction_ref op2, const
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&map_mat, size_t input_idx,[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair) const[#](#_CPPv4NK8migraphx2op7builder6einsum12process_pairER6module15instruction_ref15instruction_ref15instruction_refRK7int_mat6size_tR7int_mat)

-
inline instruction_ref batch_dot(module &m, instruction_ref ins,
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair, instruction_ref op1, instruction_ref op2, const std::vector<int> &batch_axes, const std::vector<int> &sum_axes) const[#](#_CPPv4NK8migraphx2op7builder6einsum9batch_dotER6module15instruction_refR7int_mat15instruction_ref15instruction_refRKNSt6vectorIiEERKNSt6vectorIiEE)

-
inline instruction_ref finalize_output(module &m, instruction_ref ins, instruction_ref op, const
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&map_mat,[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair) const[#](#_CPPv4NK8migraphx2op7builder6einsum15finalize_outputER6module15instruction_ref15instruction_refRK7int_matR7int_mat)

-
inline instruction_ref transpose_unsqueeze(module &m, instruction_ref ins,
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair, instruction_ref op) const[#](#_CPPv4NK8migraphx2op7builder6einsum19transpose_unsqueezeER6module15instruction_refR7int_mat15instruction_ref)

-
inline instruction_ref squeeze_transpose(module &m, instruction_ref ins,
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)&cur_pair, instruction_ref op, std::vector<int> row_output) const[#](#_CPPv4NK8migraphx2op7builder6einsum17squeeze_transposeER6module15instruction_refR7int_mat15instruction_refNSt6vectorIiEE)

-
inline instruction_ref apply_transpose_op(module &m, instruction_ref ins, instruction_ref op, const std::vector<int64_t> &perm, std::vector<int> &row) const
[#](#_CPPv4NK8migraphx2op7builder6einsum18apply_transpose_opER6module15instruction_ref15instruction_refRKNSt6vectorI7int64_tEERNSt6vectorIiEE)

-
inline std::pair<instruction_ref, instruction_ref> apply_broadcast_op(module &m, instruction_ref ins, instruction_ref opl, instruction_ref opr, const std::vector<int> &common_labels) const
[#](#_CPPv4NK8migraphx2op7builder6einsum18apply_broadcast_opER6module15instruction_ref15instruction_ref15instruction_refRKNSt6vectorIiEE)

-
inline instruction_ref apply_reduce_sum_op(module &m, instruction_ref ins, instruction_ref op, const std::vector<int> &axes, std::vector<int> &row) const
[#](#_CPPv4NK8migraphx2op7builder6einsum19apply_reduce_sum_opER6module15instruction_ref15instruction_refRKNSt6vectorIiEERNSt6vectorIiEE)

-
inline std::vector<int> extract_column(
[int_mat](#_CPPv4N8migraphx2op7builder6einsum7int_matE)map_mat, int col_idx, int row_begin, int row_end) const[#](#_CPPv4NK8migraphx2op7builder6einsum14extract_columnE7int_matiii)

-
inline std::vector<int> set_union(const std::vector<int> &lhs, const std::vector<int> &rhs) const
[#](#_CPPv4NK8migraphx2op7builder6einsum9set_unionERKNSt6vectorIiEERKNSt6vectorIiEE)

-
inline std::vector<int> set_difference(const std::vector<int> &lhs, const std::vector<int> &rhs) const
[#](#_CPPv4NK8migraphx2op7builder6einsum14set_differenceERKNSt6vectorIiEERKNSt6vectorIiEE)

-
inline std::vector<int> arange(int start_value, int end_value) const
[#](#_CPPv4NK8migraphx2op7builder6einsum6arangeEii)

-
inline size_t calc_dim(const std::vector<int> &axes, const std::vector<size_t> &lens) const
[#](#_CPPv4NK8migraphx2op7builder6einsum8calc_dimERKNSt6vectorIiEERKNSt6vectorI6size_tEE)

-
struct equation_info
[#](#_CPPv4N8migraphx2op7builder6einsum13equation_infoE)

-
inline std::vector<instruction_ref> insert(module &m, instruction_ref ins, const std::vector<instruction_ref> &args) const

-
struct gelu_quick : public migraphx::internal::op::builder::op_builder<
[gelu_quick](#_CPPv4N8migraphx2op7builder10gelu_quickE)>[#](#_CPPv4N8migraphx2op7builder10gelu_quickE)

-
struct gelu_split : public migraphx::internal::op::builder::op_builder<
[gelu_split](#_CPPv4N8migraphx2op7builder10gelu_splitE)>[#](#_CPPv4N8migraphx2op7builder10gelu_splitE)

-
struct mean_variance_normalization : public migraphx::internal::op::builder::op_builder<
[mean_variance_normalization](#_CPPv4N8migraphx2op7builder27mean_variance_normalizationE)>[#](#_CPPv4N8migraphx2op7builder27mean_variance_normalizationE)

-
template<class T>

struct op_builder : public migraphx::internal::auto_register<[register_builder_action](#_CPPv4N8migraphx2op7builder23register_builder_actionE),[T](#_CPPv4I0EN8migraphx2op7builder10op_builderE)>[#](#_CPPv4I0EN8migraphx2op7builder10op_builderE) *#include </home/docs/checkouts/readthedocs.org/user_builds/advanced-micro-devices-amdmigraphx/checkouts/latest/src/op/builder/include/migraphx/op/builder/op_builder.hpp>*Subclassed by

[migraphx::internal::op::builder::convolution_base< convolution >](#structmigraphx_1_1internal_1_1op_1_1builder_1_1convolution__base),[migraphx::internal::op::builder::convolution_base< quant_convolution >](#structmigraphx_1_1internal_1_1op_1_1builder_1_1convolution__base)

-
struct quant_convolution : public migraphx::internal::op::builder::convolution_base<
[quant_convolution](#_CPPv4N8migraphx2op7builder17quant_convolutionE)>[#](#_CPPv4N8migraphx2op7builder17quant_convolutionE) Public Functions

-
inline std::vector<instruction_ref> insert(module &m, instruction_ref ins, const std::vector<instruction_ref> &args)
[#](#_CPPv4N8migraphx2op7builder17quant_convolution6insertER6module15instruction_refRKNSt6vectorI15instruction_refEE)

-
inline instruction_ref add_int8_shift(module &m, instruction_ref ins, const instruction_ref &offset_op, instruction_ref &unshifted_input) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution14add_int8_shiftER6module15instruction_refRK15instruction_refR15instruction_ref)

-
inline void shift_input_and_bias(module &m, instruction_ref ins, const instruction_ref &offset_op, const bool has_bias, instruction_ref &input, instruction_ref &input_bias) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution20shift_input_and_biasER6module15instruction_refRK15instruction_refKbR15instruction_refR15instruction_ref)

-
inline float get_symmetric_value(const instruction_ref &input) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution19get_symmetric_valueERK15instruction_ref)

-
inline instruction_ref gen_symmetric_literal(module &m, const instruction_ref &input) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution21gen_symmetric_literalER6moduleRK15instruction_ref)

-
inline instruction_ref get_zero_point(module &m, const instruction_ref &input, int index, const std::vector<instruction_ref> &args) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution14get_zero_pointER6moduleRK15instruction_refiRKNSt6vectorI15instruction_refEE)

-
inline bool is_symmetric_zero_point(instruction_ref zp) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution23is_symmetric_zero_pointE15instruction_ref)

-
inline auto qparam_broadcast_op(instruction_ref qparam, std::vector<std::size_t> lens, std::size_t axis) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution19qparam_broadcast_opE15instruction_refNSt6vectorINSt6size_tEEENSt6size_tE)

-
inline instruction_ref handle_quant_bias(module &m, instruction_ref ins, const operation &op, const instruction_ref &input, const instruction_ref &x, const instruction_ref &weights, const instruction_ref &x_zp, const instruction_ref &w_zp) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution17handle_quant_biasER6module15instruction_refRK9operationRK15instruction_refRK15instruction_refRK15instruction_refRK15instruction_refRK15instruction_ref)

-
inline void handle_quant_inputs(module &m, instruction_ref ins, instruction_ref &input, instruction_ref &weights, instruction_ref &input_zp, instruction_ref &weight_zp) const
[#](#_CPPv4NK8migraphx2op7builder17quant_convolution19handle_quant_inputsER6module15instruction_refR15instruction_refR15instruction_refR15instruction_refR15instruction_ref)

-
inline std::vector<instruction_ref> insert(module &m, instruction_ref ins, const std::vector<instruction_ref> &args)

-
struct register_builder_action
[#](#_CPPv4N8migraphx2op7builder23register_builder_actionE) *#include </home/docs/checkouts/readthedocs.org/user_builds/advanced-micro-devices-amdmigraphx/checkouts/latest/src/op/builder/include/migraphx/op/builder/op_builder.hpp>*

-
std::vector<instruction_ref> insert(const std::string &name, module &m, instruction_ref ins, const std::vector<instruction_ref> &args, const

-
enum class normalize_attribute
