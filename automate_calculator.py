import pyautogui
import time

pyautogui.click(pyautogui.locateCenterOnScreen('1key.png'))
pyautogui.click(pyautogui.locateCenterOnScreen('pluskey.png'))
time.sleep(.5)
pyautogui.click(pyautogui.locateCenterOnScreen('1key.png'))
pyautogui.press('enter')