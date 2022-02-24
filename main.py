import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
import mysql.connector as mc
import csv
import database

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui",self)
        self.pushButton_login.clicked.connect(self.goToLogin)
        self.pushButton_newAcc.clicked.connect(self.goToCreate)

    def goToLogin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToCreate(self):
        createAcc = CreateAccScreen()
        widget.addWidget(createAcc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.pushButton_login.clicked.connect(self.loginFunc)

    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def loginFunc(self):
        try:
            username = self.lineEdit_username.text()
            password = self.lineEdit_password.text()
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()
            query = "SELECT username,password from users where username like '" + username + "'and password like '" + password +  "'"
            mycursor.execute(query)

            result = mycursor.fetchone()

            if result ==None:
                self.label_result.setText("Incorrect email or password")

            else:
                self.goToDashboard()
        except mc.Error as e:
            self.label_result.setText("Error")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        self.pushButton_signup.clicked.connect(self.signup)

    def signup(self):

        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confPassword = self.lineEdit_confpassword.text()
        if len(username)==0 or len(password)==0 or len(confPassword)==0:
            self.label_result.setText("Please fill in all fields.")

        elif password != confPassword:
            self.label_result.setText("Passwords do not match")

        else:
            try:
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="project"
            )

                mycursor = mydb.cursor()
                query = 'INSERT INTO users(username, password)' 'VALUES(%s, %s)'
                value = (username, password)

                mycursor.execute(query, value)

                mydb.commit()
                self.label_result.setText("User added to database")

        
            except mc.Error as e:
                self.label_result.setText("Error inserting data")

            dashboard = DashboardScreen()
            widget.addWidget(dashboard)
            widget.setCurrentIndex(widget.currentIndex()+1)

class DashboardScreen(QDialog):
    def __init__(self):
        super(DashboardScreen, self).__init__()
        loadUi("dashboard.ui",self)
        self.pushButton_inv.clicked.connect(self.goToInv)
        self.pushButton_custOrders.clicked.connect(self.goToOrders)

    def goToInv(self):
        inventory = InvScreen()
        widget.addWidget(inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToOrders(self):
        orders = OrdersScreen()
        widget.addWidget(orders)
        widget.setCurrentIndex(widget.currentIndex()+1)


class InvScreen(QDialog):
    def __init__(self):
        super(InvScreen, self).__init__()
        loadUi("inventory.ui",self)
        self.pushButton_import.clicked.connect(self.importData)
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_delete.clicked.connect(self.goToDelete)
        self.pushButton_update.clicked.connect(self.goToUpdate)
        self.pushButton_back.clicked.connect(self.goToDashboard)

    def fetchData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM {} ".format("inventory"))

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error occured")
    
    def importData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
        )

            mycursor = mydb.cursor()
            file = open("inventory_team1.csv")
            csv_data = csv.reader(file)

            skipHeader = True

            for row in csv_data:
                if skipHeader:
                    skipHeader = False
                    continue
                mycursor.execute('INSERT INTO inventory(Product_ID, Quantity, Wholesale_Price, Sale_Price, Supplier_ID)' 'VALUES(%s, %s, %s, %s, %s)', row)

        except mc.Error as e:
            print("Error occured")
            
    def goToDelete(self):
        delete = DeleteScreen()
        delete.setFixedHeight(200)
        delete.setFixedWidth(500)
        delete.exec()

    def goToUpdate(self):
        update = AddScreen()
        update.setFixedHeight(350)
        update.setFixedWidth(500)
        update.exec()

    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

class OrdersScreen(QDialog):
    def __init__(self):
        super(OrdersScreen, self).__init__()
        loadUi("orders.ui",self)
        self.pushButton_import.clicked.connect(self.importData)
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_back.clicked.connect(self.goToDashboard)

    def fetchData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM {} ".format("orders"))

            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error occured")
    
    def importData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
        )

            mycursor = mydb.cursor()
            file = open("customer_orders_team1.csv")
            csv_data = csv.reader(file)

            skipHeader = True

            for row in csv_data:
                if skipHeader:
                    skipHeader = False
                    continue
                mycursor.execute('INSERT INTO orders(Date, Cust_Email, Cust_Location, Product_ID, Quantity)' 'VALUES(%s, %s, %s, %s, %s)', row)

        except mc.Error as e:
            print("Error occured")

    def goToDashboard(self):
        dashboard = DashboardScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)
            

class DeleteScreen(QDialog):
    def __init__(self):
        super(DeleteScreen, self).__init__()
        loadUi("deleteData.ui",self)
        self.pushButton_commit.clicked.connect(self.deleteData)

    def deleteData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()
            product = self.lineEdit_product.text()

            query = ('DELETE FROM inventory WHERE Product_ID = VALUES (%s)')
            value = (product)
            
            mycursor.execute(query, value)
            mydb.commit()
            self.label_result.setText("Data has been deleted from the database")

        except mc.Error as e:
            print("Error occured")

class AddScreen(QDialog):
    def __init__(self):
        super(AddScreen, self).__init__()
        loadUi("addData.ui",self)
        self.pushButton_commit.clicked.connect(self.addData)

    def addData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()

        

            product = self.lineEdit_product.text()
            quantity = self.lineEdit_quantity.text()
            wholesale = self.lineEdit_wholesale.text()
            sale = self.lineEdit_sale.text()
            supplier = self.lineEdit_supplier.text()

            query = "INSERT INTO inventory (Product_ID, Quantity, Wholesale_Price, Sale_Price, Supplier_ID) VALUES (%s, %s, %s, %s, %s)"
            value = (product, quantity, wholesale, sale, supplier)

            mycursor.execute(query, value)

            mydb.commit()
            self.label_result.setText("Data added to database")


        except mc.Error as e:
            self.label_result.setText("Error inserting data")


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


