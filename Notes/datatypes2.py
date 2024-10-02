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
