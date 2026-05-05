---
title: "How to use rocThrust in a CMake project &#8212; rocThrust Documentation 4.2.0 documentation"
source_url: "https://rocm.docs.amd.com/projects/rocThrust/en/latest/how-to/use-rocThrust-in-a-project.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-02T21:19:32.370822+00:00
content_hash: "5d5bc00dad83271a"
---

# How to use rocThrust in a CMake project[#](#how-to-use-rocthrust-in-a-cmake-project)

To use rocThrust in your own project, add the following lines to your CMakeLists file:

```
# On ROCm rocThrust requires rocPRIM
find_package(rocprim REQUIRED CONFIG PATHS "/opt/rocm/rocprim")
# "/opt/rocm" - default install prefix
find_package(rocthrust REQUIRED CONFIG PATHS "/opt/rocm/rocthrust")
[...]
# include rocThrust headers and roc::rocprim_hip target
target_link_libraries(<your_target> roc::rocthrust)
```
