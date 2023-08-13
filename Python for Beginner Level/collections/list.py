# lsit is a collection of multiple values of same or different data tupes
# list index startes from 0.
student = ["Yash" ,"Shormi", "Ram" , "Kajol" , "Monica" , "Chintu"]
marks = [23, 45,67,234,67,24]
multi_list = [23, 45,True,"Yash",67,24.0]
print(type(student))
print(type(marks))
print(type(multi_list))
print(student)
print(marks)
print(multi_list)
#  indexing 
#  indexing  singel element
print(student[0])
print(student[5])
#  indexing for multiple elements 
# including 0 and excluding 3
print(student[0:3])

print(student[:3])

# reverse indexing
print(student[-1])
print(student[-3])
print(student[-6])

print(student[-3:])
print(student[:])

