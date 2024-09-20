from pages.Page import Page
from values.AddressValue import address_value
from values.DateValue import date_value
from values.EmailValue import email_value
from values.NameValue import name_value
from values.NumericValue import numeric_value
from values.CompanyValue import company_value


class OpenAccount(Page):
    def __init__(self):
        super(Page, self).__init__()

        self.NameValue = name_value()

        self.NumericalValue = numeric_value()
        self.EmailValue = email_value()
        self.AddressValue = address_value()
        self.DateValue = date_value()
        self.CompanyValue = company_value()

        pass

    def resetValues(self):
        self.fieldNames = [
            "first name", "last name", "account number", "id number", "email", "address", "phone", "monthly income",
            "employer", "job", "marital status", "date of birth", "type of account"]

        self.fieldNamesSynonyms = {}
        self.values = {}
        self.possible_values = {"first name": self.NameValue.get_value(), "last name": self.NameValue.get_value(),
                                "account number": self.NumericalValue.get_value(),
                                "id number": self.NumericalValue.get_value(),
                                "email": self.EmailValue.get_value(), "address": self.AddressValue.get_value(),
                                "phone": self.NumericalValue.get_value(),
                                "monthly income": self.NumericalValue.get_value(),
                                "employer": self.CompanyValue.get_value(), "job": self.NameValue.get_value(),
                                "marital status": self.NameValue.get_value(),
                                "date of birth": self.DateValue.get_value(),
                                "type of account": self.NameValue.get_value()}
        self.currnet_page = ""
