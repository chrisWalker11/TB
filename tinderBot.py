import time
import pyautogui
import random
value = random.randint(0, 1000)

print("next photo")
input("press enter when in postion")
print(pyautogui.position())
px = int(input("input x coordinate for next photo: "))
py = int(input("input y coordinate for next photo: "))
print("like")
input("enter when ready")
print(pyautogui.position())
lx = int(input("input x coordinate for like: "))
ly = int(input("input y coordinate for like: "))
print("dislike")
input("enter when ready")
print(pyautogui.position())
dx = int(input("input x coordinate for dislike: "))
dy = int(input("input y coordinate for dislike: "))


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
