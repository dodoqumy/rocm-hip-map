---
title: "ROCgdb Quick Start Guide"
source_url: "https://rocm.docs.amd.com/projects/ROCgdb/en/latest/how-to/quick-start.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:03:33.133097+00:00
content_hash: "58760c185662350b"
---

# ROCgdb quick start[#](#rocgdb-quick-start)

After [installing ROCgdb](../install/installation.html#rocgdb-installation), follow the [setup](#rocgdb-setup) to start debugging your application.

## Source compilation[#](#source-compilation)

Before debugging, compile your software with debug information.

To compile your source with debug symbols, use:

```
hipcc -ggdb -O0 saxpy.cpp -o saxpy
```

Or, compile using amd-llvm:

```
-ggdb -O0 -x hip --offload-arch=native saxpy.cpp -o saxpy
```

Adding the `-g`

flag to your compilation command generates debug information even when optimizations
are turned on. Note that higher optimization levels make debugging more difficult,
so it might be helpful to turn off these optimizations with the `-O0`

compiler option.

For saxpy source code, see [main.hip](https://github.com/ROCm/rocm-examples/blob/amd-staging/HIP-Basic/saxpy/main.hip).

## Debugging using ROCgdb[#](#debugging-using-rocgdb)

You can either launch and run your application under debugger control or attach the debugger to a running process and continue execution.

To start debugging your application under debugger control, follow these steps:

Launch your application under debugger control:

rocgdb ./saxpy […]

At this point, the application is not running, but you’ll have access to the debugger console. On the console, you can use any

[gdb option](../quick-reference/essential-commands.html#rocgdb-essential-commands)for host debugging along with ROCgdb-specific features for device debugging.Set a breakpoint before running the application with debugger.

`my_app.cpp:458`

This places a temporary breakpoint at the specified line. To start your application, use:

(gdb) run

If the breakpoint is in the device code, the debugger shows the device and host threads. The device threads are not individual work items; instead, they represent a wavefront on the device. You can switch between the device wavefronts as you can between the host threads.


To attach the debugger to a running process and continue execution, use:

```
rocgdb -pid <process_id>
[…]
(gdb) continue
```

Use `ps`

command to get the <process_id> of the running application, to which the debugger needs to be attached.

You can also switch between layouts, which allows you to use different layouts for different situations while debugging.

```
src
layout asm
```

The `src`

layout is the source code view, while the `asm`

is the assembly view. For more layouts, see [TUI-specific commands](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/ROCgdb/gdb/doc/gdb/TUI-Commands.html).

After starting or attaching your application with the debugger, you can utilize these [ROCgdb commands for key operations](../quick-reference/essential-commands.html#rocgdb-essential-commands) to perform further operations.

## ROCgdb user guide[#](#rocgdb-user-guide)

The [ROCgdb user guide](https://rocm.docs.amd.com/projects/ROCgdb/en/latest/ROCgdb/gdb/doc/gdb/index.html) provides detailed information about using ROCgdb.
This user guide is also installed in the following directories when you [install ROCm](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/):

`/opt/rocm/share/info/rocgdb/gdb.info`

as a texinfo file`/opt/rocm/share/doc/rocgdb/rocgdb.pdf`

as a PDF file

For specific information about debugging heterogeneous programs on ROCm software, refer to the following chapters in the ROCgdb user guide:

**Debugging Heterogeneous Programs:**Provides general information about debugging heterogeneous programs. It also discusses features and commands that are not currently implemented but provisionally planned for future versions.**Configuration-Specific Information > Architectures > AMD GPU:**Provides specific information about debugging heterogeneous programs on ROCm software with supported AMD GPU hardware. This section also lists the implementation status and known issues of the current version.

You can use the standard [GDB](http://www.gnu.org/software/gdb) commands for both CPU and GPU code debugging.
