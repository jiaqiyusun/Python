#String

print(type("hi hello i am here!"))

username = 'supercoder'
password = 'supersecret'

long_string ='''
WPW
= =
...
''' # long string with three single quotes
print(long_string)

first_name = "jiaqi"
last_name = "Yu"
full_name = first_name +' '+ last_name #space between last name and first name

print(full_name)

#string concatenation
print('hello' + ' Jiaqi')
#print('hello' + 5) does not work, because print just for str

print(type(str(100))) # converted int for string

print(type(int(str(100)))) 

a = str(100)
b = int(a)
c = type(b)
print(c)

#Type conversion

#Escape Sequence
weather = "\tit\'s \"kind of\" sunny\n hope you have a good day!"

print(weather)

#formatted strings
name = 'Jonhny'
age = 55
print('hi '+name+'. You are '+str(age)+' years old.')
#print(f'hi{name}, you are{age} years old.') python3
#print('hi{}, you are{} years old.').format('jonny','56')
#print('hi{}, you are{} years old.').format(name,age)
#print('hi{1}, you are{0} years old.').format(name,age)
#print('hi{new_name}, you are{age} years old.').format(new_name='sally',age=100)

#String index
#'mem mem mem'# m is stolen in space 0, e is stolen in space 1 etc

selfish = 'me me me'
print(selfish[0])# grab in location 0

#[start:stop:stepover] stop the letter before stop location
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[-1])# end one 
print(selfish[::-1])#reverse an order
print(selfish[::-2])

#Immutability 
#we can not change what we create, we can create new thing

selfish =  selfish +'8'
print(selfish)