from random import choice

import pandas as pd


class name_value:
    def __init__(self):
        self.list_of_name = pd.read_csv("../names.csv")
        self.list_of_name = self.list_of_name.loc[self.list_of_name["percent"] > 0.01]["name"].drop_duplicates()
        self.list_of_name = self.list_of_name.reset_index()["name"]

    def get_value(self):
        return choice(self.list_of_name)


print(name_value().get_value())
