---
title: "JAX on ROCm installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:40.610015+00:00
content_hash: "db3b52607d652f00"
---

# JAX on ROCm installation[#](#jax-on-rocm-installation)

2026-04-16

7 min read time

[JAX](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html) is a library
for array-oriented numerical computation (similar to NumPy), with automatic differentiation
and just-in-time (JIT) compilation to enable high-performance machine learning research.

This topic covers setup instructions and the necessary files to build, test, and run
JAX with ROCm support in a Docker environment. To learn more about JAX on ROCm,
including its use cases, recommendations, as well as hardware and software compatibility,
see [JAX compatibility](https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/jax-compatibility.html).

## Install JAX on ROCm[#](#install-jax-on-rocm)

To install JAX on ROCm, you have the following options:

[Use a prebuilt Docker image with JAX preinstalled](#using-docker-with-jax-pre-installed)**(recommended)**

### Use a prebuilt Docker image with JAX preinstalled[#](#use-a-prebuilt-docker-image-with-jax-preinstalled)

The ROCm JAX team provides prebuilt Docker images, which is the simplest way to use JAX on ROCm. These images are available on Docker Hub and come with JAX configured for ROCm.

To pull the latest ROCm JAX Docker image, run:

pull rocm/jax:latest

Once the image is downloaded, launch a container using the following command:

run -it \ --network=host \ --device=/dev/kfd \ --device=/dev/dri \ --ipc=host \ --shm-size 64G \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v $(pwd):/jax_dir \ --name rocm_jax \ rocm/jax:latest /bin/bash

Tip

The

`--shm-size`

parameter allocates shared memory for the container. Adjust it based on your system’s resources if needed.Replace

`$(pwd)`

with the absolute path to the directory you want to mount inside the container.

Verify the installation of ROCm JAX. See

[Test the JAX installation](#jax-verify-installation).

### Docker image support[#](#docker-image-support)

AMD validates and publishes ready-made JAX images with ROCm backends on Docker
Hub. The following Docker image tags and associated inventories are validated
for ROCm 7.2.2.
For `jax-community`

images, see [rocm/jax-community](https://hub.docker.com/r/rocm/jax-community/tags) on Docker Hub.

### Use a ROCm base Docker image to install JAX[#](#use-a-rocm-base-docker-image-to-install-jax)

If you prefer to use the ROCm Ubuntu image or already have a ROCm Ubuntu container, follow these steps to install JAX in the container.

Pull the ROCm Ubuntu Docker image. For example, use the following command to pull the ROCm Ubuntu image:

pull rocm/dev-ubuntu-24.04:7.2.2-complete

Launch the Docker container. After pulling the image, launch a container using this command:

run -it \ --network=host \ --device=/dev/kfd \ --device=/dev/dri \ --ipc=host \ --shm-size 64G \ --group-add video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v $(pwd):/jax_dir \ --name rocm_jax \ rocm/dev-ubuntu-24.04:7.2.2-complete /bin/bash

Install the latest version of JAX. Inside the running container, install the required version of JAX with ROCm support using pip:

install --break-system-packages jax==0.8.2 pip3 install --break-system-packages jax-rocm7-pjrt==0.8.2 pip3 install --break-system-packages jax-rocm7-plugin==0.8.2 pip3 install --break-system-packages https://github.com/ROCm/rocm-jax/releases/download/rocm-jax-v0.8.2/jaxlib-0.8.2+rocm7-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl

Verify the installed JAX version. Check whether the correct version of JAX and its ROCm plugins are installed.

freeze | grep jax

Expected output:

jax==0.8.2 jax-rocm7-pjrt==0.8.2 jax-rocm7-plugin==0.8.2 jaxlib==0.8.2

Explicitly set the

`LLVM_PATH`

environment variable. This helps XLA find`ld.lld`

in the PATH at runtime.export LLVM_PATH=/opt/rocm/llvm

Install

`libdw1`

if neededupdate apt install libdw1

Verify the installation of ROCm JAX. See

[Test the JAX installation](#jax-verify-installation).

### Install JAX on bare-metal or a custom container[#](#install-jax-on-bare-metal-or-a-custom-container)

Follow these steps if you prefer to install ROCm manually on your host system or in a custom container.

Install ROCm. Follow the

[ROCm installation guide](https://rocm.docs.amd.com/en/latest/deploy/linux/quick_start.html)to install ROCm on your system.Once installed, verify your ROCm installation using:

| AMD-SMI 26.2.1+fc0010cf6a amdgpu version: 6.14.14 ROCm version: 7.2.2 | | VBIOS version: 023.040.001.008.000001 | | Platform: Linux Baremetal | |-------------------------------------+----------------------------------------| | BDF GPU-Name | Mem-Uti Temp UEC Power-Usage | | GPU HIP-ID OAM-ID Partition-Mode | GFX-Uti Fan Mem-Usage | |=====================================+========================================| | 0000:05:00.0 AMD Instinct MI355X | 0 % 54 °C 0 234/1400 W | | 0 1 6 SPX/NPS1 | 0 % N/A 283/294896 MB | |-------------------------------------+----------------------------------------| | 0000:15:00.0 AMD Instinct MI355X | 0 % 54 °C 0 238/1400 W | | 1 3 7 SPX/NPS1 | 0 % N/A 283/294896 MB | +-------------------------------------+----------------------------------------+ +------------------------------------------------------------------------------+ | Processes: | | GPU PID Process Name GTT_MEM VRAM_MEM MEM_USAGE CU % | |==============================================================================| | No running processes found | +------------------------------------------------------------------------------+

Install the required version of JAX with ROCm support using pip:

install --break-system-packages jax==0.8.2 pip3 install --break-system-packages jax-rocm7-pjrt==0.8.2 pip3 install --break-system-packages jax-rocm7-plugin==0.8.2 pip3 install --break-system-packages https://github.com/ROCm/rocm-jax/releases/download/rocm-jax-v0.8.2/jaxlib-0.8.2+rocm7-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl

Verify the installed JAX version. Check whether the correct version of JAX and its ROCm plugins are installed.

freeze | grep jax

Explicitly set the

`LLVM_PATH`

environment variable.export LLVM_PATH=/opt/rocm/llvm

Install

`libdw1`

if neededupdate apt install libdw1

Verify the installation of ROCm JAX. See

[Test the JAX installation](#jax-verify-installation).

### Build JAX from source[#](#build-jax-wheels)

The [ROCm/rocm-jax](https://github.com/ROCm/rocm-jax/tree/rocm-jaxlib-v0.8.2) repository contains sources for the ROCm
plugin for JAX as well as Dockerfiles used to build the AMD `rocm/jax`

images.
For the most up-to-date instructions, refer directly to the instructions in the repository:

See

[Quick build](https://github.com/ROCm/ROCm-jax/tree/rocm-jaxlib-v0.8.2?tab=readme-ov-file#quickbuild)for concise high-level steps.See

[Building](https://github.com/ROCm/rocm-jax/blob/rocm-jaxlib-v0.8.2/BUILDING.md#building)for more in-depth build instructions and troubleshooting suggestions.

## Test the JAX installation[#](#test-the-jax-installation)

After launching the container, test whether JAX detects ROCm devices as expected:

```
-c "import jax; print(jax.devices())"
python3 -c "import jax.numpy as jnp; x = jnp.arange(5); print(x)"
```

If the setup is successful, the output should list all available ROCm devices.

Expected output:

```
[RocmDevice(id=0), RocmDevice(id=1), RocmDevice(id=2), RocmDevice(id=3)]
```

```
[0 1 2 3 4]
```
