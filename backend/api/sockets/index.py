from . import sio
from ..routes import generate

# Overview:
# Client connects when they open the webpage
# Client emits a join_room event when the click play
# join_room will link the client to a room on the socket
# When the game has enough people to start / is forced to start
#	start_round data will be emitted to all clients within the room
# Once everyone has returned answers, results will be emitted, wait, then the next round emitted


@sio.event
def connect(sid, environ):
	print('connect ', sid)


@sio.event
async def join_room(sid, data):
	# Get connection information
	name = 'testName' # TODO get name from data
	# TODO generate new room if needed, use one room for now
	room = 'test'

	# Save connection information
	await sio.save_session(sid, {
		'name': name,
		'room': room
	})

	sio.enter_room(sid, room)
	return "OK", "Joined room"


@sio.event
async def start_game(sid, data):
	await start_round()
	return "OK"


async def start_round():
	data = await generate.return_acronyms()
	await sio.emit('round_start', data, room='test') # TODO add room


@sio.event
async def send_answer(sid, data):
	# Validate answer
	answer = data['answer']
	is_correct = True # TODO validate answer with backend

	# Start new round if needed
	# TODO only start new round / return results if everyone has finished
	await start_round()

	# TODO only return results if everyone has finished
	return "OK", is_correct


@sio.event
def message(sid, data):
    print('message ', data)
    return "OK", "Hi there"


@sio.event
def disconnect(sid):
	print('disconnect ', sid)
