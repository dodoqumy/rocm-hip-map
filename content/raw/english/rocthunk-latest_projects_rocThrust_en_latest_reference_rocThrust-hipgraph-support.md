---
title: "rocThrust hipGraph Support &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/reference/rocThrust-hipgraph-support.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:12.860102+00:00
content_hash: "a2f941e269a36e83"
---

# rocThrust hipGraph Support[#](#rocthrust-hipgraph-support)

Currently, rocThrust does not support the use of `hipGraphs`

. `hipGraphs`

are not allowed to contain any synchronous
function calls or barriers. Thrust API functions are blocking (synchronous with respect to the host) by default.

Thrust does provide asynchronous versions of a number of algorithms. These are contained in the `thrust::async`

namespace
(see the headers in `rocThrust/thrust/async/`

). However, these algorithms operate asynchronously by returning futures.
This approach is different from the form of asynchronous execution required within `hipGraphs`

, which must be achieved by
issuing calls into a user-defined `hipStream`

.

While it is possible to create execution policies that encourage Thrust API algorithms to execute within a user-defined stream,
(eg. `thrust::hip_rocprim::par.on(stream)`

), this is not enough to guarantee that synchronization will not occur within
a given algorithm. This is because some Thrust functions require execution policies to be passed in at compile time (via template
arguments) rather than at runtime. Since streams must be created at runtime, there is no way to pass these functions a stream.
Adding a stream argument to such functions breaks compatibility with the Thrust API.

For these reasons, we recommend that you do not use hipGraphs together with rocThrust code.
