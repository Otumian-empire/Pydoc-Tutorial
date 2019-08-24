# A class may have an attribute (a variable)
# there are mainly two instances of this variables
# one, class variable and the other an instance variable
# the difference, class variable is like a static variable (it is shared
#  by all instances of the class) - something too like a global variable
# but the instance variable is local (bundled) to the instance


class Food:

    fav_food = []  # class variable

    def __init__(self, name):
        self.name = name  # instance variable (attr)

    def set_fav_food(self, food: str):
        self.fav_food.append(food)


person_a = Food('jerry')
person_a.set_fav_food('rice and pancake')
# person_a can access fav_food
print(person_a.fav_food)

person_b = Food('Lee')
person_b.set_fav_food('roated groundnut and catchup')
print(person_b.fav_food)

# when you check the output, you realise that the second instance modifies the
# fav_food variable
