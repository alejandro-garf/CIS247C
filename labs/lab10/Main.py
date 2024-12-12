# Main.py
#Alejandro Fonseca

# get the Contact class from our other file
from Contact import *
import pickle


def load_contacts():
    # try to open our save file and get the contacts
    try:
        file = open("myfile.dat", "rb")
        contact_list = pickle.load(file)
        file.close()
    # if we can't find the file, start with empty contacts
    except FileNotFoundError:
        contact_list = {}

    return contact_list


def save_contacts(contacts):
    # save all our contacts to a file
    file = open("myfile.dat", "wb")
    pickle.dump(contacts, file)
    file.close()


def add_contact(contacts):
    # ask for the new person's info
    print("Adding a New Contact\n")

    # get their name
    name = input("Name: ")
    # make sure we don't already have someone with that name
    if name in contacts:
        print("There is already a contact with that name")
        return

    # get their email (they don't have to give one)
    email = input("Email (leave empty to skip): ")

    # make a new contact with or without email
    if email == "":
        new_person = Contact(name)
    else:
        new_person = Contact(name, email)

    # keep asking for phone numbers until they're done
    while True:
        num = input("Enter a phone number (or 'q' to stop): ")
        # if they type q, stop asking for numbers
        if num == 'q':
            break
        # add the number to their contact
        new_person.add_number(num)

    # add the new person to our contacts
    contacts[name] = new_person


def lookup(contacts):
    # ask who they want to look up
    name = input("Enter a name: ")
    # if we found them, show their info
    if name in contacts:
        print(contacts[name])
    # if we didn't find them, let them know
    else:
        print("Contact not found")


def delete(contacts):
    # ask who they want to delete
    name = input("Enter the name of the contact to delete: ")
    # if we found them, delete them
    if name in contacts:
        contacts.pop(name)
    # if we didn't find them, let them know
    else:
        print("Contact not found")


def edit(contacts):
    # get the name of contact to edit
    print("Who do you want to edit?")
    name = input()

    # check if we found them
    if name in contacts:
        done = False
        # keep editing until they want to stop
        while not done:
            print("\nWhat do you want to do?")
            print("1 - take away a phone number")
            print("2 - add a phone number")
            print("3 - change their email")
            print("4 - change their name")
            print("5 - done editing")

            # get their choice
            choice = input("Pick a number: ")

            # remove a phone number
            if choice == "1":
                # first check if they have any numbers
                if len(contacts[name].phone_numbers) == 0:
                    print("They don't have any numbers!")
                else:
                    # show all the numbers
                    print("Here are their numbers:")
                    i = 1
                    for num in contacts[name].phone_numbers:
                        print(str(i) + ": " + num)
                        i = i + 1
                    number = input("Which number do you want to remove? ")
                    contacts[name].remove_number(number)

            # add a new number
            elif choice == "2":
                new_num = input("Type the new number: ")
                contacts[name].add_number(new_num)

            # change email
            elif choice == "3":
                new_email = input("Type the new email: ")
                contacts[name].email = new_email
                print("OK, email is changed!")

            # change their name
            elif choice == "4":
                new_name = input("What's their new name? ")
                # make sure new name isn't taken
                if new_name in contacts:
                    print("Someone already has that name!")
                else:
                    # save the contact info
                    temp = contacts[name]
                    # remove old name from contacts
                    contacts.pop(name)
                    # change their name
                    temp.name = new_name
                    # put them back in contacts with new name
                    contacts[new_name] = temp
                    # update the name variable for the loop
                    name = new_name
                    print("OK, changed their name!")

            # stop editing
            elif choice == "5":
                done = True

            # they typed something wrong
            else:
                print("That's not a choice! Pick 1-5")
    else:
        print("Couldn't find anyone named", name)


def main():
    # load all our saved contacts
    contacts = load_contacts()

    # keep showing menu until they want to quit
    while True:
        # show them their choices
        choice = int(input("1) Add a contact\n2) Lookup a Contact\n3) Delete a Contact\n4) Edit a Contact\n5) Quit "))

        # do what they picked
        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            lookup(contacts)
        elif choice == 3:
            delete(contacts)
        elif choice == 4:
            edit(contacts)
        elif choice == 5:
            break
        else:
            print("That's not a choice!")

    # save all our contacts before quitting
    save_contacts(contacts)


# start the program
main()