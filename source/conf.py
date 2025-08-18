# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import time

# add the python code
yxkj_docs_dir = os.path.abspath(os.path.dirname(__file__))

# -- Project information -----------------------------------------------------
#

project = "SilverStar SCS Documentation"
copyright = f"2011-{time.strftime('%Y')}, SilverStar Technology"
author = "vayoger"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

# -- Options for Autodoc --------------------------------------------------------------
#

autodoc_member_order = "bysource"
autodoc_preserve_defaults = True

# Keep the type hints outside the function signature, moving them to the
# descriptions of the relevant function/methods.
autodoc_typehints = "description"

# -- Options for extlinks ----------------------------------------------------
#

extlinks = {}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#

html_theme = "furo"
html_title = "SilverStar SCS Documentation"
language = "zh_CN"

html_static_path = ["_static"]
# html_css_files = ["css/custom.css"]

html_favicon = "_static/favicon-32x32.png"
html_logo = "_static/silverstar-logo.svg"

html_theme_options = {
    "light_css_variables": {
        # 衔接以及左侧目录的颜色
        "color-brand-primary": "#c0d725",
        "color-brand-content": "#c0d725",
        # "font-stack": "Montserrat, LXGW WenKai, sans-serif",
        # "font-stack--monospace": "Courier, monospace",
    },
    "dark_css_variables": {
        "color-brand-primary": "#c0d725",
        "color-brand-content": "#c0d725",
    },
    "source_repository": "https://github.com/Project-YXKJ/SilverStarSCS.Docs-zh-cn",
    "source_branch": "main",
    "source_directory": "source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Project-YXKJ/SilverStarSCS.Docs-zh-cn",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

# -- Options for sphinx-copybutton -----------------------------------------------------
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html
#

copybutton_prompt_text = r">>> |\.\.\. |\$ |> "
copybutton_prompt_is_regexp = True

# -- Options for LaTeX output ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output
#

latex_elements = {}
latex_documents = [
    (
        "index",
        "silverstarscsdocs.tex",
        "SilverStar SCS Documentation",
        "vayoger",
        "manual",
    ),
]

# -- Options for manual page output ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output
#

man_pages = [
    (
        "index",
        "silverstarscsdocs",
        "SilverStar SCS Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-texinfo-output
#

texinfo_documents = [
    (
        "index",
        "silverstarscsdocs",
        "SilverStar SCS Documentation",
        author,
        "silverstarscsdocs",
        "One line description of project.",
        "Miscellaneous",
    ),
]
