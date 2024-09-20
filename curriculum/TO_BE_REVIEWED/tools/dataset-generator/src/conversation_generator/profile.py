from values.NameValue import name_value
from values.AddressValue import address_value
from values.CompanyValue import company_value
from values.DateValue import date_value
from values.EmailValue import email_value
from values.NumericValue import numeric_value


class CustomerProfileGenerator:
    def __init__(self):
        self.names = name_value()
        self.addresses = address_value()
        self.companies = company_value()
        self.dates = date_value()
        self.emails = email_value()
        self.numbers = numeric_value()

    def generateProfile(self):
        return {
            "first name": self.names.get_value(),
            "last name": self.names.get_value(),
            "phone number": self.numbers.get_value(),
            "mobile number": self.numbers.get_value(),
            "email": self.emails.get_value(),
        }
