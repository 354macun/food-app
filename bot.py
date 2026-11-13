"""Мини-бот: по /start показывает кнопку, а кнопка «Меню» открывает мини-приложение."""
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, MenuButtonWebApp,
                           Message, WebAppInfo)

TOKEN = os.getenv("BOT_TOKEN", "")
URL = os.getenv("WEBAPP_URL", "")  # https-адрес, где лежит index.html

dp = Dispatcher()


@dp.message(CommandStart())
async def start(m: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🍳 Открыть «Что приготовить»", web_app=WebAppInfo(url=URL))]])
    await m.answer("Привет! Нажмите кнопку, чтобы открыть приложение.", reply_markup=kb)


async def main():
    if not TOKEN or not URL.startswith("https://"):
        raise SystemExit("Задайте BOT_TOKEN и WEBAPP_URL (адрес должен начинаться с https://)")
    bot = Bot(TOKEN)
    await bot.set_chat_menu_button(menu_button=MenuButtonWebApp(text="Что приготовить", web_app=WebAppInfo(url=URL)))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
