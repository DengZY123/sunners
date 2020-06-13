from flask import Blueprint
from web.controllers.api import *
from flask import request,jsonify,current_app
from application import app,db
import requests,json
from common.models.Member import Member
from common.models.OauthMember import OauthMemberBind
from common.lib.Helper import getCurrentDate
from common.lib.member.MemberService import MemberService


from web.controllers.api.User import *

@route_api.route("/test/testa",methods = ["GET","POST"])
def testaa():
    return "this is Test.py"