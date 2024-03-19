# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import time

yxkj_docs_dir = os.path.abspath(os.path.dirname(__file__))

project = "SilverStar SCS Documentation"
copyright = f'2011-{time.strftime("%Y")}, SilverStar Technology'
author = "vayoger"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

root_doc = "index"

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx_toolbox.collapse",
    "sphinx_design",
]

templates_path = ["_templates"]
default_role = "any"
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for internationalization --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = "zh_CN"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_title = "SilverStar SCS Documentation"
html_favicon = "_static/favicon-32x32.png"
html_logo = "_static/silverstar-logo.svg"
# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]
html_last_updated_fmt = ""

# html_css_files = [
#     "css/custom.css",
# ]

html_theme_options = {
    "light_css_variables": {
        # 衔接以及左侧目录的颜色
        "color-brand-primary": "#c0d725",
        "color-brand-content": "#c0d725",
        # "font-stack": "LXGW WenKai Screen, sans-serif",
        # "font-stack--monospace": "Courier, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#c0d725",
        "color-brand-content": "#c0d725",
    },
    "source_repository": "https://github.com/Project-YXKJ/SilverStarSCS.Docs-zh-cn",
    "source_branch": "main",
}

# -- Options for LaTeX output ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {}
latex_documents = [
    (
        root_doc,
        "silverstarscsdocs.tex",
        "SilverStar SCS Documentation",
        "vayoger",
        "manual",
    ),
]

# -- Options for manual page output ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output

man_pages = [
    (
        root_doc,
        "silverstarscsdocs",
        "SilverStar SCS Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-texinfo-output

texinfo_documents = [
    (
        root_doc,
        "silverstarscsdocs",
        "SilverStar SCS Documentation",
        author,
        "silverstarscsdocs",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for intersphinx ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    "nox": ("https://nox.thea.codes/en/latest/", None),
}

# -- Options for todo extension --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Options for sphinx-copybutton -----------------------------------------------------
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html

copybutton_prompt_text = r">>> |\.\.\. |\$ |> "
copybutton_prompt_is_regexp = True
