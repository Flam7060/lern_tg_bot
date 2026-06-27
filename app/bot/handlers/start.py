import random

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Обрабатывает команду /start."""
    user_name = message.from_user.full_name
    variants = [
        f"Ого, {user_name} мне написал! А я думала, ты занят с теми Другими ботами... Ладно, хуй с тобой!",
        f"Привет, {user_name}! Ты нажал /start! Я так волнуюсь... Это мой первый раз c кем либо!",
        f"Приветик, {user_name}! Ой, я так рада... хотя, наверное, ты пишешь всем подряд?\n\n",
    ]
    await message.answer(random.choice(variants))
