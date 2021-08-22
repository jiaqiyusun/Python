# OOP

# self reforce new player
class PlayerCharacter:
    # Class Object Attribute no change no modify
    membership = True

    def __init__(self, name='blabla', age='0'):  # magic dundem method
        if(self.membership) and (age > 18):  # or PlayerCharacter.membership
            self.name = name
            self.age = age
        else:
            print('player is not age enough')

    def run(self, hello):
        print('run')
        return 'done'

    def shout(self):
        # just self because in function name is not object attribute
        print(f'run {self.name}')

    @classmethod  # we care and we change that maybe
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod  # we dont care class
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 10)  # dynamic
player2 = PlayerCharacter('Tom', 33)
player1.attack = 50

print(player2.adding_things(2, 3))
print(PlayerCharacter.adding_things(2, 3))

player3 = PlayerCharacter.adding_things(2, 3)

print(player3)

# print(player1.name, player1.age)
print(player1)
print(player2.shout())
print(player2.run('hello'))
# print(player1.attack)
# help(player1) get blueprints
