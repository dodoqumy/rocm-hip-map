---
title: "AMD SMI Go interface overview &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/how-to/amdsmi-go-lib.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:24:56.446849+00:00
content_hash: "ffd8c4cb2f246c07"
---

# AMD SMI Go interface overview[#](#amd-smi-go-interface-overview)

The AMD SMI Go interface provides a convenient way to interact with AMD
hardware through a simple and accessible [API](../reference/amdsmi-go-api.html).
The API is compatible with Go 1.20 and higher and requires the AMD driver to
be loaded for initialization. Review the [prerequisites](../install/install.html#install-reqs).

## Prerequisites[#](#prerequisites)

Before get started, make sure your environment satisfies the following prerequisites.
See the [requirements](../install/install.html#install-reqs) section for more information.

Ensure

`amdgpu`

drivers are installed properly for initialization.Export

`LD_LIBRARY_PATH`

to the`amdsmi`

installation directory.export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/lib:/opt/rocm/lib64:

Install Go 1.20+.

Download Go from

[https://go.dev/dl/](https://go.dev/dl/)and follow the official installation documentation at[Download and install](https://go.dev/doc/install).Alternatively, use a third-party utility like update-golang.

clone https://github.com/udhos/update-golang cd update-golang sudo ./update-golang.sh source /etc/profile.d/golang_path.sh go version


## Get started[#](#get-started)

Note

`hipcc`

and other compilers will not automatically link in the `libamd_smi`

dynamic library. To compile code that uses the AMD SMI library API, ensure the
`libamd_smi.so`

can be located by setting the `LD_LIBRARY_PATH`

environment
variable to the directory containing `librocm_smi64.so`

(usually
`/opt/rocm/lib`

) or by passing the `-lamd_smi`

flag to the compiler.

A Go application using AMD SMI must call `goamdsmi.GO_gpu_init()`

to initialize
the AMI SMI library before all other calls. This call initializes the internal
data structures required for subsequent AMD SMI operations.

`goamdsmi.GO_gpu_shutdown()`

must be the last call to properly close connection to
driver and make sure that any resources held by AMD SMI are released.

## Usage[#](#usage)

For an example on using the AMD SMI Go API, refer to this implementation
[amd/amd_smi_exporter](https://github.com/amd/amd_smi_exporter/tree/master).

### Add AMD SMI library to your project[#](#add-amd-smi-library-to-your-project)

To include the AMD SMI Go API in your project, update your Makefile or Go module configuration to fetch the appropriate version of the AMD SMI library.

```
# Add to go.mod
go get github.com/ROCm/rocm-systems/projects/amdsmi@develop
```

Then import it:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
```

When using a Makefile, ensure you’re fetching the latest AMD SMI repository
with Go API support. See
[amd/amd_smi_exporter](https://github.com/amd/amd_smi_exporter/blob/master/src/Makefile)
for an example implementation.
