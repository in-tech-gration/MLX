from random import choice

import pandas as pd


class address_value:

    def __init__(self):
        self.list_of_cities = pd.read_csv("../cities.csv")
        self.list_of_name = pd.read_csv("../names.csv")
        self.list_of_name = self.list_of_name.loc[self.list_of_name["percent"] > 0.01]["name"].drop_duplicates()
        self.list_of_name = self.list_of_name.reset_index()["name"]

    def get_value(self):
        l = choice(range(1, 4, 1))
        num = choice(range(2, 150, 1))
        ZIP = choice(range(20000, 99999, 1))
        l2 = choice(range(5, 15, 1))
        return \
            (' '.join([choice(self.list_of_name) for i in range(l)])).lower() + " " + \
            choice([" street ", ""]) + \
            choice([str(num) + " ", " "]) + \
            choice([str(ZIP), ""]) + " " + \
            choice(self.list_of_name).lower()


import os as os

print(os.getcwd())
print(address_value().get_value())
