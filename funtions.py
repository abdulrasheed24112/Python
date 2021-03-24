# Functions 
def sum(num1,num2):
    result = num1+num2
    print(result)

sum(10,20)

def names():
    name="Abdul"
    return name

print(names())

#Built-In Functions
#Search function for finding string from substring
str_find = "This is Pakistan"
print(str_find.find("Pakistan"))
print(str_find.find("is",1,10))

#Replace
print(str_find.replace("Pakistan","Python"))

#Letter case
print(str_find.upper())
print(str_find.lower())

#Type Conversions 
i_number = 23
f_number = 22.22
b_value = False
str_value = "python"

#Interger Conversions 
print(int(f_number))
print(int(b_value))

#Character to Unicode
print(ord('a'))
print(ord('1'))

#Float Conversions
print(float(i_number))
print(float(b_value))

#String Conversions
print(str(i_number) + '445')

#Lambda Function
m_func = lambda num3 : num3*3
print(m_func(5)) 

my_sum = lambda a,b,c : a+b+c
print(my_sum(1,2,5))

str_con = lambda a,b,c : a+b+c
print(str_con("Pro","gram","ing"))

my_func2 = lambda num: "High" if num>50 else "Low"
print(my_func2(90))


#Calculator using simple functions
def add(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2

def calculator(operation,n1,n2):
    return operation(n1,n2)

rzlt = calculator(mul,10,20)
print(rzlt)

#Using Lambda 
def calculator1(operation,a,b):
    return operation(a,b)
cal = calculator1(lambda a,b:a+b,10,20)
print(cal)
print(calculator(lambda a,b:a-b,100,30))

num_list = [0,1,2,3,4,5]
print(list(map(lambda n: n*2,num_list)))

def rec_count(number):
    print(number)
    # Base case
    if number == 0:
        return 0
    rec_count(number - 1)  # A recursive call with a different argument
    print(number)


rec_count(5)