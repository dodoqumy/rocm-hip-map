---
title: "AMD SMI Python interface overview &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/how-to/amdsmi-py-lib.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:13:12.057887+00:00
content_hash: "470612fc79757d9d"
---

# AMD SMI Python interface overview[#](#amd-smi-python-interface-overview)

The AMD SMI Python interface provides a convenient way to interact with AMD
hardware through a simple and accessible [API](../reference/amdsmi-py-api.html).

## Prerequisites[#](#prerequisites)

Before get started, make sure your environment satisfies the following prerequisites.
See the [requirements](../install/install.html#install-reqs) section for more information.

Ensure

`amdgpu`

drivers are installed properly for initialization.Export

`LD_LIBRARY_PATH`

to the`amdsmi`

installation directory.export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/lib:/opt/rocm/lib64:

Install Python 3.6.8+.


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

Note

The environment variable `AMDSMI_GPU_METRICS_CACHE_MS`

may be set to
control the internal GPU metrics cache duration (ms).
Default 1, set to 0 to disable.

The environment variable `AMDSMI_ASIC_INFO_CACHE_MS`

may be set to
control the internal GPU asic info cache duration (ms).
Default 10000 ms, set to 0 to disable.

You can apply them in one of two ways:

In Python code (before the AMDSMI library loads):


```
import os
os.environ["AMDSMI_GPU_METRICS_CACHE_MS"] = "200"
from amdsmi import *
```

Note

On the shell when invoking Python:


```
AMDSMI_GPU_METRICS_CACHE_MS=200 python tools/amdsmi_quick_start.py
```

To get started, the `amdsmi`

folder should be copied and placed next to
the importing script. Import it as follows:

```
from amdsmi import *
try:
amdsmi_init()
# amdsmi calls ...
except AmdSmiException as e:
print(e)
finally:
try:
amdsmi_shut_down()
except AmdSmiException as e:
print(e)
```

### Folder structure[#](#folder-structure)

File name |
Description |
|---|---|
|
Python package initialization file |
|
Amdsmi library Python interface |
|
Python wrapper around amdsmi binary |
|
Amdsmi |

## Usage[#](#usage)

An application using AMD SMI must call `amdsmi_init()`

to initialize the AMI SMI
library before all other calls. This call initializes the internal data
structures required for subsequent AMD SMI operations. In the call, a flag can
be passed to indicate if the application is interested in a specific device
type.

`amdsmi_shut_down()`

must be the last call to properly close connection to
driver and make sure that any resources held by AMD SMI are released.

## Exceptions[#](#exceptions)

All exceptions are in `amdsmi_exception.py`

file.

Exceptions that can be thrown by AMD SMI are:

`AmdSmiException`

: base amdsmi exception class`AmdSmiLibraryException`

: derives base`AmdSmiException`

class and represents errors that can occur in amdsmi-lib. When this exception is thrown,`err_code`

and`err_info`

are set.`err_code`

is an integer that corresponds to errors that can occur in amdsmi-lib and`err_info`

is a string that explains the error that occurred.For example:

try: num_of_GPUs = len(amdsmi_get_processor_handles()) if num_of_GPUs == 0: print("No GPUs on machine") except AmdSmiException as e: print("Error code: {}".format(e.err_code)) if e.err_code == amdsmi_wrapper.AMDSMI_STATUS_RETRY: print("Error info: {}".format(e.err_info))

`AmdSmiRetryException`

: Derives`AmdSmiLibraryException`

class and signals device is busy and call should be retried.`AmdSmiTimeoutException`

: Derives`AmdSmiLibraryException`

class and represents that call had timed out.`AmdSmiParameterException`

: Derives base`AmdSmiException`

class and represents errors related to invaild parameters passed to functions. When this exception is thrown,`err_msg`

is set and it explains what is the actual and expected type of the parameters.`AmdSmiBdfFormatException`

: Derives base`AmdSmiException`

class and represents invalid bdf format.
