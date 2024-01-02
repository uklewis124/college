import os
import time
import sys

os.system("pip install pyautogui")
os.system("pip install pywin32")

from pyautogui import *

try:
    import win32api, win32con

    screensize = size()
    print(screensize)
    width = screensize[0]
    height = screensize[1]
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


    def free_skins():
        click(0, 1435)
        time.sleep(0.1)
        click(0, 1367)
        time.sleep(0.1)
        click(10, 1289)
        time.sleep(0.1)
        click(10, 1289)


    free_skins()

except:
    directory = os.getcwd()
    os.system('"'+sys.argv[0]+'"')
#-Made by James Leggott, Dexter Oldroyd, Oscar O'Brien