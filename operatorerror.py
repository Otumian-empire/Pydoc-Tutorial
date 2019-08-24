# user defined-exceptions
# an exception handler class for the operator error
# and extend or inherits CalculatorError
from calculatorerror import CalculatorError


class OperatorError(CalculatorError):
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
