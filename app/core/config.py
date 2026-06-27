from logging import getLogger
from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = getLogger(__name__)

# Корень проекта: app/core/config.py -> app/core -> app -> <root>
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class ConfigBase(BaseSettings):
    """Общая база: откуда читать переменные и как себя вести."""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )


class BotSettings(ConfigBase):
    """Настройки самого бота. Переменные с префиксом BOT_ (например BOT_TOKEN)."""

    TOKEN: SecretStr

    model_config = SettingsConfigDict(env_prefix="BOT_", extra="ignore")


class Settings(BaseSettings):
    """Единая точка доступа ко всем настройкам приложения.

    Группы добавляются по мере роста (db, redis, ...) той же схемой.

    :example:
        >>> from app.core.config import settings
        >>> settings.bot.TOKEN.get_secret_value()
    """

    bot: BotSettings = Field(default_factory=BotSettings)

    @classmethod
    def load(cls) -> "Settings":
        return cls()


settings = Settings.load()
logger.debug("config loaded from %s", ENV_FILE)
