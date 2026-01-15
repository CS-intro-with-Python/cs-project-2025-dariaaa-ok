[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DESIFpxz)

# CS_2025_project

## Description

This project is an Animal Shelter Management Tool for keeping track of the animals in the shelter. Users can view cats
and dogs, access their detailed profiles, add new animals, edit existing records, and delete animals from the system.

## Setup

Run the application using Docker Compose:

`docker-compose up --build`

The application will be available at:
`http://localhost:8080`

## Requirements

* Python 3.11

* Flask

* Flask-SQLAlchemy

* PostgreSQL

* Docker and Docker Compose

* Requests

* pytest

## Features

* View all animals - See a list of cats and dogs in the shelter.

* View cats and dogs separately

* View detailed information for each animal

* Add new cats and dogs

* Edit animal records

* Delete animal records

## Client and Healthcheck

Run `client.py` to check that the main routes are accessible:

`python client.py`

## CI/CD

The project uses GitHub Actions to:

* Build the Docker images

* Start the application using Docker Compose

* Run unit and integration tests

* Execute a healthcheck client to verify route availability

## Git

[Specify which branch will store the latest stable version of the application]: #

* `main` branch stores the latest stable version.

## Success Criteria

[Describe the criteria by which the success of the project can be determined
(this will be updated in the future)]: #

* Users can view, add, edit, and delete animals

* The application runs correctly using Docker Compose

* All main routes return valid responses

* CI workflows pass successfully
