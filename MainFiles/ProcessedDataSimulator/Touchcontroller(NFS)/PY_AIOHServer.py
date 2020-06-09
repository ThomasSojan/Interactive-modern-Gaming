from aiohttp import web
import socketio
import win32directx as dx



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
        if data.get("accelerator") == True:
            dx.PressKey(0x11)
        if data.get("accelerator") == False:
            dx.ReleaseKey(0x11)    
        if data.get("brake") == True:
            dx.PressKey(0x1F)
        if data.get("brake") == False:
            dx.ReleaseKey(0x1F)
        if data.get("nitro") == True:
            dx.PressKey(0x31)
        if data.get("nitro") == False:
            dx.ReleaseKey(0x31)
        if data.get("handbrake") == True:
            dx.PressKey(0x39)
        if data.get("handbrake") == False:
            dx.ReleaseKey(0x39) 
        
    if data.get("type") == "deviceOrientation":
        beta = data.get("beta")
        if beta > 20:
            #dx.ReleaseKey(0x1E)
            #dx.PressKey(0x20)
            print("right")
                 
        if beta < -20:
            #dx.ReleaseKey(0x20) 
            #dx.PressKey(0x1E)
            print("left")

        if -20 < beta < 20:
            #dx.ReleaseKey(0x20)
            #dx.ReleaseKey(0x1E) 
            print('still')   
            
         

    
    
    
    
    
    
    
    
    
    
app.router.add_get('/', index)
if __name__ == '__main__':
    web.run_app(app)
    
   