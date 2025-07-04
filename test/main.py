from name_generator import NameGenerator, Country, Gender

if __name__ == '__main__':
    for _ in range(10):
        print(NameGenerator(Country.CHN).next_name(Gender.Female, surname_first=False, hyphenate=True), end=', ')
