# -*- coding: utf-8 -*-

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

#Press "a"
keyboard.press("a")
keyboard.release("a")

#Press the Windows Key
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)

#Type "This is a sentence written in Python 3!"
keyboard.type("This is a sentence written in Python 3!")
