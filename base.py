import sqlite3
import xml.etree.ElementTree as ET

#Establish a connection to the SQLite database
conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

#Retrieve required fields from the database
cur.execute('SELECT product.product_id, product.model, product.price, product.status, '
            'product_description.name, product_description.description, '
            '(SELECT product_image.image FROM product_image WHERE product_image.product_id = product.product_id) as image '
            'FROM product '
            'JOIN product_description ON product.product_id = product_description.product_id')
rows = cur.fetchall()

#Create the root element for the XML feed
root = ET.Element('feed')
root.set('xmlns', 'http://www.w3.org/2005/Atom')

#Iterate through the fetched database rows and create the needed element and fields
for row in rows:
    #prod_id,
    model, price, status, brand, title, desc, im_link = row  

    prod_el = ET.SubElement(root, 'product')

    #ET.SubElement(prod_el, 'id').text = str(prod_id)
    ET.SubElement(prod_el, 'title').text = title
    ET.SubElement(prod_el, 'description').text = desc
    #ET.SubElement(prod_el, 'link').text = f'https://butopea.com/p/{prod_id}'
    ET.SubElement(prod_el, 'image_link').text = im_link
    ET.SubElement(prod_el, 'additional_image_link').text = ''
    ET.SubElement(prod_el, 'availability').text = 'in stock' if status == 1 else 'out of stock'
    ET.SubElement(prod_el, 'price').text = str(price) + ' HUF'
    ET.SubElement(prod_el, 'brand').text = brand
    ET.SubElement(prod_el, 'condition').text = 'new'

#Create an ElementTree from the root element
tree = ET.ElementTree(root)

#Write the XML content to the 'feed.xml' file with specified encoding and declaration
tree.write('feed.xml', encoding='utf-8', xml_declaration=True)

#Close the database connection
conn.close()

#Print conformation message if succesful
print("ok")