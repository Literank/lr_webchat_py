import socketio

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)

users = {}


@sio.event
async def connect(sid, environ):
    print('A user connected:', sid)


@sio.on('user-join')
async def user_join(sid, user):
    if 'name' not in user:
        return
    print(f"User {sid} => {user['emoji']} {user['name']} joined")
    users[sid] = {**user, 'sid': sid}
    print(list(users.items()))
    # Broadcast to all connected clients
    await sio.emit('contacts', list(users.items()))
