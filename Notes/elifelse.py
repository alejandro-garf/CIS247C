
correct_value = 5
guess = int(input("Guess a number between 1 and 10: "))

if guess < 1 or guess > 10:
    print("The guess must be between 1 and 10")
elif guess > correct_value:
    print("The guess is too high, try again!")
elif guess < correct_value:
    print("The guess is too low, try again!")
else:
    print("The guess is correct! Congrats!")

