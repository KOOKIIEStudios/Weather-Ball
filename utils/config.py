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
from collections import namedtuple
from pathlib import Path


TARGET_URI = "https://www.pokemon.com/us/play-pokemon/about/tournaments-rules-and-resources"
INPUT_FOLDER = Path.cwd() / "in"
OUTPUT_FOLDER = Path.cwd() / "out"

DeckListType = namedtuple("DeckListType", "letter a4")
PDF_FILE_NAME = DeckListType(
    "pokemon_decklist_letter.pdf",
    "pokemon_decklist_a4.pdf",
)
OUTPUT_FILE_NAME = DeckListType(
    "pokemon_decklist_letter.webp",
    "pokemon_decklist_a4.webp",
)
