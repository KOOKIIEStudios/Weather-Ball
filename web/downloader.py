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
import requests

from utils import config, logger

log = logger.get_logger(__name__)


def download_pdf(link: str, location: Path) -> None:
    log.info("Downloading: %s", link)
    response = requests.get(
        link,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "https://www.pokemon.com/us/play-pokemon/about/tournaments-rules-and-resources",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
        },
        stream=True,
    )
    if response.status_code != 200:
        log.error(f"Unable to reach URI! Status code: {response.status_code}")
    with open(location, "wb") as pdf_file:
        for chunk in response.iter_content(chunk_size=128):
            pdf_file.write(chunk)


def download_all_pdf(links: list[str], temp_folder: Path) -> None:
    if len(links) != len(config.PDF_FILE_NAME):  # More files than expected
        for link in links:
            tokens = link.split("/")  # Use original file name
            file_path = temp_folder / tokens[-1]
            download_pdf(link, file_path)
    else:
        for index, link in enumerate(links):
            file_path = temp_folder / config.PDF_FILE_NAME[index]
            download_pdf(link, file_path)
