import datetime
import json

from flask import Blueprint, abort, request, redirect, url_for

from internal.db.db import get_group
from internal.schedule.schedule import Schedule

blueprint = Blueprint("redirect_router", __name__)

with open('internal/schedule/schedule.json', "r", encoding='utf-8') as file:
    configuration = json.load(file)
schedule = Schedule(configuration)


@blueprint.route("/user", methods=['GET'])
def handle_user():
    args = request.args
    user_id = args.get("user_id", type=int, default=0)

    if not user_id:
        abort(404)

    try:
        group_user = get_group(user_id)
    except:
        abort(500)

    if not group_user:
        abort(404)

    return redirect(
        url_for(
            "schedule_router.handle_schedule",
            group=group_user,
            date=datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")
        ),
    )