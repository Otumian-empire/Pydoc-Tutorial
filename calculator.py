class Calculator(OperandError, OperatorError):
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
