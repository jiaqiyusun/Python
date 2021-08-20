#Loop
#for item(variable) in 'Zaro to Mastery':
for item in 'Zaro to Mastery':
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in (1,2,3,4,5):
    print(item)
print(item) # will print laste letter


for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item,x)

#Iterable - list, dictionary, tuple, set, string
#iterated(action) -> one by one check each item in the collection.

users = {
    'name': 'Gogo',
    'age': 200,
    'can_swim': False
}#dictionary

for item in users:
    print(item)

for item in users.values():
    #key, value = item,
    #print(key, value)
    print(item)

for key, value in users.items():
    print('laal')
    print(key, value)

for item in users.items():
    print(item)

for item in users.keys():
    print(item)

#ex

#counter 
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

for item in my_list:
    counter = counter + item
print(counter)

#range
print(range(100))

for number in range(10,0,-1): #reverse
    print(number)

for number in range(10,0,-2): #reverse
    print(number)

for _ in range(10,0,-2): #reverse
    print(list(range(10)))#quickly make list range

#enumerate
for i, char in enumerate('hello'):
    print(i, char)

for i, char in enumerate((1,2,3,4)):#counter
    print(i, char)

for i, char in enumerate(list(range(10))):
    if char == 5:
        print(f'index of 5 is: {i}')

#while
i = 0
while i<50:
    i+=1
    print(i)
    break
else:
    print('done with all the work!')

#for u can do list
#while very flexible
x = 0
while x < len([1,2,3]):
    print(i)
    x+=1

while True:#infinite loop
    i = input('say something:')
    if(i == 'bye'):
        break

#break
#continue first end loop 

x = 0
while x < len([1,2,3]):
    x+=1
    continue
    print(i)#never spit out

#pass something u are not finish, u just pass it

    