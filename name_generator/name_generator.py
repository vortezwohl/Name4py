import json
import os
import random

import gdown
import requests

from name_generator.enum.country import Country
from name_generator.enum.gender import Gender
from name_generator.resource import __PATH__


class NameGenerator(object):
    def __init__(self, country: Country):
        self._country = country
        self._resource_path = os.path.join(__PATH__, f'{self._country.numeric}.json')
        self._resource = None
        if not os.path.exists(self._resource_path):
            url = f'https://github.com/vortezwohl/NameGenerator/releases/download/0.0.0/{self._country.numeric}.json'
            if requests.get(url=url).status_code == 200:
                try:
                    gdown.download(
                        url=url,
                        output=self._resource_path,
                        quiet=True,
                        proxy=os.getenv('HTTPS_PROXY', os.getenv('https_proxy', None))
                    )
                except:
                    os.remove(self._resource_path)
            else:
                raise ValueError(f'{self._country.official_name} is currently not supported.')
        with open(self._resource_path, 'r', encoding='utf-8') as r:
            self._resource = json.load(r)

    def next_name(self, gender: Gender, family_name: str | None = None, surname_first: bool = False, hyphenate: bool = True):
        first_name = random.sample(self._resource['first_name'][gender.value], k=1)[0]
        last_name = random.sample(self._resource['last_name'], k=1)[0] if not family_name else family_name
        while first_name in last_name:
            first_name = random.sample(self._resource['first_name'][gender.value], k=1)[0]
        segment = ' ' if hyphenate else ''
        if surname_first:
            first_name, last_name = last_name, first_name
        return f'{first_name}{segment}{last_name}'
