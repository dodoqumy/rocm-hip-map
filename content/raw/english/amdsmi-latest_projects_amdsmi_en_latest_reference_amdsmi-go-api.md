---
title: "AMD SMI Go API reference &#8212; AMD SMI 26.2.2 documentation"
source_url: "https://rocm.docs.amd.com/projects/amdsmi/en/latest/reference/amdsmi-go-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-03T06:25:13.240606+00:00
content_hash: "a33e4a4ca5009dab"
---

# AMD SMI Go API reference[#](#amd-smi-go-api-reference)

The AMD SMI Go interface provides a convenient way to interact with AMD
hardware through a simple and accessible API. The API is compatible with Go
version 1.20 and higher and requires the AMD driver to be loaded for
initialization. Review the [prerequisites](../how-to/amdsmi-go-lib.html#go-prereqs) before getting
started.

This section provides documentation for the AMD SMI Go API. Explore these sections to understand the full scope of available functionalities and how to implement them in your applications.

## GPU functions[#](#gpu-functions)

### GO_gpu_init[#](#go-gpu-init)

```
func GO_gpu_init() bool
```

`GO_gpu_init`

initializes the GPU and reports whether the initialization was successful. This function must be called before using other AMD SMI functions.

Output: `bool`

, returns true on success or false on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
GPU initialization is successful...
}
```

### GO_gpu_shutdown[#](#go-gpu-shutdown)

```
func GO_gpu_shutdown() bool
```

`GO_gpu_shutdown`

shuts down the GPU and reports whether the shutdown was successful.

Output: `bool`

, returns true on success or false on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_shutdown() {
GPU shutdown is successful...
}
```

### GO_gpu_num_monitor_devices[#](#go-gpu-num-monitor-devices)

```
func GO_gpu_num_monitor_devices() uint
```

`GO_gpu_num_monitor_devices`

returns the number of GPU monitor devices available.

Output: `uint`

, returns the number of GPU monitor devices on success or 0 on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_shutdown() {
GPU shutdown is successful...
}
```

### GO_gpu_dev_name_get[#](#go-gpu-dev-name-get)

```
func GO_gpu_dev_name_get(i int) *C.char
```

`GO_gpu_dev_name_get`

returns the name of the GPU device at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `char*`

, returns GPU device name on success or “NA” on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
goamdsmi.GO_gpu_dev_name_get(i)
}
}
```

### GO_gpu_dev_id_get[#](#go-gpu-dev-id-get)

```
func GO_gpu_dev_id_get(i int) C.uint16_t
```

`GO_gpu_dev_id_get`

returns the device ID of the GPU device at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint16`

, returns GPU device ID on success or `0xFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
value16 := goamdsmi.GO_gpu_dev_id_get(i)
}
}
```

### GO_gpu_dev_pci_id_get[#](#go-gpu-dev-pci-id-get)

```
func GO_gpu_dev_pci_id_get(i int) C.uint64_t
```

`GO_gpu_dev_pci_id_get`

returns the device PCI ID of the device at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU devices PCI ID on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
dev_pci_id := int(goamdsmi.GO_gpu_dev_pci_id_get())
}
```

### GO_gpu_dev_vbios_version_get[#](#go-gpu-dev-vbios-version-get)

```
func GO_gpu_dev_vbios_version_get(i int) *C.char
```

`GO_gpu_dev_vbios_version_get`

returns the VBIOS version of the GPU device at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `char*`

, returns VBIOS version on success or “NA” on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
dev_pci_id := int(goamdsmi.GO_gpu_dev_pci_id_get())
}
```

### GO_gpu_dev_vendor_name_get[#](#go-gpu-dev-vendor-name-get)

```
func GO_gpu_dev_vendor_name_get(i int) *C.char
```

`GO_gpu_dev_vendor_name_get`

returns the vendor name of the GPU device at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `char*`

, returns the GPU device name on success or “NA” on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
goamdsmi.GO_gpu_dev_vendor_name_get()
}
}
```

### GO_gpu_dev_power_cap_get[#](#go-gpu-dev-power-cap-get)

```
func GO_gpu_dev_power_cap_get(i int) C.uint64_t
```

`GO_gpu_dev_power_cap_get`

returns the power cap of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU power cap on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_power_cap := int(goamdsmi.GO_gpu_dev_power_cap_get(i))
}
}
```

### GO_gpu_dev_power_get[#](#go-gpu-dev-power-get)

```
func GO_gpu_dev_power_get(i int) C.uint64_t
```

`GO_gpu_dev_power_get`

returns the power of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU power on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_power := int(goamdsmi.GO_gpu_dev_power_get(i))
}
}
```

### GO_gpu_dev_temp_metric_get[#](#go-gpu-dev-temp-metric-get)

```
func GO_gpu_dev_temp_metric_get(i int, sensor int, metric int) C.uint64_t
```

`GO_gpu_dev_temp_metric_get`

returns the temperature of the GPU at the specified GPU index, sensor, and metric number.

- Input parameters:
int, GPU index.

int, sensor number.

int, metric number.



Output: `uint64`

, returns GPU temperature on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
temp := int(goamdsmi.GO_gpu_dev_temp_metric_get(i, 1, 0))
}
}
```

### GO_gpu_dev_perf_level_get[#](#go-gpu-dev-perf-level-get)

```
func GO_gpu_dev_perf_level_get(i int) C.uint32_t
```

`GO_gpu_dev_perf_level_get`

returns the perf level of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint32`

, returns GPU perf level on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_perf_level := int(goamdsmi.GO_gpu_dev_perf_level_get(i))
}
}
```

### GO_gpu_dev_overdrive_level_get[#](#go-gpu-dev-overdrive-level-get)

```
func GO_gpu_dev_overdrive_level_get(i int) C.uint32_t
```

`GO_gpu_dev_overdrive_level_get`

returns the overdrive level of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint32`

, returns GPU perf level on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_overdrive_level := int(goamdsmi.GO_gpu_dev_overdrive_level_get(i))
}
}
```

### GO_gpu_dev_mem_overdrive_level_get[#](#go-gpu-dev-mem-overdrive-level-get)

```
func GO_gpu_dev_mem_overdrive_level_get(i int) C.uint32_t
```

`GO_gpu_dev_mem_overdrive_level_get`

returns the mem overdrive level of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint32`

, returns GPU perf level on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
mem_overdrive_level := int(goamdsmi.GO_gpu_dev_mem_overdrive_level_get(i))
}
}
```

### GO_gpu_dev_gpu_clk_freq_get_sclk[#](#go-gpu-dev-gpu-clk-freq-get-sclk)

```
func GO_gpu_dev_gpu_clk_freq_get_sclk(i int) C.uint64_t
```

`GO_gpu_dev_gpu_clk_freq_get_sclk`

returns the system clock (SCLK) frequency of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU SCLK frequency level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_sclk_freq := int(goamdsmi.GO_gpu_dev_gpu_clk_freq_get_sclk(i))
}
}
```

### GO_gpu_dev_gpu_clk_freq_get_mclk[#](#go-gpu-dev-gpu-clk-freq-get-mclk)

```
func GO_gpu_dev_gpu_clk_freq_get_mclk(i int) C.uint64_t
```

`GO_gpu_dev_gpu_clk_freq_get_mclk`

returns the memory clock (MCLK) frequency of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU MCLK frequency level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_sclk_freq := int(goamdsmi.GO_gpu_dev_gpu_clk_freq_get_mclk(i))
}
}
```

### GO_gpu_od_volt_freq_range_min_get_sclk[#](#go-gpu-od-volt-freq-range-min-get-sclk)

```
func GO_gpu_od_volt_freq_range_min_get_sclk(i int) C.uint64_t
```

`GO_gpu_od_volt_freq_range_min_get_sclk`

returns the minimum system clock (SCLK) frequency of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU minimum SCLK frequency level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_min_sclk := int(goamdsmi.GO_gpu_od_volt_freq_range_min_get_sclk(i))
}
}
```

### GO_gpu_od_volt_freq_range_min_get_mclk[#](#go-gpu-od-volt-freq-range-min-get-mclk)

```
func GO_gpu_od_volt_freq_range_min_get_mclk(i int) C.uint64_t
```

`GO_gpu_od_volt_freq_range_min_get_mclk`

returns the minimum memory clock (MCLK) frequency of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU minimum MCLK frequency level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_min_mclk := int(goamdsmi.GO_gpu_od_volt_freq_range_min_get_mclk(i))
}
}
```

### GO_gpu_od_volt_freq_range_max_get_sclk[#](#go-gpu-od-volt-freq-range-max-get-sclk)

```
func GO_gpu_od_volt_freq_range_max_get_sclk(i int) C.uint64_t
```

`GO_gpu_od_volt_freq_range_max_get_sclk`

returns the maximum system clock (SCLK) frequency of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU maximum SCLK frequency level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_max_sclk := int(goamdsmi.GO_gpu_od_volt_freq_range_max_get_sclk(i))
}
}
```

### GO_gpu_od_volt_freq_range_max_get_mclk[#](#go-gpu-od-volt-freq-range-max-get-mclk)

```
func GO_gpu_od_volt_freq_range_max_get_mclk(i int) C.uint64_t
```

`GO_gpu_od_volt_freq_range_max_get_mclk`

returns the maximum memory clock (MCLK) frequency of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU maximum MCLK frequency level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_max_mclk := int(goamdsmi.GO_gpu_od_volt_freq_range_max_get_mclk(i))
}
}
```

### GO_gpu_dev_gpu_busy_percent_get[#](#go-gpu-dev-gpu-busy-percent-get)

```
func GO_gpu_dev_gpu_busy_percent_get(i int) C.uint32_t
```

`GO_gpu_dev_gpu_busy_percent_get`

returns the busy percentage of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint32`

, returns GPU busy percentage on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
dev_busy_perc := int(goamdsmi.GO_gpu_dev_gpu_busy_percent_get(i))
}
}
```

### GO_gpu_dev_gpu_memory_busy_percent_get[#](#go-gpu-dev-gpu-memory-busy-percent-get)

```
func GO_gpu_dev_gpu_memory_busy_percent_get(i int) C.uint64_t
```

`GO_gpu_dev_gpu_memory_busy_percent_get`

returns the memory busy percentage of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU memory busy percentage on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
mem_busy_perc := int(goamdsmi.GO_gpu_dev_gpu_memory_busy_percent_get(i))
}
}
```

### GO_gpu_dev_gpu_memory_usage_get[#](#go-gpu-dev-gpu-memory-usage-get)

```
func GO_gpu_dev_gpu_memory_usage_get(i int) C.uint64_t
```

`GO_gpu_dev_gpu_memory_usage_get`

returns the memory usage of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU memory usage on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
mem_usage := int(goamdsmi.GO_gpu_dev_gpu_memory_usage_get(i))
}
}
```

### GO_gpu_dev_gpu_memory_total_get[#](#go-gpu-dev-gpu-memory-total-get)

```
func GO_gpu_dev_gpu_memory_total_get(i int) C.uint64_t
```

`GO_gpu_dev_gpu_memory_total_get`

returns the total memory of the GPU at the specified GPU index.

Input parameter: `int`

, GPU index.

Output: `uint64`

, returns GPU memory usage on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
num_gpus := int(goamdsmi.GO_gpu_num_monitor_devices())
for i := 0; i < num_gpus; i++ {
mem_total := int(goamdsmi.GO_gpu_dev_gpu_memory_total_get(i))
}
}
```

### GO_gpu_uma_carveout_info_get[#](#go-gpu-uma-carveout-info-get)

```
func GO_gpu_uma_carveout_info_get(device_index int, current_index *uint32, num_options *uint32, options *[16][256]byte) int32
```

`GO_gpu_uma_carveout_info_get`

retrieves the UMA carveout configuration information for the specified GPU device. Note: This is a kernel UAPI feature (sysfs), not libdrm.

- Input parameters:
`device_index int`

: GPU device index`current_index *uint32`

: pointer to store current carveout option index`num_options *uint32`

: pointer to store number of available options`options *[16][256]byte`

: pointer to array for option descriptions (16 == AMDSMI_MAX_CARVEOUT_OPTIONS, 256 == AMDSMI_MAX_STRING_LENGTH from amdsmi.h)


Output: `int32`

, returns `0`

on success or `-1`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
var currentIdx, numOpts uint32
var opts [16][256]byte
ret := goamdsmi.GO_gpu_uma_carveout_info_get(0, ¤tIdx, &numOpts, &opts)
if ret == 0 {
// Process UMA carveout info...
}
}
```

### GO_gpu_uma_carveout_set[#](#go-gpu-uma-carveout-set)

```
func GO_gpu_uma_carveout_set(device_index int, option_index uint32) int32
```

`GO_gpu_uma_carveout_set`

sets the UMA carveout size for the specified GPU device by option index. Requires system reboot to take effect. Note: This is a kernel UAPI feature (sysfs), not libdrm.

- Input parameters:
`device_index int`

: GPU device index`option_index uint32`

: carveout option index to set


Output: `int32`

, returns `0`

on success or `-1`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_gpu_init() {
ret := goamdsmi.GO_gpu_uma_carveout_set(0, 3)
if ret == 0 {
// UMA carveout set successfully, reboot required
}
}
```

## CPU functions[#](#cpu-functions)

### GO_cpu_init[#](#go-cpu-init)

```
func GO_cpu_init() bool
```

`GO_cpu_init`

initializes the CPU and reports whether the initialization was successful.

Output: `bool`

, returns true on success or false on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
CPU initialization is successful...
}
```

### GO_cpu_number_of_sockets_get[#](#go-cpu-number-of-sockets-get)

```
func GO_cpu_number_of_sockets_get() uint
```

`GO_cpu_number_of_sockets_get`

returns the number of available CPU sockets.

Output: `uint`

, returns the number of CPU sockets on success or 0 on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_sockets := int(goamdsmi.GO_cpu_number_of_sockets_get())
}
```

### GO_cpu_number_of_threads_get[#](#go-cpu-number-of-threads-get)

```
func GO_cpu_number_of_threads_get() uint
```

`GO_cpu_number_of_threads_get`

returns the number of available CPU sockets.

Output: `uint`

, returns the number of CPU threads on success or 0 on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_threads := int(goamdsmi.GO_cpu_number_of_threads_get())
}
```

### GO_cpu_threads_per_core_get[#](#go-cpu-threads-per-core-get)

```
func GO_cpu_threads_per_core_get() uint
```

`GO_cpu_threads_per_core_get`

returns the thread count per available CPU core.

Output: `uint`

, returns the CPU thread count on success or 0 on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_threads_per_core := int(goamdsmi.GO_cpu_threads_per_core_get())
}
```

### GO_cpu_core_energy_get[#](#go-cpu-core-energy-get)

```
func GO_cpu_core_energy_get(i int) C.uint64_t
```

`GO_cpu_core_energy_get`

returns the CPU core energy for the specified thread index.

Input parameter: `int`

, thread index.

Output: `uint64`

, returns CPU core energy on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_threads := int(goamdsmi.GO_cpu_number_of_threads_get())
for i := 0; i < num_threads; i++ {
core_energy := int(goamdsmi.GO_cpu_core_energy_get(i))
}
}
```

### GO_cpu_core_boostlimit_get[#](#go-cpu-core-boostlimit-get)

```
func GO_cpu_core_boostlimit_get(i int) C.uint32_t
```

`GO_cpu_core_boostlimit_get`

returns the CPU core boost limit for the specified thread index.

Input parameter: `int`

, thread index.

Output: `uint32`

, returns CPU core boost limit on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_threads := int(goamdsmi.GO_cpu_number_of_threads_get())
for i := 0; i < num_threads; i++ {
core_boost_limit := int(goamdsmi.GO_cpu_core_boostlimit_get(i))
}
}
```

### GO_cpu_socket_energy_get[#](#go-cpu-socket-energy-get)

```
func GO_cpu_socket_energy_get(i int) C.uint64_t
```

`GO_cpu_socket_energy_get`

returns the CPU socket energy for the specified socket index.

Input parameter: `int`

, socket index.

Output: `uint64`

, returns socket energy level on success or `0xFFFFFFFFFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_sockets := int(goamdsmi.GO_cpu_number_of_sockets_get())
for i := 0; i < num_sockets; i++ {
socket_energy := int(goamdsmi.GO_cpu_socket_energy_get(i))
}
}
```

### GO_cpu_socket_power_get[#](#go-cpu-socket-power-get)

```
func GO_cpu_socket_power_get(i int) C.uint32_t
```

`GO_cpu_socket_power_get`

returns the socket power for the specified socket index.

Input parameter: `int`

, socket index.

Output: `uint32`

, returns socket energy level on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_sockets := int(goamdsmi.GO_cpu_number_of_sockets_get())
for i := 0; i < num_sockets; i++ {
socket_power := int(goamdsmi.GO_cpu_socket_power_get(i))
}
}
```

### GO_cpu_socket_power_cap_get[#](#go-cpu-socket-power-cap-get)

```
func GO_cpu_socket_power_cap_get(i int) C.uint32_t
```

`GO_cpu_socket_power_cap_get`

returns the socket power cap for the specified socket index.

Input parameter: `int`

, socket index.

Output: `uint32`

, returns socket power cap on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_sockets := int(goamdsmi.GO_cpu_number_of_sockets_get())
for i := 0; i < num_sockets; i++ {
socket_power_cap := int(goamdsmi.GO_cpu_socket_power_cap_get(i))
}
}
```

### GO_cpu_prochot_status_get[#](#go-cpu-prochot-status-get)

```
func GO_cpu_prochot_status_get(i int) C.uint32_t
```

`GO_cpu_socket_power_cap_get`

returns the PROCHOT status for the specified socket index.

Input parameter: `int`

, socket index.

Output: `uint32`

, returns PROCHOT status on success or `0xFFFFFFFF`

on fail.

Example:

```
import "github.com/ROCm/rocm-systems/projects/amdsmi"
if true == goamdsmi.GO_cpu_init() {
num_sockets := int(goamdsmi.GO_cpu_number_of_sockets_get())
for i := 0; i < num_sockets; i++ {
prochot_status := int(goamdsmi.GO_cpu_prochot_status_get(i))
}
}
```
