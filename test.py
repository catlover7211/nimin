import pyautogui
import time

time.sleep(2)


x = 0
y = 540
num_seconds = 1
pyautogui.moveTo(x, y, duration=num_seconds)  

pyautogui.scroll(clicks=-1400)
