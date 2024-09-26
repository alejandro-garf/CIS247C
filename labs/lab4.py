def main():
    print("Hello! Welcome to my store sales enterprise data analysis software.\n")
    input("Press Enter to continue....\n")

    # Get number of stores
    while True:
        try:
            num_stores = input("Enter the number of stores to collect data for (between 1 and 10): ")
            num_stores = int(num_stores)

            if 1 <= num_stores <= 10:
                print(f"\nYou will now enter sales data for {num_stores} stores.\n")
                break
            else:
                print("Please enter a number between 1 and 10.\n")
        except ValueError as e:
            print(f"Invalid input: {e}\n")

    # Collect sales data for all stores
    store_sales = []
    for i in range(1, num_stores + 1):
        while True:
            try:
                # Prompt for sales input, convert to integer
                sales = input(f"Enter today's sales for store {i}: ")
                sales = int(sales)
                store_sales.append(sales)
                break
            except ValueError:
                # Display the custom message for sales input
                print("Invalid input: All inputs must be integers.\n")

    input("\nPress Enter to show the sales bar chart....\n")

    # sales chart
    print("\nSALES BAR CHART (Each * = $100):")
    for i in range(1, num_stores + 1):
        stars = '*' * (store_sales[i - 1] // 100)  # 1 star for every $100
        print(f"Store {i}: {stars}")

    print("\nThank you for using my program!")

# Run the program
main()
