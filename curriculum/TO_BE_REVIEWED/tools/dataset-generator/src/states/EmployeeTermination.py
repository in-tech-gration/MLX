from states.State import State


class EmployeeTermination(State):
    sentence_1 = ["So, is that all for today", "Have we handled all your issues today", "are there any more questions",
                  "have we answered all your questions ", "do you have any other question",
                  ]

    sentence_2 = ["thank you very much", "no that was all"
        , "thanks for your help"
        , "all good"
        , "no you have answered all my questions"
                  ]

    sentence_3 = ["have a nice day", "looking forward to see you again "
        , "see you again "]

    def __init__(self):
        pass

    def generate_sentence(self):
        conv = ""
        conv += self.generate_from_list(self.sentence_1) + "\n"
        conv += self.generate_from_list(self.sentence_2) + "\n"
        conv += self.generate_from_list(self.sentence_3) + "\n"
        return conv

    def populate_param(self, sentence, page=""):
        return sentence, "", ""
        # print(Greetings().generate_sentence())
