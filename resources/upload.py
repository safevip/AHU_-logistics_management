from flask_restful import Resource, reqparse
import werkzeug
from resources.Base import BaseResource

class UploadImg(BaseResource):
    #图片上传测试
    def post(self, name):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        audioFile = args['file']
        audioFile.save("%s.jpg" % (name))
        return {'message': 'upload success'}, 200



