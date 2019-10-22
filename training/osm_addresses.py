import re
import overpy
from random import randint
from address_templeter import STREET_PRETEXT, PUNCTUATION_MARK, \
    HOUSE_PRETEXT, PLACE_PRETEXT, REGION_PRETEXT, COMMA

api = overpy.Overpass()

geo_polygon = "(50.482287,30.509273,50.539674,30.520974)"
response = api.query(f"""way["addr:street"]["addr:housenumber"]{geo_polygon};
    (._;>;);
    out body;""")

iter_address = [way.tags for way in response.ways]

geo_polygon = "(48.460824,35.005537,48.480824, 35.055107)"
response = api.query(f"""way["addr:street"]["addr:housenumber"]{geo_polygon};
    (._;>;);
    out body;""")

iter_address+= [way.tags for way in response.ways]

REGION_PRETEXT = list(REGION_PRETEXT.keys())
STREET_PRETEXT = list(STREET_PRETEXT.keys())


def addr_housenumber(housenumber):
    def mark_house(part_house):
        if part_house in PUNCTUATION_MARK:
            return "PunctuationMark", part_house
        elif part_house in COMMA:
            return "Comma", part_house
        elif part_house == '-':
            return "Dash", part_house
        else:
            return 'HouseNumber', part_house

    result = []
    housenumber = re.findall("\d+|\w+|[/]", housenumber)
    variant = randint(1, 4)
    if len(housenumber) > 3:
        variant = randint(1, 2)
    patterns = {1: ["".join(housenumber)], 2: housenumber, 3: ["-".join(housenumber)],
                4: [housenumber[0], "-", housenumber[1] if len(housenumber) >= 2 else "".join(housenumber)]}
    for s in patterns.get(variant):
        result.append(mark_house(s))
    return result


def addr_name(name):
    result = []
    splited = [re.findall(r"[\w\d]+|[\,\(\)\!\?\-]", name),
               re.findall(r"[\w\d-]+", name)]
    splited = splited[randint(0, 1)]
    for s in splited:
        if s in PUNCTUATION_MARK:
            result.append(("PunctuationMark", s))
        elif s in COMMA:
            result.append(("Comma", s))
        elif s in HOUSE_PRETEXT:
            result.append(("HousePretext", s))
        else:
            result.append(("HouseName", s))
    return result


def post_code(code):
    return [("PostCode", code)]


def street(street_name):
    result = []
    splited = [re.findall(r"[\w\d]+|[\,\(\)\!\?\-]", street_name),
               re.findall(r"[\w\d-]+", street_name)]
    splited = splited[randint(0, 1)]
    for s in splited:
        if s in PUNCTUATION_MARK:
            result.append(("PunctuationMark", s))
        elif s in STREET_PRETEXT:
            result.append(("StreetPretext", s))
        elif s in COMMA:
            result.append(("Comma", s))
        elif s == "-":
            result.append(("Dash", s))
        else:
            result.append(("Street", s))
    if randint(0, 1):
        pre = result.pop(-1)
        if randint(0, 1):
            result.insert(0, pre)
    return result


def other(text):
    result = []
    splited = [re.findall(r"[\w\d]+|[\,\(\)\!\?\-]", text),
               re.findall(r"[\w\d-]+", text)]
    splited = splited[randint(0, 1)]
    for s in splited:
        if s in PUNCTUATION_MARK:
            result.append(("PunctuationMark", s))
        elif s in COMMA:
            result.append(("Comma", s))
        elif s.isdigit():
            result.append(("OtherNumber", s))
        else:
            result.append(("OtherText", s))
    return result


def get_row():
    city = ["Киев", "Харьков", "Львов", "Днепропетровск", "Кропивницкий", "Николаев"]
    city2 = ["Белая", "Франковск", "Подольск", "Рог"]
    city = city[randint(0, 5)]
    city2 = city2[randint(0, 3)]
    city_prefix = PLACE_PRETEXT[randint(0, 7)]
    region_prefix = REGION_PRETEXT[randint(0, 7)]
    reg = ["Ясиноватский", "Донецкая", "Киевский", "Ивано-Франковский", "Лювовский", "Ивано", "Лат"]
    region = reg[randint(0, 6)]
    region2 = reg[randint(0, 6)]
    rnd = randint(0, 6)
    row = [[("PlacePretext", city_prefix), ("Place", city), ],
           [("PlacePretext", city_prefix), ("Place", city), ("Dash", "-"), ("Place", city2), ],
           [("PlacePretext", city_prefix), ("Place", f"{city}-{city2}")],
           [("PlacePretext", city_prefix), ("Place", f'"{city}"')],
           [("Place", f'{city}')],
           [("Place", city), ("Place", city2), ], []]
    row = row[rnd]
    rnd = randint(0, 3)
    if rnd == 0:
        for s in ("Region", region), ("RegionPretext", region_prefix):
            row.insert(0, s)
    elif rnd == 1:
        for s in (("RegionPretext", region_prefix), ("Region", region)):
            row.insert(0, s)
    elif rnd == 2 and randint(0, 2) == 0:
        for s in (("RegionPretext", region_prefix), ("Region", region), ("Dash", "-"), ("Region", region2)):
            row.insert(0, s)
    return row


func_dict = {'addr:housenumber': addr_housenumber,
             'addr:postcode': post_code,
             'addr:street': street,
             'name': addr_name, }


def pars_address(address):  # add random address name
    row = get_row()
    address = {'addr:street': address.get('addr:street'),
               'addr:housenumber': address.get('addr:housenumber'),
               'name': address.get('name'),
               'addr:postcode': address.get('addr:postcode'),
               **address, 'building': 0, 'building:levels': 0}

    for key, value in address.items():
        if value:
            if randint(0, 1):
                row.append(("Comma", ","))
            for v in func_dict.get(key, other)(value):
                row.append(v)
    return row


def address_generator():
    for addr in iter_address:
        yield pars_address(addr)


if __name__ == '__main__':
    for address in address_generator():
        print(address)