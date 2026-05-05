---
title: "Internal threading management &#8212; ROCprofiler-SDK 1.1.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/api-reference/rocprofiler-sdk_api/modules/internal_threading_management.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:24:38.342932+00:00
content_hash: "1b75acdce6597f12"
---

# Internal threading management[#](#internal-threading-management)

-
typedef void (*rocprofiler_internal_thread_library_cb_t)(
[rocprofiler_runtime_library_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv429rocprofiler_runtime_library_t), void*)[#](#_CPPv440rocprofiler_internal_thread_library_cb_t) (experimental) Callback type before and after internal thread creation.


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_at_internal_thread_create([rocprofiler_internal_thread_library_cb_t](#_CPPv440rocprofiler_internal_thread_library_cb_t)precreate,[rocprofiler_internal_thread_library_cb_t](#_CPPv440rocprofiler_internal_thread_library_cb_t)postcreate, int libs, void *data)[#](#_CPPv437rocprofiler_at_internal_thread_create40rocprofiler_internal_thread_library_cb_t40rocprofiler_internal_thread_library_cb_tiPv) (experimental) Invoke this function to receive callbacks before and after the creation of an internal thread by a library which as invoked on the thread which is creating the internal thread(s).

Use the

[rocprofiler_runtime_library_t](../global_data_structures_topics_files/global_basic_data_types.html#group___b_a_s_i_c___d_a_t_a___t_y_p_e_s_1gad6fd541ff293c8fb83065605c0b825a9)enumeration for specifying which libraries you want callbacks before and after the library creates an internal thread. These callbacks will be invoked on the thread that is about to create the new thread (not on the newly created thread). In thread-aware tools that wrap pthread_create, this can be used to disable the wrapper before the pthread_create invocation and re-enable the wrapper afterwards. In many cases, tools will want to ignore the thread(s) created by rocprofiler since these threads do not exist in the normal application execution, whereas the internal threads for HSA, HIP, etc. are created in normal application execution; however, the HIP, HSA, etc. internal threads are typically background threads which just monitor kernel completion and are unlikely to contribute to any performance issues. Please note that the postcreate callback is guaranteed to be invoked after the underlying system call to create a new thread but it does not guarantee that the new thread has been started. Please note, that once these callbacks are registered, they cannot be removed so the caller is responsible for ignoring these callbacks if they want to ignore them beyond a certain point in the application.- Parameters:
**precreate**–**[in]**Callback invoked immediately before a new internal thread is created**postcreate**–**[in]**Callback invoked immediately after a new internal thread is created**libs**–**[in]**Bitwise-or of libraries, e.g.`ROCPROFILER_LIBRARY | ROCPROFILER_MARKER_LIBRARY`

means the callbacks will be invoked whenever rocprofiler and/or the marker library create internal threads but not when the HSA or HIP libraries create internal threads.**data**–**[in]**Data shared between callbacks

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– There are currently no conditions which result in any other value, even if internal threads have already been created- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_create_callback_thread([rocprofiler_callback_thread_t](#_CPPv429rocprofiler_callback_thread_t)*cb_thread_id)[#](#_CPPv434rocprofiler_create_callback_threadP29rocprofiler_callback_thread_t) (experimental) Create a handle to a unique thread (created by rocprofiler) which, when associated with a particular buffer, will guarantee those buffered results always get delivered on the same thread. This is useful to prevent/control thread-safety issues and/or enable multithreaded processing of buffers with non-overlapping data

- Parameters:
**cb_thread_id**–**[in]**User-provided pointer to a[rocprofiler_callback_thread_t](#structrocprofiler__callback__thread__t)- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Successful thread creation**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– Thread creation is no longer available post-initialization**ROCPROFILER_STATUS_ERROR**– Failed to create thread

- Returns:


-
[rocprofiler_status_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv420rocprofiler_status_t)rocprofiler_assign_callback_thread([rocprofiler_buffer_id_t](../global_data_structures_topics_files/global_basic_data_types.html#_CPPv423rocprofiler_buffer_id_t)buffer_id,[rocprofiler_callback_thread_t](#_CPPv429rocprofiler_callback_thread_t)cb_thread_id)[#](#_CPPv434rocprofiler_assign_callback_thread23rocprofiler_buffer_id_t29rocprofiler_callback_thread_t) (experimental) By default, all buffered results are delivered on the same thread. Using

[rocprofiler_create_callback_thread](#group___i_n_t_e_r_n_a_l___t_h_r_e_a_d_i_n_g_1gac11a2d92f8b1606f73d52b9f0b60a9f6), one or more buffers can be assigned to deliever their results on a unique, dedicated thread.- Parameters:
**buffer_id**–**[in]**Buffer identifier**cb_thread_id**–**[in]**Callback thread identifier via[rocprofiler_create_callback_thread](#group___i_n_t_e_r_n_a_l___t_h_r_e_a_d_i_n_g_1gac11a2d92f8b1606f73d52b9f0b60a9f6)

- Return values:
**ROCPROFILER_STATUS_SUCCESS**– Successful assignment of the delivery thread for the given buffer**ROCPROFILER_STATUS_ERROR_CONFIGURATION_LOCKED**– Thread assignment is no longer available post-initialization**ROCPROFILER_STATUS_ERROR_THREAD_NOT_FOUND**– Thread identifier did not match any of the threads created by rocprofiler**ROCPROFILER_STATUS_ERROR_BUFFER_NOT_FOUND**– Buffer identifier did not match any of the buffers registered with rocprofiler

- Returns:


-
struct rocprofiler_callback_thread_t
[#](#_CPPv429rocprofiler_callback_thread_t) *#include <rocprofiler-sdk/internal_threading.h>*(experimental) opaque handle to an internal thread identifier which delivers callbacks for buffers
