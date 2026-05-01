---
title: "xDiT diffusion inference"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/xdit-diffusion-inference.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:57:23.218806+00:00
content_hash: "17aba9f1e8f417ea"
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 37 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

The [rocm/pytorch-xdit](https://hub.docker.com/layers/rocm/pytorch-xdit/v26.4/images/sha256-b4296a638eb8dc7ebcafc808e180b78a3c44177580c21986082ec9539496067c){.reference .external} Docker image offers a prebuilt, optimized environment based on [xDiT](https://github.com/xdit-project/xDiT){.reference .external} for benchmarking diffusion model video and image generation on gfx942 and gfx950 series (AMD Instinct™ MI300X, MI325X, MI350X, and MI355X) GPUs. The image runs [ROCm 7.12.0 (preview)](https://rocm.docs.amd.com/en/7.12.0-preview/about/release-notes.html){.reference .external} based on [TheRock](https://github.com/ROCm/TheRock){.reference .external} and includes the following components:

[Software components - xdit:v26.4]{.sd-summary-text}[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jaGV2cm9uLXJpZ2h0IiBoZWlnaHQ9IjEuNWVtIiB2ZXJzaW9uPSIxLjEiIHZpZXdib3g9IjAgMCAyNCAyNCIgd2lkdGg9IjEuNWVtIj48cGF0aCBkPSJNOC43MiAxOC43OGEuNzUuNzUgMCAwIDEgMC0xLjA2TDE0LjQ0IDEyIDguNzIgNi4yOGEuNzUxLjc1MSAwIDAgMSAuMDE4LTEuMDQyLjc1MS43NTEgMCAwIDEgMS4wNDItLjAxOGw2LjI1IDYuMjVhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtNi4yNSA2LjI1YS43NS43NSAwIDAgMS0xLjA2IDBaIiAvPjwvc3ZnPg==){.sd-octicon .sd-octicon-chevron-right}]{.sd-summary-state-marker .sd-summary-chevron-right}

:
{.sd-summary-content .sd-card-body .docutils}

pst-scrollable-table-container
  Software component                                                                       Version
  ---------------------------------------------------------------------------------------- ---------
  [TheRock](https://github.com/ROCm/TheRock){.reference .external}                         9b611c6
  [rocm-libraries](https://github.com/ROCm/rocm-libraries){.reference .external}           7567d83
  [rocm-systems](https://github.com/ROCm/rocm-systems){.reference .external}               93bc019
  [torch](https://github.com/ROCm/pytorch){.reference .external}                           ff65f5b
  [torchaudio](https://github.com/pytorch/audio){.reference .external}                     e3c6ee2
  [torchvision](https://github.com/pytorch/vision){.reference .external}                   b919bd0
  [triton](https://github.com/ROCm/triton){.reference .external}                           a272dfa
  [accelerate](https://github.com/huggingface/accelerate){.reference .external}            46ba481
  [aiter](https://github.com/ROCm/aiter){.reference .external}                             a169e14
  [diffusers](https://github.com/huggingface/diffusers){.reference .external}              a80b192
  [distvae](https://github.com/xdit-project/DistVAE){.reference .external}                 bf7531e
  [xfuser](https://github.com/xdit-project/xDiT){.reference .external}                     45c44e7
  [yunchang](https://github.com/feifeibear/long-context-attention){.reference .external}   631bdfd

:

Follow this guide to pull the required image, spin up a container, download the model, and run a benchmark. For preview and development releases, see [amdsiloai/pytorch-xdit](https://hub.docker.com/r/amdsiloai/pytorch-xdit){.reference .external}.

{#what-s-new .section}
## What's new[\#](#what-s-new "Link to this heading"){.headerlink}

- Qwen-Image-2512 support

- Z-Image support

- Parallel VAE decode support for Wan models

- Batch inference and data parallel support

:::::::::::::::::::::::::::::::::::::::::::::::::::::
{#supported-models .section}
[]{#xdit-video-diffusion-supported-models}

## Supported models[\#](#supported-models "Link to this heading"){.headerlink}

The following models are supported for inference performance benchmarking. Some instructions, commands, and recommendations in this documentation might vary by model -- select one to get started.

::::::::::::::::::::::::::
{#vllm-benchmark-ud-params-picker .container-fluid}
:::::::::
{.row .gx-0}

{.col-2 .me-1 .px-2 .model-param-head}
Model

:::::::
{.row .col-10 .pe-0}

{.col-6 .px-2 .model-param param-k="model-group" param-v="hunyuan" tabindex="0"}
Hunyuan Video

{.col-6 .px-2 .model-param param-k="model-group" param-v="wan" tabindex="0"}
Wan-AI

{.col-6 .px-2 .model-param param-k="model-group" param-v="flux" tabindex="0"}
FLUX

{.col-6 .px-2 .model-param param-k="model-group" param-v="stablediffusion" tabindex="0"}
StableDiffusion

{.col-6 .px-2 .model-param param-k="model-group" param-v="z_image" tabindex="0"}
Z-Image

{.col-6 .px-2 .model-param param-k="model-group" param-v="ltx" tabindex="0"}
LTX

{.col-6 .px-2 .model-param param-k="model-group" param-v="qwen_image" tabindex="0"}
Qwen-Image

:::::::
:::::::::

:::::::::::::::
{.row .gx-0 .pt-1}

{.col-2 .me-1 .px-2 .model-param-head}
Variant

:::::::::::::
{.row .col-10 .pe-0}

{.col-6 .px-2 .model-param param-group="hunyuan" param-k="model" param-v="hunyuan_tag" tabindex="0"}
Hunyuan Video

{.col-6 .px-2 .model-param param-group="hunyuan" param-k="model" param-v="hunyuan_1_5_tag" tabindex="0"}
Hunyuan Video 1.5

{.col-6 .px-2 .model-param param-group="wan" param-k="model" param-v="wan_21_tag" tabindex="0"}
Wan2.1

{.col-6 .px-2 .model-param param-group="wan" param-k="model" param-v="wan_22_tag" tabindex="0"}
Wan2.2

{.col-6 .px-2 .model-param param-group="flux" param-k="model" param-v="flux_1_tag" tabindex="0"}
FLUX.1

{.col-6 .px-2 .model-param param-group="flux" param-k="model" param-v="flux_1_kontext_tag" tabindex="0"}
FLUX.1 Kontext

{.col-6 .px-2 .model-param param-group="flux" param-k="model" param-v="flux_2_tag" tabindex="0"}
FLUX.2

{.col-6 .px-2 .model-param param-group="flux" param-k="model" param-v="flux_2_klein_tag" tabindex="0"}
FLUX.2 Klein

{.col-6 .px-2 .model-param param-group="stablediffusion" param-k="model" param-v="stable_diffusion_3_5_large_tag" tabindex="0"}
stable-diffusion-3.5-large

{.col-6 .px-2 .model-param param-group="z_image" param-k="model" param-v="z_image_tag" tabindex="0"}
Z-Image

{.col-6 .px-2 .model-param param-group="ltx" param-k="model" param-v="ltx2_tag" tabindex="0"}
LTX-2

{.col-6 .px-2 .model-param param-group="qwen_image" param-k="model" param-v="qwen_image_tag" tabindex="0"}
Qwen-Image

{.col-6 .px-2 .model-param param-group="qwen_image" param-k="model" param-v="qwen_image_edit_tag" tabindex="0"}
Qwen-Image-Edit

:::::::::::::
:::::::::::::::
::::::::::::::::::::::::::

:
{.model-doc .hunyuan-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Hunyuan Video model card on Hugging Face](https://huggingface.co/tencent/HunyuanVideo){.reference .external} or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .hunyuan-1-5-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Hunyuan Video 1.5 model card on Hugging Face](https://huggingface.co/hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v){.reference .external} or visit the [GitHub page](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

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
{.model-doc .flux-1-kontext-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [FLUX.1 Kontext model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev){.reference .external} or visit the [GitHub page](https://github.com/black-forest-labs/flux){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .flux-2-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [FLUX.2 model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.2-dev){.reference .external} or visit the [GitHub page](https://github.com/black-forest-labs/flux2){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .flux-2-klein-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [FLUX.2 Klein model card on Hugging Face](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B){.reference .external} or visit the [GitHub page](https://github.com/black-forest-labs/flux2){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .stable-diffusion-3-5-large-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [stable-diffusion-3.5-large model card on Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-3.5-large){.reference .external} or visit the [GitHub page](https://github.com/Stability-AI/sd3.5){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .z-image-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Z-Image model card on Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image){.reference .external} or visit the [GitHub page](https://github.com/Tongyi-MAI/Z-Image){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .ltx2-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [LTX-2 model card on Hugging Face](https://huggingface.co/Lightricks/LTX-2){.reference .external} or visit the [GitHub page](https://github.com/Lightricks/LTX-2){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .qwen-image-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Qwen-Image model card on Hugging Face](https://huggingface.co/Qwen/Qwen-Image-2512){.reference .external} or visit the [GitHub page](https://github.com/QwenLM/Qwen-Image){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:

:
{.model-doc .qwen-image-edit-tag .docutils .container}

{.admonition .note}
Note

To learn more about your specific model see the [Qwen-Image-Edit model card on Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit){.reference .external} or visit the [GitHub page](https://github.com/QwenLM/Qwen-Image){.reference .external}. Note that some models require access authorization before use via an external license agreement through a third party.

:
:::::::::::::::::::::::::::::::::::::::::::::::::::::

{#system-validation .section}
## System validation[\#](#system-validation "Link to this heading"){.headerlink}

Before running AI workloads, it's important to validate that your AMD hardware is configured correctly and performing optimally.

If you have already validated your system settings, including aspects like NUMA auto-balancing, you can skip this step. Otherwise, complete the procedures in the [[System validation and optimization]{.std .std-ref}](../system-setup/prerequisite-system-validation.html#rocm-for-ai-system-optimization){.reference .internal} guide to properly configure your system settings before starting.

To test for optimal performance, consult the recommended [[System health benchmarks]{.std .std-ref}](../system-setup/system-health-check.html#rocm-for-ai-system-health-bench){.reference .internal}. This suite of tests will help you verify and fine-tune your system's configuration.

::
{#pull-the-docker-image .section}
## Pull the Docker image[\#](#pull-the-docker-image "Link to this heading"){.headerlink}

For this tutorial, it's recommended to use the latest [`rocm/pytorch-xdit:v26.4`{.docutils .literal .notranslate}]{.pre} Docker image. Pull the image using the following command:

:
{.highlight-shell .notranslate}

highlight
    docker pull rocm/pytorch-xdit:v26.4

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
{#validate-and-benchmark .section}
## Validate and benchmark[\#](#validate-and-benchmark "Link to this heading"){.headerlink}

Once the image has been downloaded you can follow these steps to run benchmarks and generate outputs.

{.model-doc .hunyuan-tag .docutils .container}
The following commands are written for Hunyuan Video. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .hunyuan-1-5-tag .docutils .container}
The following commands are written for Hunyuan Video 1.5. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .wan-21-tag .docutils .container}
The following commands are written for Wan2.1. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .wan-22-tag .docutils .container}
The following commands are written for Wan2.2. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .flux-1-tag .docutils .container}
The following commands are written for FLUX.1. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .flux-1-kontext-tag .docutils .container}
The following commands are written for FLUX.1 Kontext. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .flux-2-tag .docutils .container}
The following commands are written for FLUX.2. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .flux-2-klein-tag .docutils .container}
The following commands are written for FLUX.2 Klein. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .stable-diffusion-3-5-large-tag .docutils .container}
The following commands are written for stable-diffusion-3.5-large. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .z-image-tag .docutils .container}
The following commands are written for Z-Image. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .ltx2-tag .docutils .container}
The following commands are written for LTX-2. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .qwen-image-tag .docutils .container}
The following commands are written for Qwen-Image. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

{.model-doc .qwen-image-edit-tag .docutils .container}
The following commands are written for Qwen-Image-Edit. See [[Supported models]{.std .std-ref}](#xdit-video-diffusion-supported-models){.reference .internal} to switch to another available model.

::::::::::::::::::::::::::::::::::::::::::::::::::::
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
        hf download tencent/HunyuanVideo  --revision refs/pr/18 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download tencent/HunyuanVideo  --revision refs/pr/18 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .hunyuan-1-5-tag .docutils .container}
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
        hf download hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v 
    
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
        hf download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download Wan-AI/Wan2.1-I2V-14B-720P-Diffusers 
    
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
        hf download Wan-AI/Wan2.2-I2V-A14B-Diffusers 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download Wan-AI/Wan2.2-I2V-A14B-Diffusers 
    
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
        hf download black-forest-labs/FLUX.1-dev 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download black-forest-labs/FLUX.1-dev 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .flux-1-kontext-tag .docutils .container}
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
        hf download black-forest-labs/FLUX.1-Kontext-dev 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download black-forest-labs/FLUX.1-Kontext-dev 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .flux-2-tag .docutils .container}
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
        hf download black-forest-labs/FLUX.2-dev 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download black-forest-labs/FLUX.2-dev 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .flux-2-klein-tag .docutils .container}
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
        hf download black-forest-labs/FLUX.2-klein-9B 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download black-forest-labs/FLUX.2-klein-9B 
    
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
        hf download stabilityai/stable-diffusion-3.5-large 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download stabilityai/stable-diffusion-3.5-large 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .z-image-tag .docutils .container}
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
        hf download Tongyi-MAI/Z-Image 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download Tongyi-MAI/Z-Image 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .ltx2-tag .docutils .container}
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
        hf download Lightricks/LTX-2 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download Lightricks/LTX-2 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .qwen-image-tag .docutils .container}
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
        hf download Qwen/Qwen-Image-2512 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download Qwen/Qwen-Image-2512 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

{.model-doc .qwen-image-edit-tag .docutils .container}
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
        hf download Qwen/Qwen-Image-Edit 
    
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
            rocm/pytorch-xdit:v26.4
    
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
            rocm/pytorch-xdit:v26.4
    
    :

2.  Inside the container, set the Hugging Face cache location and download the model.

    :
{.highlight-shell .notranslate}
    
highlight
        export HF_HOME=/app/huggingface_models
        hf download Qwen/Qwen-Image-Edit 
    
    :

    
{.admonition .warning}
    Warning

    Models will be downloaded to the container's filesystem and will be lost when the container is removed unless you persist the data with a volume.
    

::

::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
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
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .hunyuan-1-5-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [Hunyuan Video 1.5](https://huggingface.co/hunyuanvideo-community/HunyuanVideo-1.5-Diffusers-720p_t2v){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_hunyuanvideo_1_5 \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_hunyuanvideo_1_5`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_hunyuanvideo_1_5_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_hunyuanvideo_1_5_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Hunyuan Video 1.5, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
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
    mkdir results
       xdit \
       --model Wan-AI/Wan2.1-I2V-14B-720P-Diffusers \
       --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
       --height 720 \
       --width 1280 \
       --input_images /app/data/wan_input.jpg \
       --num_frames 81 \
       --ulysses_degree 8 \
       --use_parallel_vae \
       --seed 42 \
       --num_iterations 1 \
       --num_inference_steps 40 \
       --use_torch_compile \
       --attention_backend aiter \
       --output_directory results

:

The generated content and timing information will be stored under the results directory.
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
    mkdir results
       xdit \
       --model Wan-AI/Wan2.2-I2V-A14B-Diffusers \
       --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside." \
       --height 720 \
       --width 1280 \
       --input_images /app/data/wan_input.jpg \
       --num_frames 81 \
       --ulysses_degree 8 \
       --use_parallel_vae \
       --seed 42 \
       --num_iterations 1 \
       --num_inference_steps 40 \
       --use_torch_compile \
       --attention_backend aiter \
       --output_directory results

:

The generated content and timing information will be stored under the results directory.
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
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .flux-1-kontext-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [FLUX.1 Kontext](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_flux_kontext \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_flux_kontext`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_flux_kontext_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_flux_kontext_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for FLUX.1 Kontext, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .flux-2-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [FLUX.2](https://huggingface.co/black-forest-labs/FLUX.2-dev){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_flux_2 \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_flux_2`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_flux_2_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_flux_2_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for FLUX.2, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .flux-2-klein-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [FLUX.2 Klein](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_flux_2_klein \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_flux_2_klein`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_flux_2_klein_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_flux_2_klein_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for FLUX.2 Klein, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
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
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .z-image-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_z_image \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_z_image`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_z_image_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_z_image_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Z-Image, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
       xdit \
       --model Tongyi-MAI/Z-Image \
       --seed 42 \
       --prompt "A crowded beach" \
       --height 1088 \
       --width 1920 \
       --num_inference_steps 50 \
       --ulysses_degree 2 \
       --ring_degree 2 \
       --use_cfg_parallel \
       --use_torch_compile \
       --guidance_scale 4.0 \
       --num_iterations 25 \
       --attention_backend aiter \
       --output_directory results

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .ltx2-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [LTX-2](https://huggingface.co/Lightricks/LTX-2){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_ltx2 \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_ltx2`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_ltx2_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_ltx2_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for LTX-2, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .qwen-image-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen-Image](https://huggingface.co/Qwen/Qwen-Image-2512){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_qwen_image \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_qwen_image`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_qwen_image_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_qwen_image_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Qwen-Image, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
       xdit \
       --model Qwen/Qwen-Image-2512 \
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::

:::::
{.model-doc .qwen-image-edit-tag .docutils .container}
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

2.  On the host machine, use this command to run the performance benchmark test on the [Qwen-Image-Edit](https://huggingface.co/Qwen/Qwen-Image-Edit){.reference .external} model using one node.

    :
{.highlight-shell .notranslate}
    
highlight
        export MAD_SECRETS_HFTOKEN="your personal Hugging Face token to access gated models"
        madengine run \
            --tags pyt_xdit_qwen_image_edit \
            --keep-model-dir \
            --live-output
    
    :

MAD launches a Docker container with the name [`container_ci-pyt_xdit_qwen_image_edit`{.docutils .literal .notranslate}]{.pre}. The throughput and serving reports of the model are collected in the following paths: [`pyt_xdit_qwen_image_edit_throughput.csv`{.docutils .literal .notranslate}]{.pre} and [`pyt_xdit_qwen_image_edit_serving.csv`{.docutils .literal .notranslate}]{.pre}.

Standalone benchmarking

::
{.sd-tab-content .docutils}
To run the benchmarks for Qwen-Image-Edit, use the following command:

:
{.highlight-shell .notranslate}

highlight
    mkdir results
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

:

The generated content and timing information will be stored under the results directory.
::
::::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{#previous-versions .section}
## Previous versions[\#](#previous-versions "Link to this heading"){.headerlink}

See [[xDiT diffusion inference performance testing version history]{.doc}](benchmark-docker/previous-versions/xdit-history.html){.reference .internal} to find documentation for previous releases of xDiT diffusion inference performance testing.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
