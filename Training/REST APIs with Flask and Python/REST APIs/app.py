from flask import  Flask, request

app=Flask(__name__)

stores = [
    {
        "name":"my store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99

            }
        ]
    }
]

@app.route("/")
def home():
    return "Welcome to your first API "
@app.get("/store")
def get_stores():
    return {"stores":stores}

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404
