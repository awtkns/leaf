from . import sio
from ..routes import generate


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
async def start_round(sid, data):

    # sio.enter_room(sid, 'chat_users')
    # store room value somewhere?
	payload = await generate.return_acronyms()
	return "OK", payload

# Send info back with: sio.emit('my event', {'data': 'foobar'})

@sio.event
async def send_answer(sid, data):
	answer = data.answer
	is_correct = True # TODO validate with backend first
	# If everyone has finished {return results}
	return "OK", is_correct

@sio.event
def message(sid, data):
    print('message ', data)
    return "OK", "Hi there"


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
