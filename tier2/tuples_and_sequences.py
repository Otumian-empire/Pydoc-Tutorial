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
