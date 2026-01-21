import pyautogui
import time

time.sleep(3)

pyautogui.write("test_user")
pyautogui.press("tab")
pyautogui.write("test_password")
pyautogui.press("enter")
