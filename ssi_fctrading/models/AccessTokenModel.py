from datetime import datetime
from . import fcmodel_responses
import jwt

class AccessTokenModel(object):

	def __init__(self, access_token: fcmodel_responses.AccessToken):
		jj = jwt.decode(access_token.accessToken, verify=False, options={"verify_signature": False})
		self._token_expire_at = datetime.fromtimestamp(jj['exp'])
		self._access_token = access_token.accessToken

	def get_access_token(self):
		return self._access_token

	def is_expired(self):
		delta = self._token_expire_at - datetime.now()
		if delta.total_seconds() < 3600:
			return True
		return False