---
title: "Contributing to ROCm documentation"
source_url: "https://rocm.docs.amd.com/en/docs-6.0.0/contribute/contribute-docs.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T16:10:42.686852+00:00
content_hash: "5245db22c6c72d65"
---

# Contributing to ROCm documentation[#](#contributing-to-rocm-documentation)



AMD values and encourages contributions to our code and documentation. If you choose to contribute, we encourage you to be polite and respectful. Improving documentation is a long-term process, to which we are dedicated.

If you have issues when trying to contribute, refer to the
[discussions](https://github.com/RadeonOpenCompute/ROCm/discussions) page in our GitHub
repository.

## Folder structure and naming convention[#](#folder-structure-and-naming-convention)

Our documentation follows the Pitchfork folder structure. Most documentation files are stored in the
`/docs`

folder. Some special files (such as release, contributing, and changelog) are stored in the root
(`/`

) folder.

All images are stored in the `/docs/data`

folder. An image’s file path mirrors that of the documentation
file where it is used.

Our naming structure uses kebab case; for example, `my-file-name.rst`

.

## Supported formats and syntax[#](#supported-formats-and-syntax)

Our documentation includes both Markdown and RST files. We are gradually transitioning existing Markdown to RST in order to more effectively meet our documentation needs. When contributing, RST is preferred; if you must use Markdown, use GitHub-flavored Markdown.

We use [Sphinx Design](https://sphinx-design.readthedocs.io/en/latest/index.html) syntax and compile
our API references using [Doxygen](https://www.doxygen.nl/).

The following table shows some common documentation components and the syntax convention we use for each:

| Component | RST syntax |
|---|---|
| Code blocks |
```
.. code-block:: language-name
My code block.
``` |
| Cross-referencing internal files |
```
:doc:`Title <../path/to/file/filename>`
``` |
| External links |
```
`link name <URL>`_
``` |
| Headings |
```
******************
Chapter title (H1)
******************
Section title (H2)
===============
Subsection title (H3)
---------------------
Sub-subsection title (H4)
^^^^^^^^^^^^^^^^^^^^
``` |
| Images |
```
.. image:: image1.png
``` |
| Internal links |
```
1. Add a tag to the section you want to reference:
.. _my-section-tag: section-1
Section 1
==========
2. Link to your tag:
As shown in :ref:`section-1`.
``` |
| Lists |
```
* Unordered (bulleted) list item
``` |
| Math (block) |
```
.. math::
A = \begin{pmatrix}
0.0 & 1.0 & 1.0 & 3.0 \\
4.0 & 5.0 & 6.0 & 7.0 \\
\end{pmatrix}
``` |
| Math (inline) |
```
:math:`2 \times 2 `
``` |
| Notes |
```
.. note::
My note here.
``` |
| Tables |
```
.. csv-table:: Optional title here
:widths: 30, 70 #optional column widths
:header: "entry1 header", "entry2 header"
"entry1", "entry2"
``` |

## Language and style[#](#language-and-style)

We use the
[Google developer documentation style guide](https://developers.google.com/style/highlights) to
guide our content.

Font size and type, page layout, white space control, and other formatting
details are controlled via
[rocm-docs-core](https://github.com/RadeonOpenCompute/rocm-docs-core). If you want to notify us
of any formatting issues, create a pull request in our
[rocm-docs-core](https://github.com/RadeonOpenCompute/rocm-docs-core) GitHub repository.

## Building our documentation[#](#building-our-documentation)

To learn how to build our documentation, refer to
[Building documentation](building.html).
