# user defined-exceptions
# an exception class, that will serve as the base file for calculations


class CalculatorError(Exception):
    """ Base class for my exception handlers for the calculator class\n
    None value may be returned after a calculation, when an exception is caught """
    pass
