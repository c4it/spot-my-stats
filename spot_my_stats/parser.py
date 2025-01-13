"""Parse streaming history."""

import json
import os
from datetime import datetime, date


def _decode_ts(obj):
    for k, v in obj.items():
        if k == "ts":
            obj[k] = datetime.fromisoformat(v)
    return obj

def _filter_dates(history: list[dict], start_date: date, end_date: date) -> list[dict]:
    return [h for h in history if start_date <= h["ts"].date() <= end_date]


def load(fp: str, start_date: date, end_date: date) -> list[dict]:
    history: list[dict] = []
    for f in os.listdir(fp):
        if f.endswith(".json") and "Video" not in f:
            history.extend(json.load(open(f"{fp}/{f}"), object_hook=_decode_ts))
    return sorted(_filter_dates(history, start_date, end_date), key=lambda v: v["ts"])

