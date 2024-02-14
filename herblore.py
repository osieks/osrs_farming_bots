#pip3 install pyautogui
import pyautogui
import time
from datetime import datetime
import keyboard  # using module keyboard

tab_grimmy = ['grimmy2.png']
tab_clean = ['clean.png']
tab_close = ['close.png']
tab_banker = ['banker1.png','banker2.png','banker1a.png','banker2a.png']
health_conf = 0.9
click_conf = 0.8
clean_conf = 0.9

pyautogui.FAILSAFE = False

check = 0

while(True):
    
    if keyboard.is_pressed('q'):
        raise
    
    clean_location = pyautogui.locateCenterOnScreen(tab_grimmy[0],confidence=clean_conf, grayscale=False)
    if(clean_location != None):
        print("cleaning")
        prev_mouse_location = pyautogui.position()
        pyautogui.click(clean_location)
        #pyautogui.moveTo(clean_location)
        for x in range(0,1):
            print(x)
            pyautogui.moveRel(52, 0)
            pyautogui.click()
        pyautogui.moveTo(prev_mouse_location)
        check = 0 
        time.sleep(0.1)
    else:
        check = check +1
        print("check = "+str(check))
            
    if check >= 10:
        szukanie_conf=1
        for z in range(0,len(tab_banker)):
            print("szukanie bankera")
            banker_location = pyautogui.locateCenterOnScreen(tab_banker[z],confidence=click_conf, grayscale=False)
            if(banker_location != None):
                print("banker found")
                prev_mouse_location = pyautogui.position()
                pyautogui.moveTo(banker_location) 
                time.sleep(0.2)
                pyautogui.click(banker_location)
                time.sleep(0.2)
                pyautogui.moveTo(prev_mouse_location) 
                szukanie_conf=1
                while(True):
                    print("deposit clean")
                    print(szukanie_conf)
                    clean_location = pyautogui.locateCenterOnScreen(tab_clean[0],confidence=clean_conf, grayscale=False)
                    if(clean_location != None):
                        print("clean deposited")
                        prev_mouse_location = pyautogui.position()
                        pyautogui.click(clean_location)
                        time.sleep(0.2)
                        pyautogui.moveTo(prev_mouse_location) 
                        break
                    szukanie_conf=szukanie_conf-0.1
                    if(szukanie_conf<0.1):
                        szukanie_conf=0.1

                szukanie_conf=1
                while(True):
                    print("szukanie grimmy")
                    print(szukanie_conf)
                    grimmy_location = pyautogui.locateCenterOnScreen(tab_grimmy[0],confidence=szukanie_conf, grayscale=False)
                    if(grimmy_location != None):
                        print("branie grimmy")
                        prev_mouse_location = pyautogui.position()
                        pyautogui.click(grimmy_location)
                        time.sleep(0.2)
                        pyautogui.moveTo(prev_mouse_location) 
                        break
                    szukanie_conf=szukanie_conf-0.1  
                    if(szukanie_conf<0.1):
                        szukanie_conf=0.1
                        
                szukanie_conf=1
                while(True):
                    print("szukanie close")
                    print(szukanie_conf)
                    close_location = pyautogui.locateCenterOnScreen(tab_close[0],confidence=szukanie_conf, grayscale=False)
                    if(close_location != None):
                        print("klikanie close")
                        prev_mouse_location = pyautogui.position()
                        pyautogui.click(close_location)
                        time.sleep(0.2)
                        pyautogui.moveTo(prev_mouse_location) 
                        check = 0
                        break
                    szukanie_conf=szukanie_conf-0.1  
                    if(szukanie_conf<0.1):
                        szukanie_conf=0.1  
                        
        szukanie_conf=szukanie_conf-0.1
        if(szukanie_conf<0.1):
            szukanie_conf=0.1    
    else:
        print(datetime.now())
