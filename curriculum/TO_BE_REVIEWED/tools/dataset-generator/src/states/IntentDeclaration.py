import math as math
import numpy as np

import pages.Page as P
from states.State import State


class IntentDeclaration(State):
    list_of_samples = ["i want to PARAM1", "i would like to PARAM1", "i am here for PARAM1", "i am here to PARAM1",
                       "i am interested in PARAM1", "i came to PARAM1"]

    def __init__(self):
        pass

    def populate_param(self, sentence, page=""):
        params1 = P.Page.pages
        param1 = ""
        if len(params1) > 0 and "PARAM1" in sentence:
            i = np.random.uniform(0, len(params1))
            i = (math.floor(i))
            param1 = params1[i]
            sentence = sentence.replace("PARAM1", param1)
        return sentence, param1, ""

        return super().populate_param(sentence, )
