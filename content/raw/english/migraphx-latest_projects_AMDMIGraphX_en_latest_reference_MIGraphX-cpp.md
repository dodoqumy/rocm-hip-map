---
title: "MIGraphX C++ API reference"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/reference/MIGraphX-cpp.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:10.489851+00:00
content_hash: "ff871abfbc69eb1e"
---

# MIGraphX C++ API reference[#](#migraphx-c-api-reference)

2025-10-14

10 min read time

## shape[#](#shape)

-
enum migraphx_shape_datatype_t
[#](#_CPPv425migraphx_shape_datatype_t) An enum to represent the different data type inputs.

*Values:*-
enumerator migraphx_shape_tuple_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_tuple_typeE)

-
enumerator migraphx_shape_fp4x2_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_fp4x2_typeE)

-
enumerator migraphx_shape_bool_type
[#](#_CPPv4N25migraphx_shape_datatype_t24migraphx_shape_bool_typeE)

-
enumerator migraphx_shape_half_type
[#](#_CPPv4N25migraphx_shape_datatype_t24migraphx_shape_half_typeE)

-
enumerator migraphx_shape_float_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_float_typeE)

-
enumerator migraphx_shape_double_type
[#](#_CPPv4N25migraphx_shape_datatype_t26migraphx_shape_double_typeE)

-
enumerator migraphx_shape_uint8_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_uint8_typeE)

-
enumerator migraphx_shape_int8_type
[#](#_CPPv4N25migraphx_shape_datatype_t24migraphx_shape_int8_typeE)

-
enumerator migraphx_shape_uint16_type
[#](#_CPPv4N25migraphx_shape_datatype_t26migraphx_shape_uint16_typeE)

-
enumerator migraphx_shape_int16_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_int16_typeE)

-
enumerator migraphx_shape_int32_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_int32_typeE)

-
enumerator migraphx_shape_int64_type
[#](#_CPPv4N25migraphx_shape_datatype_t25migraphx_shape_int64_typeE)

-
enumerator migraphx_shape_uint32_type
[#](#_CPPv4N25migraphx_shape_datatype_t26migraphx_shape_uint32_typeE)

-
enumerator migraphx_shape_uint64_type
[#](#_CPPv4N25migraphx_shape_datatype_t26migraphx_shape_uint64_typeE)

-
enumerator migraphx_shape_fp8e4m3fnuz_type
[#](#_CPPv4N25migraphx_shape_datatype_t31migraphx_shape_fp8e4m3fnuz_typeE)

-
enumerator migraphx_shape_fp8e4m3fn_type
[#](#_CPPv4N25migraphx_shape_datatype_t29migraphx_shape_fp8e4m3fn_typeE)

-
enumerator migraphx_shape_fp8e5m2_type
[#](#_CPPv4N25migraphx_shape_datatype_t27migraphx_shape_fp8e5m2_typeE)

-
enumerator migraphx_shape_bf16_type
[#](#_CPPv4N25migraphx_shape_datatype_t24migraphx_shape_bf16_typeE)

-
enumerator migraphx_shape_fp8e5m2fnuz_type
[#](#_CPPv4N25migraphx_shape_datatype_t31migraphx_shape_fp8e5m2fnuz_typeE)

-
enumerator migraphx_shape_tuple_type

-
template<class Lens, class Strides>

struct shape : public migraphx::handle_base<>, public migraphx::equality_comparable<[shape](#_CPPv4I00EN8migraphx5shapeE)<[Lens](#_CPPv4I00EN8migraphx5shapeE),[Strides](#_CPPv4I00EN8migraphx5shapeE)>>[#](#_CPPv4I00EN8migraphx5shapeE) Describe shape of tensor.

A shape consists of a data type, lengths of multi-dimension tensor, and strides

Public Functions

-
inline shape()
[#](#_CPPv4N8migraphx5shape5shapeEv)

-
inline shape(const migraphx_shape *p)
[#](#_CPPv4N8migraphx5shape5shapeEPK14migraphx_shape)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx5shape5shapeEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline shape([HandleType](#_CPPv4I000EN8migraphx5shape5shapeEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx5shape5shapeEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx5shape5shapeEP10HandleType8Lifetime)

-
inline shape(
[migraphx_shape_datatype_t](#_CPPv425migraphx_shape_datatype_t)type)[#](#_CPPv4N8migraphx5shape5shapeE25migraphx_shape_datatype_t) Construct a scalar shape.


-
inline shape(
[migraphx_shape_datatype_t](#_CPPv425migraphx_shape_datatype_t)type, std::vector<size_t> plengths)[#](#_CPPv4N8migraphx5shape5shapeE25migraphx_shape_datatype_tNSt6vectorI6size_tEE) Construct a shape with its type and lengths. The strides are automatically computed assumming a packed layout.


-
inline shape(
[migraphx_shape_datatype_t](#_CPPv425migraphx_shape_datatype_t)t, std::initializer_list<std::size_t> d)[#](#_CPPv4N8migraphx5shape5shapeE25migraphx_shape_datatype_tNSt16initializer_listINSt6size_tEEE)

-
inline shape(
[migraphx_shape_datatype_t](#_CPPv425migraphx_shape_datatype_t)type, std::vector<size_t> plengths, std::vector<size_t> pstrides)[#](#_CPPv4N8migraphx5shape5shapeE25migraphx_shape_datatype_tNSt6vectorI6size_tEENSt6vectorI6size_tEE)

-
inline shape(
[migraphx_shape_datatype_t](#_CPPv425migraphx_shape_datatype_t)type, const dynamic_dimensions &dyn_dims)[#](#_CPPv4N8migraphx5shape5shapeE25migraphx_shape_datatype_tRK18dynamic_dimensions)

-
inline std::vector<size_t> lengths() const
[#](#_CPPv4NK8migraphx5shape7lengthsEv)

-
inline std::vector<size_t> strides() const

-
inline dynamic_dimensions dyn_dims() const
[#](#_CPPv4NK8migraphx5shape8dyn_dimsEv) Get the dynamic dimensions of the shape.


-
inline
[migraphx_shape_datatype_t](#_CPPv425migraphx_shape_datatype_t)type() const[#](#_CPPv4NK8migraphx5shape4typeEv)

-
inline size_t elements() const
[#](#_CPPv4NK8migraphx5shape8elementsEv)

-
inline size_t bytes() const
[#](#_CPPv4NK8migraphx5shape5bytesEv)

-
inline bool standard() const
[#](#_CPPv4NK8migraphx5shape8standardEv)

-
inline bool dynamic() const
[#](#_CPPv4NK8migraphx5shape7dynamicEv) Is the shape dynamic.


-
inline size_t index(size_t i) const
[#](#_CPPv4NK8migraphx5shape5indexE6size_t)

-
constexpr shape() = default

-
inline constexpr auto elements() const

-
inline constexpr auto element_space() const
[#](#_CPPv4NK8migraphx5shape13element_spaceEv)

-
inline constexpr auto packed() const
[#](#_CPPv4NK8migraphx5shape6packedEv)

-
inline constexpr auto broadcasted() const
[#](#_CPPv4NK8migraphx5shape11broadcastedEv)

-
inline constexpr auto transposed() const
[#](#_CPPv4NK8migraphx5shape10transposedEv)

-
inline constexpr auto skips() const
[#](#_CPPv4NK8migraphx5shape5skipsEv)

-
inline constexpr auto standard() const

-
inline constexpr index_int index(
[index_array](#_CPPv4N8migraphx5shape11index_arrayE)x) const[#](#_CPPv4NK8migraphx5shape5indexE11index_array)

-
inline constexpr index_int index(index_int i) const
[#](#_CPPv4NK8migraphx5shape5indexE9index_int)

-
inline constexpr index_int compute_index(index_int i) const
[#](#_CPPv4NK8migraphx5shape13compute_indexE9index_int)

-
inline constexpr
[index_array](#_CPPv4N8migraphx5shape11index_arrayE)multi(index_int idx) const[#](#_CPPv4NK8migraphx5shape5multiE9index_int) Convert single index into a multi-index.


-
inline constexpr index_int single(
[index_array](#_CPPv4N8migraphx5shape11index_arrayE)idx) const[#](#_CPPv4NK8migraphx5shape6singleE11index_array) Convert multi-index into a single index.


-
inline shape()

## argument[#](#argument)

-
struct argument : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx8argumentE) Arguments to be passed to an migraphx arguments.

An

`argument`

represents a raw buffer of data with a shape.Public Functions

-
inline argument()
[#](#_CPPv4N8migraphx8argument8argumentEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx8argument8argumentEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline argument([HandleType](#_CPPv4I000EN8migraphx8argument8argumentEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx8argument8argumentEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx8argument8argumentEP10HandleType8Lifetime)

-
inline argument(const migraphx_argument *p)
[#](#_CPPv4N8migraphx8argument8argumentEPK17migraphx_argument)

-
inline char *data() const
[#](#_CPPv4NK8migraphx8argument4dataEv)

-
inline argument()

## target[#](#target)

-
struct target : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx6targetE) A target for compilation.

Public Functions

-
inline target()
[#](#_CPPv4N8migraphx6target6targetEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx6target6targetEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline target([HandleType](#_CPPv4I000EN8migraphx6target6targetEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx6target6targetEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx6target6targetEP10HandleType8Lifetime)

-
inline target(const char *name)
[#](#_CPPv4N8migraphx6target6targetEPKc) Construct a target from its name.


-
inline target()

## program[#](#program)

-
struct program_parameter_shapes : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx24program_parameter_shapesE) Public Functions

-
inline program_parameter_shapes()
[#](#_CPPv4N8migraphx24program_parameter_shapes24program_parameter_shapesEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx24program_parameter_shapes24program_parameter_shapesEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline program_parameter_shapes([HandleType](#_CPPv4I000EN8migraphx24program_parameter_shapes24program_parameter_shapesEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx24program_parameter_shapes24program_parameter_shapesEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx24program_parameter_shapes24program_parameter_shapesEP10HandleType8Lifetime)

-
inline size_t size() const
[#](#_CPPv4NK8migraphx24program_parameter_shapes4sizeEv)

-
inline std::vector<const char*> names() const
[#](#_CPPv4NK8migraphx24program_parameter_shapes5namesEv)

-
inline program_parameter_shapes()

-
struct program_parameters : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx18program_parametersE) A class to construct the inputs parameters for a program.

Public Functions

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx18program_parameters18program_parametersEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline program_parameters([HandleType](#_CPPv4I000EN8migraphx18program_parameters18program_parametersEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx18program_parameters18program_parametersEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx18program_parameters18program_parametersEP10HandleType8Lifetime)

-
inline program_parameters(migraphx_program_parameters *p)
[#](#_CPPv4N8migraphx18program_parameters18program_parametersEP27migraphx_program_parameters)

-
inline program_parameters()
[#](#_CPPv4N8migraphx18program_parameters18program_parametersEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<

-
struct migraphx_compile_options
[#](#_CPPv424migraphx_compile_options)

-
struct program : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx7programE) A program represents the all computation graphs to be compiled and executed.

Public Functions

-
inline program()
[#](#_CPPv4N8migraphx7program7programEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx7program7programEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline program([HandleType](#_CPPv4I000EN8migraphx7program7programEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx7program7programEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx7program7programEP10HandleType8Lifetime)

-
inline void compile(const
[target](#_CPPv4N8migraphx6targetE)&ptarget, const compile_options &poptions) const[#](#_CPPv4NK8migraphx7program7compileERK6targetRK15compile_options) Compile the program for a specific target to be ran on.


-
inline void compile(const
[target](#_CPPv4N8migraphx6targetE)&ptarget) const[#](#_CPPv4NK8migraphx7program7compileERK6target) Compile the program for a specific target to be ran on.


-
inline
[program_parameter_shapes](#_CPPv4N8migraphx24program_parameter_shapesE)get_parameter_shapes() const[#](#_CPPv4NK8migraphx7program20get_parameter_shapesEv) Return the shapes for the input parameters.


-
inline shapes get_output_shapes() const
[#](#_CPPv4NK8migraphx7program17get_output_shapesEv) Get the shapes of all the outputs returned by this program.


-
inline arguments eval(const
[program_parameters](#_CPPv4N8migraphx18program_parametersE)&pparams) const[#](#_CPPv4NK8migraphx7program4evalERK18program_parameters) Run the program using the inputs passed in.


-
template<class Stream>

inline arguments run_async(const[program_parameters](#_CPPv4N8migraphx18program_parametersE)&pparams,[Stream](#_CPPv4I0ENK8migraphx7program9run_asyncE9argumentsRK18program_parametersP6Stream)*s) const[#](#_CPPv4I0ENK8migraphx7program9run_asyncE9argumentsRK18program_parametersP6Stream) Overloaded to allow for execution_environment input.


-
inline void print() const
[#](#_CPPv4NK8migraphx7program5printEv)

-
call &migraphx_program_get_main_module()
[#](#_CPPv4N8migraphx7program32migraphx_program_get_main_moduleEv)

-
inline context experimental_get_context()
[#](#_CPPv4N8migraphx7program24experimental_get_contextEv)

- call & migraphx_program_create_module (), name.data()

Public Members

- return module = {p_modu, this->share_handle()}

-
inline program()

## quantize[#](#quantize)

-
struct quantize_op_names : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx17quantize_op_namesE) Public Functions

-
inline quantize_op_names()
[#](#_CPPv4N8migraphx17quantize_op_names17quantize_op_namesEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx17quantize_op_names17quantize_op_namesEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline quantize_op_names([HandleType](#_CPPv4I000EN8migraphx17quantize_op_names17quantize_op_namesEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx17quantize_op_names17quantize_op_namesEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx17quantize_op_names17quantize_op_namesEP10HandleType8Lifetime)

-
inline void add(const std::string &name)
[#](#_CPPv4N8migraphx17quantize_op_names3addERKNSt6stringE)

-
inline quantize_op_names()

-
inline void migraphx::quantize_fp16(const
[program](#_CPPv4N8migraphx7programE)&prog, const[quantize_op_names](#_CPPv4N8migraphx17quantize_op_namesE)&names)[#](#_CPPv4N8migraphx13quantize_fp16ERK7programRK17quantize_op_names) Quantize program to use fp16.


-
struct quantize_int8_options : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx21quantize_int8_optionsE) Options to be passed when quantizing for int8.

Public Functions

-
inline quantize_int8_options()
[#](#_CPPv4N8migraphx21quantize_int8_options21quantize_int8_optionsEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx21quantize_int8_options21quantize_int8_optionsEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline quantize_int8_options([HandleType](#_CPPv4I000EN8migraphx21quantize_int8_options21quantize_int8_optionsEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx21quantize_int8_options21quantize_int8_optionsEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx21quantize_int8_options21quantize_int8_optionsEP10HandleType8Lifetime)

-
inline void add_op_name(const std::string &name)
[#](#_CPPv4N8migraphx21quantize_int8_options11add_op_nameERKNSt6stringE) Add an operator that should be quantized.


-
inline void add_calibration_data(const
[program_parameters](#_CPPv4N8migraphx18program_parametersE)&pp)[#](#_CPPv4N8migraphx21quantize_int8_options20add_calibration_dataERK18program_parameters) Add calibrartion data to be used for quantizing.


-
inline quantize_int8_options()

## parse_onnx[#](#parse-onnx)

-
struct onnx_options : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx12onnx_optionsE) Options for parsing onnx options.

Public Functions

-
inline onnx_options()
[#](#_CPPv4N8migraphx12onnx_options12onnx_optionsEv)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx12onnx_options12onnx_optionsEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline onnx_options([HandleType](#_CPPv4I000EN8migraphx12onnx_options12onnx_optionsEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx12onnx_options12onnx_optionsEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx12onnx_options12onnx_optionsEP10HandleType8Lifetime)

-
inline void set_input_parameter_shape(const std::string &name, std::vector<std::size_t> dim)
[#](#_CPPv4N8migraphx12onnx_options25set_input_parameter_shapeERKNSt6stringENSt6vectorINSt6size_tEEE) Make onnx parser treat an inputs with a certain dimensions.


-
inline void set_dyn_input_parameter_shape(const std::string &name, const dynamic_dimensions &dyn_dims)
[#](#_CPPv4N8migraphx12onnx_options29set_dyn_input_parameter_shapeERKNSt6stringERK18dynamic_dimensions)

-
inline void set_default_dim_value(unsigned int value)
[#](#_CPPv4N8migraphx12onnx_options21set_default_dim_valueEj) When there is a dimension parameter, then use this default value.


-
inline void set_default_dyn_dim_value(const dynamic_dimension &dd)
[#](#_CPPv4N8migraphx12onnx_options25set_default_dyn_dim_valueERK17dynamic_dimension)

-
inline void set_default_loop_iterations(int64_t value)
[#](#_CPPv4N8migraphx12onnx_options27set_default_loop_iterationsE7int64_t) Set default max iteration number for the loop operator.


-
inline void set_limit_loop_iterations(int64_t value)
[#](#_CPPv4N8migraphx12onnx_options25set_limit_loop_iterationsE7int64_t) Set max iteration limit for the loop operator.


-
inline void set_external_data_path(const std::string &external_data_path)
[#](#_CPPv4N8migraphx12onnx_options22set_external_data_pathERKNSt6stringE) Set absolute path for external data files.


-
inline onnx_options()

-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::parse_onnx(const char *filename)[#](#_CPPv4N8migraphx10parse_onnxEPKc) Parse an onnx file into a migraphx program.


-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::parse_onnx(const char *filename, const migraphx::[onnx_options](#_CPPv4N8migraphx12onnx_optionsE)&options)[#](#_CPPv4N8migraphx10parse_onnxEPKcRKN8migraphx12onnx_optionsE) Parse an onnx file into a migraphx program.


-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::parse_onnx_buffer(const std::string &buffer)[#](#_CPPv4N8migraphx17parse_onnx_bufferERKNSt6stringE) Parse a buffer of memory as an onnx file.


-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::parse_onnx_buffer(const std::string &buffer, const migraphx::[onnx_options](#_CPPv4N8migraphx12onnx_optionsE)&options)[#](#_CPPv4N8migraphx17parse_onnx_bufferERKNSt6stringERKN8migraphx12onnx_optionsE) Parse a buffer of memory as an onnx file.


-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::parse_onnx_buffer(const void *data, size_t size)[#](#_CPPv4N8migraphx17parse_onnx_bufferEPKv6size_t) Parse a buffer of memory as an onnx file.


-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::parse_onnx_buffer(const void *data, size_t size, const migraphx::[onnx_options](#_CPPv4N8migraphx12onnx_optionsE)&options)[#](#_CPPv4N8migraphx17parse_onnx_bufferEPKv6size_tRKN8migraphx12onnx_optionsE) Parse a buffer of memory as an onnx file.


## load[#](#load)

-
struct file_options : public migraphx::handle_base<>
[#](#_CPPv4N8migraphx12file_optionsE) Public Functions

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<
[HandleType](#_CPPv4I000EN8migraphx12file_options12file_optionsEP10HandleType8Lifetime)*, handle_type*>{}>::type>

inline file_options([HandleType](#_CPPv4I000EN8migraphx12file_options12file_optionsEP10HandleType8Lifetime)*p,[Lifetime](#_CPPv4I000EN8migraphx12file_options12file_optionsEP10HandleType8Lifetime)lifetime)[#](#_CPPv4I000EN8migraphx12file_options12file_optionsEP10HandleType8Lifetime)

-
inline file_options()
[#](#_CPPv4N8migraphx12file_options12file_optionsEv)

-
inline void set_file_format(const char *format)
[#](#_CPPv4N8migraphx12file_options15set_file_formatEPKc)

-
template<class HandleType, class Lifetime, class = typename std::enable_if<std::is_convertible<

-
inline
[program](#_CPPv4N8migraphx7programE)migraphx::load(const char *filename, const[file_options](#_CPPv4N8migraphx12file_optionsE)&options)[#](#_CPPv4N8migraphx4loadEPKcRK12file_options) Load a saved migraphx program from a file.


## save[#](#save)

-
inline void migraphx::save(const
[program](#_CPPv4N8migraphx7programE)&p, const char *filename, const[file_options](#_CPPv4N8migraphx12file_optionsE)&options)[#](#_CPPv4N8migraphx4saveERK7programPKcRK12file_options) Save a program to a file.
