import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from dbscript import Database_Functions
import dbscript
import time
import allRev, threeRev, diffRev, allOrders, threeOrders, diffOrders

class Buttons(QDialog):
    def __init__(self):
        super().__init__()
        loadUi(r'''backend_files\ui_files\home.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

    def goToInv(self):
        '''function to go to the inventory screen.'''
        inventory = InvScreen()
        widget.addWidget(inventory)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToOrders(self):
        '''function to go to the customer orders screen.'''
        orders = OrdersScreen()
        widget.addWidget(orders)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def goToMarket(self):
        '''function to go to Market screen.'''
        market = MarketScreen()
        widget.addWidget(market)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToFinance(self):
        '''function to go to Finance screen.'''
        finance = FinanceScreen()
        widget.addWidget(finance)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToSettings(self):
        '''function to go to Settings screen.'''
        settings = SettingsScreen()
        widget.addWidget(settings)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToHelp(self):
        '''function to go to Help screen.'''
        help = HelpScreen()
        widget.addWidget(help)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToInfo(self):
        '''function to go to Info screen.'''
        info = InfoScreen()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex()+1)


class WelcomeScreen(QDialog):
    '''This class displays the welcome screen.'''
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\welcome.ui''',self)
        
        #Implementation of the buttons on the page.
        self.loginBtn.clicked.connect(self.goToLogin)
        #self.pushButton_newAcc.clicked.connect(self.goToCreate)

    def goToLogin(self):
        '''function to bring you to login page.'''
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginScreen(QDialog):
    '''This class displays the employee login screen.'''
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\login.ui''',self)

        #Implementation of the buttons on the page.
        self.goBtn.clicked.connect(self.loginFunc)
        self.createBtn.clicked.connect(self.employeeCreate)

    def goToHome(self):
        '''Function to bring you to the dashboard if you successfully log in.'''
        dashboard = HomeScreen()
        widget.addWidget(dashboard)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginFunc(self):
        '''Function to login'''

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


class CreateEmpScreen(QDialog):
    '''This class displays the create employee screen.'''
    def __init__(self):
        super(CreateEmpScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\createEmployee.ui''',self)

        #Implementation of the buttons on the page.
        self.createBtn.clicked.connect(self.signup)

    def signup(self):
        '''function to create a record in the table employees'''
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
    '''This class implements the buttons on the HomeScreen'''
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\home.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)



class InvScreen(Buttons):
    '''This class displays the inventory screen'''
    def __init__(self):
        super(InvScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\inventory.ui''',self)

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
        '''Fetches data to display.'''
        result = dbscript.Database_Functions.fetchInventory()

        #starts row count at 0 and inserts all the data for each row
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def importData(self):
        '''Calls import function from dbscript to import data to inventory.'''
        
        dbscript.Database_Functions.importInventory()

    def goToDelete(self):
        '''Function to open delete product screen'''
        delete = DeleteScreen()
        delete.setFixedHeight(200)
        delete.setFixedWidth(500)
        delete.exec()

    def goToUpdate(self):
        '''Function to open the update product screen'''
        update = AddScreen()
        update.setFixedHeight(350)
        update.setFixedWidth(500)
        update.exec()

class OrdersScreen(Buttons):
    '''This class displays the customer orders screen.'''
    def __init__(self):
        super(OrdersScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\orders.ui''',self)

        #Implementation of the buttons on the page.
        self.fetchBtn.clicked.connect(self.fetchData)
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)
        self.importBtn.clicked.connect(self.importOrders)

        self.fetchData()
    def importOrders(self):
        '''Imports orders from csv to MySQL'''
        Database_Functions.importOrders()
        
    def fetchData(self):
        '''Fetches data from Orders to display'''
        result = dbscript.Database_Functions.fetchOrders()

        #starts row count at 0 and inserts all the data for each row
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


            
class MarketScreen(Buttons):
    '''This class displays the marketing screen.'''
    def __init__(self):
        super(MarketScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\market.ui''',self)

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
        '''Creates and displays daily marketing report.'''

        date = self.lineDate.text()
        dailyP = Database_Functions.dailyProduct(date)
        self.lineLabelP.setText("The most purchased daily product is:")
        self.lineProduct.setText(str(dailyP[0]) + " with " + str(dailyP[1]) + " sold")

        #customer = Database_Functions.dailyCustomer(date)
        dailyC = Database_Functions.dailyCustomer(date)
        self.lineLabelC.setText("Daily customer that purchased the most:")
        self.lineCustomer.setText(str(dailyC[0]) + " with $" + str(dailyC[1]))

    def weeklyReport(self):
        '''Creates and displays weekly marketing report.'''

        date = self.lineDate.text()
        weeklyP = Database_Functions.weeklyProduct(date)
        self.lineLabelP.setText("The most purchased weekly product is:")
        self.lineProduct.setText(str(weeklyP[0]) + " with " + '%.2f' % weeklyP[1] + " sold")

        #customer = Database_Functions.dailyCustomer(date)
        weeklyC = Database_Functions.weeklyCustomer(date)
        self.lineLabelC.setText("Weekly customer that purchased the most:")
        self.lineCustomer.setText(str(weeklyC[0]) + " with $" + str(weeklyC[1]))

    def monthlyReport(self):
        '''Creates and displays monthly marketing report.'''
        date = self.lineDate.text()
        monthlyP = Database_Functions.monthlyProduct(date)
        self.lineProduct.setText(str(monthlyP[0]) + " with " + str(monthlyP[1]) + " sold")

        #customer = Database_Functions.dailyCustomer(date)
        monthlyC = Database_Functions.monthlyCustomer(date)
        self.lineLabelC.setText("Monthly customer that purchased the most:")
        self.lineCustomer.setText(str(monthlyC[0]) + " with $" + str(monthlyC[1]))

    
        
class FinanceScreen(Buttons):
    '''This class implements the buttons on the finance screen.'''
    def __init__(self):
        super(FinanceScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\finance.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)
        self.revAllBtn.clicked.connect(self.allRev)
        self.revMonthBtn.clicked.connect(self.monthRev)
        self.revDiffBtn.clicked.connect(self.diffRev)
        self.custAllBtn.clicked.connect(self.allOrder)
        self.custMonthBtn.clicked.connect(self.monthOrder)
        self.custDiffBtn.clicked.connect(self.diffOrder)

    def allRev(self):
        allRev.main()
    def monthRev(self):
        threeRev.main()
    def diffRev(self):
        diffRev.main()
    def allOrder(self):
        allOrders.main()
    def monthOrder(self):
        threeOrders.main()
    def diffOrder(self):
        diffOrders.main()

class SettingsScreen(Buttons):
    '''This class implements the buttons for the Settings screen.'''
    def __init__(self):
        super(SettingsScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\settings.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.infoBtn.clicked.connect(self.goToInfo)

class HelpScreen(Buttons):
    '''This class implements the buttons for the Help screen.'''
    def __init__(self):
        super(HelpScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\help.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.ordersBtn.clicked.connect(self.goToOrders)
        self.infoBtn.clicked.connect(self.goToInfo)

class InfoScreen(Buttons):
    '''This class implements the buttons for the Info screen.'''
    def __init__(self):
        super(InfoScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\info.ui''',self)

        #Implementation of the buttons on the page.
        self.invBtn.clicked.connect(self.goToInv)
        self.marketBtn.clicked.connect(self.goToMarket)
        self.financeBtn.clicked.connect(self.goToFinance)
        self.settingsBtn.clicked.connect(self.goToSettings)
        self.helpBtn.clicked.connect(self.goToHelp)
        self.ordersBtn.clicked.connect(self.goToOrders)



class DeleteScreen(QDialog):
    '''This class displays the delete product screen'''
    def __init__(self):
        super(DeleteScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\deleteData.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_commit.clicked.connect(self.deleteData)

    def deleteData(self):
        '''function to delete data from the database'''

        product = self.lineEdit_product.text()

        dbscript.Database_Functions.deleteInventory(product)


#This class displays the update the 
class AddScreen(QDialog):
    def __init__(self):
        super(AddScreen, self).__init__()
        loadUi(r'''backend_files\ui_files\addData.ui''',self)

        #Implementation of the buttons on the page.
        self.pushButton_commit.clicked.connect(self.addData)

    def addData(self):
        '''function to add new data record to the database table inventory'''

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