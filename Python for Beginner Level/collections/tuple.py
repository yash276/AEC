# collection is used when you want to store multiple values in a variable
# tuple() 
# indexing for tuple starts with 0 

# tuple is ordered
# tuple is unchangable (not allowed add , remove/delete, modify)
# tuple allows duplicate items.

streamers = ("Carryminati","Gareeb","RakaZone","Tanamy Bhat","RakaZone")
marks =(34,45,67,78)
mixed_tuple = ("NAme",45.75,True,45)

print(streamers)
print(marks)
print(mixed_tuple)
print(type(streamers))
print(type(marks))
print(type(mixed_tuple))

# indexing for single element
print(streamers[0])
# indexing for multipkle elements [ from : to ]
# include 0
# exclude 3
print(streamers[0:3])
print(streamers[1:4])
print(streamers[:3])
print(streamers[1:])

# reverse indexing
# single lement
print(streamers[-1])
print(streamers[-3])
# multiple elements
print(streamers[-2:])

# length of list
print(len(streamers))


list_streamers = list(streamers)
print(list_streamers)
list_streamers.pop(-1)
streamers = tuple(list_streamers)
print(streamers)