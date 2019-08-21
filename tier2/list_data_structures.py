# making use of the list and implementings some of it's methods

# initialized an empty list
mylist = []
print(mylist)

# append an element to the start, end
mylist.append("first element")
print(mylist)

# append another element, after the first
mylist.append("last element")
print(mylist)

# insert an element in the middle
mid_pos = len(mylist) // 2
mylist.insert(mid_pos, "middle element")
print(mylist)

# attach or extend the list by adding another list
another_list = [1, 2, 3, 4]
mylist.extend(another_list)
print(mylist)

# remove an item by passing its value
# let's remove "first element"
mylist.remove("first element")
print(mylist)

# remove an item by passing its index (position - 1)
mylist.pop(0)
print(mylist)

# this will remove the last element if no index is passed
mylist.pop()
print(mylist)

# clear the list (empty it)
# mylist.clear()
# print(mylist)
# i comment this part, because i am still using the data in the list

# find the index of an item, by passing the value in the index method
print(f"The index of 2 in {mylist} is {mylist.index(2)}")

# count the number of times an item appears in a list
print(f"2 appeared {mylist.count(2)} time(s) in {mylist}")

# sort the items in the list
# this is actually change the order of things in the original
# list compared to sorted() which will on return a sorted list
# the immediate line below will raise an error because of the different kind of types
# print(f"{mylist} when passed into sorted as sorted({mylist}) is {sorted(mylist)}")
# so here we'd clear the list and git it new values
mylist.clear()
print(mylist)

mylist.extend([3, 5, 7, 32, 6, 8, 42, 1, 0])
print(f"{mylist} when passed into sorted as sorted({mylist}) is {sorted(mylist)}")
print(f"{mylist} is still the same")

# now we change the order in memory
mylist.sort()
print(f"{mylist} after it has been \"sort\"")

# reverse the list
mylist.reverse()
print(mylist)

# we could have also revsered the list we sorted it by passing, reverse=True in sort
mylist.sort(reverse=True)
print(mylist)

# though the above line won't sort like we expected, it actually did
# it sorted and reversed it as it is
# by default reverse=False
mylist.sort() 
print(mylist)

# the difference is that reverse will reverse (change the order of arrangement) the items in the 
# list without sorting them
mylist.reverse()
print(mylist)

# copy the content of a list into another
new_list = mylist[:]
print("new list:", new_list, "mylist:", mylist)

# similar approach is to use the copy method
another_nl = mylist.copy()
print("another new list:", another_nl, "my list:", mylist)

# list comprehension
sqr_list = list(map(lambda x:x ** 2, mylist))
print(sqr_list)

# new sqr list
sqr_list_1 = [(x ** 2) for x in mylist]
print(sqr_list_1)

# it is time we move to other topic
del mylist[:]
del new_list[:]
del sqr_list[:]
del sqr_list_1[:]
