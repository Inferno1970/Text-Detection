# import sys

# sys.path.append(r'C:\Users\sepeh\AppData\Local\Programs\Python\Python310\Lib\site-packages')

import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

#read image

image_path=r'D:\Data Science\Python Assignment\Computer Vision\text-detection-python-easyocr-master\data\test1.png'

img=cv2.imread(image_path)
# img = Image.open(image_path)
#instance text on image
reader= easyocr.Reader(['en'], gpu=False)

# cv2.imshow('Road Sign', img)
# cv2.waitKey(0)

#detect text on image
text_= reader.readtext(img)



threshold=0.25
#draw box and text
for t in text_:
    print(text_)
    bbx,text,score=text_
    if score>threshold:
        cv2.rectangle(img,bbx[0],bbx[3],(0,255,0),5)  #upper lef corner and bottom right corner, color, thickness
        cv2.putText(img,text,bbx[0],cv2.FONT_HERSHEY_COMPLEX,0.65,(255,0,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)) #changing color space
plt.show