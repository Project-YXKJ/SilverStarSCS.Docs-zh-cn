# SilverStar-CSSM-Reference-Book

Documentation for SilverStar-CSSM

Built with [Sphinx](https://www.sphinx-doc.org/), and host on [Read the Docs](https://readthedocs.org/)

## Build guide

### Setup

- 安装 Python
- 安装 Git

**Step 1.** 克隆本仓库, 创建虚拟环境(非必须, 但是建议)

[Installing packages using pip and virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

```bash
$ cd SilverStar-CSSM-Reference-Book-CHS
$ py -m venv env
```

### Activate virtual environment

**Step 2.** 激活虚拟环境, 并安装必要的包.

```bash
$ .\env\Scripts\activate
$ py -m pip install -r requirements.txt
```

### Render the documentation as HTML

**Step 3.** 输出本地 html, 打开 `docs/build/html/index.html` 查看

```bash
$ cd docs
$ make clean // 不是必须
$ make html
```

### Build the documentation in **PDF** format

```bash
$ cd docs
$ make latexpdf
```



## Q&A

### CairoSVG安装？

LaTeX不支持SVG，[sphinxcontrib-svg2pdfconverter](https://pypi.org/project/sphinxcontrib-svg2pdfconverter/) 可以帮你转换SVG到PDF，但是此插件并不具体提供转换功能，需要自行安装[CairoSVG](https://cairosvg.org/)，当然你可以选择其他转换器。CairoSVG又依赖一些其他工具，可以参考[这里](https://cairosvg.org/documentation/#installation)。

## Reference

[多语言](https://docs.readthedocs.io/en/stable/localization.html#projects-with-multiple-translations-sphinx-only)

[reStructuredText 语法参考](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)

[sphinx-design](https://sphinx-design.readthedocs.io/en/furo-theme/index.html)

[furo theme](https://pradyunsg.me/furo/quickstart/)
