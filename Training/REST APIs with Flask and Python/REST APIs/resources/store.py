import uuid
from flask_smorest import Blueprint, abort
from flask import  request
from flask.views import MethodView

from ..db import stores

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except:
            abort (message="Store not found!")
    def __delete__(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except:
            return {"message": "Store not found"}
@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:
            abort(400,"Bad Request!, Ensure 'name' and 'price' are included in the JSON Payload")

        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort("Store already exists")
        store_id = uuid.uuid4().hex
        store = {**store_data,"id":store_id}
        stores[store_id] = store
        return store