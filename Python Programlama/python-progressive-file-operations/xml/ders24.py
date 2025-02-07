import xml.etree.ElementTree as ET

root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "Bu bir örnek metin."

tree = ET.ElementTree(root)
tree.write("dosya.xml")