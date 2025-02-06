import xml.etree.ElementTree as ET
from xml.dom import minidom

def toXMLString(tree):
    string = ET.tostring(tree.getroot(), encoding='unicode')
    return string

def prettyPrint(xml_string):
    dom = minidom.parseString(xml_string)
    pretty = dom.toprettyxml(indent="\t")
    lines = [line for line in pretty.split('\n') if line.strip()]
    return '\n'.join(lines)

def append_xml(elements, names, values, file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element("root")

    doc = ET.SubElement(root, "newDoc")
    #for index, (name, text) in enumerate(new_data.items(), start=1):
    for element, name, value in zip(elements, names, values):
        ET.SubElement(doc, element, name=name).text = str(value)

    tree = ET.ElementTree(root)
    treeString = toXMLString(tree)
    prettyTree = prettyPrint(treeString)
    with open(file_path,"w") as f:
        f.write(prettyTree)

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "element1", name='Rush').text = "Best Drummer"
ET.SubElement(doc, "element2", name="Van Halen").text = "Best Guitar Player"

tree = ET.ElementTree(root)
treeString = toXMLString(tree)
prettyTree = prettyPrint(treeString)

with open("testfile.xml", "w") as f:
    f.write(prettyTree)

element = ['elema','elemb','elemc']
names = ['x','y','z']
values = [1,2,3]

'''
new = {}

for elem, name, value in zip(element, names, values):
    new.update({name: value})

print(new)
'''

append_xml(element, names, values, "testfile.xml")
