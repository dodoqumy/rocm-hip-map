---
title: "Building documentation"
source_url: "https://rocm.docs.amd.com/en/latest/contribute/building.html"
source_type: "official"
source_org: "amd"
original_lang: "en"
credibility: 5
lifecycle: "latest"
synced_date: 2026-05-03
---

:::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
::::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-angle-right}
:::

::: header-article-item
- [](../index.html){.nav-link aria-label="Home"}
- [Contributing to the ROCm documentation](contributing.html){.nav-link}
- Building\...
:::
:::::

::::: header-article-items__end
:::: header-article-item
::: article-header-buttons
[]{.fa-solid .fa-list}
:::
::::
:::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Building documentation

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [GitHub](#github){.reference .internal .nav-link}
- [Command line](#command-line){.reference .internal .nav-link}
- [Visual Studio Code](#visual-studio-code){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::: {#building-documentation .section .tex2jax_ignore .mathjax_ignore}
# Building documentation[\#](#building-documentation "Link to this heading"){.headerlink}

::::::::::: {#rocm-docs-core-article-info .sd-container-fluid .sd-sphinx-override .sd-p-0 .sd-mt-2 .sd-mb-4 .sd-p-2 .sd-rounded-1 .docutils}
:::::::::: {.sd-row .sd-row-cols-2 .sd-gx-2 .sd-gy-1 .docutils}
::::::::: {.sd-col .sd-d-flex-row .sd-align-minor-center .docutils}
:::::::: {.sd-container-fluid .sd-sphinx-override .docutils}
::::::: {.sd-row .sd-row-cols-2 .sd-row-cols-xs-2 .sd-row-cols-sm-3 .sd-row-cols-md-3 .sd-row-cols-lg-3 .sd-gx-3 .sd-gy-1 .docutils}
::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 min read time
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils style="color:gray;"}
Applies to Linux and Windows
:::

::: {.sd-col .sd-col-auto .sd-d-flex-row .sd-align-minor-center .docutils}
:::
:::::::
::::::::
:::::::::
::::::::::
:::::::::::

::: {#github .section}
## GitHub[\#](#github "Link to this heading"){.headerlink}

If you open a pull request and scroll down to the summary panel, there is a commit status section. Next to the line [`docs/readthedocs.com:advanced-micro-devices-demo`{.docutils .literal .notranslate}]{.pre}, there is a [`Details`{.docutils .literal .notranslate}]{.pre} link. If you click this, it takes you to the Read the Docs build for your pull request.

![GitHub PR commit status](../_images/commit-status.png)

If you don't see this line, click [`Show`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`all`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`checks`{.docutils .literal .notranslate}]{.pre} to get an itemized view.
:::

:::::::::: {#command-line .section}
## Command line[\#](#command-line "Link to this heading"){.headerlink}

You can build our documentation via the command line using Python.

See the [`build.tools.python`{.docutils .literal .notranslate}]{.pre} setting in the [Read the Docs configuration file](https://github.com/ROCm/ROCm/blob/develop/.readthedocs.yaml){.reference .external} for the Python version used by Read the Docs to build documentation.

See the [Python requirements file](https://github.com/ROCm/ROCm/blob/develop/docs/sphinx/requirements.txt){.reference .external} for Python packages needed to build the documentation.

Use the Python Virtual Environment ([`venv`{.docutils .literal .notranslate}]{.pre}) and run the following commands from the project root:

::::::::: {.sd-tab-set .docutils}
Linux and WSL

::::: {.sd-tab-content .docutils}
:::: {.highlight-sh .notranslate}
::: highlight
    python3 -mvenv .venv

    .venv/bin/python -m pip install -r docs/sphinx/requirements.txt
    .venv/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
:::
::::
:::::

Windows

::::: {.sd-tab-content .docutils}
:::: {.highlight-powershell .notranslate}
::: highlight
    python -mvenv .venv

    .venv\Scripts\python.exe -m pip install -r docs/sphinx/requirements.txt
    .venv\Scripts\python.exe -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html
:::
::::
:::::
:::::::::

Navigate to [`_build/html/index.html`{.docutils .literal .notranslate}]{.pre} and open this file in a web browser.
::::::::::

::: {#visual-studio-code .section}
## Visual Studio Code[\#](#visual-studio-code "Link to this heading"){.headerlink}

With the help of a few extensions, you can create a productive environment to author and test documentation locally using Visual Studio (VS) Code. Follow these steps to configure VS Code:

1.  Install the required extensions:

    - Python: [`(ms-python.python)`{.docutils .literal .notranslate}]{.pre}

    - Live Server: [`(ritwickdey.LiveServer)`{.docutils .literal .notranslate}]{.pre}

2.  Add the following entries to [`.vscode/settings.json`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-json .notranslate}
    ::: highlight
          {
            "liveServer.settings.root": "/.vscode/build/html",
            "liveServer.settings.wait": 1000,
            "python.terminal.activateEnvInCurrentTerminal": true
          }
    :::
    ::::

    - [`liveServer.settings.root`{.docutils .literal .notranslate}]{.pre}: Sets the root of the output website for live previews. Must be changed alongside the [`tasks.json`{.docutils .literal .notranslate}]{.pre} command.

    - [`liveServer.settings.wait`{.docutils .literal .notranslate}]{.pre}: Tells the live server to wait with the update in order to give Sphinx time to regenerate the site contents and not refresh before the build is complete.

    - [`python.terminal.activateEnvInCurrentTerminal`{.docutils .literal .notranslate}]{.pre}: Activates the automatic virtual environment, so you can build the site from the integrated terminal.

3.  Add the following tasks to [`.vscode/tasks.json`{.docutils .literal .notranslate}]{.pre}.

    :::: {.highlight-json .notranslate}
    ::: highlight
          {
            "version": "2.0.0",
            "tasks": [
              {
                "label": "Build Docs",
                "type": "process",
                "windows": {
                  "command": "${workspaceFolder}/.venv/Scripts/python.exe"
                },
                "command": "${workspaceFolder}/.venv/bin/python3",
                "args": [
                  "-m",
                  "sphinx",
                  "-j",
                  "auto",
                  "-T",
                  "-b",
                  "html",
                  "-d",
                  "${workspaceFolder}/.vscode/build/doctrees",
                  "-D",
                  "language=en",
                  "${workspaceFolder}/docs",
                  "${workspaceFolder}/.vscode/build/html"
                ],
                "problemMatcher": [
                  {
                    "owner": "sphinx",
                    "fileLocation": "absolute",
                    "pattern": {
                      "regexp": "^(?:.*\\.{3}\\s+)?(\\/[^:]*|[a-zA-Z]:\\\\[^:]*):(\\d+):\\s+(WARNING|ERROR):\\s+(.*)$",
                      "file": 1,
                      "line": 2,
                      "severity": 3,
                      "message": 4
                    }
                  },
                  {
                  "owner": "sphinx",
                    "fileLocation": "absolute",
                    "pattern": {
                      "regexp": "^(?:.*\\.{3}\\s+)?(\\/[^:]*|[a-zA-Z]:\\\\[^:]*):{1,2}\\s+(WARNING|ERROR):\\s+(.*)$",
                      "file": 1,
                      "severity": 2,
                      "message": 3
                    }
                  }
                ],
                "group": {
                  "kind": "build",
                  "isDefault": true
                }
              }
            ]
          }
    :::
    ::::

    > ::: {}
    > Implementation detail: two problem matchers were needed to be defined, because VS Code doesn't tolerate some problem information being potentially absent. While a single regex could match all types of errors, if a capture group remains empty (the line number doesn't show up in all warning/error messages) but the [`pattern`{.docutils .literal .notranslate}]{.pre} references said empty capture group, VS Code discards the message completely.
    > :::

4.  Configure the Python virtual environment ([`venv`{.docutils .literal .notranslate}]{.pre}).

    From the Command Palette, run [`Python:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Create`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Environment`{.docutils .literal .notranslate}]{.pre}. Select [`venv`{.docutils .literal .notranslate}]{.pre} environment and [`docs/sphinx/requirements.txt`{.docutils .literal .notranslate}]{.pre}.

5.  Build the docs.

    Launch the default build task using one of the following options:

    - A hotkey (the default is [`Ctrl+Shift+B`{.docutils .literal .notranslate}]{.pre})

    - Issuing the [`Tasks:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Run`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Task`{.docutils .literal .notranslate}]{.pre} from the Command Palette

6.  Open the live preview.

    Navigate to the site output within VS Code: right-click on [`.vscode/build/html/index.html`{.docutils .literal .notranslate}]{.pre} and select [`Open`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`with`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Live`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Server`{.docutils .literal .notranslate}]{.pre}. The contents should update on every rebuild without having to refresh the browser.
:::
::::::::::::::::::::::

::::: prev-next-area
[](toolchain.html "previous page"){.left-prev}

::: prev-next-info
previous

ROCm documentation toolchain
:::

[](feedback.html "next page"){.right-next}

::: prev-next-info
next

Providing feedback about the ROCm documentation
:::
:::::
:::::::::::::::::::::::::::::::::::::::

:::::: {.bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {.page-toc .tocsection .onthispage}
Contents
:::

- [GitHub](#github){.reference .internal .nav-link}
- [Command line](#command-line){.reference .internal .nav-link}
- [Visual Studio Code](#visual-studio-code){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::
