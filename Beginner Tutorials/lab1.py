 # Lab One by Alejandro Fonseca


print("Hello, welcome to my first lab in CIS 247, this is a simple calculator program\n")

def main():
    length = input("Enter the length of the rectangle: ") #Searched up how to take input
    width = input("Enter the width of the rectangle: ")

    #searched this up as well because I kept getting "can't multiply by non int of type str"
    length = float(length)
    width = float(width)
    area = length * width

    print("The area of the rectangle is: ")
    print(area)


main()