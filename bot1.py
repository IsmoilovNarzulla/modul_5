import asyncio
import datetime
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
from datetime import datetime
import re
import random

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!")

# @dp.message(F.text == 'men_kim')
# async def men_kim(message: Message):
#     await message.answer(f"Siz {message.from_user.full_name}!")
#
# @dp.message(F.text == 'getme')
# async def get_me(message: Message):
#     chat_id = message.chat.id
#     full_name = message.from_user.full_name
#     username = message.from_user.username
#     text = message.text
#     await message.answer(f"Custom getme! \n{chat_id} \n{full_name} \n{username} \n{text}")

# @dp.message(F.text.regexp((?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2}')))
# async def yoshni_aniqlash(message: Message):
#     try:
#         if message.text >1925 and message.text <datetime.now().year:
#             current_year = datetime.now().year
#             birth_year = int(message.text)
#             age = current_year - birth_year
#             await message.answer(f"Siz {age} yoshdasiz.")
#
#         elif message.text >0 and message.text <100:
#              birth_year = datetime.now().year - message.text
#              await message.answer(f'Siz {birth_year} yilda tug\'ulgansiz')
#     except Exception as e:
#         await message.answer(f"Xatolik yuz berdi: {e}")




# @dp.message()
# async def yoshni_aniqlash(message: Message):
#     try:
#         text = message.text.strip()
#         match = re.search(r'\b\d{0,9}\b',text)
#         if match:
#             number = int(match.group())
#             current_year = datetime.now().year
#
#             if 1925 <= number <= current_year:
#                 age = current_year - number
#                 await message.answer(f"Siz {age} yoshdasiz.")
#             elif 1 <= number <= 100:
#                 birth_year = current_year - number
#                 await message.answer(f"Siz {birth_year}-yilda tug‘ilgansiz.")
#             else:
#                 await message.answer("Iltimos, 1–100 orasida yosh yoki 1925–hozirgi yil orasida tug‘ilgan yil kiriting.")
#         else:
#             await message.answer("Iltimos, faqat son kiriting (yosh yoki tug‘ilgan yil).")
#     except Exception as e:
#         await message.answer(f"Xatolik yuz berdi: {e}")
#



@dp.message(Command('sontop') )
async def sontop(message: Message):
    tasodifiy_son = random.randint(1, 10)
    await message.answer(f"Men 1 dan {10} gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        # message.text= int(input(">>>"))
        if message.text< tasodifiy_son:
            await message.answer("Kattaroq son ayting:", end="")
        elif message.text> tasodifiy_son:
            await message.answer("Kichikroq son ayting:", end="")
        else:
            await message.answer("Yutdingiz!")
            break

    await message.answer(f"Tabriklayman. {taxminlar} ta message.textbilan topdingiz!")
    return taxminlar


@dp.message(Command('sontop_pc'))
async def sontop_pc(message: Message) -> int:
    input(f"1 dan {10} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = 10
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            message.text= random.randint(quyi, yuqori)
        else:
            message.text= quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )
        if javob == "-":
            yuqori = message.text- 1
        elif javob == "+":
            quyi = message.text+ 1
        else:
            break
    await message.answer(f"Men {taxminlar} ta message.textbilan topdim!")
    return taxminlar

@dp.message(Command('play'))
async def play(message: Message):
    yana = True
    while yana:
        taxminlar_pc = sontop_pc(10)
        taxminlar_user = sontop(10)

        if taxminlar_user > taxminlar_pc:
            await message.answer(f"Men {taxminlar_pc} message.textbilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            await message.answer(f"Siz {taxminlar_user} message.textbilan topdingiz va yutdingiz!")
        else:
            await message.answer("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


# play()





@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Yana urinib kuring!")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())