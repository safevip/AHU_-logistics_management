from flask_restful import reqparse

NamePwdParser = reqparse.RequestParser()
NamePwdParser.add_argument('username', type=str, required=True, location='form') # 默认从过滤form 可以指定为json
NamePwdParser.add_argument('password', type=int, required=True)

