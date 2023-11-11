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

import sys
import tempfile

from utils import config, logger
from web import Web

log = logger.get_logger(__name__)


def get_local_inputs():
    return list(config.INPUT_FOLDER.glob("*.pdf"))


if __name__ == "__main__":
    log.info("----- Weather Ball -----")
    local = get_local_inputs()
    if local:
        log.info("PDF files found in local input folder; local mode activated")
        # Insert conversion logic

        logger.shutdown_logger()
        sys.exit(0)

    log.info("No local files detected; remote mode activated")
    log.info("Attempting to scrape and download PDFs")
    scraper = Web(config.TARGET_URI)
    with tempfile.TemporaryDirectory(prefix="temp_", dir=config.OUTPUT_FOLDER) as temp_folder_name:
        temp_folder = config.OUTPUT_FOLDER / temp_folder_name
        scraper.download_pdf(temp_folder)

        # sanity check
        downloaded_files = [file.name for file in list(temp_folder.glob("*.pdf"))]
        if downloaded_files:
            log.debug("Downloaded: ", downloaded_files)
        else:
            log.warning("No files downloaded; terminating...")
            logger.shutdown_logger()
            sys.exit(1)

        # Convert to PIL
        # Export to output dir

    logger.shutdown_logger()
    sys.exit(0)
