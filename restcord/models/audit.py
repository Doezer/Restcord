from enum import Enum
from .models import get_from_kwargs, get_cls_entries
from .webhook import Webhook

CDN_URL = "https://cdn.discordapp.com/"


# AUDIT LOG SECTION


class AuditLog:
    webhooks = None
    users = None
    audit_log_entries = None

    def __init__(self, **kwargs):
        if kwargs:
            self.webhooks = get_cls_entries(Webhook, **get_from_kwargs(kwargs, "webhooks"))
            self.users = get_cls_entries(User, **get_from_kwargs(kwargs, "users"))
            self.audit_log_entries = get_cls_entries(AuditLogEntry, **get_from_kwargs(kwargs, "audit_log_entries"))


class AuditLogEvent(Enum):
    GUILD_UPDATE = 1
    CHANNEL_CREATE = 10
    CHANNEL_UPDATE = 11
    CHANNEL_DELETE = 12
    CHANNEL_OVERWRITE_CREATE = 13
    CHANNEL_OVERWRITE_UPDATE = 14
    CHANNEL_OVERWRITE_DELETE = 15
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72

    def __str__(self):
        return self.action_type


class AuditLogEntry:
    id = None
    target_id = None
    changes = None
    user_id = None
    action_type = None
    options = None
    reason = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.target_id = get_cls_entries(AuditLogChange, **get_from_kwargs(kwargs, "target_id"))
            self.changes = get_from_kwargs(kwargs, "changes")
            self.user_id = get_from_kwargs(kwargs, "user_id")
            if get_from_kwargs(kwargs, "action_type"):
                self.action_type = AuditLogEvent(get_from_kwargs(kwargs, "action_type"))
            self.options = get_cls_entries(AuditLogEntryInfo, get_from_kwargs(kwargs, "options"))
            self.reason = get_from_kwargs(kwargs, "reason")


class AuditLogEntryInfo:
    id = None
    delete_member_days = None
    members_removed = None
    channel_id = None
    count = None
    type = None
    role_name = None

    def __init__(self, **kwargs):
        if kwargs:
            self.id = get_from_kwargs(kwargs, "id")
            self.delete_member_days = get_from_kwargs(kwargs, "delete_member_days")
            self.members_removed = get_from_kwargs(kwargs, "members_removed")
            self.channel_id = get_from_kwargs(kwargs, "channel_id")
            self.count = get_from_kwargs(kwargs, "count")
            self.type = get_from_kwargs(kwargs, "type")
            self.role_name = get_from_kwargs(kwargs, "role_name")


class AuditLogChange:
    new_value = None
    old_value = None
    key = None

    def __init__(self, **kwargs):
        if kwargs:
            self.new_value = get_from_kwargs(kwargs, "id")
            self.old_value = get_from_kwargs(kwargs, "target_id")
            self.key = get_from_kwargs(kwargs, "action_type")
