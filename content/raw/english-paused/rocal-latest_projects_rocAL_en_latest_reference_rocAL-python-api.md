---
title: "rocAL Python API overview &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/reference/rocAL-python-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:23:03.427707+00:00
content_hash: "23b0c85b5df7f11c"
---

# rocAL Python API overview[#](#rocal-python-api-overview)

The rocAL Python package has been created using Pybind11 which enables data transfer between the rocAL C++ API and Python API.
The `rocal_pybind`

package includes both PyTorch and TensorFlow framework support and support for multiple data readers such as `FileReader`

, `COCOReader`

, and `TFRecordReader`

.

The rocAL data types are defined in [amd.rocal.types](https://github.com/ROCm/rocAL/blob/develop/rocAL_pybind/amd/rocal/types.py).

`amd.rocal.fn`

Contains the image augmentations linked to the rocAL C++ API.

`amd.rocal.decoders`

Image, video, and audio decoders.

`amd.rocal.readers`

Image, video, and audio readers.

`amd.rocal.pipeline`

The pipeline class encapsulates the data needed to build and run a rocAL graph. This includes support for context and graph creation, functions to verify and run the graph, and data transfer functions.

`amd.rocal.types`

enums exported from the C++ API to Python.

`amd.rocal.plugin.pytorch`

PyTorch plugin that includes the

`ROCALGenericIterator`

for Pytorch. The`ROCALClassificationIterator`

class implements an iterator for image classification that returns labelled images.`amd.rocal.plugin.tf`

TensorFlow plugin that includes the

`readers.tfrecord`

TensorFlow reader.`amd.rocal.plugin.jax`

JAX plugin that includes the

`ROCALJaxIterator`

for JAX. The`ROCALJaxIterator`

implements an iterator for running a pipeline over multiple devices.
