---
title: "Surface object &#8212; HIP 7.2.53211 Documentation"
source_url: "https://rocm.docs.amd.com/projects/HIP/en/latest/reference/hip_runtime_api/modules/memory_management/surface_object.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-01T06:58:45.766307+00:00
content_hash: "71fe617479f6c74f"
---

:::::::::::::::::::::
{#main-content .bd-main role="main"}

sbt-scroll-pixel-helper

:::::::::::::::::::
bd-content
::::::::::::::
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
# Surface object

::
{#print-main-content}
:
{#jb-print-toc}

{}
## Contents

:
::

{#searchbox}

{#surface-object .section}
[]{#surface-object-reference}

# Surface object[\#](#surface-object "Link to this heading"){.headerlink}

[]{#_CPPv322hipCreateSurfaceObjectP18hipSurfaceObject_tPK15hipResourceDesc}[]{#_CPPv222hipCreateSurfaceObjectP18hipSurfaceObject_tPK15hipResourceDesc}[]{#hipCreateSurfaceObject__hipSurfaceObject_tP.hipResourceDescCP}[]{#group___surface_1gaa06a02200e471cedeed33b9d326e9dd6 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipCreateSurfaceObject]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pSurfObject]{.pre}]{.n .sig-param}, [[const]{.pre}]{.k}[ ]{.w}[[hipResourceDesc]{.pre}]{.n}[ ]{.w}[[\*]{.pre}]{.p}[[pResDesc]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv422hipCreateSurfaceObjectP18hipSurfaceObject_tPK15hipResourceDesc "Link to this definition"){.headerlink}\

:   Create a surface object.

    Parameters[:]{.colon}

    :   - **pSurfObject** -- **\[out\]** Pointer of surface object to be created.

        - **pResDesc** -- **\[in\]** Pointer of suface object descriptor.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv323hipDestroySurfaceObject18hipSurfaceObject_t}[]{#_CPPv223hipDestroySurfaceObject18hipSurfaceObject_t}[]{#hipDestroySurfaceObject__hipSurfaceObject_t}[]{#group___surface_1ga1cbf692fdb56b251d7b6d4e4d3bb2006 .target}[[hipError_t]{.pre}]{.n}[ ]{.w}[[[hipDestroySurfaceObject]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfaceObject]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv423hipDestroySurfaceObject18hipSurfaceObject_t "Link to this definition"){.headerlink}\

:   Destroy a surface object.

    Parameters[:]{.colon}

    :   **surfaceObject** -- **\[in\]** Surface object to be destroyed.

    Returns[:]{.colon}

    :   hipSuccess, hipErrorInvalidValue

<!-- -->

[]{#_CPPv317__hipGetPixelAddriii}[]{#_CPPv217__hipGetPixelAddriii}[]{#__hipGetPixelAddr__i.i.i}[]{#group___surface_a_p_i_1ga2689f43c7e1e989ee71f3674427ffde0 .target}[[static]{.pre}]{.k}[ ]{.w}[[int]{.pre}]{.kt}[ ]{.w}[[[\_\_hipGetPixelAddr]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[format]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[order]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv417__hipGetPixelAddriii "Link to this definition"){.headerlink}\

:   

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf1DreadP1T18hipSurfaceObject_tii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf1DreadP1T18hipSurfaceObject_tii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf1DreadvP1T18hipSurfaceObject_tii "surf1Dread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga4b890cdbf551d99adbe2f81def4574c8 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf1Dread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf1DreadvP1T18hipSurfaceObject_tii "surf1Dread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[boundaryMode]{.pre}]{.n .sig-param}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[hipBoundaryModeZero]{.pre}]{.n}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf1DreadvP1T18hipSurfaceObject_tii "Link to this definition"){.headerlink}\

:   Reads the value at coordinate x from the one-dimensional surface.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The coordinate where the value will be read out.

        - **boundaryMode** -- \[in\] The boundary mode is currently ignored.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf1Dwrite1T18hipSurfaceObject_ti}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf1Dwrite1T18hipSurfaceObject_ti}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf1Dwritev1T18hipSurfaceObject_ti "surf1Dwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga71ffc707653b48367be03e4ef808166e .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf1Dwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf1Dwritev1T18hipSurfaceObject_ti "surf1Dwrite::T"){.reference .internal}[ ]{.w}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf1Dwritev1T18hipSurfaceObject_ti "Link to this definition"){.headerlink}\

:   Writes the value data to the one-dimensional surface at coordinate x.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value is written to surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The coordinate where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf2DreadP1T18hipSurfaceObject_tii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf2DreadP1T18hipSurfaceObject_tii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf2DreadvP1T18hipSurfaceObject_tii "surf2Dread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gaeed6a25aec334e01b37a15441f6ea744 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf2Dread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf2DreadvP1T18hipSurfaceObject_tii "surf2Dread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf2DreadvP1T18hipSurfaceObject_tii "Link to this definition"){.headerlink}\

:   Reads the value from the two-dimensional surface at coordinate x, y.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the value will be read out.

        - **y** -- \[in\] The y coordinate where the value will be read out.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf2Dwrite1T18hipSurfaceObject_tii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf2Dwrite1T18hipSurfaceObject_tii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf2Dwritev1T18hipSurfaceObject_tii "surf2Dwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gab487fad96cb4b10ddccc63936dc18be7 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf2Dwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf2Dwritev1T18hipSurfaceObject_tii "surf2Dwrite::T"){.reference .internal}[ ]{.w}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf2Dwritev1T18hipSurfaceObject_tii "Link to this definition"){.headerlink}\

:   Writes the value data to the two-dimensional surface at coordinate x, y.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value is written to surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the data will be written.

        - **y** -- \[in\] The y coordinate where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf3DreadP1T18hipSurfaceObject_tiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf3DreadP1T18hipSurfaceObject_tiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf3DreadvP1T18hipSurfaceObject_tiii "surf3Dread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga77e15ee6530c1f245d63f6bfc15ba06f .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf3Dread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf3DreadvP1T18hipSurfaceObject_tiii "surf3Dread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[z]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE10surf3DreadvP1T18hipSurfaceObject_tiii "Link to this definition"){.headerlink}\

:   Reads the value from the three-dimensional surface at coordinate x, y, z.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the value will be read out.

        - **y** -- \[in\] The y coordinate where the value will be read out.

        - **z** -- \[in\] The z coordinate where the value will be read out.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf3Dwrite1T18hipSurfaceObject_tiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf3Dwrite1T18hipSurfaceObject_tiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf3Dwritev1T18hipSurfaceObject_tiii "surf3Dwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga6d6366f33fe3b4233f1ecbc45f7d6093 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf3Dwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf3Dwritev1T18hipSurfaceObject_tiii "surf3Dwrite::T"){.reference .internal}[ ]{.w}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[z]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE11surf3Dwritev1T18hipSurfaceObject_tiii "Link to this definition"){.headerlink}\

:   Writes the value data to the three-dimensional surface at coordinate x, y, z.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value is written to surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the data will be written.

        - **y** -- \[in\] The y coordinate where the data will be written.

        - **z** -- \[in\] The z coordinate where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf1DLayeredreadP1T18hipSurfaceObject_tii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf1DLayeredreadP1T18hipSurfaceObject_tii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf1DLayeredreadvP1T18hipSurfaceObject_tii "surf1DLayeredread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gafe82d517f355be44d00feb7754db2b3f .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf1DLayeredread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf1DLayeredreadvP1T18hipSurfaceObject_tii "surf1DLayeredread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[layer]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf1DLayeredreadvP1T18hipSurfaceObject_tii "Link to this definition"){.headerlink}\

:   Reads the value from the one-dimensional layered surface at coordinate x and layer index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The coordinate where the value will be read out.

        - **layer** -- \[in\] The layer index where the value will be read out.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf1DLayeredwrite1T18hipSurfaceObject_tii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf1DLayeredwrite1T18hipSurfaceObject_tii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf1DLayeredwritev1T18hipSurfaceObject_tii "surf1DLayeredwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga9def9bd1898baa84b4cb5810443a26b0 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf1DLayeredwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf1DLayeredwritev1T18hipSurfaceObject_tii "surf1DLayeredwrite::T"){.reference .internal}[ ]{.w}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[layer]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf1DLayeredwritev1T18hipSurfaceObject_tii "Link to this definition"){.headerlink}\

:   Writes the value data to the one-dimensional layered surface at coordinate x and layer index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value is written to surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the data will be written.

        - **layer** -- \[in\] The layer index where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf2DLayeredreadP1T18hipSurfaceObject_tiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf2DLayeredreadP1T18hipSurfaceObject_tiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf2DLayeredreadvP1T18hipSurfaceObject_tiii "surf2DLayeredread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gac2f9651c32dac134af7260328b628a16 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf2DLayeredread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf2DLayeredreadvP1T18hipSurfaceObject_tiii "surf2DLayeredread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[layer]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE17surf2DLayeredreadvP1T18hipSurfaceObject_tiii "Link to this definition"){.headerlink}\

:   Reads the value from the two-dimensional layered surface at coordinate x, y and layer index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the value will be read out.

        - **y** -- \[in\] The y coordinate where the value will be read out.

        - **layer** -- \[in\] The layer index where the value will be read out.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf2DLayeredwrite1T18hipSurfaceObject_tiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf2DLayeredwrite1T18hipSurfaceObject_tiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf2DLayeredwritev1T18hipSurfaceObject_tiii "surf2DLayeredwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga967d573c584972a226b7126c051c3bb7 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surf2DLayeredwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf2DLayeredwritev1T18hipSurfaceObject_tiii "surf2DLayeredwrite::T"){.reference .internal}[ ]{.w}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[layer]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE18surf2DLayeredwritev1T18hipSurfaceObject_tiii "Link to this definition"){.headerlink}\

:   Writes the value data to the two-dimensional layered surface at coordinate x, y and layer index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value is written to surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the data will be written.

        - **y** -- \[in\] The y coordinate where the data will be written.

        - **layer** -- \[in\] The layer index where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE15surfCubemapreadP1T18hipSurfaceObject_tiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE15surfCubemapreadP1T18hipSurfaceObject_tiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE15surfCubemapreadvP1T18hipSurfaceObject_tiii "surfCubemapread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1ga6fade4bc2ea7fc3d32f1f9c63180e270 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surfCubemapread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE15surfCubemapreadvP1T18hipSurfaceObject_tiii "surfCubemapread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[face]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE15surfCubemapreadvP1T18hipSurfaceObject_tiii "Link to this definition"){.headerlink}\

:   Reads the value from the cubemap surface at coordinate x, y and face index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the value will be read out.

        - **y** -- \[in\] The y coordinate where the value will be read out.

        - **face** -- \[in\] The face index where the value will be read out.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE16surfCubemapwrite1T18hipSurfaceObject_tiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE16surfCubemapwrite1T18hipSurfaceObject_tiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE16surfCubemapwritev1T18hipSurfaceObject_tiii "surfCubemapwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gaa658108399460ac8c410191f2f7f1249 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surfCubemapwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE16surfCubemapwritev1T18hipSurfaceObject_tiii "surfCubemapwrite::T"){.reference .internal}[ ]{.w}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[face]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE16surfCubemapwritev1T18hipSurfaceObject_tiii "Link to this definition"){.headerlink}\

:   Writes the value data to the cubemap surface at coordinate x, y and face index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value is written to surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the data will be written.

        - **y** -- \[in\] The y coordinate where the data will be written.

        - **face** -- \[in\] The face index where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE22surfCubemapLayeredreadP1T18hipSurfaceObject_tiiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE22surfCubemapLayeredreadP1T18hipSurfaceObject_tiiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE22surfCubemapLayeredreadvP1T18hipSurfaceObject_tiiii "surfCubemapLayeredread::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gac1c2ddbad403533c0783cc0cc58126c9 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surfCubemapLayeredread]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE22surfCubemapLayeredreadvP1T18hipSurfaceObject_tiiii "surfCubemapLayeredread::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[face]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[layer]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE22surfCubemapLayeredreadvP1T18hipSurfaceObject_tiiii "Link to this definition"){.headerlink}\

:   Reads the value from the layered cubemap surface at coordinate x, y and face, layer index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[out\] The T type result is stored in this pointer.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the value will be read out.

        - **y** -- \[in\] The y coordinate where the value will be read out.

        - **face** -- \[in\] The face index where the value will be read out.

        - **layer** -- \[in\] The layer index where the data will be written.

<!-- -->

[]{#_CPPv3I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE23surfCubemapLayeredwriteP1T18hipSurfaceObject_tiiii}[]{#_CPPv2I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE23surfCubemapLayeredwriteP1T18hipSurfaceObject_tiiii}[[template]{.pre}]{.k}[[\<]{.pre}]{.p}[[typename]{.pre}]{.k}[ ]{.w}[[[T]{.pre}]{.n}]{.sig-name .descname}[[,]{.pre}]{.p}[ ]{.w}[[typename]{.pre}]{.k}[ ]{.w}[[\_\_hip_internal]{.pre}]{.n}[[::]{.pre}]{.p}[[enable_if]{.pre}]{.n}[[\<]{.pre}]{.p}[[\_\_hip_is_tex_surf_channel_type]{.pre}]{.n}[[\<]{.pre}]{.p}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE23surfCubemapLayeredwritevP1T18hipSurfaceObject_tiiii "surfCubemapLayeredwrite::T"){.reference .internal}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[value]{.pre}]{.n}[[\>]{.pre}]{.p}[[::]{.pre}]{.p}[[type]{.pre}]{.n}[[\*]{.pre}]{.p}[ ]{.w}[[=]{.pre}]{.p}[ ]{.w}[[nullptr]{.pre}]{.k}[[\>]{.pre}]{.p}\
[]{#group___surface_a_p_i_1gaac0abad521879a6db626bd0d804e7a49 .target}[[static]{.pre}]{.k}[ ]{.w}[[void]{.pre}]{.kt}[ ]{.w}[[[surfCubemapLayeredwrite]{.pre}]{.n}]{.sig-name .descname}[(]{.sig-paren}[[[T]{.pre}]{.n}](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE23surfCubemapLayeredwritevP1T18hipSurfaceObject_tiiii "surfCubemapLayeredwrite::T"){.reference .internal}[ ]{.w}[[\*]{.pre}]{.p}[[data]{.pre}]{.n .sig-param}, [[hipSurfaceObject_t]{.pre}]{.n}[ ]{.w}[[surfObj]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[x]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[y]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[face]{.pre}]{.n .sig-param}, [[int]{.pre}]{.kt}[ ]{.w}[[layer]{.pre}]{.n .sig-param}[)]{.sig-paren}[\#](#_CPPv4I0_PN14__hip_internal9enable_ifIN30__hip_is_tex_surf_channel_typeI1TE5valueEE4typeEE23surfCubemapLayeredwritevP1T18hipSurfaceObject_tiiii "Link to this definition"){.headerlink}\

:   Writes the value data to the layered cubemap surface at coordinate x, y and face, layer index.

    Template Parameters[:]{.colon}

    :   **T** -- The data type of the surface.

    Parameters[:]{.colon}

    :   - **data** -- \[in\] The T type value to write to the surface.

        - **surfObj** -- \[in\] The surface descriptor.

        - **x** -- \[in\] The x coordinate where the data will be written.

        - **y** -- \[in\] The y coordinate where the data will be written.

        - **face** -- \[in\] The face index where the data will be written.

        - **layer** -- \[in\] The layer index where the data will be written.

::::::::::::::

{.bd-sidebar-secondary .bd-toc}
::
{.sidebar-secondary-items .sidebar-secondary__inner}
:
sidebar-secondary-item

{.page-toc .tocsection .onthispage}
Contents

:
::

:::::::::::::::::::
:::::::::::::::::::::
