# Macro Maker V2
Complete revamp of my original macro creator, now uses `pyautogui` instead of `pynput`.

## Prerequisites
If you haven't already, download Python 3 from https://python.org, or just use something like a package manager for a Linux distribution.
Either clone the code with `git clone https://github.com/StormLight14/macro-maker-v2.git` or click on "Code" > "Download Zip" and extract the zip.

## Running
Inside of the folder with the code, run main.py. `python3 main.py`

## Usage
The way this program works is by reading from a text file. By default, it is called "macro.txt". You can make it type letters, numbers, and (some) other keys like ctrl, esc, etc.
Here is some example syntax: `DELAY:1, REPEAT:3:0:(WRITE:Hello World!+ENTER)` This will wait for 1 second, then type "Hello World" 3 times and press enter afterwards with 0 delay.

## Syntax and Creating Macros
The syntax for creating macros is kind of messy, so feel free to modify the code to make it fit what you want, and maybe try to contribute the changes if you think they are better than what I have.

To start, there are 2 main different things you can create in the macro file: actions and functions. Actions are just things like keys and mouse buttons, while functions are more complex stuff the macro can do. 

Full list of special actions: 
```py
"SPACE", "LCTRL", "LALT", "LSHIFT", "CTRL", "RCTRL", "RALT", "RSHIFT", "TAB", "ESC", "ESCAPE", "ENTER", "DEL", "DELETE", "LCLICK", "RCLICK", "MCLICK",
"F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"
```
Full list of functions: 
```py
"DELAY", "HOLD", "WRITE", "HOTKEY", "REPEAT"
```
