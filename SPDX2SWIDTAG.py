import sys
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

package_names = []

# Open the SPDX(Tag:Value in txt) file passed as an argument to the script and extract "packageName".
# If your SPDX file has diffrent name for "packageName", please change here.
with open(sys.argv[1], 'r') as file:
    for line in file:
        if line.startswith('PackageName: '):
            package_name = line.replace('PackageName: ', '').strip()
            package_names.append(package_name)

# Open the ProductList file extracted via MyJVN API.
with open('ProductList.txt', 'r', encoding='utf-8') as f:
    search_result = []
    # Read ProductList.txt and find the line which includes names of package.
    for line in f:
        for package_name in package_names:
            if package_name in line:
                search_result.append(line)

    # Extract the line starting from "<Product".
    search_result2 = []
    for line in search_result:
        if '<Product' in line and any(name in line for name in package_names):
            search_result2.append(line)

    search_result3 = []
    for line in search_result2:
        for package_name in package_names:
            pattern = rf"\b{package_name}\b"
            if re.search(pattern, line, re.IGNORECASE):
                search_result3.append(line)

    # Extract the cpe information.
    search_result4 = []
    cpe_pattern = re.compile(r'cpe="([^"]+)"')

    for line in search_result3:
        cpe_match = cpe_pattern.search(line)
        if cpe_match:
            cpe = cpe_match.group(1)
            search_result4.append(cpe)

    unique_cpes = set(search_result4)

# Create XML-Like .swidtag file.
root = ET.Element('swid:SoftwareIdentity', {'xmlns:swid': 'http://standards.iso.org/iso/19770/-2/2015/schema.xsd',
                                             'xmlns:xsi': 'htttp://www.w3.org/2001/XMLSchema-instance',
                                             'xsi:schemaLocation': 'http://standards.iso.org/iso/19770/-2/2015/schema.xsd http://standards.iso.org/iso/19770/-2/2015-current/schema.xsd',
                                             'name': '',
                                             'tagId': '',
                                             'version': '1.0'})

# Create Entity Element.
ET.SubElement(root, 'swid:Entity', {
    'name': 'MyJVN mjcheck4',
    'regid': 'https://jvndb.jvn.jp/apis/myjvn/mjcheck4.html', 
    'role': 'tagCreator'})

# Create Link Element.
for cpe in unique_cpes:
    link = ET.SubElement(root, 'swid:Link', {'rel': 'component', 'href': cpe })

# Export .swidtag file.
xml_string = ET.tostring(root, encoding='utf-8', xml_declaration=True)
dom = minidom.parseString(xml_string)
with open('output.swidtag', 'w', encoding='utf-8') as f:
    f.write(dom.toprettyxml(indent='    '))