import cv2
import numpy as np
from keras.models import load_model
import win32directx as directx

classifier = load_model('models/subControl.h5')

print('Tensorflow loaded...')


REV_CLASS_MAP ={0: 'vertical_down',
 1: 'grab',
 2: 'vertical_up',
 3: 'horizontal_right',
 4: 'pist',
 5: 'horizontal_left',
 6: 'thumps_up',
 7: 'release'}

(camx,camy) = (1000,900)
cap = cv2.VideoCapture(0)
cap.set(3,camx)
cap.set(4,camy)
x=238
y=400
 
 
 
def mapper(val):
    return REV_CLASS_MAP[val]








while(True):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame, (350, 150), (650,350), (0, 255, 0), 2)


    image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(227,227))
    pred = classifier.predict(np.array([image]))
    move_code = np.argmax(pred[0])
    move_name = mapper(move_code)
    
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Gesture : " + move_name,
                (50, 50), font, 1.2, (130, 255, 255), 2, cv2.LINE_AA)
    
    if move_name == 'thumps_up':
        x = 238
        y = 415
        directx.set_pos(x,y)
    if move_name == 'grab' :
        directx.left_clicked()
    if move_name == "release":
        directx.left_released()  
    if move_name == 'vertical_down':
        if y > 550:
            y = 550
        else:
            y = y + 1    
        directx.set_pos(x,y)
        
        print (x,y)
    if move_name == 'vertical_up':
        if y < 250:
            y = 250
        else:
            y = y - 1    
        directx.set_pos(x,y)
       
        print(x,y)
    if move_name == 'horizontal_right':
        if x > 350:
            x = 350
        else:
            x = x + 1    
        directx.set_pos(x,y)
         
        print(x,y) 
    if move_name == 'horizontal_left':
        if x < 150:
            x = 150
        else:
            x = x - 1    
        directx.set_pos(x,y)
        
        print(x,y)         

    
    cv2.imshow("Main Frame", frame)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()