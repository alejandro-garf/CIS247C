def main():
    # User Inputs
    adult_tickets_sold = input("How many adult tickets were sold?: ")
    child_tickets_sold = input("How many child tickets were sold?: ")

    # Conversion
    adult_tickets_sold = int(adult_tickets_sold)

    print("The amount of adult tickets sold: " + str(adult_tickets_sold) + " And the amount of child tickets sold: " + str(child_tickets_sold))


if __name__ == "__main__":
    main()