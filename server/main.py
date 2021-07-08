from server.game_manager import GameManager
import eventlet
import socketio
import json
from json import JSONEncoder

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

from server.commands.command_factory import CommandFactory

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    sio.emit("t", {"test": "test"})
    print('connect ', sid)
    sio.send("data", to=sid)

@sio.event
def my_message(sid, data):
    print('message ', data, sid)

@sio.on('command')
def process_command(sid, data):
    data = json.loads(data)
    command = CommandFactory.createCommand(data)
    commandsToReturn = command.execute()
    print(commandsToReturn[0])
    print(GameManager.getInstance().players)
    # sio.send("data", to=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)