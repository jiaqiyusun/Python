#This is my first project python
#number
print(520)
#a machine do not need to know, soon """
print("hello world")
print('hello world')

print(3+1)

#create one file for write
fp=open('/Users/jiaqiyu/Documents/python/file.txt', 'a+')
fp.write('welcome')
fp.close()

print('hello\nworld')
print('hello\tworld')
print('hello\rworld')
print('hello\bworld') #lost last one caracts
print('hello\\l') #just have one \
print('hello:\'worls\'')
print(r'hello\nworld') #remove effect  \n

print(chr(000)) #charact chines
print(ord('A')) #to known de nº ascii