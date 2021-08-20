#Function

#DRY
def say_hello():
    print('hello')

for i in range(10):
    say_hello()

print(say_hello) # show location of the function

#Arguments vs Parameters make our function more expensible

# parameter inside brackin give it 
def action(name,emoji):
    print(f'zzz{name}{emoji}')

# positional arguments call invoke
action('love',':>')

#Default
#keyword arguments
action(emoji=':>',name='bbb')

#Defauly Parameters
def hi(name='jj', emoji='blaba'): #initial some item in brackin,never been empty
    print(name, emoji)

hi()