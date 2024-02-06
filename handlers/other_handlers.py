from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

rt = Router()

@rt.message()
async def other_process(message: Message):
    await message.answer(text=LEXICON_RU['no_answer'])