import asyncio
import json
import logging
import sys
from base64 import b64encode

from .restcord import exceptions
from .restcord.core import Restcord

logger = logging.getLogger(__name__)

__appname__ = 'EmojiPutter'
__version__ = "1.0"
__author__ = "Doezer"
__description__ = "Simple app to use the Restcord API wrapper. Adds an emote to a guild."


class EmojiPutter(object):

    def __init__(self, bot_token):
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.loop = asyncio.get_event_loop()
        self.token = bot_token
        self.emote_name = None
        self.image_path = None
        self.client = Restcord(token=self.token, loop=self.loop)

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

        guilds = await self.client.UserCord.get_guilds_me()  # Get list of guilds
        for guild in guilds:  # Adding account Emojis to a list
            emojis += await self.client.EmojiCord.get_guild_emojis(guild.id)

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
                await self.client.EmojiCord.create_guild_emoji(guild_id=guild.id, data=data)
            except exceptions.GuildPermissionsError:
                logger.error(f'I do not have permission to upload emotes on {guild.name}. Trying next...')
                error = True
                continue
            except exceptions.GuildEmojisFull:
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

    def run(self, name, image_path):
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

    bot_token = 'your_token_here'
    bot = EmojiPutter(bot_token)

    emote_name = 'emote_name_here'
    emote_local_path = 'local_path_to_image_here'
    bot.run(emote_name, emote_local_path)
