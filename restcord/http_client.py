import asyncio
import logging

import aiohttp
from .vars import __version__ as version
from .vars import __github__ as github

BASE_URL = "https://discordapp.com/api/v7"
logger = logging.getLogger()


class HTTPClient:
    def __init__(self, restcord, loop=None):
        if loop:
            self.loop = loop
        else:
            self.loop = asyncio.get_event_loop()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.client = restcord

    def get_headers(self, post=False):
        headers = {}
        token = self.client.token
        if not self.client.selfbot:
            token = "Bot {}".format(token)
        headers['Authorization'] = token
        headers['User-Agent'] = "RestCord Python ({}, v{})".format(github, version)
        if post:
            headers['Content-Type'] = "application/json"
        return headers

    async def close(self):
        await self.session.close()

    async def get(self, endpoint):
        resp = await self.session.get(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def post(self, endpoint, data=None):
        resp = await self.session.post(BASE_URL + endpoint, headers=self.get_headers(True), data=data)
        return await resp.json()

    async def put(self, endpoint, data=None):
        resp = await self.session.put(BASE_URL + endpoint, headers=self.get_headers(), data=data)
        return await resp.json()

    async def delete(self, endpoint):
        resp = await self.session.delete(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def head(self, endpoint):
        resp = await self.session.head(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def options(self, endpoint):
        resp = await self.session.options(BASE_URL + endpoint, headers=self.get_headers())
        return await resp.json()

    async def patch(self, endpoint, data=None):
        resp = await self.session.patch(BASE_URL + endpoint, headers=self.get_headers(), data=data)
        return await resp.json()
