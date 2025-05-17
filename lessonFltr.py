
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher,html,F
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
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message(F.photo)
async def photo_handler(msg: Message) -> None:
    await msg.answer("Siz photo yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)


@dp.message(F.document)
async def document_handler(msg: Message) -> None:
    await msg.answer("Siz document yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.video)
async def video_handler(msg: Message) -> None:
    await msg.answer("Siz video yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.voice)
async def voice_handler(msg: Message) -> None:
    await msg.answer("Siz voice yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.audio)
async def audio_handler(msg: Message) -> None:
    await msg.answer("Siz audio yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.sticker)
async def sticker_handler(msg: Message) -> None:
    await msg.answer("Siz sticker yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.location)
async def location_handler(msg: Message) -> None:
    await msg.send_copy(chat_id=msg.chat.id)
    lat = msg.location.latitude
    lon = msg.location.longitude
    await msg.answer(f"Siz location yubordingiz\n"
                     f"Latitude: {lat}\n"
                     f"Longitude: {lon}")


@dp.message(F.contact)
async def contact_handler(msg: Message) -> None:
    await msg.answer("Siz contact yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.via_bot)
async def via_bot_handler(msg: Message) -> None:
    await msg.answer("Siz via bot yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.game)
async def game_handler(msg: Message) -> None:
    await msg.answer("Siz game yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.invoice)
async def invoice_handler(msg: Message) -> None:
    await msg.answer("Siz invoice yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.poll)
async def poll_handler(msg: Message) -> None:
    await msg.answer("Siz surovnoma yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.dice)
async def dice_handler(msg: Message) -> None:
    await msg.answer("Siz dice yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.video_note)
async def video_note_handler(msg: Message) -> None:
    await msg.answer("Siz video note yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.voice_note)
async def voice_note_handler(msg: Message) -> None:
    await msg.answer("Siz voice note yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.url)
async def url_handler(msg: Message) -> None:
    await msg.answer("Siz url yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.forward)
async def forward_handler(msg: Message) -> None:
    await msg.answer("Siz forward yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.callback_query)
async def callback_query_handler(msg: Message) -> None:
    await msg.answer("Siz callback query yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.channel_post)
async def channel_post_handler(msg: Message) -> None:
    await msg.answer("Siz channel post yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.chat_photo)
async def chat_photo_handler(msg: Message) -> None:
    await msg.answer("Siz chat photo yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.pinned_message)
async def pinned_message_handler(msg: Message) -> None:
    await msg.answer("Siz pinned message yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.media_group_id)
async def media_group_id_handler(msg: Message) -> None:
    await msg.answer("Siz media group id yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.left_chat_member)
async def left_chat_member_handler(msg: Message) -> None:
    await msg.answer("Siz left chat member yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.new_chat_members)
async def new_chat_members_handler(msg: Message) -> None:
    await msg.answer("Siz new chat members yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.new_chat_title)
async def new_chat_title_handler(msg: Message) -> None:
    await msg.answer("Siz new chat title yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.new_chat_photo)
async def new_chat_photo_handler(msg: Message) -> None:
    await msg.answer("Siz new chat photo yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.delete_chat_photo)
async def delete_chat_photo_handler(msg: Message) -> None:
    await msg.answer("Siz delete chat photo yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.group_chat_created)
async def group_chat_created_handler(msg: Message) -> None:
    await msg.answer("Siz group chat created yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.supergroup_chat_created)
async def supergroup_chat_created_handler(msg: Message) -> None:
    await msg.answer("Siz supergroup chat created yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.channel_chat_created)
async def channel_chat_created_handler(msg: Message) -> None:
    await msg.answer("Siz channel chat created yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.migrate_to_chat_id)
async def migrate_to_chat_id_handler(msg: Message) -> None:
    await msg.answer("Siz migrate to chat id yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.migrate_from_chat_id)
async def migrate_from_chat_id_handler(msg: Message) -> None:
    await msg.answer("Siz migrate from chat id yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.pinned_message)
async def pinned_message_handler(msg: Message) -> None:
    await msg.answer("Siz pinned message yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.invoice)
async def invoice_handler(msg: Message) -> None:
    await msg.answer("Siz invoice yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.successful_payment)
async def successful_payment_handler(msg: Message) -> None:
    await msg.answer("Siz successful payment yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.connected_website)
async def connected_website_handler(msg: Message) -> None:
    await msg.answer("Siz connected website yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.passport_data)
async def passport_data_handler(msg: Message) -> None:
    await msg.answer("Siz passport data yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.poll_answer)
async def poll_answer_handler(msg: Message) -> None:
    await msg.answer("Siz poll answer yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.proximity_alert_triggered)
async def proximity_alert_triggered_handler(msg: Message) -> None:
    await msg.answer("Siz proximity alert triggered yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.video_chat_scheduled)
async def video_chat_scheduled_handler(msg: Message) -> None:
    await msg.answer("Siz video chat scheduled yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.gift)
async def gift_handler(msg: Message) -> None:
    await msg.answer("Siz gift yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.video_chat_started)
async def video_chat_started_handler(msg: Message) -> None:
    await msg.answer("Siz video chat started yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)

@dp.message(F.gift_card)
async def gift_card_handler(msg: Message) -> None:
    await msg.answer("Siz gift card yubordingiz")
    await msg.send_copy(chat_id=msg.chat.id)


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