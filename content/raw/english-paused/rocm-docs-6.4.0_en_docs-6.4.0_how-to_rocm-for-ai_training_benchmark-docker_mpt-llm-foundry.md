---
title: "Training MPT-30B with LLM Foundry and ROCm"
source_url: "https://rocm.docs.amd.com/en/docs-6.4.0/how-to/rocm-for-ai/training/benchmark-docker/mpt-llm-foundry.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:16:47.847505+00:00
content_hash: "6e20b155f8d87b51"
---

# Training MPT-30B with LLM Foundry and ROCm[#](#training-mpt-30b-with-llm-foundry-and-rocm)

2025-05-13

6 min read time

MPT-30B is a 30-billion parameter decoder-style transformer-based model from
the Mosaic Pretrained Transformer (MPT) family – learn more about it in
MosaicML’s research blog [MPT-30B: Raising the bar for open-source foundation
models](https://www.databricks.com/blog/mpt-30b).

ROCm and [ROCm/MAD](https://github.com/ROCm/MAD) provide a pre-configured training
environment for the MPT-30B model using the `rocm/pytorch-training:v25.5`

base [Docker image](https://hub.docker.com/layers/rocm/pytorch-training/v25.5/images/sha256-d47850a9b25b4a7151f796a8d24d55ea17bba545573f0d50d54d3852f96ecde5)
and the [LLM Foundry](https://github.com/mosaicml/llm-foundry) framework.
This environment packages the following software components to train
on AMD Instinct MI300X series accelerators:

Software component |
Version |
|---|---|
ROCm |
6.3.4 |
PyTorch |
2.7.0a0+git6374332 |
Flash Attention |
3.0.0.post1 |

Using this image, you can build, run, and test the training process for MPT-30B with access to detailed logs and performance metrics.

## System validation[#](#system-validation)

Before running AI workloads, it’s important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you
can skip this step. Otherwise, complete the procedures in the [System validation and
optimization](../prerequisite-system-validation.html#rocm-for-ai-system-optimization) guide to properly configure your system settings
before starting training.

To test for optimal performance, consult the recommended [System health benchmarks](../../system-health-check.html#rocm-for-ai-system-health-bench). This suite of tests will help you verify and fine-tune your
system’s configuration.

## Getting started[#](#getting-started)

The following procedures help you set up the training environment in a reproducible Docker container. This training environment is tailored for training MPT-30B using LLM Foundry and the specific model configurations outlined. Other configurations and run conditions outside those described in this document are not validated.

On your host machine, clone the ROCm Model Automation and Dashboarding
([ROCm/MAD](https://github.com/ROCm/MAD)) repository to a local directory and
install the required packages.

```
clone https://github.com/ROCm/MAD
cd MAD
pip install -r requirements.txt
```

Use this command to initiate the MPT-30B training benchmark.

```
tools/run_models.py --tags pyt_mpt30b_training --keep-model-dir --live-output --clean-docker-cache
```

Tip

If you experience data download failures, set the
`MAD_SECRETS_HFTOKEN`

variable to your Hugging Face access token. See
[User access tokens](https://huggingface.co/docs/hub/security-tokens)
for details.

```
export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
```

Note

For improved performance (training throughput), consider enabling TunableOp.
By default, `pyt_mpt30b_training`

runs with TunableOp disabled. To enable it,
run `tools/run_models.py`

with the `--tunableop on`

argument or edit the
`models.json`

configuration before running training.

Although this might increase the initial training time, it can result in a performance gain.

To set up the training environment, clone the
[ROCm/MAD](https://github.com/ROCm/MAD) repo and build the Docker image. In
this snippet, the image is named `mosaic_mpt30_image`

.

```
clone https://github.com/ROCm/MAD
cd MAD
docker build --build-arg MAD_SYSTEM_GPU_ARCHITECTURE=gfx942 -f docker/pyt_mpt30b_training.ubuntu.amd.Dockerfile -t mosaic_mpt30_image .
```

Start a `mosaic_mpt30_image`

container using the following command.

```
run -it --device=/dev/kfd --device=/dev/dri --group-add=video --ipc=host --shm-size=8G mosaic_mpt30_image
```

In the Docker container, clone the [ROCm/MAD](https://github.com/ROCm/MAD)
repository and navigate to the benchmark scripts directory at
`/workspace/MAD/scripts/pyt_mpt30b_training`

.

```
clone https://github.com/ROCm/MAD
cd MAD/scripts/pyt_mpt30b_training
```

To initiate the training process, use the following command. This script uses the hyperparameters defined in
`mpt-30b-instruct.yaml`

.

```
source run.sh
```

Note

For improved performance (training throughput), consider enabling TunableOp.
To enable it, add the `--tunableop on`

flag.

```
source run.sh --tunableop on
```

Although this might increase the initial training time, it can result in a performance gain.

## Interpreting the output[#](#interpreting-the-output)

The training output will be displayed in the terminal and simultaneously saved
to the `output.txt`

file in the current directory. Key performance metrics will
also be extracted and appended to the `perf_pyt_mpt30b_training.csv`

file.

Key performance metrics include:

Training logs: Real-time display of loss metrics, accuracy, and training progress.

Model checkpoints: Periodically saved model snapshots for potential resume or evaluation.

Performance metrics: Detailed summaries of training speed and training loss metrics.

Performance (throughput/samples_per_sec)

Overall throughput, measuring the total samples processed per second. Higher values indicate better hardware utilization.

Performance per device (throughput/samples_per_sec)

Throughput on a per-device basis, showing how each GPU or CPU is performing.

Language Cross Entropy (metrics/train/LanguageCrossEntropy)

Measures prediction accuracy. Lower cross entropy suggests the model’s output is closer to the expected distribution.

Training loss (loss/train/total)

Overall training loss. A decreasing trend indicates the model is learning effectively.
