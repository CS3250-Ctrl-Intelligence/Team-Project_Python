import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from dbscript import Database_Functions
import dbscript
import time

class Buttons(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r'''backend_files\home.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

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
    
    def goToMarket(self):
        market = MarketScreen()
        widget.addWidget(market)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToFinance(self):
        finance = FinanceScreen()
        widget.addWidget(finance)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToSettings(self):
        settings = SettingsScreen()
        widget.addWidget(settings)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHelp(self):
        help = HelpScreen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToInfo(self):
        info = InfoScreen()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex()+1)


#This class displays the welcome screen
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(r'''backend_files\welcome.ui''',self)
        
        #Implementation of the buttons on the page.
        self.loginBtn.clicked.connect(self.goToLogin)
        #self.pushButton_newAcc.clicked.connect(self.goToCreate)

    #function to bring you to login page
    def goToLogin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

#This class displays the employee login screen
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi(r'''backend_files\login.ui''',self)

        #Implementation of the buttons on the page.
        self.goBtn.clicked.connect(self.loginFunc)
        self.createBtn.clicked.connect(self.employeeCreate)

    #function to bring you to the dashboard if you successfully log in
    def goToHome(self):
        dashboard = HomeScreen()
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
            self.goToHome()

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
        self.createBtn.clicked.connect(self.signup)
        
    #function to create a record in the table employees
    def signup(self):
        #get user input from text fields
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        confPassword = self.lineEdit_confpassword.text()

        #test to if all fields have an input and the password and confirm password match each other.
        if username=="" or password=="" or confPassword=="":
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
            login = LoginScreen()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

class HomeScreen(Buttons):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi(r'''backend_files\home.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)


#This class displays the inventory screen
class InvScreen(Buttons):
    def __init__(self):
        super(InvScreen, self).__init__()
        loadUi(r'''backend_files\inventory.ui''',self)

        #Implementation of the buttons on the page.
        self.importBtn.clicked.connect(self.importData)
        self.fetchBtn.clicked.connect(self.fetchData)
        self.deleteBtn.clicked.connect(self.goToDelete)
        self.updateBtn.clicked.connect(self.goToUpdate)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

        self.fetchData()

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

#This class displays the customer orders screen.
class OrdersScreen(Buttons):
    def __init__(self):
        super(OrdersScreen, self).__init__()
        loadUi(r'''backend_files\orders.ui''',self)

        #Implementation of the buttons on the page.
        self.fetchBtn.clicked.connect(self.fetchData)
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

        self.fetchData()

    def fetchData(self):
        result = dbscript.Database_Functions.fetchOrders()

        #starts row count at 0 and inserts all the data for each row
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


            
class MarketScreen(Buttons):
    def __init__(self):
        super(MarketScreen, self).__init__()
        loadUi(r'''backend_files\market.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)
        self.dailyBtn.clicked.connect(self.dailyReport)
        self.weeklyBtn.clicked.connect(self.weeklyReport)
        self.monthlyBtn.clicked.connect(self.monthlyReport)

    def dailyReport(self):

        date = self.lineDate.text()
        dailyP = Database_Functions.dailyProduct(date)
        self.lineLabelP.setText("The most purchased daily product is:")
        self.lineProduct.setText(str(dailyP[0]) + " with " + str(dailyP[1]) + " sold")

        #customer = Database_Functions.dailyCustomer(date)
        dailyC = Database_Functions.dailyCustomer(date)
        self.lineLabelC.setText("Daily customer that purchased the most:")
        self.lineCustomer.setText(str(dailyC[0]) + " with $" + str(dailyC[1]))

    def weeklyReport(self):

        date = self.lineDate.text()
        weeklyP = Database_Functions.weeklyProduct(date)
        self.lineLabelP.setText("The most purchased weekly product is:")
        self.lineProduct.setText(str(weeklyP[0]) + " with " + '%.2f' % weeklyP[1] + " sold")

        #customer = Database_Functions.dailyCustomer(date)
        weeklyC = Database_Functions.weeklyCustomer(date)
        self.lineLabelC.setText("Weekly customer that purchased the most:")
        self.lineCustomer.setText(str(weeklyC[0]) + " with $" + str(weeklyC[1]))

    def monthlyReport(self):

        date = self.lineDate.text()
        monthlyP = Database_Functions.monthlyProduct(date)
        self.lineProduct.setText(str(monthlyP[0]) + " with " + str(monthlyP[1]) + " sold")

        #customer = Database_Functions.dailyCustomer(date)
        monthlyC = Database_Functions.monthlyCustomer(date)
        self.lineLabelC.setText("Monthly customer that purchased the most:")
        self.lineCustomer.setText(str(monthlyC[0]) + " with $" + str(monthlyC[1]))
        
class FinanceScreen(Buttons):
    def __init__(self):
        super(FinanceScreen, self).__init__()
        loadUi(r'''backend_files\finance.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.OrdersBtn.clicked.connect(self.goToOrders)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

class SettingsScreen(Buttons):
    def __init__(self):
        super(SettingsScreen, self).__init__()
        loadUi(r'''backend_files\settings.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

class HelpScreen(Buttons):
    def __init__(self):
        super(HelpScreen, self).__init__()
        loadUi(r'''backend_files\help.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.infoBtn.clicked.connect(self.goToInfo)

class InfoScreen(Buttons):
    def __init__(self):
        super(InfoScreen, self).__init__()
        loadUi(r'''backend_files\info.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.ordersBtn.clicked.connect(self.goToOrders)



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
widget.setFixedHeight(561)
widget.setFixedWidth(891)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")