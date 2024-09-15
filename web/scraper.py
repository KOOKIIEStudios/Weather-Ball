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
from parsel import Selector
import requests

from utils import logger

log = logger.get_logger(__name__)


def get_base_selector(uri: str) -> Selector:
    log.info("Fetching Pokemon website contents")
    raw_content = requests.get(
        uri,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
        },
    )
    return Selector(text=raw_content.text)


def get_links(uri: str) -> list[str]:
    log.info("Extracting relevant links")
    selector = get_base_selector(uri)
    target_table = selector.xpath("//div[@class='full-article-body']/ul[2]")
    target_rows = target_table.xpath(".//a[contains(., 'Deck List')]/@href")
    suffixes = target_rows.getall()

    log.debug("Suffixes: %s", ", ".join(suffixes))
    links = [f"https://www.pokemon.com{suffix}" for suffix in suffixes]
    log.debug("Download Links: %s", ", ".join(links))
    return links


# For debug use only
if __name__ == "__main__":
    test_selector = get_base_selector("https://www.pokemon.com/us/play-pokemon/about/tournaments-rules-and-resources")
    test_target_table = test_selector.xpath("//div[@class='full-article-body']/ul[2]")
    log.debug(test_target_table.getall())
    line_selector = test_target_table.xpath(".//a[contains(., 'Deck List')]/@href")
    log.debug(line_selector.getall())
