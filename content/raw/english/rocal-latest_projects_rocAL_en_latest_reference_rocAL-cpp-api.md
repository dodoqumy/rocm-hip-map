---
title: "The rocAL C++ API for contributors &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/reference/rocAL-cpp-api.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:59.583217+00:00
content_hash: "9cfcaab3d5f87aee"
---

# The rocAL C++ API for contributors[#](#the-rocal-c-api-for-contributors)

The rocAL C++ API is meant for developers who want to contribute to the rocAL project, or who want to create their own custom augmentations.

## C++ Common APIs[#](#c-common-apis)

The following sections list the commonly used C++ APIs.

### rocalCreate[#](#rocalcreate)

Use: To create the pipeline

Returns: The context for the pipeline

Arguments:

RocalProcessMode: Defines whether rocal data loading should be on the CPU or

[GPU](https://github.com/ROCm/rocAL/blob/develop/rocAL/include/api/rocal_api_types.h#L153).

```
RocalProcessMode:: ROCAL_PROCESS_GPU
RocalProcessMode::ROCAL_PROCESS_CPU
```

RocalTensorOutputType: Defines whether the output of rocal tensor is

[FP32 or FP16](https://github.com/ROCm/rocAL/blob/develop/rocAL/include/api/rocal_api_types.h#L227).

```
RocalTensorOutputType::ROCAL_FP32
RocalTensorOutputType::ROCAL_FP16
```

See [rocalCreate example](https://github.com/ROCm/rocAL/blob/develop/rocAL/include/api/rocal_api.h#L54).

```
extern "C" RocalContext ROCAL_API_CALL rocalCreate(size_t batch_size, RocalProcessMode affinity, int gpu_id = 0, size_t cpu_thread_count = 1, size_t prefetch_queue_depth = 3, RocalTensorOutputType output_tensor_data_type = RocalTensorOutputType::ROCAL_FP32);
```

### rocalVerify[#](#rocalverify)

Use: To verify the graph for all the inputs and outputs

Returns: A status code indicating the success or failure

See [rocalVerify example](https://github.com/ROCm/rocAL/blob/develop/rocAL/include/api/rocal_api.h#L68).

```
extern "C" RocalStatus ROCAL_API_CALL rocalVerify(RocalContext context);
```

### rocalRun[#](#rocalrun)

Use: To process and run the built and verified graph

Returns: A status code indicating the success or failure

See [rocalRun example](https://github.com/ROCm/rocAL/blob/develop/rocAL/include/api/rocal_api.h#L77).

```
extern "C" RocalStatus ROCAL_API_CALL rocalRun(RocalContext context);
```

### rocalRelease[#](#rocalrelease)

Use: To free all the resources allocated during the graph creation process

Returns: A status code indicating the success or failure

See [rocalRelease example](https://github.com/ROCm/rocAL/blob/develop/rocAL/include/api/rocal_api.h#L86).

```
extern "C" RocalStatus ROCAL_API_CALL rocalRelease(RocalContext rocal_context);
```

### Image Augmentation Using C++ API[#](#image-augmentation-using-c-api)

The example below shows how to create a pipeline, read JPEG images, perform certain augmentations on them, and show the output using OpenCV by utilizing [C++ API](https://github.com/ROCm/rocAL/blob/develop/tests/cpp_api/image_augmentation/image_augmentation.cpp#L103).

```
Auto handle = rocalCreate(inputBatchSize, processing_device?RocalProcessMode::ROCAL_PROCESS_GPU:RocalProcessMode::ROCAL_PROCESS_CPU, 0,1);
input1 = rocalJpegFileSource(handle, folderPath1, color_format, shard_count, false, shuffle, false, ROCAL_USE_USER_GIVEN_SIZE, decode_width, decode_height, dec_type);
image0 = rocalResize(handle, input1, resize_w, resize_h, true);
RocalImage image1 = rocalRain(handle, image0, false);
RocalImage image11 = rocalFishEye(handle, image1, false);
rocalRotate(handle, image11, true, rand_angle);
// Creating successive blur nodes to simulate a deep branch of augmentations
RocalImage image2 = rocalCropResize(handle, image0, resize_w, resize_h, false, rand_crop_area);;
for(int i = 0 ; i < aug_depth; i++)
{
image2 = rocalBlur(handle, image2, (i == (aug_depth -1)) ? true:false );
}
// Calling the API to verify and build the augmentation graph
if(rocalVerify(handle) != ROCAL_OK)
{
std::cout << "Could not verify the augmentation graph" << std::endl;
return -1;
}
while (!rocalIsEmpty(handle))
{
if(rocalRun(handle) != 0)
break;
}
```

To see a sample image augmentation application in C++, see [Image Augmentation](https://github.com/ROCm/rocAL/tree/develop/tests/cpp_api/image_augmentation).
