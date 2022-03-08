import mysql.connector as mc
import unittest

#function to create the database if it does not exist
def createDB():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password=""
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS project")

#function to create the table inventory in the project database if it does not exist.
def createInventory():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS inventory (Product_ID VARCHAR(45), Quantity INT, Wholesale_Price FLOAT, Sale_Price FLOAT, Supplier_ID VARCHAR(45))")

#function to create the table orders in the project database if it does not exist.
def createOrders():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS orders (Date DATE, Cust_Email VARCHAR(45), Cust_Location INT, Product_ID VARCHAR(45), Quantity INT)")

#function to create the table employees in the project database if it does not exist.
def createEmployees():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS employees (username VARCHAR(45), password VARCHAR(45))")

#function to create the table customers in the project database if it does not exist.
def createCustomers():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (cust_email VARCHAR(45), username VARCHAR(45), password VARCHAR(45))")

#main function to call all previous functions into main.py
def main():
    createDB()
    createInventory()
    createOrders()
    createEmployees()
    createCustomers()

main()


class TestDatabase(unittest.TestCase):

    def test_write(self):
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
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
