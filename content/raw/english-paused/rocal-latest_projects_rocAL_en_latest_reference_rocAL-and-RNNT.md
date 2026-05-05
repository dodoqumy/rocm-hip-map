---
title: "rocAL RNNT dataloading in Python &#8212; rocAL 2.5.0 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocAL/en/latest/reference/rocAL-and-RNNT.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:22:43.469412+00:00
content_hash: "619701c27b73c8c7"
---

# rocAL RNNT dataloading in Python[#](#rocal-rnnt-dataloading-in-python)

rocAL supports the RNNT speech recognition model through audio readers and other functions that can be used with PyTorch.

All the functions used for RNNT dataloading are available in the `amd.rocal.fn`

module. See [Using rocAL with the Python API](rocAL-python-api.html) for more details about this module.

All the augmentations used in the RNNT dataloader pipeline are available as part of rocAL. These augmentations need to be plugged into the rocAL PyTorch dataloader to run the training. PyTorch samples can be found [in the rocAL GitHub repository](https://github.com/ROCm/rocAL/tree/develop/docs/examples/pytorch).
.. Note:

```
The rocAL GitHub repository does not host the entire RNNT dataloader source.
```

Function |
Description |
Details |
|---|---|---|
|
Resamples an audio signal. |
Resampling is achieved by applying a sinc filter with a Hann window. The extent is controlled by the function’s |
|
Detects leading and trailing silences. |
Returns the beginning and length of the non-silent region. Compares the short-term power calculated for the window length of the signal with a silence cut-off threshold. The signal is considered to be silent when the short term power in decibels is less than the cut-off threshold in decibels. |
|
Slices the input. |
The slice is specified by an anchor and a shape for the slice. |
|
Applies a preemphasis filter to the input. |
The filter used is |
|
Produces a spectrogram from a 1D audio signal. |
|
|
Converts a spectrogram to a mel spectrogram. |
Conversion is done by applying a bank of triangular filters where the frequency dimension is selected from the input layout. |
|
Converts a magnitude to decibels. |
The conversion is done using |
|
Normalizes an input. |
Normalization is done by removing the mean and dividing by the standard deviation. |
