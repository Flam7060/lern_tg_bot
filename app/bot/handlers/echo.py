from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def echo_handler(message: Message) -> None:
    """Ловит любое необработанное сообщение и возвращает его копию."""
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
