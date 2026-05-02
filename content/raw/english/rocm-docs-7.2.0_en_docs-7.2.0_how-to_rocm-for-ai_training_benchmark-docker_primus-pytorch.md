---
title: "Training a model with Primus and PyTorch"
source_url: "https://rocm.docs.amd.com/en/docs-7.2.0/how-to/rocm-for-ai/training/benchmark-docker/primus-pytorch.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T12:04:51.409782+00:00
content_hash: "85c989dff0b08b07"
---

# Training a model with Primus and PyTorch[#](#training-a-model-with-primus-and-pytorch)

2026-02-24

16 min read time

[Primus](https://github.com/AMD-AGI/Primus) is a unified and flexible
LLM training framework designed to streamline training. It streamlines LLM
training on AMD Instinct GPUs using a modular, reproducible configuration paradigm.
Primus now supports the PyTorch torchtitan backend.

Note

For a unified training solution on AMD GPUs with ROCm, the [rocm/pytorch-training](https://hub.docker.com/r/rocm/pytorch-training/) Docker Hub registry will be
deprecated soon in favor of [rocm/primus](https://hub.docker.com/r/rocm/primus).
The `rocm/primus`

Docker containers will cover PyTorch training ecosystem frameworks,
including torchtitan and [Megatron-LM](primus-megatron.html).

Primus with the PyTorch torchtitan backend is designed to replace the
[ROCm PyTorch training](pytorch-training.html) workflow. See
[Training a model with PyTorch on ROCm](pytorch-training.html) to see steps to run workloads without Primus.

AMD provides a ready-to-use Docker image for MI355X, MI350X, MI325X, and MI300X GPUs containing essential components for Primus and PyTorch training with Primus Turbo optimizations.

Software component |
Version |
|---|---|
ROCm |
7.1.0 |
PyTorch |
2.10.0.dev20251112+rocm7.1 |
Python |
3.10 |
Transformer Engine |
2.6.0.dev0+f141f34b |
Flash Attention |
2.8.3 |
hipBLASLt |
34459f66ea |

## Supported models[#](#supported-models)

The following models are pre-optimized for performance on the AMD Instinct MI325X and MI300X GPUs. Some instructions, commands, and training recommendations in this documentation might vary by model – select one to get started.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

This Docker image is optimized for specific model configurations outlined below. Performance can vary for other training workloads, as AMD doesn’t test configurations and run conditions outside those described.

## Pull the Docker image[#](#pull-the-docker-image)

Use the following command to pull the Docker image from Docker Hub.

```
pull rocm/primus:v26.1
```

## Run training[#](#run-training)

Once the setup is complete, choose between the following two workflows to start benchmarking training.
For fine-tuning workloads and multi-node training examples, see [Training a model with PyTorch on ROCm](pytorch-training.html) (without Primus).
For best performance on MI325X, MI350X, and MI355X GPUs, you might need to
tweak some configurations (such as batch sizes).

The following run commands are tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v26-01) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.1`

Docker image from Docker Hub.pull rocm/primus:v26.1

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.1

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

The Docker container hosts verified commit

`9c529cd4`

of the[Primus](https://github.com/AMD-AGI/Primus/tree/9c529cd4a934a68a880ede036c3e97b792e38167/)repository.

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

Pretraining

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Benchmarking examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
--training.local_batch_size 6
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
--training.local_batch_size 7
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
--training.local_batch_size 6
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
--training.local_batch_size 5
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
--training.local_batch_size 10
```

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run commands are tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v26-01) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.1`

Docker image from Docker Hub.pull rocm/primus:v26.1

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.1

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

The Docker container hosts verified commit

`9c529cd4`

of the[Primus](https://github.com/AMD-AGI/Primus/tree/9c529cd4a934a68a880ede036c3e97b792e38167/)repository.

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

Pretraining

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Benchmarking examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
--training.local_batch_size 6
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
--training.local_batch_size 7
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
--training.local_batch_size 6
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
--training.local_batch_size 5
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
--training.local_batch_size 10
```

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run commands are tailored to DeepSeek V3 16B.
See [Supported models](#amd-primus-pytorch-model-support-v26-01) to switch to another available model.

Download the Docker image and required packages

Pull the

`rocm/primus:v26.1`

Docker image from Docker Hub.pull rocm/primus:v26.1

Run the Docker container.

run -it \ --device /dev/dri \ --device /dev/kfd \ --network host \ --ipc host \ --group-add video \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --privileged \ -v $HOME:$HOME \ -v $HOME/.ssh:/root/.ssh \ --shm-size 64G \ --name training_env \ rocm/primus:v26.1

Use these commands if you exit the

`training_env`

container and need to return to it.start training_env docker exec -it training_env bash

The Docker container hosts verified commit

`9c529cd4`

of the[Primus](https://github.com/AMD-AGI/Primus/tree/9c529cd4a934a68a880ede036c3e97b792e38167/)repository.

Prepare training datasets and dependencies

The following benchmarking examples require downloading models and datasets
from Hugging Face. To ensure successful access to gated repos, set your
`HF_TOKEN`

.

```
export HF_TOKEN=$your_personal_hugging_face_access_token
```

Pretraining

To get started, navigate to the `Primus`

directory in your container.

```
cd /workspace/Primus
```

Now, to start the pretraining benchmark, use the `run_pretrain.sh`

script
included with Primus with the appropriate options.

Benchmarking examples

Use the following command to run train Llama 3.1 8B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-BF16-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml \
--training.local_batch_size 6
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-BF16-pretrain.yaml
```

To train Llama 3.1 8B with FP8 precision, use the following command.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_8B-FP8-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml \
--training.local_batch_size 7
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_8B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_8B-FP8-pretrain.yaml
```

Use the following command to run train Llama 3.1 70B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-BF16-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml \
--training.local_batch_size 6
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-BF16-pretrain.yaml
```

To train Llama 3.1 70B with FP8 precision, use the following command.

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/llama3.1_70B-FP8-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml \
--training.local_batch_size 5
```

```
runner/primus-cli direct \
--log_file /tmp/primus_llama3.1_70B_fp8.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/llama3.1_70B-FP8-pretrain.yaml
```

Use the following command to run train DeepSeek V3 16B with BF16 precision using Primus torchtitan.

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI355X/deepseek_v3_16b-pretrain.yaml
```

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml \
--training.local_batch_size 10
```

```
runner/primus-cli direct \
--log_file /tmp/primus_deepseek_v3_16b.log \
-- train pretrain \
--config examples/torchtitan/configs/MI300X/deepseek_v3_16b-pretrain.yaml
```

The following run command is tailored to Llama 3.1 8B.
See [Supported models](#amd-primus-pytorch-model-support-v26-01) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 8B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-8b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-8b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to Llama 3.1 70B.
See [Supported models](#amd-primus-pytorch-model-support-v26-01) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the Llama 3.1 70B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_llama-3.1-70b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_llama-3.1-70b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

The following run command is tailored to DeepSeek V3 16B.
See [Supported models](#amd-primus-pytorch-model-support-v26-01) to switch to another available model.

Clone the ROCm Model Automation and Dashboarding (

[ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and install the required packages on the host machine.clone https://github.com/ROCm/MAD cd MAD pip install -r requirements.txt

For example, use this command to run the performance benchmark test on the DeepSeek V3 16B model using one node with the BF16 data type on the host machine.

export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models" madengine run \ --tags primus_pyt_train_deepseek-v3-16b \ --keep-model-dir \ --live-output \ --timeout 28800

MAD launches a Docker container with the name

`container_ci-primus_pyt_train_deepseek-v3-16b`

. The latency and throughput reports of the model are collected in`~/MAD/perf.csv`

.

## Further reading[#](#further-reading)

For an introduction to Primus, see

[Primus: A Lightweight, Unified Training Framework for Large Models on AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/primus/README.html).To learn more about MAD and the

`madengine`

CLI, see the[MAD usage guide](https://github.com/ROCm/MAD?tab=readme-ov-file#usage-guide).To learn more about system settings and management practices to configure your system for AMD Instinct MI300X Series GPUs, see

[AMD Instinct MI300X system optimization](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/system-optimization/mi300x.html).For a list of other ready-made Docker images for AI with ROCm, see

[AMD Infinity Hub](https://www.amd.com/en/developer/resources/infinity-hub.html#f-amd_hub_category=AI%20%26%20ML%20Models).

## Previous versions[#](#previous-versions)

See [PyTorch training performance testing version history](previous-versions/pytorch-training-history.html) to find documentation for previous releases
of the `ROCm/pytorch-training`

Docker image.
