from .models import get_from_kwargs, get_cls_entries

CDN_URL = "https://cdn.discordapp.com/"
import logging
logger = logging.getLogger()


# WEBHOOK SECTION


class Webhook:
    id = None
    guild_id = None
    channel_id = None
    user = None
    name = None
    avatar = None
    token = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.guild_id = get_from_kwargs(kwargs, "guild_id")
            self.channel_id = get_from_kwargs(kwargs, "channel_id")
            self.user = get_cls_entries(User, get_from_kwargs(kwargs, "user"))
            self.name = get_from_kwargs(kwargs, "name")
            self.avatar = get_from_kwargs(kwargs, "avatar")
            self.token = get_from_kwargs(kwargs, "token")