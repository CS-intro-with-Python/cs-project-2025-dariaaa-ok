from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, union_all

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:daria@localhost:5433/shelter"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Cat(db.Model):
    __tablename__ = "cat"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(40))
    age = db.Column(db.Integer, db.CheckConstraint('age  between 0 and 40'), nullable=False)
    gender = db.Column(db.String(6), db.CheckConstraint("gender IN ('male', 'female')"))
    weight = db.Column(db.Numeric(6, 2))
    arrival_date = db.Column(db.Date, nullable=False)
    adopted = db.Column(db.Boolean, default=False)
    rabies_vaccine = db.Column(db.Boolean, default=False)
    feline_leukemia_vaccine = db.Column(db.Boolean, default=False)
    indoor = db.Column(db.Boolean)
    declawed = db.Column(db.Boolean)
    favorite_toy = db.Column(db.String(30))
    litter_trained = db.Column(db.Boolean)
    character = db.Column(db.String(50))
    picture_url = db.Column(db.String(200))
    notes = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "weight": self.weight,
            "arrival_date": self.arrival_date,
            # "weight": float(self.weight) if self.weight else None,  # Convert to float
            # "arrival_date": self.arrival_date.isoformat() if self.arrival_date else None,  # Convert to string
            "adopted": self.adopted,
            "rabies_vaccine": self.rabies_vaccine,
            "feline_leukemia_vaccine": self.feline_leukemia_vaccine,
            "indoor": self.indoor,
            "declawed": self.declawed,
            "favorite_toy": self.favorite_toy,
            "litter_trained": self.litter_trained,
            "character": self.character,
            "picture_url": self.picture_url,
            "notes": self.notes
        }


class Dog(db.Model):
    __tablename__ = "dog"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(40))
    age = db.Column(db.Integer, db.CheckConstraint('age  between 0 and 31'), nullable=False)
    gender = db.Column(db.String(6), db.CheckConstraint("gender IN ('male', 'female')"))
    weight = db.Column(db.Numeric(6, 2))
    arrival_date = db.Column(db.Date, nullable=False)
    adopted = db.Column(db.Boolean, default=False)
    rabies_vaccine = db.Column(db.Boolean, default=False)
    distemper_vaccine = db.Column(db.Boolean, default=False)
    parvo_vaccine = db.Column(db.Boolean, default=False)
    trained = db.Column(db.Boolean, default=False)
    size = db.Column(db.String(6), db.CheckConstraint("size IN ('small', 'medium', 'large')"))
    good_with_children = db.Column(db.Boolean)
    energy_level = db.Column(db.String(6), db.CheckConstraint("energy_level IN ('low', 'medium', 'high')"))
    character = db.Column(db.String(50))
    picture_url = db.Column(db.String(200))
    notes = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "age": self.age,
            "gender": self.gender,
            "weight": self.weight,
            "arrival_date": self.arrival_date,
            # "weight": float(self.weight) if self.weight else None,  # Convert to float
            # "arrival_date": self.arrival_date.isoformat() if self.arrival_date else None,  # Convert to string
            "adopted": self.adopted,
            "rabies_vaccine": self.rabies_vaccine,
            "distemper_vaccine": self.distemper_vaccine,
            "parvo_vaccine": self.parvo_vaccine,
            "trained": self.trained,
            "size": self.size,
            "good_with_children": self.good_with_children,
            "energy_level": self.energy_level,
            "character": self.character,
            "picture_url": self.picture_url,
            "notes": self.notes
        }


@app.route("/")
def get_all_animals():
    dogs = Dog.query.with_entities(Dog.id, Dog.name, Dog.picture_url).all()
    cats = Cat.query.with_entities(Cat.id, Cat.name, Cat.picture_url).all()
    animals = []
    for dog in dogs:
        animals.append({
            "id": dog.id,
            "name": dog.name,
            "picture_url": dog.picture_url,
            "type": "dog"
        }
        )

    for cat in cats:
        animals.append({
            "id": cat.id,
            "name": cat.name,
            "picture_url": cat.picture_url,
            "type": "cat"

        }
        )
    animals.sort(key=lambda a: a["name"])
    return render_template('index.html', animals=animals)


@app.route("/dogs")
def list_dogs():
    dogs = Dog.query.with_entities(Dog.id, Dog.name, Dog.picture_url).all()
    return render_template('dogs.html', dogs=dogs)


@app.route("/cats")
def list_cats():
    cats = Cat.query.with_entities(Cat.id, Cat.name, Cat.picture_url).all()
    return render_template('cats.html', cats=cats)


@app.route("/cats/<int:cat_id>")
def get_cat(cat_id):
    # cat = Cat.query.filter_by(id=cat_id).first()
    cat = Cat.query.get_or_404(cat_id)
    return render_template('cat.html', cat=cat)


@app.route("/dogs/<int:dog_id>")
def get_dog(dog_id):
    dog = Dog.query.filter_by(id=dog_id).get_or_404()
    return render_template('dog.html', dog=dog)


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
