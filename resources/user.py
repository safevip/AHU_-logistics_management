from flask_restful import Resource, reqparse, abort,  marshal_with
from flask import current_app as app

# 导入对应的模型类
from models.user import UserModel
from models.address import AddressModel
from common.validation import NamePwdParser
from common.fields import resource_fields


class User(Resource):
  @marshal_with(resource_fields)
  def get(self, name):
    user = UserModel.find_by_name(name)
    if user:
      return user
    abort(404, message="user {} doesn't exist".format(name))

  def put(self, name):
    args = NamePwdParser.parse_args()
    user = UserModel.find_by_name(name)
    if user:
      user.username = args['name']
      user.password = args['password']
      user.save_to_db()
      return {'message': 'upate success'}, 200
    abort(404, message="user {} doesn't exist".format(name))



class UserList(Resource):
  def get(self):
    return {'users': [user.json() for user in UserModel.query.all()]}



