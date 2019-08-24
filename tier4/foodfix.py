# fixing the issue in food.py
# this is kind of a bug, thats not what we wanted
# this can be done by making the class variable an instance variable


class Food:

    def __init__(self, name):
        self.name = name  # instance variable (attr)
        self.fav_food = []  # class variable fix by making inst var

    def set_fav_food(self, food: str):
        self.fav_food.append(food)


person_a = Food('jerry')
person_a.set_fav_food('rice and pancake')
# person_a can access its own fav_food
print(person_a.fav_food)

person_b = Food('Lee')
person_b.set_fav_food('roated groundnut and catchup')
print(person_b.fav_food)

# when you check the output, you realise that the second instance doesn't modifies
#  the fav_food variable
