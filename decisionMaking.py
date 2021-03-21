num1 =20
if num1 > 9:
    print("The number is greater than 9")

if num1 < 9:
    print("The number is less than 9")#not excuted because the condition is not true

# Nested if statements 
num2 = 10
if num2 == 10:
    if num2 >= 10:
        if num2 >= 9:
            print("Numbers between 0-10")

# if else statment
if num1 >= 30:
    print("The Number is greater than or equal to 30")
else:
    print("The Number is less than 30")

#Contion Expression 
number = 5
output = "Number is greater than 20" \
     if number > 20 else "Number is less than 20"
print(output)

#if elif else
time = 17
if time > 5 and time < 11:
    print("Good Moring")
elif time > 11 and time < 4:
    print("Good after noon")
elif time > 4 and time<=19:
    print("Good Evening")
else:
    print("Good Night")