---
title: "DGL on ROCm installation"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/dgl-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:36.470256+00:00
content_hash: "2f3fa2fbe7667ae6"
---

# DGL on ROCm installation[#](#dgl-on-rocm-installation)

2025-12-15

8 min read time

Deep Graph Library ([DGL](https://www.dgl.ai/)) is an easy-to-use, high-performance, and scalable
Python package for deep learning on graphs.

This topic covers setup instructions and the necessary files to build, test, and run
DGL with ROCm support in a Docker environment. To learn more about DGL on ROCm,
including its use cases, recommendations, as well as hardware and software compatibility,
see [DGL compatibility](https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/dgl-compatibility.html).

Note

DGL is supported on ROCm 7.0.0, 6.4.3, and 6.4.0. This topic provides installation
instructions for ROCm 7.0.0 and 6.4.3. For ROCm 6.4.0, see [DGL version history](previous-versions/dgl-history.html).

## Install DGL[#](#install-dgl)

To install DGL on ROCm, you have the following options:

### Use a prebuilt Docker image with DGL pre-installed[#](#use-a-prebuilt-docker-image-with-dgl-pre-installed)

The recommended way to set up a DGL environment and avoid potential installation issues is with Docker. The tested, prebuilt image includes DGL, PyTorch, ROCm, and other dependencies.

Important

To follow these instructions, input your chosen tag into `<TAG>`

. Example: `dgl-2.4.0.amd0_rocm7.0.0_ubuntu24.04_py3.12_pytorch_2.8.0`

.

You can download Docker images for DGL with specific ROCm, PyTorch, Python, and operating system versions.
See the available tags on [Docker Hub](https://hub.docker.com/r/rocm/dgl/tags) and see [Docker image support](#dgl-docker-support) below.

Download your required public

[DGL Docker image](https://hub.docker.com/r/rocm/dgl/tags)pull rocm/dgl:<TAG>

Launch and connect to the Docker container using the image

docker run -it --network=host --device=/dev/kfd --device=/dev/dri \ --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt \ seccomp=unconfined --shm-size 8G rocm/dgl:<TAG>

Note

This will automatically download the image if it does not exist on the host. You can also pass the

`-v`

argument to mount any data directories from the host onto the container.

### Docker image support[#](#docker-image-support)

AMD validates and publishes ready-made [DGL Docker images](https://hub.docker.com/r/rocm/dgl/tags)
with ROCm backends on Docker Hub. The following Docker image tags and associated inventories are
validated for their respective ROCm versions listed below.

### Build your own Docker image[#](#build-your-own-docker-image)

Clone the

[ROCm/dgl](https://github.com/ROCm/dgl)repositoryclone --recurse-submodules https://github.com/ROCm/dgl cd dgl

Build the Docker container

To build the Docker container, run the following command:

# DGL on Ubuntu 24.04 + ROCm 7.0.0 + Py 3.12 + PyTorch 2.8.0 docker build \ -t dgl:dgl-2.4.0.amd0_rocm7.0.0_ubuntu24.04_py3.12_pytorch_2.8.0 \ --build-arg BASE_IMAGE=rocm/pytorch:rocm7.0_ubuntu24.04_py3.12_pytorch_release_2.8.0 \ --build-arg ARG_MAX_JOBS=8 \ --build-arg ARG_GPU_BUILD_TARGETS="gfx90a,gfx942" \ --build-arg ARG_DGL_ARTIFACTS_DIR="/artifacts" \ -f docker/Dockerfile.ci_gpu_rocm \ .

To build the Docker container, run the following command:

# DGL on Ubuntu 24.04 + ROCm 7.0 + Py 3.12 + PyTorch 2.6.0 docker build \ -t dgl:dgl-2.4.0.amd0_rocm7.0.0_ubuntu24.04_py3.12_pytorch_2.6.0 \ --build-arg BASE_IMAGE=rocm/pytorch:rocm7.0_ubuntu24.04_py3.12_pytorch_release_2.6.0 \ --build-arg ARG_MAX_JOBS=8 \ --build-arg ARG_GPU_BUILD_TARGETS="gfx90a,gfx942" \ --build-arg ARG_DGL_ARTIFACTS_DIR="/artifacts" \ -f docker/Dockerfile.ci_gpu_rocm \ .

To build the Docker container, run the following command:

# DGL on Ubuntu 22.04 + ROCm 7.0.0 + Py 3.10 + PyTorch 2.7.1 docker build \ -t dgl:dgl-2.4.0.amd0_rocm7.0.0_ubuntu22.04_py3.10_pytorch_2.7.1 \ --build-arg BASE_IMAGE=rocm/pytorch:rocm7.0_ubuntu22.04_py3.10_pytorch_release_2.7.1 \ --build-arg ARG_MAX_JOBS=8 \ --build-arg ARG_GPU_BUILD_TARGETS="gfx90a,gfx942" \ --build-arg ARG_DGL_ARTIFACTS_DIR="/artifacts" \ -f docker/Dockerfile.ci_gpu_rocm \ .

To build the Docker container, run the following command:

# DGL on Ubuntu 24.04 + ROCm 6.4.3 + Py 3.12 + PyTorch 2.6.0 docker build \ -t dgl:dgl-2.4.0.amd0_rocm6.4.3_ubuntu24.04_py3.12_pytorch_2.6.0 \ --build-arg BASE_IMAGE=rocm/pytorch:rocm6.4.3_ubuntu24.04_py3.12_pytorch_release_2.6.0 \ --build-arg ARG_CONDA_ENV=py_3.12 \ --build-arg ARG_MAX_JOBS=8 \ --build-arg ARG_GPU_BUILD_TARGETS="gfx90a,gfx942" \ -f Dockerfile.rocm \ .


### Use a wheels package[#](#use-a-wheels-package)

The DGL `.whl`

packages are hosted on the AMD PyPI repository. Instead of manually downloading the files,
you can simply install DGL using `pip`

with the provided URL.
This command will automatically download and install the appropriate `.whl`

file.

To install using wheels, run the following command:

```
install https://pypi.amd.com/rocm-7.0.0/packages/amd-dgl/amd_dgl-2.4.0+amd0.torch2.8.0.rocm7.0.0.git64359f59.ubuntu24.4-cp312-cp312-linux_x86_64.whl
```

To install using wheels, run the following command:

```
install https://pypi.amd.com/rocm-7.0.0/packages/amd-dgl/amd_dgl-2.4.0+amd0.torch2.6.0.rocm7.0.0.git2e48b21f.ubuntu24.4-cp312-cp312-linux_x86_64.whl
```

To install using wheels, run the following command:

```
install https://pypi.amd.com/rocm-7.0.0/packages/amd-dgl/amd_dgl-2.4.0+amd0.torch2.7.1.rocm7.0.0.git698b58a9.ubuntu22.4-cp310-cp310-linux_x86_64.whl
```

To install using wheels, run the following command:

```
install https://pypi.amd.com/rocm-6.4.3/packages/amd-dgl/amd_dgl-2.4.0+amd0.torch2.6.0.gitdbfe118.ubuntu24.4-cp312-cp312-linux_x86_64.whl
```

After installing a `.whl`

file, you can confirm that the package was installed successfully using:

```
show amd_dgl
```

## Test the DGL installation[#](#test-the-dgl-installation)

To verify that DGL has been successfully installed, run the Docker container as described in the [Installing DGL section](#using-pre-docker-with-dgl-pre-installed).
Once inside the container, ensure you have access to the Bash shell.

To check for a shared library:

```
/ -name libdgl.so -print -quit 2>/dev/null && echo "libdgl.so found" || echo "libdgl.so NOT found"
```

To check for Python import:

```
activate py_<python version> #You can check this with conda info --envs
export DGLBACKEND=pytorch
python -c "import dgl; print('dgl import successful, version:', dgl.__version__)" || echo "Failed to import DGL"
```

### Run tests for DGL[#](#run-tests-for-dgl)

You can also run tests from the scripts folder at `/src/dgl/`

.
These tests are only viable if you are using the above Docker containers or building Docker containers from source.

To run Python tests:

```
cd /src/dgl
bash tests/scripts/task_unit_test_rocm.sh pytorch gpu
```

To run C++ tests:

```
cd /src/dgl
bash tests/scripts/task_cpp_unit_test.sh
```

Estimated time: the tests usually take 10-15 minutes to run.

## Run a DGL example[#](#run-a-dgl-example)

Multiple use cases of DGL have been tested and verified. However, a recommended
example follows a drug discovery pipeline using the `SE3Transformer`

.
For use cases and recommendations, refer to the [AMD ROCm blog](https://rocm.blogs.amd.com/),
where you can search for DGL examples and best practices to optimize your workloads on AMD GPUs.

## Troubleshooting[#](#troubleshooting)

**Unable to access Docker or GPU in user accounts?**Ensure the user is added to`docker`

,`video`

, and`render`

groups. See[Configuring permissions for GPU access](../prerequisites.html#group-permissions).**Profiling DGL workloads?**Use the PyTorch Profiler, as explained in[PyTorch Profiler](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference-optimization/workload.html#mi300x-pytorch-profiler)to profile GPU kernels on ROCm.

## Previous versions[#](#previous-versions)

See [DGL version history](previous-versions/dgl-history.html) to find documentation for previous releases
of the `ROCm/dgl`

Docker image.
