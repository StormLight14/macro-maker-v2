# Macro Maker V2
Complete revamp of my original macro creator, now uses `pyautogui` instead of `pynput`.

## Prerequisites
If you haven't already, download Python 3 from https://python.org, or just use something like a package manager for a Linux distribution.
Either clone the code with `git clone https://github.com/StormLight14/macro-maker-v2.git` or click on "Code" > "Download Zip" and extract the zip.

## Running
Inside of the folder with the code, run main.py. `python3 main.py`

## Usage
The way this program works is by reading from a text file. By default, it is called "macro.txt". You can make it type letters, numbers, and (some) other keys like ctrl, esc, etc.
Here is some example syntax: `DELAY:1, REPEAT:3:0:(WRITE:Hello World!), ENTER` This will wait for 1 second, then type "Hello World" 3 times and press enter afterwards with 0 delay.

## Syntax
