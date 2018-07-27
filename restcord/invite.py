from .models.invite import Invite


class InviteCord:

    def __init__(self, restcord):
        self.http = restcord.http

    async def get_invite(self, code):
        resp = await self.http.get("/invites/{}".format(code))
        return Invite(**resp)

    async def delete_invite(self, code):
        resp = await self.http.delete("/invites/{}".format(code))
        return Invite(**resp)
