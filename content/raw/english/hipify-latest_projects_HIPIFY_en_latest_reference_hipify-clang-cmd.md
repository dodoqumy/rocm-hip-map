---
title: "hipify-clang commands &#8212; HIPIFY Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIPIFY/en/latest/reference/hipify-clang-cmd.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:11:34.727075+00:00
content_hash: "6f233edc1f65be1c"
---

# hipify-clang commands[#](#hipify-clang-commands)

For a list of `hipify-clang`

options, run:

```
hipify-clang --help
```

## Output:[#](#output)

### Usage[#](#usage)

```
hipify-clang [options] <source0> [... <sourceN>]
```

### Options[#](#options)

|
|
|
Separator between |
|
Define |
|
Add directory to include search path |
|
Try to hipify as much as possible; ignores |
|
Defines the path to the parent folder for the |
|
Generate documentation in CSV format |
|
CUDA GPU architecture (e.g. sm_35); may be specified more than once |
|
Keep CUDA kernel launch syntax (default) |
|
CUDA installation path. The CUDA path is required for |
|
Enable default preprocessor behavior (synonymous with |
|
Documentation format: |
|
ROC documentation generation: |
|
Combine the |
|
Hipify HIP APIs that are experimentally supported, otherwise, the corresponding warnings will be emitted |
|
Additional argument to append to the compiler command line |
|
Additional argument to prepend to the compiler command line |
|
Display available options (Use |
|
Display list of available options (Use |
|
Transform CUDA kernel launch syntax to a regular HIP function call (overrides |
|
Modify input file in-place. This will overwrite the input file with the hipify output |
|
Generate documentation in Markdown format |
|
Translate to |
|
Don’t create a backup file for the hipified source |
|
Don’t write any translated output to stdout |
|
Don’t rely on undocumented features in code transformation |
|
Suppress warnings on undocumented features in code transformation |
|
Output filename |
|
Output directory |
|
Output directory for hipify-perl script |
|
Output directory for Python map |
|
Output filename for statistics |
|
Used to read a compile command database as described in |
|
Generate |
|
Print translation statistics. See |
|
Print translation statistics in a CSV file. See |
|
Generate |
|
Translate to |
|
Save temporary files |
|
Enable default preprocessor behavior by skipping undefined conditional blocks. This has the same effect as |
|
Temporary directory |
|
Show commands to run and use verbose output |
|
Display the version of this program |
|
Display the versions of the supported 3rd-party software |
|
Specify the file paths and names of one or more source files. These paths are looked up in the compile command database. If the path of a file is absolute, it needs to point into CMake’s source tree. If the path is relative, the current working directory needs to be in the CMake source tree and the file must be in a subdirectory of the current working directory. |

### Option uses:[#](#option-uses)

Common Options:




`--help`

: Displays the help message

`-o <file>`

: Specifies the output file for the converted source

`-I <dir>`

: Adds the specified directory to the include search paths

`--cuda-path=<path>`

: Specifies the path to the CUDA installation. Required

`--hip-path=<path>`

: Specifies the path to the HIP installation (optional; defaults to the ROCm installation path)

Preprocessor and Compilation Options:




`-D<macro>`

: Defines macros for the preprocessor

`-U<macro>`

: Undefines macros

`--save-temps`

: Keeps intermediate files generated during processing

Diagnostics and Debugging:




`-v`

: Enables verbose output to provide detailed diagnostic information

`--version`

: Displays the version of HIPIFY-Clang

`--show-progress`

: Displays progress during the translation process

`--print-stats`

|`--print-stats-csv`

: Prints statistics about the translation process (e.g., the number of functions or API calls converted) into either text or CSV form

Include and Exclude Rules:




`--exclude-path=<path>`

: Specifies paths to exclude from translation

`--include-path=<path>`

: Specifies paths to explicitly include during translation
