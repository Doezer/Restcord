from .http import HTTPClient
from .models import *

def get_from_kwargs(kwargs, key):
	if not kwargs:
		return None
	if key not in kwargs:
		return None
	return kwargs[key]

class Restcord:

	def __init__(self, **kwargs):
		token = get_from_kwargs(kwargs, "token")
		if not token:
			raise RuntimeError("You must provide a token")
		selfbot = get_from_kwargs(kwargs, "selfbot")
		if not selfbot:
			selfbot = False
		self.token = token
		self.selfbot = selfbot
		self.http = HTTPClient(self)

	async def get_user(self, id):
		resp = await self.http.get("/users/{}".format(id))
		return User(**resp)