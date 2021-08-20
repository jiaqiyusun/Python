#Ex: Check dor duplicate in list
some_list = ['a','b','c','d','e','e']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)