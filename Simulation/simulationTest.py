import time
from directkeys import set_pos


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

# X-max = 1920
#X-Right
'''
for i in range(1920):
        set_pos(i,0)
        time.sleep(0.025)'''

# X-Left
'''
for i in range(1920,0,-1):
        set_pos(i,0)
        time.sleep(0.025)
'''
# Y-max = 800
#Aim-Y-Down
'''
i = 1.0
inc = 0.01
while(i<50.5):
    set_pos(0,i)
    time.sleep(0.025)
    i = i + inc '''

# Aim-Y-Up
'''
i = 50.00
dec = 0.01
while(i>1.0):
    set_pos(0,i)
    time.sleep(0.025)
    i = i - dec'''









       




