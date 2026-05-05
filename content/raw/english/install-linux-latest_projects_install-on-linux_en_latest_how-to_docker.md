---
title: "Running ROCm Docker containers"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/docker.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:14:26.424604+00:00
content_hash: "ba2e41e17817de9a"
---

# Running ROCm Docker containers[#](#running-rocm-docker-containers)

2026-04-22

6 min read time

Using Docker to run your ROCm applications is one of the best ways to get consistent and reproducible environments.

## Prerequisites[#](#prerequisites)

Docker containers share the kernel with the host OS. Therefore, the ROCm kernel-mode driver (`amdgpu-dkms`

) must be installed on the host. If you’ve already installed ROCm, you probably already have `amdgpu-dkms`

.

If you don’t have

`amdgpu-dkms`

, follow the[standard ROCm installation instructions](../install/quick-start.html#rocm-install-quick)(which comes with`amdgpu-dkms`

) or[install amdgpu-dkms](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/package-manager-index.html)separately.

## Accessing GPUs in containers[#](#accessing-gpus-in-containers)

To grant a Docker container access to the host’s AMD GPUs, run your container with the following options.
See the [Docker documentation](https://docs.docker.com/reference/cli/docker/container/run/) to learn
more about the `docker run`

command and its options.

```
run --device /dev/kfd --device /dev/dri --security-opt seccomp=unconfined <image>
```

The purpose of each option is as follows:

`--device /dev/kfd`

This is the main compute interface, shared by all GPUs. The Docker CLI’s

`--device`

option enables directly exposing host devices to a container. See[Add host device to container (–device)](https://docs.docker.com/reference/cli/docker/container/run/#device)for more information.`--device /dev/dri`

This directory contains the Direct Rendering Interface (DRI) for each GPU. To restrict access to specific GPUs, see

[Restricting GPU access](#docker-restrict-gpus).`--security-opt seccomp=unconfined`

(optional)This option enables memory mapping, and is recommended for containers running in HPC environments. See

[Optional security options (–security-opt)](https://docs.docker.com/reference/cli/docker/container/run/#security-opt).The performance of an application can vary depending on the assignment of GPUs and CPUs to the task. Typically,

`numactl`

is installed as part of many HPC applications to provide GPU/CPU mappings. This Docker runtime option supports memory mapping and can improve performance.

### Docker compose[#](#docker-compose)

You can also use `docker compose`

to launch your containers, even when launching a single
container. This can be a convenient way to run complex Docker commands without having to
remember all the CLI arguments.
The following snippet is an example `compose.yaml`

file, which is equivalent to
the preceding `docker run`

command:

```
services:
my-service:
image: <image>
devices:
- /dev/kfd
- /dev/dri
security_opt:
- seccomp=unconfined
```

You can then run this using `docker compose run my-service`

.

### Restricting GPU access[#](#restricting-gpu-access)

By default, passing `--device /dev/dri`

grants access to all GPUs on the system. To limit a container to a
specific subset of GPUs, you can instead pass in their individual device nodes.

GPU device nodes are located in `/dev/dri/`

and are typically named `renderD128`

, `renderD129`

, and so on.
You can list the available GPUs on your host system with the following command:

```
/dev/dri/render*
```

To expose only the first two GPUs to the container, specify them directly in the run command.
Note that `/dev/kfd`

is always required for the compute interface.

For example, to expose the first and second GPU:

```
run --device /dev/kfd --device /dev/dri/renderD128 --device /dev/dri/renderD129 ..
```

Note

When GPUs are partitioned (such as the Instinct MI300X or MI350X Series in DPX, QPX, or
CPX mode), you must account for the number of partitions when selecting
GPUs. For example, in CPX mode, `renderD128`

and `renderD137`

correspond to the first and second GPUs. In CPX mode, `renderD128`

to
`renderD136`

correspond to different partitions of the first GPU. For more
information, see [GPU partition](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/overview.html).

### Verifying the AMD GPU driver has been loaded on GPUs[#](#verifying-the-amd-gpu-driver-has-been-loaded-on-gpus)

`rocminfo`

is an application for reporting information about the HSA system attributes and agents.
`amd-smi`

is a tool that acts as a command line interface for manipulating and monitoring the amdgpu kernel.

Running `rocminfo`

and `amd-smi list`

inside the container will only enumerate the GPUs passed into the docker container.
Running `rocminfo`

and `amd-smi list`

on bare metal will enumerate all ROCm-capable GPUs on the machine.

## Docker images in the ROCm ecosystem[#](#docker-images-in-the-rocm-ecosystem)

The [ROCm Docker repository](https://github.com/ROCm/ROCm-docker) hosts Dockerfiles useful for
building your own ROCm-capable containers. The built images are available on
[Docker Hub](https://hub.docker.com/u/rocm). In particular:

`rocm/rocm-terminal`

is a small image with the prerequisites to build HIP applications, but does not include any libraries.[ROCm dev images](https://hub.docker.com/u/rocm?page=1&search=dev-)provide a variety of OS and ROCm versions, and are a great starting place for building applications.

### Pull a ROCm dev Docker image[#](#pull-a-rocm-dev-docker-image)

Pull a ROCm dev Docker image with a supported configuration. See [Docker
Hub](https://hub.docker.com/u/rocm?page=1&search=dev-ubuntu-2) to browse
available images. For example:

### Launch the Docker container[#](#launch-the-docker-container)

Launch the Docker container to allow GPU access. For example:

```
run -it \
--cap-add=SYS_PTRACE \
--ipc=host \
--privileged=true \
--shm-size=128GB \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
-v $HOME:$HOME \
--name rocm7 \
rocm/dev-ubuntu-24.04:7.1.1-complete
```

```
run -it \
--cap-add=SYS_PTRACE \
--ipc=host \
--privileged=true \
--shm-size=128GB \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add video \
-v $HOME:$HOME \
--name rocm7 \
rocm/dev-ubuntu-22.04:7.1.1-complete
```

### Applications[#](#applications)

AMD provides pre-built images for various GPU-ready AI and HPC applications through
[Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html). There, you’ll also find examples
for invoking each application and suggested parameters used for benchmarking.
