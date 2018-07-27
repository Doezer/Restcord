from .models.channel import Channel
from .models.invite import Invite
from .models.message import Message
from .models.user import User


class ChannelCord:

    def __init__(self, restcord):
        self.http = restcord.http

    async def create_dm(self, recipient_id):
        data = {recipient_id: recipient_id}
        resp = await self.http.post("/users/@me/channels", data)
        return Channel(**resp)

    async def get_channel(self, channel_id):
        resp = await self.http.get("/channels/{}".format(channel_id))
        return Channel(**resp)

    async def modify_channel(self, channel_id, data):
        resp = await self.http.put("/channels/{}".format(channel_id), data)
        return Channel(**resp)

    async def delete_channel(self, channel_id):
        resp = await self.http.delete("/channels/{}".format(channel_id))
        return Channel(**resp)

    async def get_messages(self, channel_id):
        resp = await self.http.get("/channels/{}/messages".format(channel_id))
        messages = []
        for msg in resp:
            messages.append(Message(**msg))
        return messages

    async def get_message(self, channel_id, message_id):
        resp = await self.http.get("/channels/{}/messages/{}".format(channel_id, message_id))
        return Message(**resp)

    async def send_message(self, channel_id, data):
        resp = await self.http.post("/channels/{}/messages".format(channel_id), data)
        return Message(**resp)

    async def add_reaction(self, channel_id, message_id, emoji):
        await self.http.put("/channels/{}/messages/{}/reactions/{}/@me".format(channel_id, message_id, emoji))

    async def remove_reaction(self, channel_id, message_id, emoji):
        await self.http.delete("/channels/{}/messages/{}/reactions/{}/@me".format(channel_id, message_id, emoji))

    async def remove_user_reaction(self, channel_id, message_id, emoji, user_id):
        await self.http.delete(
            "/channels/{}/messages/{}/reactions/{}/{}".format(channel_id, message_id, emoji, user_id))

    async def get_reactions(self, channel_id, message_id, emoji):
        resp = await self.http.get("/channels/{}/messages/{}/reactions/{}".format(channel_id, message_id, emoji))
        users = []
        for user in resp:
            users.append(User(**user))
        return users

    async def delete_all_reactions(self, channel_id, message_id):
        await self.http.delete("/channels/{}/messages/{}/reactions".format(channel_id, message_id))

    async def edit_message(self, channel_id, message_id, data):
        resp = await self.http.patch("/channels/{}/messages/{}".format(channel_id, message_id), data)
        return Message(**resp)

    async def delete_message(self, channel_id, message_id):
        await self.http.delete("/channels/{}/messages/{}".format(channel_id, message_id))

    async def get_invites_channel(self, channel_id):
        resp = await self.http.get("/channels/{}/invites".format(channel_id))
        invites = []
        for invite in resp:
            invites.append(Invite(**invite))
        return invites

    async def create_invite(self, channel_id, data):
        resp = await self.http.post("/channels/{}/invites".format(channel_id), data)
        return Invite(**resp)

    async def send_typing(self, channel_id):
        await self.http.post("/channels/{}/typing".format(channel_id))

    async def get_pinned_messages(self, channel_id):
        resp = await self.http.get("/channels/{}/pins".format(channel_id))
        messages = []
        for msg in resp:
            messages.append(Message(**msg))
        return messages

    async def pin_message(self, channel_id, message_id):
        await self.http.put("/channels/{}/pins/{}".format(channel_id, message_id))

    async def unpin_message(self, channel_id, message_id):
        await self.http.delete("/channels/{}/pins/{}".format(channel_id, message_id))
