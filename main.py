import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Не задан BOT_TOKEN в переменных окружения")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Ссылки — поменяй на свои
DISCORD_LINK = "https://discord.gg/твоя-ссылка"
GOV_LINK = "https://gov.ru"
FSB_LINK = "https://fsb.ru"
MVD_LINK = "https://мвд.рф"
GIBDD_LINK = "https://гибдд.рф"
VCH_LINK = "https://пример-вч.рф"
BA_LINK = "https://пример-ба.рф"
BY_LINK = "https://пример-бю.рф"
MEDIA_LINK = "https://пример-сми.рф"

def kb_start():
    kb = [
        [InlineKeyboardButton(text="🎮 Discord сервер", url=DISCORD_LINK)],
        [InlineKeyboardButton(text="📍 Москва", callback_data="city_moscow")],
        [InlineKeyboardButton(text="📍 Томск", callback_data="city_tomsk")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

def kb_city():
    kb = [
        [InlineKeyboardButton(text="🏛 Правительство", url=GOV_LINK)],
        [InlineKeyboardButton(text="🕵️ УФСБ", url=FSB_LINK)],
        [InlineKeyboardButton(text="👮 МВД", url=MVD_LINK)],
        [InlineKeyboardButton(text="🚗 ГИБДД", url=GIBDD_LINK)],
        [InlineKeyboardButton(text="🪖 ВЧ", url=VCH_LINK)],
        [InlineKeyboardButton(text="🛡 БА", url=BA_LINK)],
        [InlineKeyboardButton(text="📜 БЮ", url=BY_LINK)],
        [InlineKeyboardButton(text="📺 СМИ", url=MEDIA_LINK)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Выбери действие:",
        reply_markup=kb_start()
    )

@dp.callback_query(lambda c: c.data in ["city_moscow", "city_tomsk"])
async def city_selected(callback: types.CallbackQuery):
    city_name = "Москва" if callback.data == "city_moscow" else "Томск"
    await callback.message.edit_text(
        f"Вы выбрали: {city_name}. Выберите ведомство:",
        reply_markup=kb_city()
    )
    await callback.answer()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
