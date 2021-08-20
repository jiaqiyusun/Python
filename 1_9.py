#list

li = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2.5,'a',True]

#Data structure 
#amazon_cart = ['notebooks', 'sunglasses'] #list thing in memory
#print(amazon_cart[1])

# List slicing
#string = 'hellllp'
#string[0:2:1]
amazon_cart = [
    'notebooks', 
    'sunglasses',
    'toys',
    'grapes'] #list thing in memory

print(amazon_cart[0::2])

#remember we can not change string, but we can change list

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]# i want to copy and create new list
#new_cart = amazon_cart means new_cat equals amazon_cart, we not copy list, are simply change the origin list
new_cart[0]= 'gum'
print(new_cart) 
print(amazon_cart)

#Matrix
matrix = [
    [1,2,3],
    [2,4,6],
    [7,8,9]
    ]


print(matrix[0][1])

#List Methods
basket = [1, 2, 3, 4]
print(len(basket))

#adding
basket.append(5)
basket.insert(5, 100)
basket.extend([100,111])
print(basket)#add object to end list

#removing
basket.pop()#removw last one
basket.pop(0)#remove position 0
basket.remove(4)#remove position 4

new_list = basket.pop(3)
print(basket)
print(new_list)

#basket.clear() python3
del basket [:]
print(basket)

letters = ['a','b','c','d','e','d']
print(letters.index('d',0,4)) #make small list between 0 and 4, if does not exist, return erro

print('d' in letters)# is d in list letters

print('i' in 'hi my name is jiaqi')

print(letters.count('d'))#count number d exist

letters.sort()#sort list 
print(letters)
print(sorted(letters)) # does not mod

#new_letters = letters.copy()#python 3
new_letters = letters[::]

new_letters.reverse()# switvhing all the indexes into opposite


#Command list 

print(len(new_letters))
print(new_letters[::-1])#reverse
print(new_letters)

print(list(range(100)))#range(start, stop) generate quickly


#sentence = '!'
new_sentence = ' '.join(['hi','my','name'])
print(new_sentence)

#list unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)
