---
title: "Composable Kernel wrapper &#8212; Composable Kernel 1.2.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/composable_kernel/en/latest/reference/Composable-Kernel-wrapper.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:17:06.116692+00:00
content_hash: "da47391b6b38521f"
---

# Composable Kernel wrapper[#](#composable-kernel-wrapper)

The Composable Kernel library provides a lightweight wrapper to simplify the more complex operations.

Example:

```
const auto shape_4x2x4 = ck::make_tuple(4, ck::make_tuple(2, 4));
const auto strides_s2x1x8 = ck::make_tuple(2, ck::make_tuple(1, 8));
const auto layout = ck::wrapper::make_layout(shape_4x2x4, strides_s2x1x8);
std::array<ck::index_t, 32> data;
auto tensor = ck::wrapper::make_tensor<ck::wrapper::MemoryTypeEnum::Generic>(&data[0], layout);
for(ck::index_t w = 0; w < size(tensor); w++) {
tensor(w) = w;
}
// slice() == slice(0, -1) (whole dimension)
auto tensor_slice = tensor(ck::wrapper::slice(1, 3), ck::make_tuple(ck::wrapper::slice(), ck::wrapper::slice()));
std::cout << "dims:2,(2,4) strides:2,(1,8)" << std::endl;
for(ck::index_t h = 0; h < ck::wrapper::size<0>(tensor_slice); h++)
{
for(ck::index_t w = 0; w < ck::wrapper::size<1>(tensor_slice); w++)
{
std::cout << tensor_slice(h, w) << " ";
}
std::cout << std::endl;
}
```

Output:

```
dims:2,(2,4) strides:2,(1,8)
1 5 9 13 17 21 25 29
2 6 10 14 18 22 26 30
```

Tutorials:

Advanced examples:
