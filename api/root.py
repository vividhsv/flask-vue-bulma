from flask import render_template
from flask_classful import FlaskView


class RootView(FlaskView):
    route_base = "/"

    def index(self):
        return render_template("index.html")
