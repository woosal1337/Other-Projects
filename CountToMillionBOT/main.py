import pyautogui
import time

time.sleep(5)

for i in range(361, 1000001):
    pyautogui.typewrite(str(i))
    pyautogui.press("enter")
    time.sleep(0.5)