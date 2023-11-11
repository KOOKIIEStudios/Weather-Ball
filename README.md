# Weather Ball
Weather Ball is a Python script that generates templates for CastFORM.  
It automatically searches for the official registration sheet from Pokémon's official website, downloads a copy, and converts it to `webp` for use in CastFORM.

## Tech Stack
Weather Ball is developed using Python 3.12 and Poppler. The entry point is `main.py`.  
If you're using Chocolatey, install them using the following command: `choco install python poppler`

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
