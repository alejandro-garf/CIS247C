def main():
    ## Intro Stuff
    print("Hello welcome to my program that does house comparisons!\n")
    print("I will need a lot of data from you so please be patient and make sure the data you input is correct.")
    input("Press Enter to continue....\n")

    ## Get info
    print("House 1:\n")
    Adress1 = input("Address: ")
    SqFoot1 = float (input("Square Footage: "))
    Price1 = float (input("Price: "))
    taxr1= float (input("Tax rate(%): "))

    print("\n")

    print("House 2:\n")
    Adress2 = input("Address: ")
    SqFoot2 = float (input("Square Footage: "))
    Price2 = float (input("Price: "))
    taxr2 = float (input("Tax rate(%): "))

    print("\n")

    input("Press Enter to caclulate....\n")  ##Calculations below

    ## Turn int into decimal to represent percentage for House One(I looked this up)
    taxpct1 = taxr1 / 100
    ## Find out the total tax
    tax1 = taxpct1 * Price1
    ## Add it onto the price
    totalprice1 = tax1 + Price1

    taxpct2 = taxr2 / 100
    tax2 = taxpct2 * Price2
    totalprice2 = tax2 + Price2

    ## Find the price per square foot
    FootPrice1 = totalprice1 / SqFoot1
    FootPrice2 = totalprice2 / SqFoot2



    ## Print the answers
    print("House 1:")
    print(f"Price After Tax: ${totalprice1:.2f}") ##Looked up how to do this
    print(f"Price Per Square Foot: ${FootPrice1:.2f}\n")

    print("House 2:")
    print(f"Price After Tax: ${totalprice2:.2f}")
    print(f"Price Per Square Foot: ${FootPrice2:.2f}\n")

    if FootPrice2 == FootPrice1:
        print("Both Houses are the same price")
    elif FootPrice2 > FootPrice1:
        print("House 1 is cheaper")
    else:
        print("House 2 is cheaper")


main()