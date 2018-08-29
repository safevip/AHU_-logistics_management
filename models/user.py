from datetime import datetime

from db import db, cache
from common.exception import OrmError

class UserModel(db.Model):
    # UserModel对应的表格： users
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)

    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('AddressModel', backref=db.backref('users', lazy=True))

    def save_to_db(self):
        # 插入行
        db.session.add(self)
        # 提交改动
        db.session.commit()

    def json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        for (k,v) in dict.items():
            if isinstance(v, datetime):
                dict[k] = v.strftime('%Y-%m-%d %H:%M:%S')
        return dict

    @classmethod
    @cache.memoize(60)
    def find_by_name(cls, username):
        # 根据一定条件检索
        sql = cls.query.filter_by(username=username)
        return sql.first()


    @classmethod
    def find_by_id(cls, _id):
        try:
            sql = cls.query.filter_by(id=_id)
            return sql.first()
        except Exception as e:
            raise OrmError()

