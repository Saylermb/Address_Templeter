import sys
from pathlib import Path
try:
    from training.osm_addresses import address_generator
    from training.xml_writer import AddressesXML
except ModuleNotFoundError:
    sys.path.append(str(Path(__file__).parent.parent))
    from training.osm_addresses import address_generator
    from training.xml_writer import AddressesXML

file = open(Path(__file__).parent.joinpath("checked.txt"))
data = file.read()

xml = AddressesXML()
rows = eval(data)

for row in rows:
    xml.append(row)

for row in address_generator():
    xml.append(row)

xml.write(Path(__file__).parent.joinpath("dataset.xml"))

print('Update dataset.xml')


