class Page():
    pages = ["IssueCC", "Transfer", "OpenAccount"]

    def __init__(self):
        self.fieldNames = []
        self.fieldNamesSynonyms = {}
        self.values = {}
        self.possible_values = {}
        self.currnet_page = ""

        # self.fieldvalues = {}4
        pass

    def isRequestCompleted(self):
        return self.fieldNames == self.values.keys()

    def getFirstMissingField(self):
        return self.getMissingFields()[0]

    def getSecondMissingField(self):
        return self.getMissingFields()[1]

    def getFirstMissingAnswer(self, param1):
        # print(self.possible_values)
        return self.possible_values[param1]

    def getMissingFields(self):
        # self.fieldNames - self.values.keys()
        return [item for item in self.fieldNames if item not in self.values.keys()]

    def resetValues(self):
        pass


print(Page.pages)
