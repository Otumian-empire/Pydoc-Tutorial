# user defined-exceptions
# an exception handler class for operand errors
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
