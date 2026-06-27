import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("roll"))
async def command_roll(message: Message) -> None:
    """Бросает число 1-100 и отвечает в зависимости от результата."""
    user_name = message.from_user.full_name
    num = random.randint(1, 100)

    if num == 13:
        result = f"Оу {num}... Откуды ты знаешь, что у меня др в этот день!"
    elif num > 80:
        result = f"ОГО! {user_name}, тебе выпало {num}! Вселенная на твоей стороне!"
    elif num > 50:
        result = f"Неплохо, {user_name}! {num} — среднячок, как и я..?"
    elif num > 20:
        result = f"Всего {num}? Ну... бывало и лучше. Но я в тебя верю!"
    else:
        result = f"{num}... Это знак. Меня никто не любит. И тебя тоже, наверное... 😭"

    await message.answer(result)
