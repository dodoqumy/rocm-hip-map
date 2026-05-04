---
title: "RDNA2 workstation tuning guide"
source_url: "https://rocm.docs.amd.com/en/docs-6.0.0/how-to/tuning-guides/w6000-v620.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:17:55.356398+00:00
content_hash: "74cd26c07137a6c3"
---

# RDNA2 workstation tuning guide[#](#rdna2-workstation-tuning-guide)



## System settings[#](#system-settings)

This chapter reviews system settings that are required to configure the system
for ROCm virtualization on RDNA2-based AMD Radeon™ PRO GPUs. Installing ROCm on
Bare Metal follows the routine ROCm
[installation procedure](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/how-to/native-install/index.html).

To enable ROCm virtualization on V620, one has to setup Single Root I/O
Virtualization (SR-IOV) in the BIOS via setting found in the following
([System BIOS settings](#bios-settings)). A tested configuration can be followed in
([Operating system settings](#os-settings)).

Attention

SR-IOV is supported on V620 and unsupported on W6800.

### System BIOS settings[#](#system-bios-settings)

Advanced / North Bridge Configuration |
IOMMU |
Enabled |
Input-output Memory Management Unit |
|---|---|---|---|
Advanced / North Bridge Configuration |
ACS Enable |
Enabled |
Access Control Service |
Advanced / PCIe/PCI/PnP Configuration |
SR-IOV Support |
Enabled |
Single Root I/O Virtualization |
Advanced / ACPI settings |
PCI AER Support |
Enabled |
Advanced Error Reporting |

To set up the host, update SBIOS to version 1.2a.

### Operating system settings[#](#operating-system-settings)

Server |
|
|---|---|
Host OS |
Ubuntu 20.04.3 LTS |
Host Kernel |
5.4.0-97-generic |
CPU |
AMD EPYC 7552 48-Core Processor |
GPU |
RDNA2 V620 (D603GLXE) |
SBIOS |
Version SMC_r_1.2a |
VBIOS |
113-D603GLXE-077 |
Guest OS 1 |
Ubuntu 20.04.5 LTS |
Guest OS 2 |
RHEL 9.0 |
GIM Driver |
gim-dkms_1.0.0.1234577_all |
VM CPU Cores |
32 |
VM RAM |
64 GB |

Install the following Kernel-based Virtual Machine (KVM) Hypervisor packages:

```
apt-get -y install qemu-kvm qemu-utils bridge-utils virt-manager gir1.2-spiceclientgtk* gir1.2-spice-client-gtk* libvirt-daemon-system dnsmasq-base
sudo virsh net-start default /*to enable Virtual network by default
```

Enable input-output memory management unit (IOMMU) in GRUB settings by adding the following line to `/etc/default/grub`

:


Update grub and reboot

```
update=grub
sudo reboot
```

Install the GPU-IOV Module (GIM, where IOV is I/O Virtualization) driver and
follow the steps below. To obtain the GIM driver, write to us
[here](mailto:CloudGPUsupport%40amd.com):

```
dpkg -i <gim_driver>
sudo reboot
# Load Host Driver to Create 1VF
sudo modprobe gim vf_num=1
# Note: If GIM driver loaded successfully, we could see "gim info:(gim_init:213) *****Running GIM*****" in dmesg
lspci -d 1002:
```

Which should output something like:


### Guest OS installation[#](#guest-os-installation)

First, assign GPU virtual function (VF) to VM using the following steps.

Shut down the VM.

Run

`virt-manager`

In the

**Virtual Machine Manager**GUI, select the**VM**and click**Open**.In the VM GUI, go to

**Show Virtual Hardware Details > Add Hardware**to configure hardware.Go to

**Add Hardware > PCI Host Device > VF**and click**Finish**.

Then start the VM.

Finally install ROCm on the virtual machine (VM). For detailed instructions,
refer to the [Linux install guide](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/how-to/native-install/index.html). For any
issue encountered during installation, write to us
[here](mailto:CloudGPUsupport%40amd.com).
