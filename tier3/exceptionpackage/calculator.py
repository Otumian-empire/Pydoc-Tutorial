# user defined class that makes use of the sub classes of the CalculatorError class
# CalculatorError class has the OperandError and OperatorError extending it
# Calculator class uses these two subclasses to check for errors (operand and operator errors)
from operanderror import OperandError
from operatorerror import OperatorError


class Calculator:
    """ a class that makes use of OperandError and Operator error and works binarily"""

    def __init__(self, operand_1, operator, operand_2):
        self.operand_1 = operand_1
        self.operator = operator
        self.operand_2 = operand_2

    def evaluate(self):
        """ returns True if there's no error else False """
        opd_1_bool = OperandError(self.operand_1).raise_OperandError()
        opt_bool = OperatorError(self.operator).raise_OperatorError()
        opd_2_bool = OperandError(
            self.operand_2).raise_OperandError() and OperandError(self.operand_2).raise_OperandZeroError()

        if not opd_1_bool or not opt_bool or not opd_2_bool:
            return False
        return True

    def calculate(self):
        """ returns the computated value of a calculation """
        if self.evaluate():
            if self.operator == '+':
                return self.add()
            elif self.operator == '-':
                return self.difference()
            elif self.operator == '*':
                return self.product()
            elif self.operator == '**':
                return self.pow()
            elif self.operator == '/':
                return self.div()
            elif self.operator == '//':
                return self.floor_div()
            elif self.operator == '%':
                return self.mod()
            else:
                exit
            print("we can do some calculation")
        else:
            print("we can not do any calculation, fix the errors before")

    def add(self):
        """ returns the sum of the operands """
        return self.operand_1 + self.operand_2

    def difference(self):
        """ returns the difference between the operands """
        return self.operand_1 - self.operand_2

    def product(self):
        """ returns the product of the operands """
        return self.operand_1 * self.operand_2

    def pow(self):
        """ returns the power of one operands to the exponent of the second operand """
        return self.operand_1 ** self.operand_2

    def mod(self):
        """ returns the remainder of one operands when divided by the second operand """
        return self.operand_1 % self.operand_2

    def div(self):
        """ return the ratio of one operands when divided by the second operand """
        return self.operand_1 / self.operand_2

    def floor_div(self):
        """ return the quotient of one operands when divided by the second operand """
        return self.operand_1 // self.operand_2
