import time
import pyautogui
import random
value = random.randint(0, 1000)
while (1 == 1):
    if value % 2 == 0:
        time.sleep(random.randint(10, 100))
        pyautogui.click() #click on bio
        
        time.sleep(random.randint(30, 400))
        pyautogui.scroll(10) #scroll down bio

        time.sleep(random.randint(10, 100))
        pyautogui.click() #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click() #click through photo
        
        time.sleep(random.randint(10, 100))
        pyautogui.click() #click through photo
        
        time.sleep(random.randint(5, 500))
        pyautogui.click() #click like
    else:
        time.sleep(random.randint(10, 80))
        pyautogui.click() #click bio

        time.sleep(random.randint(30, 200))
        pyautogui.scroll() #scroll down for the bio

        time.sleep(random.randint(10, 70))
        pyautogui.click() #photo

        time.sleep(random.randint(10,70))
        pyautogui.click() #photo

        time.sleep(random.randint(1, 80))
        pyautogui.click() #dislike
