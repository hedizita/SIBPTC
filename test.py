import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('SELECT product.product_id, product.model, product.price, product.status,'
            'manufacturer.name, product_description.name, product_description.description,'
            'product_image.image'
            'FROM product'
            'JOIN manufacturer ON product.manufacturer_id = manufacturer.manufacturer_id'
            'JOIN product_description ON product.product_id = product_description.product_id'
            'JOIN product_image ON product.product_id = product_image.product_id')
rows = cur.fetchall()

root = ET.Element('feed')

for row in rows:
    prod_id, model, price, status, brand, title, desc, im_link = row  

    prod_el = ET.SubElement(root, 'product')
    prod_el2 = ET.SubElement(root, 'product_description')
    prod_el3 = ET.SubElement(root, 'prudcut_image')

    ET.SubElement(prod_el, 'id').text = str(prod_id)
    ET.SubElement(prod_el, 'title').text = title
    ET.SubElement(prod_el2, 'descripton').text = desc
    ET.SubElement(prod_el, 'link').text = f'https://butopea.com/p/{prod_id}'
    ET.SubElement(prod_el, 'image_link').text = im_link
    ET.SubElement(prod_el3, 'additional_image_link').text = ''
    ET.SubElement(prod_el, 'availability').text = 'in stock' if status == 1 else 'out of stock'
    ET.SubElement(prod_el, 'price').text = str(price) + ' HUF'
    ET.SubElement(prod_el, 'brand').text = brand
    ET.SubElement(prod_el, 'condition').text = 'new'

tree = ET.ElementTree(root)
tree.write('feed.xml', encoding='utf-8', xml_declaration=True)

conn.close()

print("ok")
#tree.write('/HEDI/programozas/butopea/SIBPTC/feed.xml', encoding='utf-8', xml_declaration=True)
