---
name: name4py-library
description: Add, update, review, or explain Python code that uses the `name4py` package for locale-aware personal name generation. Use when Codex needs to generate sample names for supported countries, wire `NameGenerator`, choose `Country` or `Gender` enums, handle `surname_first` or `hyphenate` formatting, account for automatic dataset download and unsupported-country behavior, or build candidate name pools for creative workflows such as fictional character naming.
---

# Name4py Library

Use this skill when work involves the local `name4py` package in this repository.

## Install And Import

Install it with one of the project-supported commands:

```bash
uv add -U name4py
```

or

```bash
pip install -U name4py
```

Use the Git repository install only when you need unreleased code from this repository:

```bash
pip install git+https://github.com/vortezwohl/Name4py.git
```

Prefer `uv` when the target project already uses `uv` or manages dependencies from `pyproject.toml`.

Import from the public package surface instead of deep internal modules unless you are modifying the library itself:

```python
from name4py import NameGenerator, Country, Gender
```

## Quick Start

Create a generator with a country enum, then call `generate(...)` or `batch_generate(...)`:

```python
generator = NameGenerator(Country.USA)
name = generator.generate(gender=Gender.Female)
names = generator.batch_generate(batch_size=8, gender=Gender.Male)
```

## Workflow

1. Confirm the task really targets `name4py` in this repo, not another naming library.
2. Prefer the public exports from `name4py.__init__` instead of importing deep internal paths unless the change is internal to the package.
3. Pick a `Country` enum member first, then set formatting flags that match local naming order.
4. Use `generate(...)` for one value and `batch_generate(...)` for lists.
5. Account for resource downloads on first use and for unsupported-country failures.
6. For creative-writing workflows, generate structured candidate pools first and let the downstream prompt or business logic perform the final selection.

## Core API

`NameGenerator(country: Country)`

- Loads a per-country JSON resource from `name4py/resource/<numeric>.json`.
- If the resource file is missing, tries to download it from the project GitHub release before loading it.
- Raises `ValueError` when the country is not currently supported by the remote dataset.

`generate(gender, family_name=None, surname_first=False, hyphenate=True, seed=None, return_respectively=False)`

- `gender` is required and must be `Gender.Male` or `Gender.Female`.
- `family_name` forces the surname or family name instead of sampling one.
- `surname_first=True` returns family name before given name.
- `hyphenate=False` removes the separator entirely; otherwise the separator is a single space.
- `seed` seeds Python `random` before sampling.
- `return_respectively=True` returns `(first_name, last_name)` before formatting them into a string.

`batch_generate(batch_size, ...)`

- Uses the same arguments as `generate(...)`, plus required `batch_size`.
- Internally fans out with `vortezwohl.concurrent.ThreadPool`.
- Returns only successful results from worker calls.

## Locale Formatting Guidance

Use `surname_first=True` for locales in this repo that commonly render family name first, especially examples like `Country.CHN`, `Country.JPN`, `Country.KOR`, and `Country.VNM`.

Use `hyphenate=False` when the expected output should concatenate without spaces. The repository examples do this for `Country.CHN`, `Country.JPN`, and `Country.KOR`.

Do not assume one formatting rule fits every supported country. If the user asks for culturally realistic display order, make that choice explicit in code.

## Creative Naming Pattern

When `name4py` is used for fiction, game content, or other generative writing systems, treat it as a candidate generator instead of the final naming authority.

Recommended pattern:

- Create one `NameGenerator` per target locale.
- Generate surnames and given names separately with `return_respectively=True` instead of splitting formatted full names.
- Build oversized candidate pools, usually larger than the number of entities you need, so the downstream creative step can enforce uniqueness, family grouping, and tone.
- Generate male and female given-name pools separately when the downstream schema tracks gender.
- Pass the candidate pools into the prompt or selection layer as inputs; do not force the first sampled value to become the final character name.
- Keep family consistency as an explicit rule in the downstream logic: characters from the same family should usually share a surname, while unrelated families should not accidentally collapse to one surname.
- Preserve cultural adaptation at the candidate-pool stage by choosing the correct `Country` and formatting options before handing names to the creative system.

A practical heuristic is to request `entity_count + buffer` candidates, where the buffer is large enough to absorb collisions and stylistic filtering.

## Implementation Notes

- `Country` currently exposes a large fixed enum set in `name4py/enum/country.py` with more than 100 entries.
- `Gender` only supports `Male` and `Female`.
- `NameGenerator.__call__(...)` forwards to `batch_generate(...)` when `batch_size` is present, otherwise to `generate(...)`.
- `generate(...)` avoids cases where the sampled first name is contained in the chosen last name by re-sampling the first name.
- Installing the package does not guarantee the country dataset is already present locally; first use may still download a JSON resource.
- Initial dataset download depends on network access and respects `HTTP_PROXY` / `HTTPS_PROXY`.

## Common Tasks

### Add example code

Use concise examples that import from `name4py` and pass explicit enums:

```python
from name4py import Country, Gender, NameGenerator

generator = NameGenerator(Country.GBR)
print(generator.generate(gender=Gender.Female))
```

### Produce locale-aware sample data

When generating fixture or demo data, keep the locale choice and formatting rule together:

```python
from name4py import Country, Gender, NameGenerator

generator = NameGenerator(Country.JPN)
samples = generator.batch_generate(
    batch_size=10,
    gender=Gender.Female,
    surname_first=True,
    hyphenate=False,
)
```

### Build candidate pools for character creation

Use `return_respectively=True` so the downstream layer receives structured first-name and surname candidates:

```python
from name4py import Country, Gender, NameGenerator

generator = NameGenerator(Country.GBR)
pool_size = character_count + 16

surname_candidates = [
    last_name
    for _, last_name in generator.batch_generate(
        batch_size=pool_size,
        gender=Gender.Female,
        return_respectively=True,
    )
]

male_given_candidates = [
    first_name
    for first_name, _ in generator.batch_generate(
        batch_size=pool_size,
        gender=Gender.Male,
        return_respectively=True,
    )
]

female_given_candidates = [
    first_name
    for first_name, _ in generator.batch_generate(
        batch_size=pool_size,
        gender=Gender.Female,
        return_respectively=True,
    )
]
```

This pattern is appropriate when a later prompt or rules engine must preserve family structure, narrative tone, or gender-specific naming style.

### Handle unsupported or offline cases

If the task needs robust application behavior, wrap generator creation and document why it may fail:

```python
from name4py import Country, NameGenerator

try:
    generator = NameGenerator(Country.CAN)
except ValueError:
    generator = None
```

If the task is documentation or testing, mention that first-run behavior may require the release asset to be reachable.

## References

Read [references/api-notes.md](references/api-notes.md) when you need:

- a compact summary of constructor and method behavior
- reminders about install-time versus first-run download behavior
- examples of country-specific formatting choices used by this repository
- guidance for structured candidate-pool generation in creative workflows