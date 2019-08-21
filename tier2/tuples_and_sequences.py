# tuples and sequences
# tuples with bracket
tuple_with_brakect = (1, 2, 3, 4, 5)
print(tuple_with_brakect)

# tuples without bracket
tuple_without_brakect = 1, 2, 3, 4, 5
print(tuple_without_brakect)

# indexing a tuple just like a list or string
print(f"The first element in {tuple_with_brakect} is {tuple_with_brakect[0]}")
print(
    f"And the last element is {tuple_with_brakect[len(tuple_with_brakect) - 1]}")

# nested tuples
multi_tuple = tuple_with_brakect, tuple_without_brakect
print(
    f"{multi_tuple}, has it first element to be ,{multi_tuple[0][0]}, and the last to be ,{multi_tuple[len(multi_tuple) - 1][len(multi_tuple[len(multi_tuple) - 1]) - 1]}")

# unpacking tuple
# there are 2 tuples in multi_tuple, we can assign then individually without indexing it
tuple_0, tuple_1 = multi_tuple
print(multi_tuple, tuple_0, tuple_1)

# a set
myset = {1, 2, 2, 4, 5, 6, 7, 7}
print(myset)

# set operations
set_a = {4, 2, 7, 4, 3, 7, 4, 9}
set_b = {8, 3, 2, 3, 6, 9, 3, 0}

print(f"The sets are set A = {set_a} and set B = {set_b}")

# union
set_union = set_a | set_b
print(f"The union of set A, {set_a} and set B, {set_b} is {set_union}")

# intersection
set_intersection = set_a & set_b
print(f"The intersection of set A, {set_a} and set B, {set_b} is {set_intersection}")

# difference
set_diff_a_b = set_a - set_b
print(f"The set difference between set A, {set_a} and set B, {set_b} is {set_diff_a_b}")

# exclusive union ^
set_exclusive_union = set_a ^ set_b
print(
    f"The exclusive union of set A, {set_a} and set B, {set_b} is {set_exclusive_union}")

# there is also a set comprehension just like thw list comprehension
set_comprehension = {x ** 2 for x in set_a}
print(set_comprehension)