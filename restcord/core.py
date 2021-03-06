import asyncio
import logging

from .user import UserCord
from .channel import ChannelCord
from .emoji import EmojiCord
from .guild import GuildCord
from .invite import InviteCord
from .audit import AuditCord
from .exceptions import *
from .http_client import HTTPClient
from .models import *

logger = logging.getLogger()


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
        else:
            self.token = token
        selfbot = get_from_kwargs(kwargs, "selfbot")
        if not selfbot:
            self.selfbot = False
        else:
            self.selfbot = selfbot
        loop = get_from_kwargs(kwargs, "loop")
        if not loop:
            self.loop = asyncio.get_event_loop()
        else:
            self.loop = loop
        self.http = HTTPClient(self, loop=self.loop)
        self.UserCord = UserCord(self)
        self.ChannelCord = ChannelCord(self)
        self.EmojiCord = EmojiCord(self)
        self.GuildCord = GuildCord(self)
        self.InviteCord = InviteCord(self)
        self.AuditCord = AuditCord(self)

    async def close(self):
        await self.http.close()
        pass
