# onlworks on 967px to 917px wide screen ¿¿make sure to zoom in ??
# https://www.crazygames.com/game/magic-piano-tiles

import pyautogui
import keyboard
import win32api
import win32con
import time

data_points = [(256, 520), (435, 520), (558, 520), (679, 520)]

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def check_and_click():
    for x, y in data_points:
        if pyautogui.pixel(x, y)[0] == 0:
            click(x, y)

while not keyboard.is_pressed('q'):
    check_and_click()