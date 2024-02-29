from typing import Dict, Tuple, List
from datetime import datetime

from dateutil.relativedelta import relativedelta
import bson

from db import MongoDB


async def prepare_conditions(start: str, end: str, group_type: str) -> Tuple[datetime, datetime, dict]:
    start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
    end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
    step_type = {'month': 0, 'day': 0, 'hour': 0}
    step_type[group_type] += 1
    return start_dt, end_dt, step_type


async def prepare_data(start_dt: datetime, end_dt: datetime, step_type: dict) -> Dict[str, List[str]]:
    result = {"dataset": [], "labels": []}

    if step_type['hour']:
        aggregate_dt = datetime(start_dt.year, start_dt.month, start_dt.day, start_dt.hour)
    else:
        aggregate_dt = datetime(start_dt.year, start_dt.month, start_dt.day)

    inc_dt = relativedelta(months=step_type['month'], days=step_type['day'], hours=step_type['hour'])

    while aggregate_dt <= end_dt:
        if aggregate_dt + inc_dt > end_dt:
            aggregate = await MongoDB.get_filter_aggregate_data(aggregate_dt, end_dt)
        else:
            aggregate = await MongoDB.get_filter_aggregate_data(aggregate_dt, aggregate_dt + inc_dt)

        if not aggregate:
            result['dataset'].append(0)
        else:
            result['dataset'].append(aggregate[0]['total'])
        result['labels'].append(aggregate_dt.strftime("%Y-%m-%dT%H:%M:%S"))
        aggregate_dt += inc_dt
    return result


async def insert_sample_collection(file: str) -> None:
    data = []
    with open(file, 'rb') as f:
        data_bson = f.read()
        data = bson.decode_all(data_bson)
    await MongoDB.insert_data(data)
