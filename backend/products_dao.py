# import mysql.connector

# from mysql.connector import errorcode
# import MySQLdb


# def get_all_products_table():
   
    



#     cnx = MySQLdb.connect(user='root', password='root',
#                               host='127.0.0.1',
#                               database='grocery_store')
  
#     cursor = cnx.cursor()
#     query = ("select products_table.product_id, products_table.product_name, products_table.uom, products_table.price_per_unit, um_table.um_name from products_table inner join um_table on products_table.uom=um_table.um_id")
#     cursor.execute(query)
#     response = []
#     for (product_id, name, um_id, price_per_unit, um_name) in cursor:
#         response.append({
#             'product_id': product_id,
#             'name': name,
#             'um_id': um_id,
#             'price_per_unit': price_per_unit,
#             'um_name': um_name
#         })
#     cnx.close()
#     return response
   


# get_all_products_table()

# if __name__ == '__main__':
#     # connection = get_sql_connection()
#     print(get_all_products_table())




from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products_table.product_id, products_table.product_name, products_table.uom, products_table.price_per_unit, um_table.um_name from products_table inner join um_table on products_table.uom=um_table.um_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products_table"
             "(product_name, uom, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products_table where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

# if __name__ == '__main__':
#     connection = get_sql_connection()
#     # print(get_all_products(connection))
#     delete_product(connection,10)
#     # print(insert_new_product(connection, {
#     #     'product_name': 'potatoes2',
#     #     'uom_id': '1',
#     #     'price_per_unit': 100
#     # }))