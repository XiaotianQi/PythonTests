# _*_coding:utf-8_*_

import os
import xml.dom.minidom

# minidom解析器打开 XML 文档
xml_path = os.path.abspath("movies.xml")
print ("xml file path:", xml_path)

dom_tree = xml.dom.minidom.parse(xml_path)
collection = dom_tree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

# 获取所有电影及其详细信息

movies = collection.getElementsByTagName("movie")

for i in movies:
    print("*** Movie ***")
    if i.hasAttribute("title"):
        print("Title: %s" % i.getAttribute("title"))

    type = i.getElementsByTagName("type")[0]
    print("Type: %s" % type.childNodes[0].data)
    format = i.getElementsByTagName("format")[0]
    print("format: %s" % format.childNodes[0].data)
    rating = i.getElementsByTagName("rating")[0]
    print("rating: %s" % rating.childNodes[0].data)
    description = i.getElementsByTagName("description")[0]
    print ("Description: %s" % description.childNodes[0].data)
