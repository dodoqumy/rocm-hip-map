---
title: "AMD SMI Python API reference &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/reference/amdsmi-py-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:33.897441+00:00
content_hash: "f461a8bfa74c348b"
---

# AMD SMI Python API reference[#](#amd-smi-python-api-reference)

The AMD SMI Python interface provides a convenient way to interact with AMD
hardware through a simple and accessible API. Compatible with Python 3.6 and
higher, this library requires the AMD driver to be loaded for initialization –
review the [prerequisites](../install/install.html#install-reqs).

This section provides comprehensive documentation for the AMD SMI Python API. Explore these sections to understand the full scope of available functionalities and how to implement them in your applications.

## API[#](#api)

### amdsmi_init[#](#amdsmi-init)

Description: Initialize amdsmi with AmdSmiInitFlags

Input parameters: AmdSmiInitFlags

Output: `None`


Exceptions that can be thrown by `amdsmi_init`

function:

`AmdSmiLibraryException`


Initialize GPUs only example:

```
try:
# by default we initalize with AmdSmiInitFlags.INIT_AMD_GPUS
ret = amdsmi_init()
# continue with amdsmi
except AmdSmiException as e:
print("Init GPUs failed")
print(e)
```

Initialize CPUs only example:

```
try:
ret = amdsmi_init(AmdSmiInitFlags.INIT_AMD_CPUS)
# continue with amdsmi
except AmdSmiException as e:
print("Init CPUs failed")
print(e)
```

Initialize both GPUs and CPUs example:

```
try:
ret = amdsmi_init(AmdSmiInitFlags.INIT_AMD_APUS)
# continue with amdsmi
except AmdSmiException as e:
print("Init both GPUs & CPUs failed")
print(e)
```

### amdsmi_shut_down[#](#amdsmi-shut-down)

Description: Finalize and close connection to driver

Input parameters: `None`


Output: `None`


Exceptions that can be thrown by `amdsmi_shut_down`

function:

`AmdSmiLibraryException`


Example:

```
try:
amdsmi_init()
amdsmi_shut_down()
except AmdSmiException as e:
print("Shut down failed")
print(e)
```

### amdsmi_get_processor_type[#](#amdsmi-get-processor-type)

Description: Checks the type of device with provided handle.

Input parameters: device handle as an instance of `amdsmi_processor_handle`


Output: Integer, type of gpu

Exceptions that can be thrown by `amdsmi_get_processor_type`

function:

`AmdSmiLibraryException`


Example:

```
try:
type_of_GPU = amdsmi_get_processor_type(processor_handle)
if type_of_GPU == 1:
print("This is an AMD GPU")
except AmdSmiException as e:
print(e)
```

### amdsmi_get_processor_handles[#](#amdsmi-get-processor-handles)

Description: Returns list of GPU device handle objects on current machine

Input parameters: `None`


Output: List of GPU device handle objects

Exceptions that can be thrown by `amdsmi_get_processor_handles`

function:

`AmdSmiLibraryException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
print(amdsmi_get_gpu_device_uuid(device))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_socket_handles[#](#amdsmi-get-socket-handles)

**Note: CURRENTLY HARDCODED TO RETURN DUMMY DATA**

Description: Returns list of socket device handle objects on current machine

Input parameters: `None`


Output: List of socket device handle objects

Exceptions that can be thrown by `amdsmi_get_socket_handles`

function:

`AmdSmiLibraryException`


Example:

```
try:
sockets = amdsmi_get_socket_handles()
print('Socket numbers: {}'.format(len(sockets)))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_socket_info[#](#amdsmi-get-socket-info)

**Note: CURRENTLY HARDCODED TO RETURN EMPTY VALUES**

Description: Return socket name

Input parameters:
`socket_handle`

socket handle

Output: Socket name

Exceptions that can be thrown by `amdsmi_get_socket_info`

function:

`AmdSmiLibraryException`


Example:

```
try:
socket_handles = amdsmi_get_socket_handles()
if len(socket_handles) == 0:
print("No sockets on machine")
else:
for socket in socket_handles:
print(amdsmi_get_socket_info(socket))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_processor_handle_from_bdf[#](#amdsmi-get-processor-handle-from-bdf)

Description: Returns device handle from the given BDF

Input parameters: bdf string in form of either `<domain>:<bus>:<device>.<function>`

or `<bus>:<device>.<function>`

in hexcode format.
Where:

`<domain>`

is 4 hex digits long from 0000-FFFF interval`<bus>`

is 2 hex digits long from 00-FF interval`<device>`

is 2 hex digits long from 00-1F interval`<function>`

is 1 hex digit long from 0-7 interval

Output: device handle object

Exceptions that can be thrown by `amdsmi_get_processor_handle_from_bdf`

function:

`AmdSmiLibraryException`

`AmdSmiBdfFormatException`


Example:

```
try:
device = amdsmi_get_processor_handle_from_bdf("0000:23:00.0")
print(amdsmi_get_gpu_device_uuid(device))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_device_bdf[#](#amdsmi-get-gpu-device-bdf)

Description: Returns BDF of the given device

Input parameters:

`processor_handle`

dev for which to query

Output: BDF string in form of `<domain>:<bus>:<device>.<function>`

in hexcode format.
Where:

`<domain>`

is 4 hex digits long from 0000-FFFF interval`<bus>`

is 2 hex digits long from 00-FF interval`<device>`

is 2 hex digits long from 00-1F interval`<function>`

is 1 hex digit long from 0-7 interval

Exceptions that can be thrown by `amdsmi_get_gpu_device_bdf`

function:

`AmdSmiParameterException`

`AmdSmiLibraryException`


Example:

```
try:
device = amdsmi_get_processor_handles()[0]
print("Device's bdf:", amdsmi_get_gpu_device_bdf(device))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_device_uuid[#](#amdsmi-get-gpu-device-uuid)

Description: Returns the UUID of the device

Input parameters:

`processor_handle`

dev for which to query

Output: UUID string unique to the device

Exceptions that can be thrown by `amdsmi_get_gpu_device_uuid`

function:

`AmdSmiParameterException`

`AmdSmiLibraryException`


Example:

```
try:
device = amdsmi_get_processor_handles()[0]
print("Device UUID: ", amdsmi_get_gpu_device_uuid(device))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_enumeration_info[#](#amdsmi-get-gpu-enumeration-info)

Description: Returns enumeration information for the given GPU

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Content |
|---|---|
|
DRM render ID |
|
DRM card ID |
|
HSA ID |
|
HIP ID |
|
HIP UUID |

Exceptions that can be thrown by `amdsmi_get_gpu_enumeration_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
for device in devices:
info = amdsmi_get_gpu_enumeration_info(device)
print("DRM Render ID:", info['drm_render'])
print("DRM Card ID:", info['drm_card'])
print("HSA ID:", info['hsa_id'])
print("HIP ID:", info['hip_id'])
print("HIP UUID:", info['hip_uuid'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_driver_info[#](#amdsmi-get-gpu-driver-info)

Description: Returns the info of the driver

Input parameters:

`processor_handle`

dev for which to query

Output: Dictionary with fields

Field |
Content |
|---|---|
|
driver name |
|
driver_version |
|
driver_date |

Exceptions that can be thrown by `amdsmi_get_gpu_driver_info`

function:

`AmdSmiParameterException`

`AmdSmiLibraryException`


Example:

```
try:
device = amdsmi_get_processor_handles()[0]
print("Driver info: ", amdsmi_get_gpu_driver_info(device))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_asic_info[#](#amdsmi-get-gpu-asic-info)

Description: Returns asic information for the given GPU

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Content |
|---|---|
|
market name |
|
vendor id |
|
vendor name |
|
device id |
|
revision id |
|
asic serial |
|
oam id |
|
number of compute units on asic |
|
hardware graphics version |
|
subsystem id |

Exceptions that can be thrown by `amdsmi_get_gpu_asic_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
asic_info = amdsmi_get_gpu_asic_info(device)
print(asic_info)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_kfd_info[#](#amdsmi-get-gpu-kfd-info)

Description: Returns KFD (kernel driver) information for the given GPU This correlates to GUID in rocm-smi

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Content |
|---|---|
|
KFD’s unique GPU identifier |
|
KFD’s internal GPU index |

Exceptions that can be thrown by `amdsmi_get_gpu_kfd_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
kfd_info = amdsmi_get_gpu_kfd_info(device)
print(kfd_info)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_power_cap_info[#](#amdsmi-get-power-cap-info)

Description: Returns dictionary of power capabilities as currently configured on the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query`sensor_ind`

The Package Power Tracking (PPT) type to query

Output: Dictionary with fields

Field |
Description |
Units |
|---|---|---|
|
power capability |
uW |
|
dynamic power management capability |
MHz |
|
default power capability |
uW |
|
min power capability |
uW |
|
max power capability |
uW |

Exceptions that can be thrown by `amdsmi_get_power_cap_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
power_cap_info = amdsmi_get_power_cap_info(device, 0)
print(power_cap_info['power_cap'])
print(power_cap_info['dpm_cap'])
print(power_cap_info['default_power_cap'])
print(power_cap_info['min_power_cap'])
print(power_cap_info['max_power_cap'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_supported_power_cap[#](#amdsmi-get-supported-power-cap)

Description: Returns dictionary of Package Power Tracking (PPT) types as currently configured on the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field | Description | Units
—|—
`sensor_inds`

| List of integer indices of the supported ppt types. 0 indicates PPT0 and 1 indicates PPT1. Should be used as input for `amdsmi_get_power_cap_info`

and `amdsmi_set_power_cap_info`

.
`sensor_types`

| Enum `AmdSmiPowerCapType`

that corresponds to the ppt types that are supported on the device.

Exceptions that can be thrown by `amdsmi_get_supported_power_cap`

function:

`AmdSmiLibraryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
power_cap_types = amdsmi_get_supported_power_cap(device)
print(power_cap_types['sensor_inds'])
print(power_cap_types['sensor_types'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_vram_info[#](#amdsmi-get-gpu-vram-info)

Description: Returns dictionary of vram information for the given GPU.

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Description |
|---|---|
|
vram type |
|
vram vendor |
|
vram size in mb |
|
vram bit width |

Exceptions that can be thrown by `amdsmi_get_gpu_vram_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vram_info = amdsmi_get_gpu_vram_info(device)
print(vram_info['vram_type'])
print(vram_info['vram_vendor'])
print(vram_info['vram_size'])
print(vram_info['vram_bit_width'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_board_info[#](#amdsmi-get-gpu-board-info)

Description: Returns board info for the given GPU

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields correctable and uncorrectable

Field |
Description |
|---|---|
|
Board serial number |
|
Product serial |
|
FRU ID |
|
Product name |
|
Manufacturer name |

Exceptions that can be thrown by `amdsmi_get_gpu_board_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
device = amdsmi_get_processor_handle_from_bdf("0000:23.00.0")
board_info = amdsmi_get_gpu_board_info(device)
print(board_info["model_number"])
print(board_info["product_serial"])
print(board_info["fru_id"])
print(board_info["product_name"])
print(board_info["manufacturer_name"])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_revision[#](#amdsmi-get-gpu-revision)

Description: Returns the GPU revision for a given processor handle.

Input parameters:

`processor_handle`

device which to query

Output: string hex value

Field |
Description |
|---|---|
|
16 bit integer value returned as hex string. |

Exceptions that can be thrown by `amdsmi_get_gpu_revision`

function:

`AmdSmiLibraryException`

If the processor handle is invalid.`AmdSmiParameterException`

If the underlying library call fails.

Example:

```
try:
devices = amdsmi_get_processor_handles(handle)
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
revision = amdsmi_get_gpu_revision(device)
print(revision)
except AmdSmiLibraryException as e:
print(e)
except AmdSmiParameterException as e:
print(e)
```

### amdsmi_get_gpu_cache_info[#](#amdsmi-get-gpu-cache-info)

Description: Returns a list of dictionaries containing cache information for the given GPU.

Input parameters:

`processor_handle`

device which to query

Output: List of Dictionaries containing cache information following the schema below: Schema:

```
{
"cache_properties":
{
"type" : "array",
"items" : {"type" : "string"}
},
"cache_size": {"type" : "number"},
"cache_level": {"type" : "number"},
"max_num_cu_shared": {"type" : "number"},
"num_cache_instance": {"type" : "number"}
}
```

Field |
Description |
|---|---|
|
list of up to 4 cache property type strings. Ex. data (“DATA_CACHE”), instruction (“INST_CACHE”), CPU (“CPU_CACHE”), or SIMD (“SIMD_CACHE”). |
|
size of cache in KB |
|
level of cache |
|
max number of compute units shared |
|
number of cache instances |

Exceptions that can be thrown by `amdsmi_get_gpu_cache_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
cache_info = amdsmi_get_gpu_cache_info(device)
for cache_index, cache_values in cache_info.items():
print(cache_values['cache_properties'])
print(cache_values['cache_size'])
print(cache_values['cache_level'])
print(cache_values['max_num_cu_shared'])
print(cache_values['num_cache_instance'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_vbios_info[#](#amdsmi-get-gpu-vbios-info)

Description: Returns the static information for the VBIOS/IFWI on the device.

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Description |
|---|---|
|
VBIOS/IFWI name |
|
VBIOS/IFWI build date |
|
VBIOS/IFWI part number |
|
VBIOS/IFWI version string |
|
Unified BootLoader version if available; N/A otherwise |

Exceptions that can be thrown by `amdsmi_get_gpu_vbios_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vbios_info = amdsmi_get_gpu_vbios_info(device)
print(vbios_info['name'])
print(vbios_info['build_date'])
print(vbios_info['part_number'])
print(vbios_info['version'])
print(vbios_info['boot_firmware'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_fw_info[#](#amdsmi-get-fw-info)

Description: Returns GPU firmware related information.

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Description |
|---|---|
|
List of dictionaries that contain information about a certain firmware block |

Exceptions that can be thrown by `amdsmi_get_fw_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
firmware_list = amdsmi_get_fw_info(device)['fw_list']
for firmware_block in firmware_list:
print(firmware_block['fw_name'])
# String formated hex or decimal value ie: 21.00.00.AC or 130
print(firmware_block['fw_version'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_activity[#](#amdsmi-get-gpu-activity)

Description: Returns the engine usage for the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary of activites to their respective usage percentage or ‘N/A’ if not supported

Field |
Description |
|---|---|
|
graphics engine usage percentage (0 - 100) |
|
memory engine usage percentage (0 - 100) |
|
average multimedia engine usages in percentage (0 - 100) |

Exceptions that can be thrown by `amdsmi_get_gpu_activity`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
engine_usage = amdsmi_get_gpu_activity(device)
print(engine_usage['gfx_activity'])
print(engine_usage['umc_activity'])
print(engine_usage['mm_activity'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_power_info[#](#amdsmi-get-power-info)

Description: Returns the current power and voltage for the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Description |
Units |
|---|---|---|
|
socket power; matches current or average socket power |
W |
|
current socket power; Mi300+ Series Cards |
W |
|
average socket power; Navi + Mi 200 and earlier Series cards |
W |
|
voltage gfx |
mV |
|
voltage soc |
mV |
|
voltage mem |
mV |
|
power limit |
W |

Exceptions that can be thrown by `amdsmi_get_power_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
power_info = amdsmi_get_power_info(device)
print(power_info['current_socket_power'])
print(power_info['average_socket_power'])
print(power_info['gfx_voltage'])
print(power_info['soc_voltage'])
print(power_info['mem_voltage'])
print(power_info['power_limit'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_vram_usage[#](#amdsmi-get-gpu-vram-usage)

Description: Returns total VRAM and VRAM in use

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Description |
|---|---|
|
VRAM total |
|
VRAM currently in use |

Exceptions that can be thrown by `amdsmi_get_gpu_vram_usage`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vram_usage = amdsmi_get_gpu_vram_usage(device)
print(vram_usage['vram_used'])
print(vram_usage['vram_total'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_violation_status[#](#amdsmi-get-violation-status)

Description: Returns dictionary of violation status information for the given GPU.

Input parameters:

`processor_handle`

The identifier of the given device as an instance of`amdsmi_processor_handle`

.`*violation_status`

pointer to object of type amdsmi_violation_status_t to get the violation status information

Output: Dictionary with fields

Field |
Description |
|---|---|
|
CPU Time Since Epoch in Microseconds |
|
Time of Violation in Nanoseconds |
|
Current Accumulated Counter |
|
Current Accumulated Processor Hot Violation Count |
|
Current Accumulated Package Power Tracking (PPT) PVIOL |
|
Current Accumulated Socket Thermal Count #TVIOL |
|
Current Accumulated Voltage Regulator Count |
|
Current Accumulated High Bandwidth Memory (HBM) Thermal Count |
|
Current Graphic Clock Below Host Limit Count. UPDATED in new driver 1.8: use new acc_gfx_clk_below_host_limit_pwr, acc_gfx_clk_below_host_limit_thm, acc_gfx_clk_below_host_limit_total values |
|
2D array with Accumulated GFX Clk Below Host Limit (Power) per XCP/XCC |
|
2D array with Accumulated GFX Clk Below Host Limit (Thermal) per XCP/XCC |
|
2D array with Accumulated Low Utilization per XCP/XCC |
|
2D array with Accumulated GFX Clk Below Host Limit (Total) per XCP/XCC |
|
Processor hot violation % (greater than 0% is a violation) |
|
PVIOL Package Power Tracking (PPT) violation % (greater than 0% is a violation) |
|
TVIOL; Socket thermal violation % (greater than 0% is a violation) |
|
Voltage regulator violation % (greater than 0% is a violation) |
|
High Bandwidth Memory (HBM) thermal violation % (greater than 0% is a violation) |
|
Graphics clock below host limit violation % (greater than 0% is a violation). UPDATED in new driver 1.8: use new per_gfx_clk_below_host_limit_pwr, per_gfx_clk_below_host_limit_thm, per_gfx_clk_below_host_limit_total values |
|
2D array with GFX Clk Below Host Limit Violation % (Power) per XCP/XCC |
|
2D array with GFX Clk Below Host Limit Violation % (Thermal) per XCP/XCC |
|
2D array with Low Utilization Violation % per XCP/XCC |
|
2D array with GFX Clk Below Host Limit Violation % (Total) per XCP/XCC |
|
Processor hot violation; 1 = active 0 = not active |
|
Package Power Tracking (PPT) violation; 1 = active 0 = not active |
|
Socket thermal violation; 1 = active 0 = not active |
|
Voltage regulator violation; 1 = active 0 = not active |
|
High Bandwidth Memory (HBM) thermal violation; 1 = active 0 = not active |
|
Graphics Clock Below Host Limit Violation; 1 = Active 0 = Not Active. UPDATED in new driver 1.8: use new active_gfx_clk_below_host_limit_pwr, active_gfx_clk_below_host_limit_thm, active_gfx_clk_below_host_limit_total values |
|
2D array with GFX Clk Below Host Limit Violation Active (Power) per XCP/XCC |
|
2D array with GFX Clk Below Host Limit Violation Active (Thermal) per XCP/XCC |
|
2D array with Low Utilization Violation Active per XCP/XCC |
|
2D array with GFX Clk Below Host Limit Violation Active (Total) per XCP/XCC |

Exceptions that can be thrown by `amdsmi_get_violation_status`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`

`AmdSmiTimeoutException`


Example:

```
try:
violation_status = amdsmi_interface.amdsmi_get_violation_status(args.gpu)
throttle_status['accumulation_counter'] = violation_status['acc_counter']
throttle_status['prochot_accumulated'] = violation_status['acc_prochot_thrm']
throttle_status['ppt_accumulated'] = violation_status['acc_ppt_pwr']
throttle_status['socket_thermal_accumulated'] = violation_status['acc_socket_thrm']
throttle_status['vr_thermal_accumulated'] = violation_status['acc_vr_thrm']
throttle_status['hbm_thermal_accumulated'] = violation_status['acc_hbm_thrm']
throttle_status['gfx_clk_below_host_limit_accumulated'] = violation_status['acc_gfx_clk_below_host_limit']
throttle_status['gfx_clk_below_host_limit_pwr_accumulated'] = violation_status['acc_gfx_clk_below_host_limit_pwr']
throttle_status['gfx_clk_below_host_limit_thm_accumulated'] = violation_status['acc_gfx_clk_below_host_limit_thm']
throttle_status['low_utilization_accumulated'] = violation_status['acc_low_utilization']
throttle_status['gfx_clk_below_host_limit_total_accumulated'] = violation_status['acc_gfx_clk_below_host_limit_total']
throttle_status['prochot_violation_status'] = violation_status['active_prochot_thrm']
throttle_status['ppt_violation_status'] = violation_status['active_ppt_pwr']
throttle_status['socket_thermal_violation_status'] = violation_status['active_socket_thrm']
throttle_status['vr_thermal_violation_status'] = violation_status['active_vr_thrm']
throttle_status['hbm_thermal_violation_status'] = violation_status['active_hbm_thrm']
throttle_status['gfx_clk_below_host_limit_violation_status'] = violation_status['active_gfx_clk_below_host_limit']
throttle_status['gfx_clk_below_host_limit_pwr_violation_status'] = violation_status['active_gfx_clk_below_host_limit_pwr']
throttle_status['gfx_clk_below_host_limit_thm_violation_status'] = violation_status['active_gfx_clk_below_host_limit_thm']
throttle_status['low_utilization_violation_status'] = violation_status['active_low_utilization']
throttle_status['gfx_clk_below_host_limit_total_violation_status'] = violation_status['active_gfx_clk_below_host_limit_total']
throttle_status['prochot_violation_activity'] = violation_status['per_prochot_thrm']
throttle_status['ppt_violation_activity'] = violation_status['per_ppt_pwr']
throttle_status['socket_thermal_violation_activity'] = violation_status['per_socket_thrm']
throttle_status['vr_thermal_violation_activity'] = violation_status['per_vr_thrm']
throttle_status['hbm_thermal_violation_activity'] = violation_status['per_hbm_thrm']
throttle_status['gfx_clk_below_host_limit_violation_activity'] = violation_status['per_gfx_clk_below_host_limit']
throttle_status['gfx_clk_below_host_limit_pwr_violation_activity'] = violation_status['per_gfx_clk_below_host_limit_pwr']
throttle_status['gfx_clk_below_host_limit_thm_violation_activity'] = violation_status['per_gfx_clk_below_host_limit_thm']
throttle_status['low_utilization_violation_activity'] = violation_status['per_low_utilization']
throttle_status['gfx_clk_below_host_limit_total_violation_activity'] = violation_status['per_gfx_clk_below_host_limit_total']
except AmdSmiException as e:
print(e)
```

### amdsmi_get_clock_info[#](#amdsmi-get-clock-info)

Description: Returns the clock measure for the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query`clock_type`

one of`AmdSmiClkType`

enum values:

Field |
Description |
|---|---|
|
SYS clock type |
|
GFX clock type |
|
DF clock type |
|
DCEF clock type |
|
SOC clock type |
|
MEM clock type |
|
PCIE clock type |
|
VCLK0 clock type |
|
VCLK1 clock type |
|
DCLK0 clock type |
|
DCLK1 clock type |

Output: Dictionary with fields

Field |
Description |
|---|---|
|
Current clock for given clock type |
|
Minimum clock for given clock type |
|
Maximum clock for given clock type |
|
flag only supported on GFX clock domain |
|
clock deep sleep mode flag |

Exceptions that can be thrown by `amdsmi_get_clock_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
clock_measure = amdsmi_get_clock_info(device, AmdSmiClkType.GFX)
print(clock_measure['clk'])
print(clock_measure['min_clk'])
print(clock_measure['max_clk'])
print(clock_measure['clk_locked'])
print(clock_measure['clk_deep_sleep'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_pcie_info[#](#amdsmi-get-pcie-info)

Description: Returns the pcie metric and static information for the given GPU. For accurate PCIe Bandwidth measurements it is recommended to use this function once per 1000ms It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with 2 fields `pcie_static`

and `pcie_metric`


Fields |
Description |
||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|
|
||||||||||||||||||
|
|

Exceptions that can be thrown by `amdsmi_get_pcie_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
pcie_info = amdsmi_get_pcie_info(device)
print(pcie_info["pcie_static"])
print(pcie_info["pcie_metric"])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_bad_page_info[#](#amdsmi-get-gpu-bad-page-info)

Description: Returns bad page info for the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: List consisting of dictionaries with fields for each bad page found; can be an empty list

Field |
Description |
|---|---|
|
Value of page |
|
Address of bad page |
|
Size of bad page |
|
Status of bad page |

Exceptions that can be thrown by `amdsmi_get_gpu_bad_page_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
bad_page_info = amdsmi_get_gpu_bad_page_info(device)
if not bad_page_info: # Can be empty list
print("No bad pages found")
continue
for bad_page in bad_page_info:
print(bad_page["value"])
print(bad_page["page_address"])
print(bad_page["page_size"])
print(bad_page["status"])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_bad_page_threshold[#](#amdsmi-get-gpu-bad-page-threshold)

Description: Returns bad page threshold for the given GPU; Requires root level access to display bad page threshold count; otherwise will return “N/A”. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Bad page threshold value

Exceptions that can be thrown by `amdsmi_get_gpu_bad_page_threshold`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
threshold = amdsmi_get_gpu_bad_page_threshold(device)
print(bad_page["threshold"])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_memory_reserved_pages[#](#amdsmi-get-gpu-memory-reserved-pages)

Description: Returns reserved memory page info for the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: List consisting of dictionaries with fields for each reserved memory page found; can be an empty list

Field |
Description |
|---|---|
|
Value of memory reserved page |
|
Address of memory reserved page |
|
Size of memory reserved page |
|
Status of memory reserved page |

Exceptions that can be thrown by `amdsmi_get_gpu_memory_reserved_pages`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
reserved_memory_page_info = amdsmi_get_gpu_memory_reserved_pages(device)
if not reserved_memory_page_info: # Can be empty list
print("No memory reserved pages found")
continue
for reserved_memory_page in reserved_memory_page_info:
print(reserved_memory_page["value"])
print(reserved_memory_page["page_address"])
print(reserved_memory_page["page_size"])
print(reserved_memory_page["status"])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_process_list[#](#amdsmi-get-gpu-process-list)

Description: Returns the list of processes running on the target GPU; Requires root level access to display root process names; otherwise will return “N/A”

Input parameters:

`processor_handle`

device which to query

Output: List of Dictionaries with the corresponding fields; empty list if no running process are detected

Field |
Description |
||||||||
|---|---|---|---|---|---|---|---|---|---|
|
Name of process. If user does not have permission this will be “N/A” |
||||||||
|
Process ID |
||||||||
|
Total memory usage by GPU during process in Bytes (sum of the process memory is not expected to be the total memory usage.) |
||||||||
|
|
||||||||
|
|
||||||||
|
Number of Compute Units utilized |
||||||||
|
Time that queues are evicted on a GPU in milliseconds |

Exceptions that can be thrown by `amdsmi_get_gpu_process_list`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
processes = amdsmi_get_gpu_process_list(device)
if len(processes) == 0:
print("No processes running on this GPU")
else:
for process in processes:
print(process)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_total_ecc_count[#](#amdsmi-get-gpu-total-ecc-count)

Description: Returns the ECC error count for the given GPU. It is not supported on virtual machine guest

See [RAS Error Count sysfs Interface (AMDGPU RAS Support - Linux Kernel
documentation)](https://docs.kernel.org/gpu/amdgpu/ras.html#ras-error-count-sysfs-interface)
to learn how these error counts are accessed.

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Description |
|---|---|
|
Correctable ECC error count |
|
Uncorrectable ECC error count |
|
Deferred ECC error count |

Exceptions that can be thrown by `amdsmi_get_gpu_total_ecc_count`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
ecc_error_count = amdsmi_get_gpu_total_ecc_count(device)
print(ecc_error_count["correctable_count"])
print(ecc_error_count["uncorrectable_count"])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_cper_entries[#](#amdsmi-get-gpu-cper-entries)

Description: Dump CPER entries for a given GPU in a file using from CPER header file from RAS tool.

Input parameters:

`processor_handle`

device which to query`severity_mask`

the severity mask of the entries to be retrieved: 1:’nonfatal-uncorrected’, 2: ‘fatal’, 4: ‘nonfatal-corrected’, ‘corrected’, 7: ‘all’`buffer_size`

number of bytes that will be used to create a buffer for copying cper entries into; default is 1048576 bytes`cursor`

the zero based index at which to start retrieving cper entries; default value is 0; for example, if there are 10 cper entries available, then with a cursor value of 8, it will retrieve the last two cper entries only

Output: Dictionary with fields, updated cursor, and a dictionary of the cper_data, status_code

Output1: Dictionary with fields

Field |
Description |
|---|---|
|
The severity of the CPER error ex: |
|
The notification type associated with the CPER entry. |
|
The time when the CPER entry was recorded, formatted as |
|
A 4-byte signature identifying the entry, typically |
|
The revision number of the CPER record format. |
|
A marker value (typically |
|
The count of sections included in the CPER entry. |
|
The total length in bytes of the CPER entry. |
|
The product serial number. Exists in raw entries in C++ API |
|
A character array identifying the GPU or platform. |
|
A character array indicating the creator of the CPER entry. |
|
A unique identifier for the CPER entry. |
|
Reserved flags related to the CPER entry. |
|
Reserved information related to persistence. |

Output2: Updated cursor (int type)

Cursor is the index of the next cper entry in the GPU ring buffer. For example, if 10 entries were fetched successfully, the value of cursor will be 11 upon return from the API. Subsequent call to the API with cursor value of 11 should fetch the next entry


Output3: A list of dictionaries, each dictionary containing the CPER record and its size:

{“bytes”:

, “size”: }

Output4: status_code AMDSMI_STATUS_SUCCESS: If all entries were retrieved successfully AMDSMI_STATUS_MORE_DATA: If some of the entries were retrieved and: * A subsequent call to the API with the updated cursor will result in the fetching the next batch of entries, or * Increasing the input buffer_size will allow more entries to be fetched with the same cursor

Exceptions that can be thrown by `amdsmi_get_gpu_cper_entries`

function:

`AmdSmiLibraryException`

`AmdSmiParameterException`


Example:

```
try:
entries, new_cursor, cper_data, status_code = amdsmi_get_gpu_cper_entries(
device, severity_mask, buffer_size, initial_cursor)
except AmdSmiException as e:
print(e)
```

Refer to [amd_smi_cper_example.py](https://github.com/ROCm/rocm-systems/blob/develop/projects/amdsmi/example/amd_smi_cper_example.py) for a complete example.

### amdsmi_get_afids_from_cper[#](#amdsmi-get-afids-from-cper)

Description: Get the AFIDs from CPER buffer

Input parameters:

`cper_afid_data`

: raw bytes of a single CPER record.

Output: Tuple[List[int], int]: A tuple containing: - A list of extracted AFIDs. - The total count of AFIDs.

`status_code`

| Upon successful retrieval of data, status_code will be AMDSMI_STATUS_SUCCESS (0) or AMDSMI_STATUS_MORE_DATA (39) if more data can be retrieve by subsequent call to the`amdsmi_get_gpu_cper_entries`

function. In the later case, the input parameter`cursor`

should be set to the updated`cursor`

that was returned from the previous call.

Exceptions that can be thrown by `amdsmi_get_gpu_cper_entries`

function:

`AmdSmiParameterException`

`AmdSmiLibraryException`

with these possible error codes: AMDSMI_STATUS_INVAL AMDSMI_STATUS_UNEXPECTED_SIZE AMDSMI_STATUS_UNEXPECTED_DATA AMDSMI_STATUS_NOT_SUPPORTED

Example 1: Using a single CPER record as bytes

```
cper_bytes = b'\x43\x50\x45\x52...' # Replace with actual bytes
afids, num_afids = amdsmi_get_afids_from_cper(cper_bytes)
print(f"AFIDs: {afids}\nTotal count: {num_afids}")
```

Example 2: Using a list of dicts

```
cper_record = {
'bytes': [67, 80, 69, 82, ...], # Replace with actual byte values
'size': 376}
afids, num_afids = amdsmi_get_afids_from_cper([cper_record])
print(f"AFIDs: {afids}\nTotal count: {num_afids}")
```

Example 3: General Usage

```
try:
with open(cper_file.path, "rb") as file:
afids, num_afids = amdsmi_interface.amdsmi_get_afids_from_cper(file.read())
print(f"AFIDs: {afids}\nTotal count: {num_afids}")
except AmdSmiException as e:
print(e)
```

Refer to [amd_smi_afid_example.py](https://github.com/ROCm/rocm-systems/blob/develop/projects/amdsmi/example/amd_smi_afid_example.py) for a complete example.

### amdsmi_get_gpu_ras_feature_info[#](#amdsmi-get-gpu-ras-feature-info)

Description: Returns RAS version and schema information It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: List containing dictionaries with fields

Field |
Description |
|---|---|
|
eeprom version |
|
parity schema |
|
single bit schema |
|
double bit schema |
|
poison schema |

Exceptions that can be thrown by `amdsmi_get_gpu_ras_feature_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
from amdsmi import *
import os
amdsmi_init()
def amdsmi_get_afids_from_cper():
directory_path = "/tmp/cper_dump/"
print(f"Searching for cper file in {directory_path}")
with os.scandir(directory_path) as cper_files:
for cper_file in cper_files:
if cper_file.is_file():
if ".bin" in cper_file.path:
print(f"Found {cper_file.path}")
with open(cper_file.path, "rb") as file:
raw = file.read()
afids, num_afids = amdsmi_interface.amdsmi_get_afids_from_cper(raw)
print(f"afids: {afids}")
amdsmi_get_afids_from_cper()
```

Output:

```
sudo python3 afid.py
Searching for cper file in /tmp/cper_dump/
Found /tmp/cper_dump/cper_entry_0.bin
afids: [17]
Found /tmp/cper_dump/cper_entry_1.bin
afids: [17]
```

### amdsmi_get_gpu_ras_block_features_enabled[#](#amdsmi-get-gpu-ras-block-features-enabled)

Description: Returns status of each RAS block for the given GPU. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: List containing dictionaries with fields for each RAS block

Field |
Description |
|---|---|
|
RAS block |
|
RAS block status |

Exceptions that can be thrown by `amdsmi_get_gpu_ras_block_features_enabled`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
ras_block_features = amdsmi_get_gpu_ras_block_features_enabled(device)
print(ras_block_features)
except AmdSmiException as e:
print(e)
```

### AmdSmiEventReader class[#](#amdsmieventreader-class)

Description: Providing methods for event monitoring. This is context manager class.
Can be used with `with`

statement for automatic cleanup.

Methods:

#### Constructor[#](#constructor)

Description: Allocates a new event reader notifier to monitor different types of events for the given GPU

Input parameters:

`processor_handle`

device handle corresponding to the device on which to listen for events`event_types`

list of event types from AmdSmiEvtNotificationType enum. Specifying which events to collect for the given device.

Event Type |
Description |
|---|---|
|
VM page fault |
|
thermal throttle |
|
gpu pre reset; this event includes a message which indicates the cause of the reset. They are as follows: |
|
gpu post reset |
|
migrate start |
|
migrate end |
|
page fault start |
|
page fault end |
|
queue eviction |
|
queue restore |
|
unmap from GPU |
|
KFD process start |
|
KFD process end |

#### read[#](#read)

Description: Reads events on the given device. When event is caught, device handle, message and event type are returned. Reading events stops when timestamp passes without event reading.

Input parameters:

`timestamp`

number of milliseconds to wait for an event to occur. If event does not happen monitoring is finished`num_elem`

number of events. This is optional parameter. Default value is 10.

#### stop[#](#stop)

Description: Any resources used by event notification for the the given device will be freed with this function. This can be used explicitly or
automatically using `with`

statement, like in the examples below. This should be called either manually or automatically for every created AmdSmiEventReader object.

Input parameters: `None`


Example with manual cleanup of AmdSmiEventReader:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
event = AmdSmiEventReader(device[0], AmdSmiEvtNotificationType.GPU_PRE_RESET, AmdSmiEvtNotificationType.GPU_POST_RESET)
event.read(10000)
except AmdSmiException as e:
print(e)
finally:
event.stop()
```

Example with automatic cleanup using `with`

statement:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
with AmdSmiEventReader(device[0], AmdSmiEvtNotificationType.GPU_PRE_RESET, AmdSmiEvtNotificationType.GPU_POST_RESET) as event:
event.read(10000)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_pci_bandwidth[#](#amdsmi-set-gpu-pci-bandwidth)

Description: Control the set of allowed PCIe bandwidths that can be used It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`bw_bitmask`

A bitmask indicating the indices of the bandwidths that are to be enabled (1) and disabled (0)

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_pci_bandwidth`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_pci_bandwidth(device, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_power_cap[#](#amdsmi-set-power-cap)

Description: Set the power cap value. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_ind`

a 0-based sensor index. Normally, this will be 0. If a device has more than one sensor, it could be greater than 0`cap`

int that indicates the desired power cap, in microwatts

Output: None

Exceptions that can be thrown by `amdsmi_set_power_cap`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
power_cap = 250 * 1000000
amdsmi_set_power_cap(device, 0, power_cap)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_power_profile[#](#amdsmi-set-gpu-power-profile)

Description: Set the power profile. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`reserved`

Not currently used, set to 0`profile`

a amdsmi_power_profile_preset_masks_t that hold the mask of the desired new power profile

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_power_profile`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
profile = ...
amdsmi_set_gpu_power_profile(device, 0, profile)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_clk_range[#](#amdsmi-set-gpu-clk-range)

Description: This function sets the clock range information. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`min_clk_value`

minimum clock value for desired clock range`max_clk_value`

maximum clock value for desired clock range`clk_type`

AMDSMI_CLK_TYPE_SYS | AMDSMI_CLK_TYPE_MEM range type

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_clk_range`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_clk_range(device, 0, 1000, AmdSmiClkType.AMDSMI_CLK_TYPE_SYS)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_bdf_id[#](#amdsmi-get-gpu-bdf-id)

Description: Get the unique PCI device identifier associated for a device

Input parameters:

`processor_handle`

device which to query

Output: device bdf The format of bdfid will be as follows:

BDFID = ((DOMAIN & 0xffffffff) << 32) | ((BUS & 0xff) << 8) | ((DEVICE & 0x1f) <<3 ) | (FUNCTION & 0x7)

Name |
Field |
|---|---|
Domain |
[64:32] |
Reserved |
[31:16] |
Bus |
[15: 8] |
Device |
[ 7: 3] |
Function |
[ 2: 0] |

Exceptions that can be thrown by `amdsmi_get_gpu_bdf_id`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
bdfid = amdsmi_get_gpu_bdf_id(device)
print(bdfid)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_pci_bandwidth[#](#amdsmi-get-gpu-pci-bandwidth)

Description: Get the list of possible PCIe bandwidths that are available. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with the possible T/s values and associated number of lanes

Field |
Content |
|---|---|
|
transfer_rate dictionary |
|
lanes |

transfer_rate dictionary

Field |
Content |
|---|---|
|
num_supported |
|
current |
|
list of frequency |

Exceptions that can be thrown by `amdsmi_get_gpu_pci_bandwidth`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
bandwidth = amdsmi_get_gpu_pci_bandwidth(device)
print(bandwidth)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_pci_throughput[#](#amdsmi-get-gpu-pci-throughput)

Description: Get PCIe traffic information. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with the fields

Field |
Content |
|---|---|
|
number of bytes sent in 1 second |
|
the number of bytes received |
|
maximum packet size |

Exceptions that can be thrown by `amdsmi_get_gpu_pci_throughput`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
pci = amdsmi_get_gpu_pci_throughput(device)
print(pci)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_pci_replay_counter[#](#amdsmi-get-gpu-pci-replay-counter)

Description: Get PCIe replay counter

Input parameters:

`processor_handle`

device which to query

Output: counter value The sum of the NAK’s received and generated by the GPU

Exceptions that can be thrown by `amdsmi_get_gpu_pci_replay_counter`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
counter = amdsmi_get_gpu_pci_replay_counter(device)
print(counter)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_topo_numa_affinity[#](#amdsmi-get-gpu-topo-numa-affinity)

Description: Get the NUMA node associated with a device

Input parameters:

`processor_handle`

device which to query

Output: NUMA node value

Exceptions that can be thrown by `amdsmi_get_gpu_topo_numa_affinity`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
numa_node = amdsmi_get_gpu_topo_numa_affinity(device)
print(numa_node)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_energy_count[#](#amdsmi-get-energy-count)

Description: Get the energy accumulator counter information of the device. energy_accumulator * counter_resolution = total_energy_consumption in micro-Joules It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query

Output: Dictionary with fields

Field |
Content |
|---|---|
|
counter for energy accumulation since last restart/gpu rest (Deprecated in ROCm 6.4) |
|
counter for energy accumulation since last restart/gpu rest |
|
counter resolution |
|
timestamp |

Exceptions that can be thrown by `amdsmi_get_energy_count`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
energy_dict = amdsmi_get_energy_count(device)
print(energy_dict)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_memory_total[#](#amdsmi-get-gpu-memory-total)

Description: Get the total amount of memory that exists

Input parameters:

`processor_handle`

device which to query`mem_type`

enum AmdSmiMemoryType

Output: total amount of memory

Exceptions that can be thrown by `amdsmi_get_gpu_memory_total`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vram_memory_total = amdsmi_get_gpu_memory_total(device, amdsmi_interface.AmdSmiMemoryType.VRAM)
print(vram_memory_total)
vis_vram_memory_total = amdsmi_get_gpu_memory_total(device, amdsmi_interface.AmdSmiMemoryType.VIS_VRAM)
print(vis_vram_memory_total)
gtt_memory_total = amdsmi_get_gpu_memory_total(device, amdsmi_interface.AmdSmiMemoryType.GTT)
print(gtt_memory_total)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_od_clk_info[#](#amdsmi-set-gpu-od-clk-info)

Description: This function sets the clock frequency information. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`level`

AMDSMI_FREQ_IND_MIN|AMDSMI_FREQ_IND_MAX to set the minimum (0) or maximum (1) speed`clk_value`

value to apply to the clock range`clk_type`

AMDSMI_CLK_TYPE_SYS | AMDSMI_CLK_TYPE_MEM range type

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_od_clk_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_od_clk_info(
device,
AmdSmiFreqInd.AMDSMI_FREQ_IND_MAX,
1000,
AmdSmiClkType.AMDSMI_CLK_TYPE_SYS
)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_memory_usage[#](#amdsmi-get-gpu-memory-usage)

Description: Get the current memory usage

Input parameters:

`processor_handle`

device which to query`mem_type`

enum AmdSmiMemoryType

Output: the amount of memory currently being used

Exceptions that can be thrown by `amdsmi_get_gpu_memory_usage`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vram_memory_usage = amdsmi_get_gpu_memory_usage(device, amdsmi_interface.AmdSmiMemoryType.VRAM)
print(vram_memory_usage)
vis_vram_memory_usage = amdsmi_get_gpu_memory_usage(device, amdsmi_interface.AmdSmiMemoryType.VIS_VRAM)
print(vis_vram_memory_usage)
gtt_memory_usage = amdsmi_get_gpu_memory_usage(device, amdsmi_interface.AmdSmiMemoryType.GTT)
print(gtt_memory_usage)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_od_volt_info[#](#amdsmi-set-gpu-od-volt-info)

Description: This function sets 1 of the 3 voltage curve points. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`vpoint`

voltage point [0|1|2] on the voltage curve`clk_value`

clock value component of voltage curve point`volt_value`

voltage value component of voltage curve point

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_od_volt_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_od_volt_info(device, 1, 1000, 980)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_fan_rpms[#](#amdsmi-get-gpu-fan-rpms)

Description: Get the fan speed in RPMs of the device with the specified device handle and 0-based sensor index. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_idx`

a 0-based sensor index. Normally, this will be 0. If a device has more than one sensor, it could be greater than 0.

Output: Fan speed in rpms as integer

Exceptions that can be thrown by `amdsmi_get_gpu_fan_rpms`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
fan_rpm = amdsmi_get_gpu_fan_rpms(device, 0)
print(fan_rpm)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_fan_speed[#](#amdsmi-get-gpu-fan-speed)

Description: Get the fan speed for the specified device as a value relative to AMDSMI_MAX_FAN_SPEED. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_idx`

a 0-based sensor index. Normally, this will be 0. If a device has more than one sensor, it could be greater than 0.

Output: Fan speed in relative to MAX

Exceptions that can be thrown by `amdsmi_get_gpu_fan_speed`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
fan_speed = amdsmi_get_gpu_fan_speed(device, 0)
print(fan_speed)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_fan_speed_max[#](#amdsmi-get-gpu-fan-speed-max)

Description: Get the max fan speed of the device with provided device handle. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_idx`

a 0-based sensor index. Normally, this will be 0. If a device has more than one sensor, it could be greater than 0.

Output: Max fan speed as integer

Exceptions that can be thrown by `amdsmi_get_gpu_fan_speed_max`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
max_fan_speed = amdsmi_get_gpu_fan_speed_max(device, 0)
print(max_fan_speed)
except AmdSmiException as e:
print(e)
```

### amdsmi_is_gpu_power_management_enabled[#](#amdsmi-is-gpu-power-management-enabled)

Description: Returns is power management enabled

Input parameters:

`processor_handle`

GPU device which to query

Output: Bool true if power management enabled else false

Exceptions that can be thrown by `amdsmi_is_gpu_power_management_enabled`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for processor in devices:
is_power_management_enabled = amdsmi_is_gpu_power_management_enabled(processor)
print(is_power_management_enabled)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_temp_metric[#](#amdsmi-get-temp-metric)

Description: Get the temperature metric value for the specified metric, from the specified temperature sensor on the specified device. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_type`

part of device from which temperature should be obtained`metric`

enum indicated which temperature value should be retrieved

Output: Temperature as integer in millidegrees Celcius

Exceptions that can be thrown by `amdsmi_get_temp_metric`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
temp_metric = amdsmi_get_temp_metric(device, AmdSmiTemperatureType.EDGE,
AmdSmiTemperatureMetric.CURRENT)
print(temp_metric)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_volt_metric[#](#amdsmi-get-gpu-volt-metric)

Description: Get the voltage metric value for the specified metric, from the specified voltage sensor on the specified device. It is not supported on virtual machine guest

Input parameters:

Parameters |
Description |
||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|
Handle for the given device |
||||||||||||||||||
|
|
||||||||||||||||||
|
|

Output: Voltage as integer in millivolts

Exceptions that can be thrown by `amdsmi_get_gpu_volt_metric`

function:

`AmdSmiLibraryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
voltage = amdsmi_get_gpu_volt_metric(
device,
AmdSmiVoltageType.VDDBOARD,
AmdSmiVoltageMetric.AVERAGE
)
print(voltage)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_utilization_count[#](#amdsmi-get-utilization-count)

Description: Get coarse/fine grain utilization counter of the specified device

Input parameters:

`processor_handle`

handle for the given device`counter_types`

List of AmdSmiUtilizationCounterType counters requested

Output: List containing dictionaries with fields

Field |
Description |
||||||
|---|---|---|---|---|---|---|---|
|
The timestamp when the counter is retreived - Resolution: 1 ns |
||||||
|
|

Exceptions that can be thrown by `amdsmi_get_utilization_count`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
utilization = amdsmi_get_utilization_count(
device,
AmdSmiUtilizationCounterType.COARSE_GRAIN_GFX_ACTIVITY
)
print(utilization)
utilization = amdsmi_get_utilization_count(
device,
[AmdSmiUtilizationCounterType.COARSE_GRAIN_GFX_ACTIVITY,
AmdSmiUtilizationCounterType.COARSE_GRAIN_MEM_ACTIVITY,
AmdSmiUtilizationCounterType.COARSE_DECODER_ACTIVITY,
AmdSmiUtilizationCounterType.FINE_GRAIN_GFX_ACTIVITY,
AmdSmiUtilizationCounterType.FINE_GRAIN_MEM_ACTIVITY,
AmdSmiUtilizationCounterType.FINE_DECODER_ACTIVITY]
)
print(utilization)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_perf_level[#](#amdsmi-get-gpu-perf-level)

Description: Get the performance level of the device with provided device handle. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: Performance level as enum value of dev_perf_level_t

Exceptions that can be thrown by `amdsmi_get_gpu_perf_level`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
perf_level = amdsmi_get_gpu_perf_level(dev)
print(perf_level)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_perf_determinism_mode[#](#amdsmi-set-gpu-perf-determinism-mode)

Description: Enter performance determinism mode with provided device handle. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`clkvalue`

softmax value for GFXCLK in MHz

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_perf_determinism_mode`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_perf_determinism_mode(device, 1333)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_process_isolation[#](#amdsmi-get-gpu-process-isolation)

Description: Get the status of the Process Isolation

Input parameters:

`processor_handle`

handle for the given device

Output: integer corresponding to isolation_status; 0 - disabled, 1 - enabled

Exceptions that can be thrown by `amdsmi_get_gpu_process_isolation`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
isolate = amdsmi_get_gpu_process_isolation(device)
print("Process Isolation Status: ", isolate)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_process_isolation[#](#amdsmi-set-gpu-process-isolation)

Description: Enable/disable the system Process Isolation for the given device handle.

Input parameters:

`processor_handle`

handle for the given device`pisolate`

the process isolation status to set. 0 is the process isolation disabled, and 1 is the process isolation enabled.

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_process_isolation`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_process_isolation(device, 1)
except AmdSmiException as e:
print(e)
```

### amdsmi_clean_gpu_local_data[#](#amdsmi-clean-gpu-local-data)

Description: Clear the SRAM data of the given device. This can be called between user logins to prevent information leak.

Input parameters:

`processor_handle`

handle for the given device

Output: None

Exceptions that can be thrown by `amdsmi_clean_gpu_local_data`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_clean_gpu_local_data(device)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_overdrive_level[#](#amdsmi-get-gpu-overdrive-level)

Description: Get the overdrive percent associated with the device with provided device handle. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: Overdrive percentage as integer

Exceptions that can be thrown by `amdsmi_get_gpu_overdrive_level`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
od_level = amdsmi_get_gpu_overdrive_level(dev)
print(od_level)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_mem_overdrive_level[#](#amdsmi-get-gpu-mem-overdrive-level)

Description: Get the GPU memory clock overdrive percent associated with the device with provided device handle. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: Overdrive percentage as integer

Exceptions that can be thrown by `amdsmi_get_gpu_mem_overdrive_level`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
od_level = amdsmi_get_gpu_mem_overdrive_level(dev)
print(od_level)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_clk_freq[#](#amdsmi-get-clk-freq)

Description: Get the list of possible system clock speeds of device for a specified clock type. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`clk_type`

the type of clock for which the frequency is desired

Output: Dictionary with fields

Field |
Description |
|---|---|
|
The number of supported frequencies |
|
The current frequency index |
|
List of frequencies, only the first num_supported frequencies are valid |

Exceptions that can be thrown by `amdsmi_get_clk_freq`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_get_clk_freq(device, AmdSmiClkType.SYS)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_od_volt_info[#](#amdsmi-get-gpu-od-volt-info)

Description: This function retrieves the voltage/frequency curve information. If the num_regions is 0 then the voltage curve is not supported. It is not supported on virtual machine guest.

Input parameters:

`processor_handle`

handle for the given device

Output: Dictionary with fields

Field |
Description |
||||||
|---|---|---|---|---|---|---|---|
|
|
||||||
|
|
||||||
|
|
||||||
|
|
||||||
|
List of voltage curve points |
||||||
|
The number of voltage curve regions |

Exceptions that can be thrown by `amdsmi_get_gpu_od_volt_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_get_gpu_od_volt_info(dev)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_metrics_info[#](#amdsmi-get-gpu-metrics-info)

Description: This function retrieves the gpu metrics information. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: Dictionary with fields

Field |
Description |
Unit |
|---|---|---|
|
Edge temperature value |
Celsius © |
|
Hotspot (aka junction) temperature value |
Celsius © |
|
Memory temperature value |
Celsius © |
|
vrgfx temperature value |
Celsius © |
|
vrsoc temperature value |
Celsius © |
|
vrmem temperature value |
Celsius © |
|
Average gfx activity |
% |
|
Average umc (Universal Memory Controller) activity |
% |
|
Average mm (multimedia) engine activity |
% |
|
Average socket power |
W |
|
Energy accumulated with a 15.3 uJ resolution over 1ns |
uJ |
|
System clock counter |
ns |
|
Average gfx clock frequency |
MHz |
|
Average soc clock frequency |
MHz |
|
Average uclk frequency |
MHz |
|
Average vclk0 frequency |
MHz |
|
Average dclk0 frequency |
MHz |
|
Average vclk1 frequency |
MHz |
|
Average dclk1 frequency |
MHz |
|
Current gfx clock |
MHz |
|
Current soc clock |
MHz |
|
Current uclk |
MHz |
|
Current vclk0 |
MHz |
|
Current dclk0 |
MHz |
|
Current vclk1 |
MHz |
|
Current dclk1 |
MHz |
|
Current throttle status |
bool |
|
Current fan speed |
RPM |
|
PCIe link width (number of lanes) |
lanes |
|
PCIe link speed in 0.1 GT/s (Giga Transfers per second) |
GT/s |
|
padding |
|
|
gfx activity accumulated |
% |
|
Memory activity accumulated |
% |
|
list of hbm temperatures |
Celsius © |
|
timestamp from PMFW (10ns resolution) |
ns |
|
soc voltage |
mV |
|
gfx voltage |
mV |
|
mem voltage |
mV |
|
ASIC independent throttle status (see drivers/gpu/drm/amd/pm/swsmu/inc/amdgpu_smu.h for bit flags) |
|
|
Current socket power (also known as instant socket power) |
W |
|
List of VCN encode/decode engine utilization per AID |
% |
|
Clock lock status. Bits 0:7 correspond to each gfx clock engine instance. Bits 0:5 for APU/AID devices |
|
|
XGMI bus width |
lanes |
|
XGMI bitrate |
GB/s |
|
PCIe accumulated bandwidth |
GB/s |
|
PCIe instantaneous bandwidth |
GB/s |
|
PCIe L0 to recovery state transition accumulated count |
|
|
PCIe replay accumulated count |
|
|
PCIe replay rollover accumulated count |
|
|
XGMI accumulated read data transfer size (KiloBytes) |
KB |
|
XGMI accumulated write data transfer size (KiloBytes) |
KB |
|
List of current gfx clock frequencies |
MHz |
|
List of current soc clock frequencies |
MHz |
|
List of current v0 clock frequencies |
MHz |
|
List of current d0 clock frequencies |
MHz |
|
PCIe NAC sent count accumulated |
|
|
PCIe NAC received count accumulated |
|
|
List of JPEG engine activity |
% |

Exceptions that can be thrown by `amdsmi_get_gpu_metrics_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_get_gpu_metrics_info(dev)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_pm_metrics_info[#](#amdsmi-get-gpu-pm-metrics-info)

Description: This function will retreive the name and value for each item in the pm metrics table with the given processor handle.

Input parameters:

`processor_handle`

handle for the given device

Output: List containing dictionaries of pm metrics and their values

Field |
Description |
|---|---|
|
name of PM metric |
|
value of pm metric |

Exceptions that can be thrown by `amdsmi_get_gpu_pm_metrics_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
print(amdsmi_get_gpu_pm_metrics_info(device))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_reg_table_info[#](#amdsmi-get-gpu-reg-table-info)

Description: This function will retrieve register metrics table with provided device index and register type.

Input parameters:

`processor_handle`

handle for the given device`reg_type`

register type

Output: List containing dictionaries of register metrics and their values

Field |
Description |
|---|---|
|
name of register metric |
|
value of register metric |

Exceptions that can be thrown by `amdsmi_get_gpu_reg_table_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
print(amdsmi_get_gpu_reg_table_info(device, AmdSmiRegType.PCIE))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_od_volt_curve_regions[#](#amdsmi-get-gpu-od-volt-curve-regions)

Description: This function will retrieve the current valid regions in the frequency/voltage space. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`num_regions`

number of freq volt regions

Output: List containing a dictionary with fields for each freq volt region

Field |
Description |
||||||
|---|---|---|---|---|---|---|---|
|
|
||||||
|
|

Exceptions that can be thrown by `amdsmi_get_gpu_od_volt_curve_regions`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_get_gpu_od_volt_curve_regions(device, 3)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_power_profile_presets[#](#amdsmi-get-gpu-power-profile-presets)

Description: Get the list of available preset power profiles and an indication of which profile is currently active. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_idx`

number of freq volt regions

Output: Dictionary with fields

Field |
Description |
|---|---|
|
Which profiles are supported by this system |
|
Which power profile is currently active |
|
How many power profiles are available |

Exceptions that can be thrown by `amdsmi_get_gpu_power_profile_presets`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_get_gpu_power_profile_presets(device, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_gpu_counter_group_supported[#](#amdsmi-gpu-counter-group-supported)

Description: Tell if an event group is supported by a given device. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

device which to query`event_group`

event group being checked for support

Output: None

Exceptions that can be thrown by `amdsmi_gpu_counter_group_supported`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_gpu_counter_group_supported(device, AmdSmiEventGroup.XGMI)
except AmdSmiException as e:
print(e)
```

### amdsmi_gpu_create_counter[#](#amdsmi-gpu-create-counter)

Description: Creates a performance counter object

Input parameters:

`processor_handle`

device which to query`event_type`

event group being checked for support

Output: An event handle of the newly created performance counter object

Exceptions that can be thrown by `amdsmi_gpu_create_counter`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
event_handle = amdsmi_gpu_create_counter(device, AmdSmiEventGroup.XGMI)
except AmdSmiException as e:
print(e)
```

### amdsmi_gpu_destroy_counter[#](#amdsmi-gpu-destroy-counter)

Description: Destroys a performance counter object

Input parameters:

`event_handle`

event handle of the performance counter object

Output: None

Exceptions that can be thrown by `amdsmi_gpu_destroy_counter`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
event_handle = amdsmi_gpu_create_counter(device, AmdSmiEventGroup.XGMI)
amdsmi_gpu_destroy_counter(event_handle)
except AmdSmiException as e:
print(e)
```

### amdsmi_gpu_control_counter[#](#amdsmi-gpu-control-counter)

Description: Issue performance counter control commands. It is not supported on virtual machine guest

Input parameters:

`event_handle`

event handle of the performance counter object`counter_command`

command being passed to counter as AmdSmiCounterCommand

Output: None

Exceptions that can be thrown by `amdsmi_gpu_control_counter`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
event_handle = amdsmi_gpu_create_counter(device, AmdSmiEventType.XGMI_1_REQUEST_TX)
amdsmi_gpu_control_counter(event_handle, AmdSmiCounterCommand.CMD_START)
except AmdSmiException as e:
print(e)
```

### amdsmi_gpu_read_counter[#](#amdsmi-gpu-read-counter)

Description: Read the current value of a performance counter

Input parameters:

`event_handle`

event handle of the performance counter object

Output: Dictionary with fields

Field |
Description |
|---|---|
|
Counter value |
|
Time that the counter was enabled in nanoseconds |
|
Time that the counter was running in nanoseconds |

Exceptions that can be thrown by `amdsmi_gpu_read_counter`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
event_handle = amdsmi_gpu_create_counter(device, AmdSmiEventType.XGMI_1_REQUEST_TX)
amdsmi_gpu_read_counter(event_handle)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_available_counters[#](#amdsmi-get-gpu-available-counters)

Description: Get the number of currently available counters. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`event_group`

event group being checked as AmdSmiEventGroup

Output: Number of available counters for the given device of the inputted event group

Exceptions that can be thrown by `amdsmi_get_gpu_available_counters`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
available_counters = amdsmi_get_gpu_available_counters(device, AmdSmiEventGroup.XGMI)
print(available_counters)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_perf_level[#](#amdsmi-set-gpu-perf-level)

Description: Set a desired performance level for given device. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`perf_level`

performance level being set as AmdSmiDevPerfLevel

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_perf_level`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_perf_level(device, AmdSmiDevPerfLevel.STABLE_PEAK)
except AmdSmiException as e:
print(e)
```

### amdsmi_reset_gpu[#](#amdsmi-reset-gpu)

Description: Reset the gpu associated with the device with provided device handle It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: None

Exceptions that can be thrown by `amdsmi_reset_gpu`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_reset_gpu(device)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_fan_speed[#](#amdsmi-set-gpu-fan-speed)

Description: Set the fan speed for the specified device with the provided speed, in RPMs. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_idx`

sensor index as integer`fan_speed`

the speed to which the function will attempt to set the fan

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_fan_speed`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_fan_speed(device, 0, 1333)
except AmdSmiException as e:
print(e)
```

### amdsmi_reset_gpu_fan[#](#amdsmi-reset-gpu-fan)

Description: Reset the fan to automatic driver control. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`sensor_idx`

sensor index as integer

Output: None

Exceptions that can be thrown by `amdsmi_reset_gpu_fan`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_reset_gpu_fan(device, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_clk_freq[#](#amdsmi-set-clk-freq)

Description: Control the set of allowed frequencies that can be used for the specified clock. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`clk_type`

the type of clock for which the set of frequencies will be modified as AmdSmiClkType`freq_bitmask`

bitmask indicating the indices of the frequencies that are to be enabled (1) and disabled (0). Only the lowest ::amdsmi_frequencies_t.num_supported bits of this mask are relevant.

Output: None

Exceptions that can be thrown by `amdsmi_set_clk_freq`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
freq_bitmask = 0
amdsmi_set_clk_freq(device, AmdSmiClkType.GFX, freq_bitmask)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_soc_pstate[#](#amdsmi-get-soc-pstate)

Description: Get dpm policy information.

Input parameters:

`processor_handle`

handle for the given device`policy_id`

the policy id to set.

Output: Dictionary with fields

Field |
Description |
|---|---|
|
total number of supported policies |
|
current policy id |
|
list of dictionaries containing possible policies |

Exceptions that can be thrown by `amdsmi_get_soc_pstate`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
dpm_policies = amdsmi_get_soc_pstate(device)
print(dpm_policies)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_soc_pstate[#](#amdsmi-set-soc-pstate)

Description: Set the dpm policy to corresponding policy_id. Typically following: 0(default),1,2,3

Input parameters:

`processor_handle`

handle for the given device`policy_id`

the policy id to set.

Output: None

Exceptions that can be thrown by `amdsmi_set_soc_pstate`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_soc_pstate(device, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_xgmi_plpd[#](#amdsmi-set-xgmi-plpd)

Description: Set the xgmi per-link power down policy parameter for the processor

Input parameters:

`processor_handle`

handle for the given device`policy_id`

the xgmi plpd id to set.

Output: None

Exceptions that can be thrown by `amdsmi_set_xgmi_plpd`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_xgmi_plpd(device, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_xgmi_plpd[#](#amdsmi-get-xgmi-plpd)

Description: Get the xgmi per-link power down policy parameter for the processor

Input parameters:

`processor_handle`

handle for the given device

Output: Dict containing information about xgmi per-link power down policy

Field |
Description |
|---|---|
|
The number of supported policies |
|
The current policy index |
|
List of policies. ( |

Exceptions that can be thrown by `amdsmi_get_xgmi_plpd`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
xgmi_plpd = amdsmi_get_xgmi_plpd(device)
print(xgmi_plpd)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_overdrive_level[#](#amdsmi-set-gpu-overdrive-level)

Description: **deprecated** Set the overdrive percent associated with the
device with provided device handle with the provided value. It is not
supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device`overdrive_value`

value to which the overdrive level should be set

Output: None

Exceptions that can be thrown by `amdsmi_set_gpu_overdrive_level`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_overdrive_level(device, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_ecc_count[#](#amdsmi-get-gpu-ecc-count)

Description: Retrieve the error counts for a GPU block. It is not supported on virtual machine guest

See [RAS Error Count sysfs Interface (AMDGPU RAS Support - Linux Kernel
documentation)](https://docs.kernel.org/gpu/amdgpu/ras.html#ras-error-count-sysfs-interface)
to learn how these error counts are accessed.

Input parameters:

`processor_handle`

handle for the given device`block`

The block for which error counts should be retrieved

Output: Dict containing information about error counts

Field |
Description |
|---|---|
|
Count of correctable errors |
|
Count of uncorrectable errors |
|
Count of deferred errors |

Exceptions that can be thrown by `amdsmi_get_gpu_ecc_count`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
ecc_count = amdsmi_get_gpu_ecc_count(device, AmdSmiGpuBlock.UMC)
print(ecc_count)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_ecc_enabled[#](#amdsmi-get-gpu-ecc-enabled)

Description: Retrieve the enabled ECC bit-mask. It is not supported on virtual machine guest

See [RAS Error Count sysfs Interface (AMDGPU RAS Support - Linux Kernel
documentation)](https://docs.kernel.org/gpu/amdgpu/ras.html#ras-error-count-sysfs-interface)
to learn how these error counts are accessed.

Input parameters:

`processor_handle`

handle for the given device

Output: Enabled ECC bit-mask

Exceptions that can be thrown by `amdsmi_get_gpu_ecc_enabled`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
enabled = amdsmi_get_gpu_ecc_enabled(device)
print(enabled)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_ecc_status[#](#amdsmi-get-gpu-ecc-status)

Description: Retrieve the ECC status for a GPU block. It is not supported on virtual machine guest

See [RAS Error Count sysfs Interface (AMDGPU RAS Support - Linux Kernel
documentation)](https://docs.kernel.org/gpu/amdgpu/ras.html#ras-error-count-sysfs-interface)
to learn how these error counts are accessed.

Input parameters:

`processor_handle`

handle for the given device`block`

The block for which ECC status should be retrieved

Output: ECC status for a requested GPU block

Exceptions that can be thrown by `amdsmi_get_gpu_ecc_status`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
status = amdsmi_get_gpu_ecc_status(device, AmdSmiGpuBlock.UMC)
print(status)
except AmdSmiException as e:
print(e)
```

### amdsmi_status_code_to_string[#](#amdsmi-status-code-to-string)

Description: Get a description of a provided AMDSMI error status

Input parameters:

`status`

The error status for which a description is desired

Output: String description of the provided error code

Exceptions that can be thrown by `amdsmi_status_code_to_string`

function:

`AmdSmiParameterException`


Example:

```
try:
status_str = amdsmi_status_code_to_string(ctypes.c_uint32(0))
print(status_str)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_compute_process_info[#](#amdsmi-get-gpu-compute-process-info)

Description: Get process information about processes currently using GPU

Input parameters: None

Output: List of python dicts each containing a process information

Field |
Description |
|---|---|
|
Process ID |
|
PASID (Not working in ROCm 6.4+, Deprecated in 7.0) |
|
VRAM usage |
|
SDMA usage in microseconds |
|
Compute Unit usage in percents |
|
Time that queues are evicted on a GPU in milliseconds |

note: Sum of the process memory is not expected to be the total memory usage.

Exceptions that can be thrown by `amdsmi_get_gpu_compute_process_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`


Example:

```
try:
procs = amdsmi_get_gpu_compute_process_info()
for proc in procs:
print(proc)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_compute_process_info_by_pid[#](#amdsmi-get-gpu-compute-process-info-by-pid)

Description: Get process information about processes currently using GPU

Input parameters:

`pid`

The process ID for which process information is being requested

Output: Dict containing a process information

Field |
Description |
|---|---|
|
Process ID |
|
PASID (Not working in ROCm 6.4+, deprecating in 7.0) |
|
VRAM usage |
|
SDMA usage in microseconds |
|
Compute Unit usage in percents |
|
Time that queues are evicted on a GPU in milliseconds |

Exceptions that can be thrown by `amdsmi_get_gpu_compute_process_info_by_pid`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
pid = 0 # << valid pid here
proc = amdsmi_get_gpu_compute_process_info_by_pid(pid)
print(proc)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_compute_process_gpus[#](#amdsmi-get-gpu-compute-process-gpus)

Description: Get the device indices currently being used by a process

Input parameters:

`pid`

The process id of the process for which the number of gpus currently being used is requested

Output: List of indices of devices currently being used by the process

Exceptions that can be thrown by `amdsmi_get_gpu_compute_process_gpus`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
pid = 0 # << valid pid here
indices = amdsmi_get_gpu_compute_process_gpus(pid)
print(indices)
except AmdSmiException as e:
print(e)
```

### amdsmi_gpu_xgmi_error_status[#](#amdsmi-gpu-xgmi-error-status)

Description: Retrieve the XGMI error status for a device. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: XGMI error status for a requested device

Exceptions that can be thrown by `amdsmi_gpu_xgmi_error_status`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
status = amdsmi_gpu_xgmi_error_status(device)
print(status)
except AmdSmiException as e:
print(e)
```

### amdsmi_reset_gpu_xgmi_error[#](#amdsmi-reset-gpu-xgmi-error)

Description: Reset the XGMI error status for a device. It is not supported on virtual machine guest

Input parameters:

`processor_handle`

handle for the given device

Output: None

Exceptions that can be thrown by `amdsmi_reset_gpu_xgmi_error`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_reset_gpu_xgmi_error(device)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_vendor_name[#](#amdsmi-get-gpu-vendor-name)

Description: Returns the device vendor name

Input parameters:

`processor_handle`

device which to query

Output: device vendor name

Exceptions that can be thrown by `amdsmi_get_gpu_vendor_name`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vendor_name = amdsmi_get_gpu_vendor_name(device)
print(vendor_name)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_id[#](#amdsmi-get-gpu-id)

Description: Get the device id associated with the device with provided device handler

Input parameters:

`processor_handle`

device which to query

Output: device id

Exceptions that can be thrown by `amdsmi_get_gpu_id`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
dev_id = amdsmi_get_gpu_id(device)
print(dev_id)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_vram_vendor[#](#amdsmi-get-gpu-vram-vendor)

Description: Get the vram vendor string of a gpu device.

Input parameters:

`processor_handle`

device which to query

Output: vram vendor

Exceptions that can be thrown by `amdsmi_get_gpu_vram_vendor`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
vram_vendor = amdsmi_get_gpu_vram_vendor(device)
print(vram_vendor)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_subsystem_id[#](#amdsmi-get-gpu-subsystem-id)

Description: Get the subsystem device id associated with the device with provided device handle.

Input parameters:

`processor_handle`

device which to query

Output: subsystem device id

Exceptions that can be thrown by `amdsmi_get_gpu_subsystem_id`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
id = amdsmi_get_gpu_subsystem_id(device)
print(id)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_subsystem_name[#](#amdsmi-get-gpu-subsystem-name)

Description: Get the name string for the device subsytem

Input parameters:

`processor_handle`

device which to query

Output: device subsytem

Exceptions that can be thrown by `amdsmi_get_gpu_subsystem_name`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
subsystem_nam = amdsmi_get_gpu_subsystem_name(device)
print(subsystem_nam)
except AmdSmiException as e:
print(e)
```

### amdsmi_topo_get_numa_node_number[#](#amdsmi-topo-get-numa-node-number)

Description: Retrieve the NUMA CPU node number for a device

Input parameters:

`processor_handle`

device which to query

Output: node number of NUMA CPU for the device

Exceptions that can be thrown by `amdsmi_topo_get_numa_node_number`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
node_number = amdsmi_topo_get_numa_node_number()
print(node_number)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_minmax_bandwidth_between_processors[#](#amdsmi-get-minmax-bandwidth-between-processors)

Description: Retreive minimal and maximal io link bandwidth between 2 GPUs.

Input parameters:

`processor_handle_src`

the source device handle`processor_handle_dest`

the destination device handle

Output: Dictionary with fields:

Field |
Description |
|---|---|
|
minimal bandwidth for the connection |
|
maximal bandwidth for the connection |

Exceptions that can be thrown by `amdsmi_get_minmax_bandwidth_between_processors`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
processor_handle_src = devices[0]
processor_handle_dest = devices[1]
bandwidth = amdsmi_get_minmax_bandwidth_between_processors(processor_handle_src, processor_handle_dest)
print(bandwidth['min_bandwidth'])
print(bandwidth['max_bandwidth'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_P2P_status[#](#amdsmi-get-p2p-status)

Description: Retrieve the connection type and P2P capabilities between 2 GPUs

Input parameters:

`processor_handle_src`

the source device handle`processor_handle_dest`

the destination device handle

Output: Dictionary with fields:

Fields |
Description |
||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|
The connection type as an int. This should be translated according to the enum amdsmi_link_type_t. Refer to the example below for more details. |
||||||||||||
|
|

Exceptions that can be thrown by `amdsmi_get_P2P_status`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
processor_handle_src = devices[0]
processor_handle_dest = devices[1]
link_type = amdsmi_get_P2P_status(processor_handle_src, processor_handle_dest)
if link_type['type'] == AmdSmiLinkType.AMDSMI_LINK_TYPE_INTERNAL:
print('internal')
if link_type['type'] == AmdSmiLinkType.AMDSMI_LINK_TYPE_PCIE:
print('pcie')
if link_type['type'] == AmdSmiLinkType.AMDSMI_LINK_TYPE_XGMI:
print('xgmi')
if link_type['type'] == AmdSmiLinkType.AMDSMI_LINK_TYPE_NOT_APPLICABLE:
print('not applicable')
if link_type['type'] == AmdSmiLinkType.AMDSMI_LINK_TYPE_UNKNOWN:
print('unknown')
print(link_type['caps'])
except AmdSmiException as e:
print(e)
```

### amdsmi_is_P2P_accessible[#](#amdsmi-is-p2p-accessible)

Description: Return P2P availability status between 2 GPUs

Input parameters:

`processor_handle_src`

the source device handle`processor_handle_dest`

the destination device handle

Output: P2P availability status between 2 GPUs

Exceptions that can be thrown by `amdsmi_is_P2P_accessible`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
processor_handle_src = devices[0]
processor_handle_dest = devices[1]
accessible = amdsmi_is_P2P_accessible(processor_handle_src, processor_handle_dest)
print(accessible)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_compute_partition[#](#amdsmi-get-gpu-compute-partition)

Description: Get the compute partition from the given GPU

Input parameters:

`processor_handle`

the device handle

Output: String of the partition type

Exceptions that can be thrown by `amdsmi_get_gpu_compute_partition`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
compute_partition_type = amdsmi_get_gpu_compute_partition(device)
print(compute_partition_type)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_compute_partition[#](#amdsmi-set-gpu-compute-partition)

Description: Set the compute partition to the given GPU. This function does not allow any concurrent operations. Device must be idle and have no workloads when performing set partition operations.

Input parameters:

`processor_handle`

the device handle`compute_partition`

the type of compute_partition to set

Output: String of the partition type

Exceptions that can be thrown by `amdsmi_set_gpu_compute_partition`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
compute_partition = AmdSmiComputePartitionType.SPX
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_compute_partition(device, compute_partition)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_memory_partition[#](#amdsmi-get-gpu-memory-partition)

Description: Get the memory partition from the given GPU

Input parameters:

`processor_handle`

the device handle

Output: String of the partition type

Exceptions that can be thrown by `amdsmi_get_gpu_memory_partition`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
memory_partition_type = amdsmi_get_gpu_memory_partition(device)
print(memory_partition_type)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_gpu_memory_partition[#](#amdsmi-set-gpu-memory-partition)

Description: Set the memory partition to the given GPU. This function does not allow any concurrent operations. Devices must be idle and have no workloads when performing set partition operations.

Input parameters:

`processor_handle`

the device handle`memory_partition`

the type of memory_partition to set

Output: String of the partition type

Exceptions that can be thrown by `amdsmi_set_gpu_memory_partition`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
memory_partition = AmdSmiMemoryPartitionType.NPS1
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
amdsmi_set_gpu_memory_partition(device, memory_partition)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_accelerator_partition_profile[#](#amdsmi-get-gpu-accelerator-partition-profile)

**Note: CURRENTLY HARDCODED TO RETURN EMPTY VALUES**

Description: Get partition information for target device

Input parameters:

`processor_handle`

the device handle

Output: Dictionary with fields:

Field |
Description |
|---|---|
|
ID of the partition on the GPU provided |
|
Dict containing partition data (TBD) |

Exceptions that can be thrown by `amdsmi_get_gpu_accelerator_partition_profile`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
partition_id = amdsmi_get_gpu_accelerator_partition_profile(device)["partition_id"]
print(partition_id)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_xgmi_info[#](#amdsmi-get-xgmi-info)

Description: Returns XGMI information for the GPU.

Input parameters:

`processor_handle`

device handle

Output: Dictionary with fields:

Field |
Description |
|---|---|
|
xgmi lanes |
|
xgmi hive id |
|
xgmi node id |
|
index |

Exceptions that can be thrown by `amdsmi_get_xgmi_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
xgmi_info = amdsmi_get_xgmi_info(device)
print(xgmi_info['xgmi_lanes'])
print(xgmi_info['xgmi_hive_id'])
print(xgmi_info['xgmi_node_id'])
print(xgmi_info['index'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_gpu_virtualization_mode[#](#amdsmi-get-gpu-virtualization-mode)

Description: Retrieve the virtualization mode for the selected GPU.

Input parameters:

`processor_handle`

The identifier of the given device.

Output: Dictionary holding the following fields.

`mode`

AmdSmiVirtualizationMode; an IntEnum denoting the possible virtualization modes Field | Description —|—`UNKNOWN`

| Virtualization mode not detected`BAREMETAL`

| Baremetal paltform detected`HOST`

| Host/Hypervisor platform detected`GUEST`

| Guest/Virtual Machine detected`PASSTHROUGH`

| GPU Passthrough mode detected

Exceptions that can be thrown by `amdsmi_get_gpu_virtualization_mode`

function:

`AmdSmiLibraryException`


Example:

```
try:
device_handles = amdsmi_interface.amdsmi_get_processor_handles()
for dev in device_handles:
virtualization_info = amdsmi_interface.amdsmi_get_gpu_virtualization_mode(dev)
print(virtualization_info['mode'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_affinity_with_scope[#](#amdsmi-get-cpu-affinity-with-scope)

Description: Returns list of bitmask information for the given GPU.

Input parameters:

`processor_handle`

device which to query

Output: List with fields

Field |
Description |
|---|---|
|
array size = (num of sockets * num of cores)/ size of 64-bit |
|
enum value for numa or socket affinity |

Exceptions that can be thrown by `amdsmi_get_gpu_vram_info`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
devices = amdsmi_get_processor_handles()
if len(devices) == 0:
print("No GPUs on machine")
else:
for device in devices:
bitmask = amdsmi_get_cpu_affinity_with_scope(device)
print(bitmask['size'])
except AmdSmiException as e:
print(e)
```

## CPU APIs[#](#cpu-apis)

### amdsmi_get_processor_info[#](#amdsmi-get-processor-info)

**Note: CURRENTLY HARDCODED TO RETURN EMPTY VALUES**

Description: Return processor name

Input parameters:
`processor_handle`

processor handle

Output: Processor name

Exceptions that can be thrown by `amdsmi_get_processor_info`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_processor_handles()
if len(processor_handles) == 0:
print("No processors on machine")
else:
for processor in processor_handles:
print(amdsmi_get_processor_info(processor))
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_hsmp_proto_ver[#](#amdsmi-get-cpu-hsmp-proto-ver)

Description: Get the hsmp protocol version.

Output: amdsmi hsmp protocol version

Exceptions that can be thrown by `amdsmi_get_cpu_hsmp_proto_ver`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
version = amdsmi_get_cpu_hsmp_proto_ver(processor)
print(version)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_threads_per_core[#](#amdsmi-get-threads-per-core)

Description: Get number of threads per core.

Output: cpu family

Exceptions that can be thrown by `amdsmi_get_cpu_family`

function:

`AmdSmiLibraryException`


Example:

```
try:
threads_per_core = amdsmi_get_threads_per_core()
print(threads_per_core)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_hsmp_driver_version[#](#amdsmi-get-cpu-hsmp-driver-version)

Description: Get the HSMP Driver version.

Output: amdsmi HSMP Driver version

Exceptions that can be thrown by `amdsmi_get_cpu_hsmp_driver_version`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
version = amdsmi_get_cpu_hsmp_driver_version(processor)
print(version['major'])
print(version['minor'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_smu_fw_version[#](#amdsmi-get-cpu-smu-fw-version)

Description: Get the SMU Firmware version.

Output: amdsmi SMU Firmware version

Exceptions that can be thrown by `amdsmi_get_cpu_smu_fw_version`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
version = amdsmi_get_cpu_smu_fw_version(processor)
print(version['debug'])
print(version['minor'])
print(version['major'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_prochot_status[#](#amdsmi-get-cpu-prochot-status)

Description: Get the CPU’s prochot status.

Output: amdsmi cpu prochot status

Exceptions that can be thrown by `amdsmi_get_cpu_prochot_status`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
prochot = amdsmi_get_cpu_prochot_status(processor)
print(prochot)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_fclk_mclk[#](#amdsmi-get-cpu-fclk-mclk)

Description: Get the Data fabric clock and Memory clock in MHz.

Output: amdsmi data fabric clock and memory clock

Exceptions that can be thrown by `amdsmi_get_cpu_fclk_mclk`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
clk = amdsmi_get_cpu_fclk_mclk(processor)
for fclk, mclk in clk.items():
print(fclk)
print(mclk)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_cclk_limit[#](#amdsmi-get-cpu-cclk-limit)

Description: Get the core clock in MHz.

Output: amdsmi core clock

Exceptions that can be thrown by `amdsmi_get_cpu_cclk_limit`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
cclk_limit = amdsmi_get_cpu_cclk_limit(processor)
print(cclk_limit)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_current_active_freq_limit[#](#amdsmi-get-cpu-socket-current-active-freq-limit)

Description: Get current active frequency limit of the socket.

Output: amdsmi frequency value in MHz and frequency source name

Exceptions that can be thrown by `amdsmi_get_cpu_socket_current_active_freq_limit`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
freq_limit = amdsmi_get_cpu_socket_current_active_freq_limit(processor)
for freq, src in freq_limit.items():
print(freq)
print(src)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_freq_range[#](#amdsmi-get-cpu-socket-freq-range)

Description: Get socket frequency range

Output: amdsmi maximum frequency and minimum frequency

Exceptions that can be thrown by `amdsmi_get_cpu_socket_freq_range`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
freq_range = amdsmi_get_cpu_socket_freq_range(processor)
for fmax, fmin in freq_range.items():
print(fmax)
print(fmin)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_core_current_freq_limit[#](#amdsmi-get-cpu-core-current-freq-limit)

Description: Get socket frequency limit of the core

Output: amdsmi frequency

Exceptions that can be thrown by `amdsmi_get_cpu_core_current_freq_limit`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpucore_handles()
if len(processor_handles) == 0:
print("No CPU cores on machine")
else:
for processor in processor_handles:
freq_limit = amdsmi_get_cpu_core_current_freq_limit(processor)
print(freq_limit)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_power[#](#amdsmi-get-cpu-socket-power)

Description: Get the socket power.

Output: amdsmi socket power

Exceptions that can be thrown by `amdsmi_get_cpu_socket_power`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
sock_power = amdsmi_get_cpu_socket_power(processor)
print(sock_power)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_power_cap[#](#amdsmi-get-cpu-socket-power-cap)

Description: Get the socket power cap.

Output: amdsmi socket power cap

Exceptions that can be thrown by `amdsmi_get_cpu_socket_power_cap`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
sock_power = amdsmi_get_cpu_socket_power_cap(processor)
print(sock_power)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_power_cap_max[#](#amdsmi-get-cpu-socket-power-cap-max)

Description: Get the socket power cap max.

Output: amdsmi socket power cap max

Exceptions that can be thrown by `amdsmi_get_cpu_socket_power_cap_max`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
sock_power = amdsmi_get_cpu_socket_power_cap_max(processor)
print(sock_power)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_pwr_svi_telemetry_all_rails[#](#amdsmi-get-cpu-pwr-svi-telemetry-all-rails)

Description: Get the SVI based power telemetry for all rails.

Output: amdsmi svi based power value

Exceptions that can be thrown by `amdsmi_get_cpu_pwr_svi_telemetry_all_rails`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
power = amdsmi_get_cpu_pwr_svi_telemetry_all_rails(processor)
print(power)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_socket_power_cap[#](#amdsmi-set-cpu-socket-power-cap)

Description: Set the power cap value for a given socket.

Input: amdsmi socket power cap value

Exceptions that can be thrown by `amdsmi_set_cpu_socket_power_cap`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
power = amdsmi_set_cpu_socket_power_cap(processor, 1000)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_pwr_efficiency_mode[#](#amdsmi-set-cpu-pwr-efficiency-mode)

Description: Set the power efficiency profile policy.

Input: mode(0, 1, or 2)

Exceptions that can be thrown by `amdsmi_set_cpu_pwr_efficiency_mode`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
policy = amdsmi_set_cpu_pwr_efficiency_mode(processor, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_core_boostlimit[#](#amdsmi-get-cpu-core-boostlimit)

Description: Get boost limit of the cpu core

Output: amdsmi frequency

Exceptions that can be thrown by `amdsmi_get_cpu_core_boostlimit`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpucore_handles()
if len(processor_handles) == 0:
print("No CPU cores on machine")
else:
for processor in processor_handles:
boost_limit = amdsmi_get_cpu_core_boostlimit(processor)
print(boost_limit)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_c0_residency[#](#amdsmi-get-cpu-socket-c0-residency)

Description: Get the cpu socket C0 residency.

Output: amdsmi C0 residency value

Exceptions that can be thrown by `amdsmi_get_cpu_socket_c0_residency`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
c0_residency = amdsmi_get_cpu_socket_c0_residency(processor)
print(c0_residency)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_core_boostlimit[#](#amdsmi-set-cpu-core-boostlimit)

Description: Set the cpu core boost limit.

Output: amdsmi boostlimit value

Exceptions that can be thrown by `amdsmi_set_cpu_core_boostlimit`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpucore_handles()
if len(processor_handles) == 0:
print("No CPU cores on machine")
else:
for processor in processor_handles:
boost_limit = amdsmi_set_cpu_core_boostlimit(processor, 1000)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_socket_boostlimit[#](#amdsmi-set-cpu-socket-boostlimit)

Description: Set the cpu socket boost limit.

Input: amdsmi boostlimit value

Exceptions that can be thrown by `amdsmi_set_cpu_socket_boostlimit`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
boost_limit = amdsmi_set_cpu_socket_boostlimit(processor, 1000)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_ddr_bw[#](#amdsmi-get-cpu-ddr-bw)

Description: Get the CPU DDR Bandwidth.

Output: amdsmi ddr bandwidth data

Exceptions that can be thrown by `amdsmi_get_cpu_ddr_bw`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
ddr_bw = amdsmi_get_cpu_ddr_bw(processor)
print(ddr_bw['max_bw'])
print(ddr_bw['utilized_bw'])
print(ddr_bw['utilized_pct'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_temperature[#](#amdsmi-get-cpu-socket-temperature)

Description: Get the socket temperature.

Output: amdsmi temperature value

Exceptions that can be thrown by `amdsmi_get_cpu_socket_temperature`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
ptmon = amdsmi_get_cpu_socket_temperature(processor)
print(ptmon)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_dimm_temp_range_and_refresh_rate[#](#amdsmi-get-cpu-dimm-temp-range-and-refresh-rate)

Description: Get DIMM temperature range and refresh rate.

Output: amdsmi dimm metric data

Exceptions that can be thrown by `amdsmi_get_cpu_dimm_temp_range_and_refresh_rate`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
dimm = amdsmi_get_cpu_dimm_temp_range_and_refresh_rate(processor)
print(dimm['range'])
print(dimm['ref_rate'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_dimm_power_consumption[#](#amdsmi-get-cpu-dimm-power-consumption)

Description: amdsmi_get_cpu_dimm_power_consumption.

Output: amdsmi dimm power consumption value

Exceptions that can be thrown by `amdsmi_get_cpu_dimm_power_consumption`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
dimm = amdsmi_get_cpu_dimm_power_consumption(processor)
print(dimm['power'])
print(dimm['update_rate'])
print(dimm['dimm_addr'])
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_dimm_thermal_sensor[#](#amdsmi-get-cpu-dimm-thermal-sensor)

Description: Get DIMM thermal sensor value.

Output: amdsmi dimm temperature data

Exceptions that can be thrown by `amdsmi_get_cpu_dimm_thermal_sensor`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
dimm = amdsmi_get_cpu_dimm_thermal_sensor(processor)
print(dimm['sensor'])
print(dimm['update_rate'])
print(dimm['dimm_addr'])
print(dimm['temp'])
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_xgmi_width[#](#amdsmi-set-cpu-xgmi-width)

Description: Set xgmi width.

Input: amdsmi xgmi width

Exceptions that can be thrown by `amdsmi_set_cpu_xgmi_width`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
xgmi_width = amdsmi_set_cpu_xgmi_width(processor, 0, 100)
except AmdSmiException as e:
print(e)
```

### amdsmi_cpu_apb_enable[#](#amdsmi-cpu-apb-enable)

Description: Enable APB.

Input: amdsmi processor handle

Exceptions that can be thrown by `amdsmi_cpu_apb_enable`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
apb_enable = amdsmi_cpu_apb_enable(processor)
except AmdSmiException as e:
print(e)
```

### amdsmi_cpu_apb_disable[#](#amdsmi-cpu-apb-disable)

Description: Disable APB.

Input: pstate value

Exceptions that can be thrown by `amdsmi_cpu_apb_disable`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
apb_disable = amdsmi_cpu_apb_disable(processor, 0)
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_socket_lclk_dpm_level[#](#amdsmi-set-cpu-socket-lclk-dpm-level)

Description: Set NBIO lclk dpm level value.

Input: nbio id, min value, max value

Exceptions that can be thrown by `amdsmi_set_cpu_socket_lclk_dpm_level`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for socket in socket_handles:
nbio = amdsmi_set_cpu_socket_lclk_dpm_level(socket, 0, 0, 2)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_socket_lclk_dpm_level[#](#amdsmi-get-cpu-socket-lclk-dpm-level)

Description: Get NBIO LCLK dpm level.

Output: nbio id

Exceptions that can be thrown by `amdsmi_get_cpu_socket_lclk_dpm_level`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
nbio = amdsmi_get_cpu_socket_lclk_dpm_level(processor)
print(nbio['max_dpm_level'])
print(nbio['max_dpm_level'])
except AmdSmiException as e:
print(e)
```

### amdsmi_set_cpu_df_pstate_range[#](#amdsmi-set-cpu-df-pstate-range)

Description: Set df pstate range.

Input: max pstate, min pstate

Exceptions that can be thrown by `amdsmi_set_cpu_df_pstate_range`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
pstate_range = amdsmi_set_cpu_df_pstate_range(processor, 0, 2)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_current_io_bandwidth[#](#amdsmi-get-cpu-current-io-bandwidth)

Description: Get current input output bandwidth.

Output: link id and bw type to which io bandwidth to be obtained

Exceptions that can be thrown by `amdsmi_get_cpu_current_io_bandwidth`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
io_bw = amdsmi_get_cpu_current_io_bandwidth(processor)
print(io_bw)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_current_xgmi_bw[#](#amdsmi-get-cpu-current-xgmi-bw)

Description: Get current xgmi bandwidth.

Output: amdsmi link id and bw type to which xgmi bandwidth to be obtained

Exceptions that can be thrown by `amdsmi_get_cpu_current_xgmi_bw`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
xgmi_bw = amdsmi_get_cpu_current_xgmi_bw(processor)
print(xgmi_bw)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_hsmp_metrics_table_version[#](#amdsmi-get-hsmp-metrics-table-version)

Description: Get HSMP metrics table version.

Output: amdsmi HSMP metrics table version

Exceptions that can be thrown by `amdsmi_get_hsmp_metrics_table_version`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
met_ver = amdsmi_get_hsmp_metrics_table_version(processor)
print(met_ver)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_hsmp_metrics_table[#](#amdsmi-get-hsmp-metrics-table)

Description: Get HSMP metrics table

Output: HSMP metric table data

Exceptions that can be thrown by `amdsmi_get_hsmp_metrics_table`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
mtbl = amdsmi_get_hsmp_metrics_table(processor)
print(mtbl['accumulation_counter'])
print(mtbl['max_socket_temperature'])
print(mtbl['max_vr_temperature'])
print(mtbl['max_hbm_temperature'])
print(mtbl['socket_power_limit'])
print(mtbl['max_socket_power_limit'])
print(mtbl['socket_power'])
except AmdSmiException as e:
print(e)
```

### amdsmi_first_online_core_on_cpu_socket[#](#amdsmi-first-online-core-on-cpu-socket)

Description: Get first online core on cpu socket.

Output: first online core on cpu socket

Exceptions that can be thrown by `amdsmi_first_online_core_on_cpu_socket`

function:

`AmdSmiLibraryException`


Example:

```
try:
processor_handles = amdsmi_get_cpusocket_handles()
if len(processor_handles) == 0:
print("No CPU sockets on machine")
else:
for processor in processor_handles:
pcore_ind = amdsmi_first_online_core_on_cpu_socket(processor)
print(pcore_ind)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_family[#](#amdsmi-get-cpu-family)

Description: Get cpu family.

Output: cpu family

Exceptions that can be thrown by `amdsmi_get_cpu_family`

function:

`AmdSmiLibraryException`


Example:

```
try:
cpu_family = amdsmi_get_cpu_family()
print(cpu_family)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_model[#](#amdsmi-get-cpu-model)

Description: Get cpu model.

Output: cpu model

Exceptions that can be thrown by `amdsmi_get_cpu_model`

function:

`AmdSmiLibraryException`


Example:

```
try:
cpu_model = amdsmi_get_cpu_model()
print(cpu_model)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_cpu_model_name[#](#amdsmi-get-cpu-model-name)

Description: Get cpu model name.

Output: cpu model name

Exceptions that can be thrown by `amdsmi_get_cpu_model_name`

function:

`AmdSmiLibraryException`


Example:

```
try:
cpu_model_name = amdsmi_get_cpu_model_name()
print(cpu_model_name)
except AmdSmiException as e:
print(e)
```

## No amdsmi_init APIs[#](#no-amdsmi-init-apis)

### amdsmi_get_lib_version[#](#amdsmi-get-lib-version)

Description: Get the build version information for the currently running build of AMDSMI. This function doesn’t require amdsmi library init.

Output: amdsmi build version

Exceptions that can be thrown by `amdsmi_get_lib_version`

function:

`AmdSmiLibraryException`

`AmdSmiRetryException`

`AmdSmiParameterException`


Example:

```
try:
version = amdsmi_get_lib_version()
print(version)
except AmdSmiException as e:
print(e)
```

### amdsmi_get_rocm_version[#](#amdsmi-get-rocm-version)

Description: This function attempts to retrieve the ROCm version by loading the `librocm-core.so`

shared library. This function doesn’t require amdsmi library init.

Output: Tuple (bool, str) containing rocm_load_status and version_message

Exceptions that can be thrown by `amdsmi_get_rocm_version`

function:

`AmdSmiLibraryException`


Example:

```
try:
import amdsmi
rocm_load_status, version_message = amdsmi_get_rocm_version()
print(f"ROCm load status: {rocm_load_status}")
print(f"ROCm version msg: {version_message}")
except AmdSmiException as e:
print(e)
```
