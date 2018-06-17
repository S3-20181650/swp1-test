from UpDown import UpDown

ud=UpDown()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	up.new(count)

	return {'code': 'success'}


def guess(d):
	try:
		guess = d.get('guess', [''])[0]
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	response = up.start(guess)
	trials = up.total()

	return {'code': 'success', 'msg': response, 'trials': trials}
