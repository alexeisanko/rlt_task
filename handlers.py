import json

from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from utils import prepare_conditions, prepare_data, validate_data

router = Router()


@router.message(Command('start'))
async def _start(message: Message):
    await message.answer('Привет, жду вашего запроса')


@router.message()
async def get_data(message: Message):

    request = json.loads(message.text)
    start_dt, end_dt, step_type = await prepare_conditions(request['dt_from'], request['dt_upto'],
                                                           request['group_type'])
    result = await prepare_data(start_dt, end_dt, step_type)
    await message.answer(json.dumps(result))
