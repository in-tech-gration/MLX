import math as math
import numpy as np


class State:
    list_of_samples = ["excuse me", "pardon", "come again", "sorry", "what"]

    def __init__(self):
        pass

    def generate_sentence(self, *argv):
        return self.generate_from_list(self.list_of_samples)

    def generate_from_list(self, list_of_samples, *params1):
        num_of_samples = len(list_of_samples)

        i = np.random.uniform(0, num_of_samples)
        i = (math.floor(i))
        sentence = list_of_samples[i]
        return sentence

    # def populate_param(self, sentence, params1, param_name="PARAM1"):
