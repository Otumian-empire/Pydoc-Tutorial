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
