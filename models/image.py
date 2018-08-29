from db import db

class image(db.Model):
    """docstring for image"""
    id = db.Column(db.Integer, primary_key=True)
    file = db.Column(db.LargeBinary, nullable=False)


    def save_to_db(self):
        # 插入行
        db.session.add(self)
        # 提交改动
        db.session.commit()
