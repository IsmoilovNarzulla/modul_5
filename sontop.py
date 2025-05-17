import asyncio
import logging
import random
import sys
from os import getenv
import psycopg2



from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher(storage=MemoryStorage())


class Regester(StatesGroup):
    firstname = State()
    lastname = State()
    phone = State()
    address = State()
    confirm = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    await message.answer("Ismingizni kriting: ")
    await state.set_state(Regester.firstname)

@dp.message(Regester.firstname)
async def firstname_handler(message: Message, state: FSMContext):
    await state.update_data(firstame=message.text)
    await message.answer("Familiyangizni kiriting:")
    await state.set_state(Regester.lastname)

@dp.message(Regester.lastname)
async def lastname_handler(message: Message, state: FSMContext):
    await state.update_data(lastname=message.text)
    await message.answer("Tel raqamingizni kriting  kriting: ")
    await state.set_state(Regester.phone)

@dp.message(Regester.phone)
async def phone_phone_handler(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Manzilingizni kriting: ")
    await state.set_state(Regester.address)

@dp.message(Regester.address)
async def address_handler(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    state_data = await state.get_data()
    chat_id = message.chat.id
    datas = {
            "chat_id":chat_id,
            "firstame":state_data.get('firstame'),
            "lastname":state_data.get('lastname'),
            "phone":state_data.get('phone'),
            "address":state_data.get('address')
    }
    await state.update_data(datas=datas)

    msg = (
        f"Ism: {state_data.get('firstame')}\n"
        f"Familiya: {state_data.get('lastname')}\n"
        f"Telefon: {state_data.get('phone')}\n"
        f"Manzil: {state_data.get('address')}\n"
    )
    await message.answer(msg)
    await message.answer("Ma'lumotlar to‘g‘rimi? (ha/yo'q)")
    await state.set_state(Regester.confirm)
    return datas

@dp.message(Regester.confirm)
async def confirm_handler(message: Message, state: FSMContext):
    text = message.text
    state_data = await state.get_data()
    datas = state_data.get('datas')
    if text.lower() == "ha":
        await state.update_data(confirmed=True)
        await message.answer("Malumot saqlandi.\n\n"
                             "o'yin o'ynash uchun /play ni bosing")

        Database().insert_user(datas)



    elif text == "/play":
        user_data = await state.get_data()
        if user_data.get("confirmed"):
            await state.set_state(GameState.guess_number)
            await message.answer("O'yin boshlandi!")
            geus_number = random.randint(1, 10)
            await state.update_data(geus_number=geus_number, attemp=0)
            await message.answer('Men 1 dan 10 gacha bo\'lgan bir son o\'yladim topaolasizmi')
            return
        else:
            await message.answer("Avval ro'yxatdan o'ting. /start buyrug'ini bosing.")
            await state.clear()

    else:
        await state.update_data(confirmed=False)
        await message.answer("Ro'yxatdan o'tish uchun /start ni bos")
        await state.clear()



class GameState(StatesGroup):
    guess_number = State()

@dp.message(GameState.guess_number)
async def command_start_lop(message: Message, state: FSMContext) -> None:
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
        attemp = state_data.get("attemp", 0 ) + 1
        await state.update_data(attemp=attemp)
        await message.answer(f"Men o'ylagan son {text} dan kichik")
        return

    elif int(text) < gues_number:
        attemp = state_data.get("attemp", 0) + 1
        await state.update_data(attemp=attemp)
        await message.answer(f"Men o'ylagan son {text} dan kotta")
        return

    attemp = state_data.get("attemp", 0) + 1
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



class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='sontop',
            user='postgres',
            password='NARZULLA',
            host='localhost',
            port='5432'
        )
        self.curr = self.conn.cursor()

    def execute(self, query):
        with self.conn:
            self.curr.execute(query)
        return self.curr

    def users(self):
        sql_query = """
        CREATE TABLE IF NOT EXISTS users(
        chat_id INTEGER NOT NULL UNIQUE,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50)UNIQUE NOT NULL,
        phone VARCHAR(13) NOT NULL,
        address VARCHAR(50) NOT NULL
        );"""
        try:
            with self.conn:
                self.curr.execute(sql_query)
        except Exception as e:
            print(f"Error {e}")

    def insert_user(self,datas):
        try:
            chat_id = datas.get("chat_id")
            firstname = datas.get("firstname")
            lastname = datas.get("lastname")
            phone = datas.get("phone")
            address = datas.get("address")
            self.curr.execute("""
            INSERT INTO users (chat_id, firstname, lastname, phone, address) 
            VALUES (%s, %s, %s,%s,%s) ON CONFLICT (chat_id) DO NOTHING;
            """, (chat_id, firstname, lastname, phone, address))
            self.conn.commit()
        except Exception as e:
            print(f" Foydalanuvchini qo‘shishda xatolik: {e}")

    def close(self):
        self.curr.close()
        self.conn.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())




