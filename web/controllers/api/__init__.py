from flask import Blueprint

route_api = Blueprint("api_page",__name__)

from web.controllers.api.User import *
from web.controllers.api.Test import *
from web.controllers.api.user.User import *

@route_api.route("/")
def index():
    return "Mina api v1.0"