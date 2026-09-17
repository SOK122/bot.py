import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


BOT_TOKEN = "8994756863:AAHlefccgJ14BtNHBJioatd23Yyf1Z8s6Fw"
TELEGRAM_CONTACT = "bizneseuropa1"


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="📄 Фактуры (до 100 000 €)", callback_data="factures")
    kb.button(text="💬 Контакт", url=f"https://t.me/{TELEGRAM_CONTACT}")
    kb.button(text="👷 Оформление работников", callback_data="workers")
    kb.button(text="🎁 Пригласи друга", callback_data="invite")
    kb.adjust(1)
    return kb.as_markup()


def back_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="💬 Контакт", url=f"https://t.me/{TELEGRAM_CONTACT}")
    kb.button(text="⬅️ В главное меню", callback_data="back")
    kb.adjust(1)
    return kb.as_markup()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    text = (
        "👋 <b>Добро пожаловать в M&R Company!</b>\n\n"
        "Выберите интересующий вас раздел ниже 👇"
    )
    await message.answer(text, reply_markup=main_menu(), parse_mode="HTML")


@dp.callback_query(F.data == "factures")
async def cb_factures(call: CallbackQuery):
    text = (
        "📄 <b>Фактуры</b>\n\n"
        "Мы можем обработать фактуры <b>до 100 000 €</b>.\n\n"
        "<b>Наша комиссия — 10%.</b>\n\n"
        "<u>Работаем строго в рамках закона.</u>\n\n"
        "✅ Полное сопровождение документов\n"
        "✅ Прозрачные условия\n"
        "✅ Быстрая обработка\n\n"
        "Для консультации — нажмите <b>Контакт</b> 👇"
    )
    await call.message.edit_text(
        text, reply_markup=back_menu(), parse_mode="HTML"
    )
    await call.answer()


@dp.callback_query(F.data == "workers")
async def cb_workers(call: CallbackQuery):
    text = (
        "👷 <b>Оформление работников</b>\n\n"
        "<b>Зарплата работника за 1 месяц:</b>\n\n"
        "▪️ 1000 – 1199 €  →  <b>380 €</b> – налоги\n"
        "▪️ 1200 – 1399 €  →  <b>455 €</b> – налоги\n"
        "▪️ 1400 – 1599 €  →  <b>500 €</b> – налоги\n"
        "▪️ 1600 – 1799 €  →  <b>580 €</b> – налоги\n"
        "▪️ 1800 – 1999 €  →  <b>650 €</b> – налоги\n"
        "▪️ 2000 – 2199 €  →  <b>700 €</b> – налоги\n"
        "▪️ 2200 – 2299 €  →  <b>770 €</b> – налоги\n"
        "▪️ 2300 – 2399 €  →  <b>805 €</b> – налоги\n"
        "▪️ 2400 – 3000 €  →  <b>900 €</b> – налоги\n"
        "▪️ 3050 – 4000 €  →  <b>950 €</b> – налоги\n"
        "▪️ 4050 – 5000 €  →  <b>1000 €</b> – налоги\n\n"
        "▪️ Ниже 1000 €  →  <b>+35%</b> (налоги + комиссия M&R)\n\n"
        "ℹ️ К каждой сумме добавляется <b>комиссия M&R</b>.\n\n"
        "Для оформления — нажмите <b>Контакт</b> 👇"
    )
    await call.message.edit_text(
        text, reply_markup=back_menu(), parse_mode="HTML"
    )
    await call.answer()


@dp.callback_query(F.data == "invite")
async def cb_invite(call: CallbackQuery):
    text = (
        "🎁 <b>Пригласи друга</b>\n\n"
        "Хочешь заработать?\n\n"
        "Нажми на кнопку <b>Контакт</b> и выйди с нами на связь — "
        "мы расскажем все условия 👇"
    )
    await call.message.edit_text(
        text, reply_markup=back_menu(), parse_mode="HTML"
    )
    await call.answer()


@dp.callback_query(F.data == "back")
async def cb_back(call: CallbackQuery):
    text = (
        "👋 <b>Главное меню</b>\n\n"
        "Выберите раздел ниже 👇"
    )
    await call.message.edit_text(
        text, reply_markup=main_menu(), parse_mode="HTML"
    )
    await call.answer()


async def main():
    logging.info("Бот запущен ✅")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")
