import math as math
import numpy as np
import string
import random

from pages.IssueCC import IssueCC
from pages.OpenAccount import OpenAccount
from pages.Transfer import Transfer
from states.CustomerAnswer import CustomerAnswer
from states.CustomerHold import CustomerHold
from states.CustomerRandomSentence import CustomerRandomSentence
from states.EmployeeQuestion import EmployeeQuestion
from states.EmployeeTermination import EmployeeTermination
from states.Greetings import Greetings
from states.IntentDeclaration import IntentDeclaration
from states.RandomConversation import RandomConversation


class flow:
    def __init__(self):
        self.graph = np.array([
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0.6, 0.1, 0.3, 0],
            [0, 0, 0.95, 0, 0, 0, 0.05],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0]
        ]).T

        # States
        self.Greetings = Greetings()
        self.IntentDeclaration = IntentDeclaration()
        self.EmployeeQuestion = EmployeeQuestion()
        self.CustomerAnswer = CustomerAnswer()
        self.CustomerRandomSentence = CustomerRandomSentence()
        self.CustomerHold = CustomerHold()
        self.RandomConversation = RandomConversation()

        # Pages
        self.IssueCC = IssueCC()
        self.Transfer = Transfer()
        self.OpenAccount = OpenAccount()

    def create_dialogue(self):

        self.IssueCC.resetValues()
        self.Transfer.resetValues()
        self.OpenAccount.resetValues()

        dialogue = ''
        states_map = {0: self.Greetings, 1: self.IntentDeclaration, 2: self.EmployeeQuestion, 3: self.CustomerAnswer,
                      4: self.CustomerRandomSentence, 5: self.CustomerHold, 6: self.RandomConversation}
        pages_map = {"": None, "IssueCC": self.IssueCC, "Transfer": self.Transfer, "OpenAccount": self.OpenAccount}

        current_page = ""
        current_state = np.array([1, 0, 0, 0, 0, 0, 0])
        list_of_values = []
        intent = ""
        while current_page == "" or len(pages_map[current_page].getMissingFields()) > 0:
            # valid_current_states = current_state[current_state != 0]
            c = np.cumsum(current_state) * np.array([math.ceil(x) for x in current_state])
            rand = np.random.uniform(0, 1)
            # rand = 0.3
            position = np.argmax(c > rand)
            # print(current_state)
            current_state = np.zeros(len(current_state))
            current_state[position] = 1
            sentence = states_map[current_state.argmax()].generate_sentence()
            sentence, intent, values = states_map[current_state.argmax()].populate_param(sentence,
                                                                                         pages_map[current_page])
            if intent == "":
                pass
            else:
                current_page = intent
            dialogue = dialogue + sentence
            dialogue = dialogue + ". "
            if values == "":
                pass
            else:
                list_of_values.append(values)
            current_state = np.dot(self.graph, current_state)
        # print(EmployeeTermination().generate_sentence())
        dialogue += (EmployeeTermination().generate_sentence())
        flat_list = [item for sublist in list_of_values for item in sublist]
        return dialogue, intent, flat_list

def generateRandomString(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(n))
# f = flow()
# for i in range(1):
#     dialogue, intent, vals = f.create_dialogue()
#     print(dialogue)
#     print('-----------------------------------------------------------------    ')
#     print(intent)
#     print('-----------------------------------------------------------------    ')
#     print(vals)
#     print('-----------------------------------------------------------------    ')
#     print('-----------------------------------------------------------------    ')
