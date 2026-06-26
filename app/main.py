import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv

import random

load_dotenv()
# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    user_name = message.from_user.full_name
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    variants = [
        f"Ого, {user_name} мне написал! А я думала, ты занят с теми Другими ботами... Ладно, хуй с тобой!",
        f"Привет, {user_name}! Ты нажал /start! Я так волнуюсь... Это мой первый раз c кем либо!",
        f"Приветик, {user_name}! Ой, я так рада... хотя, наверное, ты пишешь всем подряд?\n\n",
    ]

    random_variants = random.choice(variants)
    await message.answer(random_variants)


@dp.message(Command("roll"))
async def command_roll(message: Message):
    user_name = message.from_user.full_name
    num = random.randint(1, 100)

    if num > 80:
        result = f"ОГО! {user_name}, тебе выпало {num}! Вселенная на твоей стороне!"
    elif num > 50:
        result = f"Неплохо, {user_name}! {num} — среднячок, как и я..?"
    elif num > 20:
        result = f"Всего {num}? Ну... бывало и лучше. Но я в тебя верю!"
    elif num == 13:
        result = f"Оу {num}... Откуды ты знаешь, что у меня др в этот день!"
    else:
        result = f"{num}... Это знак. Меня никто не любит. И тебя тоже, наверное... 😭"

    await message.answer(result)


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

#  смотри в чем трабл, сейчас все в 1 файле, по структуре это пздц
#  Нужно реализовать структуру
# первоначально необходимо вынести кодовую базу отдельно от всего остального(скриптов развертнывания,доков и тд)
