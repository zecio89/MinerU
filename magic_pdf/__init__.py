"""MinerU - A powerful PDF parsing and extraction library.

This package provides tools for extracting structured content from PDF files,
including text, tables, images, and mathematical formulas.

Personal fork notes:
- Forked for learning purposes and local experimentation
- Upstream: https://github.com/opendatalab/MinerU
- Added __author_email__ and bumped version to track local changes
- Added PARSE_TYPE_TXT to __all__ exports (was missing from upstream)
"""

__version__ = "0.1.1-local"
__author__ = "OpenDataLab"
__author_email__ = ""  # not set for personal fork
__license__ = "AGPL-3.0"

from magic_pdf.config.constants import (
    MODEL_NAME,
    PARSE_TYPE_AUTO,
    PARSE_TYPE_OCR,
    PARSE_TYPE_TXT,
)

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "MODEL_NAME",
    "PARSE_TYPE_AUTO",
    "PARSE_TYPE_OCR",
    "PARSE_TYPE_TXT",
]
