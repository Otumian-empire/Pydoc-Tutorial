# if and else statements
# chceking if a user input -ve, 0 or +ve
""" print("# chceking if a user input -ve, 0 or +ve")
user_input = int(input("Enter a number: "))

if user_input > 0:
    print(f"user input, {user_input} is positive")
elif user_input < 0:
    print(f"user input, {user_input} is negative")
else:
    print(f"user input, {user_input} is zero") """


# some list to work with
""" mylist = [1, 2, 4, 5, 7] """

# for loop
""" for number in mylist:
    print(number + 1) """

# while loop
""" i = 0
while i < len(mylist):
    print(mylist[i] + 1)
    i += 1 """

# using a map to loop through the iterable
""" list(map(lambda i: print(i+1), mylist)) """

# using a for loop and % to loop thriugh a list
""" for i in mylist:
    if not (i % 2):
        print(f"{i} is a multiple of 2")
    else:
        print(f"{i} not is a multiple of 2") """

# An actual v ersion of the above code
""" for i in mylist:
    if i % 2 == 0:
        print(f"{i} is a multiple of 2")
    else:
        print(f"{i} not is a multiple of 2") """

# looping with range and len
""" for number in range(len(mylist)):
    print(number + 1) """
