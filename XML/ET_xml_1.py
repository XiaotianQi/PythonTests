# _*_coding:utf-8_*_

import xml.etree.ElementTree as ET

tree = ET.parse("movies_1.xml")
root = tree.getroot()

for child in root.findall('movie'):
    child.remove(child.find('format'))

    studio = ET.Element('studio')
    studio.text = 'XX'
    child.append(studio)

tree.write('movies_new.xml')
