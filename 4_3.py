#list, set, dixtionary

#my_list = [param for param in iterable]

# for char in 'hello':
#     my_list.append(char)

my_list = [param for param in 'hello']

my_list2 = [num*2 for num in range(0, 100)]

my_list3 = [num**2 for num in range(0, 100)]

my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# set same list

my_set = {char for char in 'hello'}

# dictionary
sim_dic = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in sim_dic.items() if value % 2 == 0}

my_dict1 = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
print(my_dict1)
