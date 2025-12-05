# Routes Documentation

## Route "All Animals" (/) GET

**Shows:** Homepage with all animals listed (cats and dogs).

**Actions:**

* Click on an animal name or picture to view details (redirects to /dogs/<id> or /cats/<id>).
* Click on "Dogs" or "Cats" buttons to filter the list (redirects to /dogs or /cats).

**Elements:**

* List of animal names with images.
* Filter buttons: Dogs, Cats.

---

## Route "All dogs" (/dogs) GET

**Shows:** List of all dogs.

**Actions:**

* Click on a dog's name or picture to view details (redirects to /dogs/<id>).
* Optional: filter dogs by name.

**Elements:**

* List of dog names with images.

---

## Route "All cats" (/cats) GET

**Shows:** List of all cats.

**Actions:**

* Click on a cat's name or picture to view details (redirects to /cats/<id>).
* Optional: filter cats by name.

**Elements:**

* List of cat names with images.

---

## Route "A specific dog" (/dogs/<int:dog_id>) GET

**Shows:** Details page for a single dog.

**Actions:**

* Edit or delete this dog.

**Elements:**

* Name, picture, and other info.
* "Edit" button -> redirects to /dogs/<dog_id>/edit.
* "Delete" button -> submits POST to /dogs/<dog_id>/delete.

---

## Route "A specific cat" (/cats/<int:cat_id>) GET

**Shows:** Details page for a single cat.

**Actions:**

* Edit or delete this cat.

**Elements:**

* Name, picture, and other info.
* "Edit" button -> redirects to /cats/<cat_id>/edit.
* "Delete" button -> submits POST to /cats/<cat_id>/delete.

---

## Route "Edit dog's information" (/dogs/<int:dog_id>/edit) GET + POST

**Shows:** Form page to edit dog information.

**Actions:**

* Fill out form and submit to update info.
* Redirects to /dogs/<dog_id> after submission.

**Elements:**

* Form fields for name, picture URL, and other details.
* Submit button: "Update Dog".

---

## Route "Edit cat's information" (/cats/<int:cat_id>/edit) GET + POST

**Shows:** Form page to edit cat information.

**Actions:**

* Fill out form and submit to update info.
* Redirects to /cats/<cat_id> after submission.

**Elements:**

* Form fields for name, picture URL, and other details.
* Submit button: "Update Cat".

---

## Route "Delete a dog" (/dogs/<int:dog_id>/delete) POST

**Shows:** No page; action deletes dog and redirects.

**Actions:**

* Deletes the dog from the database.
* Redirects to /dogs.

**Elements:**

* "Delete" button (form submits POST).

---

## Route "Delete a cat" (/cats/<int:cat_id>/delete) POST

**Shows:** No page; action deletes cat and redirects.

**Actions:**

* Deletes the cat from the database.
* Redirects to /cats.

**Elements:**

* "Delete" button (form submits POST).
