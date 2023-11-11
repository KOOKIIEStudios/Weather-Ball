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

from PIL import Image

from utils import config, logger

log = logger.get_logger(__name__)


def save(image_object: Image, file_path: Path) -> None:
    log.info("Saving as %s lossless - this may take a while", file_path.name)
    image_object.save(
        file_path,
        format="WEBP",
        lossless=True,
        quality=100,
        method=6,
    )


def save_a4(image_object: Image) -> None:
    save(image_object, config.OUTPUT_FOLDER / config.OUTPUT_FILE_NAME.a4)


def save_letter(image_object: Image) -> None:
    save(image_object, config.OUTPUT_FOLDER / config.OUTPUT_FILE_NAME.letter)
