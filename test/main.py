from name4py import NameGenerator, Country, Gender

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
    print(NameGenerator(country).batch_generate(batch_size=32, gender=Gender.Female, surname_first=surname_first, hyphenate=hyphenate))
