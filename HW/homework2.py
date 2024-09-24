def main():
    print("Hello! Welcome to my Bookstore Rewards Program!\n")
    input("Press Enter to continue....\n")

    # Constants for tax rate & discount for paid members
    TAX_RATE = 0.0925
    DISCOUNT_RATE = 0.10

    # Initializing total earnings and points
    total_earnings = 0.0
    total_points = 0

    while True:
        # Display options for the user
        print("Bookstore Rewards Program")
        print("1. Enter a new customer sale")
        print("2. See total earnings")
        print("3. Quit")

        option = input("Please select an option (1-3): ")

        if option == '1':
            # New customer sale option
            try: # Getting user input
                print("\nNew Sale:")
                num_books = int(input("Number of books: "))
                price_per_book = float(input("Price per book ($): "))

                # Get membership status
                print("\nMember status:")
                print("1. Non-Member")
                print("2. Free Member")
                print("3. Paid Member")
                membership_option = input("Enter your choice (1-3): ")

                # Set member status and discount based on input
                if membership_option == '1':
                    member_status = "Non-Member"
                    discount = 0.0  # Non-members get no discount
                elif membership_option == '2':
                    member_status = "Free Member"
                    discount = 0.0  # Free members also get no discount
                elif membership_option == '3':
                    member_status = "Paid Member"
                    discount = DISCOUNT_RATE  # Paid members get 10% discount
                else:
                    print("Invalid membership selection.")  # Handle invalid membership input
                    continue  # Return to the main menu

                input("Press Enter to calculate....\n")  # Wait for user before calculating

                # Calculate the total sale amount before applying discount
                sale_total = num_books * price_per_book

                # Apply discount if applicable
                discount_amount = sale_total * discount  # Discount for paid members
                sale_total_after_discount = sale_total - discount_amount  # Final sale amount after discount

                # Apply tax
                tax_amount = sale_total_after_discount * TAX_RATE  # Calculate the tax
                final_price = sale_total_after_discount + tax_amount  # Final price after tax

                # Update the total earnings with the final price
                total_earnings += final_price

                # Calculate points earned based on membership status and number of books
                if member_status == "Non-Member":
                    points_earned = 0  # Non-members earn no points
                elif member_status == "Free Member":
                    points_earned = calculate_points(num_books, "Free Member")
                else:
                    points_earned = calculate_points(num_books, "Paid Member")
                total_points += points_earned  # Update total points

                # Show the sale summary to the user
                print("\nSale Recorded!")
                print(f"Final Price (with tax): ${final_price:.2f}")  # Display final price
                print(f"Points Earned: {points_earned}")  # Display points earned

            except ValueError:
                print("Invalid input. Please enter valid numbers for the sale.")  # Handle input errors

        elif option == '2':
            # Display total earnings and total points
            print(f"\nTotal money earned today: ${total_earnings:.2f}")
            print(f"Total points earned today: {total_points}")

        elif option == '3':
            # Quit the program and show final earnings and points
            print(f"\nExiting the program. Total money earned today: ${total_earnings:.2f}")
            print(f"Total points earned today: {total_points}")
            break  # Exit the loop and end the program

        else:
            print("Invalid option. Please choose 1, 2, or 3.")  # Handle invalid menu input


# Function to calculate points based on membership status and number of books
def calculate_points(num_books, membership_status):
    # Free member point system
    if membership_status == "Free Member":
        if num_books == 1:
            return 5  # 5 points for 1 book
        elif num_books == 2:
            return 15  # 15 points for 2 books
        elif num_books == 3:
            return 30  # 30 points for 3 books
        else:
            return 60  # 60 points for 4 or more books

    # Paid member point system
    elif membership_status == "Paid Member":
        if num_books == 1:
            return 5  # 5 points for 1 book
        elif num_books == 2:
            return 15  # 15 points for 2 books
        elif num_books == 3:
            return 50  # 50 points for 3 books
        else:
            return 100  # 100 points for 4 or more books


# Run the program
main()
