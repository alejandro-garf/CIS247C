# Data Types lecture part two

state = "California"
state.find("for")
state.find("a")
state.find("xyz")
print(state)

newState = state.replace("Ca", "Bz")
print(newState)

# String Operations: isDigit and isapha
str = "Hello"
print(str.isalpha())
str = "Hello12"
print(str.isalpha())

str = "1234"
print(str.isdigit())
str = "123b4"
print(str.isdigit())

# Upper
str = "Hello"
print(str.upper())

# Lower
str = "HELLO"
print(str.lower())

# Lists
L = [1, 'List', 23, "b"]
L[1] = 54
print(L)

L = [1, 'List', 23, "b"]
print(L)

MyList = [1, 'List', 23, "b"]
print(len(MyList))
MyList.append("Sup Baby")
print(len(MyList))

## Pop
PopList = [1, 'List', 23, "b"]
PopList.pop()
print(PopList)

## Sort - Note; They must all be a valid operand pair since they are evaluated with an >
List = [1,4,34,14,10,22]
List.sort()
print(List)

# Variable and String Literals
num_sales = 50
print("You have made", num_sales, "sales today!")

#Formatted String Literals
print(f'Hello World')
name = "Alejandro"
print(f"Hello {name}")

# Placeholder Expressions
num = 2
print(f"The answer is {num * 2}")

# Formatting Placeholder Values
total_cost = 500
cost_per_unit = 500/12
print(f"The cost per unit is {cost_per_unit: .2f}")

#Inserting Comma separators
mynetworth = 523450333
print(f"My net worth is {mynetworth:,}")

# Combining format specifiers
monthly_pay = 31242.68
yearly_pay = monthly_pay * 12
print(f"My yearly pay is {yearly_pay:,.2f}")

# Specifying a minimum field width
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.861

print(f'{num1:10.2f} {num2:10.2f}')
print(f'{num3:10.2f} {num4:10.2f}')

