import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8349584164:AAHMS-RarqdJdntec03FzXUlW3r_J6hORZI"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Motivatsion iqtiboslar ro'yxati
quotes = [
    "“Muvaffaqiyat — bu xatolardan qo'rqmasdan, oldinga intilish.” 🚀",
    "“Bugungi qilgan harakatingiz — ertangi kelajagingiz poydevori.” 💡",
    "“Hech qachon taslim bo'lmang. Qiyinchiliklar faqat kuchliroq qiladi.” 🔥",
    "“Har kuni oz-ozdan o'rganish — katta natijalarga olib keladi.” 📚",
    "“Imkoniyatni kutmang, uni o'zingiz yarating!” ⭐"
]

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    text = (
        "Salom! Men Motivatsiya va Iqtiboslar botman ✨\n\n"
        "Sizga har safar yaxshi kayfiyat va ilhom ulashaman.\n"
        "Iqtibos olish uchun /quote buyrug'ini yuboring!"
    )
    await message.answer(text)

@dp.message(Command("quote"))
async def send_quote(message: types.Message):
    random_quote = random.choice(quotes)
    await message.answer(random_quote)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())