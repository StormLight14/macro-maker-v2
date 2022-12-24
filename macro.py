from pyautogui import press, click, write, keyDown, keyUp, hotkey
from time import sleep

file_name = "macro.txt"


class Macro:
    def __init__(self):
        self.create_macro = open(file_name, "a")
        with open(file_name) as macro_file:
            self.macro_actions = macro_file.read()
        self.macro_actions = self.macro_actions.split(", ", -1)
        self.special_actions = {
            "SPACE", "LCTRL", "LALT", "LSHIFT", "CTRL", "RCTRL", "RALT", "RSHIFT", "TAB", "ESC", "ESCAPE", "ENTER", "DEL", "DELETE", "LCLICK", "RCLICK", "MCLICK",
            "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12"
        }
        self.special_functions = {
            "DELAY", "HOLD", "WRITE", "HOTKEY", "REPEAT"
        }

    def run_macro(self):
        for action in self.macro_actions:
            self.macro(action)

    def macro(self, action):
        self.action = action

        if self.action == ",":
            pass
        else:
            if ":" in self.action:
                self.special_function_split()

            if self.action in self.special_actions:
                self.macro_special_action(self.action)
            elif self.action in self.special_functions:
                self.macro_special_function(self.action)
            else:
                self.button = self.action
                press(self.action)

    def special_function_split(self):
        self.action_split = self.action.split(":", 3)

        match self.action_split[0]:
            case "DELAY":
                self.sleep_time = float(self.action_split[1])
            case "HOLD":
                self.button = self.action_split[1]
                self.hold_time = float(self.action_split[2])
            case "WRITE":
                self.word = self.action_split[1]
                self.word = self.word.replace(",", "")
            case "HOTKEY":
                self.hotkeys = self.action_split[1].split("+")
                for key in self.hotkeys:
                    if key in self.special_actions:
                        key = self.set_button(key)
            case "REPEAT":
                # REPEAT:TIMES:DELAY BETWEEN:(ACTION)
                self.repeat_count = int(self.action_split[1])
                self.sleep_time = float(self.action_split[2])
                self.actions = self.action_split[3].replace(
                    "(", "").replace(")", "").split("+")
                print(self.actions)

        self.action = self.action_split[0]

    def set_button(self, action):
        match action:
            case "SPACE":
                return "space"
            case "CTRL":
                return "ctrl"
            case "LCTRL":
                return "ctrlleft"
            case "RCTRL":
                return "ctrlright"
            case "LALT":
                return "altleft"
            case "RALT":
                return "altright"
            case "LSHIFT":
                return "shiftleft"
            case "RSHIFT":
                return "shiftright"
            case "TAB":
                return "tab"
            case "ESC":
                return "esc"
            case "ESCAPE":
                return "esc"
            case "ENTER":
                return "enter"
            case "DEL":
                return "delete"
            case "DELETE":
                return "delete"

    def macro_special_action(self, action):
        self.button = self.set_button(action)

        match action:
            case "LCLICK":
                self.button = None
                click(button="left")
            case "RCLICK":
                self.button = None
                click(button="right")
            case "MCLICK":
                self.button = None
                click(button="middle")
        if self.button:
            press(self.button)

    def macro_special_function(self, function):
        match function:
            case "DELAY":
                sleep(self.sleep_time)
            case "HOLD":
                keyDown(self.button)
                sleep(self.hold_time)
                keyUp(self.button)
            case "WRITE":
                write(self.word)
            case "HOTKEY":
                hotkey(*self.hotkeys)
            case "REPEAT":
                for i in range(self.repeat_count):
                    for action in self.actions:
                        self.action = action
                        self.macro(self.action)
                        sleep(self.sleep_time)
