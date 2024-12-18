.. readthedocsQuickStart documentation master file, created by
   sphinx-quickstart on Tue Dec  3 15:00:29 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:


sphinx-quickstart
====================

- **step1: create sphinx_project**
  
  .. code-block:: sh

    sphinx-quickstart .

  after run the above cmd, the directory layout looks like below::

    .
    ├── build
    ├── make.bat
    ├── Makefile
    ├── README.md
    └── source
        ├── _static
        ├── _templates
        ├── conf.py
        └── index.rst

- **step2: add readthedocs.yaml**
  
  create readthedocs.yaml file at the root dirctory,the necessary contents look like this::

    version: 2

    # Set the OS, Python version and other tools you might need
    build:
    os: ubuntu-22.04
    tools:
        python: "3.12"
        # You can also specify other tool versions:
        # nodejs: "20"
        # rust: "1.70"
        # golang: "1.20"

    # Build documentation in the "docs/" directory with Sphinx
    sphinx:
    configuration: source/conf.py


    # Optionally build your docs in additional formats such as PDF and ePub
    # formats:
    #   - pdf
    #   - epub

    # Optional but recommended, declare the Python requirements required
    # to build your documentation
    # See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
    python:
    install:
        - requirements: source/requirements.txt
  
  
- **step3: add requirements.txt file**
  
  list required python requirements in source/requirements.txt::

    # theme
    sphinx==7.1.2
    sphinx-copybutton
    furo
    sphinx-design

  the final dirctory layout looks liek this::

    .
    ├── build
    ├── make.bat
    ├── Makefile
    ├── README.md
    ├── readthedocs.yaml
    └── source
        ├── _static
        ├── _templates
        ├── conf.py
        ├── index.rst
        └── requirements.txt

- **step4: import reopo into readthedocs**

查看pdf文档
============

文档连接
--------

`[view pdf] <_static/CCRIO2.3.pdf>`_

直接嵌入
----------

iframe网页嵌入
~~~~~~~~~~~~~~~

.. raw:: html
    
   <iframe src="_static/CCRIO2.3.pdf" width="100%" height="800px" style="border: none;"></iframe>

pdf.js 插件网页嵌入
~~~~~~~~~~~~~~~~~~~

.. raw:: html

      <iframe src="_static/web/viewer.html?file=../CCRIO2.3.pdf"
           width="100%" height="800px" style="border: none;"></iframe>

image指令嵌入
~~~~~~~~~~~~~~

.. image:: _static/images/ccrio.png
   :alt: descriptive text



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
