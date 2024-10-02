def main():
    print("Welcome! Please enter your full name.")

    full_name = input("Enter your name: ").strip() ##Looked this up


    if " " in full_name:
        first_name, last_name = full_name.split(' ', 1) #Looked this up as well
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")
    else:
        print("Invalid Input: Name format must include a space.")

main()

## Don't feel great because I had to look most of this up but still learned
