import json
import os
import random

import gdown
import requests
from vortezwohl.concurrent import ThreadPool

from name4py.enum.country import Country
from name4py.enum.gender import Gender
from name4py.resource import __PATH__


class NameGenerator(object):
    def __init__(self, country: Country):
        self._country = country
        self._resource_path = os.path.join(__PATH__, f'{self._country.numeric}.json')
        self._resource = None
        self.__proxies = {
            'http': os.getenv('HTTP_PROXY', os.getenv('http_proxy')),
            'https': os.getenv('HTTPS_PROXY', os.getenv('https_proxy'))
        }
        if not os.path.exists(self._resource_path):
            url = f'https://github.com/vortezwohl/Name4py/releases/download/0.0.0/{self._country.numeric}.json'
            if requests.get(url=url, proxies=self.__proxies).status_code == 200:
                try:
                    gdown.download(
                        url=url,
                        output=self._resource_path,
                        quiet=True,
                        proxy=self.__proxies.get('https')
                    )
                except:
                    os.remove(self._resource_path)
            else:
                raise ValueError(f'{self._country.official_name} is currently not supported.')
        with open(self._resource_path, 'r', encoding='utf-8') as r:
            self._resource = json.load(r)

    def __call__(self, **kwargs) -> str | list[str]:
        if 'batch_size' in kwargs.keys():
            return self.batch_generate(**kwargs)
        return self.generate(**kwargs)

    def generate(self, gender: Gender, family_name: str | None = None, surname_first: bool = False,
                 hyphenate: bool = True, seed: int | None = None, return_respectively: bool = False) -> str | tuple:
        if seed:
            random.seed(seed)
        first_name = random.sample(self._resource['first_name'][gender.value], k=1)[0]
        last_name = random.sample(self._resource['last_name'], k=1)[0] if not family_name else family_name
        while first_name in last_name:
            first_name = random.sample(self._resource['first_name'][gender.value], k=1)[0]
        if return_respectively:
            return first_name, last_name
        segment = ' ' if hyphenate else ''
        if surname_first:
            first_name, last_name = last_name, first_name
        return f'{first_name}{segment}{last_name}'

    def batch_generate(self, batch_size: int, gender: Gender, family_name: str | None = None,
                       surname_first: bool = False, hyphenate: bool = True, seed: int | None = None,
                       return_respectively: bool = False) -> list[str]:
        threads = ThreadPool()
        results = threads.map(job=self.generate,
                              arguments=[(gender, family_name, surname_first, hyphenate, seed, return_respectively)] * batch_size)
        results = [_.returns for _ in results if not _.error]
        return results
