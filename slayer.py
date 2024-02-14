#pip3 install pyautogui
import pyautogui
import time


tab_targets = ['kalph1.png','kalph2.png','kalph3.png']

def find_red(ilosc_klikniec, czas_walki,debug):
    found = 0
    conf = 1
    conf_step = 0.02

    for i in range(0, ilosc_klikniec):
        while found==0:
            if debug==1:
                print('conf'+str(conf))
            for z in range(0,len(tab_targets)):
                red_location = pyautogui.locateCenterOnScreen(tab_targets[z],confidence=conf)
                if debug==1:
                    print(red_location)
                if(red_location != None):
                    if debug==1:
                        print('found')
                        pyautogui.moveTo(red_location)
                    else:
                        pyautogui.moveTo(red_location)
                        time.sleep(0.1)
                        pyautogui.click(red_location)
                    found = 1
                    print("found")
                    break
                else:
                    conf=conf-conf_step
                    if conf<0.5:
                        conf=0.5
                    print(conf)
        
        conf = 1
        found = 0

        if debug==1:
            for i in range(0,czas_walki):
                time.sleep(1)
                print("Sleeping "+str(i))
        else:
            time.sleep(czas_walki)


ilosc_klikniec = 1000
czas_walki = 15
debug = 0

find_red(ilosc_klikniec,czas_walki,debug)
