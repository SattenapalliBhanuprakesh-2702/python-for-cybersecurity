import pyautogui
import time
import random

time.sleep(5)

for _ in range(5):
    pyautogui.moveRel(random.randint(-100,100), random.randint(-100,100), duration=0.5)
    pyautogui.click()
    time.sleep(1)

