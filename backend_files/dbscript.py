import mysql.connector as mc
import unittest
import csv

class Initialize_database():

    def createDB():
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            port=3306
        )
        cur = mydb.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS ci_db")
        
        cur.close()
        mydb.close()

    def createTables():

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="ci_db",
            port=3306
        )

        cur = mydb.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS inventory (Product_ID VARCHAR(45), Quantity INT, Wholesale_Price FLOAT, Sale_Price FLOAT, Supplier_ID VARCHAR(45))")
        cur.execute("CREATE TABLE IF NOT EXISTS orders (Date DATE, Cust_Email VARCHAR(45), Cust_Location INT, Product_ID VARCHAR(45), Quantity INT)")
        cur.execute("CREATE TABLE IF NOT EXISTS employees (username VARCHAR(45), password VARCHAR(45))")
        cur.execute("CREATE TABLE IF NOT EXISTS customers (cust_email VARCHAR(45), username VARCHAR(45), password VARCHAR(45))")

        cur.close()
        mydb.close()
        
class Database_Functions():

    def connect():

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="ci_db",
            port=3306
        )

        return mydb

    def login(username, password):

        mydb = Database_Functions.connect()

        #find the username and password in the database table employees
        cur = mydb.cursor()
        query = "SELECT username,password from employees where username like '" + username + "'and password like '" + password +  "'"
        cur.execute(query)
        result = cur.fetchone()

        return result

    def createEmployee(username, password):

        mydb = Database_Functions.connect()
        #create record of employee in database table employees
        cur = mydb.cursor()
        query = 'INSERT INTO employees(username, password)' 'VALUES(%s, %s)'
        value = (username, password)
        cur.execute(query, value)
        mydb.commit()
    
    def fetchInventory():

        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        cur.execute("SELECT * FROM {} ".format("inventory"))
        result = cur.fetchall()

        return result
    
    def importInventory():

                #connect to database
        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        #open the .csv file and read it into variable.
        file = open(r'''backend_files\inventory_team1.csv''')
        csv_data = csv.reader(file)

        skipHeader = True

        #import the data from csv variable into the database table "inventory"
        for row in csv_data:
            if skipHeader:
                skipHeader = False 
                continue
            cur.execute('INSERT IGNORE INTO inventory(Product_ID, Quantity, Wholesale_Price, Sale_Price, Supplier_ID)' 'VALUES(%s, %s, %s, %s, %s)', row)
        mydb.commit()

    def importOrders():
        mydb = Database_Functions.connect()

        cur = mydb.cursor()

        #open the .csv file and read it into variable.
        file = open(r'''backend_files\customer_orders_team1.csv''')
        csv_data = csv.reader(file)

        skipHeader = True

        #import the data from csv variable into the database table "inventory"
        for row in csv_data:
            if skipHeader:
                skipHeader = False
                continue
            cur.execute('INSERT IGNORE INTO orders(Date, Cust_Email, Cust_Location, Product_ID, Quantity)' 'VALUES(%s, %s, %s, %s, %s)', row)
        mydb.commit()

    def fetchOrders():
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        cur.execute("SELECT * FROM {} ".format("orders"))
        result = cur.fetchall()

        return result

    def addInventory(product, quantity, wholesale, sale, supplier):

        #connect to database
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "INSERT INTO inventory (Product_ID, Quantity, Wholesale_Price, Sale_Price, Supplier_ID) VALUES (%s, %s, %s, %s, %s)"
        value = (product, quantity, wholesale, sale, supplier)
        cur.execute(query, value)
        #pushes the new data to the inventory table in the database.
        mydb.commit()

    def deleteInventory(product):

        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = ("DELETE FROM inventory WHERE Product_ID = '" + product + "'")
        
        #execute query to delete data from database
        cur.execute(query)
        mydb.commit()

    def dailyProduct(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Product_ID,Quantity from orders where date =" + "'" + str(searchDate) + "'" + "AND Quantity=(SELECT MAX(Quantity) FROM orders where date=" + "'" + str(searchDate) + "'" + ");"
        cur.execute(query)
        dailyP = cur.fetchone()

        return dailyP

    def dailyCustomer(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Cust_Email,SUM(orders.Quantity*inventory.Sale_Price) as Amount_Paid from orders INNER JOIN inventory ON orders.Product_ID = inventory.Product_ID WHERE date =" + "'" + str(searchDate) + "'" + "GROUP BY orders.Cust_Email ORDER BY Amount_Paid DESC;"
        cur.execute(query)
        dailyC = cur.fetchone()
        x = [dailyC[0], float(dailyC[1])]
        x[1] = '%.2f' % x[1]
        return x


    def weeklyProduct(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Product_ID,Quantity from orders where WEEKOFYEAR(date)=WEEKOFYEAR(" + "'" + str(searchDate) + "'" + ") AND Quantity=(SELECT MAX(Quantity) FROM orders where WEEKOFYEAR(date)=WEEKOFYEAR(" + "'" + str(searchDate) + "'" + "));"
        cur.execute(query)
        weeklyP = cur.fetchone()

        return weeklyP

    def weeklyCustomer(date):
        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Cust_Email,SUM(orders.Quantity*inventory.Sale_Price) as Amount_Paid from orders INNER JOIN inventory ON orders.Product_ID = inventory.Product_ID WHERE WEEKOFYEAR(date)=WEEKOFYEAR(" + "'" + str(searchDate) + "'" + ") GROUP BY orders.Cust_Email ORDER BY Amount_Paid DESC;"
        cur.execute(query)
        weeklyC = cur.fetchone()
        x = [weeklyC[0], float(weeklyC[1])]
        x[1] = '%.2f' % x[1]
        return x

    def monthlyProduct(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Product_ID,Quantity from orders where MONTH(date)=MONTH(" + "'" + str(searchDate) + "'" + ") AND Quantity=(SELECT MAX(Quantity) FROM orders where MONTH(date)=MONTH(" + "'" + str(searchDate) + "'" + "));"
        cur.execute(query)
        monthlyP = cur.fetchone()

        return monthlyP

    def monthlyCustomer(date):
        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Cust_Email,SUM(orders.Quantity*inventory.Sale_Price) as Amount_Paid from orders INNER JOIN inventory ON orders.Product_ID = inventory.Product_ID WHERE MONTH(date)=MONTH(" + "'" + str(searchDate) + "'" + ") GROUP BY orders.Cust_Email ORDER BY Amount_Paid DESC;"
        cur.execute(query)
        monthlyC = cur.fetchone()
        x = [monthlyC[0], float(monthlyC[1])]
        x[1] = '%.2f' % x[1]
        return x

class TestDatabase(unittest.TestCase):

    def test_write(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password=""
        )
        test_cursor = mydb.cursor()

        test_cursor.execute("CREATE DATABASE IF NOT EXISTS unittest")

        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="unittest"
        )
        test_cursor = mydb.cursor()

        test_cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT, text VARCHAR(45))")

        test_cursor.execute("INSERT INTO `test_table` (id, `text`) VALUES (3, 'test_text_3')")

        test_cursor.execute("SELECT text FROM test_table ORDER BY id DESC LIMIT 1")

        test = test_cursor.fetchall()

        self.assertEqual(test, [('test_text_3',)])

    def test_delete(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="unittest"
        )
        test_cursor = mydb.cursor()

        test_cursor.execute("""DELETE FROM `test_table` WHERE id= 3 """)

        test_cursor.execute("""SELECT text FROM test_table ORDER BY id DESC LIMIT 1""")

        test = test_cursor.fetchall()

        self.assertEqual(test, [])


Initialize_database.createDB()
Initialize_database.createTables()
Database_Functions.importOrders()

