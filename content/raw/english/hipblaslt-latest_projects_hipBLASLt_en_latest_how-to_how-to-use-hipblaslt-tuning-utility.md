---
title: "Using the hipBLASLt tuning utility &#8212; hipBLASLt 1.2.2 Documentation"
source_url: "https://rocm.docs.amd.com/projects/hipBLASLt/en/latest/how-to/how-to-use-hipblaslt-tuning-utility.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:20:35.079440+00:00
content_hash: "709c5c2801b812bb"
---

# Using the hipBLASLt tuning utility[#](#using-the-hipblaslt-tuning-utility)

hipBLASLt includes a simple tuning utility that uses the existing kernel pools to search for the best solution for a given problem size.

## The template.yaml file[#](#the-template-yaml-file)

The `template.yaml`

file is found in the `utilities`

directory. Download and modify this file to use it as
input for the `find_exact.py`

script, as described below.

```
# Two steps, can comment out Bench or CreateLogic if you want to disable.
Bench:
ProblemType: # Same as the given problem type
ComputeDataType: s
ComputeInputDataType: s # Usually the same as DataTypeA and DataTypeB unless you are using mix precisions.
DataTypeA: s
DataTypeB: s
DataTypeC: s
DataTypeD: s
TransposeA: 0
TransposeB: 0
UseBias: False
TestConfig:
ColdIter: 20
Iter: 100 # You can change this to a larger value for a more stable result, but the executing time also increases.
AlgoMethod: "all" # Fixed value
RotatingBuffer: 512 # It's recommended to set this value larger than the cache size of the GPU.
TuningParameters:
# SplitK list control parameter example
# SplitK: [0, 4, 8] # [0] For disable
ProblemSizes:
- [128, 128, 128] # M, N, K
CreateLogic: {} # Fixed
```

## Running the tuning utility[#](#running-the-tuning-utility)

To run the tuning utility, use the `find_exact.py`

script, which is found in the `utilities`

directory.

Follow these steps to run the tuning:

Run the install script. See

[Building and installing hipBLASLt](../install/building-installing-hipblaslt.html#installation)for more details.Ensure the

`MatchTable.yaml`

file exists in the`build/release/library`

directory.Run the

`find_exact.py`

command with the following parameters:find_exact.py <your yaml file> <hipblaslt_root_folder>/build/release <output folder>

The utility generates a message like the one shown below. This example is for NN

`FP32`

tuning:benchmarks --Running size: result_NN_SSS_128x128x128.txt

After the tuning completes, the script generates the following summary:

exact logic --Reading matching table: <hipblaslt_root_folder>/build/release/library/MatchTable.yaml --Reading bench files --Found file <output folder>/0_Bench/result_NN_SSS_88x12x664.txt Writing logic yaml files: 100%| | 1/1 [00:05<00:00, 5.69s/it]

Review the results. The final structure of the output folder looks like this:

The

`0_Bench`

folder stores the raw benchmark results. The`1_LogicYaml`

folder stores the output, which is a tuned equality logic YAML file.
