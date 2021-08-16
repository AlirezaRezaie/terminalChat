import asyncio
import socketio
import winsound
from aioconsole import ainput

greetings_message = """
┌──────────────────────────────────┐
│                                  │
│   salam bar dost daran moein     │
│                                  │
│                                  │
│   be server global chat khoshamadid
│                                  │
│  -ridam                          │
│                                  │
│  lotfan adab ra raiat konid      │
│                                  │
│                                  │
│  moein sama will always watch you│
│                                  │
│                                  │
└──────────────────────────────────┘
"""

sio = socketio.AsyncClient()
client_name = input("please enter your name: ")

@sio.event
async def connect():
    await sio.emit('clientJoined',{'clientName':client_name})
    await sio.emit('successHandler',{})
    print('connection established')
    print(greetings_message)
    

@sio.event
async def success(event):
    if 'message'in  event:
        print(f"<{event['author']}>{event['message']}")
        winsound.Beep(200,200)

    # waiting for the user to fill the input   
    client_messages = await ainput("")
        
    if client_messages == "quit":
        await sio.emit('disconnection',{"message":f"{client_name} left the room"})
        await asyncio.sleep(.1)
        await sio.disconnect()
        
    else:
        await sio.emit('message',{"message":client_messages,"author":client_name} )

"""
  note that sio.emit('successHandler') redirect's user to the success function
  which is the main terminal chat
"""
    
@sio.event
async def clientLeaved(event):
    print(event["message"])
    await sio.emit('successHandler',{})
@sio.event
async def clientJoined(event):
    print(event["clientName"]+" joined")
    await sio.emit('successHandler',{})
@sio.event
async def disconnect():
    print('disconnected from server(press enter to exit)')

async def main():
    try:
       await sio.connect('https://socket-server884.herokuapp.com/')
    except Exception as e:
        print(f"server refused to connect {e}")
    await sio.wait()

if __name__ == '__main__':   
    asyncio.run(main())
