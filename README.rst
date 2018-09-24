Restcord
========

Restcord is a Python wrapper for the Discord API, but without using WebSockets.
This is for people who only want to make requests to the api without having a full-fledged bot.

It was originally developed by JustMaffie, I (Doezer) modified it to make it work with last version of API.

Breaking Changes
~~~~~~~~~~~~~~~~

The Discord API is subject to breaking changes, so this wrapper is also subject to these changes.

Installing
----------

To install this library, you should either clone it or download it.
The version on PyPi is the original one, without any of the fixes here.

Please note that on Linux installing voice you must install the following packages via your
favourite package manager (e.g. ``apt``, ``yum``, etc) before running the above command:

- python<version>-dev (e.g. ``python3.5-dev`` for Python 3.5)

Quick Example
-------------

.. code:: py

    import restcord
    import asyncio

    loop = asyncio.get_event_loop() # Get current asyncio loop
    client = restcord.Restcord(token="Your token here") # Start the REST API session

    async def get_guild():
        guild = await client.GuildCord.get_guild("Some guild id of a guild that ur bot/user account is in")
        print(guild.__dict__)

    loop.run_until_complete(test())
    client.close()

Check the file example.py for an application used to upload an emote to the first guild with permissions OK & storage OK.

For user accounts:
~~~~~~~~~~~~~~~~~~

.. code:: py

    client = restcord.Restcord(token="Your token here", selfbot=True)

Requirements
------------

-  Python 3.4.2+ (There will be no effort to add support for lower
   versions)
-  ``aiohttp`` library

Usually ``pip`` will handle these for you.

Related Projects
----------------

-  `Restcord`_
-  `discord.py`_

.. _discord.py: https://github.com/rapptz/discord.py
.. _Restcord:: https://github.com/JustMaffie/Restcord