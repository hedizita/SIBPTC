import sqlite3
import xml.etree.ElementTree as ET
import sys


sys.stdout.reconfigure(encoding='utf-8')


conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('SELECT product.product_id, product.model, product.price, product.status, '
            'product_description.name, product_description.description, '
            '(SELECT product_image.image FROM product_image WHERE product_image.product_id = product.product_id) as image '
            'FROM product '
            'JOIN product_description ON product.product_id = product_description.product_id')
rows = cur.fetchall()


root = ET.Element('feed')
root.set('xmlns', 'http://www.w3.org/2005/Atom')

for row in rows:
    #print(row)
    
    #prod_id, 
    model, price, status, brand, title, desc, im_link = row  

    prod_el = ET.SubElement(root, 'product')

    #ET.SubElement(prod_el, 'id').text = str(prod_id)
    ET.SubElement(prod_el, 'title').text = title.encode('utf-8')
    ET.SubElement(prod_el, 'description').text = desc.encode('utf-8')
    #ET.SubElement(prod_el, 'link').text = f'https://butopea.com/p/{prod_id}'
    ET.SubElement(prod_el, 'image_link').text = im_link
    ET.SubElement(prod_el, 'additional_image_link').text = ''
    ET.SubElement(prod_el, 'availability').text = 'in stock' if status.encode('utf-8') == 1 else 'out of stock'
    ET.SubElement(prod_el, 'price').text = str(price) + ' HUF'
    ET.SubElement(prod_el, 'brand').text = brand.encode('utf-8')
    ET.SubElement(prod_el, 'condition').text = 'new'

tree = ET.ElementTree(root)
tree.write('feed.xml', encoding='utf-8', xml_declaration=True)

conn.close()

print("ok")
for row in rows:
    print(row)
