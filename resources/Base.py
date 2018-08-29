from flask_restful import Resource
from db import db

class BaseResource(Resource):

    def save_to_db(self):
        # 插入行
        db.session.add(self)
        # 提交改动
        db.session.commit()
        
    def to_json(self, model):
        dict = model.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        for (k,v) in dict.items():
            if isinstance(v, datetime):
                dict[k] = v.strftime('%Y-%m-%d %H:%M:%S')
        return dict
    