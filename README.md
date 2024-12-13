<p align="center">
    <img src="https://raw.githubusercontent.com/neuml/txtmarker/master/logo.png"/>
</p>

<p align="center">
    <b>Highlight text in documents</b>
</p>

<p align="center">
    <a href="https://github.com/neuml/txtmarker/releases">
        <img src="https://img.shields.io/github/release/neuml/txtmarker.svg?style=flat&color=success" alt="Version"/>
    </a>
    <a href="https://github.com/neuml/txtmarker/releases">
        <img src="https://img.shields.io/github/release-date/neuml/txtmarker.svg?style=flat&color=blue" alt="GitHub Release Date"/>
    </a>
    <a href="https://github.com/neuml/txtmarker/issues">
        <img src="https://img.shields.io/github/issues/neuml/txtmarker.svg?style=flat&color=success" alt="GitHub issues"/>
    </a>
    <a href="https://github.com/neuml/txtmarker">
        <img src="https://img.shields.io/github/last-commit/neuml/txtmarker.svg?style=flat&color=blue" alt="GitHub last commit"/>
    </a>
    <a href="https://github.com/neuml/txtmarker/actions?query=workflow%3Abuild">
        <img src="https://github.com/neuml/txtmarker/workflows/build/badge.svg" alt="Build Status"/>
    </a>
    <a href="https://coveralls.io/github/neuml/txtmarker?branch=master">
        <img src="https://img.shields.io/coverallsCoverage/github/neuml/txtmarker" alt="Coverage Status">
    </a>
</p>

-------------------------------------------------------------------------------------------------------------------------------------------------------

![demo](https://raw.githubusercontent.com/neuml/txtmarker/master/demo.png)

txtmarker highlights text in documents. txtmarker takes a list of (name, text) pairs, scans an input document and creates a modified version with highlights embedded.

Current file formats supported:

- pdf

## Installation
The easiest way to install is via pip and PyPI

```
pip install txtmarker
```

Python 3.9+ is supported. Using a Python [virtual environment](https://docs.python.org/3/library/venv.html) is recommended.

txtmarker can also be installed directly from GitHub to access the latest, unreleased features.

```
pip install git+https://github.com/neuml/txtmarker
```

Python 3.9+ is supported

## Examples

The examples directory has a series of examples and notebooks giving an overview of txtmarker. See the list of notebooks below.

### Notebooks

| Notebook     |      Description      |   |
|:----------|:-------------|------:|
| [Introducing txtmarker](https://github.com/neuml/txtmarker/blob/master/examples/01_Introducing_txtmarker.ipynb) | Overview of the functionality provided by txtmarker | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtmarker/blob/master/examples/01_Introducing_txtmarker.ipynb) |
| [Highlighting with Transformers](https://github.com/neuml/txtmarker/blob/master/examples/02_Highlighting_with_Transformers.ipynb) | AI-driven highlighting with Transformers | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/neuml/txtmarker/blob/master/examples/02_Highlighting_with_Transformers.ipynb) |


## Configuration

The following section gives an overview of highlighters and available methods/configuration. See the notebooks above for detailed examples.

### Create a new highlighter

```python
from txtmarker.factory import Factory
highlighter = Factory.create("pdf")
```

#### extension
```yaml
extension: string
```

Type of highlighter to create (i.e. pdf)

#### Optional constructor arguments:

#### formatter
```yaml
formatter: callable
```

Formats queries and input text using this method. Helps with cleanup of files with lots of symbols and other content.

#### chunks
```yaml
chunks: int
```

Splits queries into multiple chunks. This is designed for very long text matches.

### Highlight text

```python
highlighter.highlight("input.pdf", "output.pdf", [("name", "text to highlight")])
```

#### infile
```yaml
infile: string
```

Full path to input file

#### outfile
```yaml
outfile: string
```

Full path to output file, i.e. the highlighted file

#### highlights
```yaml
highlights: list of (string, string|regex)
```

List of highlight elements. Each pair has a name (can be None) and text value. The text can either be a string or a regular expression.
