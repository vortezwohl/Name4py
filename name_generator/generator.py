import json
import os
import random

from name_generator.enum.country import Country
from name_generator.enum.gender import Gender
from name_generator.resource import __PATH__


class Generator(object):
    def __init__(self, country: Country):
        self._country = country
        self._resource_path = os.path.join(__PATH__, f'{self._country.numeric}.json')
        self._resource = None
        if not os.path.exists(self._resource_path):
            ...
        with open(self._resource_path, 'r', encoding='utf-8') as r:
            self._resource = json.load(r)

    def next_name(self, gender: Gender, family_name: str | None = None, surname_first: bool = False, hyphenate: bool = True):
        first_name = random.sample(self._resource['first_name'][gender.value], k=1)[0]
        last_name = random.sample(self._resource['last_name'], k=1)[0] if not family_name else family_name
        segment = ' ' if hyphenate else ''
        if surname_first:
            first_name, last_name = last_name, first_name
        return f'{first_name}{segment}{last_name}'


if __name__ == '__main__':
    for _ in range(100):
        print(Generator(Country.CHN).next_name(Gender.Male, surname_first=True, hyphenate=False, family_name='必养的'), end=', ')
