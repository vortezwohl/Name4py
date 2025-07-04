import json

from name4py import NameGenerator, Country, Gender
from name4py.resource import __PATH__


print(NameGenerator(Country.CHN).next_name(Gender.Female, surname_first=True, hyphenate=False))
print(NameGenerator(Country.CAN).next_name(Gender.Male, surname_first=False, hyphenate=True))
print(NameGenerator(Country.PRT).next_name(Gender.Male, surname_first=False, hyphenate=True))
print(NameGenerator(Country.ESP).next_name(Gender.Male, surname_first=False, hyphenate=True))
print(NameGenerator(Country.DEU).next_name(Gender.Female, surname_first=False, hyphenate=True))


def read_json(file_name: str) -> dict | list:
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(data: dict, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        return json.dump(data, f)


def combine(data_1: dict, data_2: dict) -> dict:
    data_1['first_name']['female'].extend(data_2['first_name']['female'])
    data_1['first_name']['female'] = list(set(data_1['first_name']['female']))
    data_1['first_name']['male'].extend(data_2['first_name']['male'])
    data_1['first_name']['male'] = list(set(data_1['first_name']['male']))
    data_1['last_name'].extend(data_2['last_name'])
    data_1['last_name'] = list(set(data_1['last_name']))
    return data_1


# data1 = read_json(f'{__PATH__}/840.json')
# data2 = read_json(f'{__PATH__}/250.json')
# print(write_json(combine(data1, data2), f'{__PATH__}/124.json'))

# for _ in range(100):
#     print(NameGenerator(Country.GBR).next_name(Gender.Female, surname_first=False, hyphenate=True))