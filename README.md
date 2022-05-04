# Team-Project_Python

This is a a database oriented project that has two sides. Their is the the web side for the customers and is built using Python and Django. The other is the GUI side for the 
employees that is using Python and PyQt6. The database server that is being use is a MySQL and is host by bluehost.com.

## Installation

There are many packages that need to be installed using the python package manager [pip](https://pip.pypa.io/en/stable/)
The web side has a requirement.txt file that can be used to install the majority of the packages.

'''bash
pip install -r requirements.txt
'''

In addition, the majority of the project is run through a virtual environment

The GUI side does not have a text file to make it easy but there are not many packages to install.

'''bash
pip install pyqt6
'''

'''bash
pip install pyqt6-tools
'''

'''bash
pip install pyqtgraph
'''

'''bash
pip install mysql-connector-python
'''

# Using the project

To use the project the user will have to input the values for their database whether it is remote or local. 
For the web side this will be in the settings.py file and the GUI side will be in the dbscript.py file.

When the database is connect the user can run the web host in a virtual environment and go to "127.0.0.1" in their browser.
To use the GUI side run the main.py file and you will have to create a user before baing able to sign in.

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

