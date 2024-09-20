from states.State import State


class CustomerHold(State):
    list_of_samples = ["hold on", "one second", "one moment let me find it for you", "let me remember",
                       "let me think about that", "hold on i cant find it here it is"]

    def __init__(self):
        pass

    def populate_param(self, sentence, page=""):
        return sentence, "", ""
        # print(Greetings().generate_sentence())
