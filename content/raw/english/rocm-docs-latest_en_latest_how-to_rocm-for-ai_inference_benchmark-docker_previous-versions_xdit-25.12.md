---
title: "xDiT diffusion inference"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/previous-versions/xdit-25.12.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:56:07.713785+00:00
content_hash: "645db8d7146ab19e"
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# xDiT diffusion inference

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#xdit-diffusion-inference .section}
# xDiT diffusion inference[\#](#xdit-diffusion-inference "Link to this heading"){.headerlink}

::::::::
{#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::
{.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::
{.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::
{.sd-container-fluid .sd-sphinx-override .docutils}
::::
{.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 18 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

{.admonition .caution}
Caution

This documentation does not reflect the latest version of xDiT diffusion inference performance documentation. See [[xDiT diffusion inference]{.doc}](../../xdit-diffusion-inference.html){.reference .internal} for the latest version.

The [rocm/pytorch-xdit](https://hub.docker.com/layers/rocm/pytorch-xdit/v25.12/images/sha256-e06895132316bf3c393366b70a91eaab6755902dad0100e6e2b38310547d9256){.reference .external} Docker image offers a prebuilt, optimized environment based on [xDiT](https://github.com/xdit-project/xDiT){.reference .external} for benchmarking diffusion model video and image generation on AMD Instinct MI355X, MI350X (gfx950), MI325X, and MI300X (gfx942) GPUs.

The image runs ROCm **7.10.0** (preview) based on [TheRock](https://github.com/ROCm/TheRock){.reference .external} and includes the following components:

[Software components]{.sd-summary-text}[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiBoZWlnaHQ9IjEuNWVtIiB2ZXJzaW9uPSIxLjEiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjEuNWVtIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg==){.sd-octicon .sd-octicon-chevron-right}]{.sd-summary-state-marker .sd-summary-chevron-right}

:
{.sd-summary-content .sd-card-body .docutils}

pst-scrollable-table-container
  Software component                                                                       Version
  ---------------------------------------------------------------------------------------- ---------
  [TheRock](https://github.com/ROCm/TheRock){.reference .external}                         3e3f834
  [rccl](https://github.com/ROCm/rccl){.reference .external}                               d23d18f
  [composable_kernel](https://github.com/ROCm/composable_kernel){.reference .external}     2570462
  [rocm-libraries](https://github.com/ROCm/rocm-libraries){.reference .external}           0588f07
  [rocm-systems](https://github.com/ROCm/rocm-systems){.reference .external}               473025a
  [torch](https://github.com/pytorch/pytorch){.reference .external}                        73adac
  [torchvision](https://github.com/pytorch/vision){.reference .external}                   f5c6c2e
  [triton](https://github.com/triton-lang/triton){.reference .external}                    7416ffc
  [accelerate](https://github.com/huggingface/accelerate){.reference .external}            34c1779
  [aiter](https://github.com/ROCm/aiter){.reference .external}                             de14bec
  [diffusers](https://github.com/huggingface/diffusers){.reference .external}              40528e9
  [xfuser](https://github.com/xdit-project/xDiT){.reference .external}                     ccba9d5
  [yunchang](https://github.com/feifeibear/long-context-attention){.reference .external}   2c9b712

:

Follow this guide to pull the required image, spin up a container, download the model, and run a benchmark. For preview and development releases, see [amdsiloai/pytorch-xdit](https://hub.docker.com/r/amdsiloai/pytorch-xdit){.reference .external}.

{#what-s-new .section}
## What's new[\#](#what-s-new "Link to this heading"){.headerlink}

- Adds T2V and TI2V support for Wan models.

- Adds support for SD-3.5 T2I model.

::::::::::::::::::::::::::
{#supported-models .section}
[]{#xdit-video-diffusion-supported-models-2512}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for inference performance benchmarking. Some instructions, commands, and recommendations in this documentation might vary by model -- select one to get started.

:::::::::::::::
{#vllm-benchmark-ud-params-picker .container-fluid}
::::::
{.row .gx-0}

{.col-2 .me-1 .px-2 .model-param-head}
Model

::::
{.row .col-10 .pe-0}

{.col-6 .px-2 .model-param param-k="model-group" param-v="hunyuan" tabindex="0"}
Hunyuan Video

{.col-6 .px-2 .model-param param-k="model-group" param-v="wan" tabindex="0"}
Wan-AI

{.col-6 .px-2 .model-param param-k="model-group" param-v="flux" tabindex="0"}
FLUX

{.col-6 .px-2 .model-param param-k="model-group" param-v="stablediffusion" tabindex="0"}
Stable Diffusion

::::
::::::

:::::::
{.row .gx-0 .pt-1}

{.col-2 .me-1 .px-2 .model-param-head}
Variant

:::::
{.row .col-10 .pe-0}

{.col-6 .px-2 .model-param param-group="hunyuan" param-k="model" param-v="hunyuan_tag" tabindex="0"}
Hunyuan Video

{.col-6 .px-2 .model-param param-group="wan" param-k="model" param-v="wan_21_tag" tabindex="0"}
Wan2.1

{.col-6 .px-2 .model-param param-group="wan" param-k="model" param-v="wan_22_tag" tabindex="0"}
Wan2.2

{.col-6 .px-2 .model-param param-group="flux" param-k="model" param-v="flux_1_tag" tabindex="0"}
FLUX.1

{.col-6 .px-2 .model-param param-group="stablediffusion" param-k="model" param-v="stable_diffusion_3_5_large_tag" tabindex="0"}
stable-diffusion-3.5-large

:::::
:::::::
:::::::::::::::

:
{.model-doc .hunyuan-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo){.reference .external} or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .wan-21-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Wan2.1 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P-Diffusers){.reference .external} or visit the [GitHub page](https://github.com/Wan-Video/Wan2.1){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .wan-22-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Wan2.2 model card on Hugging Face](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers){.reference .external} or visit the [GitHub page](https://github.com/Wan-Video/Wan2.2){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .flux-1-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [FLUX.1 model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-dev){.reference .external} or visit the [GitHub page](https://github.com/black-forest-labs/flux){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .stable-diffusion-3-5-large-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [stable-diffusion-3.5-large model card on Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-3.5-large){.reference .external} or visit the [GitHub page](https://github.com/Stability-AI/sd3.5){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:
::::::::::::::::::::::::::

{#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../../../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../../../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

::
{#pull-the-docker-image .section}
## Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

For this tutorial, it's recommended to use the latest [`rocm/pytorch-xdit:v25.12`{.docutils .literal .notranslate}]{.pre} Docker image. Pull the image using the following command:

:
{.highlight-shell .notranslate}

highlight
    docker pull rocm/pytorch-xdit:v25.12

:
::

::::::::::::::::::::::::::
{#validate-and-benchmark .section}
## Validate and benchmark[\#](#validate-and-benchmark "Link to this heading"){.headerlink}

Once the image has been downloaded you can follow these steps to run benchmarks and generate outputs.

{.model-doc .hunyuan-tag .docutils .container}
The following commands are written for Hunyuan Video. See [[Supported models]{.std .std-ref}](../../xdit-diffusion-inference.html#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .wan-21-tag .docutils .container}
The following commands are written for Wan2.1. See [[Supported models]{.std .std-ref}](../../xdit-diffusion-inference.html#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .wan-22-tag .docutils .container}
The following commands are written for Wan2.2. See [[Supported models]{.std .std-ref}](../../xdit-diffusion-inference.html#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .flux-1-tag .docutils .container}
The following commands are written for FLUX.1. See [[Supported models]{.std .std-ref}](../../xdit-diffusion-inference.html#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .stable-diffusion-3-5-large-tag .docutils .container}
The following commands are written for stable-diffusion-3.5-large. See [[Supported models]{.std .std-ref}](../../xdit-diffusion-inference.html#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

::::::::::::::::::::
{#choose-your-setup-method .section}
### Choose your setup method[\#](#choose-your-setup-method "Link to this heading"){.headerlink}

You can either use an existing Hugging Face cache or download the model fresh inside the container.

{.model-doc .hunyuan-tag .docutils .container}
::
{.sd-tab-set .docutils}
Option 1: Use existing Hugging Face cache

{.sd-tab-content .docutils}
If you already have models downloaded on your host system, you can mount your existing cache.

1.  Set your Hugging Face cache location.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/your/hf_cache/location
    
    :

2.  Download the model (if not already cached).

    :
{.highlight-shell .notranslate}
    
highlight
        huggingface-cli download tencent/HunyuanVideo  --revision refs/pr/18 
    
    :

3.  Launch the container with mounted cache.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            -e HF_HOME=/app/huggingface_models \
            -v $HF_HOME:/app/huggingface_models \
            rocm/pytorch-xdit:v25.12
    
    :

Option 2: Download inside container

{.sd-tab-content .docutils}
If you prefer to keep the container self-contained or don't have an existing cache.

1.  Launch the container

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            rocm/pytorch-xdit:v25.12
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        huggingface-cli download tencent/HunyuanVideo  --revision refs/pr/18 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .wan-21-tag .docutils .container}
::
{.sd-tab-set .docutils}
Option 1: Use existing Hugging Face cache

{.sd-tab-content .docutils}
If you already have models downloaded on your host system, you can mount your existing cache.

1.  Set your Hugging Face cache location.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/your/hf_cache/location
    
    :

2.  Download the model (if not already cached).

    :
{.highlight-shell .notranslate}
    
highlight
        huggingface-cli download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers 
    
    :

3.  Launch the container with mounted cache.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            -e HF_HOME=/app/huggingface_models \
            -v $HF_HOME:/app/huggingface_models \
            rocm/pytorch-xdit:v25.12
    
    :

Option 2: Download inside container

{.sd-tab-content .docutils}
If you prefer to keep the container self-contained or don't have an existing cache.

1.  Launch the container

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            rocm/pytorch-xdit:v25.12
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        huggingface-cli download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .wan-22-tag .docutils .container}
::
{.sd-tab-set .docutils}
Option 1: Use existing Hugging Face cache

{.sd-tab-content .docutils}
If you already have models downloaded on your host system, you can mount your existing cache.

1.  Set your Hugging Face cache location.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/your/hf_cache/location
    
    :

2.  Download the model (if not already cached).

    :
{.highlight-shell .notranslate}
    
highlight
        huggingface-cli download Wan-AI/Wan2.2-I2V-A14B-Diffusers 
    
    :

3.  Launch the container with mounted cache.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            -e HF_HOME=/app/huggingface_models \
            -v $HF_HOME:/app/huggingface_models \
            rocm/pytorch-xdit:v25.12
    
    :

Option 2: Download inside container

{.sd-tab-content .docutils}
If you prefer to keep the container self-contained or don't have an existing cache.

1.  Launch the container

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            rocm/pytorch-xdit:v25.12
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        huggingface-cli download Wan-AI/Wan2.2-I2V-A14B-Diffusers 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .flux-1-tag .docutils .container}
::
{.sd-tab-set .docutils}
Option 1: Use existing Hugging Face cache

{.sd-tab-content .docutils}
If you already have models downloaded on your host system, you can mount your existing cache.

1.  Set your Hugging Face cache location.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/your/hf_cache/location
    
    :

2.  Download the model (if not already cached).

    :
{.highlight-shell .notranslate}
    
highlight
        huggingface-cli download black-forest-labs/FLUX.1-dev 
    
    :

3.  Launch the container with mounted cache.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            -e HF_HOME=/app/huggingface_models \
            -v $HF_HOME:/app/huggingface_models \
            rocm/pytorch-xdit:v25.12
    
    :

Option 2: Download inside container

{.sd-tab-content .docutils}
If you prefer to keep the container self-contained or don't have an existing cache.

1.  Launch the container

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            rocm/pytorch-xdit:v25.12
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        huggingface-cli download black-forest-labs/FLUX.1-dev 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .stable-diffusion-3-5-large-tag .docutils .container}
::
{.sd-tab-set .docutils}
Option 1: Use existing Hugging Face cache

{.sd-tab-content .docutils}
If you already have models downloaded on your host system, you can mount your existing cache.

1.  Set your Hugging Face cache location.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/your/hf_cache/location
    
    :

2.  Download the model (if not already cached).

    :
{.highlight-shell .notranslate}
    
highlight
        huggingface-cli download stabilityai/stable-diffusion-3.5-large 
    
    :

3.  Launch the container with mounted cache.

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            -e HF_HOME=/app/huggingface_models \
            -v $HF_HOME:/app/huggingface_models \
            rocm/pytorch-xdit:v25.12
    
    :

Option 2: Download inside container

{.sd-tab-content .docutils}
If you prefer to keep the container self-contained or don't have an existing cache.

1.  Launch the container

    :
{.highlight-shell .notranslate}
    
highlight
        docker run \
            -it --rm \
            --cap-add=SYS_PTRACE \
            --security-opt seccomp=unconfined \
            --user root \
            --device=/dev/kfd \
            --device=/dev/dri \
            --group-add video \
            --ipc=host \
            --network host \
            --privileged \
            --shm-size 128G \
            --name pytorch-xdit \
            -e HSA_NO_SCRATCH_RECLAIM=1 \
            -e OMP_NUM_THREADS=16 \
            -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
            rocm/pytorch-xdit:v25.12
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        huggingface-cli download stabilityai/stable-diffusion-3.5-large 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

::::::::::::::::::::
::::::::::::::::::::::::::

::::::::::::::::::::::::::::::
{#run-inference .section}
## Run inference[\#](#run-inference "Link to this heading"){.headerlink}

:::::
{.model-doc .hunyuan-tag .docutils .container}
::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

{.sd-tab-content .docutils}
1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  On the host machine, use this command to run the performance benchmark test on the [Hunyuan Video](https://huggingface.co/tencent/HunyuanVideo){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_hunyuanvideo \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_hunyuanvideo`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_hunyuanvideo_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_hunyuanvideo_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Hunyuan Video, use the following command:

:
{.highlight-shell .notranslate}

highlight
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

:

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see stdout.
::
::::
:::::

:::::
{.model-doc .wan-21-tag .docutils .container}
::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

{.sd-tab-content .docutils}
1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  On the host machine, use this command to run the performance benchmark test on the [Wan2.1](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P-Diffusers){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_wan_2_1 \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_wan_2_1`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_wan_2_1_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_wan_2_1_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Wan2.1, use the following command:

:
{.highlight-shell .notranslate}

highlight
    cd Wan
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

:

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/outputs/rank0\_\*.json
::
::::
:::::

:::::
{.model-doc .wan-22-tag .docutils .container}
::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

{.sd-tab-content .docutils}
1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  On the host machine, use this command to run the performance benchmark test on the [Wan2.2](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B-Diffusers){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_wan_2_2 \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_wan_2_2`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_wan_2_2_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_wan_2_2_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Wan2.2, use the following command:

:
{.highlight-shell .notranslate}

highlight
    cd Wan
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

:

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/outputs/rank0\_\*.json
::
::::
:::::

:::::
{.model-doc .flux-1-tag .docutils .container}
::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

{.sd-tab-content .docutils}
1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  On the host machine, use this command to run the performance benchmark test on the [FLUX.1](https://huggingface.co/black-forest-labs/FLUX.1-dev){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_flux \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_flux`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_flux_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_flux_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for FLUX.1, use the following command:

:
{.highlight-shell .notranslate}

highlight
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
       --num_repetitions 50

:

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see results/timing.json

You may also use [`run_usp.py`{.docutils .literal .notranslate}]{.pre} which implements USP without modifying the default diffusers pipeline.
::
::::
:::::

:::::
{.model-doc .stable-diffusion-3-5-large-tag .docutils .container}
::::
{.sd-tab-set .docutils}
MAD-integrated benchmarking

{.sd-tab-content .docutils}
1.  Clone the ROCm Model Automation and Dashboarding ([ROCm/MAD](https://github.com/ROCm/MAD){.github .reference .external}) repository to a local directory and install the required packages on the host machine.

    :
{.highlight-shell .notranslate}
    
highlight
        git clone https://github.com/ROCm/MAD
        cd MAD
        pip install -r requirements.txt
    
    :

2.  On the host machine, use this command to run the performance benchmark test on the [stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_sd_3_5 \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_sd_3_5`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_sd_3_5_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_sd_3_5_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for stable-diffusion-3.5-large, use the following command:

:
{.highlight-shell .notranslate}

highlight
    cd StableDiffusion3.5
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

:

The generated video will be stored under the results directory. For the actual benchmark step runtimes, see benchmark_results.csv
::
::::
:::::
::::::::::::::::::::::::::::::

{#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[xDiT diffusion inference performance testing version history]{.doc}](xdit-history.html){.reference .internal} to find documentation for previous releases of xDiT diffusion inference performance testing.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
