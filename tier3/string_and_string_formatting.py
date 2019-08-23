# Input and output
# string formating
# item_cost = 1210
# tax_rate = 0.02
# actual_cost = item_cost - (item_cost * tax_rate)

# print("An item of price", item_cost, "at a tax rate of",
#       tax_rate, "will cost", actual_cost)

# print("An item of price {} at a tax rate of {} will cost {}".format(
#     item_cost, tax_rate, actual_cost))

# print("An item of price {:5} at a tax rate of {:5.2} will cost {:5.4%}".format(
#     item_cost, tax_rate, actual_cost))

# print(
#     f"An item of price {item_cost} at a tax rate of {tax_rate} will cost {actual_cost}")

# print(
#     f"An item of price {item_cost:.2f} at a tax rate of {tax_rate:.2f} will cost {actual_cost:.2f}")

# print(
#     f"An item of price {item_cost:7.2f} at a tax rate of {tax_rate:7.2f} will cost {actual_cost:7.2f}")


# my_assets = {
#     'web': 'flask',
#     'ml': 'numpy',
#     'ai': 'tensorflow',
#     'game': 'pygame',
#     'gui': 'tkinter'
# }

# for purpose, tool in my_assets.items():
#     print(f"{purpose} ==> {tool}")

# print('$', '#~' * 20, '$')

# for purpose, tool in my_assets.items():
#     print(f"{purpose:5} ==> {tool:10}")


# cake = "green chocolate cake"
# egg = "baked green egg and beans"
# print("The junk that daily, touches by belly is {} and at sun down is {}".format(cake, egg))
# print("The junk that daily, touches by belly is {1} and at sun down is {0}".format(cake, egg))
# print("The junk that daily, touches by belly is {cake} and at sun down is {egg} and sometime i take {both}".format(
#     cake=cake, egg=egg, both=cake + ", " + egg + " and pesi bean milk shake"))


# my_daily_bread = {
#     "junk": "green chocolate cake",
#     "break_fast": "baked green egg and beans",
#     "dinner": "pesi green bean horse milk shake"
# }

# print("I take {0[junk]} every afternoon, {0[break_fast]} for break fast and when i feel really kinda moody i take {0[dinner]} with my cat".format(my_daily_bread))

# print("I take {junk} every afternoon, {break_fast} for break fast and when i feel really kinda moody i take {dinner} with my cat".format(**my_daily_bread))  # pass the dict as a **kwarg

# print numbers, their square and cubes using the str.rjust
# there is str.ljust, str.center, str.zfill(n: int)
# for number in range(1, 11):
#     print(repr(number).rjust(2), repr(
#         number ** 2).rjust(3), repr(number ** 3).rjust(4))

# for number in range(1, 11):
#     print(repr(number).ljust(2), repr(
#         number ** 2).ljust(3), repr(number ** 3).ljust(4))

# for number in range(1, 11):
#     print(repr(number).center(3), repr(
#         number ** 2).center(5), repr(number ** 3).center(6))

# for number in range(1, 11):
#     print(repr(number).zfill(3), repr(
#         number ** 2).zfill(5), repr(number ** 3).zfill(6))

# c-like format (old)
# num_i = 34
# num_f = 1.23
# print("%d + %.2f = %.2f" % (num_i,num_f,num_i + num_f))

# for number in range(1, 11):
#     print("%2d %4d %6d" % (number, number ** 2, number ** 3))
