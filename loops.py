for i in range(1,10):
    if i%2==0:
        print(i, "is Even number")
    else:
        print(i,"is odd number")
#Table
for a in range(1,11):
    print(a,"*",2,"=",a*2)

#Looping through List
int_list = [1,2,3,4,6,7,8,9]
print(int_list)
for b in range(0,len(int_list)):
    int_list[b] = int_list[b]*2
    print(int_list[b]) 

#continue 
for i in range(0,10):
    if i%2==0:
        continue 
    print(i) 

#while loop 
print("while loop")
num=1
while num<5:
    num=num+2
    print(num)
print("Length")
mList = ["Abdul","Rasheed","aziz"]
for i in mList:
    print(len(i))

