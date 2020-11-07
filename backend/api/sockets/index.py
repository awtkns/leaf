from . import sio
from ..routes import generate

import random
import string


def get_random_string(length=6):
	letters = string.ascii_letters
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str


def get_random_words():
	return [get_random_string() for _ in range(4)]

# Overview:
# Client connects when they open the webpage
# Client emits a join_room event when the click play
# join_room will link the client to a room on the socket
# When the game has enough people to start / is forced to start
#	start_round data will be emitted to all clients within the room
# Once everyone has returned answers, results will be emitted, wait, then the next round emitted


# Join game -> instantly populated with the current question, create question other wise
# Someone picks -> 10 seconds for everyone else before (Start in a different thread)

ROUND_DELAY = 1

global global_round_data
global_round_data = None

global countdown_timer
countdown_timer = False


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
		await new_round()

	return "OK", global_round_data


async def new_round():
	print('Starting new round')
	global global_round_data
	global_round_data = await generate.return_acronyms()
	global_round_data['words'] = get_random_words()
	print(global_round_data)

	print('emiting round start')
	await sio.emit('round_start', global_round_data) # TODO add room

	global countdown_timer
	countdown_timer = False


async def round_timer(delay):

	# Create a timer for the new round if one does not exist already
	if not countdown_timer:
		await sio.sleep(delay)
		await new_round()


@sio.event
async def send_answer(sid, data):
	# Validate answer
	print('Answer validation')

	answer = data['answer']
	is_correct = True  # TODO validate answer with backend
	if is_correct:
		sio.start_background_task(round_timer, ROUND_DELAY)




	# Start new round if needed
	# TODO only start new round / return results if everyone has finished
	# await start_round()


	# TODO only return results if everyone has finished
	return "OK", is_correct



@sio.event
def message(sid, data):
    print('message ', data)
    return "OK", "Hi there"


@sio.event
def disconnect(sid):
	print('disconnect ', sid)
