from calculator import Calculator

# test cases expected to fail
# i chose the '+' operator and the int and str for simplicity sake.
# this will also work for float and str
str_str_cal = Calculator('4', '+', '6')
print(str_str_cal.calculate())

str_int_cal = Calculator('4', '+', 6)
print(str_int_cal.calculate())

int_str_cal = Calculator(4, '+', '6')
print(int_str_cal.calculate())

# test case expected to pass
int_int_cal = Calculator(4, '+', 6)
print(int_int_cal.calculate())
