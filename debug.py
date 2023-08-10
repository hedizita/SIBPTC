import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('SELECT product.product_id, product.model, product.price, product.status, '
            'product_description.name, product_description.description, '
            '(SELECT product_image.image FROM product_image WHERE product_image.product_id = product.product_id) as image '
            'FROM product '
            'JOIN product_description ON product.product_id = product_description.product_id')
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
