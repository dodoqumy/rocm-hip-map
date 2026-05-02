---
title: "xDiT diffusion inference"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/xdit-25.10.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T18:01:35.694806+00:00
content_hash: "41f60290062e4214"
---

# xDiT diffusion inference[#](#xdit-diffusion-inference)

2026-04-21

16 min read time

The [rocm/pytorch-xdit](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.10/images/sha256-d79715ff18a9470e3f907cec8a9654d6b783c63370b091446acffc0de4d7070e) Docker image offers
a prebuilt, optimized inference environment based on [xDiT](https://github.com/xdit-project/xDiT) for benchmarking diffusion-based
video and image generation on AMD Instinct MI355X, MI350X (gfx950), MI325X,
and MI300X (gfx942) GPUs.
This image is based on ROCm 7.9.0 preview release via [TheRock](https://github.com/ROCm/TheRock)
and includes the following software components:

Software component |
Version |
|---|---|
TheRock |
7afbe45 |
rccl |
9b04b2a |
composable_kernel |
b7a806f |
rocm-libraries |
f104555 |
rocm-systems |
25922d0 |
torch |
2.10.0a0+gite9c9017 |
torchvision |
0.22.0a0+966da7e |
triton |
3.5.0+git52e49c12 |
accelerate |
1.11.0.dev0 |
aiter |
0.1.5.post4.dev20+ga25e55e79 |
diffusers |
0.36.0.dev0 |
xfuser |
0.4.4 |
yunchang |
0.6.3.post1 |

Follow this guide to pull the required image, spin up a container, download the model, and run a benchmark.
For preview and development releases, see [amdsiloai/pytorch-xdit](https://hub.docker.com/r/amdsiloai/pytorch-xdit).

## What’s new[#](#what-s-new)

Initial ROCm-enabled xDiT Docker release for diffusion inference.

Supported architectures: gfx942 and gfx950 (AMD Instinct™ MI300X, MI325X, MI350X, and MI355X).

Supported workloads: Wan 2.1, Wan 2.2, HunyuanVideo, and Flux models.


## Supported models[#](#supported-models)

The following models are supported for inference performance benchmarking. Some instructions, commands, and recommendations in this documentation might vary by model – select one to get started.

Note

To learn more about your specific model see the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo)
or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Wan2.1 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P)
or visit the [GitHub page](https://github.com/Wan-Video/Wan2.1). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [Wan2.2 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B)
or visit the [GitHub page](https://github.com/Wan-Video/Wan2.2). Note that some models require access authorization before use via an
external license agreement through a third party.

Note

To learn more about your specific model see the [FLUX.1 model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev)
or visit the [GitHub page](https://github.com/black-forest-labs/flux). Note that some models require access authorization before use via an
external license agreement through a third party.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA
auto-balancing, you can skip this step. Otherwise, complete the procedures in
the [System validation and optimization](https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/system-setup/prerequisite-system-validation.html)
guide to properly configure your system settings before starting.

## Pull the Docker image[#](#pull-the-docker-image)

For this tutorial, it’s recommended to use the latest `rocm/pytorch-xdit:v25.10`

Docker image.
Pull the image using the following command:

```
pull rocm/pytorch-xdit:v25.10
```

## Validate and benchmark[#](#validate-and-benchmark)

Once the image has been downloaded you can follow these steps to run benchmarks and generate outputs.

The following commands are written for Hunyuan Video.
See [Supported models](#xdit-video-diffusion-supported-models-2510) to switch to another available model.

The following commands are written for Wan2.1.
See [Supported models](#xdit-video-diffusion-supported-models-2510) to switch to another available model.

The following commands are written for Wan2.2.
See [Supported models](#xdit-video-diffusion-supported-models-2510) to switch to another available model.

The following commands are written for FLUX.1.
See [Supported models](#xdit-video-diffusion-supported-models-2510) to switch to another available model.

### Prepare the model[#](#prepare-the-model)

Note

If you’re using ROCm MAD to [run your model](#xdit-video-diffusion-run-2510), you can skip this section. MAD will handle
starting the container and downloading required models inside the container.

You can either use an existing Hugging Face cache or download the model fresh inside the container.

If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download tencent/HunyuanVideo --revision refs/pr/18

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.10


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.10

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download tencent/HunyuanVideo --revision refs/pr/18

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Wan-AI/Wan2.1-I2V-14B-720P

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.10


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.10

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Wan-AI/Wan2.1-I2V-14B-720P

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download Wan-AI/Wan2.2-I2V-A14B

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.10


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.10

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download Wan-AI/Wan2.2-I2V-A14B

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


If you already have models downloaded on your host system, you can mount your existing cache.

Set your Hugging Face cache location.

export HF_HOME=/your/hf_cache/location

Download the model (if not already cached).

download black-forest-labs/FLUX.1-dev

Launch the container with mounted cache.

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ -e HF_HOME=/app/huggingface_models \ -v $HF_HOME:/app/huggingface_models \ rocm/pytorch-xdit:v25.10


If you prefer to keep the container self-contained or don’t have an existing cache.

Launch the container

run \ -it --rm \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ --user root \ --device=/dev/kfd \ --device=/dev/dri \ --group-add video \ --ipc=host \ --network host \ --privileged \ --shm-size 128G \ --name pytorch-xdit \ -e HSA_NO_SCRATCH_RECLAIM=1 \ -e OMP_NUM_THREADS=16 \ -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \ rocm/pytorch-xdit:v25.10

Inside the container, set the Hugging Face cache location and download the model.

export HF_HOME=/app/huggingface_models huggingface-cli download black-forest-labs/FLUX.1-dev

Warning

Models will be downloaded to the container’s filesystem and will be lost when the container is removed unless you persist the data with a volume.


## Run inference[#](#run-inference)

You can benchmark models through [MAD](https://github.com/ROCm/MAD)-integrated automation or standalone
torchrun commands.

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

[Wan2.1](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_wan_2_1 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_wan_2_1`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_wan_2_1_throughput.csv`

and `pyt_xdit_wan_2_1_serving.csv`

.

To run the benchmarks for Wan2.1, use the following command:

```
cd Wan2.1
mkdir results
torchrun --nproc_per_node=8 run.py \
--task i2v-14B \
--size 720*1280 --frame_num 81 \
--ckpt_dir "${HF_HOME}/hub/models--Wan-AI--Wan2.1-I2V-14B-720P/snapshots/8823af45fcc58a8aa999a54b04be9abc7d2aac98/" \
--image "/app/Wan2.1/examples/i2v_input.JPG" \
--ulysses_size 8 --ring_size 1 \
--prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--benchmark_output_directory results --save_file video.mp4 --num_benchmark_steps 1 \
--offload_model 0 \
--vae_dtype bfloat16 \
--allow_tf32 \
--compile
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/outputs/rank0_*.json

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

On the host machine, use this command to run the performance benchmark test on the

[Wan2.2](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B)model using one node.export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags pyt_xdit_wan_2_2 \ --keep-model-dir \ --live-output


MAD launches a Docker container with the name
`container_ci-pyt_xdit_wan_2_2`

. The throughput and serving reports of the
model are collected in the following paths: `pyt_xdit_wan_2_2_throughput.csv`

and `pyt_xdit_wan_2_2_serving.csv`

.

To run the benchmarks for Wan2.2, use the following command:

```
cd Wan2.2
mkdir results
torchrun --nproc_per_node=8 run.py \
--task i2v-A14B \
--size 720*1280 --frame_num 81 \
--ckpt_dir "${HF_HOME}/hub/models--Wan-AI--Wan2.2-I2V-A14B/snapshots/206a9ee1b7bfaaf8f7e4d81335650533490646a3/" \
--image "/app/Wan2.2/examples/i2v_input.JPG" \
--ulysses_size 8 --ring_size 1 \
--prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
--benchmark_output_directory results --save_file video.mp4 --num_benchmark_steps 1 \
--offload_model 0 \
--vae_dtype bfloat16 \
--allow_tf32 \
--compile
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
cd Flux
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
--num_repetitions 1 \
--benchmark_output_directory results
```

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/timing.json

You may also use `run_usp.py`

which implements USP without modifying the default diffusers pipeline.

## Further reading[#](#further-reading)

To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [xDiT diffusion inference performance testing version history](xdit-history.html) to find documentation for previous releases
of xDiT diffusion inference performance testing.
