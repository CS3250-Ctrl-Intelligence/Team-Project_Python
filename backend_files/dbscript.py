import mysql.connector as mc
import unittest
import csv
import pandas as pd
import os

class Initialize_database():

    def createDB():
        mydb = mc.connect(
            host="ctrlintel.net",
            user="ctrlinte_admin",
            password="CS3250!!",
            port=3306
        )
        cur = mydb.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS ctrlinte_ci_db")
        
        cur.close()
        mydb.close()

    def createTables():

        mydb = mc.connect(
            host="ctrlintel.net",
            user="ctrlinte_admin",
            password="CS3250!!",
            database="ctrlinte_ci_db",
            port='3306'
        )

        cur = mydb.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS product (Product_ID VARCHAR(45) PRIMARY KEY NOT NULL, Quantity INT, Wholesale_Cost FLOAT, Sale_Price FLOAT, Supplier_ID VARCHAR(45), slug VARCHAR(45), in_stock INT, featured BOOLEAN)")
        cur.execute("CREATE TABLE IF NOT EXISTS customer_orders (Date DATE , Cust_Email VARCHAR(45) , Cust_Location INT , Product_ID VARCHAR(45) , Quantity INT)")
        cur.execute("CREATE TABLE IF NOT EXISTS employees (username VARCHAR(45), password VARCHAR(45))")

        cur.close()
        mydb.close()
        
class Database_Functions():

    def connect():

        mydb = mc.connect(
            host="ctrlintel.net",
            user="ctrlinte_admin",
            password="CS3250!!",
            database="ctrlinte_ci_db",
            port='3306'
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
        cur.close()
    
    def fetchInventory():

        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        cur.execute("SELECT Product_Id, Quantity, Wholesale_Cost, Sale_Price, Supplier_Id FROM {} ".format("product"))
        result = cur.fetchall()
        cur.close()
        return result

    def searchInventory(product):

        identifier = product

        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query =("SELECT Product_Id, Quantity, Wholesale_Cost, Sale_Price, Supplier_Id FROM product WHERE Product_Id like %s".format("product"))
        values = (identifier)
        cur.execute(query, values)
        result = cur.fetchall()
        cur.close()
        return result


    def importInventory():
        def in_stock(x):
            if x >0:
                return 1
            else:
                return 0
                #connect to database
        try:
            mydb = Database_Functions.connect()

            cur = mydb.cursor()
            
            df = pd.read_csv(r'''backend_files\inventory_team1.csv''')
            
            df['slug'] = df['product_id'].str.lower().values
            df['in_stock'] = df['quantity'].apply(in_stock)
            df['featured'] = df['quantity'] - df['quantity']
            insert_inventory_data=list(zip(df['product_id'], df['quantity'], df['wholesale_cost'], df['sale_price'], df['supplier_id'], df['slug'], df['in_stock']))
            # update product quantity in inventory
            insert_inventory_query = """INSERT IGNORE INTO product (Product_Id, Quantity, Wholesale_Cost, Sale_Price, Supplier_Id, slug, in_stock,featured) VALUES (%s,%s,%s,%s,%s,%s,%s,0)"""
            cur.executemany(insert_inventory_query,insert_inventory_data)
            mydb.commit()

            print("Record updated successfully into Product table")

        except mc as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if mydb.is_connected():
                cur.close()
                mydb.close()
                print("MySQL connection is closed")

    def importOrders():
        try:
            mydb = Database_Functions.connect()

            cur = mydb.cursor()

            df = pd.read_csv(r'''backend_files\customer_orders_team1.csv''')
            customer_order_data= list(zip(df['date'],df['cust_email'],df['cust_location'],df['product_id'],df['product_quantity']))
            update_inventory_data=list(zip(df['product_quantity'],df['product_id'],df['product_quantity']))

            # insert customer order data to table
            insert_customer_orders_query = """INSERT IGNORE INTO customer_orders (Date, Cust_Email, Cust_Location,Product_Id,Quantity) VALUES (%s, %s, %s, %s, %s)"""
            cur.executemany(insert_customer_orders_query, customer_order_data)
            mydb.commit()

            # update product quantity in inventory
            update_inventory_query = """UPDATE product INNER JOIN customer_orders ON product.Product_Id = customer_orders.Product_Id SET product.Quantity = product.Quantity - %s WHERE product.Product_Id=%s AND product.Quantity > %s"""
            cur.executemany(update_inventory_query,update_inventory_data)
            mydb.commit()
            print("Record updated successfully into Customer Order table")

        except mc as error:
            print("Failed to insert into MySQL table {}".format(error))

        finally:
            if mydb.is_connected():
                cur.close()
                mydb.close()
                print("MySQL connection is closed")


    def fetchOrders():
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        cur.execute("SELECT Date, Cust_Email, Cust_Location,Product_Id,Quantity FROM {} ".format("customer_orders"))
        result = cur.fetchall()

        return result

    def searchOrders(customer):

        identifier = customer

        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query =("SELECT Date, Cust_Email, Cust_Location,Product_Id,Quantity FROM customer_orders WHERE Cust_Email like %s".format("customer_orders"))
        values = (identifier)
        cur.execute(query, values)
        result = cur.fetchall()
        cur.close()
        return result

    def addInventory(product, quantity, wholesale, sale, supplier):

        #connect to database
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "INSERT INTO product (Product_ID, Quantity, Wholesale_Cost, Sale_Price, Supplier_ID) VALUES (%s, %s, %s, %s, %s)"
        value = (product, quantity, wholesale, sale, supplier)
        cur.execute(query, value)
        #pushes the new data to the inventory table in the database.
        mydb.commit()

    def updateInventory(product, quantity, wholesale, sale, supplier):

        #connect to database
        mydb = Database_Functions.connect()

        identifier = product

        cur = mydb.cursor()
        query = "UPDATE product SET Product_ID = %s, Quantity = %s, Wholesale_Cost = %s, Sale_Price = %s, Supplier_ID = %s WHERE Product_ID = %s"
        value = (product, quantity, wholesale, sale, supplier, identifier)
        cur.execute(query, value)
        #pushes the new data to the inventory table in the database.
        mydb.commit()


    def deleteInventory(product):

        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = ("DELETE FROM product WHERE Product_ID = '" + product + "'")
        
        #execute query to delete data from database
        cur.execute(query)
        mydb.commit()

    def dailyProduct(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Product_ID,Quantity from customer_orders where date =" + "'" + str(searchDate) + "'" + "AND Quantity=(SELECT MAX(Quantity) FROM customer_orders where date=" + "'" + str(searchDate) + "'" + ");"
        cur.execute(query)
        dailyP = cur.fetchone()

        return dailyP

    def dailyCustomer(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Cust_Email,SUM(customer_orders.Quantity*product.Sale_Price) as Amount_Paid from customer_orders INNER JOIN product ON customer_orders.Product_ID = products.Product_ID WHERE date =" + "'" + str(searchDate) + "'" + "GROUP BY customer_orders.Cust_Email ORDER BY Amount_Paid DESC;"
        cur.execute(query)
        dailyC = cur.fetchone()
        x = [dailyC[0], float(dailyC[1])]
        x[1] = '%.2f' % x[1]
        return x


    def weeklyProduct(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Product_ID,Quantity from customer_orders where WEEKOFYEAR(date)=WEEKOFYEAR(" + "'" + str(searchDate) + "'" + ") AND Quantity=(SELECT MAX(Quantity) FROM customer_orders where WEEKOFYEAR(date)=WEEKOFYEAR(" + "'" + str(searchDate) + "'" + "));"
        cur.execute(query)
        weeklyP = cur.fetchone()

        return weeklyP

    def weeklyCustomer(date):
        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Cust_Email,SUM(customer_orders.Quantity*product.Sale_Price) as Amount_Paid from customer_orders INNER JOIN product ON customer_orders.Product_ID = product.Product_ID WHERE WEEKOFYEAR(date)=WEEKOFYEAR(" + "'" + str(searchDate) + "'" + ") GROUP BY customer_orders.Cust_Email ORDER BY Amount_Paid DESC;"
        cur.execute(query)
        weeklyC = cur.fetchone()
        x = [weeklyC[0], float(weeklyC[1])]
        x[1] = '%.2f' % x[1]
        return x

    def monthlyProduct(date):

        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Product_ID,Quantity from customer_orders where MONTH(date)=MONTH(" + "'" + str(searchDate) + "'" + ") AND Quantity=(SELECT MAX(Quantity) FROM customer_orders where MONTH(date)=MONTH(" + "'" + str(searchDate) + "'" + "));"
        cur.execute(query)
        monthlyP = cur.fetchone()

        return monthlyP

    def monthlyCustomer(date):
        searchDate = date
        mydb = Database_Functions.connect()

        cur = mydb.cursor()
        query = "SELECT Cust_Email,SUM(customer_orders.Quantity*product.Sale_Price) as Amount_Paid from customer_orders INNER JOIN product ON customer_orders.Product_ID = product.Product_ID WHERE MONTH(date)=MONTH(" + "'" + str(searchDate) + "'" + ") GROUP BY customer_orders.Cust_Email ORDER BY Amount_Paid DESC;"
        cur.execute(query)
        monthlyC = cur.fetchone()
        x = [monthlyC[0], float(monthlyC[1])]
        x[1] = '%.2f' % x[1]
        return x

    def getThreeRev():

        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        query = "SELECT WEEKOFYEAR(Date),SUM(customer_orders.Quantity*product.Sale_Price) as Amount_Paid from customer_orders INNER JOIN product ON customer_orders.Product_ID = product.Product_ID WHERE Date >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH) AND Date <= CURDATE() Group by WEEKOFYEAR(Date)"
        cur.execute(query)


        weeklyRev = cur.fetchall()

        date = []
        amount = []
        for x in range(len(weeklyRev)):
            week = [int(weeklyRev[x][0]),float(weeklyRev[x][1])]
            week[1] = '%.2f' % week[1]
            amount += [float(week[1])]
            date += [week[0]]
        return date, amount

    def getAllRev():

        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        query = "SELECT YEARWEEK(Date),SUM(customer_orders.Quantity*product.Sale_Price) as Amount_Paid from customer_orders INNER JOIN product ON customer_orders.Product_ID = product.Product_ID Group by WEEKOFYEAR(Date)"
        cur.execute(query)


        weeklyRev = cur.fetchall()

        amount = []
        for x in range(len(weeklyRev)):
            week = [int(weeklyRev[x][0]),float(weeklyRev[x][1])]
            week[1] = '%.2f' % week[1]
            amount += [float(week[1])]
        return amount

    def getDiffRev():

        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        query = "SELECT YEARWEEK(Date),SUM(customer_orders.Quantity*product.Sale_Price) as Amount_Paid from customer_orders INNER JOIN product ON customer_orders.Product_ID = product.Product_ID WHERE Date >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH) AND Date <= CURDATE() Group by WEEKOFYEAR(Date)"
        cur.execute(query)


        weeklyRev = cur.fetchall()

        date = []
        data = []
        for x in range(len(weeklyRev)):
            week = [int(weeklyRev[x][0]),float(weeklyRev[x][1])]
            week[1] = '%.2f' % week[1]
            data += [float(week[1])]
            date += [week[0]]
        date.pop(0)
        x = 0
        result = []
        while x < (len(data) - 1):
            diff = data[x + 1] - data[x]
            result += [[date[x],float('%.2f' % diff)]]
            x += 1
        return result

    def getThreeOrders():

        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        query = "SELECT WEEKOFYEAR(Date),Count(*) as Number_Orders from customer_orders  WHERE Date >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH) AND Date <= CURDATE() Group by WEEKOFYEAR(Date)"
        cur.execute(query)


        weeklyOrders = cur.fetchall()

        date = []
        amount = []
        for x in range(len(weeklyOrders)):
            week = [int(weeklyOrders[x][0]),float(weeklyOrders[x][1])]
            week[1] = '%.2f' % week[1]
            amount += [float(week[1])]
            date += [week[0]]
        return date, amount

    def getAllOrders():

        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        query = "SELECT YEARWEEK(Date),COUNT(*) as Amount_Paid from customer_orders Group by WEEKOFYEAR(Date)"
        cur.execute(query)


        weeklyOrders = cur.fetchall()

        amount = []
        for x in range(len(weeklyOrders)):
            week = [int(weeklyOrders[x][0]),float(weeklyOrders[x][1])]
            week[1] = '%.2f' % week[1]
            amount += [float(week[1])]
        return amount

    def getDiffOrders():
        mydb = Database_Functions.connect()
        cur = mydb.cursor()
        query = "SELECT YEARWEEK(Date),Count(*) as Number_Orders from customer_orders WHERE Date >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH) AND Date <= CURDATE() Group by WEEKOFYEAR(Date)"
        cur.execute(query)


        weeklyOrders = cur.fetchall()

        date = []
        data = []
        for x in range(len(weeklyOrders)):
            week = [int(weeklyOrders[x][0]),float(weeklyOrders[x][1])]
            week[1] = '%.2f' % week[1]
            data += [float(week[1])]
            date += [week[0]]
        date.pop(0)
        x = 0
        result = []
        while x < (len(data) - 1):
            diff = data[x + 1] - data[x]
            result += [[date[x],float('%.2f' % diff)]]
            x += 1
        return result

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


