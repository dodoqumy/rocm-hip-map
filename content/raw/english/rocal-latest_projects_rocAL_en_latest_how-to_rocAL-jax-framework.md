---
title: "Using rocAL with JAX for training &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/how-to/rocAL-jax-framework.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:35.431878+00:00
content_hash: "b88da375ba13cbe1"
---

# Using rocAL with JAX for training[#](#using-rocal-with-jax-for-training)

The Jax plugin for rocAL can process the entire dataset at once or it can divide the dataset into shards that are distributed over a mesh of GPUs.

```
from jax.sharding import PositionalSharding
from jax.experimental import mesh_utils
mesh = mesh_utils.create_device_mesh((jax.device_count(), 1))
sharding = PositionalSharding(mesh)
```

Note

The [ jax_classification_reader.py](https://github.com/ROCm/rocAL/tree/develop/tests/python_api/jax_classification_reader.py) sample and the

[Jax Jupyter notebook](../examples/notebooks/jax_training_example.html)both use the

`PositionalSharding()`

helper function to automatically divide the dataset into shards. In later versions of Jax, this function has been deprecated. The `NamedSharding()`

function is used instead.When the dataset is divided over multiple GPUs, one [pipeline](../reference/rocAL-pipeline.html) is assigned to each GPU. The pipelines process the data shard assigned to the GPU.

The pipelines are then processed by the iterators. Two rocAL Jax iterators are available:

`ROCALJaxIterator`

is used for general data processing pipelines.`ROCALPeekableIterator`

is a peekable version of`ROCALJaxIterator`

that lets you peek at the next item without consuming it.

Both Jax iterators can take a single pipeline if the dataset is being processed all at once, or an array of pipelines and the sharding value if the dataset has been divided over a mesh of GPUs.

Pipelines are created by either instantiating them with `Pipeline()`

or decorating a graph function with `@pipeline_def`

.

In the [Jax Jupyter notebook](../examples/notebooks/jax_training_example.html), training is done over a mesh of GPUs.

Each training pipeline is instantiated, populated with graph elements, and built, before being added to the array of pipelines:

```
from amd.rocal.pipeline import Pipeline
from amd.rocal.plugin.jax import ROCALJaxIterator
[...]
train_pipelines = []
for id in range(device_count):
train_pipeline = Pipeline(batch_size=batch_size, num_threads=8, device_id=id, seed=id+42, rocal_cpu=False, tensor_dtype = types.FLOAT, tensor_layout=types.NCHW, prefetch_queue_depth = 3, mean=[0.5 * 255,0.5 * 255,0.5 * 255], std = [0.5 * 255,0.5 * 255,0.5 * 255], output_memory_type = types.DEVICE_MEMORY)
with train_pipeline:
cifar10_reader_output = fn.readers.cifar10(file_root=f'{data_path}/cifar-10-batches-bin', shard_id=id, num_shards=device_count, filename_prefix='data_batch_', random_shuffle=True, last_batch_policy=types.LAST_BATCH_DROP)
cmnp = fn.crop_mirror_normalize(cifar10_reader_output,
output_layout = types.NCHW,
output_dtype = types.FLOAT,
crop=(32, 32),
mirror=0,
mean=[0.5 * 255,0.5 * 255,0.5 * 255],
std=[0.5 * 255,0.5 * 255,0.5 * 255])
train_pipeline.set_outputs(cmnp)
train_pipeline.build()
train_pipelines.append(train_pipeline)
training_iterator = ROCALJaxIterator(train_pipelines, sharding)
```

The pipelines are then passed to the iterator:

```
imageIteratorPipeline = ROCALJaxIterator(pipelines, sharding=sharding)
```

Jax isn’t tied to a specific data loader and can use any dataset reader.

The validation pipeline in the [Jax Jupyter notebook](../examples/notebooks/jax_training_example.html) processes the entire dataset without sharding:

```
val_pipeline = Pipeline(batch_size=batch_size, num_threads=8, device_id=0, seed=42, rocal_cpu=False, tensor_dtype = types.FLOAT, tensor_layout=types.NCHW, prefetch_queue_depth = 3, mean=[0.5 * 255,0.5 * 255,0.5 * 255], std = [0.5 * 255,0.5 * 255,0.5 * 255], output_memory_type = types.DEVICE_MEMORY)
with val_pipeline:
val_cifar10_reader_output = fn.readers.cifar10(file_root=f'{data_path}/cifar-10-batches-bin', shard_id=0, num_shards=1, filename_prefix='test_batch', last_batch_policy=types.LAST_BATCH_DROP)
val_cmnp = fn.crop_mirror_normalize(val_cifar10_reader_output,
output_layout = types.NCHW,
output_dtype = types.FLOAT,
crop=(32, 32),
mirror=0,
mean=[0.5 * 255,0.5 * 255,0.5 * 255],
std=[0.5 * 255,0.5 * 255,0.5 * 255])
val_pipeline.set_outputs(val_cmnp)
val_pipeline.build()
validation_iterator = ROCALJaxIterator(val_pipeline)
```

[Prebuilt Docker images with Jax pre-installed](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html#using-docker-with-jax-pre-installed) are available.
