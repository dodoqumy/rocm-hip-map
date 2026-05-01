---
title: "Debugging rocSPARSE functions &#8212; rocSPARSE 4.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocSPARSE/en/latest/reference/debugging.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:26.270397+00:00
content_hash: "3e1949e15ee736b1"
---

# Debugging rocSPARSE functions[#](#debugging-rocsparse-functions)

This module contains all routines useful for debugging rocSPARSE programs.

## rocsparse_enable_debug_kernel_launch()[#](#rocsparse-enable-debug-kernel-launch)

-
void rocsparse_enable_debug_kernel_launch()
[#](#_CPPv436rocsparse_enable_debug_kernel_launchv) Enable debug kernel launch.

If the debug kernel launch is enabled then hip errors are checked before and after every kernel launch.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_KERNEL_LAUNCH.


## rocsparse_disable_debug_kernel_launch()[#](#rocsparse-disable-debug-kernel-launch)

-
void rocsparse_disable_debug_kernel_launch()
[#](#_CPPv437rocsparse_disable_debug_kernel_launchv) Disable debug kernel launch.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_KERNEL_LAUNCH.


## rocsparse_state_debug_kernel_launch()[#](#rocsparse-state-debug-kernel-launch)

-
int rocsparse_state_debug_kernel_launch()
[#](#_CPPv435rocsparse_state_debug_kernel_launchv) Query whether debugging kernel launch has been enabled. See

[rocsparse_enable_debug_kernel_launch](#rocsparse-debugging_8h_1a6ae154ed6d22f218de218f3e4bcd8709).- Returns:
1 if enabled, 0 otherwise.



## rocsparse_enable_debug_arguments()[#](#rocsparse-enable-debug-arguments)

-
void rocsparse_enable_debug_arguments()
[#](#_CPPv432rocsparse_enable_debug_argumentsv) Enable debug arguments.

If the debug arguments is enabled then messages are displayed when errors occur during argument checking. It provide information to the user depending of the setup of the verbosity

[rocsparse_enable_debug_arguments_verbose](#rocsparse-debugging_8h_1a3efa35eea3ee5934e77a7700616ed744),[rocsparse_disable_debug_arguments_verbose](#rocsparse-debugging_8h_1ade4bcdce2c5f3cac0559c5a75a3f629e)and[rocsparse_state_debug_arguments_verbose](#rocsparse-debugging_8h_1aa264cf67f995c44dc584f532e926839e).Note

This routine ignores the environment variable ROCSPARSE_DEBUG_ARGUMENTS.


## rocsparse_disable_debug_arguments()[#](#rocsparse-disable-debug-arguments)

-
void rocsparse_disable_debug_arguments()
[#](#_CPPv433rocsparse_disable_debug_argumentsv) Disable debug arguments.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_ARGUMENTS.

Note

This routines disables debug arguments verbose.


## rocsparse_state_debug_arguments()[#](#rocsparse-state-debug-arguments)

-
int rocsparse_state_debug_arguments()
[#](#_CPPv431rocsparse_state_debug_argumentsv) Query whether debugging arguments has been enabled. See

[rocsparse_enable_debug_arguments](#rocsparse-debugging_8h_1aea11034824132c254509fc7f796ff98d).- Returns:
1 if enabled, 0 otherwise.



## rocsparse_enable_debug_arguments_verbose()[#](#rocsparse-enable-debug-arguments-verbose)

-
void rocsparse_enable_debug_arguments_verbose()
[#](#_CPPv440rocsparse_enable_debug_arguments_verbosev) Enable debug arguments verbose.

If the debug arguments (verbose) is enabled then messages are displayed when errors occur during argument checking. It provide information to the user depending of the setup of the verbosity

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_ARGUMENTS_VERBOSE)


## rocsparse_disable_debug_arguments_verbose()[#](#rocsparse-disable-debug-arguments-verbose)

-
void rocsparse_disable_debug_arguments_verbose()
[#](#_CPPv441rocsparse_disable_debug_arguments_verbosev) Disable debug arguments verbose.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_ARGUMENTS_VERBOSE)


## rocsparse_state_debug_arguments_verbose()[#](#rocsparse-state-debug-arguments-verbose)

-
int rocsparse_state_debug_arguments_verbose()
[#](#_CPPv439rocsparse_state_debug_arguments_verbosev) Query whether debugging arguments (verbose) has been enabled. See

[rocsparse_enable_debug_arguments_verbose](#rocsparse-debugging_8h_1a3efa35eea3ee5934e77a7700616ed744).- Returns:
1 if enabled, 0 otherwise.



## rocsparse_enable_debug()[#](#rocsparse-enable-debug)

-
void rocsparse_enable_debug()
[#](#_CPPv422rocsparse_enable_debugv) Enable debug.

If the debug is enabled then code traces are generated when unsuccessful status returns occur. It provides information to the user depending of the set of the verbosity (

[rocsparse_enable_debug_verbose](#rocsparse-debugging_8h_1ad01a5358824144ff8532a5bc0010492a),[rocsparse_disable_debug_verbose](#rocsparse-debugging_8h_1a3d7133fe0196d670d1a4d4f8abd5c1ab)and[rocsparse_state_debug_verbose](#rocsparse-debugging_8h_1a021e2b07766dc37e1c7358ca394ecd68)).Note

This routine ignores the environment variable ROCSPARSE_DEBUG.


## rocsparse_disable_debug()[#](#rocsparse-disable-debug)

-
void rocsparse_disable_debug()
[#](#_CPPv423rocsparse_disable_debugv) Disable debug.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG.


## rocsparse_state_debug()[#](#rocsparse-state-debug)

-
int rocsparse_state_debug()
[#](#_CPPv421rocsparse_state_debugv) Query whether debug has been enabled. See

[rocsparse_enable_debug](#rocsparse-debugging_8h_1aaf3a4e3afc44f0265566a30fe4e9bab2).- Returns:
1 if enabled, 0 otherwise.



## rocsparse_enable_debug_warnings()[#](#rocsparse-enable-debug-warnings)

-
void rocsparse_enable_debug_warnings()
[#](#_CPPv431rocsparse_enable_debug_warningsv) Enable debug warnings.

If the debug warnings are enabled, then some specific warnings could be printed during the execution.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_WARNINGS.


## rocsparse_disable_debug_warnings()[#](#rocsparse-disable-debug-warnings)

-
void rocsparse_disable_debug_warnings()
[#](#_CPPv432rocsparse_disable_debug_warningsv) Disable debug warnings.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_WARNINGS.


## rocsparse_enable_debug_verbose()[#](#rocsparse-enable-debug-verbose)

-
void rocsparse_enable_debug_verbose()
[#](#_CPPv430rocsparse_enable_debug_verbosev) Enable debug verbose.

The debug verbose displays a stack of code traces showing where the code is handling a unsuccessful status.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_VERBOSE.


## rocsparse_disable_debug_verbose()[#](#rocsparse-disable-debug-verbose)

-
void rocsparse_disable_debug_verbose()
[#](#_CPPv431rocsparse_disable_debug_verbosev) Disable debug verbose.

Note

This routine ignores the environment variable ROCSPARSE_DEBUG_VERBOSE.


## rocsparse_state_debug_verbose()[#](#rocsparse-state-debug-verbose)

-
int rocsparse_state_debug_verbose()
[#](#_CPPv429rocsparse_state_debug_verbosev) Query whether debug (verbose) has been enabled. See

[rocsparse_enable_debug_verbose](#rocsparse-debugging_8h_1ad01a5358824144ff8532a5bc0010492a).- Returns:
1 if enabled, 0 otherwise.



## rocsparse_enable_debug_force_host_assert()[#](#rocsparse-enable-debug-force-host-assert)

-
void rocsparse_enable_debug_force_host_assert()
[#](#_CPPv440rocsparse_enable_debug_force_host_assertv) Enable debug force host assert.

The debug force host assert forces the evaluation of assert on host when the compiler directive NDEBUG is used.


## rocsparse_disable_debug_force_host_assert()[#](#rocsparse-disable-debug-force-host-assert)

-
void rocsparse_disable_debug_force_host_assert()
[#](#_CPPv441rocsparse_disable_debug_force_host_assertv) Disable debug force host assert.


## rocsparse_state_debug_force_host_assert()[#](#rocsparse-state-debug-force-host-assert)

-
int rocsparse_state_debug_force_host_assert()
[#](#_CPPv439rocsparse_state_debug_force_host_assertv) Query whether debug force host assert has been enabled. See

[rocsparse_enable_debug_force_host_assert](#rocsparse-debugging_8h_1a20bdafe3dee6bf645185a92e5b974368).- Returns:
1 if enabled, 0 otherwise.
