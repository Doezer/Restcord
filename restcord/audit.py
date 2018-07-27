from .models.audit import *


class AuditCord:

    def __init__(self, restcord):
        self.http = restcord.http

    async def get_guild_audit_log(self, guild_id: int):
        resp = await self.http.get("/guilds/{}/audit-logs".format(guild_id))
        return AuditLog(**resp)
