# Alejandro Fonseca
from date import Date
from event import Event

def main():
    # List to store all our events
    all_events = []

    # Keep running until the user wants to quit
    while True:
        # Show the menu
        print("\nWhat would you like to do?")
        print("1. Add a new event")
        print("2. Cancel an event")
        print("3. See all events")
        print("4. Quit")

        # Get the user's choice
        choice = input("Type a number (1-4): ")

        # Add a new event
        if choice == "1":
            # Get all the info from the user
            name = input("What's the name of the event? ")

            # Get the date info
            month = int(input("What month? (1-12) "))
            day = int(input("What day? (1-31) "))
            year = int(input("What year? "))

            # Get the time info
            start = int(input("What hour does it start? (0-23) "))
            end = int(input("What hour does it end? (0-23) "))

            # Make a new date and event
            event_date = Date(day, month, year)
            new_event = Event(name, start, end, event_date)

            # Check if it overlaps with any other events
            can_add = True
            for event in all_events:
                if new_event.has_overlap(event):
                    print("\nSorry, this overlaps with:")
                    print(event.print_event())
                    can_add = False
                    break

            # Add it if there's no overlap
            if can_add:
                all_events.append(new_event)
                print("\nOkay, event added!")

        # Cancel an event
        elif choice == "2":
            name = input("What's the name of the event to cancel? ")
            # Look through all events
            found = False
            for event in all_events:
                if event.name == name:
                    all_events.remove(event)
                    print("\nOkay, event cancelled!")
                    found = True
                    break
            if not found:
                print("\nCouldn't find that event!")

        # Show all events
        elif choice == "3":
            if len(all_events) == 0:
                print("\nNo events yet!")
            else:
                print("\nHere are all the events:")
                for event in all_events:
                    print("\n" + event.print_event())

        # Quit the program
        elif choice == "4":
            print("\nGoodbye!")
            break

        # Invalid choice
        else:
            print("\nThat's not a valid choice!")


if __name__ == "__main__":
    main()