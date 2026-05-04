---
title: "Running RCCL using Docker &#8212; RCCL 2.27.7 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rccl/en/latest/install/docker-install.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:22:54.944665+00:00
content_hash: "c88408d7f66dc3b2"
---

# Running RCCL using Docker[#](#running-rccl-using-docker)

To use Docker to run RCCL, Docker must already be installed on the system. To build the Docker image and run the container, follow these steps.

Build the Docker image

By default, the Dockerfile uses

`docker.io/rocm/dev-ubuntu-22.04:latest`

as the base Docker image. It then installs RCCL and rccl-tests (in both cases, it uses the version from the`develop`

branch).Use this command to build the Docker image:

build -t rccl-tests -f Dockerfile.ubuntu --pull .

The base Docker image, rccl repository, rccl-tests repository, and GPU targets can be modified by using

`--build-args`

in the`docker build`

command above. For example, to use a different base Docker image for the MI250 GPU, use this command:build -t rccl-tests -f Dockerfile.ubuntu --build-arg="ROCM_IMAGE_NAME=rocm/dev-ubuntu-20.04" --build-arg="ROCM_IMAGE_TAG=6.2" --build-arg="GPU_TARGETS=gfx90a" --pull .

Launch an interactive Docker container on a system with AMD GPUs:

run --rm --device=/dev/kfd --device=/dev/dri --group-add video --ipc=host --network=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -it rccl-tests /bin/bash


To run, for example, the `all_reduce_perf`

test from rccl-tests on 8 AMD GPUs from inside the Docker container, use this command
for ROCm 6.4.1 or earlier:

```
--allow-run-as-root -np 8 --mca pml ucx --mca btl ^openib -x NCCL_DEBUG=VERSION -x HSA_NO_SCRATCH_RECLAIM=1 /workspace/rccl-tests/build/all_reduce_perf -b 1 -e 16G -f 2 -g 1
```

For ROCm 6.4.2 or later, use this command:

```
--allow-run-as-root -np 8 --mca pml ucx --mca btl ^openib -x NCCL_DEBUG=VERSION /workspace/rccl-tests/build/all_reduce_perf -b 1 -e 16G -f 2 -g 1
```

For more information on the rccl-tests options, see the [Usage guidelines](https://github.com/ROCm/rccl-tests#usage) in the GitHub repository.
