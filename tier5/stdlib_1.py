# Brief Tour of the Standard Library

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
