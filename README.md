# AirBnB clone - The Console

Airbnb, as in “Air Bed and Breakfast,” is a service that lets property owners rent out their spaces to travelers looking for a place to stay. Travelers can rent a space for multiple people to share, a shared space with private rooms, or the entire property for themselves.

### 🎯 Learning Objectives
---

* How to create a Python package
* How to create a command interpreter in Python using the ``cmd`` module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage ``datetime``
* What is an ``UUID``
* What is ``*args`` and how to use it
* What is ``**kwargs`` and how to use it
* How to handle named arguments in a function

### 📋 Requirements
---

#### Python Scripts

* Allowed editors: ``vi``, ``vim``, ``emacs``.
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
* The first line of all your files should be exactly ``#!/usr/bin/python3``
* All your files must be executable
* The length of your files will be tested using ``wc``
* Your code should use the pycodestyle (version 2.7.*)

#### Python Unit Tests

* All your test files should be inside a folder ``tests``
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* All your test files should be python files (extension: ``.py``)

### ⌨️ Repository projects
---

#### Scripts

|File|Description|
|---|---|
|[console.py](https://github.com/rayd1893/AirBnB_clone/blob/main/console.py)|Contains the entry point of the command interpreter.|
|[models/base_model.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/base_model.py)|Defines all common attributes/methods for other classes.|
|[models/amenity.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/amenity.py)|Defines class Amenity|
|[models/city.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/city.py)|Defines class City|
|[models/place.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/place.py)|Defines class Place|
|[models/review.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/review.py)|Defines class Review|
|[models/state.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/state.py)|Defines class State|
|[models/user.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/user.py)|Defines class User|
|[models/engine/file_storage.py](https://github.com/rayd1893/AirBnB_clone/blob/main/models/engine/file_storage.py)|Serializes instances to a JSON file and deserializes JSON file to instances.|



