import numpy as np
import cv2
import wx
import time
from win32directx import PressKey, UP,LEFT,RIGHT,DOWN,LSH , ReleaseKey,set_pos


g_detect = False
b_detect = False

app = wx.App(False)
(sx,sy) = wx.GetDisplaySize()
(camx,camy) = (600,600)

glb = np.array([33,80,40])
gub = np.array([72,255,255])

rlb = np.array([90,86,0])
rub = np.array([121,255,255])

cam = cv2.VideoCapture(0)
cam.set(3,camx)
cam.set(4,camy)

kernalOpen = np.ones((5,5))
kernalClose = np.ones((20,20))



for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


while True:
    ret, img = cam.read()
   # img = cv2.resize(img,()
    img = cv2.flip(img,1)
    img = cv2.GaussianBlur(img,(5,5),0)
    blue = (255,0,0)
    cv2.line(img,(200,0),(200,600),blue,thickness=1)
    cv2.line(img,(400,0),(400,600),blue,thickness=1)
    cv2.line(img,(0,200),(640,200),blue,thickness=1)
    cv2.line(img,(0,400),(640,400),blue,thickness=1)



    #convert BGR to HSV
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #create mask
    mask = cv2.inRange(imgHSV,glb,gub)
    mask2 = cv2.inRange(imgHSV,rlb,rub)


    #morphology
    maskOpen = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernalOpen)
    maskOpen2 = cv2.morphologyEx(mask2,cv2.MORPH_OPEN,kernalOpen)

    maskClose = cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernalClose)
    maskClose2 = cv2.morphologyEx(maskOpen2,cv2.MORPH_CLOSE,kernalClose)


    maskFinal = maskClose
    maskFinal2 = maskClose2
   
    g_conts,h = cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)   
    r_conts,h = cv2.findContours(maskFinal2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for cont in g_conts:
        areag = cv2.contourArea(cont)
        if areag > 1000 :
            
            g_detect = True
        else:
            g_detect = False
  
    for cont in r_conts:
        areab = cv2.contourArea(cont)
        if areab > 1000 :
            
            b_detect = True       
        else:
            b_detect = False

    if (g_detect == True):
        x1,y1,h1,w1 = cv2.boundingRect(g_conts[0])
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        cx=x1+w1//2
        cy=y1+h1//2
        cv2.circle(img,(cx,cy),2,(0,0,255),2)
          
        
        if(cx > 400):
            PressKey(LSH)
            PressKey(RIGHT)
            time.sleep(0.05)
            ReleaseKey(RIGHT)
            ReleaseKey(LSH)
            print("RSMODE")
        if(cx < 200):
            PressKey(LSH)
            PressKey(LEFT)
            time.sleep(0.05)
            ReleaseKey(LEFT)
            ReleaseKey(LSH)
            print("LSMODE")
        if(cy < 200):

            PressKey(UP)
            time.sleep(0.05)
            ReleaseKey(UP)
            print("UPMODE")


    elif(b_detect == True):
        x1,y1,h1,w1 = cv2.boundingRect(r_conts[0])
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
        cx=x1+w1//2
        cy=y1+h1//2
        cv2.circle(img,(cx,cy),2,(0,0,255),2)
          
        
        if(cx > 400):

            PressKey(RIGHT)
            time.sleep(0.05)
            ReleaseKey(RIGHT)
            print("RRMODE")
        if(cx < 200):

            PressKey(LEFT)
            time.sleep(0.05)
            ReleaseKey(LEFT)
            print("LRMODE")
        if(cy < 200):

            PressKey(UP)
            time.sleep(0.05)
            ReleaseKey(UP)
            print("UPMODE")


        

    
   

   # cv2.imshow("maskClose2",maskClose)
   # cv2.imshow("maskOpen",maskOpen)
   # cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.waitKey(1)    


    # git toutorial 