import pandas as pd
import mysql.connector

def in_stock(x):
    if x >0:
        return 1
    else:
        return 0

try:

    connection = mysql.connector.connect(host='localhost',
                                            database='ci_db6',
                                            user='root',
                                            password='')
    cursor = connection.cursor()
    
    df = pd.read_csv('inventory_team1.csv')
    
    df['slug'] = df['product_id'].str.lower().values
    df['in_stock'] = df['quantity'].apply(in_stock)
    df['featured'] = df['quantity'] - df['quantity']
    insert_inventory_data=list(zip(df['product_id'], df['quantity'], df['wholesale_cost'], df['sale_price'], df['supplier_id'], df['slug'], df['in_stock']))
    # update product quantity in inventory
    insert_inventory_query = """INSERT INTO product (product_id, quantity, wholesale_cost, sale_price, supplier_id, slug, in_stock,featured) VALUES (%s,%s,%s,%s,%s,%s,%s,0)"""
    cursor.executemany(insert_inventory_query,insert_inventory_data)
    connection.commit()

    print("Record updated successfully into Product table")

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



