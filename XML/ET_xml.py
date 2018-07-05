# _*_coding:utf-8_*_

import xml.etree.ElementTree as ET

tree = ET.parse("movies.xml")
root = tree.getroot()

for child in root:
    if child.tag == "movie":
        print("*** movie ***")
        print("Title:", child.attrib['title'])
    for sub in child:
         print(sub.tag.capitalize(),":",sub.text)
