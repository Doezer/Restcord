import logging

from .user import UserCord
from .channel import ChannelCord
from .emoji import EmojiCord
from .guild import GuildCord
from .invite import InviteCord
from .audit import AuditCord
from .exceptions import *
from .http import HTTPClient
from .models import *


# TODO : separate these requests in logical classes.

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
            selfbot = False
        else:
            self.selfbot = selfbot
        loop = get_from_kwargs(kwargs, "loop")
        if not loop:
            loop = False
        else:
            self.loop = loop
        proxy_url = get_from_kwargs(kwargs, "proxy_url")
        proxy_auth = get_from_kwargs(kwargs, "proxy_auth")
        if proxy_url:
            self.http = HTTPClient(self, proxy_url, proxy_auth, loop=self.loop)
        else:
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
