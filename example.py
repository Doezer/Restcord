import json
import sys
from base64 import b64encode

import asyncio
import logging

import aiohttp

import restcord

logger = logging.getLogger(__name__)

__appname__ = 'EmojiPutter'
__version__ = "1.0"
__author__ = "Doezer"
__description__ = "Simple app to use the Restcord API wrapper. Adds an emote to a guild."


class EmojiPutter(object):

    def __init__(self, proxy_url=None, proxy_auth=None):
        """

        :param str proxy_url: (optional) URL of the HTTP proxy to use
        :param aiohttp.BasicAuth proxy_auth: (optional) for authentication with the Proxy
        """
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.loop = asyncio.get_event_loop()
        self.client = restcord.Restcord(token='NDU5NzIxOTcwMjM4NDg4NTc4.Dg6WwA.7ZAM1P3D9e966PKAKQljeUsvVQc',
                                        proxy_url=proxy_url,
                                        proxy_auth=proxy_auth)

        self.token = None
        self.emote_name = None
        self.image_path = None

    async def add_emote(self):
        """ Add an emote recursively to the guilds the account has access to.

        Checks if the emote is already present in the account's emotes using self.emote_name.
        If not, loads self.image_path as base64 URI.
        Then, browser throuh guilds to check either if the account has permission and the guild has room for emotes.
        Finally, uploads the emote if those conditions are OK, and exits the function.
        """
        name = self.emote_name
        image_path = self.image_path

        emoji_uploaded = False
        error = False
        emojis = []

        guilds = await self.client.get_guilds_me()  # Get list of guilds
        for guild in guilds:  # Adding account Emojis to a list
            emojis += await self.client.get_guild_emojis(guild.id)

        if name in [emoji.name for emoji in emojis]:  # Check presence of emoji in list
            logger.info(f'The bot already has this emote in its list. Terminating.')
            return
        try:
            with open(image_path, 'rb') as imgf:  # Open the image as decoded base64 string
                encoded = b64encode(imgf.read()).decode('utf-8')
        except:
            logger.exception('Issue while trying to read the given image.')
            return

        try:
            img_ext = image_path.split('/')[-1]  # Remove slashes from the path
        except:
            img_ext = image_path.split('\\')[-1]  # If on Windows, remove antislashes

        img_ext = img_ext.split('.')[-1]  # Retrieve the file extension (only PNG/JPG authorized)

        if img_ext.upper() not in ['PNG', 'JPG', 'JPEG']:
            raise Exception('Image needs to be JPG or PNG.')

        img_uri = 'data:image/{};base64,{}'.format(img_ext, encoded)  # Create the URI string

        for guild in guilds:
            data = json.dumps({"name": name, "image": img_uri})  # Create the JSON data
            try:
                await self.client.create_guild_emoji(guild_id=guild.id, data=data)
            except restcord.exceptions.GuildPermissionsError:
                logger.error(f'I do not have permission to upload emotes on {guild.name}. Trying next...')
                error = True
                continue
            except restcord.exceptions.GuildEmojisFull:
                logger.error(f'Too much emojis on {guild.name}. Trying next...')
                error = True
                continue
            except:
                logger.exception(f'Unknown exception during the creation of emoji.')
                return
            emoji_uploaded = True
            break

        if emoji_uploaded:
            logger.info(f'{image_path} has been created as emoji {name} on {guild.name}.')
            return
        elif error:
            logger.warning(
                f'Could not upload {image_path} as emoji {name} to any server. Check that servers are not full.')

    def run(self, token, name, image_path):
        self.token = token
        self.emote_name = name
        self.image_path = image_path
        try:
            self.loop.run_until_complete(self.add_emote())
            self.client.close()
        except RuntimeError:
            logger.exception('An error occured during runtime:')
            pass


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        stream=sys.stdout,
        format="%(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s] %(message)s <%(lineno)d>",
    )

    proxyurl = 'http://localhost:8000'
    proxy_login = 'login'
    proxy_password = 'password'
    proxyauth = aiohttp.BasicAuth(proxy_login, proxy_password)
    bot = EmojiPutter(proxyurl, proxyauth)
    bot_token = 'your_token_here'
    emote_name = 'emote_name_here'
    emote_local_path = 'local_path_to_image_here'
    bot.run('koh_lantaa', './res/koh_lanta.jpeg')
