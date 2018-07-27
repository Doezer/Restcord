import logging

from .models.channel import Channel
from .models.guild import Guild, Ban, Role, Integration, GuildEmbed
from .models.invite import Invite
from .models.user import User, GuildMember


class GuildCord:

    def __init__(self, restcord):
        self.http = restcord.http

    async def create_guild(self, data):
        resp = await self.http.post("/guilds", data)
        return Guild(**resp)

    async def get_guild(self, guild_id):
        resp = await self.http.get("/guilds/{}".format(guild_id))
        return Guild(**resp)

    async def modify_guild(self, guild_id, data=None):
        resp = await self.http.patch("/guilds/{}".format(guild_id), data)
        return Guild(**resp)

    async def delete_guild(self, guild_id):
        await self.http.delete("/guilds/{}".format(guild_id))

    async def get_guild_channels(self, guild_id):
        resp = await self.http.get("/guilds/{}/channels".format(guild_id))
        chans = []
        for channel in resp:
            chans.append(Channel(**channel))
        return chans

    async def create_guild_channel(self, guild_id, data):
        resp = await self.http.post("/guilds/{}/channels".format(guild_id), data)
        logging.info(f"create_guild_channel : {resp}")
        return Channel(**resp)

    async def get_member(self, guild_id, member_id):
        resp = await self.http.get("/guilds/{}/members/{}".format(guild_id, member_id))
        logging.info(f"get_member : {resp}")
        return User(**resp)

    async def get_members(self, guild_id):
        resp = await self.http.get("/guilds/{}/members".format(guild_id))
        membs = []
        for m in resp:
            membs.append(GuildMember(**m))
        return membs

    async def modify_guild_member(self, guild_id, member_id, data):
        await self.http.patch("/guilds/{}/members/{}".format(guild_id, member_id), data)

    async def set_nick_self(self, guild_id, nick):
        data = {nick: nick}
        await self.http.patch("/guilds/{}/members/@me/nick".format(guild_id), data)

    async def add_role(self, guild_id, member_id, role_id):
        await self.http.put("/guilds/{}/members/{}/roles/{}".format(guild_id, member_id, role_id))

    async def remove_member_role(self, guild_id, member_id, role_id):
        await self.http.delete("/guilds/{}/members/{}/roles/{}".format(guild_id, member_id, role_id))

    async def kick_member(self, guild_id, member_id):
        await self.http.delete("/guilds/{}/members/{}".format(guild_id, member_id))

    async def get_bans(self, guild_id):
        resp = await self.http.get("/guilds/{}/bans".format(guild_id))
        bans = []
        for ban in resp:
            bans.append(Ban(**ban))
        return bans

    async def ban_user(self, guild_id, member_id, delete_message_days):
        data = {'delete-message-days': delete_message_days}
        await self.http.put("/guilds/{}/bans/{}".format(guild_id, member_id), data)

    async def unban(self, guild_id, member_id):
        await self.http.delete("/guilds/{}/bans/{}".format(guild_id, member_id))

    async def get_roles(self, guild_id):
        resp = await self.http.get("/guilds/{}/roles".format(guild_id))
        roles = []
        for role in resp:
            roles.append(Role(**role))
        return roles

    async def create_role(self, guild_id, data):
        resp = await self.http.post("/guilds/{}/roles".format(guild_id), data)
        return Role(**resp)

    async def modify_guild_roles(self, guild_id, data):
        resp = await self.http.patch("/guilds/{}/roles".format(guild_id), data)
        roles = []
        for role in resp:
            roles.append(Role(**role))
        return roles

    async def modify_guild_role(self, guild_id, role_id, data):
        resp = await self.http.patch("/guilds/{}/roles/{}".format(guild_id, role_id), data)
        return Role(**resp)

    async def remove_guild_role(self, guild_id, role_id):
        await self.http.delete("/guilds/{}/roles/{}".format(guild_id, role_id))

    async def get_prune_count(self, guild_id, days):
        resp = await self.http.get("/guilds/{}/prune?days={}".format(guild_id, days))
        return resp['pruned']

    async def begin_prune(self, guild_id, days):
        data = {days: days}
        await self.http.post("/guilds/{}/prune".format(guild_id), data)

    async def get_invites_guild(self, guild_id):
        resp = await self.http.get("/guilds/{}/invites".format(guild_id))
        invites = []
        for invite in resp:
            invites.append(Invite(**invite))
        return invites

    async def get_guild_integrations(self, guild_id):
        resp = await self.http.get("/guilds/{}/integrations".format(guild_id))
        integrations = []
        for integration in resp:
            integrations.append(Integration(**integration))
        return integrations

    async def create_guild_integration(self, guild_id, data):
        await self.http.post("/guilds/{}/integrations".format(guild_id), data)

    async def modify_guild_integration(self, guild_id, integration_id, data):
        await self.http.patch("/guilds/{}/integrations/{}".format(guild_id, integration_id), data)

    async def delete_guild_integration(self, guild_id, integration_id):
        await self.http.delete("/guilds/{}/integrations/{}".format(guild_id, integration_id))

    async def sync_guild_integration(self, guild_id, integration_id):
        await self.http.post("/guilds/{}/integrations/{}/sync".format(guild_id, integration_id))

    async def get_guild_embed(self, guild_id):
        resp = await self.http.get("/guilds/{}/embed".format(guild_id))
        return GuildEmbed(**resp)

    async def modify_guild_embed(self, guild_id, data):
        resp = await self.http.patch("/guilds/{}/embed".format(guild_id), data)
        return GuildEmbed(**resp)
