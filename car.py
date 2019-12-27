import numpy as np
import cv2
import wx
import time
from win32directx import PressKey, W,A,S,D , ReleaseKey,set_pos




app = wx.App(False)
(sx,sy) = wx.GetDisplaySize()
(camx,camy) = (600,600)

lowerBound = np.array([33,80,40])
upperBound = np.array([102,255,255])

cam = cv2.VideoCapture(0)
cam.set(3,camx)
cam.set(4,camy)

kernalOpen = np.ones((5,5))
kernalClose = np.ones((20,20))

mLocOld =np.array([0,0])
mouseLoc = np.array([0,0])
DampingFactor = 2 #should be greater than 1

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


while True:
    ret, img = cam.read()
   # img = cv2.resize(img,()
    img = cv2.flip(img,1)

    #convert BGR to HSV
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #create mask
    mask = cv2.inRange(imgHSV,lowerBound,upperBound)

    #morphology
    maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernalOpen)
    maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernalClose)

    maskFinal = maskClose
    conts,h = cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)    

    if (len(conts) == 1):
        x1,y1,h1,w1 = cv2.boundingRect(conts[0])
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        cx1=x1+w1//2
        cy1=y1+h1//2
        cv2.circle(img,(cx1,cy1),2,(0,0,255),2)
        print(cy1)      
        if(cy1<250):
            PressKey(A)
            time.sleep(0.05)
            ReleaseKey(A)
        if(cy1>300):
            PressKey(D)
            time.sleep(0.05)
            ReleaseKey(D)    
        

        
        



    
   

    cv2.imshow("maskClose",maskClose)
    cv2.imshow("maskOpen",maskOpen)
    cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(5)    