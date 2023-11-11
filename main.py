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

from manipulation import pdf, webp
from utils import config, io, logger
from web import Web

log = logger.get_logger(__name__)


def handle_expected_pdf(input_folder, temp_folder) -> None:
    # Read PDF file to Python Image object
    a4_image = pdf.read_pdf(input_folder / config.PDF_FILE_NAME.a4, temp_folder)
    letter_image = pdf.read_pdf(input_folder / config.PDF_FILE_NAME.letter, temp_folder)

    # Export as webp to output dir
    webp.save_a4(a4_image)
    webp.save_letter(letter_image)


def handle_unexpected_pdf(pdf_path_list: list, temp_folder) -> None:
    log.warning("Too many PDFs downloaded. Unable to automatically rename")
    for pdf_file in pdf_path_list:
        image_object = pdf.read_pdf(pdf_file, temp_folder)
        webp.save(image_object, config.OUTPUT_FOLDER / f"{pdf_file.stem}.webp")


def local_mode(pdf_path_list: list) -> None:
    log.info("PDF files found in local input folder; local mode activated")

    with tempfile.TemporaryDirectory(prefix="temp_", dir=config.OUTPUT_FOLDER) as temp_folder_name:
        temp_folder = config.OUTPUT_FOLDER / temp_folder_name

        if len(pdf_path_list) == 2:
            io.rename_local_files(pdf_path_list)
            handle_expected_pdf(config.INPUT_FOLDER, temp_folder)

        else:
            handle_unexpected_pdf(pdf_path_list, temp_folder)

    log.info("Completed!")


def remote_mode() -> None:
    log.info("No local files detected; remote mode activated")
    log.info("Attempting to scrape and download PDFs")

    scraper = Web(config.TARGET_URI)
    with tempfile.TemporaryDirectory(prefix="temp_", dir=config.OUTPUT_FOLDER) as temp_folder_name:
        temp_folder = config.OUTPUT_FOLDER / temp_folder_name
        scraper.download_pdf(temp_folder)

        # sanity check
        downloaded_files = list(temp_folder.glob("*.pdf"))
        if downloaded_files:
            downloaded_files_names = [file.name for file in downloaded_files]
            log.debug("Downloaded: %s", downloaded_files)
        else:
            log.warning("No files downloaded; try local mode instead")
            logger.shutdown_logger()
            sys.exit(1)

        # Convert to PIL
        if len(downloaded_files) == 2:
            handle_expected_pdf(temp_folder, temp_folder)
        else:
            handle_unexpected_pdf(downloaded_files, temp_folder)

    log.info("Completed!")


if __name__ == "__main__":
    log.info("----- Weather Ball -----")
    local = io.get_local_inputs()
    if local:
        local_mode(local)
        logger.shutdown_logger()
        sys.exit(0)

    remote_mode()
    logger.shutdown_logger()
    sys.exit(0)
