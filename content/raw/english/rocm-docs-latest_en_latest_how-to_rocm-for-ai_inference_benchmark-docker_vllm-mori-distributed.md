---
title: "vLLM distributed inference with MoRI"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/vllm-mori-distributed.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../../../../index.html){.nav-link aria-label="Home"}
- [Use ROCm for AI](../../index.html){.nav-link}
- [Use ROCm for AI inference](../index.html){.nav-link}
- vLLM\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# vLLM distributed inference with MoRI

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Prerequisites](#prerequisites){.reference .internal .nav-link}
- [System configuration](#system-configuration){.reference .internal .nav-link}
  - [Verify baseline software](#verify-baseline-software){.reference .internal .nav-link}
  - [Verify best known configuration (BKC)](#verify-best-known-configuration-bkc){.reference .internal .nav-link}
  - [Run basic system health checks](#run-basic-system-health-checks){.reference .internal .nav-link}
  - [Configure your backend network (netplan)](#configure-your-backend-network-netplan){.reference .internal .nav-link}
  - [Configure your network file system (NFS)](#configure-your-network-file-system-nfs){.reference .internal .nav-link}
  - [Configure static hostname resolution for backend initialization (optional)](#configure-static-hostname-resolution-for-backend-initialization-optional){.reference .internal .nav-link}
- [Software installation](#software-installation){.reference .internal .nav-link}
  - [Install CX7 driver and firmware](#install-cx7-driver-and-firmware){.reference .internal .nav-link}
  - [Install ROCm](#install-rocm){.reference .internal .nav-link}
  - [Install AMD GPU Driver (amdgpu)](#install-amd-gpu-driver-amdgpu){.reference .internal .nav-link}
- [Network verification and testing](#network-verification-and-testing){.reference .internal .nav-link}
  - [Verify network connectivity](#verify-network-connectivity){.reference .internal .nav-link}
  - [Validate your RDMA setup](#validate-your-rdma-setup){.reference .internal .nav-link}
  - [Run RDMA bandwidth benchmarks](#run-rdma-bandwidth-benchmarks){.reference .internal .nav-link}
    - [Install RDMA Performance Tools](#install-rdma-performance-tools){.reference .internal .nav-link}
    - [Run a bandwidth test (GPU memory)](#run-a-bandwidth-test-gpu-memory){.reference .internal .nav-link}
- [vLLM serving and MoRI unit tests](#vllm-serving-and-mori-unit-tests){.reference .internal .nav-link}
  - [Install Docker Engine](#install-docker-engine){.reference .internal .nav-link}
  - [Download the DeepSeek PTPC model](#download-the-deepseek-ptpc-model){.reference .internal .nav-link}
  - [Launch the serving container](#launch-the-serving-container){.reference .internal .nav-link}
  - [Run MoRI inter-node unit tests](#run-mori-inter-node-unit-tests){.reference .internal .nav-link}
  - [Deploy and serve the model](#deploy-and-serve-the-model){.reference .internal .nav-link}
    - [Create serving scripts](#create-serving-scripts){.reference .internal .nav-link}
    - [Run the serving scripts](#run-the-serving-scripts){.reference .internal .nav-link}
- [Reproducing performance](#reproducing-performance){.reference .internal .nav-link}
  - [Configuration for EP16 (16 GPUs)](#configuration-for-ep16-16-gpus){.reference .internal .nav-link}
    - [Benchmark target](#benchmark-target){.reference .internal .nav-link}
  - [Performance reproduction commands](#performance-reproduction-commands){.reference .internal .nav-link}
    - [Decode benchmark](#decode-benchmark){.reference .internal .nav-link}
- [Troubleshooting](#troubleshooting){.reference .internal .nav-link}
  - [Bandwidth test fails with error](#bandwidth-test-fails-with-error){.reference .internal .nav-link}
  - [vLLM EP 16 with MoRI backend fails to launch](#vllm-ep-16-with-mori-backend-fails-to-launch){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#vllm-distributed-inference-with-mori .section .tex2jax_ignore .mathjax_ignore}
# vLLM distributed inference with MoRI[\#](#vllm-distributed-inference-with-mori "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 17 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

This document provides a comprehensive guide for setting up a high-performance vLLM serving environment on an AMD Instinct MI300X or MI325X GPU cluster using the [MoRI (Modular RDMA Interface)](https://github.com/rocm/mori){.reference .external} communication backend. It also includes detailed instructions on how to reproduce the benchmark results published in the AMD ROCm blog [Practical, Fault-Robust Distributed Inference for DeepSeek on AMD MI300X](https://rocm.blogs.amd.com/software-tools-optimization/wide-ep-deepseek/README.html){.reference .external}.

::: {#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

The following hardware configuration is required to implement this setup:

- **Nodes**: A minimum of two GPU nodes (virtual machines or physical machines) for wide expert parallelism (EP) evaluation.

- **GPUs**: 8x AMD Instinct MI300X/MI325X GPU cards per node.

- **Networking**: 8x NVIDIA Mellanox ConnectX-7 (CX7) NICs per node, providing a dedicated 1:1 mapping between GPUs and network interfaces for optimal inter-node communication.
:::

:::::::::::::::::::::: {#system-configuration .section}
## System configuration[\#](#system-configuration "Link to this heading"){.headerlink}

This section outlines infrastructure steps required to prepare your cluster for high-performance AI workloads. It covers validating your system's software baselines and firmware versions, configuring high-bandwidth backend networking for inter-node communication, and establish shared storage to ensure a synchronized distributed computing environment.

:::: {#verify-baseline-software .section}
### Verify baseline software[\#](#verify-baseline-software "Link to this heading"){.headerlink}

This setup has been validated using the **AI/ML Ready Image (ROCm 7-based)** on Digital Ocean AMD GPU Droplets. The following table outlines the software stack versions and appropriate shell commands for verification:

::: pst-scrollable-table-container
  Component                               Version              Verification command
  --------------------------------------- -------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **OS**                                  Ubuntu 24.04.3 LTS   [`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/etc/os-release`{.docutils .literal .notranslate}]{.pre}
  **Kernel**                              6.8.0-87-generic     [`uname`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-r`{.docutils .literal .notranslate}]{.pre}
  **ROCm**                                7.0.2                [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`version`{.docutils .literal .notranslate}]{.pre}
  **PLDM bundle (firmware) for MI300X**   01.25.03.12          [Verify BKC](#verify-best-known-configuration-bkc){.reference .internal}
  **PLDM bundle (firmware) for MI325X**   01.25.03.03          [Verify BKC](#verify-best-known-configuration-bkc){.reference .internal}
  **CX7 Firmware**                        28.46.3048           [`dkms`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`status`{.docutils .literal .notranslate}]{.pre}
  **CX7 Driver**                          24.10-3.2.5          [`dkms`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`status`{.docutils .literal .notranslate}]{.pre}
  **DOCA**                                2.9.3                [`dpkg`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-l`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`|`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`grep`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`doca`{.docutils .literal .notranslate}]{.pre}
:::
::::

::: {#verify-best-known-configuration-bkc .section}
### Verify best known configuration (BKC)[\#](#verify-best-known-configuration-bkc "Link to this heading"){.headerlink}

The BKC defines a validated configuration of GPU firmware, baseboard firmware, ROCm user space components, the AMD GPU Driver, and virtualization tooling. These components are tested together to attain best performance and compatibility.

While AMD publishes the AMD GPU driver and ROCm user space components, your server OEM or infrastructure provider distributes the firmware packages. AMD supplies those firmware images (PLDM bundles), which the OEM integrates and distributes.

To verify the active BKC and IFWI (Integrated Firmware Image) versions via the Redfish API:

1.  Prepare credentials: Identify your BMC IP, username, and password.

2.  Run Redfish queries: Use the following commands to check the active firmware inventory.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        # Define BMC connection variables
        BMC_IP="<BMC_IP>"
        AUTH="<username>:<password>"

        # Query active BKC bundle version
        curl -X GET "https://${BMC_IP}/redfish/v1/UpdateService/FirmwareInventory/bundle_active" \
             -u "${AUTH}" -k | json_pp

        # Query active IFWI (Integrated Firmware Image)
        curl -X GET "https://${BMC_IP}/redfish/v1/UpdateService/FirmwareInventory/firmware_active" \
             -u "${AUTH}" -k | json_pp
    :::
    ::::
:::

::: {#run-basic-system-health-checks .section}
### Run basic system health checks[\#](#run-basic-system-health-checks "Link to this heading"){.headerlink}

Before proceeding with software deployment, verify that all cluster nodes comply with the [MI300X Basic Health Checks](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi300x.html#basic-health-checks){.reference .external} or [MI325X Basic Health Checks](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi325x.html#basic-health-checks){.reference .external}. Key requirements include specific kernel boot arguments, minimum system memory thresholds, PCIe Gen5 link stability, and so on.
:::

:::::::::: {#configure-your-backend-network-netplan .section}
### Configure your backend network (netplan)[\#](#configure-your-backend-network-netplan "Link to this heading"){.headerlink}

Configure the backend NICs for high-bandwidth inter-node communication. Suppose the GPU's eight network interface controllers (NICs) are eth2 to eth9. Each NIC must have its own subnet that is disjoint from the others. For example, [`eth2`{.docutils .literal .notranslate}]{.pre} could use [`192.168.50.0/24`{.docutils .literal .notranslate}]{.pre}, [`eth3`{.docutils .literal .notranslate}]{.pre} could use [`192.168.51.0/24`{.docutils .literal .notranslate}]{.pre}, and so on. Each node needs a unique IP address on each subnet. You should use the same final octet in each subnet for a given node. For example, one node would have the addresses [`192.168.50.2`{.docutils .literal .notranslate}]{.pre}, [`192.168.51.2`{.docutils .literal .notranslate}]{.pre}, and so on. Another node might have [`192.168.50.3`{.docutils .literal .notranslate}]{.pre}, [`192.168.51.3`{.docutils .literal .notranslate}]{.pre}, and so on. Ensure MTU is set to [`4200`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

Ensure you identify the correct interface names for your system using ip link before applying this configuration.
:::

For example, your [`/etc/netplan/50-backend.yaml`{.docutils .literal .notranslate}]{.pre} might include something like the following:

:::: {.highlight-yaml .notranslate}
::: highlight
    eth2:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.50.2/24
      mtu: 4200
    eth3:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.51.2/24
      mtu: 4200
    eth4:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.52.2/24
      mtu: 4200
    eth5:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.53.2/24
      mtu: 4200
    eth6:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.54.2/24
      mtu: 4200
    eth7:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.55.2/24
      mtu: 4200
    eth8:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.56.2/24
      mtu: 4200
    eth9:
      dhcp4: false
      dhcp6: false
      link-local: []
      addresses:
        - 192.168.57.2/24
      mtu: 4200
:::
::::

To apply the configuration, use the following command.

:::: {.highlight-bash .notranslate}
::: highlight
    sudo netplan apply
:::
::::

To verify your configuration, use the following command.

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt install -y net-tools && ip -br a
:::
::::
::::::::::

:::::: {#configure-your-network-file-system-nfs .section}
### Configure your network file system (NFS)[\#](#configure-your-network-file-system-nfs "Link to this heading"){.headerlink}

Setting up a shared NFS volume facilitates centralized storage for models, recipes, and logs across the cluster. Use the following commands to install the necessary client tools and mount the remote directory.

::: {.admonition .important}
Important

Replace [`nfs_server_ip:/shared/folder`{.docutils .literal .notranslate}]{.pre} and [`/mount/point`{.docutils .literal .notranslate}]{.pre} with your specific server details and desired local mount path.
:::

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt update && sudo apt install -y nfs-common
    sudo mkdir -p /mount/point
    sudo mount -t nfs nfs_server_ip:/shared/folder /mount/point
    echo "nfs_server_ip:/shared/folder /mount/point nfs _netdev,nofail,x-systemd.automount,x-systemd.idle-timeout=600,vers=4.2 0 0" | sudo tee -a /etc/fstab
:::
::::
::::::

::::: {#configure-static-hostname-resolution-for-backend-initialization-optional .section}
### Configure static hostname resolution for backend initialization (optional)[\#](#configure-static-hostname-resolution-for-backend-initialization-optional "Link to this heading"){.headerlink}

If the high-speed RDMA/IB interfaces are used for the initial distributed coordination (such as [`MASTER_ADDR`{.docutils .literal .notranslate}]{.pre}), you must configure static hostname resolution. This ensures that cluster host names resolve to the backend network IPs rather than the management or local loopback addresses.

Follow these steps to configure static hostname resolution:

1.  Edit [`/etc/hosts`{.docutils .literal .notranslate}]{.pre} on all nodes: for example, using [`sudo`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`vim`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/etc/hosts`{.docutils .literal .notranslate}]{.pre}.

2.  Add the backend IP and hostname mappings.

3.  Comment out any default local mappings (such as [`127.0.1.1`{.docutils .literal .notranslate}]{.pre}) for the current hostname to avoid resolution conflicts.

For example, your [`/etc/hosts`{.docutils .literal .notranslate}]{.pre} entries might look like:

:::: {.highlight-text .notranslate}
::: highlight
    # Map host names to backend network IPs
    192.168.50.2 mori_test_01
    192.168.50.3 mori_test_02

    # Comment out the default entry to ensure resolution via the backend IP
    # 127.0.1.1 mori_test_01 mori_test_01
:::
::::
:::::
::::::::::::::::::::::

:::::::::: {#software-installation .section}
## Software installation[\#](#software-installation "Link to this heading"){.headerlink}

Next, install the essential software stack required to operate the AMD Instinct GPUs and high-speed networking components. Follow these steps to deploy the NVIDIA DOCA drivers for Mellanox ConnectX-7 NICs, the ROCm software stack, and the necessary kernel modules to enable hardware acceleration.

::: {#install-cx7-driver-and-firmware .section}
### Install CX7 driver and firmware[\#](#install-cx7-driver-and-firmware "Link to this heading"){.headerlink}

1.  Download and install the [`DOCA`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`2.9.3`{.docutils .literal .notranslate}]{.pre} driver following the instructions in [NVIDIA DOCA 2.9.3 Downloads](https://developer.nvidia.com/doca-2-9-3-download-archive?deployment_platform=Host-Server&amp;deployment_package=DOCA-Host&amp;target_os=Linux&amp;Architecture=x86_64&amp;Profile=doca-all&amp;Distribution=Ubuntu&amp;version=24.04&amp;installer_type=deb_local){.reference .external}.

2.  Download the appropriate firmware for your hardware PSID from the [NVIDIA official website](https://network.nvidia.com/support/firmware/connectx7/){.reference .external} and flash the device.

3.  To verify driver and firmware versions, use the following command. Replace [`IB`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Device`{.docutils .literal .notranslate}]{.pre} with your specific backend interface.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        ethtool -i <IB Device>
    :::
    ::::
:::

::::: {#install-rocm .section}
### Install ROCm[\#](#install-rocm "Link to this heading"){.headerlink}

Use the following commands to quickly install ROCm 7.0.2 on Ubuntu 24.04:

:::: {.highlight-bash .notranslate}
::: highlight
    wget https://repo.radeon.com/amdgpu-install/7.0.2/ubuntu/noble/amdgpu-install_7.0.2.70002-1_all.deb
    sudo apt install ./amdgpu-install_7.0.2.70002-1_all.deb
    sudo apt update
    sudo apt install python3-setuptools python3-wheel
    sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
    sudo apt install rocm
:::
::::

For detailed installation instructions, refer to the [ROCm 7.0.2 documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.0.2/install/quick-start.html#rocm-installation){.reference .external}.
:::::

::::: {#install-amd-gpu-driver-amdgpu .section}
### Install AMD GPU Driver (amdgpu)[\#](#install-amd-gpu-driver-amdgpu "Link to this heading"){.headerlink}

Use the following commands to quickly install the AMD GPU Driver (ROCm 7.0.2) on Ubuntu 24.04:

:::: {.highlight-bash .notranslate}
::: highlight
    wget https://repo.radeon.com/amdgpu-install/7.0.2/ubuntu/noble/amdgpu-install_7.0.2.70002-1_all.deb
    sudo apt install ./amdgpu-install_7.0.2.70002-1_all.deb
    sudo apt update
    sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
    sudo apt install amdgpu-dkms
:::
::::

For detailed installation instructions, refer to the [ROCm 7.0.2 documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.0.2/install/quick-start.html#amdgpu-driver-installation){.reference .external}.
:::::
::::::::::

:::::::::::::::::: {#network-verification-and-testing .section}
## Network verification and testing[\#](#network-verification-and-testing "Link to this heading"){.headerlink}

Before deploying the inference engine, validate the health and performance of the cluster interconnects.

::::: {#verify-network-connectivity .section}
### Verify network connectivity[\#](#verify-network-connectivity "Link to this heading"){.headerlink}

Verify that all network interfaces are reachable across the cluster nodes. Assuming [`eth0`{.docutils .literal .notranslate}]{.pre} is the management interface, [`eth1`{.docutils .literal .notranslate}]{.pre} is for the VPC, and [`eth2`{.docutils .literal .notranslate}]{.pre} through [`eth9`{.docutils .literal .notranslate}]{.pre} are the dedicated RoCE backend interfaces, use the following loop to test reachability to a remote node (for instance, a target node with host IP suffix [`.3`{.docutils .literal .notranslate}]{.pre}).

:::: {.highlight-bash .notranslate}
::: highlight
    # Test connectivity for RoCE subnets 192.168.50.x through 192.168.57.x
    for i in {0..7}; do ping -c 1 192.168.5${i}.3; done
:::
::::
:::::

::::::: {#validate-your-rdma-setup .section}
### Validate your RDMA setup[\#](#validate-your-rdma-setup "Link to this heading"){.headerlink}

Confirm that all eight RDMA network interfaces are in [`UP`{.docutils .literal .notranslate}]{.pre} state. Verify the MTU setting of [`4096`{.docutils .literal .notranslate}]{.pre} and ensure each device has a valid GID mapped to its assigned IP address.

:::: {.highlight-bash .notranslate}
::: highlight
    ibv_devinfo -v
:::
::::

The output should look something like this:

:::: {.highlight-bash .notranslate}
::: highlight
    hca_id: mlx5_0
            transport:                      InfiniBand (0)
            fw_ver:                         28.46.3048
            ...
            board_id:                       MT_0000000838
            phys_port_cnt:                  1
                    port:   1
                            state:                  PORT_ACTIVE (4)
                            max_mtu:                4096 (5)
                            active_mtu:             4096 (5)
                            sm_lid:                 0
                            port_lid:               0
                            port_lmc:               0x00
                            link_layer:             Ethernet
                            ...
                            GID[  0]:               fe80:0000:0000:0000:d894:24ff:fe4a:96e2, RoCE v1
                            GID[  1]:               fe80::d894:24ff:fe4a:96e2, RoCE v2
                            GID[  2]:               0000:0000:0000:0000:0000:ffff:c0a8:3903, RoCE v1
                            GID[  3]:               ::ffff:192.168.57.3, RoCE v2
:::
::::
:::::::

::::::::: {#run-rdma-bandwidth-benchmarks .section}
### Run RDMA bandwidth benchmarks[\#](#run-rdma-bandwidth-benchmarks "Link to this heading"){.headerlink}

Verify the inter-node RDMA performance to ensure the network fabric can saturate the link bandwidth.

::::: {#install-rdma-performance-tools .section}
#### Install RDMA Performance Tools[\#](#install-rdma-performance-tools "Link to this heading"){.headerlink}

To get started, build the ROCm-optimized [`rdma-perftest`{.docutils .literal .notranslate}]{.pre} test suite from source:

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt install -y libibumad-dev libpci-dev libibverbs-dev librdmacm-dev ibverbs-utils libtool
    git clone https://github.com/ROCm/rdma-perftest
    cd rdma-perftest/
    ./autogen.sh
    ./configure --enable-rocm --with-rocm=/opt/rocm
    make -j$(nproc)
    sudo make install
:::
::::
:::::

::::: {#run-a-bandwidth-test-gpu-memory .section}
#### Run a bandwidth test (GPU memory)[\#](#run-a-bandwidth-test-gpu-memory "Link to this heading"){.headerlink}

Perform a bandwidth test using ROCm GPU memory between two nodes. One acts as a server and the other acts as a client. For 400G interfaces, the expected peak throughput is approximately 390 Gbps. Replace [`<SERVER_IP>`{.docutils .literal .notranslate}]{.pre} with the appropriate IP.

:::: {.highlight-bash .notranslate}
::: highlight
    # On Server Node
    ./ib_write_bw --use_rocm=0 -d mlx5_0 --report_gbits -a

    # On Client Node
    ./ib_write_bw --use_rocm=0 -d mlx5_0 --report_gbits -a <SERVER_IP>
:::
::::
:::::
:::::::::
::::::::::::::::::

::::::::::::::::::::: {#vllm-serving-and-mori-unit-tests .section}
## vLLM serving and MoRI unit tests[\#](#vllm-serving-and-mori-unit-tests "Link to this heading"){.headerlink}

::::: {#install-docker-engine .section}
### Install Docker Engine[\#](#install-docker-engine "Link to this heading"){.headerlink}

Install the Docker engine to manage the containerized vLLM and MoRI serving environments.

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt update && sudo apt install -y docker.io
:::
::::
:::::

::::: {#download-the-deepseek-ptpc-model .section}
### Download the DeepSeek PTPC model[\#](#download-the-deepseek-ptpc-model "Link to this heading"){.headerlink}

This guide uses the [DeepSeek-R1-FP8-Dynamic](https://huggingface.co/EmbeddedLLM/deepseek-r1-FP8-Dynamic){.reference .external} model optimized for PTPC. Use the following commands to install the Hugging Face CLI and download the model to your shared NFS directory:

:::: {.highlight-bash .notranslate}
::: highlight
    # Set up a virtual environment and install the Hugging Face CLI
    sudo apt update && sudo apt install -y python3-venv
    python3 -m venv ~/venvs/hf
    source ~/venvs/hf/bin/activate
    pip install huggingface_hub

    # Download the model to the shared NFS mount point
    hf download --token <your_hf_token> \
        EmbeddedLLM/deepseek-r1-FP8-Dynamic \
        --local-dir /mount/point/models/EmbeddedLLM/deepseek-r1-FP8-Dynamic
:::
::::
:::::

::::: {#launch-the-serving-container .section}
### Launch the serving container[\#](#launch-the-serving-container "Link to this heading"){.headerlink}

Deploy the vLLM MoRI serving Docker container on each node.

:::: {.highlight-bash .notranslate}
::: highlight
    CONTAINER_NAME=vllm_mori
    IMAGE_NAME=aigmkt/vllm:mori_rocm6.4.1_20251105

    docker run -it \
        --rm \
        --device /dev/dri --device /dev/kfd --device=/dev/infiniBand \
        --network host --ipc host \
        --group-add video \
        --cap-add SYS_PTRACE \
        --security-opt seccomp=unconfined \
        --privileged \
        -v /mount/point/models:/models \
        --shm-size 128G \
        --name ${CONTAINER_NAME} \
        ${IMAGE_NAME} /bin/bash
:::
::::
:::::

:::::: {#run-mori-inter-node-unit-tests .section}
### Run MoRI inter-node unit tests[\#](#run-mori-inter-node-unit-tests "Link to this heading"){.headerlink}

Before starting the vLLM service, run the MoRI unit test to verify that the inter-node communication backend is correctly configured.

The key configuration variables are:

- [`GLOO_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre}: The network interface used for backend initialization such as [`eth2`{.docutils .literal .notranslate}]{.pre}.

- [`<MASTER_IP>`{.docutils .literal .notranslate}]{.pre}: The IP address of the primary node's backend interface.

::: {.admonition .note}
Note

You can find reference performance data in the [ROCm/MoRI repository](https://github.com/ROCm/mori?tab=readme-ov-file#mori-ep){.reference .external}.
:::

:::: {.highlight-bash .notranslate}
::: highlight
    # Set up environment inside the container
    cd /app/mori
    export PYTHONPATH=/app/mori:$PYTHONPATH
    export GLOO_SOCKET_IFNAME=<BACKEND_INTERFACE>

    # Node 0 (Primary)
    torchrun --nnodes=2 --node_rank=0 --nproc_per_node=1 \
        --master_addr="<MASTER_IP>" --master_port=1234 \
        examples/ops/dispatch_combine/test_dispatch_combine_internode.py \
        --cmd bench --kernel-type v1

    # Node 1 (Secondary)
    torchrun --nnodes=2 --node_rank=1 --nproc_per_node=1 \
        --master_addr="<MASTER_IP>" --master_port=1234 \
        examples/ops/dispatch_combine/test_dispatch_combine_internode.py \
        --cmd bench --kernel-type v1
:::
::::
::::::

::::::: {#deploy-and-serve-the-model .section}
### Deploy and serve the model[\#](#deploy-and-serve-the-model "Link to this heading"){.headerlink}

To deploy DeepSeek-R1 (PTPC) with Expert Parallelism 16 (EP16) across two nodes, use the following serving scripts.

::: {#create-serving-scripts .section}
#### Create serving scripts[\#](#create-serving-scripts "Link to this heading"){.headerlink}

Create the following scripts inside the container on each node.

- Node 0 (master node): [`ep16_node0.sh`{.docutils .literal .notranslate}]{.pre}

  :::: {.highlight-bash .notranslate}
  ::: highlight
      #!/bin/bash

      # Add VLLM_ENFORCE_EPLB=1 to enforce EP balance
      export VLLM_ROCM_USE_AITER=1
      export VLLM_ROCM_USE_AITER_MOE=1
      export VLLM_LOGGING_LEVEL=INFO
      export VLLM_USE_V1=1
      export VLLM_ROCM_USE_AITER_MLA=1
      export VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=0
      export VLLM_ALL2ALL_BACKEND=mori

      vllm serve /models/EmbeddedLLM/deepseek-r1-FP8-Dynamic/ \
          -dp 16 \
          --enable-expert-parallel \
          --data-parallel-size-local 8 \
          --data-parallel-address ${IP} \
          --data-parallel-rpc-port 1212 \
          --served-model-name deepseek \
          --port 8777 \
          --block-size 1 \
          --distributed-executor-backend mp \
          --gpu-memory-utilization 0.8 \
          --max-model-len 8192 \
          --max-num-batched-tokens 4096 \
          --max-num-seqs 4096 \
          --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "custom_ops": ["+quant_fp8"]}' \
          --cuda-graph-sizes 1 2 4 8 16 32 64 128 256 \
          --kv-cache-dtype fp8 \
          --no-enable-prefix-caching \
          --trust-remote-code 2>&1 | tee serving_node0_ep16.log
  :::
  ::::

- Node 1: [`ep16_node1.sh`{.docutils .literal .notranslate}]{.pre}

  :::: {.highlight-bash .notranslate}
  ::: highlight
      #!/bin/bash

      # Add VLLM_ENFORCE_EPLB=1 to enforce EP balance
      export VLLM_ROCM_USE_AITER=1
      export VLLM_ROCM_USE_AITER_MOE=1
      export VLLM_LOGGING_LEVEL=INFO
      export VLLM_USE_V1=1
      export VLLM_ROCM_USE_AITER_MLA=1
      export VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS=0
      export VLLM_ALL2ALL_BACKEND=mori

      vllm serve /models/EmbeddedLLM/deepseek-r1-FP8-Dynamic/ \
              -dp 16 \
              --enable-expert-parallel \
              --headless \
              --data-parallel-size-local 8 \
              --data-parallel-start-rank 8 \
              --data-parallel-address ${IP} \
              --data-parallel-rpc-port 1212 \
              --served-model-name deepseek \
              --port 8777 \
              --block-size 1 \
              --distributed-executor-backend mp \
              --gpu_memory_utilization 0.8 \
              --max-model-len 8192 \
              --max_num_batched_token 4096 \
              --max-num-seqs 4096 \
              --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY", "custom_ops": ["+quant_fp8"]}' \
              --cuda-graph-sizes 1 2 4 8 16 32 64 128 256 \
              --kv-cache-dtype fp8 \
              --no-enable-prefix-caching \
              --trust-remote-code 2>&1 | tee serving_node1_ep16.log
  :::
  ::::
:::

::::: {#run-the-serving-scripts .section}
#### Run the serving scripts[\#](#run-the-serving-scripts "Link to this heading"){.headerlink}

Run the scripts on each node to launch the distributed serving instance. Replace [`<MASTER_IP>`{.docutils .literal .notranslate}]{.pre} with the backend network IP of Node 0.

:::: {.highlight-bash .notranslate}
::: highlight
    # On Node 0 (Primary)
    export NCCL_SOCKET_IFNAME=<BACKEND_INTERFACE>
    export GLOO_SOCKET_IFNAME=<BACKEND_INTERFACE>
    IP=<MASTER_IP> bash ep16_node0.sh

    # On Node 1 (Secondary)
    export NCCL_SOCKET_IFNAME=<BACKEND_INTERFACE>
    export GLOO_SOCKET_IFNAME=<BACKEND_INTERFACE>
    IP=<MASTER_IP> bash ep16_node1.sh
:::
::::
:::::
:::::::
:::::::::::::::::::::

::::::::: {#reproducing-performance .section}
## Reproducing performance[\#](#reproducing-performance "Link to this heading"){.headerlink}

This section details how to reproduce the performance metrics published in the AMD ROCm Blog: [Practical, Fault-Robust Distributed Inference for DeepSeek on AMD MI300X](https://rocm.blogs.amd.com/software-tools-optimization/wide-ep-deepseek/README.html){.reference .external}.

:::: {#configuration-for-ep16-16-gpus .section}
### Configuration for EP16 (16 GPUs)[\#](#configuration-for-ep16-16-gpus "Link to this heading"){.headerlink}

To achieve the reported throughput, expert parallelism 16 (EP16) is used across the decode nodes.

::: {#benchmark-target .section}
#### Benchmark target[\#](#benchmark-target "Link to this heading"){.headerlink}

- Decode throughput: \~12.4k output tokens/s per node.
:::
::::

:::::: {#performance-reproduction-commands .section}
### Performance reproduction commands[\#](#performance-reproduction-commands "Link to this heading"){.headerlink}

Use the following configurations to reproduce published performance metrics.

::::: {#decode-benchmark .section}
#### Decode benchmark[\#](#decode-benchmark "Link to this heading"){.headerlink}

To reproduce the 12.4k output tokens/s, use the following configuration:

:::: {.highlight-bash .notranslate}
::: highlight
    #!/bin/bash

    MAX_CONCURRENCY=${1:-3072}
    TIMES=2
    NUM_PROMPTS=$((MAX_CONCURRENCY*TIMES))
    vllm bench serve \
        --max-concurrency $MAX_CONCURRENCY \
        --num-prompts $NUM_PROMPTS \
        --model /models/EmbeddedLLM/deepseek-r1-FP8-Dynamic/ \
        --served-model-name deepseek \
        --port 8777 \
        --ignore-eos \
        --trust-remote-code \
        --dataset-name random \
        --seed 2025 \
        --random-input-len 2048 \
        --random-output-len 1024 2>&1 | tee bench_decode_${MAX_CONCURRENCY}_isl_2k_osl_1k.log
:::
::::

To calculate the per-node throughput for comparison with the blog data, take the reported **Peak output token throughput (tok/s)** from the benchmark results and divide it by the total number of nodes in the cluster.
:::::
::::::
:::::::::

::::: {#troubleshooting .section}
## Troubleshooting[\#](#troubleshooting "Link to this heading"){.headerlink}

The following section outlines common issues and their solutions.

::: {#bandwidth-test-fails-with-error .section}
### Bandwidth test fails with error[\#](#bandwidth-test-fails-with-error "Link to this heading"){.headerlink}

1.  Use ROCm-optimized [`rdma-perftest`{.docutils .literal .notranslate}]{.pre}, not the generic [`perftest`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        which ib_write_bw
    :::
    ::::

2.  Confirm the [`SERVER_IP`{.docutils .literal .notranslate}]{.pre} is accessible.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        ping <SERVER_IP>
    :::
    ::::

3.  Check system logs, use [`dmesg`{.docutils .literal .notranslate}]{.pre} for kernel-level errors.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        sudo dmesg -T | grep -i 'error|warn|fail|exception'
    :::
    ::::
:::

::: {#vllm-ep-16-with-mori-backend-fails-to-launch .section}
### vLLM EP 16 with MoRI backend fails to launch[\#](#vllm-ep-16-with-mori-backend-fails-to-launch "Link to this heading"){.headerlink}

1.  Error: [`Waiting`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`for`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`init`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`message`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`from`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`front-end.`{.docutils .literal .notranslate}]{.pre} Check the connectivity of the [`IP`{.docutils .literal .notranslate}]{.pre}. Disable firewall/selinux or allow traffic for port [`1212`{.docutils .literal .notranslate}]{.pre}.

2.  Verify server name resolution. Ensure server names are correctly mapped in [`/etc/hosts`{.docutils .literal .notranslate}]{.pre}.

3.  Confirm whether environment variable [`GLOO_SOCKET_IFNAME`{.docutils .literal .notranslate}]{.pre} is set before running the vLLM serving script.
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](sglang.html "previous page"){.left-prev}

::: prev-next-info
previous

SGLang inference performance testing DeepSeek-R1-Distill-Qwen-32B
:::

[](sglang-mori-distributed.html "next page"){.right-next}

::: prev-next-info
next

SGLang distributed inference with MoRI
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [Prerequisites](#prerequisites){.reference .internal .nav-link}
- [System configuration](#system-configuration){.reference .internal .nav-link}
  - [Verify baseline software](#verify-baseline-software){.reference .internal .nav-link}
  - [Verify best known configuration (BKC)](#verify-best-known-configuration-bkc){.reference .internal .nav-link}
  - [Run basic system health checks](#run-basic-system-health-checks){.reference .internal .nav-link}
  - [Configure your backend network (netplan)](#configure-your-backend-network-netplan){.reference .internal .nav-link}
  - [Configure your network file system (NFS)](#configure-your-network-file-system-nfs){.reference .internal .nav-link}
  - [Configure static hostname resolution for backend initialization (optional)](#configure-static-hostname-resolution-for-backend-initialization-optional){.reference .internal .nav-link}
- [Software installation](#software-installation){.reference .internal .nav-link}
  - [Install CX7 driver and firmware](#install-cx7-driver-and-firmware){.reference .internal .nav-link}
  - [Install ROCm](#install-rocm){.reference .internal .nav-link}
  - [Install AMD GPU Driver (amdgpu)](#install-amd-gpu-driver-amdgpu){.reference .internal .nav-link}
- [Network verification and testing](#network-verification-and-testing){.reference .internal .nav-link}
  - [Verify network connectivity](#verify-network-connectivity){.reference .internal .nav-link}
  - [Validate your RDMA setup](#validate-your-rdma-setup){.reference .internal .nav-link}
  - [Run RDMA bandwidth benchmarks](#run-rdma-bandwidth-benchmarks){.reference .internal .nav-link}
    - [Install RDMA Performance Tools](#install-rdma-performance-tools){.reference .internal .nav-link}
    - [Run a bandwidth test (GPU memory)](#run-a-bandwidth-test-gpu-memory){.reference .internal .nav-link}
- [vLLM serving and MoRI unit tests](#vllm-serving-and-mori-unit-tests){.reference .internal .nav-link}
  - [Install Docker Engine](#install-docker-engine){.reference .internal .nav-link}
  - [Download the DeepSeek PTPC model](#download-the-deepseek-ptpc-model){.reference .internal .nav-link}
  - [Launch the serving container](#launch-the-serving-container){.reference .internal .nav-link}
  - [Run MoRI inter-node unit tests](#run-mori-inter-node-unit-tests){.reference .internal .nav-link}
  - [Deploy and serve the model](#deploy-and-serve-the-model){.reference .internal .nav-link}
    - [Create serving scripts](#create-serving-scripts){.reference .internal .nav-link}
    - [Run the serving scripts](#run-the-serving-scripts){.reference .internal .nav-link}
- [Reproducing performance](#reproducing-performance){.reference .internal .nav-link}
  - [Configuration for EP16 (16 GPUs)](#configuration-for-ep16-16-gpus){.reference .internal .nav-link}
    - [Benchmark target](#benchmark-target){.reference .internal .nav-link}
  - [Performance reproduction commands](#performance-reproduction-commands){.reference .internal .nav-link}
    - [Decode benchmark](#decode-benchmark){.reference .internal .nav-link}
- [Troubleshooting](#troubleshooting){.reference .internal .nav-link}
  - [Bandwidth test fails with error](#bandwidth-test-fails-with-error){.reference .internal .nav-link}
  - [vLLM EP 16 with MoRI backend fails to launch](#vllm-ep-16-with-mori-backend-fails-to-launch){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
