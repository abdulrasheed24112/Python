phone_book = dict(batman=12434,superman=132345,spiderman=344556)
print(phone_book)

phone_book1 = dict([('batman',12434),('superman',132345),('spiderman',344556)])
#adding value in dictionary
d1 = {"dell":5576,"hp" :232,"Macbook":10}
print(d1)
d1["Macbook"] = 12 #update 
print(d1)
d1["Samsung"] = 12444
print(d1)
#Removing element using del key word
del d1["dell"]
print(d1)
#Remove using pop method 
d1.pop("hp")
print(d1)

#check length of dictionary 
print(len(d1))

#copy content 
phone_book.update(d1)
print(phone_book)