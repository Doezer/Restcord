from .channel import Channel
from .guild import Guild
from .models import get_cls_entries, get_from_kwargs

CDN_URL = "https://cdn.discordapp.com/"
import logging
logger = logging.getLogger()


# INVITE SECTION


class Invite:
    code = None
    guild = None
    channel = None

    def __init__(self, **kwargs):
        if kwargs:
            self.code = get_from_kwargs(kwargs, "code")
            self.guild = Guild(**get_from_kwargs(kwargs, "guild"))
            self.channel = Channel(**get_from_kwargs(kwargs, "channel"))

