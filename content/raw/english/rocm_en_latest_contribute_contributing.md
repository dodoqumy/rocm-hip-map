---
title: "Contributing to the ROCm documentation"
source_url: "https://rocm.docs.amd.com/en/latest/contribute/contributing.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-04-28
---

::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- Contributing\...

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}

# Contributing to the ROCm documentation

## Contents

- [The ROCm repositories](#the-rocm-repositories){.reference .internal .nav-link}
- [Editing and adding to the documentation](#editing-and-adding-to-the-documentation){.reference .internal .nav-link}


# Contributing to the ROCm documentation[\#](#contributing-to-the-rocm-documentation "Link to this heading"){.headerlink}

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time

Applies to Linux and Windows


The ROCm documentation, like all of ROCm, is open source and available on GitHub. You can contribute to the ROCm documentation by forking the appropriate repository, making your changes, and opening a pull request.

To provide feedback on the ROCm documentation, including submitting an issue or suggesting a feature, see [[Providing feedback about the ROCm documentation]{.std .std-doc}](feedback.html){.reference .internal}.

## The ROCm repositories[\#](#the-rocm-repositories "Link to this heading"){.headerlink}

The repositories for ROCm and all ROCm components are available on GitHub.

::: pst-scrollable-table-container
  Module                                  Documentation location
  --------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  ROCm framework                          [ROCm/ROCm](https://github.com/ROCm/ROCm/tree/develop/docs){.github .reference .external}
  ROCm installation for Linux             [ROCm/rocm-install-on-linux](https://github.com/ROCm/rocm-install-on-linux/tree/develop/docs){.github .reference .external}
  ROCm HIP SDK installation for Windows   [ROCm/rocm-install-on-windows](https://github.com/ROCm/rocm-install-on-windows/tree/develop/docs){.github .reference .external}

Individual components have their own repositories with their own documentation in their own [`docs`{.docutils .literal .notranslate}]{.pre} folders.

The sub-folders within the [`docs`{.docutils .literal .notranslate}]{.pre} folders across ROCm are typically structured as follows:

::: pst-scrollable-table-container
  Sub-folder name                                         Documentation type
  ------------------------------------------------------- ------------------------------------------------------------------
  [`install`{.docutils .literal .notranslate}]{.pre}      Installation instructions, build instructions, and prerequisites
  [`conceptual`{.docutils .literal .notranslate}]{.pre}   Important concepts
  [`how-to`{.docutils .literal .notranslate}]{.pre}       How to implement specific use cases
  [`tutorials`{.docutils .literal .notranslate}]{.pre}    Tutorials
  [`reference`{.docutils .literal .notranslate}]{.pre}    API references and other reference resources

## Editing and adding to the documentation[\#](#editing-and-adding-to-the-documentation "Link to this heading"){.headerlink}

ROCm documentation follows the [Google developer documentation style guide](https://developers.google.com/style/highlights){.reference .external}.

Most topics in the ROCm documentation are written in [reStructuredText (rst)](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html){.reference .external}, with some topics written in Markdown. Only use reStructuredText when adding new topics. Only use Markdown if the topic you are editing is already in Markdown.

To edit or add to the documentation:

1.  Fork the repository you want to add to or edit.

2.  Clone your fork locally.

3.  Create a new local branch cut from the [`develop`{.docutils .literal .notranslate}]{.pre} branch of the repository.

4.  Make your changes to the documentation.

5.  Optionally, build the documentation locally before creating a pull request by running the following commands from within the [`docs`{.docutils .literal .notranslate}]{.pre} folder:

    ::: highlight
         pip3 install -r sphinx/requirements.txt  # You only need to run this command once
         python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html

    The output files will be located in the [`docs/_build`{.docutils .literal .notranslate}]{.pre} folder. Open [`docs/_build/html/index.html`{.docutils .literal .notranslate}]{.pre} to view the documentation.

    For more information on ROCm build tools, see [[Documentation toolchain]{.std .std-doc}](toolchain.html){.reference .internal}.

6.  Push your changes. A GitHub link will be returned in the output of the [`git`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`push`{.docutils .literal .notranslate}]{.pre} command. Open this link in a browser to create the pull request.

    The documentation is built as part of the checks on pull request, along with spell checking and linting. Scroll to the bottom of your pull request to view all the checks.

    Verify that the linting and spell checking have passed, and that the documentation was built successfully. New words or acronyms can be added to the [wordlist file](https://github.com/ROCm/rocm-docs-core/blob/develop/.wordlist.txt){.reference .external}. The wordlist is subject to approval by the ROCm documentation team.

    The Read The Docs build of your pull request can be accessed by clicking on the Details link next to the Read The Docs build check. Verify that your changes are in the build and look as expected.

    ![The GitHub checks are collapsed by default and can be accessed by clicking on \"Show All Checks\".](../_images/GitHubCheck-Highlight.png)

    ![The Read The Docs Build is accessed from the Details link in the Read The Docs check.](../_images/GitHub-ReadThe-Docs-Highlight.png)

    Your pull request will be reviewed by a member of the ROCm documentation team.

See the [GitHub documentation](https://docs.github.com/en){.reference .external} for information on how to fork and clone a repository, and how to create and push a local branch.

Important

By creating a pull request (PR), you agree to allow your contribution to be licensed under the terms of the LICENSE.txt file in the corresponding repository. Different repositories can use different licenses.


::::: prev-next-area
[](../reference/glossary/performance.html "previous page"){.left-prev}

::: prev-next-info
previous

Performance analysis glossary

[](toolchain.html "next page"){.right-next}

::: prev-next-info
next

ROCm documentation toolchain

:::: sidebar-secondary-item
Contents

- [The ROCm repositories](#the-rocm-repositories){.reference .internal .nav-link}
- [Editing and adding to the documentation](#editing-and-adding-to-the-documentation){.reference .internal .nav-link}
