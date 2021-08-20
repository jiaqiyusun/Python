#set create unique obj

my_set = {1,2,3,4,5,5} #everthing will be unique

your_set = {4,5,6,7,8,9,10}

#.difference
print(my_set.difference(your_set))# only show difference my set
my_set.discard(5) #remove 5
my_set.difference_update(your_set)# change and update

my_set.intersection(your_set)
my_set.isdisjoint(your_set) # have intersection if not return true
my_set.union(your_set)#union two set
print(my_set | your_set)#union two ser
print(my_set & your_set)#interesetion 

print(my_set.issubset(your_set))# all my_set is in yor set
print(my_set.issuperset(your_set))#oposite
print(my_set)














my_set.add(100)
my_set.add(1)#does not work only just one in memory
print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))#image user_name

#print(my_set[0]) does not work
print(1 in my_set)
print(len(my_set))

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)