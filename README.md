# MinerU

A powerful tool for extracting and processing content from PDF documents and other file formats.

[![PyPI version](https://badge.fury.io/py/mineru.svg)](https://badge.fury.io/py/mineru)
[![Python Version](https://img.shields.io/pypi/pyversions/mineru)](https://pypi.org/project/mineru/)
[![License](https://img.shields.io/github/license/opendatalab/MinerU)](LICENSE)
[![CI](https://github.com/opendatalab/MinerU/actions/workflows/python-package.yml/badge.svg)](https://github.com/opendatalab/MinerU/actions/workflows/python-package.yml)

## Overview

MinerU is an open-source document parsing and extraction tool that converts PDFs and other document formats into structured, machine-readable content. It leverages advanced layout analysis and OCR capabilities to accurately extract text, tables, figures, and formulas.

## Features

- 📄 **PDF Parsing** — Extract text, tables, images, and formulas from PDFs
- 🔍 **Layout Analysis** — Intelligent document layout detection
- 📊 **Table Extraction** — Structured table data extraction
- 🔢 **Formula Recognition** — LaTeX formula extraction
- 🌐 **Multi-language OCR** — Support for multiple languages
- 📦 **Multiple Output Formats** — Export to Markdown, JSON, and more
- 🚀 **CLI & Python API** — Flexible usage options

## Installation

### Prerequisites

- Python 3.9+
- pip

### Install via pip

```bash
pip install mineru
```

### Install from source

```bash
git clone https://github.com/opendatalab/MinerU.git
cd MinerU
pip install -e .
```

## Quick Start

### Command Line Interface

```bash
# Parse a PDF file and output Markdown
mineru parse document.pdf -o output/

# Parse with specific backend
mineru parse document.pdf -o output/ --backend pipeline

# Parse a URL
mineru parse https://example.com/document.pdf -o output/
```

### Python API

```python
from mineru.api import parse_pdf

# Parse a PDF file
result = parse_pdf("document.pdf")

# Access extracted content
print(result.markdown)      # Markdown text
print(result.tables)        # Extracted tables
print(result.images)        # Extracted images
```

## Documentation

Full documentation is available at [https://mineru.readthedocs.io](https://mineru.readthedocs.io)

## Configuration

MinerU can be configured via a YAML configuration file or environment variables. See [Configuration Guide](docs/configuration.md) for details.

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) before submitting a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the AGPL-3.0 License — see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Original project: [opendatalab/MinerU](https://github.com/opendatalab/MinerU)
- Thanks to all contributors and the open-source community

## Citation

If you use MinerU in your research, please cite:

```bibtex
@misc{mineru2024,
  title={MinerU: A One-stop Open-source High-quality Information Extraction Tool},
  author={OpenDataLab},
  year={2024},
  url={https://github.com/opendatalab/MinerU}
}
```
