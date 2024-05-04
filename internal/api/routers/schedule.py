import datetime
import json
from dataclasses import asdict

from flask import Blueprint, request, abort
from internal.schedule.schedule import Schedule

blueprint = Blueprint("schedule_router", __name__)

with open('internal/schedule/schedule.json', "r", encoding='utf-8') as file:
    configuration = json.load(file)
schedule = Schedule(configuration)


@blueprint.route("/schedule", methods=['GET'])
def handle_schedule():
    args = request.args

    group = args.get("group", type=str, default=None)
    date = args.get("date", type=str, default=None)

    if not date:
        date = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
    if not group:
        abort(404)

    sc = schedule.get_schedule(group, date)
    if not sc:
        abort(404)

    return asdict(sc)
