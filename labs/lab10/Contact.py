# Contact.py
#Alejandro Fonseca

# this class holds info about one person in our contacts
class Contact:
    def __init__(self, name, email=None):
        # store their basic info
        # use _ to show these shouldn't be changed directly
        self._name = name
        self._email = email
        # start with empty list of phone numbers
        self._phone_numbers = []

    # these let us safely get and set the name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    # these let us safely get and set the email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email

    # this lets us safely get the phone numbers
    @property
    def phone_numbers(self):
        return self._phone_numbers

    def add_number(self, new_number):
        # check if they already have this number
        if new_number in self._phone_numbers:
            print("That number is already saved for this person!")
        else:
            # if not, add it to their numbers
            self._phone_numbers.append(new_number)

    def remove_number(self, num_to_remove):
        # try to remove the number
        if num_to_remove in self._phone_numbers:
            self._phone_numbers.remove(num_to_remove)
            print("OK, removed that number!")
        else:
            print("They don't have that number!")

    def __str__(self):
        # start with their name
        info = "Name: " + self._name + "\n"

        # add their phone numbers if they have any
        if len(self._phone_numbers) > 0:
            info += "Phone Numbers: "
            # add each number with a space after it
            for num in self._phone_numbers:
                info += num + " "
            info += "\n"

        # add their email if they have one
        if self._email is not None:
            info += "Email: " + self._email
            info += "\n"

        return info