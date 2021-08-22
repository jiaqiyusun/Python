some_list = ['a', 'b', 'c', 'd', 'e', 'a', 'c']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

a = list(set([num for num in some_list if some_list.count(num) > 1]))

print(a)
