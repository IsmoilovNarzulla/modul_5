
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher,html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = (f"b yoki strong:<b>Aiogram</b>\n"                           # yozuvni qalin qilish
    f"i yoki em:<i>Aiogram</i>\n"                                       # yozuvni yonboshlatish
    f"u yoki ins:<u>Aiogram</u>\n"                                      # yozuvni tagiga chizish
    f"s,strike yoki del:<s>Aiogram</s>\n"                               # yozuvni ustidan chizish
    f"span yoki tg_spoiler:<span class='tg-spoiler'>Aiogram</span>\n"          # yozuvni bijir_bijir qilish
    # f"Link:<a href=>\"https://t.me/loyiha1_bot\" tg api html format</a>\n"   # link
    f"CR7 rasm:<a href=\"https://t.me/Rasmlar_glavnigae/177870\">CR7</a>\n"    # rasm
    f"Python code:<code>inline fixed-widh code</code>\n"                       # copy kurinish
    f"<pre><code class=\"language-python\">Hello world</code></pre>\n"         # copy kurinish actual
    f"")
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\n\n"+ text)


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())