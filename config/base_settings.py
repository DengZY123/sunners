SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3333/sunners"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SERVER_PORT = 8999
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SQLALCHEMY_ECHO = True
AUTH_COOKIE_NAME = "mooc_food"
IGNORE_URLS = [
    "^/user/login",
    "^/api"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static/",
    "^favicon.icow"
]
PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

MINA_APP = {
    'appid':'wx4fa7a55bf7816815',
    'appkey':'a0afc74b33923c0f7e6c380ca4720d1a'
}