---
title: "ROCprofiler-SDK Quick Reference Guide &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/quick_guide.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:15:27.795901+00:00
content_hash: "90acaa537015ebc6"
---

# ROCprofiler-SDK Quick Reference Guide[#](#rocprofiler-sdk-quick-reference-guide)

This quick reference guide provides an overview of the most commonly used `rocprofv3`

commands and links to detailed documentation sections.

## Getting Started[#](#getting-started)

Export the ROCm binary path:

```
source /opt/rocm/share/rocprofiler-sdk/setup-env.sh
```

Check rocprofv3 version and help:

```
--version
rocprofv3 --help
```

## Essential Commands[#](#essential-commands)

### Querying System Capabilities[#](#querying-system-capabilities)

List available counters and capabilities:

```
# List all available features
rocprofv3 --list-avail
# Using the dedicated tool for detailed queries
rocprofv3-avail list
rocprofv3-avail info
```

**Documentation:** [Using rocprofv3-avail](how-to/using-rocprofv3-avail.html#using-rocprofv3-avail)

### Basic Tracing[#](#basic-tracing)

Application tracing (HIP API + kernel dispatches + memory operations):

```
# Runtime tracing (recommended for most use cases)
rocprofv3 --runtime-trace -- ./your_app
# System-level tracing (includes HSA API)
rocprofv3 --sys-trace -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3)

### Granular Tracing Options[#](#granular-tracing-options)

```
# HIP API, kernel dispatches, and memory operations tracing
rocprofv3 --hip-trace --kernel-trace --memory-copy-trace -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (Basic tracing section)

### Performance Counter Collection[#](#performance-counter-collection)

```
# List available counters
rocprofv3-avail list --pmc
# Check if counters can be collected together
rocprofv3-avail pmc-check SQ_WAVES SQ_INSTS_VALU
# Collect specific counters
rocprofv3 --pmc SQ_WAVES,SQ_INSTS_VALU -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (Counter collection section)

## Advanced Profiling Features[#](#advanced-profiling-features)

### PC Sampling (Beta)[#](#pc-sampling-beta)

```
# Check PC sampling support
rocprofv3-avail list --pc-sampling
# Enable PC sampling
rocprofv3 --pc-sampling-beta-enabled --pc-sampling-interval 1000 -- ./your_app
```

**Documentation:** [Using PC sampling](how-to/using-pc-sampling.html#using-pc-sampling)

### Thread Trace[#](#thread-trace)

```
# Collect thread trace data
rocprofv3 --att --output-format csv -- ./your_app
```

**Documentation:** [Using thread trace](how-to/using-thread-trace.html#using-thread-trace)

### Process Attachment[#](#process-attachment)

```
# Attach to a running process by PID
rocprofv3 --pid 12345 --runtime-trace -d ./results
# or
# Attach for a specific duration (10 seconds)
rocprofv3 --pid 12345 --runtime-trace --attach-duration-msec 1000
```

**Documentation:** using-rocprofv3-process-attachment

## Output Formats and Post-processing[#](#output-formats-and-post-processing)

rocprofv3 supports multiple output formats for different analysis needs. The default format is `rocpd`

, which stores data in a structured SQLite3 database.

### Working with rocpd Database Format[#](#working-with-rocpd-database-format)

```
# Generate rocpd database (default format)
rocprofv3 --runtime-trace -- ./your_app
# Creates: hostname/pid_results.db
# Query the database directly with SQL
sqlite3 hostname/12345_results.db "SELECT * FROM regions;"
# Convert rocpd database to other formats
rocpd convert -i *.db -f csv pftrace otf2 --start 20% --end 80%
```

### Collecting and converting to Other Formats[#](#collecting-and-converting-to-other-formats)

```
# Multiple output formats in one run
rocprofv3 --runtime-trace --output-format csv json pftrace otf2 -- ./your_app
```

**Documentation:** [Using rocpd output format](how-to/using-rocpd-output-format.html#using-rocpd-output-format)

### Summary and Statistics[#](#summary-and-statistics)

```
# Overall summary statistics per domain grouped by kernel and memory operations
rocprofv3 --runtime-trace --summary-per-domain --summary-groups "KERNEL_DISPATCH|MEMORY_COPY" -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (Post-processing tracing section)

## Filtering and Selection[#](#filtering-and-selection)

### Kernel Filtering[#](#kernel-filtering)

```
# Include specific kernels by regex
rocprofv3 --kernel-trace --kernel-iteration-range 10-20 --kernel-include-regex "matmul.*" --kernel-exclude-regex ".*copy.*" -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (Filtering section)

### Time-based Collection[#](#time-based-collection)

```
# Collect for specific time periods (start_delay:collection_time:repeat)
rocprofv3 --runtime-trace --collection-period 500:2000:0 --collection-period-unit msec -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (Filtering section)

## Kernel Naming and Display[#](#kernel-naming-and-display)

```
# Keep mangled kernel names
rocprofv3 --kernel-trace --mangled-kernels -- ./your_app
# Truncate kernel names for readability
rocprofv3 --kernel-trace --truncate-kernels -- ./your_app
# Use ROCTx regions to rename kernels
rocprofv3 --kernel-trace --kernel-rename -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (Kernel naming section)

## Code Annotation with ROCTx[#](#code-annotation-with-roctx)

```
# Trace ROCTx markers and ranges
rocprofv3 --marker-trace -- ./your_app
```

**Documentation:** [Using ROCTx](how-to/using-rocprofiler-sdk-roctx.html#using-rocprofiler-sdk-roctx)

## Parallel and Distributed Applications[#](#parallel-and-distributed-applications)

### MPI Applications[#](#mpi-applications)

```
# Profile MPI applications
mpirun -n 4 rocprofv3 --runtime-trace --output-format csv -- ./your_mpi_app
```

**Documentation:** [Using rocprofv3 with MPI](how-to/using-rocprofv3-with-mpi.html#using-rocprofv3-with-mpi)

### OpenMP Applications[#](#openmp-applications)

```
# Profile OpenMP applications
rocprofv3 --runtime-trace --output-format csv -- ./your_openmp_app
```

**Documentation:** [Using rocprofv3 with OpenMP](how-to/using-rocprofv3-with-openmp.html#using-rocprofv3-with-openmp)

## Output Management[#](#output-management)

### File Organization[#](#file-organization)

```
# Specify output directory
rocprofv3 --runtime-trace --output-directory ./results --output-file my_trace -- ./your_app
# Generate configuration file
rocprofv3 --runtime-trace --output-config -- ./your_app
```

**Documentation:** [Using rocprofv3](how-to/using-rocprofv3.html#using-rocprofv3) (I/O options section)

## Common Use Cases[#](#common-use-cases)

### Basic Performance Analysis[#](#basic-performance-analysis)

```
# Quick performance overview
rocprofv3 --runtime-trace --summary -- ./your_app
```

**Use case:** Get a high-level view of application performance

### Detailed Kernel Analysis[#](#detailed-kernel-analysis)

```
# Detailed kernel profiling with counters
rocprofv3 --kernel-trace --pmc SQ_WAVES,SQ_INSTS_VALU,TCP_PERF_SEL_TOTAL_CACHE_ACCESSES -- ./your_app
```

**Use case:** Analyze specific kernel performance bottlenecks

### Memory Transfer Analysis[#](#memory-transfer-analysis)

```
# Focus on memory operations
rocprofv3 --memory-copy-trace --memory-allocation-trace -- ./your_app
```

**Use case:** Optimize data movement between CPU and GPU

### Timeline Visualization[#](#timeline-visualization)

```
# Generate timeline for visualization tools
rocprofv3 --runtime-trace -- ./your_app
# Convert to Perfetto format
rocpd2pftrace -i hostname/pid_results.db -o perfetto_trace
```

**Use case:** Visualize execution timeline in Perfetto or similar tools

## Installation and Setup[#](#installation-and-setup)

**Installation Documentation:** [Installing ROCprofiler-SDK](install/installation.html#installing-rocprofiler-sdk)

**API Reference:** [Tool library](api-reference/tool_library.html)

**Samples and Examples:** [Samples](how-to/samples.html)

## Troubleshooting Quick Tips[#](#troubleshooting-quick-tips)

**Permission Issues:**Ensure proper access to GPU devices and`/dev/kfd`

**Counter Collection Fails:**Use`rocprofv3-avail pmc-check`

to verify counter compatibility**Large Output Files:**Use`--minimum-output-data`

to set file size thresholds**Signal Handling:**Use`--disable-signal-handlers`

if conflicts with application handlers**ROCm Path Issues:**Use`--rocm-root`

to specify custom ROCm installation paths

For comprehensive documentation on each feature, refer to the detailed sections linked throughout this guide.
