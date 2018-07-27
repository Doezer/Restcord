from enum import Enum
from .models import get_from_kwargs, get_cls_entries
from .webhook import Webhook
import logging
logger = logging.getLogger()


# MESSAGE SECTION


class MessageType(Enum):
    default = 0
    recipient_add = 1
    recipient_remove = 2
    call = 3
    channel_name_change = 4
    channel_icon_change = 5
    pins_add = 6
    guild_member_join = 7
    no = None


class Message:
    id = None
    channel_id = None
    author = None
    content = None
    timestamp = None
    edited_timestamp = None
    tts = None
    mention_everyone = None
    mentions = None
    mention_roles = None
    attachments = None
    embeds = None
    reactions = None
    nonce = None
    pinned = None
    type = None
    webhook_id = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.channel_id = get_from_kwargs(kwargs, "channel_id")
            self.author = get_from_kwargs(kwargs, "author")
            self.content = get_from_kwargs(kwargs, "content")
            self.timestamp = get_from_kwargs(kwargs, "timestamp")
            self.edited_timestamp = get_from_kwargs(kwargs, "edited_timestamp")
            self.tts = get_from_kwargs(kwargs, "tts")
            self.mention_everyone = get_from_kwargs(kwargs, "mention_everyone")
            self.mentions = get_from_kwargs(kwargs, "mentions")
            self.mention_roles = get_from_kwargs(kwargs, "mention_roles")
            self.attachments = get_from_kwargs(kwargs, "attachments")
            self.embeds = get_from_kwargs(kwargs, "embeds")
            self.reactions = get_from_kwargs(kwargs, "reactions")
            self.nonce = get_from_kwargs(kwargs, "nonce")
            self.pinned = get_from_kwargs(kwargs, "pinned")
            self.webhook_id = get_from_kwargs(kwargs, "webhook_id")
            type = get_from_kwargs(kwargs, "type")
            if type:
                self.type = MessageType(int(type))


class Reaction:
    count = None
    me = None
    emoji = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.me = get_from_kwargs(kwargs, "me")
            self.emoji = get_from_kwargs(kwargs, "emoji")


class Attachment:
    id = None
    filename = None
    size = None
    url = None
    proxy_url = None
    height = None
    width = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.filename = get_from_kwargs(kwargs, "filename")
            self.size = get_from_kwargs(kwargs, "size")
            self.url = get_from_kwargs(kwargs, "url")
            self.proxy_url = get_from_kwargs(kwargs, "proxy_url")
            self.height = get_from_kwargs(kwargs, "height")
            self.width = get_from_kwargs(kwargs, "width")


# EMBED


class EmbedThumbnail:
    url = None
    proxy_url = None
    height = None
    width = None

    def __init__(self, **kwargs):
        if kwargs:
            self.url = get_from_kwargs(kwargs, "url")
            self.proxy_url = get_from_kwargs(kwargs, "proxy_url")
            self.height = get_from_kwargs(kwargs, "height")
            self.width = get_from_kwargs(kwargs, "width")


class EmbedVideo:
    url = None
    height = None
    width = None

    def __init__(self, **kwargs):
        if kwargs:
            self.url = get_from_kwargs(kwargs, "url")
            self.height = get_from_kwargs(kwargs, "height")
            self.width = get_from_kwargs(kwargs, "width")


class EmbedImage:
    url = None
    proxy_url = None
    height = None
    width = None

    def __init__(self, **kwargs):
        if kwargs:
            self.url = get_from_kwargs(kwargs, "url")
            self.proxy_url = get_from_kwargs(kwargs, "proxy_url")
            self.height = get_from_kwargs(kwargs, "height")
            self.width = get_from_kwargs(kwargs, "width")


class EmbedProvider:
    name = None
    url = None

    def __init__(self, **kwargs):
        if kwargs:
            self.name = get_from_kwargs(kwargs, "name")
            self.url = get_from_kwargs(kwargs, "url")


class EmbedAuthor:
    name = None
    url = None
    icon_url = None
    proxy_icon_url = None

    def __init__(self, **kwargs):
        if kwargs:
            self.name = get_from_kwargs(kwargs, "name")
            self.url = get_from_kwargs(kwargs, "url")
            self.icon_url = get_from_kwargs(kwargs, "icon_url")
            self.proxy_icon_url = get_from_kwargs(kwargs, "proxy_icon_url")


class EmbedFooter:
    text = None
    icon_url = None
    proxy_icon_url = None

    def __init__(self, **kwargs):
        if kwargs:
            self.text = get_from_kwargs(kwargs, "text")
            self.icon_url = get_from_kwargs(kwargs, "icon_url")
            self.proxy_icon_url = get_from_kwargs(kwargs, "proxy_icon_url")


class EmbedField:
    name = None
    value = None
    inline = None

    def __init__(self, **kwargs):
        if kwargs:
            self.name = get_from_kwargs(kwargs, "name")
            self.value = get_from_kwargs(kwargs, "value")
            self.inline = get_from_kwargs(kwargs, "inline")


class Embed:
    title = None
    type = None
    description = None
    url = None
    timestamp = None
    color = None
    footer = None
    image = None
    thumbnail = None
    video = None
    provider = None
    author = None
    fields = None

    def __init__(self, **kwargs):
        if kwargs:
            self.title = get_from_kwargs(kwargs, "title")
            self.type = get_from_kwargs(kwargs, "type")
            self.description = get_from_kwargs(kwargs, "description")
            self.url = get_from_kwargs(kwargs, "url")
            self.timestamp = get_from_kwargs(kwargs, "timestamp")
            self.color = get_from_kwargs(kwargs, "color")
            self.footer = EmbedFooter(**get_from_kwargs(kwargs, "footer"))
            self.image = EmbedImage(**get_from_kwargs(kwargs, "image"))
            self.thumbnail = EmbedThumbnail(**get_from_kwargs(kwargs, "thumbnail"))
            self.video = EmbedVideo(**get_from_kwargs(kwargs, "video"))
            self.provider = EmbedProvider(**get_from_kwargs(kwargs, "provider"))
            self.author = EmbedAuthor(**get_from_kwargs(kwargs, "author"))
            self.fields = get_cls_entries(EmbedField, **get_from_kwargs(kwargs, "fields"))

    def __str__(self):
        return json.dumps(self.__dict__)


