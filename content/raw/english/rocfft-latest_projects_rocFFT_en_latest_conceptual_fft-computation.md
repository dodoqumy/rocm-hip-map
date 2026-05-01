---
title: "FFT computation &#8212; rocFFT 1.0.36 Documentation"
source_url: "https://rocm.docs.amd.com/projects/rocFFT/en/latest/conceptual/fft-computation.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T09:16:30.118454+00:00
content_hash: "dfa731bda4388fb7"
---

# FFT computation[#](#fft-computation)

rocFFT is an implementation of the Discrete Fourier Transform (DFT) that makes use of symmetries in the DFT definition to reduce the mathematical complexity from \(O(N^2)\) to \(O(N \log N)\).

## How does the library compute DFTs?[#](#how-does-the-library-compute-dfts)

Here are the formulas for 1D, 2D, and 3D complex DFTs:

For a 1D complex DFT:

\({\tilde{x}}_j = \sum_{k=0}^{n-1}x_k\exp\left({\pm i}{{2\pi jk}\over{n}}\right)\hbox{ for } j=0,1,\ldots,n-1\)

Where \(x_k\) is the complex data to be transformed, \(\tilde{x}_j\) is the transformed data, and the sign \(\pm\) determines the direction of the transform: \(-\) for forward and \(+\) for backward.

For a 2D complex DFT:

\({\tilde{x}}_{jk} = \sum_{q=0}^{m-1}\sum_{r=0}^{n-1}x_{rq}\exp\left({\pm i} {{2\pi jr}\over{n}}\right)\exp\left({\pm i}{{2\pi kq}\over{m}}\right)\)

For \(j=0,1,\ldots,n-1\hbox{ and } k=0,1,\ldots,m-1\), where \(x_{rq}\) is the complex data to be transformed, \(\tilde{x}_{jk}\) is the transformed data, and the sign \(\pm\) determines the direction of the transform.

For a 3D complex DFT:

\(\tilde{x}_{jkl} = \sum_{s=0}^{p-1}\sum_{q=0}^{m-1}\sum_{r=0}^{n-1}x_{rqs}\exp\left({\pm i} {{2\pi jr}\over{n}}\right)\exp\left({\pm i}{{2\pi kq}\over{m}}\right)\exp\left({\pm i}{{2\pi ls}\over{p}}\right)\)

For \(j=0,1,\ldots,n-1\hbox{ and } k=0,1,\ldots,m-1\hbox{ and } l=0,1,\ldots,p-1\), where \(x_{rqs}\) is the complex data to be transformed, \(\tilde{x}_{jkl}\) is the transformed data, and the sign \(\pm\) determines the direction of the transform.
