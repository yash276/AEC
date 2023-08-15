# collection is used when you want to store multiple values in a variable
# list() 
# indexing for list starts with 0 
# list is ordered
# list is changable ( add , remove/delete, modify)
# list allows duplicate items.

student = ["Carryminati","Gareeb","RakaZone","Tanamy Bhat"]
marks =[34,45,67,78]
mixed_list = ["NAme",45.75,True,45]

print(student)
print(type(student))

# indexing for single element
print(student[0])
# indexing for multipkle elements [ from : to ]
# include 0
# exclude 3
print(student[0:3])
print(student[1:4])
print(student[:3])
print(student[1:])

# reverse indexing
# single lement
print(student[-1])
print(student[-3])
# multiple elements
print(student[-2:])

# add element at the end of the list
student.append("Scout")
student.append("RakaZone")
print(student)
# add element to an index
student.insert(2,"Mortal")
print(student)

# remove an element
student.remove("Tanamy Bhat")
print(student) 
# remove an element from index
student.pop(3)
print(student)
# length of list
print(len(student))

# modify single element
student[2] = "Tanmay Baht"
print(student)
# modify multiple elements in a list
student[-2:] = ["Mortal","Daddy"]
print(student)