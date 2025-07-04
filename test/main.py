from name4py import NameGenerator, Country, Gender


chinese_name = NameGenerator(Country.CHN).next_name(Gender.Female, surname_first=True, hyphenate=False)
french_name = NameGenerator(Country.FRA).next_name(Gender.Male, surname_first=False, hyphenate=True)

print('Chinese name', chinese_name)
print('French name', french_name)
