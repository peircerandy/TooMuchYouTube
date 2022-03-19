import pyautogui
import keyboard
import mouse
import time

if mouse.is_pressed():
    pos1 = pyautogui.position()
    print(pos1)
    time.sleep(.5)
if mouse.is_pressed():
    pos2 = pyautogui.position()
    print(pos2)
    time.sleep(.5)

width = pos2[0] - pos1[0]
height = pos2[1] - pos1[0]
im = pyautogui.screenshot(region=(pos1[0],pos1[1], width, height))

tablocation = pyautogui.locateOnScreen(im)
tabx,  taby = tablocation
tabx + width - 4
taby + height - 4
pyautogui.click(tabx, taby)
