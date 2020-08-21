from xml.etree import ElementTree
import os
import sys

input_file_name = sys.argv[1]
full_file_name = os.path.abspath(input_file_name)
file_name = input_file_name.split('.')[0]+'.out'

dom = ElementTree.parse(full_file_name)
property = dom.findall('property')

with open(file_name, 'w') as write_xml_conf:
    for p in property:
        name = p.find('name').text
        value = p.find('value').text
        print("{} = {}".format(name, value))
        write_xml_conf.write("{} = {}\n".format(name, value))

