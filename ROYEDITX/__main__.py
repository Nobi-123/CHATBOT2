import logging
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client

import config
from ROYEDITX.modules import all_modules

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(name)

boot = time.time()
mongo = MongoCli(config.MONGO_URL)
db = mongo.Anonymous

OWNER = config.OWNER_ID

class LOCOPILOT(Client):
    def init(self):
        super().init(
            name="LOCOPILOT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="ROYEDITX.modules"),
        )
        self.id = None
        self.name = None
        self.username = None
        self.mention = None
        self.dc_id = None

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.id = me.id
        self.name = me.first_name + (me.last_name or "")
        self.username = me.username
        self.mention = me.mention
        self.dc_id = me.dc_id
        LOGGER.info(f"Bot started as {self.name} (@{self.username})")

    async def stop(self, *args):
        LOGGER.info("Bot is shutting down...")
        await super().stop()
