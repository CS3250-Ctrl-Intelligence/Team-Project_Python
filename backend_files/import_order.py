import pandas as pd
import mysql.connector



try:

    connection = mysql.connector.connect(host='localhost',
                                            database='ci_db6',
                                            user='root',
                                            password='')
    cursor = connection.cursor()
    
    df = pd.read_csv('customer_orders_team1.csv')
    customer_order_data= list(zip(df['date'],df['cust_email'],df['cust_location'],df['product_id'],df['product_quantity']))
    update_inventory_data=list(zip(df['product_quantity'],df['product_id'],df['product_quantity']))

    
    # update product quantity in inventory
    update_inventory_query = """UPDATE product INNER JOIN customer_orders ON product.product_id = customer_orders.product_id SET product.quantity = product.quantity - %s WHERE product.product_id=%s AND product.quantity > %s"""
    cursor.executemany(update_inventory_query,update_inventory_data)
    connection.commit()

    # insert customer order data to table
    insert_customer_orders_query = """INSERT INTO customer_orders (date, cust_email, cust_location,product_id,quantity) VALUES (%s, %s, %s, %s, %s)"""
    cursor.executemany(insert_customer_orders_query, customer_order_data)
    connection.commit()
    print("Record updated successfully into Customer Order table")

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




# Insert whole DataFrame into MySQL
# df.to_sql('product', con = engine, if_exists = 'append', chunksize = 1000,index=False)