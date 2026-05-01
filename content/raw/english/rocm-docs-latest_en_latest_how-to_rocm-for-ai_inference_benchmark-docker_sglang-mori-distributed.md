---
title: "SGLang distributed inference with MoRI"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/rocm-for-ai/inference/benchmark-docker/sglang-mori-distributed.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-01
---

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
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
- SGLang\...
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
# SGLang distributed inference with MoRI

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
  - [Install AMD Pensando Pollara 400 AI NIC drivers](#install-amd-pensando-pollara-400-ai-nic-drivers){.reference .internal .nav-link}
  - [Configure thermal management (fan speed)](#configure-thermal-management-fan-speed){.reference .internal .nav-link}
    - [Configure fan speed via Redfish (Supermicro)](#configure-fan-speed-via-redfish-supermicro){.reference .internal .nav-link}
  - [Configure your backend network (netplan)](#configure-your-backend-network-netplan){.reference .internal .nav-link}
  - [Configure Quality of Service (QoS) and Congestion Control (DCQCN)](#configure-quality-of-service-qos-and-congestion-control-dcqcn){.reference .internal .nav-link}
    - [Configure DCQCN](#configure-dcqcn){.reference .internal .nav-link}
    - [Configure QoS and PFC](#configure-qos-and-pfc){.reference .internal .nav-link}
    - [Verification your configuration](#verification-your-configuration){.reference .internal .nav-link}
  - [Configure your network file system (NFS)](#configure-your-network-file-system-nfs){.reference .internal .nav-link}
- [Software installation](#software-installation){.reference .internal .nav-link}
  - [Install ROCm](#install-rocm){.reference .internal .nav-link}
  - [Install AMD GPU Driver (amdgpu)](#install-amd-gpu-driver-amdgpu){.reference .internal .nav-link}
- [Network verification and testing](#network-verification-and-testing){.reference .internal .nav-link}
  - [Verify network connectivity](#verify-network-connectivity){.reference .internal .nav-link}
  - [Validate your RDMA setup](#validate-your-rdma-setup){.reference .internal .nav-link}
    - [Verify link status MTU, NIC temperature, and NIC speed](#verify-link-status-mtu-nic-temperature-and-nic-speed){.reference .internal .nav-link}
    - [Verify GID](#verify-gid){.reference .internal .nav-link}
  - [Run RDMA bandwidth benchmarks](#run-rdma-bandwidth-benchmarks){.reference .internal .nav-link}
    - [Install RDMA Performance Tools](#install-rdma-performance-tools){.reference .internal .nav-link}
    - [Run a bandwidth test (GPU memory)](#run-a-bandwidth-test-gpu-memory){.reference .internal .nav-link}
- [SGLang serving and MoRI unit tests](#sglang-serving-and-mori-unit-tests){.reference .internal .nav-link}
  - [Install Docker Engine](#install-docker-engine){.reference .internal .nav-link}
  - [Launch the serving container](#launch-the-serving-container){.reference .internal .nav-link}
  - [Run MoRI inter-node unit tests](#run-mori-inter-node-unit-tests){.reference .internal .nav-link}
- [End-to-end 1P2D performance testing](#end-to-end-1p2d-performance-testing){.reference .internal .nav-link}
  - [Download the model and setup your run environment](#download-the-model-and-setup-your-run-environment){.reference .internal .nav-link}
  - [Clone the SGLang disaggregation recipe](#clone-the-sglang-disaggregation-recipe){.reference .internal .nav-link}
  - [Configure InfiniBand devices](#configure-infiniband-devices){.reference .internal .nav-link}
  - [Configure the script and submit the job](#configure-the-script-and-submit-the-job){.reference .internal .nav-link}
  - [Log file analysis](#log-file-analysis){.reference .internal .nav-link}
- [Troubleshooting](#troubleshooting){.reference .internal .nav-link}
  - [Bandwidth test fails with error](#bandwidth-test-fails-with-error){.reference .internal .nav-link}
  - [Slurm job fails](#slurm-job-fails){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#sglang-distributed-inference-with-mori .section .tex2jax_ignore .mathjax_ignore}
# SGLang distributed inference with MoRI[\#](#sglang-distributed-inference-with-mori "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-21
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 23 min read time
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

This document provides a comprehensive guide for deploying a high-performance SGLang distributed inference serving environment on an AMD Instinct MI355X GPU cluster, utilizing the [MoRI (Modular RDMA Interface)](https://github.com/rocm/mori){.reference .external} communication backend for optimized inter-node collective operations. It also includes systematic instructions for benchmarking 1P2D (1 prefill 2 decode, 3 nodes) configurations using automated scripts.

::: {#prerequisites .section}
## Prerequisites[\#](#prerequisites "Link to this heading"){.headerlink}

The following configuration is required to implement this setup:

- **Nodes:** A minimum of three GPU nodes (Virtual machines or Physical machines) for wide expert parallelism (EP) evaluation.

- **GPUs** 8x AMD Instinct MI355X GPU cards per node.

- **Networking:** 8x AMD Pensando™ Pollara 400 AI NICs per node, providing a dedicated 1:1 mapping between GPUs and network interfaces for optimal inter-node communication.

- **Orchestration:** A Slurm cluster with at least three nodes -- one for prefill service and two for decode services (EP16)
:::

:::::::::::::::::::::::::::::::::: {#system-configuration .section}
## System configuration[\#](#system-configuration "Link to this heading"){.headerlink}

This section outlines the infrastructure setup required to support your AMD Instinct MI355X cluster. It covers essential procedures for verifying software baselines and firmware versions, configuring the AMD Pensando Pollara 400 AI NICs for high-bandwidth networking, and applying thermal and Quality of Service (QoS) tunings to ensure a stable, lossless RDMA fabric.

:::: {#verify-baseline-software .section}
[]{#sglang-mori-verify-baseline}

### Verify baseline software[\#](#verify-baseline-software "Link to this heading"){.headerlink}

The following table outlines the validated software stack. Use the provided shell commands to verify the environment on each node before proceeding.

::: pst-scrollable-table-container
  Component                    Version              Verification command
  ---------------------------- -------------------- ----------------------------------------------------------------------------------------------------------------------------------------------
  **OS**                       Ubuntu 22.04.5 LTS   [`cat`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/etc/os-release`{.docutils .literal .notranslate}]{.pre}
  **Kernel**                   5.15.0-163-generic   [`uname`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-r`{.docutils .literal .notranslate}]{.pre}
  **ROCm**                     7.1.1                [`amd-smi`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`version`{.docutils .literal .notranslate}]{.pre}
  **PLDM bundle (firmware)**   01.25.16.03          [Verify BKC](#verify-best-known-configuration-bkc){.reference .internal}
  **AI NIC Firmware**          1.117.5.a.45         [`dkms`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`status`{.docutils .literal .notranslate}]{.pre}
  **AI NIC Driver**            25.11.1.001          [`dkms`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`status`{.docutils .literal .notranslate}]{.pre}
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

Before proceeding with software deployment, verify that all cluster nodes comply with the [MI355X Basic Health Checks](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/gpus/mi355x.html#basic-health-checks){.reference .external} Key requirements include specific kernel boot arguments, minimum system memory thresholds, PCIe Gen5 link stability, and so on.
:::

::::: {#install-amd-pensando-pollara-400-ai-nic-drivers .section}
### Install AMD Pensando Pollara 400 AI NIC drivers[\#](#install-amd-pensando-pollara-400-ai-nic-drivers "Link to this heading"){.headerlink}

For detailed instructions on upgrading the firmware and installing drivers for the AMD Pensando Pollara 400 AI NIC, refer to the [AMD Instinct System Acceptance Guide](https://instinct.docs.amd.com/projects/system-acceptance/en/latest/network/nic-installation.html#amd-pensando-pollara-400-ai-nic){.reference .external}. After installation, verify the active firmware version on all NICs to ensure it matches the software baseline. See [Verify baseline software](#verify-best-known-configuration-bkc){.reference .internal}.

To display the current firmware version for all AI NICs, use the following command.

:::: {.highlight-bash .notranslate}
::: highlight
    sudo nicctl show version firmware
:::
::::
:::::

:::::: {#configure-thermal-management-fan-speed .section}
### Configure thermal management (fan speed)[\#](#configure-thermal-management-fan-speed "Link to this heading"){.headerlink}

For systems equipped with 400G optics, standard fan profiles are often insufficient for maintaining stable operating temperatures. To prevent thermal throttling or optics failure, the system fans must be set to [`FullSpeed`{.docutils .literal .notranslate}]{.pre}.

- Requirement: A fan speed of approximately 25,000 RPM is required to maintain the AI NIC modules at an optimal operating temperature (\~50°C).

- Constraint: Default profiles (typically around 4,000 RPM) and "Performance IO" settings (around 9,000 RPM) do not provide adequate airflow for 400G optical transceivers.

::::: {#configure-fan-speed-via-redfish-supermicro .section}
#### Configure fan speed via Redfish (Supermicro)[\#](#configure-fan-speed-via-redfish-supermicro "Link to this heading"){.headerlink}

Run the following command to set the fan mode to [`FullSpeed`{.docutils .literal .notranslate}]{.pre} through the BMC:

:::: {.highlight-bash .notranslate}
::: highlight
    # Define BMC connection variables
    BMC_IP="<BMC_IP>"
    AUTH="<username>:<password>"

    # Set Fan Mode to FullSpeed
    curl -X PATCH "https://${BMC_IP}/redfish/v1/Managers/1/Oem/Supermicro/FanMode" \
         -k -u "${AUTH}" \
         -H "Content-Type: application/json" \
         -d '{"Mode": "FullSpeed"}'
:::
::::
:::::
::::::

:::::::::: {#configure-your-backend-network-netplan .section}
### Configure your backend network (netplan)[\#](#configure-your-backend-network-netplan "Link to this heading"){.headerlink}

Configure the backend NICs for high-bandwidth inter-node communication. Suppose the GPU's eight network interface controllers (NICs) are [`benic1p1`{.docutils .literal .notranslate}]{.pre} to [`benic8p1`{.docutils .literal .notranslate}]{.pre}. Each NIC must have its own subnet that is disjoint from the others. Each node needs a unique IP address on each subnet. You should use the same final octet in each subnet for a given node. For example, one node would have the addresses [`192.168.1.36`{.docutils .literal .notranslate}]{.pre}, [`192.168.2.36`{.docutils .literal .notranslate}]{.pre}, and so on. Another node would have [`192.168.1.37`{.docutils .literal .notranslate}]{.pre}, [`192.168.2.37`{.docutils .literal .notranslate}]{.pre}, and so on. Ensure MTU is set to [`9000`{.docutils .literal .notranslate}]{.pre}.

::: {.admonition .note}
Note

Ensure you identify the correct interface names for your system using ip link before applying this configuration.
:::

For example, your [`/etc/netplan/70-backend.yaml`{.docutils .literal .notranslate}]{.pre} should look like the following:

:::: {.highlight-yaml .notranslate}
::: highlight
    network:
      ethernets:
        benic8p1:
          addresses:
          - 192.168.8.38/31
          match:
            macaddress: 04:90:81:2a:34:08
          mtu: 9000
          routes:
          - table: 108
            to: 0.0.0.0/0
            via: 192.168.8.39
          routing-policy:
          - from: 192.168.8.38
            table: 108
          set-name: benic8p1
        benic7p1:
          addresses:
          - 192.168.7.38/31
          match:
            macaddress: 04:90:81:2b:82:40
          mtu: 9000
          routes:
          - table: 107
            to: 0.0.0.0/0
            via: 192.168.7.39
          routing-policy:
          - from: 192.168.7.38
            table: 107
          set-name: benic7p1
        benic6p1:
          addresses:
          - 192.168.6.38/31
          match:
            macaddress: 04:90:81:30:c9:30
          mtu: 9000
          routes:
          - table: 106
            to: 0.0.0.0/0
            via: 192.168.6.39
          routing-policy:
          - from: 192.168.6.38
            table: 106
          set-name: benic6p1
        benic5p1:
          addresses:
          - 192.168.5.38/31
          match:
            macaddress: 04:90:81:2a:23:40
          mtu: 9000
          routes:
          - table: 105
            to: 0.0.0.0/0
            via: 192.168.5.39
          routing-policy:
          - from: 192.168.5.38
            table: 105
          set-name: benic5p1
        benic4p1:
          addresses:
          - 192.168.4.38/31
          match:
            macaddress: 04:90:81:2d:69:60
          mtu: 9000
          routes:
          - table: 104
            to: 0.0.0.0/0
            via: 192.168.4.39
          routing-policy:
          - from: 192.168.4.38
            table: 104
          set-name: benic4p1
        benic3p1:
          addresses:
          - 192.168.3.38/31
          match:
            macaddress: 04:90:81:2a:2c:40
          mtu: 9000
          routes:
          - table: 103
            to: 0.0.0.0/0
            via: 192.168.3.39
          routing-policy:
          - from: 192.168.3.38
            table: 103
          set-name: benic3p1
        benic2p1:
          addresses:
          - 192.168.2.38/31
          match:
            macaddress: 04:90:81:30:d5:30
          mtu: 9000
          routes:
          - table: 102
            to: 0.0.0.0/0
            via: 192.168.2.39
          routing-policy:
          - from: 192.168.2.38
            table: 102
          set-name: benic2p1
        benic1p1:
          addresses:
          - 192.168.1.38/31
          match:
            macaddress: 04:90:81:30:e4:00
          mtu: 9000
          routes:
          - table: 101
            to: 0.0.0.0/0
            via: 192.168.1.39
          routing-policy:
          - from: 192.168.1.38
            table: 101
          set-name: benic1p1
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

:::::::::: {#configure-quality-of-service-qos-and-congestion-control-dcqcn .section}
### Configure Quality of Service (QoS) and Congestion Control (DCQCN)[\#](#configure-quality-of-service-qos-and-congestion-control-dcqcn "Link to this heading"){.headerlink}

To ensure lossless communication and optimal performance for RDMA traffic, the network must be configured with specific QoS and Data Center Quantized Congestion Notification (DCQCN) settings.

The following configuration achieves: • It enables RX and TX Pause frames on the ports • Maps DSCP 24 (Data) to Q3 and DSCP 46 (CNP) to Q6, all other DSCP to Q0 • Enables PFC for Q3 • Scheduling : 99% to Q3, 1% to Q0 and strict priority for Q6

::::: {#configure-dcqcn .section}
#### Configure DCQCN[\#](#configure-dcqcn "Link to this heading"){.headerlink}

Create and run a [`/nfsdata/enable_dcqcn.sh`{.docutils .literal .notranslate}]{.pre} script to initialize congestion control parameters.

:::: {.highlight-bash .notranslate}
::: highlight
    # !/bin/bash

    TOKEN_BUCKET_SIZE=800000
    AI_RATE=160
    ALPHA_UPDATE_INTERVAL=1
    ALPHA_UPDATE_G=512
    INITIAL_ALPHA_VALUE=64
    RATE_INCREASE_BYTE_COUNT=431068
    HAI_RATE=300
    RATE_REDUCE_MONITOR_PERIOD=1
    RATE_INCREASE_THRESHOLD=1
    RATE_INCREASE_INTERVAL=1
    CNP_DSCP=46

    ROCE_DEVICES=$(ibv_devices | grep ionic_ | awk '{print $1}' | paste -sd " ")
    for roce_dev in $ROCE_DEVICES
    do
        sudo nicctl update dcqcn -r $roce_dev -i 1 \
        --token-bucket-size $TOKEN_BUCKET_SIZE \
        --ai-rate $AI_RATE \
        --alpha-update-interval $ALPHA_UPDATE_INTERVAL \
        --alpha-update-g $ALPHA_UPDATE_G \
        --initial-alpha-value $INITIAL_ALPHA_VALUE \
        --rate-increase-byte-count $RATE_INCREASE_BYTE_COUNT \
        --hai-rate $HAI_RATE \
        --rate-reduce-monitor-period $RATE_REDUCE_MONITOR_PERIOD \
        --rate-increase-threshold $RATE_INCREASE_THRESHOLD  \
        --rate-increase-interval $RATE_INCREASE_INTERVAL \
        --cnp-dscp $CNP_DSCP
    done
:::
::::
:::::

::::: {#configure-qos-and-pfc .section}
#### Configure QoS and PFC[\#](#configure-qos-and-pfc "Link to this heading"){.headerlink}

Create and run [`/nfsdata/qos.sh`{.docutils .literal .notranslate}]{.pre} to set up traffic classes and scheduling.

:::: {.highlight-bash .notranslate}
::: highlight
    #!/bin/bash
    # qos.sh

    # Enable PFC and Auto-negotiation on all ports
    for i in $(sudo nicctl show port | grep Port | awk {'print $3'}); do sudo nicctl update port -p $i --pause-type pfc --rx-pause enable --tx-pause enable; done
    for i in $(sudo nicctl show port | grep Port | awk '{print $3}'); do sudo nicctl update port --port $i --auto-neg enable; done

    # Define Priorities
    cts_dscp=46
    cts_prio=6
    data_dscp=24
    data_prio=3
    default_prio=0
    cnp_dscp=46
    cnp_prio=6

    sudo nicctl update qos pfc --priority 0 --no-drop disable
    sudo nicctl update qos dscp-to-purpose --dscp 48 --purpose none
    sudo nicctl update qos dscp-to-purpose --dscp 46 --purpose none
    sudo nicctl update qos --classification-type pcp
    sudo nicctl update qos --classification-type dscp
    sudo nicctl update qos dscp-to-priority --dscp 0-63 --priority 0
    sudo nicctl update qos dscp-to-priority --dscp 0-23,25-45,47-63 --priority $default_prio
    sudo nicctl update qos dscp-to-priority --dscp $cts_dscp --priority $cts_prio
    sudo nicctl update qos dscp-to-priority --dscp $data_dscp --priority $data_prio
    sudo nicctl update qos dscp-to-priority --dscp $cnp_dscp --priority $cnp_prio
    sudo nicctl update qos pfc --priority $data_prio --no-drop enable
    sudo nicctl update qos scheduling --priority $data_prio,$default_prio,$cts_prio --dwrr 99,1,0 --rate-limit 0,0,10
:::
::::
:::::

::: {#verification-your-configuration .section}
#### Verification your configuration[\#](#verification-your-configuration "Link to this heading"){.headerlink}

Verify the configuration using [`nicctl`{.docutils .literal .notranslate}]{.pre}.

- Verify QoS classification:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      sudo nicctl show qos
  :::
  ::::

  Expected QoS output:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      NIC  : 42424650-4c32-3531-3230-303443000000 (0000:f6:00.0)

      Port : 04908130-a7a0-4242-4242-000011010000

      Classification type         : DSCP

      DSCP-to-priority :
      DSCP bitmap               : 0xffffbffffeffffff ==> priority : 0
      DSCP bitmap               : 0x0000000001000000 ==> priority : 3
      DSCP bitmap               : 0x0000400000000000 ==> priority : 6
      DSCP                      : 0-23, 25-45, 47-63 ==> priority : 0
      DSCP                      : 24 ==> priority : 3
      DSCP                      : 46 ==> priority : 6
  :::
  ::::

- Verify DCQCN and scheduling:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      sudo nicctl show dcqcn
  :::
  ::::

  Expected DCQCN and scheduling output:

  :::: {.highlight-bash .notranslate}
  ::: highlight
      NIC : 42424650-4c32-3531-3230-303443000000 (0000:f6:00.0)
      ------------------------------------------------------------------------------------------

      Lif id                                     : 43000070-0100-0000-4242-04908130a7a0
      ROCE device                                : ionic_7
      DCQCN profile id                         : 1
      Status                                   : Enabled
      Rate increase in AI phase                : 160
      Rate increase byte count                 : 431068
      Alpha update G value                     : 512
      Alpha update interval                    : 1
      Rate increase in HAI phase               : 300
      Initial alpha value                      : 64
      Rate reduce monitor period               : 1
      Rate increase threshold                  : 1
      Rate increase interval                   : 1
      Token bucket size                        : 800000
      DSCP value used for CNP                  : 46


      PFC :
      PFC priority bitmap       : 0x8
      PFC no-drop priorities    : 3

      Scheduling :
      --------------------------------------------
      Priority  Scheduling  Bandwidth Rate-limit
                Type        (in %age) (in Gbps)
      --------------------------------------------
      0         DWRR        1         N/A
      3         DWRR        99        N/A
      6         strict      N/A       10
  :::
  ::::
:::
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
::::::::::::::::::::::::::::::::::

::::::::: {#software-installation .section}
## Software installation[\#](#software-installation "Link to this heading"){.headerlink}

Next, install the core compute stack required to operate the AMD Instinct GPUs. The following steps guide you through deploying the ROCm software stack and the necessary kernel-mode drivers to enable hardware acceleration and optimize the environment for distributed inference workloads.

::::: {#install-rocm .section}
### Install ROCm[\#](#install-rocm "Link to this heading"){.headerlink}

Use the following commands to quickly install ROCm 7.1.1 on Ubuntu 22.04:

:::: {.highlight-bash .notranslate}
::: highlight
    wget https://repo.radeon.com/amdgpu-install/7.1.1/ubuntu/jammy/amdgpu-install_7.1.1.70101-1_all.deb
    sudo apt install ./amdgpu-install_7.1.1.70101-1_all.deb
    sudo apt update
    sudo apt install python3-setuptools python3-wheel
    sudo usermod -a -G render,video $LOGNAME # Add the current user to the render and video groups
    sudo apt install rocm
:::
::::

For detailed installation instructions, refer to the [ROCm 7.1.1 documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.1.1/install/quick-start.html#rocm-installation){.reference .external}.
:::::

::::: {#install-amd-gpu-driver-amdgpu .section}
### Install AMD GPU Driver (amdgpu)[\#](#install-amd-gpu-driver-amdgpu "Link to this heading"){.headerlink}

Use the following commands to quickly install the AMD GPU Driver (ROCm 7.1.1) on Ubuntu 22.04:

:::: {.highlight-bash .notranslate}
::: highlight
    wget https://repo.radeon.com/amdgpu-install/7.1.1/ubuntu/jammy/amdgpu-install_7.1.1.70101-1_all.deb
    sudo apt install ./amdgpu-install_7.1.1.70101-1_all.deb
    sudo apt update
    sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
    sudo apt install amdgpu-dkms
:::
::::

For detailed installation instructions, refer to the [ROCm 7.1.1 documentation](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.1.1/install/quick-start.html#amdgpu-driver-installation){.reference .external}.
:::::
:::::::::

:::::::::::::::::::::::: {#network-verification-and-testing .section}
## Network verification and testing[\#](#network-verification-and-testing "Link to this heading"){.headerlink}

Before deploying the inference engine, validate the health and performance of the cluster interconnects.

::::: {#verify-network-connectivity .section}
### Verify network connectivity[\#](#verify-network-connectivity "Link to this heading"){.headerlink}

Verify that all network interfaces are reachable across the cluster nodes. Assuming [`eth0`{.docutils .literal .notranslate}]{.pre} is the management interface, and [`benic1p1`{.docutils .literal .notranslate}]{.pre} through [`benic8p1`{.docutils .literal .notranslate}]{.pre} are the dedicated RoCE backend interfaces, use the following loop to test reachability to a remote node (for instance, a target node with host IP suffix [`.38`{.docutils .literal .notranslate}]{.pre}).

:::: {.highlight-bash .notranslate}
::: highlight
    # Test connectivity for RoCE subnets 192.168.x.38 (node B) through 192.168.x.37 (node A)
    for i in {1..8}; do ping -c 1 192.168.${i}.38; done
:::
::::
:::::

::::::::::::: {#validate-your-rdma-setup .section}
### Validate your RDMA setup[\#](#validate-your-rdma-setup "Link to this heading"){.headerlink}

Confirm that all eight RDMA network interfaces are in the [`UP`{.docutils .literal .notranslate}]{.pre} state and correctly configured with the required MTU and GID settings.

::::::: {#verify-link-status-mtu-nic-temperature-and-nic-speed .section}
#### Verify link status MTU, NIC temperature, and NIC speed[\#](#verify-link-status-mtu-nic-temperature-and-nic-speed "Link to this heading"){.headerlink}

:::: {.highlight-bash .notranslate}
::: highlight
    sudo nicctl show port
:::
::::

The output should look something like this:

:::: {.highlight-bash .notranslate}
::: highlight
    -------------------------------------------------------------------------------------

    NIC  : 42424650-4c32-3531-3530-314343000000 (0000:f6:00.0)

    Port : 04908132-5d88-4242-4242-000011010000 (eth1/1)
      Spec:
        Ifindex                                  : 0x11010000
        Type                                     : ETH
        speed                                    : 400G
        Admin state                              : UP
        FEC type                                 : RS
        Pause type                               : PFC
        Number of lanes                          : 4
        MTU                                      : 9216
        TX pause                                 : enabled
        RX pause                                 : enabled
        Auto negotiation                         : enabled
      Status:
        Physical port                            : 1
        Operational status                       : UP
        Link FSM state                           : UP
        FEC type                                 : RS
        Cable type                               : Fiber
        Number of lanes                          : 4
        speed                                    : 400G
        Auto negotiation                         : disabled
        MAC ID                                   : 0
        MAC channel                              : 0
        MAC address                              : 04:90:81:32:5d:88
        Transceiver type                         : QSFP_CMIS
        Transceiver state                        : SPROM-READ
        Transceiver PID                          : QSFP-400G-DR4
        Transceiver temperature (in C)           : 45
        Transceiver warning temperature (in C)   : 75
        Transceiver alarm temperature (in C)     : 80
    -------------------------------------------------------------------------------------
:::
::::
:::::::

::::::: {#verify-gid .section}
#### Verify GID[\#](#verify-gid "Link to this heading"){.headerlink}

Ensure each device has a valid GID mapped to its assigned IP address.

:::: {.highlight-bash .notranslate}
::: highlight
    ibv_devinfo -v | grep GID
:::
::::

The output should look something like this:

:::: {.highlight-bash .notranslate}
::: highlight
          GID[  0]:               fe80::690:81ff:fe30:a7a0, RoCE v2
          GID[  1]:               ::ffff:192.168.7.36, RoCE v2
:::
::::
:::::::
:::::::::::::

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

Perform a bandwidth test using ROCm GPU memory between two nodes. One acts as a server and the other acts as a client. Replace [`<SERVER_IP>`{.docutils .literal .notranslate}]{.pre} with the appropriate IP.

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
::::::::::::::::::::::::

::::::::::::: {#sglang-serving-and-mori-unit-tests .section}
## SGLang serving and MoRI unit tests[\#](#sglang-serving-and-mori-unit-tests "Link to this heading"){.headerlink}

::::: {#install-docker-engine .section}
### Install Docker Engine[\#](#install-docker-engine "Link to this heading"){.headerlink}

Install the Docker engine to manage the containerized vLLM and MoRI serving environments.

:::: {.highlight-bash .notranslate}
::: highlight
    sudo apt update && sudo apt install -y docker.io
    sudo usermod -aG docker "$USER"
:::
::::
:::::

::::: {#launch-the-serving-container .section}
### Launch the serving container[\#](#launch-the-serving-container "Link to this heading"){.headerlink}

Deploy the SGLang MoRI serving container on each node.

:::: {.highlight-bash .notranslate}
::: highlight
    CONTAINER_NAME=sglang_mori
    IMAGE_NAME=rocm/sgl-dev:sglang-0.5.6.post1-rocm700-mi35x-mori-0113

    docker run -it \
        --rm \
        --device /dev/dri --device /dev/kfd --device=/dev/infiniBand \
        --network host --ipc host \
        --group-add video \
        --cap-add SYS_PTRACE \
        --security-opt seccomp=unconfined \
        --privileged \
        --shm-size 128G \
        --name ${CONTAINER_NAME} \
        ${IMAGE_NAME} /bin/bash
:::
::::
:::::

:::::: {#run-mori-inter-node-unit-tests .section}
### Run MoRI inter-node unit tests[\#](#run-mori-inter-node-unit-tests "Link to this heading"){.headerlink}

Before starting the vLLM service, run the MoRI unit test to verify that the inter-node communication backend is correctly configured.

MoRI unit test uses 2 nodes as a minimal validation before running the full 1P2D (3 nodes) benchmark.

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
:::::::::::::

::::::::::::: {#end-to-end-1p2d-performance-testing .section}
## End-to-end 1P2D performance testing[\#](#end-to-end-1p2d-performance-testing "Link to this heading"){.headerlink}

This section guides you through running distributed inference benchmarks using the SGLang disagg recipe. For detailed implementation details, refer to the [SGLang Disaggregation Recipe](https://github.com/billishyahao/sglang_disagg/blob/9n_cluster/README.md){.reference .external}.

::::: {#download-the-model-and-setup-your-run-environment .section}
### Download the model and setup your run environment[\#](#download-the-model-and-setup-your-run-environment "Link to this heading"){.headerlink}

This performance test supports the following models:

- [DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3){.reference .external}

- [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1){.reference .external}

- [DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528){.reference .external}

To set up your environment and download the models using the Hugging Face CLI, use the following commands. Modify the [`hf`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`download`{.docutils .literal .notranslate}]{.pre} command to download the desired model.

:::: {.highlight-bash .notranslate}
::: highlight
    # Set up a virtual environment and install the Hugging Face CLI
    sudo apt update && sudo apt install -y python3-venv
    python3 -m venv ~/venvs/hf
    source ~/venvs/hf/bin/activate
    pip install huggingface_hub

    # Download the model to the shared NFS mount point
    # Replace 'deepseek-ai/DeepSeek-R1-0528' with your desired model
    hf download --token <your_hf_token> \
        deepseek-ai/DeepSeek-R1-0528 \
        --local-dir /mount/point/models/DeepSeek-R1
:::
::::
:::::

:::::: {#clone-the-sglang-disaggregation-recipe .section}
### Clone the SGLang disaggregation recipe[\#](#clone-the-sglang-disaggregation-recipe "Link to this heading"){.headerlink}

Clone the SGLang disaggregation repository to the shared file system and switch to the appropriate branch:

:::: {.highlight-bash .notranslate}
::: highlight
    git clone https://github.com/billishyahao/sglang_disagg.git
    git checkout 9n_cluster
    cd sglang_disagg
:::
::::

::: {.admonition .note}
Note

In the 1P2D configuration, the prefill service and benchmark process run on the same node, while remaining nodes handle decode services.
:::
::::::

::: {#configure-infiniband-devices .section}
### Configure InfiniBand devices[\#](#configure-infiniband-devices "Link to this heading"){.headerlink}

Identify and configure the available InfiniBand devices.

1.  List available devices using the following command.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        ibv_devinfo -l
    :::
    ::::

    Example output:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        8 HCAs found:
                ionic_0
                ionic_1
                ionic_2
                ionic_3
                ionic_4
                ionic_5
                ionic_6
                ionic_7
    :::
    ::::

2.  Update environment variables. Edit [`set_env_vars.sh`{.docutils .literal .notranslate}]{.pre} and add the comma-separated list of your system's IB devices. For example:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        export IBDEVICES=ionic_0,ionic_1,ionic_2,ionic_3,ionic_4,ionic_5,ionic_6,ionic_7
    :::
    ::::
:::

::: {#configure-the-script-and-submit-the-job .section}
### Configure the script and submit the job[\#](#configure-the-script-and-submit-the-job "Link to this heading"){.headerlink}

1.  To set the required configuration parameters, update the following environment variables in [`run_submit_disagg.sh`{.docutils .literal .notranslate}]{.pre} to match your cluster setup:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        # SLURM Job Configuration
        export SLURM_ACCOUNT="amd"       # The account name for SLURM job accounting and resource allocation
        export SLURM_PARTITION="compute" # The specific cluster partition (queue) to submit the job to
        export TIME_LIMIT="24:00:00"     # Maximum wall time for the job (Hours:Minutes:Seconds)

        # Model Configuration
        export MODEL_PATH="/nfsdata"     # Base directory where the model weights are stored
        export MODEL_NAME="DeepSeek-R1"  # Specific model directory name (joined with MODEL_PATH)
        export CONTAINER_IMAGE="rocm/sgl-dev:sglang-0.5.6.post1-rocm700-mi35x-mori-1224" # Docker image to use for the environment

        # Cluster Topology (Disaggregation Setup)
        export PREFILL_NODES=1           # Number of prefill nodes
        export PREFILL_WORKERS=1         # Number of prefill workers
        export DECODE_NODES=2            # Number of decode nodes
        export DECODE_WORKERS=2          # Number of decode workers

        # Benchmark/Workload Parameters
        export ISL=1024                  # Input Sequence Length (number of tokens in the prompt)
        export OSL=1024                  # Output Sequence Length (number of tokens to generate)
        export CONCURRENCIES="2048"      # Total number of concurrent requests to simulate in the benchmark. The value can be "32,64,128"
        export REQUEST_RATE="inf"        # Request per second rate. "inf" means send all requests immediately

        # Parallelism Strategies
        export PREFILL_ENABLE_EP=true    # Enable Expert Parallelism (EP) for the prefill phase
        export PREFILL_ENABLE_DP=true    # Enable Data Parallelism (DP) for the prefill phase
        export DECODE_ENABLE_EP=true     # Enable Expert Parallelism (EP) for the decode phase
        export DECODE_ENABLE_DP=true     # Enable Data Parallelism (DP) for the decode phase
    :::
    ::::

2.  Then submit the batch job into slurm cluster through [`bash`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`./run_submit_disagg.sh`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-bash .notranslate}
    ::: highlight
        bash ./run_submit_disagg.sh
    :::
    ::::
:::

::: {#log-file-analysis .section}
### Log file analysis[\#](#log-file-analysis "Link to this heading"){.headerlink}

1.  After submission, retrieve the SLURM job ID:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        squeue
    :::
    ::::

    Example output:

    :::: {.highlight-bash .notranslate}
    ::: highlight
        JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
        123   compute       1p2d   alice  R    00:10:32      4 node[01-04]
    :::
    ::::

2.  A directory named [`slurm_job-$SLURM_JOB_ID`{.docutils .literal .notranslate}]{.pre} is created in [`/tmp`{.docutils .literal .notranslate}]{.pre} on each participating node. The directory contains:

    ::: pst-scrollable-table-container
      Log File                                                                                     Description
      -------------------------------------------------------------------------------------------- --------------------------------
      [`pd_sglang_bench_serving.sh_NODE${NODE_RANK}.log`{.docutils .literal .notranslate}]{.pre}   Main service log per node
      [`decode_NODE${NODE_RANK}.log`{.docutils .literal .notranslate}]{.pre}                       SGLang decode service details
      [`prefill_NODE${NODE_RANK}.log`{.docutils .literal .notranslate}]{.pre}                      SGLang prefill service details
    :::

3.  The benchmark results will be displayed in [`pd_sglang_bench_serving.sh_NODE${NODE_RANK}.log`{.docutils .literal .notranslate}]{.pre}. Key metrics include:

    ::: {.admonition .note}
    Note

    The following benchmark utility output is provided for reference only and should not be used to compare performance. See the [InferenceMAX](https://inferencemax.semianalysis.com/){.reference .external} website for validated performance results.
    :::

    :::: {.highlight-bash .notranslate}
    ::: highlight
        ============ Serving Benchmark Result ============
        Successful requests:                     20480
        Benchmark duration (s):                  1194.25
        Total input tokens:                      20971520
        Total generated tokens:                  20971520
        Request throughput (req/s):              17.15
        Output token throughput (tok/s):         17560.38
        Total Token throughput (tok/s):          35120.76
        ---------------Time to First Token----------------
        Mean TTFT (ms):                          21601.77
        Median TTFT (ms):                        24525.21
        P99 TTFT (ms):                           85417.53
        -----Time per Output Token (excl. 1st token)------
        Mean TPOT (ms):                          92.41
        Median TPOT (ms):                        85.46
        P99 TPOT (ms):                           138.67
        ---------------Inter-token Latency----------------
        Mean ITL (ms):                           92.41
        Median ITL (ms):                         74.76
        P99 ITL (ms):                            263.07
        ----------------End-to-end Latency----------------
        Mean E2EL (ms):                          116133.48
        Median E2EL (ms):                        110349.39
        P99 E2EL (ms):                           227243.97
        ==================================================
    :::
    ::::
:::
:::::::::::::

::::: {#troubleshooting .section}
## Troubleshooting[\#](#troubleshooting "Link to this heading"){.headerlink}

The following section outlines common issues and their solutions.

::: {#bandwidth-test-fails-with-error .section}
### Bandwidth test fails with error[\#](#bandwidth-test-fails-with-error "Link to this heading"){.headerlink}

1.  Use ROCm-optimized [`rdma-perftest`{.docutils .literal .notranslate}]{.pre}, not the generic [`perftest`{.docutils .literal .notranslate}]{.pre}

    :::: {.highlight-bash .notranslate}
    ::: highlight
        which ib_write_bw
    :::
    ::::

2.  Confirm the [`SERVER_IP`{.docutils .literal .notranslate}]{.pre} is accessible

    :::: {.highlight-bash .notranslate}
    ::: highlight
        ping <SERVER_IP>
    :::
    ::::

3.  Check system logs, use [`dmesg`{.docutils .literal .notranslate}]{.pre} for kernel-level errors

    :::: {.highlight-bash .notranslate}
    ::: highlight
        sudo dmesg -T | grep -i 'error|warn|fail|exception'
    :::
    ::::
:::

::: {#slurm-job-fails .section}
### Slurm job fails[\#](#slurm-job-fails "Link to this heading"){.headerlink}

Common causes and solutions for Slurm job submission failures include:

1.  Shared storage access:

    - Verify that both [`sglang_disagg`{.docutils .literal .notranslate}]{.pre} and model directories are located in a shared NFS mount accessible to all compute nodes.

    - Ensure proper permissions: [`chmod`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-R`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`755`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/shared/path/sglang_disagg`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`/shared/path/models`{.docutils .literal .notranslate}]{.pre}

2.  Log analysis:

    - Examine [`pd_sglang_bench_serving.sh_NODE${NODE_RANK}.log`{.docutils .literal .notranslate}]{.pre} on each participating node for detailed error messages.

    - Check for common issues like missing dependencies, GPU allocation failures, or network connectivity problems.

3.  Configuration validation:

    - Verify SLURM parameters in [`run_submit_disagg.sh`{.docutils .literal .notranslate}]{.pre}:

      - [`SLURM_ACCOUNT`{.docutils .literal .notranslate}]{.pre}: Ensure your account has access to the cluster

      - [`SLURM_PARTITION`{.docutils .literal .notranslate}]{.pre}: Confirm the partition exists and is accessible

      - [`MODEL_PATH`{.docutils .literal .notranslate}]{.pre}: Check that the path is correct and accessible from compute nodes

      - [`MODEL_NAME`{.docutils .literal .notranslate}]{.pre}: Verify the model subdirectory exists within [`MODEL_PATH`{.docutils .literal .notranslate}]{.pre}

    - Use [`sinfo`{.docutils .literal .notranslate}]{.pre} to check partition and node availability.
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](vllm-mori-distributed.html "previous page"){.left-prev}

::: prev-next-info
previous

vLLM distributed inference with MoRI
:::

[](sglang-distributed.html "next page"){.right-next}

::: prev-next-info
next

SGLang distributed inference with Mooncake
:::
:::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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
  - [Install AMD Pensando Pollara 400 AI NIC drivers](#install-amd-pensando-pollara-400-ai-nic-drivers){.reference .internal .nav-link}
  - [Configure thermal management (fan speed)](#configure-thermal-management-fan-speed){.reference .internal .nav-link}
    - [Configure fan speed via Redfish (Supermicro)](#configure-fan-speed-via-redfish-supermicro){.reference .internal .nav-link}
  - [Configure your backend network (netplan)](#configure-your-backend-network-netplan){.reference .internal .nav-link}
  - [Configure Quality of Service (QoS) and Congestion Control (DCQCN)](#configure-quality-of-service-qos-and-congestion-control-dcqcn){.reference .internal .nav-link}
    - [Configure DCQCN](#configure-dcqcn){.reference .internal .nav-link}
    - [Configure QoS and PFC](#configure-qos-and-pfc){.reference .internal .nav-link}
    - [Verification your configuration](#verification-your-configuration){.reference .internal .nav-link}
  - [Configure your network file system (NFS)](#configure-your-network-file-system-nfs){.reference .internal .nav-link}
- [Software installation](#software-installation){.reference .internal .nav-link}
  - [Install ROCm](#install-rocm){.reference .internal .nav-link}
  - [Install AMD GPU Driver (amdgpu)](#install-amd-gpu-driver-amdgpu){.reference .internal .nav-link}
- [Network verification and testing](#network-verification-and-testing){.reference .internal .nav-link}
  - [Verify network connectivity](#verify-network-connectivity){.reference .internal .nav-link}
  - [Validate your RDMA setup](#validate-your-rdma-setup){.reference .internal .nav-link}
    - [Verify link status MTU, NIC temperature, and NIC speed](#verify-link-status-mtu-nic-temperature-and-nic-speed){.reference .internal .nav-link}
    - [Verify GID](#verify-gid){.reference .internal .nav-link}
  - [Run RDMA bandwidth benchmarks](#run-rdma-bandwidth-benchmarks){.reference .internal .nav-link}
    - [Install RDMA Performance Tools](#install-rdma-performance-tools){.reference .internal .nav-link}
    - [Run a bandwidth test (GPU memory)](#run-a-bandwidth-test-gpu-memory){.reference .internal .nav-link}
- [SGLang serving and MoRI unit tests](#sglang-serving-and-mori-unit-tests){.reference .internal .nav-link}
  - [Install Docker Engine](#install-docker-engine){.reference .internal .nav-link}
  - [Launch the serving container](#launch-the-serving-container){.reference .internal .nav-link}
  - [Run MoRI inter-node unit tests](#run-mori-inter-node-unit-tests){.reference .internal .nav-link}
- [End-to-end 1P2D performance testing](#end-to-end-1p2d-performance-testing){.reference .internal .nav-link}
  - [Download the model and setup your run environment](#download-the-model-and-setup-your-run-environment){.reference .internal .nav-link}
  - [Clone the SGLang disaggregation recipe](#clone-the-sglang-disaggregation-recipe){.reference .internal .nav-link}
  - [Configure InfiniBand devices](#configure-infiniband-devices){.reference .internal .nav-link}
  - [Configure the script and submit the job](#configure-the-script-and-submit-the-job){.reference .internal .nav-link}
  - [Log file analysis](#log-file-analysis){.reference .internal .nav-link}
- [Troubleshooting](#troubleshooting){.reference .internal .nav-link}
  - [Bandwidth test fails with error](#bandwidth-test-fails-with-error){.reference .internal .nav-link}
  - [Slurm job fails](#slurm-job-fails){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
