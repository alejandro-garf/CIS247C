def main():
    print("Hello! Welcome to my program where we add two integers together.")
    Int1 = (input ("Integer One: "))
    Int2 = (input ("Integer Two: "))

    input("Press Enter to caclulate....\n")

## looked this up
    try:
        Int1 = int(Int1)
        Int2 = int(Int2)

        sum = Int1 + Int2
        print(f"The sum of {Int1} and {Int2} is {sum}.")
    except ValueError:
        print("INVALID: Both inputs must be integers")

#Originally I tried doing this but it didn't work.
'''
    if type(Int1) is int:
        sum = Int1 + Int2
        print(f"The sum of {Int1} and {Int2} is {sum}." )
    else:
        print("INVALID: Both inputs must be integers")
    return
'''

main()