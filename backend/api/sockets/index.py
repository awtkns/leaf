from . import sio
from ..routes import generate

# Overview:
# Client connects when they open the webpage
# Client emits a join_room event when the click play
# join_room will link the client to a room on the socket
# When the game has enough people to start / is forced to start
#	start_round data will be emitted to all clients within the room
# Once everyone has returned answers, results will be emitted, wait, then the next round emitted


# Join game -> instantly populated with the current question, create question other wise
# Someone picks -> 10 seconds for everyone else before (Start in a different thread)

ROUND_DELAY = 10

global round_data
global_round_data = None


@sio.event
def connect(sid, environ):
	print('connect ', sid)


@sio.event
async def join_game(sid, data):
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

	# Get current round or start a new round
	if(global_round_data == None):
		await create_new_round()

	return "OK", global_round_data


async def start_round():
	round_data = await create_new_round()
	await sio.emit('round_start', round_data, room='test') # TODO add room


async def create_new_round():
	print('Starting new round')
	global global_round_data 
	global_round_data = await generate.return_acronyms()
	print(global_round_data)
	return global_round_data


async def new_round(delay):
	print('waiting to start new round')
	await sio.sleep(delay)
	await create_new_round()


@sio.event
async def send_answer(sid, data):
	# Validate answer
	print('Answer validation')

	answer = data['answer']
	is_correct = True # TODO validate answer with backend

	# Start new round if needed
	# TODO only start new round / return results if everyone has finished
	# await start_round()
	sio.start_background_task(new_round, ROUND_DELAY)

	# TODO only return results if everyone has finished
	return "OK", is_correct



@sio.event
def message(sid, data):
    print('message ', data)
    return "OK", "Hi there"


@sio.event
def disconnect(sid):
	print('disconnect ', sid)
