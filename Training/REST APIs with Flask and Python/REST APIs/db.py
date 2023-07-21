from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

stores = {}

items = {
    1 : {
        "name": "chair",
        "price": 17.99
    },
    2 : {
        "name": "Table",
        "price": 180.99
    }
}