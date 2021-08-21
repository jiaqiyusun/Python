# Docstrings

def test(a):
    '''
    Info: this function teste and prints param a
    '''
    print(a)


test('!!!')
# help(test)
print(test.__doc__)

# clean code


def is_odd_or_even(num):
    return num % 2 == 0


print(is_odd_or_even(50))

# *args vs **kwargs


def super_func(*args, **kwargs):
    print(kwargs)
    print(*args)
    print(args)
    total = 0
    for items in kwargs.values():
        total = total + items
    return sum(args) + total


print(super_func(1, 2, 3, 4, num1=4, num2=2))

# Rule: param, *args, default parameters(i='hi'), **kwargs(dictionary)

# ex


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([1, 2, 3, 4, 5]))

# walrus operator :=
a = 'helllllpsss'
if((x := len(a)) > 10):
    print(f"too king {x} elements")

while((n := len(a)) > 1):
    print(n)
    a = a[:-1]

print(a)

# scope -what variable do i have access to? function scope
if True:  # universe
    x = 10


def some_f():
    total = 100

# print(total)


# scope rules
a = 1


def parent():
    a = 4

    def confusion():
        return a
    return confusion()


print(a)
print(parent())

# 1 - start with local
# 2 - Parent local?
#3 - Global
# 4 - built in python function

#global keyword
# total = 0
# def count():#every you run function, u reset total
#     global total#use global variable not useful
#     total += 1
#     return total

# count()
# print(count())


total = 0


def count(total):
    total += 1
    return total


print(count(count(total)))

# nonlocal is not global but outside my local


def outer():
    x = 'local'

    def inner():
        nonlocal x  # can change outside variable modified
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer;", x)


outer()
