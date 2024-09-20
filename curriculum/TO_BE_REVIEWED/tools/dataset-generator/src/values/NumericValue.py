import numpy as np


class numeric_value:

    def get_value(self):
        return str(int(round(np.random.rand() * 9999999999999, 0)))


print(numeric_value().get_value())
