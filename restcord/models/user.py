import logging

from .models import get_from_kwargs, get_cls_entries

CDN_URL = "https://cdn.discordapp.com/"

logger = logging.getLogger()

# USER SECTION


class User:
    id = None
    username = None
    discriminator = None
    avatar = None
    bot = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.username = get_from_kwargs(kwargs, "username")
            self.discriminator = get_from_kwargs(kwargs, "discriminator")
            self.avatar = get_from_kwargs(kwargs, "avatar")
            self.bot = get_from_kwargs(kwargs, "bot")


class GuildMember(User):
    nick = None
    roles = None
    joined_at = None
    deaf = None
    mute = None

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**get_from_kwargs(kwargs, "user"))
            self.nick = get_from_kwargs(kwargs, "nick")
            self.roles = get_from_kwargs(kwargs, "roles")
            self.joined_at = get_from_kwargs(kwargs, "joined_at")
            self.deaf = get_from_kwargs(kwargs, "deaf")
            self.mute = get_from_kwargs(kwargs, "mute")