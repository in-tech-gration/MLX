from random import choice

import pandas as pd


class company_value:
    def __init__(self):
        self.list_of_name = pd.read_csv("../companies.csv", error_bad_lines=False)
        self.list_of_name = self.list_of_name.iloc[:, 1]

    def get_value(self):
        return choice(self.list_of_name)


print(company_value().get_value())
