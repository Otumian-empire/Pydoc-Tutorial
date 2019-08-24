# user defined-exceptions
# an exception handler class for operand errors
# and extend or inherits CalculatorError
from calculatorerror import CalculatorError


class OperandError(CalculatorError):
    """ exception handler for operand error """

    def __init__(self, operand):
        self.operand = operand

    def raise_OperandError(self):
        """ raises an OperandError (this is Calculators version ValueError/TypeError - values must of type int or float) when the operand type is neither an int or float and returns a bool, False else True """

        operand_types = [int, float]

        if type(self.operand) not in operand_types:
            print(
                f"OperandError: {repr(self.operand)}, is not of type int or float but of {type(self.operand)}")
            return False

        return True

    def raise_OperandZeroError(self):
        """ raises an OperandZeroError (this is calculators version of ZeroDivisionError) - when (especially) the second operand passed, is zero and returns a bool,False else True """

        if self.operand == 0:
            print(
                f"OperandZeroError: a Non-Zero operand required, {repr(self.operand)} given")
            return False

        return True
