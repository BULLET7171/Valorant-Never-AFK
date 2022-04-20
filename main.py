import pyautogui
from time import sleep
import random
import keyboard
randomdata = ['a','w','d','s','space']
def randomkeydown():
    keydata = random.choice(randomdata)
    pyautogui.keyDown(keydata,random.randint(1,5))
    sleep(random.randint(1,5))
    pyautogui.keyUp(keydata)
    
def antiafk():
    print("Anti-AFK for valorant, made by bullet")
    while True:
        randomkeydown()
        if keyboard.is_pressed('q'):
            break


if __name__ == '__main__':
    antiafk() 