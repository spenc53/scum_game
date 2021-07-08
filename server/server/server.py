import eventlet
import socketio

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
    print("command: ", data)
    sio.emit("t", {"test": "respond"})

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)