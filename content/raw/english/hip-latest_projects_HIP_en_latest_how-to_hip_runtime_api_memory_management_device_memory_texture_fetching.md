---
title: "Texture fetching &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_runtime_api/memory_management/device_memory/texture_fetching.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:59:18.094327+00:00
content_hash: "bfee54f14cf334f4"
---

:::::::::::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::::::::::
bd-content
::::::::::::::::::::::
bd-article-container
:::::::
{.bd-header-article .d-print-none}
::::::
{.header-article-items .header-article__inner}
::
header-article-items__start

header-article-item
[]{.fa-solid .fa-angle-right}

header-article-item

::

::
header-article-items__end
:
header-article-item

article-header-buttons
[]{.fa-solid .fa-list}

:
::
::::::
:::::::

{#jb-print-docs-body .onlyprint}
# Texture fetching

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

::::::::
{#texture-fetching .section}
[]{#id1}

# Texture fetching[\#](#texture-fetching "Link to this heading"){.headerlink}

Textures give access to specialized hardware on GPUs that is usually used in graphics processing. In particular, textures use a different way of accessing their underlying device memory. Memory accesses to textures are routed through a special read-only texture cache, that is optimized for logical spatial locality, e.g. locality in 2D grids. This can also benefit certain algorithms used in GPGPU computing, when the access pattern is the same as used when accessing normal textures.

Additionally, textures can be indexed using floating-point values. This is used in graphics applications to interpolate between neighboring values of a texture. Depending on the interpolation mode the index can be in the range of [`0`{.docutils .literal .notranslate}]{.pre} to [`size`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} or [`0`{.docutils .literal .notranslate}]{.pre} to [`1`{.docutils .literal .notranslate}]{.pre}. Textures also have a way of handling out-of-bounds accesses.

Depending on the value of the index, [[texture filtering]{.std .std-ref}](#texture-filtering){.reference .internal} or [[texture addressing]{.std .std-ref}](#texture-addressing){.reference .internal} is performed.

Here is the example texture used in this document for demonstration purposes. It is 2x2 texels and indexed in the \[0 to 1\] range.

<figure id="id4" class="align-center">
<a href="../../../../_images/original.png" class="reference internal image-reference"><img src="../../../../_images/original.png" style="width: 150px;" alt="Example texture" /></a>
<figcaption><p><span class="caption-text">Texture used as example</span><a href="#id4" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

In HIP textures objects are of type [`hipTextureObject_t`{.xref .cpp .cpp-struct .docutils .literal .notranslate}]{.pre} and created using [[`hipCreateTextureObject()`{.xref .cpp .cpp-func .docutils .literal .notranslate}]{.pre}](../../../../reference/hip_runtime_api/modules/memory_management/texture_management.html#_CPPv422hipCreateTextureObjectP18hipTextureObject_tPK15hipResourceDescPK14hipTextureDescPK19hipResourceViewDesc "hipCreateTextureObject"){.reference .internal}.

For a full list of available texture functions see the [[HIP texture API reference]{.std .std-ref}](../../../../reference/hip_runtime_api/modules/memory_management/texture_management.html#texture-management-reference){.reference .internal}.

A code example for how to use textures can be found in the [ROCm texture management example](https://github.com/ROCm/rocm-examples/blob/develop/HIP-Basic/texture_management/main.hip){.reference .external}

::
{#texture-filtering .section}
[]{#id2}

## Texture filtering[\#](#texture-filtering "Link to this heading"){.headerlink}

Texture filtering handles the usage of fractional indices. When the index is a fraction, the queried value lies between two or more texels (texture elements), depending on the dimensionality of the texture. The filtering method defines how to interpolate between these values.

The filter modes are specified in [`hipTextureFilterMode`{.xref .cpp .cpp-enumerator .docutils .literal .notranslate}]{.pre}.

The various texture filtering methods are discussed in the following sections.

{#nearest-point-filtering .section}
[]{#texture-fetching-nearest}

### Nearest point filtering[\#](#nearest-point-filtering "Link to this heading"){.headerlink}

This filter mode corresponds to [`hipFilterModePoint`{.docutils .literal .notranslate}]{.pre}.

In this method, the modulo of index is calculated as:

[`tex(x)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`T[floor(x)]`{.docutils .literal .notranslate}]{.pre}

This is also applicable for 2D and 3D variants.

This doesn't interpolate between neighboring values, which results in a pixelated look.

The following image shows a texture stretched to a 4x4 pixel quad but still indexed in the \[0 to 1\] range. The in-between values are the same as the values of the nearest texel.

<figure id="id5" class="align-center">
<a href="../../../../_images/nearest.png" class="reference internal image-reference"><img src="../../../../_images/nearest.png" style="width: 300px;" alt="Texture upscaled with nearest point filtering" /></a>
<figcaption><p><span class="caption-text">Texture upscaled with nearest point filtering</span><a href="#id5" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

{#linear-filtering .section}
[]{#texture-fetching-linear}

### Linear filtering[\#](#linear-filtering "Link to this heading"){.headerlink}

This filter mode corresponds to [`hipFilterModeLinear`{.docutils .literal .notranslate}]{.pre}.

The linear filtering method does a linear interpolation between values. Linear interpolation is used to create a linear transition between two values. The formula used is [`(1-t)P1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`tP2`{.docutils .literal .notranslate}]{.pre} where [`P1`{.docutils .literal .notranslate}]{.pre} and [`P2`{.docutils .literal .notranslate}]{.pre} are the values and [`t`{.docutils .literal .notranslate}]{.pre} is within the \[0 to 1\] range.

In the case of linear texture filtering the following formulas are used:

- For one dimensional textures: [`tex(x)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)T[i]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`αT[i+1]`{.docutils .literal .notranslate}]{.pre}

- For two dimensional textures: [`tex(x,y)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)(1-β)T[i,j]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`α(1-β)T[i+1,j]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)βT[i,j+1]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`αβT[i+1,j+1]`{.docutils .literal .notranslate}]{.pre}

- For three dimensional textures: [`tex(x,y,z)`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)(1-β)(1-γ)T[i,j,k]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`α(1-β)(1-γ)T[i+1,j,k]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)β(1-γ)T[i,j+1,k]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`αβ(1-γ)T[i+1,j+1,k]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)(1-β)γT[i,j,k+1]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`α(1-β)γT[i+1,j,k+1]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`(1-α)βγT[i,j+1,k+1]`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`αβγT[i+1,j+1,k+1]`{.docutils .literal .notranslate}]{.pre}

Where x, y, and, z are the floating-point indices. i, j, and, k are the integer indices and, α, β, and, γ values represent how far along the sampled point is on the three axes. These values are calculated by these formulas: [`i`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`floor(x')`{.docutils .literal .notranslate}]{.pre}, [`α`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`frac(x')`{.docutils .literal .notranslate}]{.pre}, [`x'`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`x`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0.5`{.docutils .literal .notranslate}]{.pre}, [`j`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`floor(y')`{.docutils .literal .notranslate}]{.pre}, [`β`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`frac(y')`{.docutils .literal .notranslate}]{.pre}, [`y'`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`y`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0.5`{.docutils .literal .notranslate}]{.pre}, [`k`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`floor(z')`{.docutils .literal .notranslate}]{.pre}, [`γ`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`frac(z')`{.docutils .literal .notranslate}]{.pre} and [`z'`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`=`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`z`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`0.5`{.docutils .literal .notranslate}]{.pre}

The following image shows a texture stretched out to a 4x4 pixel quad, but still indexed in the \[0 to 1\] range. The in-between values are interpolated between the neighboring texels.

<figure id="id6" class="align-center">
<a href="../../../../_images/linear.png" class="reference internal image-reference"><img src="../../../../_images/linear.png" style="width: 300px;" alt="Texture upscaled with linear filtering" /></a>
<figcaption><p><span class="caption-text">Texture upscaled with linear filtering</span><a href="#id6" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

::

::::
{#texture-addressing .section}
[]{#id3}

## Texture addressing[\#](#texture-addressing "Link to this heading"){.headerlink}

The texture addressing modes are specified in [`hipTextureAddressMode`{.xref .cpp .cpp-enumerator .docutils .literal .notranslate}]{.pre}.

The texture addressing mode handles out-of-bounds accesses to the texture. This can be used in graphics applications to e.g. repeat a texture on a surface multiple times in various ways or create visible signs of out-of-bounds indexing.

The following sections describe the various texture addressing methods.

{#address-mode-border .section}
[]{#texture-fetching-border}

### Address mode border[\#](#address-mode-border "Link to this heading"){.headerlink}

This addressing mode is set using [`hipAddressModeBorder`{.docutils .literal .notranslate}]{.pre}.

This addressing mode returns a border value when indexing out of bounds. The border value must be set before texture fetching.

The following image shows the texture on a 4x4 pixel quad, indexed in the \[0 to 3\] range. The out-of-bounds values are the border color, which is yellow.

<figure id="id7" class="align-center">
<a href="../../../../_images/border.png" class="reference internal image-reference"><img src="../../../../_images/border.png" style="width: 300px;" alt="Texture with yellow border color" /></a>
<figcaption><p><span class="caption-text">Texture with yellow border color.</span><a href="#id7" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The purple lines are not part of the texture. They only denote the edge, where the addressing begins.

{#address-mode-clamp .section}
[]{#texture-fetching-clamp}

### Address mode clamp[\#](#address-mode-clamp "Link to this heading"){.headerlink}

This addressing mode is set using [`hipAddressModeClamp`{.docutils .literal .notranslate}]{.pre}.

This mode clamps the index between \[0 to size-1\]. Due to this, when indexing out-of-bounds, the values on the edge of the texture repeat. The clamp mode is the default addressing mode.

The following image shows the texture on a 4x4 pixel quad, indexed in the \[0 to 3\] range. The out-of-bounds values are repeating the values at the edge of the texture.

<figure id="id8" class="align-center">
<a href="../../../../_images/clamp.png" class="reference internal image-reference"><img src="../../../../_images/clamp.png" style="width: 300px;" alt="Texture with clamp addressing" /></a>
<figcaption><p><span class="caption-text">Texture with clamp addressing</span><a href="#id8" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The purple lines are not part of the texture. They only denote the edge, where the addressing begins.

{#address-mode-wrap .section}
[]{#texture-fetching-wrap}

### Address mode wrap[\#](#address-mode-wrap "Link to this heading"){.headerlink}

This addressing mode is set using [`hipAddressModeWrap`{.docutils .literal .notranslate}]{.pre}.

Wrap mode addressing is only available for normalized texture coordinates. In this addressing mode, the fractional part of the index is used:

[`tex(frac(x))`{.docutils .literal .notranslate}]{.pre}

This creates a repeating image effect.

The following image shows the texture on a 4x4 pixel quad, indexed in the \[0 to 3\] range. The out-of-bounds values are repeating the original texture.

<figure id="id9" class="align-center">
<a href="../../../../_images/wrap.png" class="reference internal image-reference"><img src="../../../../_images/wrap.png" style="width: 300px;" alt="Texture with wrap addressing" /></a>
<figcaption><p><span class="caption-text">Texture with wrap addressing.</span><a href="#id9" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The purple lines are not part of the texture. They only denote the edge, where the addressing begins.

{#address-mode-mirror .section}
[]{#texture-fetching-mirror}

### Address mode mirror[\#](#address-mode-mirror "Link to this heading"){.headerlink}

This addressing mode is set using [`hipAddressModeMirror`{.docutils .literal .notranslate}]{.pre}.

Similar to the wrap mode the mirror mode is only available for normalized texture coordinates and also creates a repeating image, but mirroring the neighboring instances.

The formula is the following:

[`tex(frac(x))`{.docutils .literal .notranslate}]{.pre}, if [`floor(x)`{.docutils .literal .notranslate}]{.pre} is even,

[`tex(1`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`-`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`frac(x))`{.docutils .literal .notranslate}]{.pre}, if [`floor(x)`{.docutils .literal .notranslate}]{.pre} is odd.

The following image shows the texture on a 4x4 pixel quad, indexed in The \[0 to 3\] range. The out-of-bounds values are repeating the original texture, but mirrored.

<figure id="id10" class="align-center">
<a href="../../../../_images/mirror.png" class="reference internal image-reference"><img src="../../../../_images/mirror.png" style="width: 300px;" alt="Texture with mirror addressing" /></a>
<figcaption><p><span class="caption-text">Texture with mirror addressing</span><a href="#id10" class="headerlink" title="Link to this image">#</a></p></figcaption>
</figure>

The purple lines are not part of the texture. They only denote the edge, where the addressing begins.

::::
::::::::
::::::::::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::::::::::
:::::::::::::::::::::::::::::
