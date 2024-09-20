from random import choice


class date_value:

    def get_value(self):
        l = choice(range(2, 18, 1))
        l2 = choice(range(2, 10, 1))
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        return str(choice(range(1, 30, 1))) + " " + str(choice(months)) + " " + str(choice(range(1955, 2020, 1)))


print(date_value().get_value())
