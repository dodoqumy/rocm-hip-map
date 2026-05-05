---
title: "Using rocprofv3-avail &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3-avail.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:37.895576+00:00
content_hash: "bbc492a9e0420cce"
---

# Using rocprofv3-avail[#](#using-rocprofv3-avail)

`rocprofv3-avail`

is a CLI tool that helps you to query the features supported by the hardware and Rocprofiler SDK.

The following sections demonstrate the use of `rocprofv3-avail`

for querying features using various command-line options.

`rocprofv3-avail`

is installed with ROCm under `/opt/rocm/bin`

. To use the tool from anywhere in the system, export `PATH`

variable:

```
export PATH=$PATH:/opt/rocm/bin
```

## Command-line options[#](#command-line-options)

The following table lists `rocprofv3-avail`

command-line options categorized according to their purpose.

Purpose |
Option |
Description |
|---|---|---|
avail-aptions commands |
`info` `list` `pmc-check` |
Info options for detailed information of counters, agents, and pc-sampling configurations.
List options for hardware counters, agents and pc-sampling support.
Checking if a set of counters can be collected together on agent.
|

```
list
```

The preceding command generates an output listing agents and hardware counters.

```
list --agent
```

The preceding command generates an output listing basic info for all agents, if used with `-d`

, only basic info for device `-d`

is listed.
Following is the sample output

```
list --pmc
```

The preceding command generates an output listing counters for all agents, if used with `-d`

, only counters on the `-d`

device is listed.
Output contains following information: logical node id, name and list of PMC counters supported on the agent.

```
list --pc-sampling
```

The preceding command generates an output listing agents that supports any kind of PC Sampling. `-d`

option is not applicable here.

```
info
```

The preceding command generates an output with agent information and listing all counters supported on each agent.

```
info --pmc
```

The preceding command generates an output with the pmc info, if used with `-d`

information of pmc for device `-d`

is generated.
Output includes the following information: logical node id, name, counter_name, description of the counter, dimensions, block/expression for every counter.

```
info --pc-sampling
```

The preceding command generates list of supported PC sampling configurations for each agent that supports PC sampling. `-d`

option is not applicable here.
Output has following information: logical node id, method supported, unit, minimum sampling interval, maximum sampling interval
flags.

```
pmc-check [pmc [pmc...]]
```

The preceding command checks if the pmc can be collected together

```
pmc-check -d 0 <pmc1> <pmc2> <pmc3>:device=1
```

The preceding command checks if the pmc1 and pmc2 can be collected together on agent 0 and pmc3 on agent 1

Note

All commands writes to the standard output.
