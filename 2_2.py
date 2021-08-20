#Short Circuiting

is_friend = False
is_user = True
#and  or
if is_friend and is_user:
    print('best friend forever')

#Logical Operator
print(4 > 5)
print(4 == 5)
print(4 > 5)
print('hello' == 'hello')
print('a'>'A')#ASCII google into it

print(1>=2<3<4)
print(1>=0)
print(1 != 0)#not equal to exclamation
#< > == <= >= != and or not

print(not(True))#opposite
print(not(False))

#exercise

is_magicion = False
is_expert = True

#check if magician aND expert: "you are a master"
#check id magician but not exper: at least 
#if you are nit a magician

if is_magicion and is_expert: 
    print('you are a master')
elif is_magicion and not(is_expert):
    print("at least you´re getting there")
elif not is_magicion:
    print('You need magic power')


#is ==
print(True == 1)
print(' ' == 1)
print(10 == 10.0)

print(True is 1)#is check a location
print(' ' is 1)
print('1' is 1)
print(10 is 10.0)
print([] is [])#list location in one memory, if u crate another one, new list will be another laction, even same letterm same number


a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
