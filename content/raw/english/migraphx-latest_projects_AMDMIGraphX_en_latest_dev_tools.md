---
title: "Tools"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/dev/tools.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:04.041015+00:00
content_hash: "1415e5f16bf383cd"
---

# Tools[#](#tools)

2025-11-22

2 min read time

## roctx.py[#](#roctx-py)

You can use the [roctx](../reference/driver-options.html#roctx) command with rocprof binary to get marker timing information for each MIGraphX operator.
To process timing information, use `roctx.py`

helper script.

```
Usage: roctx.py [-h] [--json-path json_path] [--out out]
[--study-name study-name] [--repeat repeat] [--parse]
[--run run] [--debug]
```

The `roctx.py`

helper script provides two main functionalities: `run`

and `parse`

.

-
--run
[#](#cmdoption-run)

Runs `migraphx-driver roctx`

command with the given `migraphx-driver`

knobs followed by the parsing of the result which provides GPU kernel timing information.
You can pass the MIGraphX knobs via a string to –run knob. See the _roctx-examples for usage.

-
--parse
[#](#cmdoption-parse)

Parses JSON file in the given `--json-path`

and provides GPU kernel timing information.

-
--out
[#](#cmdoption-out)

Output folder

-
--study-name
[#](#cmdoption-study-name)

Optional. Allows user to name a study for easy interpretation. Defaults to timestamp.

-
--repeat
[#](#cmdoption-repeat)

Number of iterations. Sets to **2** by default.

-
--debug
[#](#cmdoption-debug)

Provides additional debug information related to data. Use for debugging purposes only.

**Examples:**

**Running inference with rocTX for a given ONNX file:**

```
python roctx.py --run '--onnx --gpu fcn-resnet50-11.onnx' --out output_folder --repeat 5
```

Example output:

Hotspot kernel timing information:

The output provides `SUM`

, `MIN`

, `MAX`

and `COUNT`

information for each kernel executed for a given model. It also
provides the average total time. The following three files are provided for reference:

OUTPUT CSV FILE: Provides a summary of the run which includes utilized MIGraphX knobs and related kernel timing information.

KERNEL TIMING DETAILS: Provides the hotspot kernel timing information.

ALL DATA FROM ALL RUNS: Provides all output data related to all iterations executed during a run.


**Parsing an existing JSON file:**

```
python roctx.py --parse --json-path ../trace.json
```
