import pyautogui
import random
import time

postMemeChoices = ["f", "r", "i", "c", "k"]

def Seconds30():
    pyautogui.write("pls hl")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write(random.choice(["low", "high"]))

def Seconds40():
    pyautogui.write("pls hunt")
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.write("pls fish")
    pyautogui.press("enter")
    time.sleep(1.5)

    pyautogui.write("pls pm")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.write(random.choice(postMemeChoices))
    pyautogui.press("enter")

    from main_DankMemer import timeInterval
    timeInterval += 8

def Seconds45():
    pyautogui.write("pls beg")
    pyautogui.press("enter")