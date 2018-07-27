from enum import Enum
from .models import get_from_kwargs, get_cls_entries
from .webhook import Webhook


class ChannelType(Enum):
    text = 0
    private = 1
    voice = 2
    group = 3

    def __str__(self):
        return self.name


class Channel:
    id = None
    type = None
    guild_id = None
    position = None
    permission_overwrites = None
    name = None
    topic = None
    last_message_id = None
    bitrate = None
    user_limit = None
    recipients = None
    icon = None
    owner_id = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            type = get_from_kwargs(kwargs, "type")
            if type:
                self.type = ChannelType(int(type))
            self.guild_id = get_from_kwargs(kwargs, "guild_id")
            self.position = get_from_kwargs(kwargs, "position")
            self.permission_overwrites = get_cls_entries(Overwrite, **get_from_kwargs(kwargs, "permission_overwrites"))
            self.name = get_from_kwargs(kwargs, "name")
            self.topic = get_from_kwargs(kwargs, "topic")
            self.last_message_id = get_from_kwargs(kwargs, "last_message_id")
            self.bitrate = get_from_kwargs(kwargs, "bitrate")
            self.user_limit = get_from_kwargs(kwargs, "user_limit")
            self.recipients = get_from_kwargs(kwargs, "recipients")
            self.icon = get_from_kwargs(kwargs, "icon")
            self.owner_id = get_from_kwargs(kwargs, "owner_id")


class Overwrite:
    id = None
    type = None
    allow = None
    deny = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.type = get_from_kwargs(kwargs, "type")
            self.allow = get_from_kwargs(kwargs, "allow")
            self.deny = get_from_kwargs(kwargs, "deny")