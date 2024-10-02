import random

def compare(value):
    try:
        correct_value = value
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < 1 or guess > 10:
            raise ValueError("The guess must be between 1 and 10")
        elif guess > correct_value:
            print("The guess is too high, try again!")
        elif guess < correct_value:
            print("The guess is too low, try again!")
        else:
            print("The guess is correct! Congrats!")
        return False
    except ValueError as ve:
        print(ve)
        return False

random_value = random.randint(1,10)
while True:
    if compare(random_value):
        break