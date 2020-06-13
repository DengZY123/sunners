from web.controllers.api import *
from application import app,db
from common.models.User import User


@route_api.route("/user_login",methods = ["GET","POST"])
def user_login():
    resp = {'code':200,'msg':"操作成功","data":{}}
    user_info = User.query.first()
    resp['nick_name'] = user_info.nickname
    return jsonify(resp)

