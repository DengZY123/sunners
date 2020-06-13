from web.controllers.api import *
from flask import request,jsonify,current_app
from web.application import app,db
import requests,json
from common.models.Member import Member
from common.models.OauthMember import OauthMemberBind
from common.lib.Helper import getCurrentDate
from common.lib.member.MemberService import MemberService

@route_api.route("/member/apptest",methods = ["GET","POST"])
def test():
    resp = {'code':200,'msg':"操作成功","data":{}}
    return jsonify( resp )

