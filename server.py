from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def return_hello():
    return "Hello World!"

@app.route("/home")
def home():
    return {"message": "Fluffy & Barky Animal Shelter"}

@app.route("/animals")
def list_animals():
    return {"message": "List all animals"}

@app.route("/animals/dogs")
def list_dogs():
    return {"message": "List our dogs"}

@app.route("/animals/cats")
def list_cats():
    return {"message": "List our cats"}

@app.route("/animals/cats/<int:cat_id>")
def get_cat(cat_id):
    return {"message": f"Here should be a cat with id {cat_id}"}

@app.route("/animals/dogs/<int:dog_id>")
def get_dog(dog_id):
    return {"message": f"Here should be a dog with id {dog_id}"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)