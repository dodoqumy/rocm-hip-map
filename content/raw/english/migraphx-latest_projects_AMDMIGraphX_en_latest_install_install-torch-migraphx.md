---
title: "Torch-MIGraphX installation"
source_url: "https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/install/install-torch-migraphx.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:24:58.019715+00:00
content_hash: "6825d32730e19842"
---

# Torch-MIGraphX installation[#](#torch-migraphx-installation)

2025-11-11

1 min read time

MIGraphX can be integrated with PyTorch workflows by using the Torch-MIGraphX library.
It includes the `torch.compile`

API, so you can compile PyTorch models using MIGraphX.

Prerequisites:

ROCm must be installed before installing MIGraphX. See

[ROCm installation for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/)for instructions.Installing MIGraphX using a package installer is sufficient if you want to use the MIGraphX API. See

[MIGraphX installation](./install-migraphx.html)for instructions.Pytorch must be installed. See

[PyTorch installation](https://rocm.docs.amd.com/projects/install-on-linux/en/develop/how-to/3rd-party/pytorch-install.html#using-a-wheels-package)for instructions.

## Install Torch-MIGraphX[#](#install-torch-migraphx)

Use the following command to install `torch_migraphx`

using `pip`

:

```
install torch_migraphx
```

## Build Torch-MIGraphX from source[#](#build-torch-migraphx-from-source)

Use the following command to build `torch_migraphx`

from source:

```
clone https://github.com/ROCm/torch_migraphx.git
cd torch_migraphx
pip install . --no-build-isolation
```

Refer to the [ROCm/torch_migraphx](https://github.com/ROCm/torch_migraphx/) repository for more information on local builds and Docker environments.
