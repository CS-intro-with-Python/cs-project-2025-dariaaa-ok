# Routes Documentation

## Route "All Animals" (/) GET

**Shows:** Homepage with all animals combined (cats and dogs).

**Actions:**

* Click an animal image or name → redirects to /dogs/<id> or /cats/<id>
* Click _View Dogs_ -> /dogs
* Click _View Cats_ -> /cats

**Elements:**

* List of animal names with images.
* Buttons: _View Dogs_, _View Cats_

---

## Route "All dogs" (/dogs) GET

**Shows:** List of all dogs (name+ picture).

**Actions:**

* Click a dog to view details (redirects to /dogs/<id>).
* Navigate back to home.

**Elements:**

* List of dog names with images.

---

## Route "All cats" (/cats) GET

**Shows:** List of all cats.

**Actions:**

* Click a cat to view details (redirects to /cats/<id>).
* Navigate back to home.

**Elements:**

* List of cat names with images.

---

## Route "Add a new dog" (/dogs/add) GET

**Shows:** Form for adding a new dog to the shelter.

**Actions:**

* Fill out the form
* Submit to create a dog
* _Cancel_ -> redirects to /dogs

**Elements:**

* Form fields (name, age, breed, vaccines, size, etc.)
* _Add Dog_ button
* _Cancel_ button

---

## Route "Add a new dog" (/dogs/add) POST

**Does:**

* Creates a new dog in the database
* Redirects to /dogs/<id> on success
* Returns 400 on invalid age

---

## Route "Add a new cat" (/cats/add) GET

**Shows:** Form for adding a new cat to the shelter.

**Actions:**

* Fill out the form
* Submit to create a cat
* _Cancel_ -> redirects to /cats

**Elements:**

* Form fields (name, age, breed, vaccines, indoor, etc.)
* _Add Cat_ button
* _Cancel_ button

---

## Route "Add a new cat" (/cats/add) POST

**Does:**

* Creates a new cat in the database
* Redirects to /cats/<id> on success
* Returns 400 on invalid age

---

## Route "A specific dog" (/dogs/<int:dog_id>) GET

**Shows:** Detailed profile page for one dog.

**Actions:**

* Edit the dog
* Delete the dog
* Navigate to home or all dogs

**Elements:**

* Dog details (name, picture, breed, age, vaccines, size, character, notes)
* _Edit_ button -> redirects to /dogs/<dog_id>/edit.
* _Delete_ button -> submits POST to /dogs/<dog_id>/delete.
* Navigation icons

---

## Route "A specific cat" (/cats/<int:cat_id>) GET

**Shows:** Detailed profile page for one cat.

**Actions:**

* Edit the cat
* Delete the cat
* Navigate to home or all cats

**Elements:**

* Cat details (name, picture, breed, age, vaccines, indoor, litter trained, notes)
* _Edit_ button -> redirects to /cats/<cat_id>/edit.
* _Delete_ button -> submits POST to /cats/<cat_id>/delete.
* Navigation icons

---

## Route "Edit dog information" (/dogs/<int:dog_id>/edit) GET

**Shows:** Form pre-filled with the dog’s current information.

**Actions:**

* Update fields
* Save changes
* Cancel -> return to dog page

**Elements:**

* Edit form
* _Save_ button
* _Cancel_ button

---

## Route "Edit dog information" (/dogs/<int:dog_id>/edit) POST

**Does:**

* Updates dog data in the database
* Redirects to /dogs/<dog_id>

---

## Route "Edit cat's information" (/cats/<int:cat_id>/edit) GET 

**Shows:** Form pre-filled with the cat’s current information.

**Actions:**

* Update fields
* Save changes
* Cancel -> return to cat page

**Elements:**

* Edit form
* _Save_ button
* _Cancel_ button

---

## Route "Edit cat information" (/cats/<int:cat_id>/edit) POST

**Does:**

* Updates cat data in the database
* Redirects to /cats/<cat_id>

---

## Route "Delete a dog" (/dogs/<int:dog_id>/delete) POST

**Actions:**

* Deletes the dog from the database.
* Redirects to /dogs.

**Elements:**

* _Delete_ button (POST form).

---

## Route "Delete a cat" (/cats/<int:cat_id>/delete) POST

**Actions:**

* Deletes the cat from the database.
* Redirects to /cats.

**Elements:**

* _Delete_ button (POST form).
