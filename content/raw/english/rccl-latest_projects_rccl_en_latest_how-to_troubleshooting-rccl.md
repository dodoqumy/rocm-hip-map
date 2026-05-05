---
title: "Troubleshooting RCCL &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/how-to/troubleshooting-rccl.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:42.884133+00:00
content_hash: "ac284e8f1799e759"
---

# Troubleshooting RCCL[#](#troubleshooting-rccl)

This topic explains the steps to troubleshoot functional and performance issues with RCCL. While debugging, collect the output from the commands in this guide. This data can be used as supporting information when submitting an issue report to AMD.

## Collecting system information[#](#collecting-system-information)

Collect this information about the ROCm version, GPU/accelerator, platform, and configuration.

Verify the ROCm version. This might be a release version or a mainline or staging version. Use this command to display the version:

`/opt/rocm/.info/version`

Run the following command and collect the output:

Also, collect the name of the GPU or accelerator:

Run these

`amd-smi`

commands to display the system topology.topology amd-smi static --driver amd-smi firmware amd-smi xgmi

Determine the values of the

`PATH`

and`LD_LIBRARY_PATH`

environment variables.echo $PATH echo $LD_LIBRARY_PATH

Collect the HIP configuration.

`--full`

Verify the network settings and setup. Use the

`ibv_devinfo`

command to display information about the available RDMA devices and determine whether they are installed and functioning properly. Run`rdma link`

to print a summary of the network links.`link`


### Isolating the issue[#](#isolating-the-issue)

The problem might be a general issue or specific to the architecture or system. To narrow down the issue, collect information about the GPU or accelerator and other details about the platform and system. Some issues to consider include:

Is ROCm running on:

A bare-metal setup

In a Docker container (determine the name of the Docker image)

In an SR-IOV virtualized

Some combination of these configurations


Is the problem only seen on a specific GPU architecture?

Is it only seen on a specific system type?

Is it happening on a single node or multinode setup?

Use the following troubleshooting techniques to attempt to isolate the issue.

Build or run the develop branch version of RCCL and see if the problem persists.

Try an earlier RCCL version (minor or major).

If you recently changed the ROCm runtime configuration, AMD Kernel-mode GPU Driver (KMD), or compiler, rerun the test with the previous configuration.



## Collecting RCCL information[#](#collecting-rccl-information)

Collect the following information about the RCCL installation and configuration.

Run the

`ldd`

command to list any dynamic dependencies for RCCL.`<specify-path-to-librccl.so>`

Determine the RCCL version. This might be the pre-packaged component in

`/opt/rocm/lib`

or a version that was built from source. To verify the RCCL version, enter the following command, then run either rccl-tests or an e2e application.export NCCL_DEBUG=VERSION

Run rccl-tests and collect the results. For information on how to build and run rccl-tests, see the

[rccl-tests GitHub](https://github.com/ROCm/rccl-tests/blob/develop/README.md).Collect the RCCL logging information. Enable the debug logs, then run rccl-tests or any e2e workload to collect the logs. Use the following command to enable the logs.

export NCCL_DEBUG=INFO


### Using the RCCL Replayer[#](#using-the-rccl-replayer)

The RCCL Replayer is a debugging tool designed to analyze and replay the collective logs obtained from RCCL runs.
It can be helpful when trying to reproduce problems, because it uses dummy data and doesn’t have any dependencies
on non-RCCL calls. For more information,
see [RCCL Replayer GitHub documentation](https://github.com/ROCm/rccl/tree/develop/tools/RcclReplayer).

You must build the RCCL Replayer before you can use it. To build it, run these commands. Ensure `MPI_DIR`

is set to
the path where MPI is installed.

```
cd rccl/tools/rccl_replayer
MPI_DIR=/path/to/mpi make
```

To use the RCCL Replayer, follow these steps:

Collect the per-rank logs from the RCCL run by adding the following environment variables. This prevents any race conditions that might cause ranks to interrupt the output from other ranks.

NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=COLL NCCL_DEBUG_FILE=some_name_here.%h.%p.log

Combine all the logs into a single file. This will become the input to the RCCL Replayer.

some_name_here_*.log > some_name_here.log

Run the RCCL Replayer using the following command. Replace

`<numProcesses>`

with the number of MPI processes to run,`</path/to/logfile>`

with the path to the collective log file generated during the RCCL runs, and`<numGpusPerMpiRank>`

with the number of GPUs per MPI rank used in the application.-np <numProcesses> ./rcclReplayer </path/to/logfile> <numGpusPerMpiRank>

In a multi-node application environment, you can replay the collective logs on multiple nodes using the following command:

--hostfile <path/to/hostfile.txt> -np <numProcesses> ./rcclReplayer </path/to/logfile> <numGpusPerMpiRank>

Note

Depending on the MPI library you’re using, you might need to modify the

`mpirun`

command.

## Analyzing performance issues[#](#analyzing-performance-issues)

If the issues involve performance issues in an e2e workload, try the following microbenchmarks and collect the results. Follow the instructions in the subsequent sections to run these benchmarks and provide the results to the support team.

TransferBench

RCCL Unit Tests

rccl-tests


### Collect the TransferBench data[#](#collect-the-transferbench-data)

TransferBench allows you to benchmark simultaneous copies between
user-specified devices. For more information,
see the [TransferBench documentation](https://rocm.docs.amd.com/projects/TransferBench/en/latest/index.html).

To collect the TransferBench data, follow these steps:

Clone the TransferBench Git repository.

clone https://github.com/ROCm/TransferBench.git

Change to the new directory and build the component.

cd TransferBench make

Run the TransferBench utility with the following parameters and save the results.

USE_FINE_GRAIN=1 GFX_UNROLL=2 ./TransferBench a2a 64M 8


### Collect the RCCL microbenchmark data[#](#collect-the-rccl-microbenchmark-data)

To use the RCCL tests to collect the RCCL benchmark data, follow these steps:

Disable NUMA auto-balancing using the following command:

sysctl kernel.numa_balancing=0

Run the following command to verify the setting. The expected output is

`0`

.`/proc/sys/kernel/numa_balancing`

Build MPI, RCCL, and rccl-tests. To download and install MPI, see either

[OpenMPI](https://www.open-mpi.org/software/ompi/v5.0/)or[MPICH](https://www.mpich.org/). To learn how to build and run rccl-tests, see the[rccl-tests GitHub](https://github.com/ROCm/rccl-tests/blob/develop/README.md).Run rccl-tests with MPI and collect the performance numbers.


## RCCL and NCCL comparisons[#](#rccl-and-nccl-comparisons)

If you are also using NVIDIA hardware or NCCL and notice a performance gap between the two systems, collect the system and performance data on the NVIDIA platform. Provide both sets of data to the support team.
