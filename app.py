import os
import logging

from flask import Flask, jsonify
from flask_restful import Api

from resources.user import User,UserList
from resources.upload import UploadImg
from db import db, cache
from common.exception import CustomError, OrmError

app = Flask(__name__)

# 数据库配置
basedir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') #配置flask的地址
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 日志系统配置
logging.basicConfig(filename="app.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 缓存配置
cache.init_app(app)

# 全局异常处理
@app.errorhandler(CustomError)
def custom_error_handler(error):
    if error.level in [CustomError.LEVEL_WARN, CustomError.LEVEL_ERROR]:
        if isinstance(error, OrmError):
            app.logger.exception(error.message)
        else:
            app.logger.error('错误信息: %s' % (error.message))
    response = jsonify(error.to_dict())  
    response.status_code = error.status_code   
    return response

    
@app.before_first_request
def create_tables():
    db.create_all()


# 绑定资源
api = Api(app)
api.add_resource(User, '/user/<string:name>')
api.add_resource(UserList, '/users')
api.add_resource(UploadImg, '/upload/<string:name>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
