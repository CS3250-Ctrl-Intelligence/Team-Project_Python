import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
import mysql.connector as mc
import csv

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui",self)
        self.pushButton_login.clicked.connect(self.goToLogin)

    def goToLogin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.pushButton_login.clicked.connect(self.loginFunc)

    def goToTable(self):
        table = TableScreen()
        widget.addWidget(table)
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
                self.goToTable()
        except mc.Error as e:
            self.label_result.setText("Error")

class TableScreen(QDialog):
    def __init__(self):
        super(TableScreen, self).__init__()
        loadUi("table.ui",self)
        self.pushButton_import.clicked.connect(self.importData)
        self.pushButton_fetch.clicked.connect(self.fetchData)
        self.pushButton_delete.clicked.connect(self.deleteData)
        

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
            
    def deleteData(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="project"
            )

            mycursor = mydb.cursor()

            mycursor.execute('DELETE FROM inventory WHERE Product_ID=?')

        except mc.Error as e:
            print("Error occured")

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


