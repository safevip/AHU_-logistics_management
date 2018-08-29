from common.config import *

class CustomError(Exception):
    # 默认的返回码
    status_code = 400

    LEVEL_DEBUG = 0
    LEVEL_INFO = 1
    LEVEL_WARN = 2
    LEVEL_ERROR = 3

    # return_code，更细颗粒度的错误代码
    def __init__(self, message=None, return_code=None, status_code=None):
        Exception.__init__(self)
        self.message = message
        self.return_code = return_code
        if status_code is not None:
            self.status_code = status_code
        self.level = CustomError.LEVEL_DEBUG

    def to_dict(self):
        rv = dict()
        if not self.message:
            rv['return_code'] = self.return_code
            rv['message'] = err_msg[self.return_code]
        else:
            rv['message'] = self.message      
        return rv



class ValidationError(CustomError):
    def __init__(self, message="参数不合法"):
        super(ValidationError, self).__init__(message=message)
        self.level = CustomError.LEVEL_INFO


class NotFoundError(CustomError):
    def __init__(self, message="资源不存在"):
        super(NotFoundError, self).__init__(message=message)
        self.level = CustomError.LEVEL_WARN



class OrmError(CustomError):
    def __init__(self, message="数据库错误"):
        super(OrmError, self).__init__(message=message, status_code=500)
        self.level = CustomError.LEVEL_ERROR