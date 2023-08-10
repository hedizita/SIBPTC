import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM product')
rows = cur.fetchall()

root = ET.Element('feed')

for row in rows:
    prod_id, title, desc, link, im_link, add_im_link, av, price, brand, cond = row  

    prod_el = ET.SubElement(root, 'product')

    ET.SubElement(prod_el, 'id').text = str(prod_id)
    ET.SubElement(prod_el, 'title').text = title
    ET.SubElement(prod_el, 'descripton').text = desc
    ET.SubElement(prod_el, 'link').text = link
    ET.SubElement(prod_el, 'image_link').text = im_link
    ET.SubElement(prod_el, 'additional_image_link').text = add_im_link
    ET.SubElement(prod_el, 'availability').text = av
    ET.SubElement(prod_el, 'price').text = str(price)
    ET.SubElement(prod_el, 'brand').text = brand
    ET.SubElement(prod_el, 'condition').text = cond

tree = ET.ElementTree(root)
tree.write('feed.xml', encoding='utf-8', xml_declaration=True)

conn.close()

print("ok")
#tree.write('/HEDI/programozas/butopea/SIBPTC/feed.xml', encoding='utf-8', xml_declaration=True)
