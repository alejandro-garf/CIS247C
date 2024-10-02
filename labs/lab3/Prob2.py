def main():
    print("Hello! Welcome to my program where we calculate the average grade.")

    try:
        grade1_input = input("Grade One: ")
        grade1 = float(grade1_input)

        grade2_input = input("Grade Two: ")
        grade2 = float(grade2_input)

        grade3_input = input("Grade Three: ")
        grade3 = float(grade3_input)

        input("Press Enter to caclulate....\n")

        if 0 <= grade1 <= 100 and 0 <= grade2 <= 100 and 0 <= grade3 <= 100:
            average = (grade1 + grade2 + grade3) / 3
            formatted_average = round(average, 2)

    # I feel like there is a better way to do this but this is how I did it without looking it up
            if average > 90 and average < 100:
                        grade = "A"
                        print(f"Your average score is {formatted_average}, and your grade is {grade}")
            elif average > 80 and average < 90:
                        grade = "B"
                        print(f"Your average score is {formatted_average}, and your grade is {grade}")
            elif average > 70 and average < 80:
                        grade = "C"
                        print(f"Your average score is {formatted_average}, and your grade is {grade}")
            elif average > 60 and average < 70:
                        grade = "D"
                        print(f"Your average score is {formatted_average}, and your grade is {grade}")
            elif average < 60:
                        grade = "F"
                        print(f"Your average score is {formatted_average}, and your grade is {grade}")
        else:
            print("All scores must be between 0 and 100")

## Had to look up this part and it still took me a while lol, I still don't really understand it so will study
    except ValueError:
        # Check which input was invalid
        if 'grade1' not in locals():
            invalid_input = grade1_input
        elif 'grade2' not in locals():
            invalid_input = grade2_input
        else:
            invalid_input = grade3_input

        print(f"INVALID: Could not convert string to float: '{invalid_input}'.")


main()