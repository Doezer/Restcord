from enum import Enum

from .user import User
from .emoji import Emoji
from .models import get_from_kwargs, get_cls_entries, Role

CDN_URL = "https://cdn.discordapp.com/"
import logging
logger = logging.getLogger()


# GUILD SECTION

class FilterLevel(Enum):
    disabled = 0
    members_without_roles = 1
    all_members = 2
    no = None


class ServerRegion(Enum):
    # I should update this.....
    us_west = 'us-west'
    us_east = 'us-east'
    us_south = 'us-south'
    us_central = 'us-central'
    eu_west = 'eu-west'
    eu_central = 'eu-central'
    singapore = 'singapore'
    london = 'london'
    sydney = 'sydney'
    amsterdam = 'amsterdam'
    frankfurt = 'frankfurt'
    brazil = 'brazil'
    vip_us_east = 'vip-us-east'
    vip_us_west = 'vip-us-west'
    vip_amsterdam = 'vip-amsterdam'
    no = None

    def __str__(self):
        return self.value


class VerificationLevel(Enum):
    none = 0
    low = 1
    medium = 2
    high = 3
    table_flip = 3
    very_high = 4
    no = None

    def __str__(self):
        return self.name


class Guild:
    id = None
    name = None
    icon = None
    splash = None
    owner_id = None
    region = None
    afk_channel_id = None
    afk_timeout = None
    embed_enabled = None
    embed_channel_id = None
    verification_level = None
    default_message_notifications = None
    explicit_content_filter = None
    roles = None
    emojis = None
    features = None
    mfa_level = None
    widget_enabled = None
    widget_channel_id = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.name = get_from_kwargs(kwargs, "name")
            self.icon = "{}icons/{}/{}.png".format(CDN_URL, self.id, get_from_kwargs(kwargs, "icon"))
            self.splash = "{}splashes/{}/{}.png".format(CDN_URL, self.id, get_from_kwargs(kwargs, "splash"))
            self.owner_id = get_from_kwargs(kwargs, "owner_id")
            self.afk_channel_id = get_from_kwargs(kwargs, "afk_channel_id")
            self.afk_timeout = get_from_kwargs(kwargs, "afk_timeout")
            self.embed_enabled = get_from_kwargs(kwargs, "embed_enabled")
            self.embed_channel_id = get_from_kwargs(kwargs, "embed_channel_id")
            if get_from_kwargs(kwargs, "region"):
                self.region = ServerRegion(get_from_kwargs(kwargs, "region"))
            if get_from_kwargs(kwargs, "verification_level"):
                self.verification_level = VerificationLevel(get_from_kwargs(kwargs, "verification_level"))
            self.default_message_notifications = get_from_kwargs(kwargs, "default_message_notifications")
            if get_from_kwargs(kwargs, "explicit_content_filter"):
                self.explicit_content_filter = FilterLevel(int(get_from_kwargs(kwargs, "explicit_content_filter")))
            self.roles = get_cls_entries(Role, get_from_kwargs(kwargs, "roles"))
            self.emojis = get_cls_entries(Emoji, get_from_kwargs(kwargs, "emojis"))
            self.features = get_from_kwargs(kwargs, "features")
            self.mfa_level = get_from_kwargs(kwargs, "mfa_level")
            self.widget_enabled = get_from_kwargs(kwargs, "widget_enabled")
            self.widget_channel_id = get_from_kwargs(kwargs, "widget_channel_id")


class GuildEmbed:
    enabled = None
    channel_id = None

    def __init__(self, **kwargs):
        if kwargs:
            self.enabled = get_from_kwargs(kwargs, "enabled")
            self.channel_id = get_from_kwargs(kwargs, "channel_id")


class Integration:
    id = None
    name = None
    type = None
    enabled = None
    syncing = None
    role_id = None
    expire_behavior = None
    expire_grace_period = None
    user = None
    account = None
    synced_at = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.name = get_from_kwargs(kwargs, "name")
            self.type = get_from_kwargs(kwargs, "type")
            self.enabled = get_from_kwargs(kwargs, "enabled")
            self.syncing = get_from_kwargs(kwargs, "syncing")
            self.role_id = get_from_kwargs(kwargs, "role_id")
            self.syncing = get_from_kwargs(kwargs, "syncing")
            self.expire_behavior = get_from_kwargs(kwargs, "expire_behavior")
            self.expire_grace_period = get_from_kwargs(kwargs, "expire_grace_period")
            self.user = User(**get_from_kwargs(kwargs, "user"))
            self.account = IntegrationAccount(**get_from_kwargs(kwargs, "account"))
            self.synced_at = get_from_kwargs(kwargs, "synced_at")


class IntegrationAccount:
    id = None
    name = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.name = get_from_kwargs(kwargs, "name")


class Ban:
    reason = None
    user = None

    def __init__(self, **kwargs):
        if kwargs:
            self.reason = get_from_kwargs(kwargs, "reason")
            self.user = User(**get_from_kwargs(kwargs, "user"))