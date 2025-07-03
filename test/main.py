from names_dataset import NameDataset

nd = NameDataset()

names = nd.get_country_codes()

for name in names:
    print(name)
