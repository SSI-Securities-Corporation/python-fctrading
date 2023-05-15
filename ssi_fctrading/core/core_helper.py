import random
import string


class core_helper(object):
	def __init__(self):
		self.ping = 'pong'

	@staticmethod
	def random_string(length):
		stringy = string.ascii_lowercase
		return ''.join(random.choice(stringy) for i in range(length))

	@staticmethod
	def to_lower(json_object):
		new = {}
		for k, v in json_object.items():
			if isinstance(v, dict):
				v = core_helper.to_lower(v)
			new[k.lower()] = v
		return new

