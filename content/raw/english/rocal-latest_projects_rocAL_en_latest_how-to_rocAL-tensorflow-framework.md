---
title: "Using rocAL with TensorFlow for training &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/how-to/rocAL-tensorflow-framework.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:45.654307+00:00
content_hash: "6b313c361e4521a1"
---

# Using rocAL with TensorFlow for training[#](#using-rocal-with-tensorflow-for-training)

The TensorFlow plugin for rocAL includes `ROCALIterator`

. `ROCALIterator`

runs the training and validation [pipelines](../reference/rocAL-pipeline.html). It prefetches and loads the next batch of files while the previous batch is being processed.

Pipelines are created by either instantiating them with `Pipeline()`

or decorating a graph function with `@pipeline_def`

:

```
from amd.rocal.pipeline import Pipeline
import amd.rocal.fn as fn
[...]
trainPipe = Pipeline(batch_size=train_batch_size, num_threads=8, rocal_cpu=rocal_cpu, device_id=device_id, prefetch_queue_depth=6,
tensor_layout=types.NHWC, mean=[0, 0, 0], std=[255, 255, 255], tensor_dtype=types.FLOAT)
with trainPipe:
inputs = fn.readers.tfrecord(path=train_records_dir, reader_type=TFRecordReaderType, user_feature_key_map=featureKeyMap,
features={
'image/encoded': tf.io.FixedLenFeature((), tf.string, ""),
'image/class/label': tf.io.FixedLenFeature([1], tf.int64, -1),
'image/filename': tf.io.FixedLenFeature((), tf.string, "")
}
)
jpegs = inputs["image/encoded"]
labels = inputs["image/class/label"]
images = fn.decoders.image(jpegs, user_feature_key_map=featureKeyMap, output_type=types.RGB, path=train_records_dir)
resized = fn.resize(images, resize_width=image_size[0], resize_height=image_size[1])
flip_coin = fn.random.coin_flip(probability=0.5)
cmn_images = fn.crop_mirror_normalize(resized, crop=(image_size[1], image_size[0]),
mean=[127.5, 127.5, 127.5],
std=[127.5, 127.5, 127.5],
mirror=flip_coin,
output_dtype=types.FLOAT,
output_layout=types.NHWC)
trainPipe.set_outputs(cmn_images)
```

Data is read from the dataset using `readers.tfrecord`

, which reads from TFRecord datasets. `ROCALIterator`

is then used to load data and run the pipeline. For example, in [ train.py](https://github.com/ROCm/rocAL/tree/develop/docs/examples/tf/pets_training/train.py):

```
from amd.rocal.plugin.tf import ROCALIterator
[...]
trainIterator = ROCALIterator(trainPipe, device=device)
valIterator = ROCALIterator(valPipe, device=device)
```

An example of TensorFlow training using rocAL is available in the [rocAL GitHub repository](https://github.com/ROCm/rocAL/blob/develop/docs/examples/tf/). [Jupyter Notebooks](https://github.com/ROCm/rocAL/tree/develop/docs/examples/notebooks) are also available.

A [Docker container](https://github.com/ROCm/rocAL/blob/develop/docker/README.md) is available for PyTorch training with rocAL.
