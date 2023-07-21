from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.column(db.Integer, primary_key =True)
    name = db.column(db.String(80),unique =False, nullable=False)
    price = db.column(db.Float(precision=2), unique=False, nullable =False )
    store_id =db.column(db.Integer, db.ForeignKey("stores.id"), unique = False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")