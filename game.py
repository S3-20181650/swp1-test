from UpDown import updown

ud=updown()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	ud.new(count)

	return {'code': 'success'}


def guess(d):
	try:
		guess = int(d.get('guess', [''])[0])
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	response = ud.start(guess)
	trials = ud.total()

	return {'code': 'success', 'msg': response, 'trials': trials}
