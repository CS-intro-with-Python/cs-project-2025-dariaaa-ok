[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)
# CS_2025_project

## Description

This project is an Animal Shelter Management Tool for keeping track of the animals in the shelter. Users can view and sort cats and dogs, edit or delete animal records, and see basic information about them.

## Setup

```
docker build -t animalshelter:latest .
docker run -p 8080:5000 animalshelter:latest
```

## Requirements

[Describe technologies, libraries, languages you are using (this can be updated in the future).]: #

* Python 3.11

* Flask

* Docker


## Features

View all animals - See a list of cats and dogs in the shelter.

Sort animals - Filter or sort animals by type (cats/dogs) or other basic info.

Edit animal records - Update details about an animal.

Delete animal records - Remove an animal from the system.

## Git

[Specify which branch will store the latest stable version of the application]: #

* `main` branch stores the latest stable version.

## Success Criteria

[Describe the criteria by which the success of the project can be determined
(this will be updated in the future)]: #

* Users can view, sort, edit, and delete animals successfully.

* Application runs in Docker without errors.

