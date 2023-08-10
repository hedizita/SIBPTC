import sqlite3
import xml.etree.ElementTree as ET


conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM product')
rows = cur.fetchall() #This will return a list of all the rows in the `product` table

#we need and XML document for each row
for row in rows:
    prod_id = row[0]
    title = row[1]
    desc = row[2]
    link = row[3]
    im_link = row[4]
    add_im_link = row[5]
    av = row[6]
    price = row[7]
    brand = row[8]
    cond = row[9]

    root = ET.element('product')
    root.set('id', prod_id)
    root.set('title', title)
    root.set('description', desc)
    root.set('link', link)
    root.set('image_link', im_link)
    root.set('additional_image_link', add_im_link)
    root.set('availability', av)
    root.set('price', price)
    root.set('brand', brand)
    root.set('condition', cond)

tree = ET.ElementTree(root)
tree.write('feed.xml')
