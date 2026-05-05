---
title: "PyTorch on ROCm installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T18:20:34.600035+00:00
content_hash: "5bfc688f2b2cc83a"
---

# PyTorch on ROCm installation[#](#pytorch-on-rocm-installation)

2026-04-16

13 min read time

[PyTorch](https://pytorch.org/) is an open-source tensor library designed for deep learning.
PyTorch on ROCm provides mixed-precision and large-scale training using AMD [MIOpen](https://github.com/ROCm/MIOpen)
and [RCCL](https://github.com/ROCm/rccl) libraries.

This topic covers setup instructions and the necessary files to build, test, and run
PyTorch with ROCm support in a Docker environment. To learn more about PyTorch on ROCm,
including its use cases, recommendations, as well as hardware and software compatibility,
see [PyTorch compatibility](https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/pytorch-compatibility.html).

## Install PyTorch[#](#install-pytorch)

To install PyTorch for ROCm, you have the following options:

[Use a prebuilt Docker image with PyTorch pre-installed](#using-docker-with-pytorch-pre-installed)**(recommended)**

### Use a prebuilt Docker image with PyTorch pre-installed[#](#use-a-prebuilt-docker-image-with-pytorch-pre-installed)

The recommended setup to get a PyTorch environment is through Docker, as it avoids potential installation issues.
The tested, prebuilt image includes PyTorch, ROCm, and other dependencies. See [Docker image support](#pytorch-docker-support).
To install ROCm on bare metal, follow [ROCm installation overview](../install-overview.html).

Download the latest public

[PyTorch Docker image](https://hub.docker.com/r/rocm/pytorch).pull rocm/pytorch:latest

Important

The

`rocm/pytorch:latest`

tag points to a Docker image with the latest ROCm-tested release of PyTorch.You can download Docker images with specific ROCm, PyTorch, and operating system versions. See the available tags on

[Docker Hub](https://hub.docker.com/r/rocm/pytorch/tags).Start a Docker container using the image.

run -it \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --shm-size 8G \ rocm/pytorch:latest

Note

This will automatically download the image if it does not exist on the host. You can also pass the

`-v`

argument to mount any data directories from the host onto the container.

### Docker image support[#](#docker-image-support)

AMD validates and publishes ready-made [PyTorch](https://hub.docker.com/r/rocm/pytorch) images
with ROCm backends on Docker Hub. The following Docker image tags and associated inventories are
validated for ROCm 7.2.2.

Docker pull tag

```
pull rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.9.1
```

Additional software components

See
`rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.9.1`

on [Docker Hub](https://hub.docker.com/layers/rocm/pytorch/rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.9.1/images/sha256-b26587aa39658886e1bc916ced9f5eefc7d951f858ecdeff4e8ad330b6e5e6c2).

Docker pull tag

```
pull rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.8.0
```

Additional software components

See
`rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.8.0`

on [Docker Hub](https://hub.docker.com/layers/rocm/pytorch/rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.8.0/images/sha256-76b53fcf1523d3456f637e1d5ed7542e8c6dc57eced29d53199df15643395910).

Docker pull tag

```
pull rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.7.1
```

Additional software components

See
`rocm/pytorch:rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.7.1`

on [Docker Hub](https://hub.docker.com/layers/rocm/pytorch/rocm7.2.2_ubuntu24.04_py3.12_pytorch_release_2.7.1/images/sha256-a27dc6ba137f029973b487699366f14464aa22c3c79ed3881826502ab8ff20cb).

### Use a wheels package[#](#use-a-wheels-package)

PyTorch supports the ROCm platform by providing tested wheels packages. To access this feature, go
to [pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/). For the correct
wheels command, you must select **Linux**, **Python**, **pip**, and **ROCm** in the matrix.

Note

The available ROCm release varies between the **PyTorch Build** of `Stable`

or `Nightly`

.
More recent releases are generally available through the Nightly builds.

## Setting up the environment for the wheel installation

Choose one of the following three options:

**Option 1:**Download a base Docker image with the correct ROCm version.

Pull the selected image.

pull rocm/dev-ubuntu-22.04:latest

Start a Docker container using the downloaded image.

run -it --device=/dev/kfd --device=/dev/dri --group-add video rocm/dev-ubuntu-22.04:latest


**Option 2:**Select a base OS Docker image. Check

[System requirements (Linux)](../../reference/system-requirements.html#system-requirements).Pull selected base OS image (Ubuntu 22.04, for example).

pull ubuntu:22.04

Start a Docker container using the downloaded image.

run -it --device=/dev/kfd --device=/dev/dri --group-add video ubuntu:22.04

Install ROCm using the directions in the

[ROCm installation overview](../install-overview.html#rocm-install-overview)section.

**Option 3:**Install on bare-metal. Check

[System requirements (Linux)](../../reference/system-requirements.html#system-requirements)and install ROCm using the instructions in the[ROCm installation overview](../install-overview.html#rocm-install-overview)section.Install the required dependencies for the wheels package.

apt update sudo apt install libjpeg-dev python3-dev python3-pip pip3 install wheel setuptools


Install

`torch`

,`torchvision`

, and`torchaudio`

, as specified in the[installation matrix](https://pytorch.org/get-started/locally/).install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.2

Note

The above command uses the ROCm 7.2 PyTorch wheel. If you want a different version of ROCm, modify the command accordingly.


### Build PyTorch from source[#](#build-pytorch-from-source)

Use the `rocm/pytorch:latest`

image, uninstall the preinstalled PyTorch
package, and rebuild PyTorch from source. This ensures compatibility with your
specific ROCm version, GPU architecture, and project requirements.

Download the latest PyTorch Docker image.

pull rocm/pytorch:latest

Start a Docker container using the downloaded image.

run -it \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --shm-size 8G \ rocm/pytorch:latest

Uninstall the pre-installed PyTorch inside the container. Otherwise, the prebuilt ROCm PyTorch from the container might conflict with your source build.

uninstall -y torch torchvision torchaudio

Clone the PyTorch repository.

cd ~ git clone https://github.com/pytorch/pytorch.git cd pytorch git submodule update --init --recursive

(Optional) Set your ROCm architecture.

By default, PyTorch builds for a broad set of AMD architectures. To speed up compilation, you can target only your GPU architecture.

To determine your architecture:

| grep gfx

Then set the

`PYTORCH_ROCM_ARCH`

environment variable:export PYTORCH_ROCM_ARCH=<uarch>

Replace

`<uarch>`

with the result from`rocminfo`

(for example,`gfx90a`

,`gfx1030`

). See[System requirements (Linux)](../../reference/system-requirements.html#system-requirements)for the list of AMD GPU architectures.Build and install PyTorch following the instructions in

[pytorch/pytorch](https://github.com/pytorch/pytorch?tab=readme-ov-file#install-pytorch).

### Use the PyTorch upstream Dockerfile[#](#use-the-pytorch-upstream-dockerfile)

If you don’t want to use a prebuilt base Docker image, you can build a custom base Docker image using scripts from the PyTorch repository. This uses a standard Docker image from operating system maintainers and installs all the required dependencies, including:

ROCm

torchvision

Conda packages

The compiler toolchain


Clone the PyTorch repository.

cd ~ git clone https://github.com/pytorch/pytorch.git cd pytorch git submodule update --init --recursive

Build the PyTorch Docker image.

cd .ci/docker ./build.sh pytorch-linux-<os-version>-rocm<rocm-version>-py<python-version> -t rocm/pytorch:build_from_dockerfile

Where:

`<os-version>`

=`ubuntu20.04`

(or`focal`

),`ubuntu22.04`

(or`jammy`

)`<rocm-version>`

=`6.0`

,`6.1`

,`6.2`

`<python-version>`

=`3.8`

-`3.11`


To verify that your image was successfully created, run:

image ls rocm/pytorch:build_from_dockerfile

If successful, the output looks like this:

TAG IMAGE ID CREATED SIZE rocm/pytorch build_from_dockerfile 17071499be47 2 minutes ago 32.8GB

Start a Docker container using the image with the mounted PyTorch folder.

run -it --cap-add=SYS_PTRACE --security-opt seccomp=unconfined \ --user root --device=/dev/kfd --device=/dev/dri \ --group-add video --ipc=host --shm-size 8G \ -v ~/pytorch:/pytorch rocm/pytorch:build_from_dockerfile

You can also pass the

`-v`

argument to mount any data directories from the host onto the container.Go to the PyTorch directory.

cd /pytorch

Set ROCm architecture.

To determine your AMD architecture, run:

| grep gfx

The result looks like this (for

`gfx1030`

architecture):gfx1030 Name: amdgcn-amd-amdhsa--gfx1030

Set the

`PYTORCH_ROCM_ARCH`

environment variable to specify the architectures you want to build PyTorch for.export PYTORCH_ROCM_ARCH=<uarch>

where

`<uarch>`

is the architecture reported by the`rocminfo`

command.Build PyTorch.

This converts PyTorch CUDA sources to

[HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)and builds the PyTorch framework.To check if your build is successful, run:

echo $? # should return 0 if success


## Test the PyTorch installation[#](#test-the-pytorch-installation)

You can use PyTorch unit tests to validate your PyTorch installation. If you used a
**prebuilt PyTorch Docker image from AMD ROCm Docker Hub** or installed an
**official wheels package**, validation tests are not necessary.

If you want to manually run unit tests to validate your PyTorch installation fully, follow these steps:

Import the torch package in Python to test if PyTorch is installed and accessible.

Note

Do not run the following command from the PyTorch home directory.

-c 'import torch' 2> /dev/null && echo 'Success' || echo 'Failure'

Check if the GPU is accessible from PyTorch. In the PyTorch framework,

`torch.cuda`

is a generic way to access the GPU. This can only access an AMD GPU if one is available.-c 'import torch; print(torch.cuda.is_available())'

Run unit tests to validate the PyTorch installation fully.

Note

You must run the following command from the PyTorch home directory.

PYTORCH_TEST_WITH_ROCM=1 python3 test/run_test.py --verbose \ --include test_nn test_torch test_cuda test_ops \ test_unary_ufuncs test_binary_ufuncs test_autograd

This command ensures that the required environment variable is set to skip certain unit tests for ROCm. This also applies to wheel installs in a non-controlled environment.

Note

Make sure your PyTorch source code corresponds to the PyTorch wheel or the installation in the Docker image. Incompatible PyTorch source code can give errors when running unit tests.

Some tests may be skipped, as appropriate, based on your system configuration. ROCm doesn’t support all PyTorch features; tests that evaluate unsupported features are skipped. Other tests might be skipped, depending on the host or GPU memory and the number of available GPUs.

If the compilation and installation are correct, all tests will pass.

(Optional) Run individual unit tests.

PYTORCH_TEST_WITH_ROCM=1 python3 test/test_nn.py --verbose

You can replace

`test_nn.py`

with any other test set.

## Run a PyTorch example[#](#run-a-pytorch-example)

The PyTorch examples repository provides basic examples that exercise the functionality of your framework.

Two of our favorite testing databases are:

**MNIST**(Modified National Institute of Standards and Technology): A database of handwritten digits that can be used to train a Convolutional Neural Network for**handwriting recognition**.**ImageNet**: A database of images that can be used to train a network for**visual object recognition**.

### MNIST PyTorch example[#](#mnist-pytorch-example)

Clone the PyTorch examples repository.

clone https://github.com/pytorch/examples.git

Go to the MNIST example folder.

cd examples/mnist

Follow the instructions in the

`README.md`

file in this folder to install the requirements. Then run:`main.py`

This generates the following output:

... Train Epoch: 14 [58240/60000 (97%)] Loss: 0.010128 Train Epoch: 14 [58880/60000 (98%)] Loss: 0.001348 Train Epoch: 14 [59520/60000 (99%)] Loss: 0.005261 Test set: Average loss: 0.0252, Accuracy: 9921/10000 (99%)


### ImageNet PyTorch example[#](#imagenet-pytorch-example)

Clone the PyTorch examples repository (if you didn’t already do this in the preceding MNIST example).

clone https://github.com/pytorch/examples.git

Go to the ImageNet example folder.

cd examples/imagenet

Follow the instructions in the

`README.md`

file in this folder to install the Requirements. Then run:`main.py`


## Troubleshooting[#](#troubleshooting)

What to do if you get the following error when trying to run PyTorch:

Unable to find code object for all current devices!

The error denotes that the installation of PyTorch and/or other dependencies or libraries do not support the current GPU. To workaround this issue, use the following steps:

Confirm that the hardware supports the ROCm stack. Refer to

[System requirements (Linux)](../../reference/system-requirements.html#system-requirements)and[System requirements for Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html#system-requirements-win).Determine the gfx target.

| grep gfx

Check if PyTorch is compiled with the correct gfx target.

TORCHDIR=$( dirname $( python3 -c 'import torch; print(torch.__file__)' ) ) llvm-readobj --offloading $TORCHDIR/lib/libtorch_hip.so # check for gfx target

Note

Recompile PyTorch with the right gfx target if compiling from the source if the hardware is not supported.


What if you are unable to access Docker or GPU in user accounts?

Ensure that the user is added to docker, video, and render Linux groups as described in

[Configuring permissions for GPU access](../prerequisites.html#group-permissions).Can you install PyTorch directly on bare metal?

Bare-metal installation of PyTorch is supported through wheels. For more information, see

[Use a wheels package](#using-wheels-package).How do you profile PyTorch workloads?

Use the PyTorch Profiler as described in

[PyTorch Profiler](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#mi300x-pytorch-profiler)to profile GPU kernels on ROCm.
