from aiogram import Router

from app.bot.handlers import echo, roll, start


def get_handlers_router() -> Router:
    """Собирает все роутеры хендлеров в один.

    Порядок важен: echo ловит любое сообщение, поэтому подключается последним.
    """
    router = Router()
    router.include_router(start.router)
    router.include_router(roll.router)
    router.include_router(echo.router)
    return router
