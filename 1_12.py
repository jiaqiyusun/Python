#Tuple more predicble work for geografh driver coordinates

my_typle = (1,2,3,4,5)#cant change like list
#my_tuple[1] = 'z' soes not work
print(5 in my_typle)

u  = {
    'a':1,
    'b':2,
    (1,2): [1,2,3]
}

print(u[1,2])

print(u.items()) # reverse dictionary to tuple

new_tuple = my_typle[1:2]
print(new_tuple)# we be (2,) if just have one item 

x,y,z,*other = (1,2,3,4,5)
print(*other)

print(my_typle.count(4))#count number of the value how many 4 in tuple
print(len(my_typle))