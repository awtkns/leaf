from . import sio
from ..routes import generate

# Overview, client connects when the open the webpage
# Client emits a join_room event when the click play
# join_room will link the client to a room on the socket
# When the game has enough people to start / is forced to start
#	start_round data will be emitted to all clients within the room

@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
async def join_room(sid, data):
	# Get connection information
	name = 'testName' # TODO get name from data
	# TODO generate new room if needed, use just one room for now
	room = 'test'
	print('vals', name, room, sid)
	# Save connection information
	await sio.save_session(sid, {
		'name': name,
		'room': room
	})

	sio.enter_room(sid, room)
	return "OK", "Joined room"


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
