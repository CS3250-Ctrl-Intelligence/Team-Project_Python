import mysql.connector as mc

def createDB():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password=""
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS project")

def createInventory():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE inventory (Product_ID VARCHAR(45), Quantity INT, Wholesale_Price FLOAT, Sale_Price FLOAT, Supplier_ID VARCHAR(45))")

def createOrders():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE orders (Date , Cust_Email VARCHAR(45), Cust_Location INT, Product_ID VARCHAR(45), Quantity INT)")


def checkDB():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES LIKE 'project'")

    if mycursor == None:
        createDB()

def checkInventory():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES LIKE 'inventory'")

    if mycursor == None:
        createInventory()

def checkOrders():

    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES LIKE 'orders'")

    if mycursor == None:
        createOrders()

def main():
    checkDB()
    checkInventory()
    checkOrders()

main()