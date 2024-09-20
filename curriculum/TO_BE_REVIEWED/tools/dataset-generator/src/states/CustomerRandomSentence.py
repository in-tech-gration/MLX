from states.State import State


class CustomerRandomSentence(State):
    list_of_samples = ["excuse me", "pardon", "come again", "sorry", "what"]

    def __init__(self):
        pass

    def populate_param(self, sentence, page=""):
        return sentence, "", ""
        # print(Greetings().generate_sentence())
