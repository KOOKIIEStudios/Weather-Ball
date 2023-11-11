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
    raw_content = requests.get(
        uri,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"},
    )
    log.debug(raw_content.text)
    return Selector(text=raw_content.text)


def get_links(uri: str) -> list[str]:
    selector = get_base_selector(uri)
    return selector.xpath("//div[@class='full-article-body']/ul[2]/a[contains(., 'Deck List')]").getall()


# For debug use only
if __name__ == "__main__":
    selector = get_base_selector("https://www.pokemon.com/us/play-pokemon/about/tournaments-rules-and-resources")
    target_table = selector.xpath("//div[@class='full-article-body']/ul[2]")
    log.debug(target_table)
    line_selector = target_table.xpath("./a[contains(., 'Deck List')]")
    log.debug(line_selector)
