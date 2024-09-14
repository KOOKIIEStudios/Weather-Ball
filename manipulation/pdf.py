# Copyright 2023 KOOKIIE
#
# This file is part of Weather Ball.
# Weather Ball is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Weather Ball is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Weather Ball. If not, see <https://www.gnu.org/licenses/>.
#
# Contact via Discord: `sessionkookiie`
from pathlib import Path

from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFSyntaxError
)

from utils import logger

log = logger.get_logger(__name__)


def read_pdf(pdf: Path):
    log.debug(f"Reading file: {pdf}")
    try:
        output = convert_from_path(pdf, dpi=300, single_file=True)
        return output[0]
    except PDFInfoNotInstalledError:
        log.error("Poppler not detected! See README for installation instructions.")
    except PDFSyntaxError:
        log.error("PDF file %s could not be read", pdf.name)
