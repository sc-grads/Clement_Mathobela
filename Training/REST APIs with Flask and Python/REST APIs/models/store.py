from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.column(db.Integer, primary_key =True)
    name = db.column(db.String(80),unique =False, nullable=False)
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
