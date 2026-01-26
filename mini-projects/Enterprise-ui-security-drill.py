import pyautogui
import time
import random
from datetime import datetime
import os

OUTPUT_DIR = "ui_drill_artifacts"
USERS = [
    ("user1", "correct_pass"),
    ("user1", "wrong_pass"),
    ("user2", "wrong_pass"),
]
ATTEMPTS_PER_USER = 2
DELAY_RANGE = (2, 5)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def capture(name):
    path = os.path.join(OUTPUT_DIR, f"{name}_{timestamp()}.png")
    pyautogui.screenshot(path)

def simulate_mouse():
    for _ in range(5):
        pyautogui.moveRel(
            random.randint(-80, 80),
            random.randint(-80, 80),
            duration=0.3
        )
        time.sleep(0.2)

def login_flow(username, password):
    pyautogui.write(username)
    pyautogui.press("tab")
    pyautogui.write(password)
    pyautogui.press("enter")

def run_drill():
    time.sleep(5)
    capture("before_any_attempt")

    for user, pwd in USERS:
        for i in range(ATTEMPTS_PER_USER):
            simulate_mouse()
            capture(f"before_attempt_{user}_{i+1}")

            login_flow(user, pwd)

            time.sleep(3)
            capture(f"after_attempt_{user}_{i+1}")

            time.sleep(random.randint(*DELAY_RANGE))

    capture("after_all_attempts")

if __name__ == "__main__":
    run_drill()
    print("UI security drill completed")
