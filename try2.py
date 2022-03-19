import cv2
import pyautogui
import time
# tablocation = pyautogui.locateOnScreen('youtube2.png')
# print(tablocation)
# tabx = tablocation[0] + 1
# taby = tablocation[1] + 1
# pyautogui.moveTo(tabx, taby)
# pyautogui.click(button='right')  # clicks the center of where the tab was found
# pyautogui.click('closetab.png')

print(pyautogui.locateCenterOnScreen('youtube2.png'))
time.sleep(1)
# pyautogui.moveTo(1234, 11)
# pyautogui.click(button='right')
# print(pyautogui.click('closetab.png'))
# pyautogui.moveTo(1325, 404)
# pyautogui.click(button='right')