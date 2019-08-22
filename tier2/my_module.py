# my_module.py is about the use of modules in python
# I did random things that came to mind


# makes use of the type function
# returns the type as expected from the type function
#
# put the bracket around a sequence of numbers before you cast,
# when you are looking for the type of the casted obj
# that is, pass it as a tuple
# sample: get_obj_type((1,2,3,4)), get_obj_type takes on positional argument
def get_obj_type(obj):
    """ returns the type of an object """
    return type(obj)


# makes use of the len function
# this works on any sequence i know off as at now
# i changed the length of True to 1 and False to 0
# for numbers such as int and float
# it returns the length of the number when casted
# for the float the dot, "." is also counted
def get_obj_len(obj):
    """ 
    returns the length of an object 
    """
    number_types = [int, float]
    if get_obj_type(obj) in number_types:
        return len(str(obj))
    elif get_obj_type(obj) == bool:
        return 1 if obj == True else 0
    elif get_obj_type(obj) == type:
        return 0
    else:
        return len(obj)


# check if an object is a sequence (an iterable)
def is_obj_sequence(obj):
    """ 
    checks if an object is a sequence (an iterable) and returns a boolean\r\n 
    """
    sequence = [set, list, tuple, str, dict]
    return True if obj in sequence or get_obj_type(obj) in sequence else False


# calls the above functions on the object
def display_obj_stats(obj):
    """ 
    makes call to get_obj_type, get_obj_len and is_obj_sequence, passes obj as argument and prints the result\r\n
    sample use case: \r\n
    display_obj_stats("python") -> arg: python type: < class 'str' > size: 6 sequential: True\r\n
    display_obj_stats("Afro circus") -> arg: Afro circus type: < class 'str' > size: 11 sequential: True
     """
    print("arg:", obj, "type:", get_obj_type(obj), "size:",
          get_obj_len(obj), "sequential:", is_obj_sequence(obj))


# test cases as a module
display_obj_stats(0)
display_obj_stats(-3143)
display_obj_stats(int())
display_obj_stats(int('123'))
display_obj_stats(int)

display_obj_stats(3.143)

display_obj_stats("")
display_obj_stats("python")

display_obj_stats(True)
display_obj_stats(False)

display_obj_stats((1, 2, 3, 4))

display_obj_stats({1, 2, 2, 3, 4})
display_obj_stats(set)
display_obj_stats(set((2, 3, 4)))

display_obj_stats(list((2, 3, 4)))

display_obj_stats(dict([('c', 0), ('python', 1), ('cotu', 2)]))


# this part isn't working as i thought it would
# i hope i get it later
# if __name__ == "__main__":
#     from sys import argv

#     obj = argv[1]
#     print(get_obj_type(obj))
#     print(get_obj_len(obj))
#     print(is_obj_sequence(obj))


# from tier2.my_module import get_obj_type as _type, get_obj_len as _len, is_obj_sequence as _seq
# my_module was in tier2 on my pc
# from my_module import get_obj_type as _type, get_obj_len as _len, is_obj_sequence as _seq
# if you have my_module in same directory as the command line
# from path.to.my_module.my_module import get_obj_type as _type, get_obj_len as _len, is_obj_sequence as _seq
# it will be better if a try and catch is added
