from db import db
class AddressModel(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))   

        