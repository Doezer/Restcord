import logging

from .exceptions import *
from .models.guild import Emoji

logger = logging.getLogger()


class EmojiCord:

    def __init__(self, restcord):
        self.http = restcord.http

    async def get_guild_emojis(self, guild_id):
        resp = await self.http.get("/guilds/{}/emojis".format(guild_id))
        emojis = []
        for e in resp:
            emojis.append(Emoji(**e))
        return emojis

    async def create_guild_emoji(self, guild_id, data):
        resp = await self.http.post("/guilds/{}/emojis".format(guild_id), data)

        if 'Missing Permissions' in str(resp):
            raise GuildPermissionsError('The current account does not have the MANAGE EMOJI permission.')
        elif 'Maximum number of emojis reached (50)' in str(resp):
            raise GuildEmojisFull('The current guild emote storage is full.')
        return Emoji(**resp)
