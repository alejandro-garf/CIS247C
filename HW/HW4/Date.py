class Date:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        if 1 <= value <= 31:
            self._day = value
        else:
            raise ValueError("Day must be between 1 and 31")

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        if 1 <= value <= 12:
            self._month = value
        else:
            raise ValueError("Month must be between 1 and 12")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value >= 0:
            self._year = value
        else:
            raise ValueError("Year cannot be negative")

    def __str__(self):
        return f"{self._month}/{self._day}/{self._year}"

    def __eq__(self, other):
        if isinstance(other, Date):
            return (self._day == other.day and
                    self._month == other.month and
                    self._year == other.year)
        return False