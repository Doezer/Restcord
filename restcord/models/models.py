import logging

CDN_URL = "https://cdn.discordapp.com/"
logger = logging.getLogger()

# COMMON SECTION


def get_from_kwargs(kwargs, key):
    if not kwargs:
        return None
    if key not in kwargs:
        return None
    return kwargs[key]


def get_cls_entries(cls, entries):
    if not entries:
        return []
    real_entries = []
    for e in entries:
        real_entries.append(cls(**e))
    return real_entries


class Role:
    id = None
    name = None
    color = None
    hoist = None
    position = None
    permissions = None
    managed = None
    mentionable = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.name = get_from_kwargs(kwargs, "name")
            self.color = get_from_kwargs(kwargs, "color")
            self.hoist = get_from_kwargs(kwargs, "hoist")
            self.position = get_from_kwargs(kwargs, "position")
            self.permissions = get_from_kwargs(kwargs, "permissions")
            self.managed = get_from_kwargs(kwargs, "managed")
            self.mentionable = get_from_kwargs(kwargs, "mentionable")