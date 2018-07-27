from .models.channel import Channel
from .models.guild import Guild
from .models.user import User


class UserCord:

    def __init__(self, restcord):
        self.http = restcord.http

    async def get_user_dms(self):
        resp = await self.http.get("/users/@me/channels")
        channels = []
        for chan in resp:
            channels.append(Channel(**chan))
        return channels

    async def get_user(self, user_id: int):
        resp = await self.http.get("/users/{}".format(user_id))
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
            guilds.append(Guild(**guild))
        return guilds

    async def leave_guild(self, guild_id):
        await self.http.delete("/users/@me/guilds/{}".format(guild_id))
