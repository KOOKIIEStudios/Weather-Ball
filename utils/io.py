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

from utils import config, logger

log = logger.get_logger(__name__)


def clear_outputs_folder() -> None:
    log.info("Clearing output folder")
    pdf_files = config.OUTPUT_FOLDER.glob("*.pdf")
    for file in pdf_files:
        file.unlink()


def get_local_inputs():
    log.info("Checking for files in input folder")
    return list(config.INPUT_FOLDER.glob("*.pdf"))


def rename_local_files(list_of_files: list[Path]):
    """Rename official file names to CastFORM format"""
    for file in list_of_files:
        if "a4" in file.stem:
            file.rename(file.parent / config.PDF_FILE_NAME.a4)
            continue
        if "85x11" in file.stem:
            file.rename(file.parent / config.PDF_FILE_NAME.letter)
            continue
        if "letter" not in file.stem:
            log.warning("Unexpected PDF name: %s", file.name)
