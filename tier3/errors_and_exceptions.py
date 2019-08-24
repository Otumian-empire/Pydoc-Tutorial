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


# # raising exceptions
# # programmer force an esception
# raise NameError('my guy, this is a name error')
# # this can done this way too, without braces
# raise ValueError
# # try to raise any unhandled error
# try:
#     raise NameError('I am raising a NameError')
# except NameError:
#     print("we had a NameError")
#     raise  # this will raise any error as i do not want to handle it
#     # or to say will raise any unhandled error




class OperandError(BaseException):
    """ exception handler for operand error """

    def __init__(self, operand):
        self.operand = operand

    def raise_OperandError(self):
        """ raises an OperandError (this is Calculators version ValueError - values must of type int or float"""

        operand_types = [int, float]

        if type(self.operand) not in operand_types:
            print(
                f"OperandError: {repr(self.operand)}, is not an int() or a float() but of {type(self.operand)}")
            return 0

        return 1


class OperatorError(BaseException):
    """ exception handler for operator error """

    def __init__(self, operator):
        self.operator = operator

    def raise_OperatorError(self):
        """ raises an OperatorError (this is likely to be a SynthaxError as it is called when 
        the operator is nor recognised)"""

        operators = ['%', '*', '**', '-', '+', '/', '//']

        if self.operator not in operators:
            print(
                f"OperatorError: {repr(self.operator)}, is not known, use any of {repr(operators)}")
            return False

        return True


class Calculator:
    """ a class that makes use of OperandError and Operator error and works binarily"""

    def __init__(self, operand_1, operator, operand_2):
        self.operand_1 = operand_1
        self.operator = operator
        self.operand_2 = operand_2

    def evaluate(self):
        opd_1_bool = OperandError(self.operand_1).raise_OperandError()
        opt_bool = OperatorError(self.operator).raise_OperatorError()
        opd_2_bool = OperandError(self.operand_2).raise_OperandError()

        if not opd_1_bool or not opt_bool or not opd_2_bool:
            return False
        return True

    def calculate(self):
        if self.evaluate():
            print("we can do some calculation")
        else:
            print("we can not do any calculation, fix the errors before")


my_calc = Calculator(3, '+', 3)
# print(my_calc.evaluate())
my_calc.calculate()


# print(f"stack trace: {self.with_traceback(None)}")
# """
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
#  """
# read on how to create a traceback
