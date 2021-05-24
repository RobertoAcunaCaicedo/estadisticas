# Leer el corpus Life
import os
from xml.dom import pulldom
import xml.etree.ElementTree as ET
path = "E:\\Cursos\\Python\\Codigo\\significancia\\corpus\\"
# r=root, d=directories, f = files
files = []
for r, d, files in os.walk(path):
    for file in files:
        if file.endswith(".xml"):
            archivo_xml = ET.parse(file)
            rai = archivo_xml.getroot()
            print(rai)