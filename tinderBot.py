import time
import pyautogui
import random
from variables import *
counter = 0

while counter <= 100
    value = random.randint(1, 1000000)

    if value % 2 == 0:

        time.sleep(random.randint(10, 100))
        pyautogui.click(px, py) #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click(px, py) #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click(px, py) #click through photo
        
        time.sleep(random.randint(5, 90))
        pyautogui.click(lx, ly) #click like
        counter = counter + 1
    else:

        time.sleep(random.randint(10, 70))
        pyautogui.click(px, py) #photo

        time.sleep(random.randint(10,70))
        pyautogui.click(px, py) #photo

        time.sleep(random.randint(5, 80))
        pyautogui.click(dx, dy) #dislike
