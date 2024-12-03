# Alejandro Fonseca

from date import Date

# Class keeps track of events at the convention center
class Event:
    def __init__(self, name, start, end, date):
        # Check if the times are valid before saving them
        if start < 0 or start > 23:
            print("Error: start time must be between 0 and 23")
            return
        if end < 0 or end > 23:
            print("Error: end time must be between 0 and 23")
            return
        if end <= start:
            print("Error: end time must be after start time")
            return

        # Save all the info about the event
        self.name = name  # name of the event
        self.start_time = start  # when it starts (in 24-hour time)
        self.end_time = end  # when it ends (in 24-hour time)
        self.date = date  # what day it happens

    # Checks if two events happen at the same time
    def has_overlap(self, other_event):
        # First check if they're on the same day
        if self.date.is_same_date(other_event.date):
            # Check if the times overlap
            if self.start_time < other_event.end_time and self.end_time > other_event.start_time:
                return True
        # If we get here, there's no overlap
        return False

    # Prints out all the event info
    def print_event(self):
        return "Event: " + self.name + "\nDate: " + self.date.print_date() + \
            "\nTime: " + str(self.start_time) + ":00 to " + str(self.end_time) + ":00"