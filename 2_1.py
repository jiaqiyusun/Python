is_old = True
is_licenced = True

if is_old:  # if true other not mater if false see other one
    print('you are old enough to drive!')
elif is_licenced:
    print('you can drive now!')
else:  # otherwise
    print('you are nit of age!')

print('okok')

if is_old and is_licenced:  # and
    print('ok!')
else:
    print('nono!')

#Truthy and Falsy
#false id ' ' or 0, None, False, empty, 

is_o = 'hello'
is_l = 5

if is_o and is_l:
    print('good!')
else:
    print('nem nem!')

password = '123'
username = 'johnny'

if password and username:
    print('ok')
else:
    print('not')

#another way
#Ternary Operator (short)

#condition_if_true if condition else condition_if_else

is_friend = True
can_msg = "msg allowed" if is_friend else "not allowed to msg"
print(can_msg)