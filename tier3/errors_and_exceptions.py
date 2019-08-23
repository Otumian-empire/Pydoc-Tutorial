# errors and exceptions
# syntax error = parsing error (complaints - they come from a misuse of a token)
# exception error = runtime error (they are detected when the script is executed
# - may come from an error in the logic, perhaps)

# sample error
# print("hello world)
# #  error message  #
"""
  File "tier3/errors_and_exceptions.py", line 7
    print("hello world)
                      ^
SyntaxError: EOL while scanning string literal
"""
# print("hello world) - there is no close double quote

# sample exception
# 1/0
# #  error message #
""" 
Traceback (most recent call last):
  File "tier3/errors_and_exceptions.py", line 16, in <module>
    1/0
ZeroDivisionError: division by zero
"""
# this isn't just an error, it is an exception error - not allowed (kind of)
# any number divided by zero is undefine as such not permissible:
# here i had a, ZeroDivisionError: division by zero


# exception handling
# using try and except
# a simple program that asks the user to enter an integer
# until the value entered is actually an integer or the user
# terminates the program, then the program terminates
# while True:
#     try:
#         num = int(input("Enter a number: "))
#         print(f"you entered {num} and a doulbe of it is {num * 2}")
#         print("great now you did well, terminate with Ctrl(Cmd) + C(Z)")
#     # except ValueError:  # here we passed a ValueError Exception which means
#         # that if we had a different exception othere than ValueError, the exception won't be handled
#         # what we could do is pass in a general exception handler, Exception or add more exceptions to it
#     # except Exception as e:
#     except (ValueError, NameError, TypeError) as e:
#         print(f"error message: ({e})\nplease enter a number... the value you entered is not in example 1,2,3, ...")


# # an instance of an exception may have a type and arguments
# try:
#     num = int(input('enter a number: '))
#     print(f'you entered {num} and its double is {num * 2}')
# except Exception as e:
#     print(f'exception type: {type(e)}')
#     print(f'exception arguments: {e.args}')
#     print(f'exception message: {e}')
# this would have an output like this
# enter a number: q
# exception type: < class 'ValueError' >
# exception arguments: ("invalid literal for int() with base 10: 'q'",)
# exception message: invalid literal for int() with base 10: 'q'

