from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400 #请求参数错误
    msg = 'client is  invail'
    error_code = 1006