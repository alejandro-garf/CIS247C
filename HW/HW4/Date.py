# Alejandro Fonseca
# Class that keeps track of dates
class Date:
    def __init__(self, d, m, y):
        # These are instance variables that store the date info
        self.day = d  # the day of the month
        self.month = m  # which month it is
        self.year = y  # what year it is

    # Function that checks if two dates are the same
    def is_same_date(self, other_date):
        if self.day == other_date.day and self.month == other_date.month and self.year == other_date.year:
            return True
        else:
            return False

    # Prints out the date
    def print_date(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)