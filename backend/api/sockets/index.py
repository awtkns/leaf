from . import sio


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
async def join_room(sid, data):
	# TODO generate new room if needed, use just one room for now
	await sio.save_session(sid, {'username': username})
	is_joined = await sio.enter_room(sid, 'chat_users')
	return "OK" if is_joined else "ERROR"


async def start_game():
    # data = get_round_data()
    # sio.emit('round_start', data, room= get room value here)
    pass


@sio.event
async def send_value(sid, data):
    # value = data.answer
    # is_correct = test_value(value)
    # If everyone has finished {return results}
    sio.enter_room(sid, 'chat_users')
    # store room value somewhere?
    pass

# Send info back with: sio.emit('my event', {'data': 'foobar'})


@sio.event
def message(sid, data):
    print('message ', data)
    return False, "yes"


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
