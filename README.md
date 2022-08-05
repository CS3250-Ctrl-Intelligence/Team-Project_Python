# Team-Project_Python

In this project we built an ecommerce website that is supported with backend capabilities such as a MySQL database to keep track of inventory. We have also built an app that can only be accessed by employees that is used to track company revenue, progression, and marketing information. 

# Installation

## Install pip
<hr />

You'll need to make sure you havce the lastest version of pip installed

```
py -m pip install --upgrade pip
```
## Install Virtual Environment
<hr />

```
py -m pip install --user virtualenv
```
## Create Virtual Environment
<hr />

```
py -m venv env
```
## Activate Virtual Environment
<hr />

After your virtual environment has been created, run this command:

```
.\env\Scripts\activate
```

As long as your virtual environment is activated, pip will install packages into that specific environment 

## Required Module
<hr />
 
To install required modules for django, run this command **INSIDE** of the virtual environment:

```
pip install -r requirements.txt
```

There are two requirements.txt file, each in the front end and back end files. 



# Using the project

To use the project the user will have to input the values for their database whether it is remote or local. 
For the web side this will be in the settings.py file and the GUI side will be in the dbscript.py file.

When the database is connected the user can run the web host in a virtual environment and go to "localhost:8000" in their browser.
To use the GUI side run the main.py file and you will have to create a user before being able to sign in.

# Credits

This project has been worked on by the users:

FindingDorri
Brlan7
CameronSpear
Matthewjww
SHamil36

# License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

