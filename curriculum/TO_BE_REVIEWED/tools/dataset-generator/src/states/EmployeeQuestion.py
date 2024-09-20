from states.State import State


class EmployeeQuestion(State):
    catalogue = {
        'personal_names': ["what can i call you", "may i ask you for your PARAM1", "what is your PARAM1 sir"],
        'past_date': [],
        'future_date': [],
        'job_location': [],
        'job_income': [],
        'validation': []
    }
    list_of_samples = ["what is PARAM1", "what about PARAM1", "would you provide your PARAM1 ",
                       "can you read me your PARAM1", "tell me your PARAM1", "now the PARAM1",
                       "can you supply me with your PARAM1", "may i ask you for your PARAM1", "we need your PARAM1",
                       "as for PARAM1", "next PARAM1", "PARAM1"]

    def __init__(self):
        pass

    def populate_param(self, sentence, page):
        param1 = page.getFirstMissingField()
        sentence = sentence.replace("PARAM1", param1)
        return sentence, "", ""
