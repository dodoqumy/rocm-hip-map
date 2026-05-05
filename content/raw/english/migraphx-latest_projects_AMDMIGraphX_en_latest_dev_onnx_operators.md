---
title: "Supported ONNX Operators"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/onnx_operators.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:52.122515+00:00
content_hash: "246ed76a8680d547"
---

# Supported ONNX Operators[#](#supported-onnx-operators)

2025-10-14

10 min read time

MIGraphX supports operators up to Opset 19. Latest information of ONNX
operators can be found in [the ONNX GitHub repository](https://github.com/onnx/onnx/blob/master/docs/Operators.md).

MIGraphX supports the following ONNX data types: BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FLOAT8, FLOAT16, FLOAT32, and DOUBLE

See below for the support matrix of ONNX operators in MIGraphX.

Note

The listed supported types are taken from the ONNX specification. An operator might support other additional datatypes.


## Operator Support Matrix[#](#operator-support-matrix)

Operator |
Supported |
Supported Types |
Limitations |
|---|---|---|---|
Abs |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Acos |
✅ |
FP8, FP16, FP32, FP64 |
|
Acosh |
✅ |
FP8, FP16, FP32, FP64 |
|
Add |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
And |
✅ |
BOOL |
|
ArgMax |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
ArgMin |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Asin |
✅ |
FP8, FP16, FP32, FP64 |
|
Asinh |
✅ |
FP8, FP16, FP32, FP64 |
|
Atan |
✅ |
FP8, FP16, FP32, FP64 |
|
Atanh |
✅ |
FP8, FP16, FP32, FP64 |
|
AveragePool |
✅ |
FP8, FP16, FP32, FP64 |
|
BatchNormalization |
✅ |
FP8, FP16, FP32, FP64 |
|
BiasGelu |
✅ |
FP8, FP16, FP32, FP64 |
|
Bernoulli |
❌ |
||
BitShift |
❌ |
||
BitwiseAnd |
❌ |
||
BitwiseNot |
❌ |
||
BitwiseOr |
❌ |
||
BitwiseXor |
❌ |
||
BlackmanWindow |
❌ |
||
Cast |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP16, FP32, FP64 |
|
CastLike |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP16, FP32, FP64 |
|
Ceil |
✅ |
FP8, FP16, FP32, FP64 |
|
Celu |
✅ |
FP32 |
|
CenterCropPad |
❌ |
||
Clip |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Col2Im |
❌ |
||
Compress |
❌ |
||
Concat |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
ConcatFromSequence |
❌ |
||
Constant |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
ConstantOfShape |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP16, FP32, FP64 |
dynamic shape is not supported |
Conv |
✅ |
FP8, FP16, FP32, FP64 |
|
ConvInteger |
✅ |
INT8 |
|
ConvTranspose |
✅ |
FP8, FP16, FP32, FP64 |
|
Cos |
✅ |
FP8, FP16, FP32, FP64 |
|
Cosh |
✅ |
FP8, FP16, FP32, FP64 |
|
CumSum |
✅ |
UINT32, UINT64, INT32, INT64, FP8, FP16, FP32, FP64 |
|
DFT |
❌ |
||
DeformConv |
❌ |
||
DepthToSpace |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
DequantizeLinear |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Det |
❌ |
||
Div |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Dropout |
✅ |
Any |
Changed to
|
DynamicQuantizeLinear |
✅ |
FP8, FP16, FP32, FP64 |
|
Einsum |
✅ |
Any |
more than 1 diagonal per
input is not supported
e.g. batch diagonal where batches
are not the leading dims is
not supported
e.g. |
Elu |
✅ |
FP8, FP16, FP32, FP64 |
|
Equal |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Erf |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Exp |
✅ |
FP8, FP16, FP32, FP64 |
|
Expand |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
dynamic shape is not supported |
EyeLike |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
FastGelu |
✅ |
FP8, FP16, FP32 |
|
Flatten |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Floor |
✅ |
FP8, FP16, FP32, FP64 |
|
Gather |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
GatherElements |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
GatherND |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Gelu |
✅ |
FP8, FP16, FP32, FP64 |
|
Gemm |
✅ |
UINT32, UINT64, INT32, INT64, FP8, FP16, FP32, FP64 |
|
GlobalAveragePool |
✅ |
FP8, FP16, FP32, FP64 |
|
GlobalLpPool |
✅ |
FP8, FP16, FP32, FP64 |
|
GlobalMaxPool |
✅ |
FP8, FP16, FP32, FP64 |
|
Greater |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
GreaterOrEqual |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
GridSample |
✅ |
UINT32, UINT64, INT32, INT64, FP16, FP32, FP64 |
5-D inputs not supported |
GroupNormalization |
✅ |
FP8, FP16, FP32, FP64 |
|
GRU |
✅ |
FP8, FP16, FP32, FP64 |
|
HammingWindow |
❌ |
||
HannWindow |
❌ |
||
HardSigmoid |
✅ |
FP8, FP16, FP32, FP64 |
|
HardSwish |
✅ |
FP8, FP16, FP32, FP64 |
|
Hardmax |
✅ |
FP8, FP16, FP32, FP64 |
|
Identity |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
If |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
InstanceNormalization |
✅ |
FP16, FP32, FP64 |
|
IsInf |
✅ |
FP8, FP16, FP32, FP64 |
|
IsNaN |
✅ |
FP8, FP16, FP32, FP64 |
|
LayerNormalization |
✅ |
FP8, FP16, FP32, FP64 |
|
LeakyRelu |
✅ |
FP8, FP16, FP32, FP64 |
|
Less |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
LessOrEqual |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Log |
✅ |
FP8, FP16, FP32, FP64 |
|
LogSoftmax |
✅ |
FP8, FP16, FP32, FP64 |
|
Loop |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
LRN |
✅ |
FP8, FP16, FP32, FP64 |
|
LSTM |
✅ |
FP32, FP16 |
|
LpNormalization |
✅ |
FP8, FP16, FP32, FP64 |
|
LpPool |
✅ |
FP32, FP16, FP8, INT8 |
|
MatMul |
✅ |
UINT32, UINT64, INT32, INT64, FP8, FP16, FP32, FP64 |
|
MatMulInteger |
✅ |
UINT8, INT8 |
dynamic shape is not supported |
Max |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
MaxPool |
✅ |
FP32, FP16, FP8, INT8 |
|
MaxRoiPool |
❌ |
||
MaxUnpool |
❌ |
||
Mean |
✅ |
FP8, FP16, FP32, FP64 |
|
MeanVarian ceNormalization |
✅ |
FP8, FP16, FP32, FP64 |
|
MelWeightMatrix |
❌ |
||
Min |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Mish |
❌ |
||
Mod |
✅ |
UINT8, UINT16, UINT32, UINT64, INT16, INT64, FP8, FP16, FP32, FP64 |
|
Mul |
✅ |
UINT8, UINT16, UINT32, UINT64, INT16, INT64, FP8, FP16, FP32, FP64 |
|
Multinomial |
✅ |
FP8, FP16, FP32, FP64 |
|
Neg |
✅ |
INT8, INT32, INT64, FP8, FP16, FP32, FP64 |
|
NegativeLogLikelihoodLoss |
❌ |
||
NonMaxSuppression |
✅ |
FP8, FP16, FP32, FP64 |
fixed output
size unless
|
NonZero |
✅ |
FP8, FP16, FP32, FP64 |
fixed output
size unless
|
Not |
✅ |
BOOL |
|
OneHot |
✅ |
UINT8, UINT16, UINT32, UINT64, INT16, INT64, FP8, FP16, FP32, FP64 |
dynamic shape is not supported |
Optional |
❌ |
||
OptionalGetElement |
❌ |
||
OptionalHasElement |
❌ |
||
Or |
✅ |
BOOL |
|
Pad |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Pow |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
PRelu |
✅ |
UINT32, UINT64, INT32, INT64, FP8, FP16, FP32, FP64 |
|
QLinearAdd |
✅ |
UINT8, INT8 |
|
QLinearAveragePool |
✅ |
UINT8, INT8 |
|
QLinearConcat |
✅ |
UINT8, INT8 |
|
QLinearConv |
✅ |
UINT8, INT8 |
|
QLinearGlobalAveragePool |
✅ |
UINT8, INT8 |
|
QLinearLeakyRelu |
✅ |
UINT8, INT8 |
|
QLinearMatMul |
✅ |
UINT8, INT8 |
non-scalar inputs are not supported |
QLinearMul |
✅ |
UINT8, INT8 |
|
QLinearSigmoid |
✅ |
UINT8, INT8 |
|
QuantizeLinear |
✅ |
FP8, FP16, FP32, INT32 |
|
RandomNormal |
✅ |
FP16, FP32, FP64 |
|
RandomNormalLike |
✅ |
FP16, FP32, FP64 |
|
RandomUniform |
✅ |
FP16, FP32, FP64 |
|
RandomUniformLike |
✅ |
FP16, FP32, FP64 |
|
Range |
✅ |
FP16, FP32, FP64, INT16, INT32, INT64 |
|
Reciprocal |
✅ |
FP8, FP16, FP32, FP64 |
|
ReduceL1 |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceL2 |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceLogSum |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceLogSumExp |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceMax |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceMean |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceMin |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceProd |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceSum |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
ReduceSumSquare |
✅ |
FP16, FP32, FP64, UINT32, UINT64, INT32, INT64 |
|
Relu |
✅ |
FP16, FP32, FP64, INT8, INT16, INT32, INT64 |
|
Reshape |
✅ |
FP32, FP16, INT32, INT64, FP8, INT8, BOOL |
|
Resize |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
ReverseSequence |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
variable
|
RNN |
✅ |
FP32, FP16 |
|
RoiAlign |
✅ |
FP8, FP16, FP32, FP64 |
|
Round |
✅ |
FP8, FP16, FP32, FP64 |
|
STFT |
❌ |
||
Scan |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Scatter (deprecated) |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
ScatterElements |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
ScatterND |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Selu |
✅ |
FP8, FP16, FP32, FP64 |
|
SequenceAt |
❌ |
||
SequenceConstruct |
❌ |
||
SequenceEmpty |
❌ |
||
SequenceErase |
❌ |
||
SequenceInsert |
❌ |
||
SequenceLength |
❌ |
||
SequenceMap |
❌ |
||
Shape |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Shrink |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Sigmoid |
✅ |
FP8, FP16, FP32, FP64 |
|
Sign |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Sin |
✅ |
FP8, FP16, FP32, FP64 |
|
Sinh |
✅ |
FP8, FP16, FP32, FP64 |
|
Size |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Slice |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
variable inputs are not supported |
Softmax |
✅ |
FP8, FP16, FP32, FP64 |
|
SoftmaxCrossEntropyLoss |
❌ |
||
Softplus |
✅ |
FP8, FP16, FP32, FP64 |
|
Softsign |
✅ |
FP8, FP16, FP32, FP64 |
|
SpaceToDepth |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Split |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
dynamic shape is not supported |
SplitToSequence |
❌ |
||
Sqrt |
✅ |
FP8, FP16, FP32, FP64 |
|
Squeeze |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
variable |
StringNormalizer |
❌ |
||
Sub |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Sum |
✅ |
FP8, FP16, FP32, FP64 |
|
Tan |
✅ |
FP8, FP16, FP32, FP64 |
|
Tanh |
✅ |
FP8, FP16, FP32, FP64 |
|
TfIdfVectorizer |
❌ |
||
ThresholdedRelu |
✅ |
FP8, FP16, FP32, FP64 |
|
Tile |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
dynamic shape is not supported |
TopK |
✅ |
UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
dynamic |
Transpose |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Trilu |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
dynamic |
Unique |
✅ |
Any |
only
|
Unsqueeze |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
variable
|
Upsample (deprecated) |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
|
Where |
✅ |
BOOL, UINT8, UINT16, UINT32, UINT64, INT8, INT16, INT32, INT64, FP8, FP16, FP32, FP64 |
mixed static and dynamic shape inputs are not supported |
Xor |
✅ |
BOOL |
