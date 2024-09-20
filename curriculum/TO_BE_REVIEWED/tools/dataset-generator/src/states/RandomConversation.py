import random
from xml.dom import minidom

from states.State import State


class RandomConversation(State):
    def __init__(self):
        corpus = minidom.parse('../corpus/Avatar_eng.xml')
        self.sentences = corpus.getElementsByTagName('text')
        self.corpusSize = len(self.sentences)
        self.maxSentences = 30
        self.minSentences = 10
        pass

    def generate_sentence(self):
        startIndex = random.randint(0, self.corpusSize - self.maxSentences)
        sentenceSize = random.randint(self.minSentences, self.maxSentences)

        conv = ""
        for i in range(sentenceSize):
            conv += self.sentences[startIndex + i].firstChild.nodeValue + " "

        conv = conv.strip()
        conv = conv[:len(conv)]
        return conv

    def populate_param(self, sentence, page=""):
        return sentence, "", ""
        # print(Greetings().generate_sentence())
