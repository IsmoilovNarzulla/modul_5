
import asyncio
import logging
import sys
from os import getenv
import random

from aiogram import Bot, Dispatcher, html, F, Router
from aiogram.client import bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm import storage
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher(storage=MemoryStorage())

class GameState(StatesGroup):
    fullname = State()
    lastname = State()
    phone = State()
    address = State()
    confirm = State()
    son = State()
    geussing = State()

router = Router()

@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    await message.answer("Ismingizni kriting: ")
    await state.set_state(GameState.fullname)

@dp.message(GameState.fullname)
async def fulname_handler(message: Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    await message.answer("Familiyangizni kiriting:")
    await state.set_state(GameState.lastname)


@dp.message(GameState.lastname)
async def lastname_handler(message: Message,state:FSMContext):
    await state.update_data(lastname=message.text)
    await message.answer("Tel raqamingizni kriting  kriting: ")
    await state.set_state(GameState.phone)

@dp.message(GameState.phone)
async def phone_phone_handler(message: Message,state:FSMContext) :
    await state.update_data(phone=message.text)
    await message.answer("Manzilingizni kriting: ")
    await state.set_state(GameState.confirm)

@dp.message(GameState.confirm)
async def confirm_handler(message: Message,state:FSMContext):
    await state.update_data(address=message.text)
    state_data = await state.get_data()
    await state.update_data(id=await message.send_copy(chat_id=message.chat.id),
                            fulname=state_data.get('fullname'),
                            lastname=state_data.get('lastname'),
                            phone=state_data.get('phone'),
                            address=state_data.get('address')
                            )

    msg = (
        f"Ism: {state_data.get('fullname')}\n"
        f"Familiya: {state_data.get('lastname')}\n"
        f"Telefon: {state_data.get('phone')}\n"
        f"Manzil: {state_data.get('address')}\n"
        "Ma'lumotlar to‘g‘rimi? (ha/yo'q)"
    )
    await message.answer(msg)
    text = message.msg
    if text.lower() == "ha":
        await state.set_state(GameState.son)

    else:
        await message.answer("Boshidan boshlaymiz")
        await state.clear()
        await state.set_state(GameState.fullname)


@dp.message(GameState.son)
async def command_start_son(message: Message,state:FSMContext) -> None:
    geus_number = random.randint(1,10)
    await state.set_state(GameState.geussing)
    await state.update_data(geus_number = geus_number,attemp = 0)
    await message.answer('Men 1 dan 10 gacha bo\'lgan bir son o\'yladim topaolasizmi')




@dp.message(GameState.geussing)
async def loop_state(message: Message, state:FSMContext):
    state_data = await state.get_data()
    gues_number = state_data.get("geus_number")
    text = message.text
    if text == 'help':
        await message.answer(f"Men o'ylagan son {gues_number}😄")
        await state.clear()
        return
    if not text.isdigit():
        await message.answer('Faqat son kriting')
        return
    if int(text) > gues_number:
        attemp = state_data.get("attemp", 0, ) + 1
        await state.update_data(attemp = attemp)
        await message.answer(f"Men o'ylagan son {text} dan kichik")
        return

    elif int(text) < gues_number:
        attemp = state_data.get("attemp", 0, ) + 1
        await state.update_data(attemp = attemp)
        await message.answer(f"Men o'ylagan son {text} dan kotta")
        return

    attemp = state_data.get("attemp", 0, ) + 1
    await message.answer(f"Tabriklayman siz {attemp} urinishda topdingiz! 🎉🎉🎉🎉 ")
    await state.clear()


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







# import asyncio
# import logging
# import sys
# from os import getenv
# import random
#
# from aiogram import Bot, Dispatcher, html, F, Router
# from aiogram.client import bot
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.fsm import storage
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import Message
# from dotenv import load_dotenv
#
# load_dotenv()
# TOKEN = getenv("BOT_TOKEN")
# dp = Dispatcher(storage=MemoryStorage())
#
# class GameState(StatesGroup):
#     fullname = State()
#     lastname = State()
#     phone = State()
#     address = State()
#     confirm = State()
#     son = State()
#     geussing = State()
#
# router = Router()
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message, state: FSMContext):
#     await message.answer("Ismingizni kiriting:")
#     await state.set_state(GameState.fullname)
#
# @dp.message(GameState.fullname)
# async def fullname_handler(message: Message, state: FSMContext):
#     await state.update_data(fullname=message.text)
#     await message.answer("Familiyangizni kiriting:")
#     await state.set_state(GameState.lastname)
#
# @dp.message(GameState.lastname)
# async def lastname_handler(message: Message, state: FSMContext):
#     await state.update_data(lastname=message.text)
#     await message.answer("Telefon raqamingizni kiriting:")
#     await state.set_state(GameState.phone)
#
# @dp.message(GameState.phone)
# async def phone_handler(message: Message, state: FSMContext):
#     await state.update_data(phone=message.text)
#     await message.answer("Manzilingizni kiriting:")
#     await state.set_state(GameState.address)
#
# @dp.message(GameState.address)
# async def address_handler(message: Message, state: FSMContext):
#     await state.update_data(address=message.text)
#     data = await state.get_data()
#     await message.answer(
#         f"Ism: {data['fullname']}\n"
#         f"Familiya: {data['lastname']}\n"
#         f"Telefon: {data['phone']}\n"
#         f"Manzil: {data['address']}\n"
#         "Ma'lumotlar to‘g‘rimi? (ha/yo‘q)"
#     )
#     await state.set_state(GameState.confirm)
#
# @dp.message(GameState.confirm)
# async def confirm_handler(message: Message, state: FSMContext):
#     if message.text.lower() == "ha":
#         await state.set_state(GameState.son)
#         await message.answer("1 dan 10 gacha son o‘ylayman, topishga harakat qiling!")
#     else:
#         await message.answer("Boshidan boshlaymiz:")
#         await state.clear()
#         await state.set_state(GameState.fullname)
#
# @dp.message(GameState.son)
# async def command_start_son(message: Message,state:FSMContext) -> None:
#     geus_number = random.randint(1,10)
#     await state.set_state(GameState.geussing)
#     await state.update_data(geus_number = geus_number,attemp = 0)
#     await message.answer('Men 1 dan 10 gacha bo\'lgan bir son o\'yladim topaolasizmi')
#
#
#
#
# @dp.message(GameState.geussing)
# async def loop_state(message: Message, state:FSMContext):
#     state_data = await state.get_data()
#     gues_number = state_data.get("geus_number")
#     text = message.text
#     if text == 'help':
#         await message.answer(f"Men o'ylagan son {gues_number}😄")
#         await state.clear()
#         return
#     if not text.isdigit():
#         await message.answer('Faqat son kriting')
#         return
#     if int(text) > gues_number:
#         attemp = state_data.get("attemp", 0) + 1
#         await state.update_data(attemp = attemp)
#         await message.answer(f"Men o'ylagan son {text} dan kichik")
#         return
#
#     elif int(text) < gues_number:
#         attemp = state_data.get("attemp", 0) + 1
#         await state.update_data(attemp = attemp)
#         await message.answer(f"Men o'ylagan son {text} dan kotta")
#         return
#
#     attemp = state_data.get("attemp", 0, ) + 1
#     await message.answer(f"Tabriklayman siz {attemp} urinishda topdingiz! 🎉🎉🎉🎉 ")
#     await state.clear()
#
#
# @dp.message()
# async def echo_handler(message: Message) -> None:
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")
#
#
# async def main() -> None:
#     bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())