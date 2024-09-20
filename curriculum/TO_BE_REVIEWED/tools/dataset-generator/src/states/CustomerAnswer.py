from states.State import State


class CustomerAnswer(State):
    list_of_samples = ["my PARAM1 is PARAM2", "PARAM2 ", "my PARAM1 is PARAM2 and my PARAM3 is PARAM4", "it is PARAM2",
                       "stated as PARAM2"]

    def __init__(self):
        pass

    def populate_param(self, sentence, page):
        list_of_values = []
        param1 = page.getFirstMissingField()
        sentence = sentence.replace("PARAM1", param1)
        param2 = page.getFirstMissingAnswer(param1)
        sentence = sentence.replace("PARAM2", param2)
        page.values[param1] = param2
        list_of_values.append([param1, param2])
        if "PARAM3" in sentence and "PARAM4" in sentence and len(page.getMissingFields()) > 0:
            param1 = page.getFirstMissingField()
            sentence = sentence.replace("PARAM3", param1)
            param2 = page.getFirstMissingAnswer(param1)
            sentence = sentence.replace("PARAM4", param2)
            page.values[param1] = param2
            list_of_values.append([param1, param2])
        else:
            sentence = sentence.replace("and my PARAM3 is PARAM4", "")
        return sentence, "", list_of_values
