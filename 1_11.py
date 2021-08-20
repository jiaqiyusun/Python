#Dictionary hash table unordered key value pair
dictionary = {
    "a":[1,2,3] ,#key value the key grab value
    "b":'hello',
    "c": True
}
#does not have sort, order
print(dictionary['a'][1])

my_list = [
    {
    "a":[1,2,3] ,#key value the key grab value
    "b":'hello',
    "c": True

    },
    {
    "a":[2,2,4] ,#key value the key grab value
    "b":'hello',
    "c": True
    }
]
# we have dictionary in list
print(dictionary["b"])

w = { # key can not change, soon list can not be key 

    123: [1, 2, 3],
    True: 'hello'
}
#most time key is descript,  key is unique

#Dictionary methods

c = {
    'basket':[1,2,3],
    'ahe':'hello'
}

c2 = dict(name = 'john')
print(c2)
print(c.get('age',55)) #get key exist, if key does not exist, grab 55

print('basket' in c.keys())
print('hello' in c.values())
print(c.items())

a = c.copy()
print(a)
print(a.popitem())
print(a)
#print(a.pop('ahe')) #return value will remove

print(a.update({'age':44}))#add new key and value
print(a)


c.clear()
print(c)