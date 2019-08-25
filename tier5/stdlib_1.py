# Brief Tour of the Standard Library

import doctest
import unittest
import timeit
import zlib
import datetime
from urllib.request import urlopen
import statistics
import random
import math
import sys  # cmdline
import glob  # list of a wildcard search
import shutil  # file and directory system interface
import os  # operating system interface

# # working briefly with the os module
# print(f"The current working directory: {os.getcwd()}")
# os.chdir('tier5')
# print(f"Changed directory into directory: {os.getcwd()}")
# os.chdir('../')
# print(f"Now the current working directory: {os.getcwd()}")

# # ls, create a file with touch, add text and echo the text from the file
# # ls again
# os.system('ls')  # execute cmds in a subshell
# os.system("touch ossystem")
# os.system("echo 'haha' >> ossystem")
# os.system("cat ossystem")
# os.system('ls')

# os as open() which there is open also one for opening of files
# avoid `import os *`


# # working briefly with the shutil module
# print(shutil.copyfile('ossystem', 'helloworld'))

# # working briefly with the glob module
# print(glob.glob('../*'))  # read all that ends with .py

# # working briefly with the sys module
# print(sys.argv)
# print(sys.stderr.write("error"))
# sys.exit()

# # working briefly with the math module
# print(f"The area of a circle of 3cm is {math.pi * math.pow(3, 2):.2f}cm^2")

# # working briefly with the random module
# print(random.randint(1, 10))

# working briefly with the statistics module
# print("The mean of [2,3,5]", statistics.mean([2, 3, 5]))

# # working briefly with the internet module - urllib
# with urlopen('file:///home/otumian/Documents/Python/python-3.7.3-docs-html/tutorial/stdlib.html') as responds:
#     for line in responds:
#         line = line.decode('utf-8')
#         if '<a' in line:
#             line = line[line.index('<a'):]
#             print(line, file=open('ossystem.txt', 'a+'))


# # working briefly with the datetime module
# print(datetime.date(1996, 12, 2))
# print(datetime.time(23, 30, 12))
# print(datetime.datetime(2012, 12, 2, 2, 3, 4))
# print(datetime.datetime.now())
# print(datetime.date.today().strftime(
#     "%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# # working briefly with the data compression module - zlib
# data = b"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Expedita cupiditate nam perferendis perspiciatis quasi, commodi quae deleniti rerum, provident suscipit possimus, eligendi repudiandae soluta repellendus neque eaque dolorem. Placeat, id!"

# data_size = len(data)

# compressed_data = zlib.compress(data)
# compressed_data_size = len(compressed_data)

# decompressed_date = zlib.decompress(compressed_data)
# decompressed_date_size = len(decompressed_date)

# print(f"date size: {data_size}\ncompressed data size: {compressed_data_size}\ndecompressed data size: {decompressed_date_size}")


# working briefly with the timeit module
# print(timeit.Timer('a += 1', 'a = 1').repeat(2))
# print(timeit.Timer('a = a + 1', 'a = 1').repeat(2))
# print(timeit.Timer('a ** 2', 'a=2').repeat(2))
# print(timeit.Timer('a * a', 'a=2').repeat(2))
# print(timeit.Timer('math.pow(a, 2)', 'a=2').repeat(2)) # name error
# print(timeit.Timer('n-(d * q)', 'n=5; d=3;q = n//d').repeat(10))
# print(timeit.Timer('n % d', 'n=5; d=3').repeat(10))

# quality control
# doctest module
def say_hi():
    """ returns a hi 

    >>> say_hi()
    'hi'
    """
    return 'hi'


doctest.testmod()

# unittest


class SayHiTest(unittest.TestCase):

    def test_say_hi_(self):
        self.assertTrue(say_hi(), "must return a value")
        self.assertEqual(say_hi(), 'hi', 'say_hi is supposed to return hi')


unittest.main()
