from flask import Flask

from internal.api.routers.user_group import blueprint as blueprint_user
from internal.api.routers.schedule import blueprint as blueprint_schedule


app = Flask(__name__)

app.register_blueprint(blueprint_user)
app.register_blueprint(blueprint_schedule)

if __name__ == '__main__':
    app.run()
