import time
import pyautogui
import random
from variables import *

value = random.randint(1, 1000000)

while (1 == 1):
    if value % 2 == 0:

        time.sleep(random.randint(10, 100))
        pyautogui.click(px, py) #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click(px, py) #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click(px, py) #click through photo
        
        time.sleep(random.randint(5, 90))
        pyautogui.click(lx, ly) #click like
    else:

        time.sleep(random.randint(10, 70))
        pyautogui.click(px, py) #photo

        time.sleep(random.randint(10,70))
        pyautogui.click(px, py) #photo

        time.sleep(random.randint(5, 80))
        pyautogui.click(dx, dy) #dislike
