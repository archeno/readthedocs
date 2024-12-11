# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'readthedocsQuickStart'
copyright = '2024, fengyang'
author = 'fengyang'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
latex_engine = 'xelatex'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_design',
    'sphinx_copybutton',
]
latex_documents = [
    ('index', 'hehe.tex', 'My title', 'fengyang', 'manual'),
]

latex_elements = {
    'pointsize': '12pt',
    'preamble': r'''
    \usepackage{xeCJK}
    \usepackage{graphicx}
    \usepackage{hyperref}
<<<<<<< HEAD
    \usepackage{pdfpages}
=======
    \usepackage{geometry}
    \geometry{a4paper, margin=1in}
>>>>>>> feea4ec (feat: modify conf.py)
    \setCJKmainfont{SimSun}  % 设置中文字体（如宋体）
    \setCJKsansfont{SimHei}           % 无衬线字体
    \setCJKmonofont{FangSong}         % 等宽字体
    \renewcommand{\maketitle}{%
    \begin{titlepage}
        \centering
        {\Huge\bfseries My Custom Title\par}  % 自定义标题
        \vspace{1cm}
        {\Large feng yang\par}             % 自定义作者
        \vspace{2cm}
        \includegraphics[width=0.5\textwidth]{logo.png}\par  % 添加 logo 或图片（可选）
        \vfill
        {\large \today\par}                  % 添加日期
    \end{titlepage}
    }
    ''',
    'figure_align': 'H',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
