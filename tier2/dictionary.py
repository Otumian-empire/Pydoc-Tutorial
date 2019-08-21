# dictionary is like a list is like a set in particular
# also known as associative memories or associative arrays
# a dictionary is kind of set of key: value pairs

# an empty dictionary
empty_dic = {}
print(empty_dic)

# initializing a dictionary
mydic = {
    'name': 'John Doe',
    'email': 'JohnD122@gmail.com',
    'hobby': 'web designing with wix',
    'profession': ['freelance web designing', 'e-marketing'],
    'age': 34,
    'status': ['single', 'ready to mingle'],
    'education': ['MIT', 'OSSU', 'MOOC']
}

# accessing items by key
print(
    f"We have here {mydic['name']}. you can reach {mydic['name']} at {mydic['email']}")
print(
    f"{mydic['name']} does {mydic['hobby']} for the fun of it but does {mydic['profession'][0]} and {mydic['profession'][1]} for livelihood")
print(f"{mydic['name']} is now {mydic['age']} and surprising {mydic['status'][0]} but is {mydic['status'][1]}")
print(
    f"{mydic['name']} is an {mydic['education'][0]} graduate, {mydic['education'][1]} and {mydic['education'][1]} advocate")

# dictionary comprehension, note the difference between that of a set
new_dic = {x: x**2 for x in range(100) if x % 2 == 1}
print(new_dic)

# looping through a dic
for key, value in new_dic.items():
    print(f"{key} ** 2 = {value}")

# the above concept runs across all sequences
mylist = ["py", 'js', 'c', 'kot']
for index, value in enumerate(mylist):
    print(f"At {index} => {value}")

# say we have 2 sequence
mylist_2 = [x % 2 for x in [843, 824, 9023, 130]]

# we can combine mylist and mylist_2
for i, v in zip(mylist, mylist_2):
    print(f"{i} is from mylist and {v} is from mylist_2")