# Alejandro Fonseca - Contact Book
import csv

# List to store all contacts
contacts = []


# Function to add a new contact
def add_contact():
    print("\nAdd a new contact:")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    # Make a dictionary for the new contact
    new_contact = {}
    new_contact["name"] = name
    new_contact["phone"] = phone
    new_contact["email"] = email
    new_contact["address"] = address

    # Add the contact to our list
    contacts.append(new_contact)

    # Save to file
    save_to_file()
    print("Contact was added!")


# Function to show all contacts
def show_contacts():
    print("\nAll Contacts:")
    print("-------------")

    # Check if we have any contacts
    if len(contacts) == 0:
        print("No contacts found!")
        return

    # Print each contact
    for i in range(len(contacts)):
        contact = contacts[i]
        print(f"Contact #{i}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print("-------------")


# Function to delete a contact
def delete_contact():
    show_contacts()

    if len(contacts) == 0:
        return

    # Ask which contact to delete
    try:
        number = input("\nEnter contact number to delete: ")
        number = int(number)

        # Make sure the number is valid
        if number >= 0 and number < len(contacts):
            # Remove the contact
            contacts.pop(number)
            save_to_file()
            print("Contact deleted!")
        else:
            print("Invalid contact number!")
    except:
        print("Please enter a valid number!")


# Function to save contacts to file
def save_to_file():
    file = open('contacts.csv', 'w', newline='')
    writer = csv.writer(file)

    # Write headers first
    writer.writerow(['name', 'phone', 'email', 'address'])

    # Write each contact
    for contact in contacts:
        writer.writerow([contact['name'], contact['phone'], contact['email'], contact['address']])

    file.close()


# Function to load contacts from file
def load_from_file():
    try:
        file = open('contacts.csv', 'r', newline='')
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Read each contact
        for row in reader:
            contact = {}
            contact['name'] = row[0]
            contact['phone'] = row[1]
            contact['email'] = row[2]
            contact['address'] = row[3]
            contacts.append(contact)

        file.close()
    except:
        # If file doesn't exist, add some example contacts
        add_example_contacts()


# Function to add example contacts
def add_example_contacts():
    # First example contact
    contact1 = {}
    contact1["name"] = "Alan Turing"
    contact1["phone"] = "5551122334"
    contact1["email"] = "alan.turing@example.com"
    contact1["address"] = "123 Turing Lane"
    contacts.append(contact1)

    # Second example contact
    contact2 = {}
    contact2["name"] = "Grace Hopper"
    contact2["phone"] = "5554433221"
    contact2["email"] = "grace.hopper@example.com"
    contact2["address"] = "234 Hopper Ave"
    contacts.append(contact2)

    # Third example contact
    contact3 = {}
    contact3["name"] = "Ada Lovelace"
    contact3["phone"] = "5556677889"
    contact3["email"] = "ada.lovelace@example.com"
    contact3["address"] = "345 Ada St"
    contacts.append(contact3)

    # Save these contacts to file
    save_to_file()


# Main program starts here
print("Welcome to Contact Manager!")

# Load any existing contacts
load_from_file()

# Main program loop
while True:
    # Show menu
    print("\nWhat would you like to do?")
    print("1. Add a contact")
    print("2. Show all contacts")
    print("3. Delete a contact")
    print("4. Quit")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

    # Do what the user asked for
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid choice (1-4)")