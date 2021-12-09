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

#### Tests

|File|Description|
|---|---|
|[tests/test_console.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_console.py)|unittests for console.|
|[tests/test_models/test_base_model.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_base_model.py)|unittests for class BaseModel.|
|[tests/test_models/test_amenity.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_amenity.py)|unittests for class Amenity.|
|[tests/test_models/test_city.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_city.py)|unittests for class City.|
|[tests/test_models/test_place.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_place.py)|unittests for class Place.|
|[tests/test_models/test_review.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_review.py)|unittests for class Review.|
|[tests/test_models/test_state.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_state.py)|unittests for class State.|
|[tests/test_models/test_user.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_user.py)|unittests for class User.|
|[tests/test_models/test_engine/test_file_storage.py](https://github.com/rayd1893/AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py)|Unittests for class FileStorage.|

### 💻 Console
---

the console contains the entry point of the command interpreter.

#### 🛠️ Installation

1. Clone this repository
```bash
$ git clone git@github.com:rayd1893/AirBnB_clone.git
```

2. Access AirBnb directory
```bash
$ cd AirBnB_clone
```

3. Run hbnb(interactively)
```bash
$ ./console.py
```

4. When this command is run the following prompt should appear:
```bash
(hbnb)
```

#### 📖 Commands

|Command|Description|
|---|---|
|``create``|Creates a new instance of BaseModel.|
|``show``|Prints the string representation of an instance based on the class name and id.|
|``destroy``|Deletes an instance based on the class name and id (save the change into the JSON file).|
|``all``|Prints all string representation of all instances based or not on the class name.|
|``update``|Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).|
|``count``|Count instances of the class.|
|``quit`` or ``EOF``|Quit command to exit the program|

### ✒️ Authors
---

Rayd Trujillo - [rayd1893](https://github.com/rayd1893)
Sammy Samp - [sammysamp](https://github.com/sammysamp)


