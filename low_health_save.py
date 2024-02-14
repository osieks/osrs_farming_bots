#pip3 install pyautogui
import pyautogui
import time
from datetime import datetime
import keyboard  # using module keyboard

tab_health = ['low_health.png']
#tab_food = ['fish.png','wine.png']
#tab_food = ['wine.png']
#tab_food = ['pie2.png','pie.png','shark.png','shark22.png']
tab_food = ['pie2.png','pie.png','pie_wild.png','pie_wild2.png','shark.png']
tab_drop = ['pie_dish.png',"big_bones.png"]
tab_special = ['special.png']
special_conf = 0.95
health_conf = 0.9
click_conf = 0.8

pyautogui.FAILSAFE = False
mouse_location_check = pyautogui.position()
        
while(True):
    
    if keyboard.is_pressed('q'):
        raise
        
    #sprawdzanie czy rusza się myszka
    while(False):
        mouse_location_check_prev = mouse_location_check
        mouse_location_check = pyautogui.position()
        #print(mouse_location_check_prev,mouse_location_check)
        if(mouse_location_check==mouse_location_check_prev):
            print("mouse not moving")
            break
        else:
            print("mouse moving")
        time.sleep(0.2)
        
    # dropping items
    for z in range(0,len(tab_drop)):
        drop_location = pyautogui.locateCenterOnScreen(tab_drop[z],confidence=click_conf, grayscale=False)
        if(drop_location != None):
            print("dropping")
            prev_mouse_location = pyautogui.position()
            pyautogui.click(drop_location)
            time.sleep(0.01)
            pyautogui.moveTo(prev_mouse_location) 
            
    # special
    for z in range(0,len(tab_special)):
        special_location = pyautogui.locateCenterOnScreen(tab_special[z],confidence=special_conf, grayscale=False)
        if(special_location != None):
            print("special")
            prev_mouse_location = pyautogui.position()
            pyautogui.click(special_location)
            time.sleep(0.01)
            pyautogui.moveTo(prev_mouse_location) 
    
    # health check
    low_health = pyautogui.locateCenterOnScreen(tab_health[0],confidence=health_conf, grayscale=False)
    if(low_health != None):
        print("low")
        
        # using food
        for z in range(0,len(tab_food)):
            food_location = pyautogui.locateCenterOnScreen(tab_food[z],confidence=click_conf, grayscale=False)
            if(food_location != None):
                print("healing")
                prev_mouse_location = pyautogui.position()
                pyautogui.click(food_location)
                time.sleep(0.1)
                if(tab_food[z]=='wine.png'):
                    time.sleep(0.01)
                    pyautogui.click(food_location)
                    time.sleep(0.01)
                pyautogui.moveTo(prev_mouse_location)     
                time.sleep(0.5)                   
                break
            print("no food",tab_food[z])
    else:
        print("health ok",datetime.now())
