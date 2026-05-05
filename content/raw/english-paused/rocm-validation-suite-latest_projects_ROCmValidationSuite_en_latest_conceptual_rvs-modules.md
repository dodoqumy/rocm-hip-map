---
title: "ROCm Validation Suite modules &#8212; RVS 1.3.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/conceptual/rvs-modules.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:26:46.654807+00:00
content_hash: "bbc33f9f66245202"
---

# ROCm Validation Suite modules[#](#rocm-validation-suite-modules)

ROCm Validation Suite (RVS) is implemented as a set of modules each implementing a particular test functionality. Modules are invoked from one central place (aka Launcher), which is responsible for reading input (command line and test configuration file), loading and running appropriate modules and providing test output. RVS architecture is built around concept of Linux shared objects, thus allowing for easy addition of new modules in the future.

## GPU Properties (GPUP)[#](#gpu-properties-gpup)

The GPU Properties module queries the configuration of a target device and returns the device’s static characteristics. These static values can be used to debug issues such as device support, performance and firmware problems.

## GPU Monitor (GM module) [deprecated][#](#gpu-monitor-gm-module-deprecated)

The GPU monitor tool is capable of running on one, some or all of the GPU(s) installed and will report various information at regular intervals. The module can be configured to halt another RVS modules execution if one of the quantities exceeds a specified boundary value.

## PCI Express State Monitor (PESM module) [deprecated][#](#pci-express-state-monitor-pesm-module-deprecated)

The PCIe State Monitor tool is used to actively monitor the PCIe interconnect between the host platform and the GPU. The module will register a “listener” on a target GPU’s PCIe interconnect, and log a message whenever it detects a state change. The PESM will be able to detect the following state changes:

PCIe link speed changes

GPU power state changes


## ROCm Configuration Qualification Tool (RCQT module)[#](#rocm-configuration-qualification-tool-rcqt-module)

The ROCm Configuration Qualification Tool ensures the platform is capable of running ROCm applications and is configured correctly. It checks the installed versions of the ROCm components and the platform configuration of the system. This includes checking the dependencies corresponding to the ROCm meta-packages are installed correctly.

## PCI Express Qualification Tool (PEQT module)[#](#pci-express-qualification-tool-peqt-module)

The PCIe Qualification Tool is used to qualify the PCIe bus on which the GPU is connected. The qualification test will be capable of determining the following characteristics of the PCIe bus interconnect to a GPU:

Support for Gen 3 atomic completers

DMA transfer statistics

PCIe link speed

PCIe link width


## SBIOS Mapping Qualification Tool (SMQT module) [deprecated][#](#sbios-mapping-qualification-tool-smqt-module-deprecated)

The GPU SBIOS mapping qualification tool is designed to verify that a platform’s SBIOS has satisfied the BAR mapping requirements for VDI and Radeon Instinct products for ROCm support.

## P2P Benchmark and Qualification Tool (PBQT module)[#](#p2p-benchmark-and-qualification-tool-pbqt-module)

The P2P Benchmark and Qualification Tool is designed to provide the list of all GPUs that support P2P and characterize the P2P links between peers. In addition to testing P2P compatibility, this test will perform a peer-to-peer throughput test between all P2P pairs for performance evaluation. The P2P Benchmark and Qualification Tool will allow users to pick a collection of two or more GPUs to run the test. The user will also be able to select whether or not they want to run the throughput test on each of the pairs.

## PCI Express Bandwidth Benchmark (PEBB module)[#](#pci-express-bandwidth-benchmark-pebb-module)

The PCIe Bandwidth Benchmark attempts to saturate the PCIe bus with DMA transfers between system memory and a target GPU card’s memory. The maximum bandwidth obtained is reported to help debug low bandwidth issues. The benchmark should be capable of targeting one, some or all of the GPUs installed in a platform, reporting individual benchmark statistics for each.

## GPU Stress test (GST module)[#](#gpu-stress-test-gst-module)

The GPU Stress Test runs various GEMM operations as workloads to stress the GPU FLOPS performance. GEMM operations include SGEMM, DGEMM and HGEMM (Single/Double/Half-precision General Matrix Multiplication) operations based on configured parameters. The duration of the test is configurable, both in terms of time (how long to run) and iterations (how many times to run).

## Input EDPp test (IET module)[#](#input-edpp-test-iet-module)

The Input EDPp Test runs GEMM workloads to stress the GPU power (i.e. TGP). This test is used to verify if the GPU is capable of handling max. power stress for a sustained period of time. Also checks whether GPU power reaches a set target power.

## Memory test (MEM module)[#](#memory-test-mem-module)

The Memory module tests the GPU memory for hard and soft errors using HIP. It consists of various tests that use algorithms like Walking 1 bit, Moving inversion and Modulo 20. The module executes the following memory tests [Algorithm, data pattern]

Walking 1 bit

Own address test

Moving inversions, ones & zeros

Moving inversions, 8 bit pattern

Moving inversions, random pattern

Block move, 64 moves

Moving inversions, 32 bit pattern

Random number sequence

Modulo 20, random pattern

Memory stress test


## BABEL benchmark test (BABEL module)[#](#babel-benchmark-test-babel-module)

The Babel module executes BabelStream (synthetic GPU benchmark based on the original STREAM benchmark for CPUs) benchmark that measures memory transfer rates (bandwidth) to and from global device memory. Various benchmark tests are implemented using GPU kernels in HIP (Heterogeneous Interface for Portability) programming language.
