# functions defined outside of a class


class MyClass:
    """ An empty class """
    pass


def get_name(self):
    return self.name


def set_name(self, name):
    self.name = name


# instance of MyClass
my_class = MyClass()

# calling a function on my_class
set_name(my_class, "John Doe")

print(get_name(my_class))


# So one thing you have to take home today is, that self is actuall the class
# self.name = ClassName.name


class DuoClass:
    def __init__(DuoClass, name):
        DuoClass.name = name

    def get_name(DuoClass):
        return DuoClass.name


my_duo = DuoClass('San Chu')
print(my_duo.get_name())