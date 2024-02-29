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
    if not await validate_data(message.text):
        await message.answer(
            'Невалидный запос. Пример запроса: {"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
        )
        return
    request = json.loads(message.text)
    start_dt, end_dt, step_type = await prepare_conditions(request['dt_from'], request['dt_upto'],
                                                           request['group_type'])
    result = await prepare_data(start_dt, end_dt, step_type)
    await message.answer(json.dumps(result))
