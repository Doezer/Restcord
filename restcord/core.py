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

	async def get_user_me(self):
		resp = await self.http.get("/users/@me")
		return User(**resp)

	async def modify_user_me(self, data):
		resp = await self.http.patch("/users/@me", data)
		return User(**resp)

	async def get_guilds_me(self):
		resp = await self.http.get("/users/@me/guilds")
		guilds = []
		for guild in resp:
			guilds.append(Guild(guild))
		return guilds

	async def leave_guild(self, id):
		await self.http.delete("/users/@me/guilds/{}".format(id))

	async def get_user_dms(self):
		resp = await self.http.get("/users/@me/channels")
		channels = []
		for chan in resp:
			channels.append(Channel(chan))
		return channels

	async def create_dm(self, recipient_id):
		data = {recipient_id: recipient_id}
		resp = await self.http.post("/users/@me/channels")
		return Channel(**resp)

	async def get_channel(self, id):
		resp = await self.http.get("/channels/{}".format(id))
		return Channel(**resp)

	async def modify_channel(self, id, data):
		resp = await self.http.put("/channels/{}".format(id), data)
		return Channel(**resp)

	async def delete_channel(self, id):
		resp = await self.http.delete("/channels/{}".format(id))
		return Channel(**resp)

	async def get_messages(self, channel_id):
		resp = await self.http.get("/channels/{}/messages".format(channel_id))
		messages = []
		for msg in resp:
			messages.append(Message(msg))
		return messages

	async def get_message(self, channel_id, message_id):
		resp = await self.http.get("/channels/{}/messages/{}".format(channel_id, message_id))
		return Message(**resp)

	async def send_message(self, channel_id, data):
		resp = await self.http.post("/channels/{}/messages".format(channel_id), data)
		return Message(**resp)

	async def add_reaction(self, channel_id, message_id, emoji):
		await self.http.put("/channels/{}/messages/{}/reactions/{}/@me".format(channel_id, message_id, emoji))

	async def remove_reaction(self, channel_id, message_id, emoji)
		await self.http.delete("/channels/{}/messages/{}/reactions/{}/@me".format(channel_id, message_id, emoji))

	async def remove_user_reaction(self, channel_id, message_id, emoji, user_id):
		await self.http.delete("/channels/{}/messages/{}/reactions/{}/{}".format(channel_id, message_id, emoji, user_id))

	async def get_reactions(self, channel_id, message_id, emoji):
		resp = await self.http.get("/channels/{}/messages/{}/reactions/{}".format(channel_id, message_id, emoji))
		users = []
		for user in resp:
			users.append(User(user))
		return users

	async def delete_all_reactions(self, channel_id, message_id):
		await self.http.delete("/channels/{}/messages/{}/reactions".format(channel_id, message_id))

	async def edit_message(self, channel_id, message_id, data):
		resp = await self.http.patch("/channels/{}/messages/{}".format(channel_id, message_id), data)
		return Message(**resp)

	async def delete_message(self, channel_id, message_id):
		await self.http.delete("/channels/{}/messages/{}".format(channel_id, message_id))

	async def get_invites(self, channel_id):
		resp = await self.http.get("/channels/{}/invites".format(channel_id))
		invites = []
		for invite in resp:
			invites.append(Invite(invite))
		return invites

	async def create_invite(self, channel_id, data):
		resp = await self.http.post("/channels/{}/invites".format(channel_id), data)
		return Invite(resp)

	async def send_typing(self, channel_id):
		await self.http.post("/channels/{}/typing".format(channel_id))

	async def get_pinned_messages(self, channel_id):
		resp = await self.http.get("/channels/{}/pins".format(channel_id))
		messages = []
		for msg in resp:
			messages.append(Message(msg))
		return messages

	async def pin_message(self, channel_id, message_id):
		await self.http.put("/channels/{}/pins/{}".format(channel_id, message_id))

	async def unpin_message(self, channel_id, message_id):
		await self.http.delete("/channels/{}/pins/{}".format(channel_id, message_id))

	async def create_guild(self, data):
		resp = await self.http.post("/guilds", data)
		return Guild(resp)

	async def get_guild(self, guild_id):
		resp = await self.http.get("/guilds/{}".format(guild_id))
		return Guild(resp)

	async def modify_guild(self, guild_id, data=None):
		resp = await self.http.patch("/guilds/{}".format(guild_id), data)
		return Guild(resp)

	async def delete_guild(self, guild_id):
		await self.http.delete("/guilds/{}".format(guild_id))
