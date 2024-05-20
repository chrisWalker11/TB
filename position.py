import pyautogui


print("you need to postiton the cursor over the next photo, like, and dislike buttons to find the coordinates")

print("start with next photo")
input("press enter once over next photo")
print(pyautogui.position())
px = input("input x coordinate for next photo: ")
py = input("input y coordinate for next photo: ")
with open("variables.py", "w") as f:
    f.writelines("px = " + px + '\n')
    f.writelines("py = " + py + '\n')


print("put cursor over like button")
input("press enter once over like")
print(pyautogui.position())
lx = input("input x coordinate for like: ")
ly = input("input y coordinate for like: ")
with open('variables.py', 'a') as f:
    f.writelines("lx = " +  lx + '\n')
    f.writelines("ly = " + ly + '\n')

print("put cursor over the dislike button")
input("press enter once over dislike")
print(pyautogui.position())
dx = input("input x coordinate for dislike: ")
dy = input("input y coordinate for dislike: ")
with open('variables.py', 'a') as f:
    f.writelines("dx = " +  dx + '\n')
    f.writelines("dy = " + dy + '\n')

print("estimate where the button will appear")
input("R?")
print(pyautogui.position())
mx = input("x?")
my = input("Y?")
with open('variables.py', 'a') as f:
    f.writelines("mx = " + mx + '\n')
    f.writelines("my = " + my)

