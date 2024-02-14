#pip3 install pyautogui
import pyautogui
import time
from datetime import datetime
import keyboard  # using module keyboard

tab_health = ['low_health_small.png']
#tab_food = ['fish.png','wine.png']
#tab_enemies = ['bugs1.png','bugs2.png']
#tab_enemies = ['ban1.png','ban2.png','ban3.png','ban4.png']
#tab_enemies = ['kal1.png','kal2.png','kal3.png','kal4.png']
tab_enemies = ['troll1.png','troll2.png','troll3.png']
tab_food = ['pie2.png','pie.png','pie_wild.png','pie_wild2.png','shark.png']
tab_drop = ['pie_dish.png']
health_conf = 0.9
click_conf = 0.8
attack_conf = 0.6

pyautogui.FAILSAFE = False
mouse_location_check = pyautogui.position()

while(True):
    
    if keyboard.is_pressed('q'):
        raise
    
    #sprawdzanie czy rusza się myszka
    while(True):
        mouse_location_check_prev = mouse_location_check
        mouse_location_check = pyautogui.position()
        #print(mouse_location_check_prev,mouse_location_check)
        if(mouse_location_check==mouse_location_check_prev):
            print("mouse not moving")
            break
        else:
            print("mouse moving")
        time.sleep(1)
    
    # dropping items
    for z in range(0,len(tab_drop)):
        drop_location = pyautogui.locateCenterOnScreen(tab_drop[z],confidence=click_conf, grayscale=False)
        if(drop_location != None):
            print("dropping")
            prev_mouse_location = pyautogui.position()
            pyautogui.click(drop_location)
            time.sleep(0.2)
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
                time.sleep(0.2)
                pyautogui.moveTo(prev_mouse_location)                        
                break
    else:
        print("zdrowie ok")        
        
    # attacking
    print(attack_conf) 
    combat_location = pyautogui.locateCenterOnScreen('combat.png',confidence=0.9, grayscale=False)
    if(combat_location == None):
        for z in range(0,len(tab_enemies)):
            enemy_location = pyautogui.locateCenterOnScreen(tab_enemies[z],confidence=attack_conf, grayscale=False)
            if(enemy_location != None):
                print("attacking")
                print("po zdj ",tab_enemies[z])
                prev_mouse_location = pyautogui.position()
                pyautogui.moveTo(enemy_location) 
                time.sleep(0.02)
                pyautogui.click(enemy_location)
                time.sleep(0.02)
                pyautogui.moveTo(prev_mouse_location) 
                time.sleep(0.1)
                attack_conf = 0.8
                #time.sleep(5)
            else:
                print("nic")
                attack_conf = attack_conf -0.1
                print("attack_conf",attack_conf)
            if attack_conf < 0.4:
                attack_conf = 0.4   
    else:
        print("in combat") 
        attack_conf = 0.8
        print(datetime.now())
