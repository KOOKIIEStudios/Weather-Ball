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
"""Generic logger module that wraps around Python's built-in logger.
"""
from pathlib import Path
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
# Use a config file for these, in larger projects:
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
FORMATTER = logging.Formatter(LOG_FORMAT)
LOG_DIR = Path("logs")
ACTIVE_LOG_NAME = "logger.log"


def get_log_path():
    if LOG_DIR.exists():
        return Path(LOG_DIR, ACTIVE_LOG_NAME)
    raise FileNotFoundError(2, "Log output directory could not be found!")


def get_console_handler() -> logging.StreamHandler:
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler() -> TimedRotatingFileHandler:
    file_handler = TimedRotatingFileHandler(get_log_path(), when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler


class NullHandler(logging.Handler):
    """Silent handler
    
    Add this in `get_logger()` to silence the logger.
    """
    def emit(self, record):
        pass


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)

    logger.addHandler(get_console_handler())
    file_handler = get_file_handler()
    logger.addHandler(file_handler)

    try:
        logger.setLevel(logging.DEBUG)
        logger.debug(f"Fetching logger for {logger_name}")
    except PermissionError:
        logger.removeHandler(file_handler)
        file_handler.doRollover()
        logger.addHandler(file_handler)

    logger.setLevel(logging.DEBUG)  # Modify this on production!
    return logger


def shutdown_logger() -> None:
    logging.shutdown()
