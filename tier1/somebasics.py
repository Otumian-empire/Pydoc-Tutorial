# An informal introduction to variables, operations and data types
""" print("# variables")
var_name = "I am a variable with an str value"
print(var_name, end="\n\n") """


# calculate the area of a rectangle of length, 10cm and breadth, 6cm
""" print(f"# calculating the area of a rectangle of length, 10cm and breadth, 6cm")
length = 10
breadth = 5
area = length * breadth
print(
    f"The area of reactangle of length, {length}cm and breadth, {breadth}cm is {area}cm^2", end="\n\n") """

# calculate a give number to the power of 3
""" print("# calculating a give number to the power of 3")
given_number = int(input('Enter the number: '))
result = given_number ** 3
print(f"{given_number} raised to the exponent 3 is {result}", end="\n\n")
 """
# implement divmod, a function that returns the quotient and remainder of two given numbers, x and y
# where x and y are not less that 1
""" print(f"# implement divmod, a function that returns the quotient and remainder of two given numbers, x and y")
print(f"# where x and y are not less that 1")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

quotient = first_number // second_number
remainder = first_number % second_number

mydivmod = (quotient, remainder)
print(
    f"The divmod of {first_number} and {second_number} is {mydivmod}", end="\n\n") """

# printing the content of a string by slicing
""" print("# printing the content of a string by slicing")
word = input('Enter a string: ')
for char in word:
    print(char, ord(char), word[word.index(char):])

print(f"the word which you entered was {word}", end="\n\n") """

# list and its all
""" mylist = [1]
mylist.append('Hello world')
print(mylist)
map(print, mylist) """

# fib
""" a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b """
