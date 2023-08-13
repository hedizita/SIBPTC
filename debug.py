import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute("data.sqbpro")
rows = cur.fetchall()

root = ET.Element('feed')
root.set('xmlns', 'http://www.w3.org/2005/Atom')

for row in rows:
    print(row)
    prod_id, model, price, status, title, desc, brand, im_link = row  
    prod_el = ET.SubElement(root, 'product')

    ET.SubElement(prod_el, 'id').text = str(prod_id)
    ET.SubElement(prod_el, 'title').text = title
    ET.SubElement(prod_el, 'description').text = desc
    ET.SubElement(prod_el, 'link').text = f'https://butopea.com/p/{prod_id}'
    ET.SubElement(prod_el, 'image_link').text = im_link
    ET.SubElement(prod_el, 'additional_image_link').text = ''
    ET.SubElement(prod_el, 'availability').text = 'in stock' if status == 1 else 'out of stock'
    ET.SubElement(prod_el, 'price').text = str(price) + ' HUF'
    ET.SubElement(prod_el, 'brand').text = brand
    ET.SubElement(prod_el, 'condition').text = 'new'

tree = ET.ElementTree(root)
tree.write('feed.xml', encoding='utf-8', xml_declaration=True)

conn.close()

print("ok")
