import pandas as pd
from name4py import NameGenerator, Country, Gender

available_countries = [Country.CAN, Country.CHN, Country.FRA,
                       Country.DEU, Country.IDN, Country.JPN,
                       Country.KOR, Country.PHL, Country.PRT,
                       Country.RUS, Country.VNM, Country.ESP,
                       Country.THA, Country.GBR, Country.USA]

name_dataset = []

for country in available_countries:
    for gender in Gender:
        for _ in range(10):
            surname_first = True if country in [Country.CHN, Country.JPN, Country.KOR, Country.VNM] else False
            hyphenate = False if country in [Country.CHN, Country.KOR] else True
            name_dataset.append({
                'Country/Region': country.official_name,
                'Gender': gender.value,
                'Full Name': NameGenerator(country).generate(gender, surname_first=surname_first, hyphenate=hyphenate)
            })

pd.DataFrame(name_dataset).to_csv('name_dataset.csv', index=False)
