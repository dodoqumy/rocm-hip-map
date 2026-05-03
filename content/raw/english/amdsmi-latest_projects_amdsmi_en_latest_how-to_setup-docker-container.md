---
title: "Using AMD SMI in a Docker container &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/how-to/setup-docker-container.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T12:10:40.557375+00:00
content_hash: "6abe9be84482f87b"
---

# Using AMD SMI in a Docker container[#](#using-amd-smi-in-a-docker-container)

To ensure proper functionality of AMD SMI within a Docker container, the
following configuration options must be included. These settings are
particularly important for managing memory partitions, as partitioning depends
on loading and unloading drivers (with `systemd`

dependencies):

`--cap-add=SYS_MODULE`

This option adds the

`SYS_MODULE`

capability to the container, allowing it to load and interact with kernel modules.Note

Granting

`SYS_MODULE`

increases the container’s privileges and reduces isolation from the host. Use this option only with trusted containers and images.`-v /lib/modules:/lib/modules`

By mounting the

`/lib/modules/`

directory into the container, the container gains access to the host’s kernel modules, allowing it to load and interact with them. Without this access, operations requiring module loading like memory partitioning would fail.

For example:
