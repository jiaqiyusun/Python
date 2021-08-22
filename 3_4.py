# Inheritance allows new objects to take on the properyies of existing objects
class User(object):
    def sign_in(self):
        print('logged in')

    def attack(self):
        print("nothing")


class Wizard(User):  # Wizard also exist sign in
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)  # want two attack exist
        print(f'attacking with power of{self.power}')


class Aecher(User):
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def attack(self):
        print(f'attacking with num {self.num}')


wizard1 = Wizard('jiji', 20)
a = Aecher('ji', 2)


def player_attack(char):  # Polymorphism class can chare same name of methods
    char.attack()


player_attack(a)
player_attack(wizard1)
# wizard1.attack()
# a.attack()
# a.sign_in()

for char in [a, wizard1]:
    char.attack()

b = User()
b.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))  # base class
