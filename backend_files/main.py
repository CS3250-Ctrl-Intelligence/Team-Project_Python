import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
import dbscript
import time



#This class displays the welcome screen
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(r'''backend_files\welcome.ui''',self)
        
        #Implementation of the buttons on the page.
        self.pushButton_login.clicked.connect(self.goToLogin)
        self.pushButton_newAcc.clicked.connect(self.goToCreate)

    #function to bring you to login page
    def goToLogin(self):
        login = UserLoginChoice()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #function to bring you to create user page
    def goToCreate(self):
        createChoice = CreateChoiceScreen()
        widget.addWidget(createChoice)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class brings up a page where the user picks if they are an employee or customer
class UserLoginChoice(QDialog):
    def __init__(self):
        super(UserLoginChoice, self).__init__()
        loadUi(r'''backend_files\userLogin.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_employee.clicked.connect(self.employeeLogin)

    #function to bring user to employee login page.
    def employeeLogin(self):
        login = EmployeeLoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the employee login screen
class EmployeeLoginScreen(QDialog):
    def __init__(self):
        super(EmployeeLoginScreen, self).__init__()
        loadUi(r'''backend_files\login.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_login.clicked.connect(self.loginFunc)

    #function to bring you to the dashboard if you successfully log in
    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #function to login in. 
    def loginFunc(self):

        #get the user input from the text fields
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        #Connect to the database
        result = dbscript.Database_Functions.login(username, password)

        #if username and/or password do not match a record print error text
        if result ==None:
            self.label_result.setText("Incorrect username or password")

        #if successfully verified call dashboard function
        else:
            self.goToDashboard()

class CreateChoiceScreen(QDialog):
    def __init__(self):
        super(CreateChoiceScreen, self).__init__()
        loadUi(r'''backend_files\userCreate.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_employee.clicked.connect(self.employeeCreate)

    #function to go to the create employee screen
    def employeeCreate(self):
        create = CreateEmpScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the create employee screen
class CreateEmpScreen(QDialog):
    def __init__(self):
        super(CreateEmpScreen, self).__init__()
        loadUi(r'''backend_files\createEmployee.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_signup.clicked.connect(self.signup)
        
    #function to create a record in the table employees
    def signup(self):
        #get user input from text fields
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confPassword = self.lineEdit_confpassword.text()

        #test to if all fields have an input and the password and confirm password match each other.
        if len(username)==0 or len(password)==0 or len(confPassword)==0:
            self.label_result.setText("Please fill in all fields.")

        elif password != confPassword:
            self.label_result.setText("Passwords do not match")

        else:
            dbscript.Database_Functions.createEmployee(username, password)

        #display on screen that employee was created
        self.label_result.setText("Employee created, returning to main screen")

        #wait 4 seconds before returning to welcome screen
        time.sleep(1)

        #returns to welcome screen after employee is created.
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DashboardScreen(QDialog):
    def __init__(self):
        super(DashboardScreen, self).__init__()
        loadUi(r'''backend_files\dashboard.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_inv.clicked.connect(self.goToInv)
        self.pushButton_custOrders.clicked.connect(self.goToOrders)

    #function to go to the inventory screen
    def goToInv(self):
        inventory = InvScreen()
        widget.addWidget(inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #function to go to the customer orders screen
    def goToOrders(self):
        orders = OrdersScreen()
        widget.addWidget(orders)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the inventory screen
class InvScreen(QDialog):
    def __init__(self):
        super(InvScreen, self).__init__()
        loadUi(r'''backend_files\inventory.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_import.clicked.connect(self.importData)
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_delete.clicked.connect(self.goToDelete)
        self.pushButton_update.clicked.connect(self.goToUpdate)
        self.pushButton_back.clicked.connect(self.goToDashboard)

    #function to pull all the database from mysql server and display it on screen.
    def fetchData(self):

        result = dbscript.Database_Functions.fetchInventory()

        #starts row count at 0 and inserts all the data for each row
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    #function to import data from .csv file to mysql database
    def importData(self):
        
        dbscript.Database_Functions.importInventory()

    #function to open the delete product screen        
    def goToDelete(self):
        delete = DeleteScreen()
        delete.setFixedHeight(200)
        delete.setFixedWidth(500)
        delete.exec()

    #function to open the update product screen
    def goToUpdate(self):
        update = AddScreen()
        update.setFixedHeight(350)
        update.setFixedWidth(500)
        update.exec()

    #function to go back to the dashboard screen
    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the customer orders screen.
class OrdersScreen(QDialog):
    def __init__(self):
        super(OrdersScreen, self).__init__()
        loadUi(r'''backend_files\orders.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_back.clicked.connect(self.goToDashboard)

    #function to pull all the database from mysql server and display it on screen.
    def fetchData(self):

        result = dbscript.Database_Functions.fetchOrders()

        #starts row count at 0 and inserts all the data for each row
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    #function to import data from .csv file to mysql database
 
    #function to go back to the dashboard
    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
#This class displays the delete product screen
class DeleteScreen(QDialog):
    def __init__(self):
        super(DeleteScreen, self).__init__()
        loadUi(r'''backend_files\deleteData.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_commit.clicked.connect(self.deleteData)

    #function to delete data from the database
    def deleteData(self):

        product = self.lineEdit_product.text()

        dbscript.Database_Functions.deleteInventory(product)


#This class displays the update the 
class AddScreen(QDialog):
    def __init__(self):
        super(AddScreen, self).__init__()
        loadUi(r'''backend_files\addData.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_commit.clicked.connect(self.addData)

    #function to add new data record to the database table inventory
    def addData(self):

        #get user input fields for new product and info
        product = self.lineEdit_product.text()
        quantity = self.lineEdit_quantity.text()
        wholesale = self.lineEdit_wholesale.text()
        sale = self.lineEdit_sale.text()
        supplier = self.lineEdit_supplier.text()

        dbscript.Database_Functions.addInventory(product, quantity, wholesale, sale, supplier)

#call the database.py main() function and and open the welcome screen with fixed height and width 
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")