PySprings Badging System
========================
[![Build Status](https://travis-ci.org/pysprings/Pysprings_Badging_System.svg?branch=master)](https://travis-ci.org/pysprings/Pysprings_Badging_System)

A web application to keep track of 'merit badges' for the PySprings users group.

This is a Django application that allows for people to track what they've learned.
It also allows you to see what you have the prerequisites for.


Getting Started
---------------

### Environment Setup
1.  Clone the project
1.  `cd` into the source folder
1.  Ensure Python3.6 is installed  
    `python3.6 --version`
1.  Ensure `pipenv` is installed  
    `pipenv --version`
1.  Create a virtual environment with `pipenv`  
    `pipenv install --dev`
1.  Activate the virtual environment  
    `pipenv shell`
1.  Install the `pre-commit` hooks  
    `pre-commit install`

### Running the project
 - Clone project & cd to the `badging` folder
 - run `python manage.py migrate`
 - `python manage.py runserver` to start on localhost

Build
-----
**TODO:** Continuous integration

Testing
-------
To run the tests, run the command `make tests`.
There are several environment variables that need to be set and the make file sets them.

Installation
------------
**TODO**

Contribution Guide
------------------
- Pull requests welcome.
- Summarize your change in the present imperative on the first of your commits.
- Please reference any tickets that should be closed in the body so GitHub will do so automatically.

License
-------
See LICENSE
