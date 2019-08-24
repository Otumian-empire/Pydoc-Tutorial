# first look at classes
# I have used classes already
# check from ../tier3/exceptionpackage/*
# or just locate it as a stand alone project 'exceptionpackage'
# at github.com/otumian-empire/exceptionpackage

# a simple class with an init, two methods and two attributes


class HelloClass:
    """ A simple demonstration of a class """

    def __init__(self):
        self.greetings = 'hello'
        self.name = 'user'

    def get_greetings(self):
        return f"{self.greetings}, {self.name}!!"

    def set_greetings(self, name='user', greetings='hello'):
        self.name = name
        self.greetings = greetings


my_hello_class = HelloClass()
print(my_hello_class.get_greetings())

another_hello_class = HelloClass()
another_hello_class.set_greetings('John Doe', "good afternoon")
print(another_hello_class.get_greetings())