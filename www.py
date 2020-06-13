

"""
统一拦截器
"""
from web.interceptors.AuthInterceptor import *




from application import app
from web.controllers.api import route_api
from web.controllers.index import route_index


app.register_blueprint(route_index,url_prefix="/")
app.register_blueprint(route_api,url_prefix="/api")
