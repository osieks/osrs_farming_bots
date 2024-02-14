#pip3 install pyautogui
import pyautogui
import time
from datetime import datetime
import keyboard  # using module keyboard

tab_tree = ['tree2.png','tree1.png']
tab_drop = ['logs.png']
tree_conf = 0.7
click_conf = 0.9

pyautogui.FAILSAFE = False

while(True):
    
    if keyboard.is_pressed('q'):
        raise
    
    # dropping items
    z=0
    drop_location = pyautogui.locateCenterOnScreen(tab_drop[z],confidence=click_conf, grayscale=False)
    while(drop_location != None):
        drop_location = pyautogui.locateCenterOnScreen(tab_drop[z],confidence=click_conf, grayscale=False)
        if(drop_location == None):
            break
        print("dropping")
        prev_mouse_location = pyautogui.position()
        pyautogui.click(drop_location)
        time.sleep(0.2)
        pyautogui.moveTo(prev_mouse_location)

    for z in range(0,len(tab_tree)):
        tree_location = pyautogui.locateCenterOnScreen(tab_tree[z],confidence=tree_conf, grayscale=False)
        if(tree_location != None):
            print("cutting")
            prev_mouse_location = pyautogui.position()
            pyautogui.moveTo(tree_location) 
            time.sleep(0.1)
            pyautogui.click(tree_location)
            pyautogui.moveTo(prev_mouse_location)  
            time.sleep(6)  
            tree_conf=0.8                    
            break
    else:
        print(datetime.now())
        print(tree_conf)
        tree_conf = tree_conf -0.1
        if tree_conf<0.1:
            tree_conf=0.1