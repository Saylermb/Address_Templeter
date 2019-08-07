import xml.etree.ElementTree as xml


class AddressesXML:
    def __init__(self):
        self.root = xml.Element('AddressCollection')

    def append(self, address_: iter):
        """
        add in new teg AddressString values
        :param address_: iter object in format [(key, value), (key, value))]
        """
        self.address = xml.Element('AddressString')
        self.root.append(self.address)
        for name, atr in address_:
            setattr(self, name, xml.SubElement(self.address, name))
            setattr(getattr(self, name), "text", str(atr))

    def write(self, file_name):
        tree = xml.ElementTree(self.root)
        tree.write(file_name)


if __name__ == '__main__':
    s = AddressesXML()
    s.append([("name", "1"), ("test", "2"), ("ttt", 3)])
    s.append([("street_type", 7), ("number", 4)])
    s.write("test.xml")