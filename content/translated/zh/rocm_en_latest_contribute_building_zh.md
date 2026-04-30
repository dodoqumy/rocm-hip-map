---
title: "Building documentation"
source_url: "https://rocm.docs.amd.com/en/latest/contribute/building.html"
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
- [](../index.html){.nav-link aria-label="首页"}
- [贡献 ROCm 文档](contributing.html){.nav-link}
- 构建中...

这些都是 CSS 类名和技术标识符，属于前端代码，不属于需要翻译的内容。CSS 类名（如 `header-article-items__end`、`header-article-item`、`article-header-buttons`）以及Font Awesome图标的CSS选择器（如 `.fa-solid .fa-list`）应当保持原样不变。

如果您有其他需要翻译的实际文章内容，请提供。

# 构建文档

## 目录

- [GitHub](#github){.reference .internal .nav-link}
- [命令行](#command-line){.reference .internal .nav-link}
- [Visual Studio Code](#visual-studio-code){.reference .internal .nav-link}



# 构建文档

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jYWxlbmRhciIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTQuNzUgMGEuNzUuNzUgMCAwMS43NS43NVYyaDVWLjc1YS43NS43NSAwIDAxMS41IDBWMmgxLjI1Yy45NjYgMCAxLjc1Ljc4NCAxLjc1IDEuNzV2MTAuNUExLjc1IDEuNzUgMCAwMTEzLjI1IDE2SDIuNzVBMS43NSAxLjc1IDAgMDExIDE0LjI1VjMuNzVDMSAyLjc4NCAxLjc4NCAyIDIuNzUgMkg0Vi43NUEuNzUuNzUgMCAwMTQuNzUgMHptMCAzLjVoOC41YS4yNS4yNSAwIDAxLjI1LjI1VjZoLTExVjMuNzVhLjI1LjI1IDAgMDEuMjUtLjI1aDJ6bS0yLjI1IDR2Ni43NWMwIC4xMzguMTEyLjI1LjI1aDEwLjVhLjI1LjI1IDAgMDAuMjUtLjI1VjcuNWgtMTF6IiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIC8+Cjwvc3ZnPg==){.sd-octicon .sd-octicon-calendar} ]{.sd-pr-2 .article-info-date-svg} 2026-01-23

[ ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InNkLW9jdGljb24gc2Qtb2N0aWNvbi1jbG9jayIgaGVpZ2h0PSIxNi4wcHgiIHZlcnNpb249IjEuMSIgdmlld2JveD0iMCAwIDE2IDE2IiB3aWR0aD0iMTYuMHB4Ij4KPHBhdGggZD0iTTEuNSA4YTYuNSA2LjUgMCAxMTEzIDAgNi41IDYuNSAwIDAxLTEzIDB6TTggMGE4IDggMCAxMDAgMTZBOCA4IDAgMDA4IDB6bS41IDQuNzVhLjc1Ljc1IDAgMDAtMS41IDB2My41YS43NS43NSAwIDAwLjQ3MS42OTZsMi41IDFhLjc1Ljc1IDAgMDAuNTU3LTEuMzkyTDguNSA3Ljc0MlY0Ljc1eiIgZmlsbC1ydWxlPSJldmVub2RkIiAvPgo8L3N2Zz4=){.sd-octicon .sd-octicon-clock} ]{.sd-pr-2 .article-info-read-time-svg} 5 分钟阅读时间

适用于 Linux 和 Windows

## GitHub[\#](#github "链接到此标题"){.headerlink}

如果您打开一个拉取请求并向下滚动到摘要面板，会看到一个提交状态部分。在 [`docs/readthedocs.com:advanced-micro-devices-demo`{.docutils .literal .notranslate}]{.pre} 行的旁边，有一个 [`Details`{.docutils .literal .notranslate}]{.pre} 链接。点击此链接会跳转到您拉取请求的 Read the Docs 构建页面。

![GitHub PR 提交状态](../_images/commit-status.png)

如果您看不到此行，请点击 [`Show`] [` `] [`all`] [` `] [`checks`] 以获取逐项视图。

## 命令行 [#](#command-line "Link to this heading"){.headerlink}

你可以使用 Python 通过命令行构建我们的文档。

请参阅[Read the Docs 配置文件](https://github.com/ROCm/ROCm/blob/develop/.readthedocs.yaml)中的[`build.tools.python`{.docutils .literal .notranslate}]{.pre}设置，以了解 Read the Docs 用于构建文档的 Python 版本。

请参阅 [Python requirements file](https://github.com/ROCm/ROCm/blob/develop/docs/sphinx/requirements.txt){.reference .external} 了解构建文档所需的 Python 包。

使用 Python 虚拟环境 ([`venv`{.docutils .literal .notranslate}]{.pre}) 并在项目根目录下运行以下命令：

Linux 和 WSL

python3 -mvenv .venv



.venv/bin/python -m pip install -r docs/sphinx/requirements.txt
.venv/bin/python -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html

Windows

```python
python -mvenv .venv
```

.venv\Scripts\python.exe -m pip install -r docs/sphinx/requirements.txt
.venv\Scripts\python.exe -m sphinx -T -E -b html -d _build/doctrees -D language=en docs _build/html

导航至 [`_build/html/index.html`{.docutils .literal .notranslate}]{.pre} 并在浏览器中打开此文件。

## Visual Studio Code



借助一些扩展，您可以在本地使用 Visual Studio Code 创建一个高效的环境来编写和测试文档。请按照以下步骤配置 VS Code：



1.  安装所需的扩展：



- Python：[`(ms-python.python)`{.docutils .literal .notranslate}]{.pre}

- 实时服务器: [`(ritwickdey.LiveServer)`{.docutils .literal .notranslate}]{.pre}



2. 将以下条目添加到 [`.vscode/settings.json`{.docutils .literal .notranslate}]{.pre}。

::: highlight
          {
            "liveServer.settings.root": "/.vscode/build/html",
            "liveServer.settings.wait": 1000,
            "python.terminal.activateEnvInCurrentTerminal": true
          }

- [`liveServer.settings.root`{.docutils .literal .notranslate}]{.pre}：设置直播预览的输出网站根目录。必须与 [`tasks.json`{.docutils .literal .notranslate}]{.pre} 命令一起修改。

- [`liveServer.settings.wait`{.docutils .literal .notranslate}]{.pre}：告诉实时服务器等待更新，以便为 Sphinx 提供时间重新生成站点内容，并在构建完成前不刷新。

- [`python.terminal.activateEnvInCurrentTerminal`{.docutils .literal .notranslate}]{.pre}: 激活自动虚拟环境，以便您可以从集成终端构建站点。

3. 将以下任务添加到 [`.vscode/tasks.json`{.docutils .literal .notranslate}]{.pre}。

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

> ::: {}
    > 实现细节：需要定义两个问题匹配器，因为 VS Code 不能容忍某些问题信息可能缺失的情况。虽然单个正则表达式可以匹配所有类型的错误，但如果一个捕获组为空（行号并非在所有警告/错误消息中都出现），而 [`pattern`{.docutils .literal .notranslate}]{.pre} 引用了所述空捕获组，VS Code 会完全丢弃该消息。
    > :::



4.  配置 Python 虚拟环境（[`venv`{.docutils .literal .notranslate}]{.pre}）。

从命令面板运行 `Python:` `Create` `Environment`。选择 `venv` 环境和 `docs/sphinx/requirements.txt`。

5. 编译文档。

使用以下选项之一启动默认构建任务：

- 一个快捷键（默认值为 [`Ctrl+Shift+B`{.docutils .literal .notranslate}]{.pre}）

从命令面板执行 [`Tasks:`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Run`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Build`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Task`{.docutils .literal .notranslate}]{.pre}

6. 打开实时预览。



在 VS Code 中导航到站点输出：右键点击 [`.vscode/build/html/index.html`{.docutils .literal .notranslate}]{.pre}，然后选择 [`Open`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`with`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Live`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`Server`{.docutils .literal .notranslate}]{.pre}。次重新构建后内容会自动更新，无需手动刷新浏览器。

[](toolchain.html "上一页"){.left-prev}

上一页

ROCm（Radeon 开放计算平台）文档工具链

[](feedback.html "下一页"){.right-next}

::: prev-next-info
下一页



对 ROCm 文档提供反馈

目录

- [GitHub](#github){.reference .internal .nav-link}
- [命令行](#command-line){.reference .internal .nav-link}
- [Visual Studio Code](#visual-studio-code){.reference .internal .nav-link}