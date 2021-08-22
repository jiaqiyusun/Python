# Pure function (everythings in box function, not modify by other developer)
# guideline

# map, filter, zip, and reduce
# reduce
from functools import reduce
my_list = [1, 2, 3]
your_list = [10, 12, 13]
their_list = (1, 2, 3)


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

# map


def m_sim2(item):
    return item*2


print(list(map(m_sim2, [1, 2, 3])))  # give me function i will take care their
print(list(map(m_sim2, my_list)))
print(my_list)  # does not modify


# filter


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, my_list)))


# zip
# does not metter forma list or tuple
print(list(zip(my_list, your_list, their_list)))

# reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 10))

# lambda expressions function only use once
#lambda param: action(param)

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))


#print(multiply_by2([1, 2, 3]))
