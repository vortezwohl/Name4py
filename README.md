# Name Generator

Generate names in every language.

## Installation

- From PyPi

```
pip install -U name-generator
```

- From Github

```
pip install git+https://github.com/vortezwohl/NameGenerator.git
```

## Quick Start

1. Import SDKs

```python
from name_generator import NameGenerator, Country, Gender
```

2. Generate names

```python
chinese_name = NameGenerator(Country.CHN).next_name(Gender.Female, surname_first=True, hyphenate=False)
french_name = NameGenerator(Country.FRA).next_name(Gender.Male, surname_first=False, hyphenate=True)
```

```python
print('Chinese name', chinese_name)
print('French name', french_name)
```

output:

```
Chinese name 蒋佳慧
French name Lisandre Derouin
```