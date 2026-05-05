---
title: "MIGraphX Python API reference"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/reference/MIGraphX-py.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:08.294909+00:00
content_hash: "82b93c35c9de88bb"
---

# MIGraphX Python API reference[#](#migraphx-python-api-reference)

2025-10-14

8 min read time

## shape[#](#shape)

-
*class*migraphx.shape(*type*,*lens*,*strides=None*,*dyn_dims*)[#](#migraphx.shape) Describes the shape of a tensor. This includes size, layout, and data type. Use dyn_dims for a dynamic shape.


-
migraphx.dyn_dims()
[#](#migraphx.dyn_dims) The dynamic dimensions of the shape.

- Return type:


-
migraphx.standard()
[#](#migraphx.standard) Returns true if the shape is a standard shape. That is, the shape is both packed and not transposed.

- Return type:


## dynamic_dimension[#](#dynamic-dimension)

-
*class*migraphx.dynamic_dimension(*min*,*max*,*optimals*)[#](#migraphx.dynamic_dimension) Constructs a dynamic_dimension from a minimum, a maximum, and optionally a set of optimals.


-
migraphx.is_fixed()
[#](#migraphx.is_fixed) Returns true if the dynamic_dimension is fixed.

:rtype : int


## argument[#](#argument)

-
*class*migraphx.argument(*data*)[#](#migraphx.argument) Constructs an argument from a python buffer. This can include numpy arrays.


-
migraphx.generate_argument(
*s*,*seed=0*)[#](#migraphx.generate_argument) Generates an argument with random data.


-
migraphx.fill_argument(
*s*,*value*)[#](#migraphx.fill_argument) Fills argument of shape s with the given value.


-
migraphx.create_argument(
*s*,*values*)[#](#migraphx.create_argument) Creates an argument of shape s with a set of values.


-
migraphx.argument_from_pointer(
*shape*,*address*)[#](#migraphx.argument_from_pointer) Creates argument from data stored in given address without copy.


-
*static*argument.save(*arg*,*filename*)[#](#migraphx.argument.save) Saves argument to a file encoded in msgpack format.


## target[#](#target)

-
*class*migraphx.target[#](#migraphx.target) This represents the compilation target.


## module[#](#module)

-
migraphx.print()
[#](#migraphx.print) Prints the contents of the module as list of instructions.


-
migraphx.add_instruction(
*op*,*args*,*mod_args=[]*)[#](#migraphx.add_instruction) Adds instruction into the module.

- Parameters:

:rtype instruction


-
migraphx.add_literal(
*data*)[#](#migraphx.add_literal) Adds constant or literal data of provided shape into the module from python buffer which includes numpy array.

- Parameters:
**data**(*py::buffer*) – Python buffer or numpy array

:rtype instruction


-
migraphx.add_parameter(
*name*,*shape*)[#](#migraphx.add_parameter) Adds a parameter to the module with the provided name and shape.

:rtype instruction


## program[#](#program)

-
*class*migraphx.program[#](#migraphx.program) Represents the computation graph to be compiled and run.


-
migraphx.get_parameter_names()
[#](#migraphx.get_parameter_names) Gets all the input argument’s or parameter’s names to the program as a list.

:rtype list[str]


-
migraphx.get_parameter_shapes()
[#](#migraphx.get_parameter_shapes) Gets the shapes of all the input parameters in the program.


-
migraphx.get_output_shapes()
[#](#migraphx.get_output_shapes) Gets the shapes of the final outputs of the program.


-
migraphx.compile(
*t*,*offload_copy=True*,*fast_math=True*,*exhaustive_tune=False*)[#](#migraphx.compile) Compiles the program for the target and optimizes it.

- Parameters:
**t**() – Compilation target for the program.*target***offload_copy**() – For targets with offloaded memory(such as the gpu), this will insert instructions during compilation to copy the input parameters to the offloaded memory and to copy the final result from the offloaded memory back to main memory.*bool***fast_math**() – Optimize math functions to use faster approximate versions. There may be slight accuracy degredation when enabled.*bool***exhaustive_tune**– Flag to enable exhaustive search to find the fastest version of generated kernels for selected backend.



-
migraphx.get_main_module()
[#](#migraphx.get_main_module) Gets main module of the program.

:rtype module


-
migraphx.create_module(
*name*)[#](#migraphx.create_module) Creates and adds a module with the provided name into the program.

:param str name : name of the new module. :rtype module


-
migraphx.run(
*params*)[#](#migraphx.run) Runs the program.


-
migraphx.sort()
[#](#migraphx.sort) Sorts the modules of the program for the instructions to appear in topologically sorted order.


-
migraphx.quantize_fp16(
*prog*,*ins_names=['all']*)[#](#migraphx.quantize_fp16) Quantizes the program to use fp16.


-
migraphx.quantize_bf16(
*prog*,*ins_names=['all']*)[#](#migraphx.quantize_bf16) Quantizes the program to use bf16.


-
migraphx.quantize_int8(
*prog*,*t*,*calibration=[]*,*ins_names=['dot', 'convolution']*)[#](#migraphx.quantize_int8) Quantizes the program to use int8.


## op[#](#op)

## parse_onnx[#](#parse-onnx)

-
migraphx.parse_onnx(
*filename*,*default_dim_value=1*,*map_input_dims={}*,*skip_unknown_operators=false*,*print_program_on_error=false*,*max_loop_iterations=10*,*limit_max_iterations=65535*)[#](#migraphx.parse_onnx) Loads and parses an ONNX file.

- Parameters:
**filename**() – Path to file.*str***default_dim_value**() – default dimension to use (if not specified in onnx file).*str***default_dyn_dim_value**() – default dynamic_dimension value to use.*dynamic_dimension***map_input_dims**() – Explicitly specify the dims of an input.*str***map_dyn_input_dims**(*list**[**dynamic_dimension**]*) – Explicitly specify the dynamic_dimensions of an input.**skip_unknown_operators**() – Continue parsing onnx file if an unknown operator is found.*str***print_program_on_error**() – Print program if an error occurs.*str***max_loop_iterations**() – Maximum iteration number for the loop operator if trip count is not set.*int***limit_max_iterations**() – Maximum iteration limit for the loop operator.*int*

- Return type:


## parse_tf[#](#parse-tf)

-
migraphx.parse_tf(
*filename*,*is_nhwc=True*,*batch_size=1*,*map_input_dims=dict()*,*output_names=[]*)[#](#migraphx.parse_tf) Loads and parses a tensorflow protobuf file.

- Parameters:
**filename**() – Path to file.*str***is_nhwc**() – Use nhwc as default format.*bool***batch_size**() – default batch size to use (if not specified in protobuf).*str***map_input_dims**(*dict**[**str**,**list**[**int**]**]*) – Optional arg to explictly specify dimensions of the inputs.**output_names**(*list**[**str**]*) – Optional argument specify names of the output nodes.

- Return type:
