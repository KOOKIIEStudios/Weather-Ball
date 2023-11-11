# Weather Ball
Weather Ball is a Python script that generates templates for CastFORM.  
It automatically searches for the official registration sheet from Pokémon's official website, downloads a copy, and converts it to `webp` for use in CastFORM.

Note that since the official website uses Incapsula protection, your mileage may vary.  

Weather Ball supports 2 modes of operation:
- Local Mode
  - Converts PDFs in the `/in` folder to `webp` in `/out`
  - Activated whenever there are PDF files present in this folder
  - This is a contingency measure created after I realised the site uses Incapsula
- Remote Mode
  - Activated when there are no PDFs in the `/in` folder
  - Scrapes the Pokémon website for download links, to download the latest versions
  - Downloads are saved as temp files, which get deleted after use
  - This was the original project algorithm

## A rose by any other name would smell as sweet
Weather Ball is designed as a part of the toolchain for [CastFORM](https://github.com/BAA-Studios/CastFORM), a Pokémon registration sheet filler.  
Being a form-automation application based around Pokémon TCG, CastFORM is a play on words using the name of one of the 
playable Pokémon.   
This project inherits its name from Castform's unique skill in the game. 

## Tech Stack
Weather Ball is developed using Python 3.12 and Poppler. The entry point is `main.py`.  
If you're using Chocolatey, install Python using the following command: `choco install python`, which should automatically add Python to Path.

The community build for Poppler on Chocolatey doesn't extract shims properly, for Windows, [download it](https://github.com/oschwartz10612/poppler-windows/releases/) manually and add to `PATH`.  
Many Linux distributions should already ship with Poppler. If you get an error for missing Poppler, check your package manager for `poppler-utils`.

## Usage
1. Clone, and `cd` to this repository
2. Set up your virtual environment
    - Linux: run `setup.sh`
    - Windows: run `start.sh`
3. Run `start.bat`/`start.sh` to run the program
    - If unsure, select the virtual environment when prompted
4. Check `./out` for the `webp` files

## Disclaimer
**Weather Ball** is an open-source Python application that fetches and manipulates Pokémon registration sheets.  
**Weather Ball** is part of the developer toolchain created for [CastFORM](https://github.com/BAA-Studios/CastFORM).  
**Weather Ball** is non-monetised, and provided as is. Every reasonable effort has been taken to ensure correctness and reliability of **Weather Ball**. 
We will not be liable for any special, direct, indirect, or consequential damages or any damages whatsoever resulting from 
loss of use, data or profits, whether in an action if contract, negligence or other tortious action, arising out of or in connection with the use of **Weather Ball** (in part or in whole).
