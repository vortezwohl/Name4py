# Name4py

Generate names in every language.

## Installation

- From PyPi

```
pip install -U name4py
```

- From Github

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
chinese_name = NameGenerator(Country.CHN).next_name(Gender.Female, surname_first=True, hyphenate=False)
french_name = NameGenerator(Country.FRA).next_name(Gender.Male, surname_first=False, hyphenate=True)
```

```python
print(chinese_name)
print(french_name)
```

output:

```
高思涵
Frédérick St-Martin
```