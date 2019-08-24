from calculator import Calculator


def println(val):
    print(val, '\n')


# test cases expected to fail
# test case exclude NameError - you have to do that on your own
# or best use literals

# i chose the '+' operator and the int and str for simplicity sake.
# this will also work for float and str
str_str_cal = Calculator('4', '+', '6')
println(str_str_cal.calculate())

str_int_cal = Calculator('4', '+', 6)
println(str_int_cal.calculate())

int_str_cal = Calculator(4, '+', '6')
println(int_str_cal.calculate())

# zero operand
int_div_zero = Calculator(6, '/', 0)
println(int_div_zero.calculate())

# test case expected to pass
int_int_cal = Calculator(4, '+', 6)
println(int_int_cal.calculate())

zero_div_int = Calculator(0, '/', 4)
println(zero_div_int.calculate())

zero_div_zero = Calculator(0, '/', 0)
println(zero_div_zero.calculate())
