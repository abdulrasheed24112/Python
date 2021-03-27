random_set = {"Python",121,12.3,(True,False)}
print(random_set)
#Creating using constructor and it allow us to create an empty set
empty_set =set()
print(empty_set)
m_set = set({"Python",121,12.3,(True,False)})
print(m_set)

#Adding elemenst 
empty_set.add(1)
print(empty_set)
#Multiple values add in set 
empty_set.update((1,3,5,6,7))#it does not create copy of item 
print(empty_set)

#deleting element using remove() or discard()
m_set.discard(121)
print(m_set)
m_set.remove((True,False))
print(m_set)

#Set Theory opertations 
#Union 
set_A = {1,2,4,5,7,8}
set_B = {'a','b','c','d'}
print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

#Intersection 
print(set_A & set_B)
print(set_A.intersection(set_B))#returns the similar elements which are present in both A and B set 

#difference 
print(set_A - set_B)#returns the elements which are only present in set_A.
print(set_B.difference(set_A))

my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
f_index = my_list[0]
s_index = my_list[4]
length  = len(my_list)
new_list = []
new_list.insert(0,f_index)
new_list.insert(1,s_index)
new_list.insert(2,length)
my_tuple =tuple(new_list)
print(my_tuple)

