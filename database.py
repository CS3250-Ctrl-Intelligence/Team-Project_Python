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

    mycursor.execute("CREATE TABLE IF NOT EXISTS inventory (Product_ID VARCHAR(45), Quantity INT, Wholesale_Price FLOAT, Sale_Price FLOAT, Supplier_ID VARCHAR(45))")

def createOrders():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS orders (Date DATE, Cust_Email VARCHAR(45), Cust_Location INT, Product_ID VARCHAR(45), Quantity INT)")

def createEmployees():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS employees (username VARCHAR(45), password VARCHAR(45))")

def createCustomers():
    
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS customers (cust_email VARCHAR(45), username VARCHAR(45), password VARCHAR(45))")

def main():
    createDB()
    createInventory()
    createOrders()
    createEmployees()
    createCustomers()

main()