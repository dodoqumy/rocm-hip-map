---
title: "rocAL Operators &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/conceptual/rocAL-operators.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:47.351885+00:00
content_hash: "481d5a0b17f6ec84"
---

# rocAL Operators[#](#rocal-operators)

rocAL operators offer the flexibility to run on CPU or GPU for building hybrid pipelines. They also support classification and object detection on the workload. Some of the useful operators supported by rocAL are listed below:

**Augmentations:**These are used to enhance the data set by adding effects to the original images. To use the augmentations, import the instance of`amd.rocal.fn`

into the Python script. These augmentation APIs further call the RPP kernels underneath (HIP/HOST) depending on the backend used to build RPP and rocAL.**Readers:**These are used to read and understand the different types of datasets and their metadata. Some examples of readers are list of files with folders, LMDB, TFRecord, and JSON file for metadata. To use the readers, import the instance of`amd.rocal.readers`

into the Python script.**Decoders:**These are used to support different input formats of images and videos. Decoders extract data from the datasets that are in compressed formats such as JPEG, MP4, etc. To use the decoders, import the instance of`amd.rocal.decoders`

into the Python script.

## Table 1. Augmentations Available through rocAL[#](#table-1-augmentations-available-through-rocal)

Color Augmentations |
Effects Augmentations |
Geometry Augmentations |
|---|---|---|
Blend
|
Fog
|
Crop
|
Blur
|
Jitter
|
Crop Mirror Normalization
|
Brightness
|
Pixelization
|
Crop Resize
|
Color Temperature
|
Raindrops
|
Fisheye Lens
|
Color Twist
|
Snowflakes
|
Flip (Horizontal, Vertical, and Both)
|
Contrast
|
Salt and Pepper Noise
|
Lens Correction
|
Exposure
|
Random Crop
|
|
Gamma
|
Resize
|
|
Hue
|
Resize Crop Mirror
|
|
Saturation
|
Rotation
|
|
Vignette
|
Warp Affine
|

## Table 2. Readers Available through rocAL[#](#table-2-readers-available-through-rocal)

Readers |
Description |
|---|---|
File Reader
|
Reads images from a list of files in a folder(s)
|
Video Reader
|
Reads videos from a list of files in a folder(s)
|
Caffe LMDB Reader
|
Reads (key, value) pairs from Caffe LMDB
|
Caffe2 LMDB Reader
|
Reads (key, value) pairs from Caffe2 LMDB
|
COCO Reader - file source and keypoints
|
Reads images and JSON annotations from COCO dataset
|
TFRecord Reader
|
Reads from a TFRecord dataset
|
MXNet Reader
|
Reads from a RecordIO dataset
|
Web Dataset Reader
|
Reads from a web dataset
|
CIFAR-10 Dataset Reader
|
Reads from a binary CIFAR-10 dataset
|

## Table 3. Decoders Available through rocAL[#](#table-3-decoders-available-through-rocal)

Decoders |
Description |
|---|---|
Image
|
Decodes JPEG images
|
Image_raw
|
Decodes images in raw format
|
Image_random_crop
|
Decodes and randomly crops JPEG images
|
Image_slice
|
Decodes and slices JPEG images
|

To see examples demonstrating the usage of decoders and readers, see
[rocAL Python Examples](https://github.com/ROCm/rocAL/tree/develop/docs/examples).
