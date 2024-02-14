#pip3 install pyautogui
import pyautogui
import time
import keyboard  # using module keyboard

tab_items = ['pouch2.png','neck.png']
tab_health = ['low_health_small.png','wine.png']
tab_zdjec = ['ard_pink2.png','ard_pink_right.png','ard_pink_back.png']
#tab_zdjec = ['farm1.png','farm2.png','farm3.png']
tab_pick = ['pickpocket.png']
#tab_pick = ['pickpocket_farmer.png']
item_conf = 0.85
health_conf = 0.9
click_conf = 0.8


pyautogui.FAILSAFE = False

def find_red(czas_walki,debug):
    
    conf_start = 0.6
    conf_step = 0.1
    conf_min = 0.4
        
    found = 0
    conf = conf_start
    
    print('no. images= '+str(len(tab_zdjec)))
    while(True):
        if keyboard.is_pressed('q'):
            raise
        while found==0:
            if keyboard.is_pressed('q'):
                raise
            print('conf'+str(conf))

            red_location = None
            for z in range(0, len(tab_items)):
                item_location = pyautogui.locateCenterOnScreen(tab_items[z],confidence=item_conf, grayscale=False)
                if(item_location != None):
                    if(z==0):
                        print("pouch")
                    elif(z==1):
                        print("neck")
                    prev_mouse_location = pyautogui.position()
                    pyautogui.click(item_location)
                    time.sleep(0.2)
                    pyautogui.moveTo(prev_mouse_location)
                    
            low_health = pyautogui.locateCenterOnScreen(tab_health[0],confidence=health_conf, grayscale=False)
            if(low_health != None):
                wine_location = pyautogui.locateCenterOnScreen(tab_health[1],confidence=click_conf, grayscale=False)
                print("healing")
                
                prev_mouse_location = pyautogui.position()
                pyautogui.click(wine_location)
                time.sleep(1)
                pyautogui.click(wine_location)
                time.sleep(0.2)
                pyautogui.moveTo(prev_mouse_location)
            
            for z in range(0, len(tab_zdjec)):
                red_location = pyautogui.locateCenterOnScreen(tab_zdjec[z],confidence=conf, grayscale=False)
                if(red_location != None):
                    print(tab_zdjec[z])
                    break
                
            if debug==1:
                print(red_location)
            if(red_location != None):
                prev_mouse_location = pyautogui.position()
                pyautogui.moveTo(red_location)
                found = 1
                
                pick_location = pyautogui.locateOnScreen(tab_pick[0],confidence=click_conf, grayscale=False)
                if(pick_location != None):
                    if debug==1:
                        print('found pick')
                    pyautogui.click(red_location)
                    time.sleep(0.2)
                
                pyautogui.moveTo(prev_mouse_location)
           
            else:
                conf=conf-conf_step
                if conf<conf_min:
                    conf=conf_start
            
        
        conf = conf_start
        found = 0

        if debug==1:
            for i in range(0,czas_walki):
                time.sleep(0)
                print("Sleeping "+str(i))
        else:
            time.sleep(czas_walki)

czas_walki = 0
debug=0

find_red(czas_walki,debug)
