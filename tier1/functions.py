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


# my profile function makes use of the Profile class
def my_profile(full_name, date_of_birth, occupation):
    return Prof(full_name, date_of_birth, occupation).get_user_profile()


# annotations - looks like kotlin
def kotfunc(name: str, age: int, weight: float) -> str:
    return f"name: {name}\nage: {age}\nweight: {weight}"


# main function
def main():
    pass
    # say_hello()
    # myfib(10)
    # print(my_profile("John Doe", "18th August, 2019", "Programmer"))
    # print(kotfunc("John Doe", 32, 210))
    # print(kotfunc.__annotations__)
    # print(kotfunc(3, 32, 210))


main()
