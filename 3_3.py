class PlayerCharacter:
    def __init__(self, name, age):  # __you should not touch it dunder method
        self._name = name  # _ signific privary
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self._name}, i am {self._age} yeaes old.')


player1 = PlayerCharacter('jiaqi', 19)
player1.speak()

player2 = {'name': 'jiji', 'age': 1}
print(player2['name'], end=' ')
print(player2['age'])

# abstraction  hide blanket information
print((1, 2, 3, 4, 1).count(1))
print(len((1, 2, 3, 4, 1)))
player1.name = 'jia1'
player1.speak()
player1.speak = 'BOOOO'
print(player1.speak)

# private(_) and public variable
