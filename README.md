# Name4py

Generate names in every language.

## Installation

- From [PyPi](https://pypi.org/project/name4py/)

```
pip install -U name4py
```

- From [Github](https://github.com/vortezwohl/Name4py/releases/tag/0.0.1)

```
pip install git+https://github.com/vortezwohl/Name4py.git
```

## Quick Start

1. Import SDKs

```python
from name4py import NameGenerator, Country, Gender
```

2. Generate names

```python
available_countries = [Country.CAN, Country.CHN, Country.FRA,
                       Country.DEU, Country.IDN, Country.JPN,
                       Country.KOR, Country.PHL, Country.PRT,
                       Country.RUS, Country.VNM, Country.ESP,
                       Country.THA, Country.GBR, Country.USA]


for country in available_countries:
    surname_first = False
    hyphenate = True
    if country in [Country.CHN, Country.JPN, Country.KOR, Country.VNM]:
        surname_first = True
    if country in [Country.CHN, Country.KOR, Country.JPN]:
        hyphenate = False
    print(NameGenerator(country).generate(Gender.Female, surname_first=surname_first, hyphenate=hyphenate))
```

output:

```
Pénélope Farrell
汤雨桐
Cléopâtre Fromont
Alla Koslowski
Suciati Arsyad
金田理枝
남궁계영
Fiona Sobrino
Glauce Caldeira
Татьяна Наумов
Giáp Châu Hoa
Paulina Monreal
ธนัญญา กสิกร
Gunda Dawson
Dione Kidd
```