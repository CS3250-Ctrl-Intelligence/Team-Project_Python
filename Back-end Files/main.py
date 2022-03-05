import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
import mysql.connector as mc
import csv
import database
import time



#This class displays the welcome screen
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui",self)
        
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
        loadUi("userLogin.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_employee.clicked.connect(self.employeeLogin)
        self.pushButton_customer.clicked.connect(self.customerLogin)

    #function to bring user to employee login page.
    def employeeLogin(self):
        login = EmployeeLoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #function to bring user to customer login page
    def customerLogin(self):
        login = CustomerLoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the employee login screen
class EmployeeLoginScreen(QDialog):
    def __init__(self):
        super(EmployeeLoginScreen, self).__init__()
        loadUi("login.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_login.clicked.connect(self.loginFunc)

    #function to bring you to the dashboard if you successfully log in
    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #function to login in. 
    def loginFunc(self):
        try:
            #get the user input from the text fields
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()

            #Connect to the database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            #find the username and password in the database table employees
            mycursor = mydb.cursor()
            query = "SELECT username,password from employees where username like '" + username + "'and password like '" + password +  "'"
            mycursor.execute(query)
            result = mycursor.fetchone()

            #if username and/or password do not match a record print error text
            if result ==None:
                self.label_result.setText("Incorrect email or password")

            #if successfully verified call dashboard function
            else:
                self.goToDashboard()

        #if error connecting to database. print error
        except mc.Error as e:
            self.label_result.setText("Error")

#This class displays the customer login screen
class CustomerLoginScreen(QDialog):
    def __init__(self):
        super(CustomerLoginScreen, self).__init__()
        loadUi("login.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_login.clicked.connect(self.loginFunc)

    #function to bring you to the dashboard if you successfully log in
    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    #function to log in
    def loginFunc(self):
        try:
            #get the user input from the text fields
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()

            #connect to the database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )
            #find the username and password in the database table customers
            mycursor = mydb.cursor()
            query = "SELECT username,password from customers where username like '" + username + "'and password like '" + password +  "'"
            mycursor.execute(query)
            result = mycursor.fetchone()

            #if username and/or password do not match a record print error text
            if result ==None:
                self.label_result.setText("Incorrect email or password")

            #if successfully verified call dashboard function
            else:
                self.goToDashboard()

        #if error connecting to database. print error
        except mc.Error as e:
            self.label_result.setText("Error")

#This class brings up a page where the user picks if they are an employee or customer
class CreateChoiceScreen(QDialog):
    def __init__(self):
        super(CreateChoiceScreen, self).__init__()
        loadUi("userCreate.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_employee.clicked.connect(self.employeeCreate)
        self.pushButton_customer.clicked.connect(self.customerCreate)

    #function to go to the create employee screen
    def employeeCreate(self):
        create = CreateEmpScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    #function to go the create customer screen
    def customerCreate(self):
        create = CreateCustScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the create employee screen
class CreateEmpScreen(QDialog):
    def __init__(self):
        super(CreateEmpScreen, self).__init__()
        loadUi("createEmployee.ui",self)

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
            try:
                #connect to database
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="project"
            )
                #create record of employee in database table employees
                mycursor = mydb.cursor()
                query = 'INSERT INTO employees(username, password)' 'VALUES(%s, %s)'
                value = (username, password)
                mycursor.execute(query, value)
                mydb.commit()

            #if error connecting to database. print error
            except mc.Error as e:
                self.label_result.setText("Error inserting data")

        #display on screen that employee was created
        self.label_result.setText("Employee created, returning to main screen")

        #wait 4 seconds before returning to welcome screen
        time.sleep(4)

        #returns to welcome screen after employee is created.
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the create customer screen.
class CreateCustScreen(QDialog):
    def __init__(self):
        super(CreateCustScreen, self).__init__()
        loadUi("createCustomer.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_signup.clicked.connect(self.signup)

    #function to create a record in the database
    def signup(self):
        #get user input from text fields
        email = self.lineEdit_custEmail.text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confPassword = self.lineEdit_confpassword.text()

        #validate that all text fields are filled in and that password and confpassword match
        if len(email)==0 or len(username)==0 or len(password)==0 or len(confPassword)==0:
            self.label_result.setText("Please fill in all fields.")

        elif password != confPassword:
            self.label_result.setText("Passwords do not match")

        else:
            try:
                #connect to database
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="project"
            )
                #create record in database table customers
                mycursor = mydb.cursor()
                query = 'INSERT INTO customers(cust_email, username, password)' 'VALUES(%s, %s, %s)'
                value = (email, username, password)
                mycursor.execute(query, value)
                mydb.commit()


            #if error connecting to database. print error
            except mc.Error as e:
                self.label_result.setText("Error inserting data")

            self.label_result.setText("Customer created, returning to main screen")
            time.sleep(4)

            welcome = WelcomeScreen()
            widget.addWidget(welcome)
            widget.setCurrentIndex(widget.currentIndex()+1)


#This class displays the dashboard screen after logging in
#############This is for both customers and employees at the moment.
class DashboardScreen(QDialog):
    def __init__(self):
        super(DashboardScreen, self).__init__()
        loadUi("dashboard.ui",self)

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
        loadUi("inventory.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_import.clicked.connect(self.importData)
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_delete.clicked.connect(self.goToDelete)
        self.pushButton_update.clicked.connect(self.goToUpdate)
        self.pushButton_back.clicked.connect(self.goToDashboard)

    #function to pull all the database from mysql server and display it on screen.
    def fetchData(self):
        try:
            #connect to the database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM {} ".format("inventory"))
            result = mycursor.fetchall()

            #starts row count at 0 and inserts all the data for each row
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        #if error connecting to database. print error
        except mc.Error as e:
            print("Error occured")
    
    #function to import data from .csv file to mysql database
    def importData(self):
        try:
            #connect to database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
        )
            mycursor = mydb.cursor()
            #open the .csv file and read it into variable.
            file = open("inventory_team1.csv")
            csv_data = csv.reader(file)

            skipHeader = True

            #import the data from csv variable into the database table "inventory"
            for row in csv_data:
                if skipHeader:
                    skipHeader = False
                    continue
                mycursor.execute('INSERT INTO inventory(Product_ID, Quantity, Wholesale_Price, Sale_Price, Supplier_ID)' 'VALUES(%s, %s, %s, %s, %s)', row)

        #if error connecting to database. print error
        except mc.Error as e:
            print("Error occured")

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
        loadUi("orders.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_import.clicked.connect(self.importData)
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_back.clicked.connect(self.goToDashboard)

    #function to pull all the database from mysql server and display it on screen.
    def fetchData(self):
        try:
            #connect to the database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM {} ".format("orders"))
            result = mycursor.fetchall()

            #starts row count at 0 and inserts all the data for each row
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        #if error connecting to database. print error
        except mc.Error as e:
            print("Error occured")

    #function to import data from .csv file to mysql database
    def importData(self):
        try:
            #connect to the database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
        )
            mycursor = mydb.cursor()

            #open the .csv file and read it into variable.
            file = open("customer_orders_team1.csv")
            csv_data = csv.reader(file)

            skipHeader = True

            #import the data from csv variable into the database table "inventory"
            for row in csv_data:
                if skipHeader:
                    skipHeader = False
                    continue
                mycursor.execute('INSERT INTO orders(Date, Cust_Email, Cust_Location, Product_ID, Quantity)' 'VALUES(%s, %s, %s, %s, %s)', row)

        #if error connecting to database. print error
        except mc.Error as e:
            print("Error occured")

    #function to go back to the dashboard
    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
#This class displays the delete product screen
class DeleteScreen(QDialog):
    def __init__(self):
        super(DeleteScreen, self).__init__()
        loadUi("deleteData.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_commit.clicked.connect(self.deleteData)

    #function to delete data from the database
    def deleteData(self):
        try:
            #connect to the database 
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )
            mycursor = mydb.cursor()
            product = self.lineEdit_product.text()
            query = ("DELETE FROM inventory WHERE Product_ID = '" + product + "'")
            
            #execute query to delete data from database
            mycursor.execute(query)
            mydb.commit()
            self.label_result.setText("Data has been deleted from the database")

        #if error connecting to database. print error
        except mc.Error as e:
            print("Error occured")

#This class displays the update the 
class AddScreen(QDialog):
    def __init__(self):
        super(AddScreen, self).__init__()
        loadUi("addData.ui",self)

        #Implementation of the buttons on the page.
        self.pushButton_commit.clicked.connect(self.addData)

    #function to add new data record to the database table inventory
    def addData(self):
        try:
            #connect to database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()

        
            #get user input fields for new product and info
            product = self.lineEdit_product.text()
            quantity = self.lineEdit_quantity.text()
            wholesale = self.lineEdit_wholesale.text()
            sale = self.lineEdit_sale.text()
            supplier = self.lineEdit_supplier.text()

            query = "INSERT INTO inventory (Product_ID, Quantity, Wholesale_Price, Sale_Price, Supplier_ID) VALUES (%s, %s, %s, %s, %s)"
            value = (product, quantity, wholesale, sale, supplier)

            mycursor.execute(query, value)

            #pushes the new data to the inventory table in the database.
            mydb.commit()
            self.label_result.setText("Data added to database")

        #if error connecting to database. print error
        except mc.Error as e:
            self.label_result.setText("Error inserting data")

#call the database.py main() function and and open the welcome screen with fixed height and width 
database.main()
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


