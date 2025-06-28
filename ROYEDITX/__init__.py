import asyncio
from ROYEDITX import LOGGER, LOCOPILOT

bot = LOCOPILOT()

async def main():
    await bot.start()
    LOGGER.info("❖ ᴛʜᴇ sᴀᴛᴀɴ ᴄʜᴀᴛ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ.")
    await asyncio.Event().wait()

if name == "main":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        LOGGER.info("Bot stopped by user.")
