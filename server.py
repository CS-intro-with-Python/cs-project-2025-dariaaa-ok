import os
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use DATABASE_URL if provided (e.g. PostgreSQL in production); fall back to SQLite for CI and local runs
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or "sqlite:///shelter.db"

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
    cat = Cat.query.get_or_404(cat_id)
    return render_template('cat.html', cat=cat)

@app.route("/dogs/<int:dog_id>")
def get_dog(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    return render_template('dog.html', dog=dog)

@app.route("/cats/<int:cat_id>/edit", methods=["GET", "POST"])
def edit_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    if request.method == "POST":
        # Update cat
        cat.name = request.form.get("name")
        cat.breed = request.form.get("breed") or None
        cat.age = int(request.form.get("age") or cat.age)
        cat.gender = request.form.get("gender") or None
        cat.weight = request.form.get("weight") or None
        cat.arrival_date = datetime.strptime(request.form.get("arrival_date"), "%Y-%m-%d").date()
        cat.adopted = "adopted" in request.form
        cat.rabies_vaccine = "rabies_vaccine" in request.form
        cat.feline_leukemia_vaccine = "feline_leukemia_vaccine" in request.form
        cat.indoor = "indoor" in request.form
        cat.declawed = "declawed" in request.form
        cat.litter_trained = "litter_trained" in request.form

        cat.favorite_toy = request.form.get("favorite_toy") or None
        cat.character = request.form.get("character") or None
        cat.notes = request.form.get("notes") or None
        cat.picture_url = request.form.get("picture_url") or cat.picture_url

        db.session.commit()
        return redirect(url_for("get_cat", cat_id=cat.id))

    return render_template("cat_edit.html", cat=cat)



@app.route("/dogs/<int:dog_id>/edit", methods=["GET", "POST"])
def edit_dog(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    if request.method == "POST":
        dog.name = request.form.get("name")
        dog.breed = request.form.get("breed") or None
        dog.age = int(request.form.get("age"))
        dog.gender = request.form.get("gender") or None
        dog.weight = request.form.get("weight") or None

        dog.arrival_date = datetime.strptime(
            request.form.get("arrival_date"), "%Y-%m-%d"
        ).date()

        dog.adopted = "adopted" in request.form
        dog.rabies_vaccine = "rabies_vaccine" in request.form
        dog.distemper_vaccine = "distemper_vaccine" in request.form
        dog.parvo_vaccine = "parvo_vaccine" in request.form

        dog.trained = "trained" in request.form
        dog.good_with_children = "good_with_children" in request.form

        dog.size = request.form.get("size") or None
        dog.energy_level = request.form.get("energy_level") or None
        dog.character = request.form.get("character") or None
        dog.notes = request.form.get("notes") or None
        dog.picture_url = request.form.get("picture_url") or dog.picture_url

        db.session.commit()
        return redirect(url_for("get_dog", dog_id=dog.id))

    return render_template("dog_edit.html", dog=dog)


@app.route("/dogs/<int:dog_id>/delete", methods=["POST"])
def delete_dog(dog_id):
    dog = Dog.query.get_or_404(dog_id)
    db.session.delete(dog)
    db.session.commit()
    return redirect(url_for("list_dogs"))


@app.route("/cats/<int:cat_id>/delete", methods=["POST"])
def delete_cat(cat_id):
    cat = Cat.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    return redirect(url_for("list_cats"))


@app.route("/cats/add", methods=["GET", "POST"])
def add_cat():
    if request.method == "POST":
        cat = Cat(
            name=request.form.get("name"),
            breed=request.form.get("breed") or None,
            age=int(request.form.get("age")),
            gender=request.form.get("gender") or None,
            weight=request.form.get("weight") or None,
            arrival_date=datetime.strptime(request.form.get("arrival_date"), "%Y-%m-%d").date(),
            adopted="adopted" in request.form,
            rabies_vaccine="rabies_vaccine" in request.form,
            feline_leukemia_vaccine="feline_leukemia_vaccine" in request.form,
            indoor="indoor" in request.form,
            declawed="declawed" in request.form,
            litter_trained="litter_trained" in request.form,
            favorite_toy=request.form.get("favorite_toy") or None,
            character=request.form.get("character") or None,
            notes=request.form.get("notes") or None,
            picture_url=request.form.get("picture_url") or None
        )
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('get_cat', cat_id=cat.id))

    return render_template('add_cat.html')

@app.route("/dogs/add", methods=["GET", "POST"])
def add_dog():
    if request.method == "POST":
        dog = Dog(
            name=request.form.get("name"),
            breed=request.form.get("breed") or None,
            age=int(request.form.get("age")),
            gender=request.form.get("gender") or None,
            weight=request.form.get("weight") or None,
            arrival_date=datetime.strptime(
                request.form.get("arrival_date"), "%Y-%m-%d"
            ).date(),

            adopted="adopted" in request.form,
            rabies_vaccine="rabies_vaccine" in request.form,
            distemper_vaccine="distemper_vaccine" in request.form,
            parvo_vaccine="parvo_vaccine" in request.form,
            trained="trained" in request.form,
            good_with_children="good_with_children" in request.form,

            size=request.form.get("size") or None,
            energy_level=request.form.get("energy_level") or None,
            character=request.form.get("character") or None,
            notes=request.form.get("notes") or None,
            picture_url=request.form.get("picture_url") or None
        )

        db.session.add(dog)
        db.session.commit()
        return redirect(url_for("get_dog", dog_id=dog.id))

    return render_template("add_dog.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
