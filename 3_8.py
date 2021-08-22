# multiple inheritance
class User():

    def sign_in(self):
        print('chu chu')


class Wi(User):
    def __init__(self, name, power):
        self.name = name  # i do not want add atribute email here
        self.power = power

    def attack(self):
        print(f'attack man with power of {self.power} !!!')


class Ai(User):
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def attack_energy(self):
        print(f'attack man with power of {self.energy} !!!')

    def run(self):
        print('run very faster!')


class SumPower(Wi, Ai):
    def __init__(self, name, power, energy):
        Ai.__init__(self, name, energy)
        Wi.__init__(self, name, power)


su = SumPower('jiji', 50, 100)
print(su.attack_energy())
print(su.attack())
