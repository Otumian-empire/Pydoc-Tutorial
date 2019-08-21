# file name should always match the class name
from profile import Profile as Prof


# defining functions
def say_hello():
    print("hello")


# fib function
def myfib(n):
    with open('fibout', 'w+') as f:
        a, b = 0, 1
        while a < n:
            print(a, file=f, end=" ")
            a, b = b, a+b

        print(file=f)


def my_profile(full_name, date_of_birth, occupation):
    return Prof(full_name, date_of_birth, occupation).get_user_profile()


# main function
def main():
    pass
    # say_hello()
    # myfib(10)
    # print(my_profile("John Doe", "18th August, 2019", "Programmer"))


main()
