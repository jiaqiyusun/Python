class User(object):
    def __init__(self, email):  # we add email
        self.email = email

    def sign_in(self):
        print('chu chu')

    def attack(self):
        print('O am king of world!')


class Wi(User):
    def __init__(self, name, power, email):
        #User.__init__(self, email)
        super().__init__(email)  # super class
        self.name = name  # i do not want add atribute email here
        self.power = power

    def attack(self):
        print(f'attack man with power of {self.power} !!!')


class Ai(User):
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def attack(self):
        print(f'attack man with power of {self.energy} !!!')


w = Wi('wiiii', 2, 'jijijji')
print(w.email)
# introspection
print(dir(w))
# Dunder Methods __
len([1, 2, 3])


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {'name': 'jj', 'xx': 'xx'}

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        print('yyyy')

    def __getitem__(self, i):
        return self.my_dict[i]


a = Toy('red', 1)
print(a.__str__())
print(str(a))
print(a.__len__())
print(a())  # call
print(a['name'])
