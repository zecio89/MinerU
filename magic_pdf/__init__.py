"""MinerU - A powerful PDF parsing and extraction library.

This package provides tools for extracting structured content from PDF files,
including text, tables, images, and mathematical formulas.
"""

__version__ = "0.1.0"
__author__ = "OpenDataLab"
__license__ = "AGPL-3.0"

from magic_pdf.config.constants import (
    MODEL_NAME,
    PARSE_TYPE_AUTO,
    PARSE_TYPE_OCR,
    PARSE_TYPE_TXT,
)

__all__ = [
    "__version__",
    "MODEL_NAME",
    "PARSE_TYPE_AUTO",
    "PARSE_TYPE_OCR",
    "PARSE_TYPE_TXT",
]
