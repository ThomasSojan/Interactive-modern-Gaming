from aiohttp import web
import socketio
import win32directx as dx


camx = [500.0]
camy = [500.0]
sio = socketio.AsyncServer()

app = web.Application()

sio.attach(app)


async def index(request):
    with open('indexSensor.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.on('message')
@sio.event

async def my_event(sid, data):
    print(data)
    if data.get("type") == "eventHandler":
        if data.get("forward") == True:
            dx.PressKey(0x11)
        if data.get("forward") == False:
            dx.ReleaseKey(0x11)    
        if data.get("backward") == True:
            dx.PressKey(0x1F)
        if data.get("backward") == False:
            dx.ReleaseKey(0x1F)
        if data.get("left") == True:
            dx.PressKey(0x1E)
        if data.get("left") == False:
            dx.ReleaseKey(0x1E)
        if data.get("right") == True:
            dx.PressKey(0x20)
        if data.get("right") == False:
            dx.ReleaseKey(0x20) 
        if data.get("jump") == True:
            dx.PressKey(0x39)
        if data.get("jump") == False:
            dx.ReleaseKey(0x39)
        if data.get("fire") == True:
            dx.PressKey(0x21)
        if data.get("fire") == False:
            dx.ReleaseKey(0x21)
        if data.get("aim") == True:
            dx.PressKey(0x10)
        if data.get("aim") == False:
            dx.ReleaseKey(0x10)               
        if data.get("crouch") == True:
            dx.PressKey(0x2E)
        if data.get("crouch") == False:
            dx.ReleaseKey(0x2E)
    if data.get("type") == "deviceOrientation":
        if data.get("beta") > 20:
            temp = camx[-1]
            temp = temp + 0.3
            camx.append(temp)
            dx.set_pos(camx[-1],camy[-1])        
        if data.get("beta") < -20:
            temp = camx[-1]    
            temp = temp - 0.3
            camx.append(temp)
            dx.set_pos(camx[-1],camy[-1])
        if data.get("gamma") < -20:
            tempy = camy[-1]
            tempy = tempy - 0.3
            camy.append(tempy)
            dx.set_pos(camx[-1],camy[-1])
        if data.get("gamma") > 20:
            tempy = camy[-1]
            tempy = tempy + 0.3
            camy.append(tempy)
            dx.set_pos(camx[-1],camy[-1])    


    
    
    
    
app.router.add_get('/', index)
if __name__ == '__main__':
    web.run_app(app)
    
   