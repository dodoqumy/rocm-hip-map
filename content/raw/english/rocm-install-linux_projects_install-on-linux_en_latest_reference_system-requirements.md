---
title: "System requirements (Linux)"
source_url: "https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- System\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# System requirements (Linux)

## Contents

- [Supported GPUs](#supported-gpus){.reference .internal .nav-link}
- [Supported operating systems](#supported-operating-systems){.reference .internal .nav-link}
- [Virtualization support](#virtualization-support){.reference .internal .nav-link}
- [CPU support](#cpu-support){.reference .internal .nav-link}



# System requirements (Linux)[\#](#system-requirements-linux "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-04-17

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 9 min read time

Applies to Linux



## Supported GPUs[\#](#supported-gpus "Link to this heading"){.headerlink}

The following table shows the supported AMD Instinct™ GPUs, and Radeon™ PRO and Radeon GPUs. If a GPU is not listed on this table, it's not officially supported by AMD.

GPUs listed in the following table support compute workloads (no display information or graphics). If you're using ROCm with AMD Radeon™ GPUs or Ryzen™ APUs for graphics workloads, see the [Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html){.reference .external} documentation to verify compatibility and system requirements.

Note

If your GPU is not listed, it might be community-enabled through [TheRock](https://github.com/ROCm/TheRock?tab=readme-ov-file#therock){.reference .external} nightly builds. For more information, see [TheRock supported GPUs](https://github.com/ROCm/TheRock/blob/main/SUPPORTED_GPUS.md){.reference .external}. For installation guidance, see [TheRock releases](https://github.com/ROCm/TheRock/blob/main/RELEASES.md){.reference .external}.

AMD Instinct

::: pst-scrollable-table-container
+-------------------------+------------+--------------+-------------+---------+
| GPU                     | Series     | Architecture | LLVM target | Support |
+=========================+============+==============+=============+=========+
| AMD Instinct MI355X     | MI350      | CDNA4        | gfx950      | ✅ [^1] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI350X     | MI350      | CDNA4        | gfx950      | ✅ [^2] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI325X     | MI300      | CDNA3        | gfx942      | ✅ [^3] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI300X     | MI300      | CDNA3        | gfx942      | ✅ [^4] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI300A     | MI300      | CDNA3        | gfx942      | ✅ [^5] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI250X     | MI200      | CDNA2        | gfx90a      | ✅ [^6] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI250      | MI200      | CDNA2        | gfx90a      | ✅ [^7] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI210      | MI200      | CDNA2        | gfx90a      | ✅ [^8] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI100      | MI100      | CDNA         | gfx908      | ✅ [^9] |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI50       | N/A        | GCN5.1       | gfx906      | ❌      |
+-------------------------+------------+--------------+-------------+---------+
| AMD Instinct MI25       | N/A        | GCN5.0       | gfx900      | ❌      |
+-------------------------+------------+--------------+-------------+---------+

AMD Radeon PRO

::: pst-scrollable-table-container
+--------------------------------+---------------+---------------+----------+
| GPU                            | Architecture  | LLVM target   | Support  |
+================================+===============+===============+==========+
| AMD Radeon AI PRO R9700        | RDNA4         | gfx1201       | ✅ [^10] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon AI PRO R9600D       | RDNA4         | gfx1201       | ✅ [^11] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO V710            | RDNA3         | gfx1101       | ✅ [^12] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO W7900 Dual Slot | RDNA3         | gfx1100       | ✅ [^13] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO W7900           | RDNA3         | gfx1100       | ✅ [^14] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO W7800 48GB      | RDNA3         | gfx1100       | ✅ [^15] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO W7800           | RDNA3         | gfx1100       | ✅ [^16] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO W7700           | RDNA3         | gfx1101       | ✅ [^17] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO W6800           | RDNA2         | gfx1030       | ✅ [^18] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO V620            | RDNA2         | gfx1030       | ✅ [^19] |
+--------------------------------+---------------+---------------+----------+
| AMD Radeon PRO VII             | GCN5.1        | gfx906        | ❌       |
+--------------------------------+---------------+---------------+----------+

AMD Radeon

::: pst-scrollable-table-container
+-------------------------------+---------------+---------------+----------+
| GPU                           | Architecture  | LLVM target   | Support  |
+===============================+===============+===============+==========+
| AMD Radeon RX 9070 XT         | RDNA4         | gfx1201       | ✅ [^20] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 9070 GRE        | RDNA4         | gfx1201       | ✅ [^21] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 9070            | RDNA4         | gfx1201       | ✅ [^22] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 9060 XT LP      | RDNA4         | gfx1200       | ✅ [^23] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 9060 XT         | RDNA4         | gfx1200       | ✅ [^24] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 9060            | RDNA4         | gfx1200       | ✅ [^25] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 7900 XTX        | RDNA3         | gfx1100       | ✅ [^26] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 7900 XT         | RDNA3         | gfx1100       | ✅ [^27] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 7900 GRE        | RDNA3         | gfx1100       | ✅ [^28] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 7800 XT         | RDNA3         | gfx1101       | ✅ [^29] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 7700 XT         | RDNA3         | gfx1101       | ✅ [^30] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon RX 7700            | RDNA3         | gfx1101       | ✅ [^31] |
+-------------------------------+---------------+---------------+----------+
| AMD Radeon VII                | GCN5.1        | gfx906        | ❌       |
+-------------------------------+---------------+---------------+----------+

✅: **Supported** - Official software distributions of the current ROCm release fully support this hardware.

⚠️: **Deprecated** - The current ROCm release has limited support for this hardware. Existing features and capabilities are maintained, but no new features or optimizations will be added. A future ROCm release will remove support.

❌: **Unsupported** - The current ROCm release does not support this hardware. The HIP runtime might continue to run applications for an unsupported GPU, but prebuilt ROCm libraries are not officially supported and will cause runtime errors.

Important

Systems with multiple GPUs may require [`iommu=pt`{.docutils .literal .notranslate}]{.pre} to be set at boot time to prevent application hangs, as described in [[Issue #5: Application hangs on Multi-GPU systems]{.std .std-ref}](install-faq.html#multi-gpu){.reference .internal}.

Note

See the [[Compatibility matrix]{.xref .std .std-ref}](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html#architecture-support-compatibility-matrix "(in ROCm Documentation v7.2.2)"){.reference .external} for an overview of supported GPU architectures across ROCm releases.

Footnotes

[[\[]{.fn-bracket}1[\]]{.fn-bracket}]{.label} [([1](#id2){role="doc-backlink"},[2](#id3){role="doc-backlink"})]{.backrefs}

AMD Instinct MI355X and MI350X GPUs supports all [[Supported operating systems]{.std .std-ref}](#supported-distributions){.reference .internal} listed below except RHEL 8.10, Debian 12, Rocky Linux 9, and Oracle Linux 8.

[[\[]{.fn-bracket}[2](#id4){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

AMD Instinct MI325X GPU supports all [[Supported operating systems]{.std .std-ref}](#supported-distributions){.reference .internal} listed below except RHEL 8.10, Rocky Linux 9, and Oracle Linux 8.

[[\[]{.fn-bracket}[3](#id5){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

AMD Instinct MI300X GPU supports all [[Supported operating systems]{.std .std-ref}](#supported-distributions){.reference .internal} listed below.

[[\[]{.fn-bracket}[4](#id6){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

AMD Instinct MI300A GPU supports all [[Supported operating systems]{.std .std-ref}](#supported-distributions){.reference .internal} listed below except Debian 13, Oracle Linux 10, Oracle Linux 9, and Oracle Linux 8.

[[\[]{.fn-bracket}5[\]]{.fn-bracket}]{.label} [([1](#id7){role="doc-backlink"},[2](#id8){role="doc-backlink"},[3](#id9){role="doc-backlink"})]{.backrefs}

AMD Instinct MI200 Series GPUs support all [[Supported operating systems]{.std .std-ref}](#supported-distributions){.reference .internal} listed below except Debian 13, Rocky Linux 9, Oracle Linux 10, Oracle Linux 9, and Oracle Linux 8.

[[\[]{.fn-bracket}[6](#id10){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

AMD Instinct MI100 GPU supports all [[Supported operating systems]{.std .std-ref}](#supported-distributions){.reference .internal} listed below except Debian 13, Debian 12, Rocky Linux 9, Oracle Linux 10, Oracle Linux 9, and Oracle Linux 8.

[[\[]{.fn-bracket}7[\]]{.fn-bracket}]{.label} [([1](#id11){role="doc-backlink"},[2](#id12){role="doc-backlink"},[3](#id13){role="doc-backlink"},[4](#id14){role="doc-backlink"},[5](#id15){role="doc-backlink"},[6](#id16){role="doc-backlink"},[7](#id17){role="doc-backlink"},[8](#id18){role="doc-backlink"},[9](#id19){role="doc-backlink"},[10](#id21){role="doc-backlink"},[11](#id22){role="doc-backlink"},[12](#id23){role="doc-backlink"},[13](#id24){role="doc-backlink"},[14](#id25){role="doc-backlink"},[15](#id26){role="doc-backlink"},[16](#id27){role="doc-backlink"},[17](#id28){role="doc-backlink"},[18](#id29){role="doc-backlink"},[19](#id30){role="doc-backlink"},[20](#id31){role="doc-backlink"},[21](#id32){role="doc-backlink"})]{.backrefs}

AMD Radeon PRO (AI PRO R9700, AI PRO R9600D, PRO V710, PRO W7900 Dual Slot, PRO W7900, PRO W7800 48GB, PRO W7800, PRO W7700, and PRO W6800) and AMD Radeon (RX 9070 XT, RX 9070 GRE, RX 9070, RX 9060 XT LP, RX 9060 XT, RX 9060, RX 7900 XTX, RX 7900 XT, RX 7900 GRE, RX 7800 XT, RX 7700 XT, and RX 7700) only support Ubuntu 24.04.4, Ubuntu 22.04.5, RHEL 10.1, and RHEL 9.7.

[[\[]{.fn-bracket}[8](#id20){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

AMD Radeon PRO V620 only supports Ubuntu 24.04.4 and Ubuntu 22.04.5.


## Supported operating systems[\#](#supported-operating-systems "Link to this heading"){.headerlink}

AMD ROCm software supports the following Linux distributions.

::: pst-scrollable-table-container
+----------------------+--------------------------+-----------+-----------+
| Operating system     | Kernel                   | Glibc     | Support   |
+======================+==========================+===========+===========+
| Ubuntu 24.04.4       | 6.8 \[GA\], 6.17 \[HWE\] | 2.39      | ✅        |
+----------------------+--------------------------+-----------+-----------+
| Ubuntu 22.04.5       | 5.15 \[GA\], 6.8 \[HWE\] | 2.35      | ✅        |
+----------------------+--------------------------+-----------+-----------+
| RHEL 10.1            | 6.12.0-124               | 2.39      | ✅ [^32]  |
+----------------------+--------------------------+-----------+-----------+
| RHEL 10.0            | 6.12.0-55                | 2.39      | ✅ [^33]  |
+----------------------+--------------------------+-----------+-----------+
| RHEL 9.7             | 5.14.0-611               | 2.34      | ✅ [^34]  |
+----------------------+--------------------------+-----------+-----------+
| RHEL 9.6             | 5.14.0-570               | 2.34      | ✅ [^35]  |
+----------------------+--------------------------+-----------+-----------+
| RHEL 9.4             | 5.14.0-427               | 2.34      | ✅ [^36]  |
+----------------------+--------------------------+-----------+-----------+
| RHEL 8.10            | 4.18.0-553               | 2.28      | ✅ [^37]  |
+----------------------+--------------------------+-----------+-----------+
| SLES 15 SP7          | 6.4.0-150700.51          | 2.38      | ✅ [^38]  |
+----------------------+--------------------------+-----------+-----------+
| Debian 13            | 6.12                     | 2.35      | ✅ [^39]  |
+----------------------+--------------------------+-----------+-----------+
| Debian 12            | 6.1.0                    | 2.36      | ✅ [^40]  |
+----------------------+--------------------------+-----------+-----------+
| Rocky Linux 9        | 5.14.0-570               | 2.34      | ✅ [^41]  |
+----------------------+--------------------------+-----------+-----------+
| Oracle Linux 10      | 6.12.0 (UEK)             | 2.39      | ✅ [^42]  |
+----------------------+--------------------------+-----------+-----------+
| Oracle Linux 9       | 5.15.0 (UEK)             | 2.34      | ✅ [^43]  |
+----------------------+--------------------------+-----------+-----------+
| Oracle Linux 8       | 5.15.0 (UEK)             | 2.28      | ✅ [^44]  |
+----------------------+--------------------------+-----------+-----------+

Note

- See [Red Hat Enterprise Linux Release Dates](https://access.redhat.com/articles/3078){.reference .external} to learn about the specific kernel versions supported on Red Hat Enterprise Linux (RHEL).

- See [List of SUSE Linux Enterprise Server kernel](https://www.suse.com/support/kb/doc/?id=000019587){.reference .external} to learn about the specific kernel version supported on SUSE Linux Enterprise Server (SLES).

- See the [Compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html "(in ROCm Documentation v7.2.2)"){.reference .external} for an overview of OS support across ROCm releases.

Footnotes

[[\[]{.fn-bracket}9[\]]{.fn-bracket}]{.label} [([1](#id33){role="doc-backlink"},[2](#id34){role="doc-backlink"},[3](#id35){role="doc-backlink"},[4](#id36){role="doc-backlink"})]{.backrefs}

RHEL 10.1 and RHEL 9.7 are supported on all listed [[Supported GPUs]{.std .std-ref}](#supported-gpus){.reference .internal} except AMD Radeon PRO V620 GPU.

[[\[]{.fn-bracket}[10](#id37){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

RHEL 10.0, RHEL 9.6, and RHEL 9.4 are supported on all AMD Instinct GPUs listed under [[Supported GPUs]{.std .std-ref}](#supported-gpus){.reference .internal}.

[[\[]{.fn-bracket}[11](#id38){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

RHEL 8.10 is supported only on AMD Instinct MI300X, MI300A, MI250X, MI250, MI210, and MI100 GPUs.

[[\[]{.fn-bracket}[12](#id39){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

SLES 15 SP7 is supported on all AMD Instinct GPUs listed under [[Supported GPUs]{.std .std-ref}](#supported-gpus){.reference .internal}.

[[\[]{.fn-bracket}[13](#id40){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

Debian 13 is supported only on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs.

[[\[]{.fn-bracket}[14](#id41){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

Debian 12 are supported only on AMD Instinct MI325X, MI300X, MI300A, MI250X, MI250, and MI210 GPUs.

[[\[]{.fn-bracket}[15](#id42){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

Rocky Linux 9 is supported only on AMD Instinct MI300X and MI300A GPUs.

[[\[]{.fn-bracket}16[\]]{.fn-bracket}]{.label} [([1](#id43){role="doc-backlink"},[2](#id44){role="doc-backlink"})]{.backrefs}

Oracle Linux 10 and 9 are supported only on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs.

[[\[]{.fn-bracket}[17](#id45){role="doc-backlink"}[\]]{.fn-bracket}]{.label}

Oracle Linux 8 is supported only on AMD Instinct MI300X GPUs.

## Virtualization support[\#](#virtualization-support "Link to this heading"){.headerlink}

ROCm supports virtualization for the Instinct GPUs and Radeon PRO GPUs listed in the following table.

Important

GPU virtualization with KVM-based SR-IOV requires AMD GPU Virtualization Driver (GIM) driver. Refer to [GIM Release note](https://github.com/amd/MxGPU-Virtualization/releases){.reference .external}.

::: pst-scrollable-table-container
`<style>
   table#virtualization-support-table tbody tr:last-child {
     border-bottom: 2px solid var(--pst-color-border);
   }
   table#virtualization-support-table tbody#virtualization-support-mi210x tr:last-child {
     border-bottom: 2px solid var(--pst-color-primary);
   }
 </style>`{=html}

+-----------------+-------------+---------------------------+-------------------+----------------+
| GPU             | Hypervisor  | Virtualization technology | Host OS           | Guest OS       |
+=================+=============+===========================+===================+================+
| Instinct MI355X | KVM         | Passthrough               | Ubuntu 24.04,\    | Ubuntu 24.04,\ |
|                 |             |                           | RHEL 9.6          | RHEL 9.6       |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | SR-IOV                    | Ubuntu 24.04      | Ubuntu 24.04,\ |
|                 |             |                           |                   | RHEL 10.0,\    |
|                 |             |                           |                   | RHEL 9.6       |
+-----------------+-------------+---------------------------+-------------------+----------------+
| Instinct MI350X | KVM         | Passthrough               | Ubuntu 24.04,\    | Ubuntu 24.04,\ |
|                 |             |                           | RHEL 9.6          | RHEL 9.6       |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | SR-IOV                    | Ubuntu 24.04      | Ubuntu 24.04,\ |
|                 |             |                           |                   | RHEL 10.0,\    |
|                 |             |                           |                   | RHEL 9.6       |
+-----------------+-------------+---------------------------+-------------------+----------------+
| Instinct MI325X | KVM         | Passthrough               | Ubuntu 24.04,\    | Ubuntu 24.04,\ |
|                 |             |                           | Ubuntu 22.04,\    | Ubuntu 22.04,\ |
|                 |             |                           | RHEL 9.6,\        | RHEL 9.6,\     |
|                 |             |                           | RHEL 9.4          | RHEL 9.4       |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | SR-IOV                    | Ubuntu 22.04      | Ubuntu 22.04   |
+-----------------+-------------+---------------------------+-------------------+----------------+
| Instinct MI300X | ESXi        | Passthrough               | ESXi 8.0 Update 3 | Ubuntu 24.04,\ |
|                 |             |                           |                   | Ubuntu 22.04   |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | Passthrough               | Ubuntu 24.04,\    | Ubuntu 24.04,\ |
|                 |             |                           | Ubuntu 22.04,\    | Ubuntu 22.04,\ |
|                 |             |                           | RHEL 9.6,\        | RHEL 9.6,\     |
|                 |             |                           | RHEL 9.4          | RHEL 9.4       |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | SR-IOV                    | Ubuntu 22.04      | Ubuntu 22.04   |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | SR-IOV                    | RHEL 9.4          | Ubuntu 24.04,\ |
|                 |             |                           |                   | RHEL 9.4       |
+-----------------+-------------+---------------------------+-------------------+----------------+
| Instinct MI210  | KVM         | SR-IOV                    | RHEL 9.4          | Ubuntu 22.04,\ |
|                 |             |                           |                   | RHEL 9.4       |
|                 +-------------+---------------------------+-------------------+----------------+
|                 | KVM         | Passthrough               | RHEL 9.4          | Ubuntu 22.04,\ |
|                 |             |                           |                   | RHEL 9.4       |
+-----------------+-------------+---------------------------+-------------------+----------------+
| Radeon PRO V710 | KVM         | SR-IOV                    | Ubuntu 24.04      | Ubuntu 24.04   |
+-----------------+-------------+---------------------------+-------------------+----------------+

Note

AMD Virtualization supports the following:

- Passthrough: All 8 GPUs are assigned directly to a single virtual machine (VM).

- SR-IOV: Provides 1 Virtual Function (VF) per GPU (8 VFs in total), which can be flexibly assigned among multiple VMs (for example, 8 VMs with 1 VF each, 4 VMs with 2 VFs each, or 2 VMs with 4 VFs each)

## CPU support[\#](#cpu-support "Link to this heading"){.headerlink}

ROCm requires CPUs that support PCIe™ atomics. Modern CPUs after the release of 1st generation AMD Zen CPU and Intel™ Haswell support PCIe atomics.

::::: prev-next-area
[](../index.html "previous page"){.left-prev}

::: prev-next-info
previous

ROCm installation for Linux

[](user-kernel-space-compat-matrix.html "next page"){.right-next}

::: prev-next-info
next

User and AMD GPU Driver (amdgpu) support matrix

:::: sidebar-secondary-item
Contents

- [Supported GPUs](#supported-gpus){.reference .internal .nav-link}
- [Supported operating systems](#supported-operating-systems){.reference .internal .nav-link}
- [Virtualization support](#virtualization-support){.reference .internal .nav-link}
- [CPU support](#cpu-support){.reference .internal .nav-link}

[^1]:

[^2]:

[^3]:

[^4]:

[^5]:

[^6]:

[^7]:

[^8]:

[^9]:

[^10]:

[^11]:

[^12]:

[^13]:

[^14]:

[^15]:

[^16]:

[^17]:

[^18]:

[^19]:

[^20]:

[^21]:

[^22]:

[^23]:

[^24]:

[^25]:

[^26]:

[^27]:

[^28]:

[^29]:

[^30]:

[^31]:

[^32]:

[^33]:

[^34]:

[^35]:

[^36]:

[^37]:

[^38]:

[^39]:

[^40]:

[^41]:

[^42]:

[^43]:

[^44]:
