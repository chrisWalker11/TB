import time
import pyautogui
import random
value = random.randint(0, 1000)
while (1 == 1):
    if value % 2 == 0:
       
        time.sleep(random.randint(10, 100))
        pyautogui.click() #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click() #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click() #click through photo
        
        time.sleep(random.randint(5, 500))
        pyautogui.click() #click like
    else:
        
        time.sleep(random.randint(5,45))
        pyautogui.click() #photo
        
        time.sleep(random.randint(10, 70))
        pyautogui.click() #photo

        time.sleep(random.randint(10,70))
        pyautogui.click() #photo

        time.sleep(random.randint(1, 80))
        pyautogui.click() #dislike
