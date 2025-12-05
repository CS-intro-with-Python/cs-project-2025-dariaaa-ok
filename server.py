from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/dogs")
def list_dogs():
    return {"message": "List our dogs"}


@app.route("/cats")
def list_cats():
    return {"message": "List our cats"}


@app.route("/cats/<int:cat_id>")
def get_cat(cat_id):
    return {"message": f"Here should be a cat with id {cat_id}"}


@app.route("/dogs/<int:dog_id>")
def get_dog(dog_id):
    return {"message": f"Here should be a dog with id {dog_id}"}


@app.route("/dogs/<int:dog_id>/edit", methods=["GET", "POST"])
def edit_dog(dog_id):
    return {"message": f"Edit a dog with id {dog_id} and redirect to get a dog"}


@app.route("/cats/<int:cat_id>/edit", methods=["GET", "POST"])
def edit_cat(cat_id):
    return {"message": f"Edit a cat with id {cat_id} and redirect to get a cat"}


@app.route("/dogs/<int:dog_id>/delete", methods=["POST"])
def delete_dog(dog_id):
    return {"message": f"Delete a dog with id {dog_id} and redirect to the list of dogs"}


@app.route("/cats/<int:cat_id>/delete", methods=["POST"])
def delete_cat(cat_id):
    return {"message": f"Delete a cat with id {cat_id} and redirect to the list of cats"}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
