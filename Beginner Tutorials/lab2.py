def main():
    MovieName = input("Enter the name of the movie?: ")
    AdultTickets = int(input("How many adult tickets were sold?: "))
    ChildTickets = int(input("How many child tickets were sold?: "))

    ChildTicketPrice = 6
    AdultTicketPrice = 10
    Theatre = .20
    Studio = .80

    AdultRevenue = (AdultTicketPrice * AdultTickets)
    ChildRevenue = (ChildTicketPrice * ChildTickets)
    TotalRevenue = (AdultRevenue + ChildRevenue)

    TheatreProfit = (TotalRevenue * Theatre)
    StudioProfit = (TotalRevenue * Studio)

#I know this is horrible formatting but I wanted to do this without looking anything up and I was short on time because I did this last minute.
    print("Movie Name: ")
    print(MovieName)
    print("\n")

    print("Adult Tickets: ")
    print(AdultTickets)
    print("\n")

    print("Child Tickets: ")
    print(ChildTickets)
    print("\n")

    print("Theatre Profit: ")
    print(TheatreProfit)
    print("\n")

    print("Studio Profit: ")
    print(StudioProfit)
    print("\n")

    print("Gross Profit: ")
    print(TotalRevenue)
    print("\n")

main()
