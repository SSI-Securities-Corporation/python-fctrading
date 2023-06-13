import base64
import json
from xml.etree.ElementTree import fromstring
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from xmljson import badgerfish as bf
class core_crypto(object):
	def _init_(self):
		self.ping = 'pong'

	@staticmethod
	def getRSAKey(private_key: str):
		key = base64.b64decode(private_key.encode('utf-8'))
		key_json = json.loads(json.dumps(bf.data(fromstring(key))))
		cc = key_json['RSAKeyValue']
		n = int.from_bytes(base64.b64decode(cc['Modulus']['$']), byteorder='big')
		e = int.from_bytes(base64.b64decode(cc['Exponent']['$']), byteorder='big')
		d = int.from_bytes(base64.b64decode(cc['D']['$']), byteorder='big')
		p = int.from_bytes(base64.b64decode(cc['P']['$']), byteorder='big')
		q = int.from_bytes(base64.b64decode(cc['Q']['$']), byteorder='big')
		#u = int.from_bytes(base64.b64decode(cc['InverseQ']['$']), byteorder='big')
		return RSA.construct((n, e, d, p, q))

	@staticmethod
	def sign(data: str, private_key: str):
		h = SHA256.new(data)
		rsa_key = core_crypto.getRSAKey(private_key)
		return pkcs1_15.new(rsa_key).sign(h).hex()

	@staticmethod
	def sign(data: str, rsa_key: RSA.RsaKey):
		print(data)
		h = SHA256.new(data.encode('utf-8'))
		return pkcs1_15.new(rsa_key).sign(h).hex()

