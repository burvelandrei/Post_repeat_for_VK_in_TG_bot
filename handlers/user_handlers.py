from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

rt = Router()

@rt.message(CommandStart())
async def start_process(message: Message):
    await message.answer(text=LEXICON_RU["/start"])