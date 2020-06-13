import base64
import hashlib
import random
import string
from application import app
import requests
import json

class MemberService():

    @staticmethod
    def genePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode("utf-8")),salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def genSalt( length= 16 ):
        keylist = [random.choice(( string.ascii_letters + string.digits )) for i in range( length ) ]
        return ("".join(keylist))

    @staticmethod
    def getWeChatOpenId( code ):
        url = "https://api.weixin.qq.com/sns/j" \
              "scode2session?appid={0}&secret={1}&js_code={2}&" \
              "grant_type=authorization_code".format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'],
                                                     code)
        app.logger.info(url)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid

    @staticmethod
    def geneAuthCode(member_info):
        m = hashlib.md5()
        str = "%s-%s-%s"%(member_info.id,member_info.salt,member_info.status)
        m.update(str.encode("utf-8"))
        return m.hexdigest()