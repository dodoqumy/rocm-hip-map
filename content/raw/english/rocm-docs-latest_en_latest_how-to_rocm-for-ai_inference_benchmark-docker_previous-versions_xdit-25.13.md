---
title: "xDiT diffusion inference"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/xdit-25.13.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T08:04:48.759708+00:00
content_hash: "8adc194f6f6976e8"
---

# xDiT diffusion inference[#](#xdit-diffusion-inference)

2026-04-21

23 min read time

Caution

This documentation does not reflect the latest version of the xDiT diffusion
inference performance documentation. See
[xDiT diffusion inference](../../xdit-diffusion-inference.html) for the latest
version.

The [rocm/pytorch-xdit](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.13/images/sha256-81954713070d67bde08595e03f62110c8a3dd66a9ae17a77d611e01f83f0f4ef) Docker image offers
a prebuilt, optimized environment based on [xDiT](https://github.com/xdit-project/xDiT) for benchmarking diffusion model
video and image generation on AMD Instinct MI355X, MI350X (gfx950), MI325X,
and MI300X (gfx942) GPUs.

The image runs a preview version of ROCm using the new [TheRock](https://github.com/ROCm/TheRock) build system and includes the following
components:

## Software components - xdit:v25.13

Software component |
Version |
|---|---|
1728a81 |
|
d23d18f |
|
ab0101c |
|
a2f7c35 |
|
659737c |
|
91be249 |
|
b919bd0 |
|
a272dfa |
|
b521400f |
|
de14bec0 |
|
a1f36ee3e |
|
adf2681 |
|
2c9b712 |

Follow this guide to pull the required image, spin up a container, download the model, and run a benchmark.
For preview and development releases, see [amdsiloai/pytorch-xdit](https://hub.docker.com/r/amdsiloai/pytorch-xdit).

## What’s new[#](#what-s-new)

Flux.1 Kontext support

Flux.2 Dev support

Flux FP8 GEMM support

Hybrid FP8 attention support for Wan models


## Supported models[#](#supported-models)

The following models are supported for inference performance benchmarking. Some instructions, commands, and recommendations in this documentation might vary by model – select one to get started.

Note

To learn more about your specific model see the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo)
or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo). Note that some models require access authorization before use via an
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

To learn more about your specific model see the [stable-diffusion-3.5-large model card on Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-3.5-large)
or visit the [GitHub page](https://github.com/Stability-AI/sd3.5). Note that some models require access authorization before use via an
external license agreement through a third party.

## Performance measurements[#](#performance-measurements)

To evaluate performance, the [Performance results with AMD ROCm software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8543b7e6d-item-9eda09e707-tab)
page provides reference throughput and serving measurements for inferencing popular AI models.

Important

The performance data presented in [Performance results with AMD ROCm
software](https://www.amd.com/en/developer/resources/rocm-hub/dev-ai/performance-results.html#tabs-a8543b7e6d-item-9eda09e707-tab)
only reflects the latest version of this inference benchmarking environment.
The listed measurements should not be interpreted as the peak performance
achievable by AMD Instinct GPUs or ROCm software.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting.

To test for optimal performance, consult the recommended [System health benchmarks](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Pull the Docker image[#](#pull-the-docker-image)

For this tutorial, it’s recommended to use the latest `rocm/pytorch-xdit:v25.13`

Docker image.
Pull the image using the following command:

```
pull rocm/pytorch-xdit:v25.13
```

## Validate and benchmark[#](#validate-and-benchmark)

Once the image has been downloaded you can follow these steps to run benchmarks and generate outputs.

The following commands are written for Hunyuan Video.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

The following commands are written for Wan2.1.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

The following commands are written for Wan2.2.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

The following commands are written for FLUX.1.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

The following commands are written for FLUX.1 Kontext.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

The following commands are written for FLUX.2.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

The following commands are written for stable-diffusion-3.5-large.
See [Supported models](#xdit-video-diffusion-supported-models-2513) to switch to another available model.

### Choose your setup method[#](#choose-your-setup-method)

You can either use an existing Hugging Face cache or download the model fresh inside the container.

If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download tencent/HunyuanVideo --revision refs/pr/18

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download tencent/HunyuanVideo --revision refs/pr/18

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

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

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

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

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

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

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

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

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download black-forest-labs/FLUX.2-dev

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download stabilityai/stable-diffusion-3.5-large

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.13


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.13

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download stabilityai/stable-diffusion-3.5-large

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
cd /app/Hunyuanvideo
mkdir results
torchrun --nproc_per_node=8 run.py \
--model tencent/HunyuanVideo \
--prompt "In the large cage, two puppies were wagging their tails at each other." \
--height 720 --width 1280 --num_frames 129 \
--num_inference_steps 50 --warmup_steps 1 --n_repeats 1 \
--ulysses_degree 8 \
--enable_tiling --enable_slicing \
--use_torch_compile \
--bench_output results
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see stdout.

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
cd /app/Wan
mkdir results
torchrun --nproc_per_node=8 /app/Wan/run.py \
--task i2v \
--height 720 \
--width 1280 \
--model Wan-AI/Wan2.1-I2V-14B-720P-Diffusers \
--img_file_path /app/Wan/i2v_input.JPG \
--ulysses_degree 8 \
--seed 42 \
--num_frames 81 \
--prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--num_repetitions 1 \
--num_inference_steps 40 \
--use_torch_compile
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/outputs/rank0_*.json

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
cd /app/Wan
mkdir results
torchrun --nproc_per_node=8 /app/Wan/run.py \
--task i2v \
--height 720 \
--width 1280 \
--model Wan-AI/Wan2.2-I2V-A14B-Diffusers \
--img_file_path /app/Wan/i2v_input.JPG \
--ulysses_degree 8 \
--seed 42 \
--num_frames 81 \
--prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--num_repetitions 1 \
--num_inference_steps 40 \
--use_torch_compile
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/outputs/rank0_*.json

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
cd /app/Flux
mkdir results
torchrun --nproc_per_node=8 /app/Flux/run.py \
--model black-forest-labs/FLUX.1-dev \
--seed 42 \
--prompt "A small cat" \
--height 1024 \
--width 1024 \
--num_inference_steps 25 \
--max_sequence_length 256 \
--warmup_steps 5 \
--no_use_resolution_binning \
--ulysses_degree 8 \
--use_torch_compile \
--num_repetitions 50
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/timing.json

You may also use `run_usp.py`

which implements USP without modifying the default diffusers pipeline.

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
cd /app/Flux
mkdir results
torchrun --nproc_per_node=8 /app/Flux/run_usp.py \
--model black-forest-labs/FLUX.1-Kontext-dev \
--seed 42 \
--prompt "Add a cool hat to the cat" \
--height 1024 \
--width 1024 \
--num_inference_steps 30 \
--max_sequence_length 512 \
--warmup_steps 5 \
--no_use_resolution_binning \
--ulysses_degree 8 \
--use_torch_compile \
--img_file_path /app/Flux/cat.png \
--model_type flux_kontext \
--guidance_scale 2.5 \
--num_repetitions 25
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/timing.json

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
cd /app/Flux
mkdir results
torchrun --nproc_per_node=8 /app/Flux/run_usp.py \
--model black-forest-labs/FLUX.2-dev \
--seed 42 \
--prompt "Add a cool hat to the cat" \
--height 1024 \
--width 1024 \
--num_inference_steps 50 \
--max_sequence_length 512 \
--warmup_steps 5 \
--no_use_resolution_binning \
--ulysses_degree 8 \
--use_torch_compile \
--img_file_paths /app/Flux/cat.png \
--model_type flux2 \
--guidance_scale 4.0 \
--num_repetitions 25
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/timing.json

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
cd /app/StableDiffusion3.5
mkdir results
torchrun --nproc_per_node=8 /app/StableDiffusion3.5/run.py \
--model stabilityai/stable-diffusion-3.5-large \
--num_inference_steps 28 \
--prompt "A capybara holding a sign that reads Hello World" \
--use_torch_compile \
--pipefusion_parallel_degree 4 \
--use_cfg_parallel \
--num_repetitions 50 \
--dtype torch.float16 \
--output_path results
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see benchmark_results.csv

## Previous versions[#](#previous-versions)

See
[xDiT diffusion inference performance testing version history](xdit-history.html)
to find documentation for previous releases of xDiT diffusion inference
performance testing.
