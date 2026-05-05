---
title: "Program"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/program.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:00.317281+00:00
content_hash: "80d73ab0b28dd862"
---

# Program[#](#program)

2025-10-14

6 min read time

## instruction[#](#instruction)

-
struct instruction
[#](#_CPPv4N8migraphx8internal11instructionE) Public Functions

-
inline instruction()
[#](#_CPPv4N8migraphx8internal11instruction11instructionEv)

-
instruction(
[operation](operators.html#_CPPv4N8migraphx8internal9operationE)o,[shape](data.html#_CPPv4N8migraphx8internal5shapeE)r, std::vector<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> args)[#](#_CPPv4N8migraphx8internal11instruction11instructionE9operation5shapeNSt6vectorI15instruction_refEE)

-
instruction(
[operation](operators.html#_CPPv4N8migraphx8internal9operationE)o,[shape](data.html#_CPPv4N8migraphx8internal5shapeE)r, std::vector<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> args, std::vector<module_ref> modules)[#](#_CPPv4N8migraphx8internal11instruction11instructionE9operation5shapeNSt6vectorI15instruction_refEENSt6vectorI10module_refEE)

-
void recompute_shape()
[#](#_CPPv4N8migraphx8internal11instruction15recompute_shapeEv)

-
void clear_arguments()
[#](#_CPPv4N8migraphx8internal11instruction15clear_argumentsEv)

-
bool valid(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)start, bool check_order = false) const[#](#_CPPv4NK8migraphx8internal11instruction5validE15instruction_refb)

-
bool valid() const
[#](#_CPPv4NK8migraphx8internal11instruction5validEv)

-
std::string name() const
[#](#_CPPv4NK8migraphx8internal11instruction4nameEv)

-
const std::vector<
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> &inputs() const[#](#_CPPv4NK8migraphx8internal11instruction6inputsEv)

-
const std::vector<module_ref> &module_inputs() const
[#](#_CPPv4NK8migraphx8internal11instruction13module_inputsEv)

-
const std::vector<
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> &outputs() const[#](#_CPPv4NK8migraphx8internal11instruction7outputsEv) Where this instruction is used as an input to another instruction.


-
void add_output(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins)[#](#_CPPv4N8migraphx8internal11instruction10add_outputE15instruction_ref)

-
bool can_eval() const
[#](#_CPPv4NK8migraphx8internal11instruction8can_evalEv)

-
bool is_undefined() const
[#](#_CPPv4NK8migraphx8internal11instruction12is_undefinedEv)

-
void finalize(context &ctx)
[#](#_CPPv4N8migraphx8internal11instruction8finalizeER7context)

-
void set_normalized(bool value = true)
[#](#_CPPv4N8migraphx8internal11instruction14set_normalizedEb)

-
bool is_normalized() const
[#](#_CPPv4NK8migraphx8internal11instruction13is_normalizedEv)

-
bool need_normalization() const
[#](#_CPPv4NK8migraphx8internal11instruction18need_normalizationEv)

-
std::size_t get_target_id() const
[#](#_CPPv4NK8migraphx8internal11instruction13get_target_idEv)

-
void set_target_id(std::size_t tid)
[#](#_CPPv4N8migraphx8internal11instruction13set_target_idENSt6size_tE)

-
void debug_print() const
[#](#_CPPv4NK8migraphx8internal11instruction11debug_printEv)

Public Static Functions

-
static void replace_refs(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins, const std::unordered_map<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE),[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> &map_insts, const std::unordered_map<module_ref, module_ref> &map_mods)[#](#_CPPv4N8migraphx8internal11instruction12replace_refsE15instruction_refRKNSt13unordered_mapI15instruction_ref15instruction_refEERKNSt13unordered_mapI10module_ref10module_refEE)

-
static void backreference(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ref)[#](#_CPPv4N8migraphx8internal11instruction13backreferenceE15instruction_ref)

-
static void replace_argument(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins,[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)old,[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)new_ins)[#](#_CPPv4N8migraphx8internal11instruction16replace_argumentE15instruction_ref15instruction_ref15instruction_ref)

-
static void replace_mod_argument(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins, module_ref old, module_ref new_mod)[#](#_CPPv4N8migraphx8internal11instruction20replace_mod_argumentE15instruction_ref10module_ref10module_ref)

-
static void replace(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins,[operation](operators.html#_CPPv4N8migraphx8internal9operationE)o, const[shape](data.html#_CPPv4N8migraphx8internal5shapeE)&r, std::vector<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> args)[#](#_CPPv4N8migraphx8internal11instruction7replaceE15instruction_ref9operationRK5shapeNSt6vectorI15instruction_refEE)

-
static void replace(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins,[operation](operators.html#_CPPv4N8migraphx8internal9operationE)o, const[shape](data.html#_CPPv4N8migraphx8internal5shapeE)&r, std::vector<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)> args, std::vector<module_ref> module_args)[#](#_CPPv4N8migraphx8internal11instruction7replaceE15instruction_ref9operationRK5shapeNSt6vectorI15instruction_refEENSt6vectorI10module_refEE)

-
static
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)get_output_alias([instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins, bool shallow = false)[#](#_CPPv4N8migraphx8internal11instruction16get_output_aliasE15instruction_refb)

-
static void print(std::ostream &os,
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins, const std::unordered_map<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE), std::string> &names)[#](#_CPPv4N8migraphx8internal11instruction5printERNSt7ostreamE15instruction_refRKNSt13unordered_mapI15instruction_refNSt6stringEEE)

Friends

-
friend bool operator==(const
[instruction](#_CPPv4N8migraphx8internal11instructionE)&i,[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ref)[#](#_CPPv4N8migraphx8internal11instructioneqERK11instruction15instruction_ref)

-
friend bool operator==(const
[instruction](#_CPPv4N8migraphx8internal11instructionE)&x, const[instruction](#_CPPv4N8migraphx8internal11instructionE)&y)[#](#_CPPv4N8migraphx8internal11instructioneqERK11instructionRK11instruction)

-
friend bool operator!=(const
[instruction](#_CPPv4N8migraphx8internal11instructionE)&x, const[instruction](#_CPPv4N8migraphx8internal11instructionE)&y)[#](#_CPPv4N8migraphx8internal11instructionneERK11instructionRK11instruction)

-
friend bool operator==(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ref, const[instruction](#_CPPv4N8migraphx8internal11instructionE)&i)[#](#_CPPv4N8migraphx8internal11instructioneqE15instruction_refRK11instruction)

-
friend bool operator!=(const
[instruction](#_CPPv4N8migraphx8internal11instructionE)&i,[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ref)[#](#_CPPv4N8migraphx8internal11instructionneERK11instruction15instruction_ref)

-
friend bool operator!=(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ref, const[instruction](#_CPPv4N8migraphx8internal11instructionE)&i)[#](#_CPPv4N8migraphx8internal11instructionneE15instruction_refRK11instruction)

-
inline instruction()

## instruction_ref[#](#instruction-ref)

-
type migraphx::internal::instruction_ref
[#](#_CPPv4N8migraphx8internal15instruction_refE) References an instruction in the program.


## program[#](#id1)

-
struct program
[#](#_CPPv4N8migraphx8internal7programE) Stores the instruction stream.

Public Functions

-
program()
[#](#_CPPv4N8migraphx8internal7program7programEv)

-
explicit program(module m)
[#](#_CPPv4N8migraphx8internal7program7programE6module)

-
~program() noexcept
[#](#_CPPv4N8migraphx8internal7programD0Ev)

-
std::vector<std::string> get_parameter_names() const
[#](#_CPPv4NK8migraphx8internal7program19get_parameter_namesEv)

-
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)get_parameter(std::string name) const[#](#_CPPv4NK8migraphx8internal7program13get_parameterENSt6stringE)

-
std::size_t total_instructions() const
[#](#_CPPv4NK8migraphx8internal7program18total_instructionsEv)

-
std::vector<
[argument](data.html#_CPPv4N8migraphx8internal8argumentE)> eval(const parameter_map ¶ms, execution_environment exec_env = execution_environment{}) const[#](#_CPPv4NK8migraphx8internal7program4evalERK13parameter_map21execution_environment)

-
std::vector<
[argument](data.html#_CPPv4N8migraphx8internal8argumentE)> eval_with_context(std::vector<context> &ctx, const parameter_map ¶ms) const[#](#_CPPv4NK8migraphx8internal7program17eval_with_contextERNSt6vectorI7contextEERK13parameter_map)

-
void finish() const
[#](#_CPPv4NK8migraphx8internal7program6finishEv)

-
std::size_t size() const
[#](#_CPPv4NK8migraphx8internal7program4sizeEv)

-
context &get_context() const
[#](#_CPPv4NK8migraphx8internal7program11get_contextEv)

-
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)validate() const[#](#_CPPv4NK8migraphx8internal7program8validateEv)

-
target_assignments get_target_assignments(const std::vector<
[target](targets.html#_CPPv4N8migraphx8internal6targetE)> &targets, assignment_options options = assignment_options{})[#](#_CPPv4N8migraphx8internal7program22get_target_assignmentsERKNSt6vectorI6targetEE18assignment_options)

-
bool is_compiled() const
[#](#_CPPv4NK8migraphx8internal7program11is_compiledEv)

-
void finalize()
[#](#_CPPv4N8migraphx8internal7program8finalizeEv)

-
void perf_report(std::ostream &os, std::size_t n, parameter_map params, std::size_t batch = 1, bool detailed = false) const
[#](#_CPPv4NK8migraphx8internal7program11perf_reportERNSt7ostreamENSt6size_tE13parameter_mapNSt6size_tEb)

-
void mark(const parameter_map ¶ms, marker m)
[#](#_CPPv4N8migraphx8internal7program4markERK13parameter_map6marker)

-
void debug_print() const
[#](#_CPPv4NK8migraphx8internal7program11debug_printEv)

-
void debug_print(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins) const[#](#_CPPv4NK8migraphx8internal7program11debug_printE15instruction_ref)

-
void print(std::unordered_map<
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE), std::string> &names, const std::function<void([instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE), std::unordered_map<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE), std::string>)> &print_func) const[#](#_CPPv4NK8migraphx8internal7program5printERNSt13unordered_mapI15instruction_refNSt6stringEEERKNSt8functionIFv15instruction_refNSt13unordered_mapI15instruction_refNSt6stringEEEEEE)

-
void print(const std::function<void(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE)ins, std::unordered_map<[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE), std::string>)> &print_func) const[#](#_CPPv4NK8migraphx8internal7program5printERKNSt8functionIFv15instruction_refNSt13unordered_mapI15instruction_refNSt6stringEEEEEE)

-
void print_graph(std::ostream &os, bool brief = false) const
[#](#_CPPv4NK8migraphx8internal7program11print_graphERNSt7ostreamEb)

-
void print_py(std::ostream &os) const
[#](#_CPPv4NK8migraphx8internal7program8print_pyERNSt7ostreamE)

-
void print_cpp(std::ostream &os) const
[#](#_CPPv4NK8migraphx8internal7program9print_cppERNSt7ostreamE)

-
void dry_run(const parameter_map ¶ms) const
[#](#_CPPv4NK8migraphx8internal7program7dry_runERK13parameter_map)

-
void annotate(std::ostream &os, const std::function<void(
[instruction_ref](#_CPPv4N8migraphx8internal15instruction_refE))> &a) const[#](#_CPPv4NK8migraphx8internal7program8annotateERNSt7ostreamERKNSt8functionIFv15instruction_refEEE)

-
module *create_module(const std::string &name)
[#](#_CPPv4N8migraphx8internal7program13create_moduleERKNSt6stringE)

-
module *create_module(const std::string &name, module m)
[#](#_CPPv4N8migraphx8internal7program13create_moduleERKNSt6stringE6module)

-
module *get_module(const std::string &name)
[#](#_CPPv4N8migraphx8internal7program10get_moduleERKNSt6stringE)

-
const module *get_module(const std::string &name) const
[#](#_CPPv4NK8migraphx8internal7program10get_moduleERKNSt6stringE)

-
module *get_main_module()
[#](#_CPPv4N8migraphx8internal7program15get_main_moduleEv)

-
const module *get_main_module() const
[#](#_CPPv4NK8migraphx8internal7program15get_main_moduleEv)

-
std::vector<const module*> get_modules() const
[#](#_CPPv4NK8migraphx8internal7program11get_modulesEv)

-
std::vector<module*> get_modules()
[#](#_CPPv4N8migraphx8internal7program11get_modulesEv)

-
std::unordered_multimap<module_ref, module_ref> get_module_tree()
[#](#_CPPv4N8migraphx8internal7program15get_module_treeEv)

-
void remove_module(const std::string &name)
[#](#_CPPv4N8migraphx8internal7program13remove_moduleERKNSt6stringE)

-
void rename_module(const std::string &old_name, const std::string &new_name)
[#](#_CPPv4N8migraphx8internal7program13rename_moduleERKNSt6stringERKNSt6stringE)

-
void remove_unused_modules()
[#](#_CPPv4N8migraphx8internal7program21remove_unused_modulesEv)

-
program()

## parse_onnx[#](#parse-onnx)

-
[program](#_CPPv4N8migraphx8internal7programE)migraphx::internal::parse_onnx(const std::string &name, const[onnx_options](#_CPPv4N8migraphx8internal12onnx_optionsE)& =[onnx_options](#_CPPv4N8migraphx8internal12onnx_optionsE){})[#](#_CPPv4N8migraphx8internal10parse_onnxERKNSt6stringERK12onnx_options) Create a program from an onnx file.


## parse_tf[#](#parse-tf)

-
[program](#_CPPv4N8migraphx8internal7programE)migraphx::internal::parse_tf(const std::string &name, const[tf_options](#_CPPv4N8migraphx8internal10tf_optionsE)&options =[tf_options](#_CPPv4N8migraphx8internal10tf_optionsE){})[#](#_CPPv4N8migraphx8internal8parse_tfERKNSt6stringERK10tf_options) Create a program from a tf pb file (default is nhwc format)


## onnx_options[#](#onnx-options)

-
struct onnx_options
[#](#_CPPv4N8migraphx8internal12onnx_optionsE) struct to pass in onnx options to parser


## tf_options[#](#tf-options)

-
struct tf_options
[#](#_CPPv4N8migraphx8internal10tf_optionsE) struct to pass in tf options to parser
