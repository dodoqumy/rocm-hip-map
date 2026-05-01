---
title: "AMD RDNA2 system optimization"
source_url: "https://rocm.docs.amd.com/en/latest/how-to/system-optimization/w6000-v620.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:57:19.031280+00:00
content_hash: "613fa721c5c8d8b9"
---

:::::::::::::::::::::::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::::::::::::::::::::::
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
# AMD RDNA2 system optimization

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::::::::::::::::::::::
{#amd-rdna2-system-optimization .section .tex2jax_ignore .mathjax_ignore}
# AMD RDNA2 system optimization[\#](#amd-rdna2-system-optimization "Link to this heading"){.headerlink}

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
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux

{.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}

::::
:::::
::::::
:::::::
::::::::

:
{#workstation-workloads .section}
## Workstation workloads[\#](#workstation-workloads "Link to this heading"){.headerlink}

Workstation workloads, much like those for HPC, have a unique set of requirements: a blend of both graphics and compute, certification, stability and others.

The document covers specific software requirements and processes needed to use these GPUs for Single Root I/O Virtualization (SR-IOV) and machine learning tasks.

The main purpose of this document is to help users utilize the RDNA™ 2 GPUs to their full potential.

pst-scrollable-table-container
  System Guide                                                Architecture reference                                                                                                                                     White papers
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------
  [System settings](#system-settings){.reference .internal}   [AMD RDNA 2 instruction set architecture](https://www.amd.com/system/files/TechDocs/rdna2-shader-instruction-set-architecture.pdf){.reference .external}   [RDNA 2 architecture](https://www.amd.com/system/files/documents/rdna2-explained-radeon-pro-W6000.pdf){.reference .external}

:

::::::::::::::::
{#system-settings .section}
## System settings[\#](#system-settings "Link to this heading"){.headerlink}

This chapter reviews system settings that are required to configure the system for ROCm virtualization on RDNA2-based AMD Radeon™ PRO GPUs. Installing ROCm on Bare Metal follows the routine ROCm [[installation procedure]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager-index.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}.

To enable ROCm virtualization on V620, one has to setup Single Root I/O Virtualization (SR-IOV) in the BIOS via setting found in the following ([[System BIOS settings]{.std .std-ref}](#bios-settings){.reference .internal}). A tested configuration can be followed in ([[Operating system settings]{.std .std-ref}](#os-settings){.reference .internal}).

{.admonition .attention}
Attention

SR-IOV is supported on V620 and unsupported on W6800.

:
{#system-bios-settings .section}
[]{#bios-settings}

### System BIOS settings[\#](#system-bios-settings "Link to this heading"){.headerlink}

pst-scrollable-table-container
  Advanced / North Bridge Configuration   IOMMU             Enabled   Input-output Memory Management Unit
  --------------------------------------- ----------------- --------- -------------------------------------
  Advanced / North Bridge Configuration   ACS Enable        Enabled   Access Control Service
  Advanced / PCIe/PCI/PnP Configuration   SR-IOV Support    Enabled   Single Root I/O Virtualization
  Advanced / ACPI settings                PCI AER Support   Enabled   Advanced Error Reporting

  : [Settings for the system BIOS in an ASrock platform.]{.caption-text}[\#](#v620-bios "Link to this table"){.headerlink} {#v620-bios .table}

To set up the host, update SBIOS to version 1.2a.
:

:::::::::::
{#operating-system-settings .section}
[]{#os-settings}

### Operating system settings[\#](#operating-system-settings "Link to this heading"){.headerlink}

pst-scrollable-table-container
  Server         [SMC 4124](https://www.supermicro.com/en/Aplus/system/4U/4124/AS-4124GS-TNR.cfm){.reference .external} \[AS -4124GS-TNR\]
  -------------- ---------------------------------------------------------------------------------------------------------------------------
  Host OS        Ubuntu 20.04.3 LTS
  Host Kernel    5.4.0-97-generic
  CPU            AMD EPYC 7552 48-Core Processor
  GPU            RDNA2 V620 (D603GLXE)
  SBIOS          Version SMC_r_1.2a
  VBIOS          113-D603GLXE-077
  Guest OS 1     Ubuntu 20.04.5 LTS
  Guest OS 2     RHEL 9.0
  GIM Driver     gim-dkms_1.0.0.1234577_all
  VM CPU Cores   32
  VM RAM         64 GB

  : [System Configuration Prerequisites]{.caption-text}[\#](#v620-prereq "Link to this table"){.headerlink} {#v620-prereq .table}

Install the following Kernel-based Virtual Machine (KVM) Hypervisor packages:

:
{.highlight-shell .notranslate}

highlight
    sudo apt-get -y install qemu-kvm qemu-utils  bridge-utils virt-manager  gir1.2-spiceclientgtk*  gir1.2-spice-client-gtk* libvirt-daemon-system dnsmasq-base
    sudo virsh net-start default /*to enable Virtual network by default

:

Enable input-output memory management unit (IOMMU) in GRUB settings by adding the following line to [`/etc/default/grub`{.docutils .literal .notranslate}]{.pre}:

:
{.highlight-none .notranslate}

highlight
    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" for AMD CPU

:

Update grub and reboot

:
{.highlight-shell .notranslate}

highlight
    sudo update=grub
    sudo reboot

:

Install the GPU-IOV Module (GIM, where IOV is I/O Virtualization) driver and follow the steps below.z

:
{.highlight-shell .notranslate}

highlight
    sudo dpkg -i <gim_driver>
    sudo reboot
    # Load Host Driver to Create 1VF
    sudo modprobe gim vf_num=1
    # Note: If GIM driver loaded successfully, we could see "gim info:(gim_init:213) *****Running GIM*****" in dmesg
    lspci -d 1002:

:

Which should output something like:

:
{.highlight-none .notranslate}

highlight
    01:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Device 1478
    02:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Device 1479
    03:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 73a1
    03:02.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 73ae → VF

:
:::::::::::

{#guest-os-installation .section}
### Guest OS installation[\#](#guest-os-installation "Link to this heading"){.headerlink}

First, assign GPU virtual function (VF) to VM using the following steps.

1.  Shut down the VM.

2.  Run [`virt-manager`{.docutils .literal .notranslate}]{.pre}

3.  In the **Virtual Machine Manager** GUI, select the **VM** and click **Open**.

    ![Virtual Machine Manager](../../_images/tuning014.png)

4.  In the VM GUI, go to **Show Virtual Hardware Details \> Add Hardware** to configure hardware.

    ![Show virtual hardware details](../../_images/tuning015.png)

5.  Go to **Add Hardware \> PCI Host Device \> VF** and click **Finish**.

    ![VF Selection](../../_images/tuning016.png)

Then start the VM.

Finally install ROCm on the virtual machine (VM). For detailed instructions, refer to the [[Linux install guide]{.xref .std .std-doc}](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/package-manager-index.html "(in ROCm installation on Linux v7.2.2)"){.reference .external}.

::::::::::::::::
::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::
