import sys

from utils import logger

log = logger.get_logger(__name__)


if __name__ == "__main__":
    log.info("Hello world!")

    # Scraper - get links
    # Download PDF to temp dir
    # Convert to PIL
    # Export to output dir

    logger.shutdown_logger()
    sys.exit(0)
