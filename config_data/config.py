from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    # admin_ids: list[int]|None


@dataclass
class VkPars:
    token: str
    privat_key: str
    service_key: str


@dataclass
class Config:
    tg_bot: TgBot
    vk_pars: VkPars


def load_config(path: str|None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(token=env("BOT_TOKEN")),
        vk_pars=VkPars(token=env("VK_TOKEN"),
        privat_key=env("PRIVATE_KEY"),
        service_key=env("SERVICE_KEY")
        ))