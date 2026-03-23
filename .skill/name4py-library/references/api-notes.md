# Name4py API Notes

## Install

Install from PyPI for normal usage:

```bash
uv add -U name4py
or
pip install -U name4py
```

Install from Git only when you need repository-head or unreleased changes:

```bash
pip install git+https://github.com/vortezwohl/Name4py.git
```

Package installation and runtime data availability are separate concerns. A successful install does not guarantee every country JSON file is already cached locally.

## Public Surface

Import from `name4py`:

```python
from name4py import NameGenerator, Country, Gender
```

Public exports come from:

- `name4py/__init__.py`
- `name4py/name_generator.py`
- `name4py/enum/country.py`
- `name4py/enum/gender.py`

## Constructor Behavior

`NameGenerator(country: Country)`:

- resolves the resource path from `country.numeric`
- loads `name4py/resource/<numeric>.json` if present
- otherwise performs a GET against the project release URL for that numeric code
- downloads the JSON with `gdown.download(...)` when the remote asset exists
- raises `ValueError` if the remote asset is missing

Because the constructor may hit the network, avoid creating many fresh generators in tight loops when one instance can be reused.

## Method Notes

`generate(...)`:

- returns one formatted name string by default
- returns `(first_name, last_name)` when `return_respectively=True`
- uses `family_name` as the surname override when provided
- swaps order after sampling when `surname_first=True`
- joins parts with `' '` unless `hyphenate=False`

`batch_generate(...)`:

- maps repeated `generate(...)` calls over a thread pool
- returns a list of successful worker results

## Creative-Workflow Design Rules

When the caller is a story, game, role-playing, or other generative system:

- prefer candidate pools over one-shot final names
- use `return_respectively=True` to extract first names and surnames without reparsing formatted strings
- generate surnames independently from given names when downstream logic needs to control family grouping
- generate separate given-name pools for each gender category used by the application
- oversample candidates beyond the entity count so the downstream layer can filter for uniqueness, tone, and relationship constraints
- keep family-consistency rules outside `name4py`; enforce them in the application or prompt layer after candidate generation

A proven pattern is:

```python
pool_size = entity_count + 16
surname_candidates = [last for _, last in generator.batch_generate(..., return_respectively=True)]
male_given_candidates = [first for first, _ in generator.batch_generate(..., return_respectively=True)]
female_given_candidates = [first for first, _ in generator.batch_generate(..., return_respectively=True)]
```

Treat the resulting lists as prompt inputs or rule-engine inputs, not as already approved final names.

## Known Constraints

- Only binary gender values are available in the current enum.
- Supported countries are bounded by the enum plus the availability of corresponding release JSON files.
- First-use behavior can fail in offline environments even when the Python package itself is installed.

## Repository-Conventional Formatting

The repository README and test script use:

- `surname_first=True` for China, Japan, South Korea, and Vietnam
- `hyphenate=False` for China, Japan, and South Korea

Treat those as project conventions, not universal rules for all use cases.