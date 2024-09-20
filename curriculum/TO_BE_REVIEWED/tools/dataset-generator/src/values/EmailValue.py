import string
from random import choice

import pandas as pd


class email_value:

    def __init__(self):
        self.list_of_name = pd.read_csv("../names.csv")
        self.list_of_name = self.list_of_name.loc[self.list_of_name["percent"] > 0.01]["name"].drop_duplicates()
        self.list_of_name = self.list_of_name.reset_index()["name"]

    def get_value(self):
        l = choice(range(1, 4, 1))
        l2 = choice(range(2, 10, 1))

        return \
            (' dot '.join([choice(self.list_of_name) for i in range(l)])).lower() + " at " + \
            (''.join([choice(string.ascii_letters) for i in range(l2)])).lower() + ".com"


print(email_value().get_value())
