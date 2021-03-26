#creating list with different parameters
mList = ["Abdul","Pakistan",23,9.9]
for i in mList:
    print(i)

print(mList[2])
print(len(mList))

num = range(0,10)
num_list = list(num)
print(num_list)

#List ception
area_code = [["Islamabad",44000],["Karachi",74600],["Lahore",5400]]
for i in range(len(area_code)):
    for j in range(len(area_code[i])):
        print(area_code[i][j],end=' ')
    print( )

#Merging List 
a = [1,2,3]
b = [2,3,4]
a.extend(b)
print(a)

#Adding new List element 
numList = []
numList.append(0)
numList.append(1)
numList.append(2)
numList.append(3)
print(numList)

#Adding value on the index 
print("Adding value on the index ")
numList.insert(3,10)
print(numList)

#Removing list item using pop()
print("Removing list item")
nList = ["Ak-47","M24","vector","SKRL"] 
last=nList.pop() #it removes last element of the list 
print(nList)

#Removing list item using remove()
nList.remove("Ak-47")
print(nList)

#search element
cities = ["Islamabad","London","Paris","Los Angles"]
print(cities.index("London"))
print("London" in cities)

#Sort list 
sortList = [67,71,2,80,4]
sortList.sort()
print(sortList)

#List Comprehension 
nums = [10,20,30,40]
double_nums = [n*2 for n in nums]
print(double_nums)

#adding condition in comprehension List 
numsList = [n*2 for n in nums if n%4==0]
print(numsList)


l1 = [56,23,46,70,80]
l2 = [10,20,30,40]
l3 = [(n1,n2) for n1 in l1 for n2 in l2 if n1+n2>100]
print(l3)