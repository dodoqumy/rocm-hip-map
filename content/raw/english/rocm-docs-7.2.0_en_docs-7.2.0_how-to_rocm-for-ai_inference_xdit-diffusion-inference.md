---
title: "xDiT diffusion inference"
source_url: "https://rocm.docs.amd.com/en/docs-7.2.0/how-to/rocm-for-ai/inference/xdit-diffusion-inference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:02:23.858625+00:00
content_hash: "69bd5cca8cb93b74"
---

# xDiT diffusion inference[#](#xdit-diffusion-inference)

2026-03-02

37 min read time

The [rocm/pytorch-xdit](https://hub.docker.com/layers/rocm/pytorch-xdit/v26.3/images/sha256-ac78a03d2911bf1b49c001d3be2e8bd745c1bc455cb49ae972825a7986880902) Docker image offers a prebuilt, optimized environment based on [xDiT](https://github.com/xdit-project/xDiT) for
benchmarking diffusion model video and image generation on gfx942 and gfx950 series (AMD Instinct™ MI300X, MI325X, MI350X, and MI355X) GPUs.
The image runs ROCm **7.12.0** (preview) based on [TheRock](https://github.com/ROCm/TheRock)
and includes the following components:

## Software components - xdit:v26.3

Software component |
Version |
|---|---|
e40a6da |
|
9e9e900 |
|
ca89a1a |
|
91be249 |
|
e3c6ee2 |
|
b919bd0 |
|
a272dfa |
|
46ba481 |
|
82d733f |
|
a80b192 |
|
2882027 |
|
631bdfd |

Follow this guide to pull the required image, spin up a container, download the model, and run a benchmark.
For preview and development releases, see [amdsiloai/pytorch-xdit](https://hub.docker.com/r/amdsiloai/pytorch-xdit).

## What’s new[#](#what-s-new)

Qwen-Image support

Qwen-Image-Edit support

Aiter update to support Sage attention v2

xDiT update to support MXFP4 GEMMs in Wan2.2, Wan2.1 and Flux.2


## Supported models[#](#supported-models)

The following models are supported for inference performance benchmarking. Some instructions, commands, and recommendations in this documentation might vary by model – select one to get started.

Note

To learn more about your specific model see the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo)
or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Hunyuan Video 1.5 model card on Hugging Face](https://huggingface.co/hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v)
or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Wan2.1 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P-Diffusers)
or visit the [GitHub page](https://github.com/Wan-Video/Wan2.1). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Wan2.2 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers)
or visit the [GitHub page](https://github.com/Wan-Video/Wan2.2). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [FLUX.1 model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev)
or visit the [GitHub page](https://github.com/black-forest-labs/flux). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [FLUX.1 Kontext model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)
or visit the [GitHub page](https://github.com/black-forest-labs/flux). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [FLUX.2 model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.2-dev)
or visit the [GitHub page](https://github.com/black-forest-labs/flux2). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [FLUX.2 Klein model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B)
or visit the [GitHub page](https://github.com/black-forest-labs/flux2). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [stable-diffusion-3.5-large model card on Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
or visit the [GitHub page](https://github.com/Stability-AI/sd3.5). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Z-Image Turbo model card on Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
or visit the [GitHub page](https://github.com/Tongyi-MAI/Z-Image). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [LTX-2 model card on Hugging Face](https://huggingface.co/Lightricks/LTX-2)
or visit the [GitHub page](https://github.com/Lightricks/LTX-2). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Qwen-Image model card on Hugging Face](https://huggingface.co/Qwen/Qwen-Image)
or visit the [GitHub page](https://github.com/QwenLM/Qwen-Image). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Qwen-Image-Edit model card on Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit)
or visit the [GitHub page](https://github.com/QwenLM/Qwen-Image). Note that some models require access authorization before use via an
external license agreement through a third party.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting.

To test for optimal performance, consult the recommended [System health benchmarks](../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Pull the Docker image[#](#pull-the-docker-image)

For this tutorial, it’s recommended to use the latest `rocm/pytorch-xdit:v26.3`

Docker image.
Pull the image using the following command:

```
pull rocm/pytorch-xdit:v26.3
```

## Validate and benchmark[#](#validate-and-benchmark)

Once the image has been downloaded you can follow these steps to run benchmarks and generate outputs.

The following commands are written for Hunyuan Video.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for Hunyuan Video 1.5.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for Wan2.1.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for Wan2.2.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for FLUX.1.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for FLUX.1 Kontext.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for FLUX.2.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for FLUX.2 Klein.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for stable-diffusion-3.5-large.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for Z-Image Turbo.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for LTX-2.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for Qwen-Image.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

The following commands are written for Qwen-Image-Edit.
See [Supported models](#xdit-video-diffusion-supported-models) to switch to another available model.

### Choose your setup method[#](#choose-your-setup-method)

You can either use an existing Hugging Face cache or download the model fresh inside the container.

If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download tencent/HunyuanVideo --revision refs/pr/18

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download tencent/HunyuanVideo --revision refs/pr/18

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Wan-AI/Wan2.2-I2V-A14B-Diffusers

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Wan-AI/Wan2.2-I2V-A14B-Diffusers

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download black-forest-labs/FLUX.1-dev

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download black-forest-labs/FLUX.1-dev

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download black-forest-labs/FLUX.1-Kontext-dev

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download black-forest-labs/FLUX.1-Kontext-dev

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download black-forest-labs/FLUX.2-dev

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download black-forest-labs/FLUX.2-dev

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download black-forest-labs/FLUX.2-klein-9B

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download black-forest-labs/FLUX.2-klein-9B

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download stabilityai/stable-diffusion-3.5-large

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download stabilityai/stable-diffusion-3.5-large

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Tongyi-MAI/Z-Image-Turbo

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Tongyi-MAI/Z-Image-Turbo

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Lightricks/LTX-2

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Lightricks/LTX-2

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Qwen/Qwen-Image

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Qwen/Qwen-Image

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Qwen/Qwen-Image-Edit

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v26.3


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v26.3

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Qwen/Qwen-Image-Edit

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


## Run inference[#](#run-inference)

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Hunyuan Video](https://huggingface.co/tencent/HunyuanVideo)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_hunyuanvideo \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_hunyuanvideo`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_hunyuanvideo_throughput.csv`

and `pyt_xdit_hunyuanvideo_serving.csv`

.

To run the benchmarks for Hunyuan Video, use the following command:

```
results
xdit \
--model tencent/HunyuanVideo \
--prompt "In the large cage, two puppies were wagging their tails at each other." \
--batch_size 1 \
--height 720 --width 1280 \
--seed 1168860793 \
--num_frames 129 \
--num_inference_steps 50 \
--warmup_calls 1 \
--num_iterations 1 \
--ulysses_degree 8 \
--enable_tiling --enable_slicing \
--guidance_scale 6.0 \
--use_torch_compile \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Hunyuan Video 1.5](https://huggingface.co/hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_hunyuanvideo_1_5 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_hunyuanvideo_1_5`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_hunyuanvideo_1_5_throughput.csv`

and `pyt_xdit_hunyuanvideo_1_5_serving.csv`

.

To run the benchmarks for Hunyuan Video 1.5, use the following command:

```
results
xdit \
--model hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v \
--prompt "In the large cage, two puppies were wagging their tails at each other." \
--task t2v \
--height 720 --width 1280 \
--seed 1168860793 \
--num_frames 129 \
--num_inference_steps 50 \
--num_iterations 1 \
--ulysses_degree 8 \
--enable_tiling --enable_slicing \
--use_torch_compile \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Wan2.1](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P-Diffusers)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_wan_2_1 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_wan_2_1`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_wan_2_1_throughput.csv`

and `pyt_xdit_wan_2_1_serving.csv`

.

To run the benchmarks for Wan2.1, use the following command:

```
results
xdit \
--model Wan-AI/Wan2.1-I2V-14B-720P-Diffusers \
--prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--height 720 \
--width 1280 \
--input_images /app/data/wan_input.jpg \
--num_frames 81 \
--ulysses_degree 8 \
--seed 42 \
--num_iterations 1 \
--num_inference_steps 40 \
--use_torch_compile \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Wan2.2](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_wan_2_2 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_wan_2_2`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_wan_2_2_throughput.csv`

and `pyt_xdit_wan_2_2_serving.csv`

.

To run the benchmarks for Wan2.2, use the following command:

```
results
xdit \
--model Wan-AI/Wan2.2-I2V-A14B-Diffusers \
--prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--height 720 \
--width 1280 \
--input_images /app/data/wan_input.jpg \
--num_frames 81 \
--ulysses_degree 8 \
--seed 42 \
--num_iterations 1 \
--num_inference_steps 40 \
--use_torch_compile \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[FLUX.1](https://huggingface.co/black-forest-labs/FLUX.1-dev)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_flux \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_flux`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_flux_throughput.csv`

and `pyt_xdit_flux_serving.csv`

.

To run the benchmarks for FLUX.1, use the following command:

```
results
xdit \
--model black-forest-labs/FLUX.1-dev \
--seed 42 \
--prompt "A small cat" \
--height 1024 \
--width 1024 \
--num_inference_steps 25 \
--max_sequence_length 256 \
--warmup_calls 5 \
--ulysses_degree 8 \
--use_torch_compile \
--guidance_scale 0.0 \
--num_iterations 50 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[FLUX.1 Kontext](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_flux_kontext \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_flux_kontext`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_flux_kontext_throughput.csv`

and `pyt_xdit_flux_kontext_serving.csv`

.

To run the benchmarks for FLUX.1 Kontext, use the following command:

```
results
xdit \
--model black-forest-labs/FLUX.1-Kontext-dev \
--seed 42 \
--prompt "Add a cool hat to the cat" \
--height 1024 \
--width 1024 \
--num_inference_steps 30 \
--max_sequence_length 512 \
--warmup_calls 5 \
--ulysses_degree 8 \
--use_torch_compile \
--input_images /app/data/flux_cat.png \
--guidance_scale 2.5 \
--num_iterations 25 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[FLUX.2](https://huggingface.co/black-forest-labs/FLUX.2-dev)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_flux_2 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_flux_2`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_flux_2_throughput.csv`

and `pyt_xdit_flux_2_serving.csv`

.

To run the benchmarks for FLUX.2, use the following command:

```
results
xdit \
--model black-forest-labs/FLUX.2-dev \
--seed 42 \
--prompt "Add a cool hat to the cat" \
--height 1024 \
--width 1024 \
--num_inference_steps 50 \
--max_sequence_length 512 \
--warmup_calls 5 \
--ulysses_degree 8 \
--use_torch_compile \
--input_images /app/data/flux_cat.png \
--guidance_scale 4.0 \
--num_iterations 25 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[FLUX.2 Klein](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_flux_2_klein \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_flux_2_klein`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_flux_2_klein_throughput.csv`

and `pyt_xdit_flux_2_klein_serving.csv`

.

To run the benchmarks for FLUX.2 Klein, use the following command:

```
results
xdit \
--model black-forest-labs/FLUX.2-klein-9B \
--seed 42 \
--prompt "A spectacular sunset over the ocean" \
--height 2048 \
--width 2048 \
--num_inference_steps 4 \
--warmup_calls 5 \
--ulysses_degree 8 \
--use_torch_compile \
--guidance_scale 1.0 \
--num_iterations 25 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_sd_3_5 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_sd_3_5`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_sd_3_5_throughput.csv`

and `pyt_xdit_sd_3_5_serving.csv`

.

To run the benchmarks for stable-diffusion-3.5-large, use the following command:

```
results
xdit \
--model stabilityai/stable-diffusion-3.5-large \
--prompt "A capybara holding a sign that reads Hello World" \
--num_iterations 50 \
--num_inference_steps 28 \
--pipefusion_parallel_degree 4 \
--use_cfg_parallel \
--use_torch_compile \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Z-Image Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_z_image_turbo \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_z_image_turbo`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_z_image_turbo_throughput.csv`

and `pyt_xdit_z_image_turbo_serving.csv`

.

To run the benchmarks for Z-Image Turbo, use the following command:

```
results
xdit \
--model Tongyi-MAI/Z-Image-Turbo \
--seed 42 \
--prompt "A crowded beach" \
--height 1088 \
--width 1920 \
--num_inference_steps 9 \
--ulysses_degree 2 \
--use_torch_compile \
--guidance_scale 0.0 \
--num_iterations 50 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[LTX-2](https://huggingface.co/Lightricks/LTX-2)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_ltx2 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_ltx2`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_ltx2_throughput.csv`

and `pyt_xdit_ltx2_serving.csv`

.

To run the benchmarks for LTX-2, use the following command:

```
results
xdit \
--model Lightricks/LTX-2 \
--seed 42 \
--prompt "Cinematic action packed shot. The man says silently: \"We need to run.\". The camera zooms in on his mouth then immediately screams: \"NOW!\". The camera zooms back out, he turns around and bolts it." \
--height 1088 \
--width 1920 \
--num_inference_steps 40 \
--ulysses_degree 8 \
--use_torch_compile \
--guidance_scale 4.0 \
--num_iterations 1 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Qwen-Image](https://huggingface.co/Qwen/Qwen-Image)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_qwen_image \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_qwen_image`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_qwen_image_throughput.csv`

and `pyt_xdit_qwen_image_serving.csv`

.

To run the benchmarks for Qwen-Image, use the following command:

```
results
xdit \
--model Qwen/Qwen-Image \
--seed 42 \
--prompt "A cat holding a sign that says hello world" \
--height 2048 \
--width 2048 \
--num_inference_steps 50 \
--ulysses_degree 8 \
--use_torch_compile \
--num_iterations 1 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Qwen-Image-Edit](https://huggingface.co/Qwen/Qwen-Image-Edit)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_qwen_image_edit \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_qwen_image_edit`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_qwen_image_edit_throughput.csv`

and `pyt_xdit_qwen_image_edit_serving.csv`

.

To run the benchmarks for Qwen-Image-Edit, use the following command:

```
results
xdit \
--model Qwen/Qwen-Image-Edit \
--seed 42 \
--prompt "Add a cool hat to the cat." \
--negative_prompt "" \
--input_images /app/data/flux_cat.png \
--height 2048 \
--width 2048 \
--num_inference_steps 50 \
--ulysses_degree 8 \
--use_torch_compile \
--num_iterations 1 \
--attention_backend aiter \
--output_directory results
```

The generated content and timing information will be stored under the results directory.

## Previous versions[#](#previous-versions)

See
[xDiT diffusion inference performance testing version history](benchmark-docker/previous-versions/xdit-history.html)
to find documentation for previous releases of xDiT diffusion inference
performance testing.
