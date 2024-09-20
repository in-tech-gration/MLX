import numpy as np

from states.State import State


class Greetings(State):
    sentence_1 = ["hi", "hello", "good morning",
                  "good afternoon", "good evening"]

    sentence_2 = ["how are you", "how are you today",
                  "how is it going", "how do you do",
                  ]
    sentence_2_reply = [
        "i am fine ", "fine ", "thank you",
        "doing great", "thanks"]
    sentence_3 = ["what about you? \n fine thank you "]
    sentence_last = ["Welcome to our bank, what can i do for you",
                     "what can i do for you",
                     "how can i help you",
                     "how may i assist you"]

    def __init__(self):
        pass

    def generate_sentence(self):
        conv = ""
        conv += self.generate_from_list(self.sentence_1) + "\n"
        conv += conv
        if np.random.uniform(0, 1) > 0.5:
            conv += self.generate_from_list(self.sentence_2) + "\n"
            conv += self.generate_from_list(self.sentence_2_reply) + "\n"
        conv += self.generate_from_list(self.sentence_last)
        return conv

    def populate_param(self, sentence, page=""):
        return sentence, "", ""
        # print(Greetings().generate_sentence())
