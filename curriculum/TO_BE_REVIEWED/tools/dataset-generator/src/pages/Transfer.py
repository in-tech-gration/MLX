from pages.Page import Page
from values.DateValue import date_value
from values.NameValue import name_value
from values.NumericValue import numeric_value


class Transfer(Page):
    def __init__(self):
        super(Page, self).__init__()
        self.NameValue = name_value()
        self.NumericalValue = numeric_value()
        self.DateValue = date_value()

    def resetValues(self):
        self.fieldNames = ["beneficiary name", "beneficiary iban", "beneficiary bank name", "beneficiary BIC",
                           "first name",
                           "last name", "account number", "phone", "date of transfer"]

        self.fieldNamesSynonyms = {}
        self.values = {}
        self.possible_values = {"beneficiary name": self.NameValue.get_value()
            , "beneficiary iban": self.NumericalValue.get_value()
            , "beneficiary bank name": self.NameValue.get_value()
            , "beneficiary BIC": self.NumericalValue.get_value()
            , "first name": self.NameValue.get_value()
            , "last name": self.NameValue.get_value()
            , "account number": self.NumericalValue.get_value()
            , "phone": self.NumericalValue.get_value()
            , "date of transfer": self.DateValue.get_value()}
        self.currnet_page = ""
