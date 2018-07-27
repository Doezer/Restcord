import logging
from enum import Enum
import json

from .models import get_from_kwargs, get_cls_entries
from .models import Role
from .user import User

CDN_URL = "https://cdn.discordapp.com/"
logger = logging.getLogger()


# EMOJI SECTION


class Emoji:
    id = None
    name = None
    roles = None
    user = None
    require_colons = None
    managed = None
    animated = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.name = get_from_kwargs(kwargs, "name")
            self.roles = get_from_kwargs(kwargs, "roles")
            self.user = get_from_kwargs(kwargs, "user")
            self.require_colons = get_from_kwargs(kwargs, "require_colons")
            self.managed = get_from_kwargs(kwargs, "managed")
            self.animated = get_from_kwargs(kwargs, "managed")
