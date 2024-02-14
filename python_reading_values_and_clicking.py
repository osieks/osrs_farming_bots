 #Now it's working. Give your pytess path here:
 #pytesseract.pytesseract.tesseract_cmd = r' ' 
 #& check it out! 

import numpy as np
import cv2
from PIL import ImageGrab as ig
import pytesseract as pt
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r''

def screencap():
    while(True):
        screen = np.array(ig.grab(bbox=(807,987,957,1035)))
        gray = cv2.cvtColor(screen,cv2.COLOR_RGB2GRAY)
        cv2.imshow("test", gray)
        if cv2.waitKey(25) & 0xFF == ord('e'):
            cv2.destroyAllWindows()
            break

image_data = pytesseract.image_to_data(screencap(), 
output_type=Output.DICT)

print(image_data)