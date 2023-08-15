# collection is used when you want to store multiple values in a variable
# dict() 

# dict is ordered
# dict is changable ( add , remove/delete, modify)
# dict not allowed duplicate items.
# key(str): value ( can be any datatype) pair

streamer = {
    "name" : "CarrryMinati",
    "age" : 24,
    "gender": "male",
    "height" : 5.6,
    "dob": "12 MArch 1999",
    "name": "rakaZone"
}

print(streamer)
print(type(streamer))
# access single element
print(streamer["age"])
print(streamer["gender"])
# add a new key-value pair
streamer["youtube_channel"] = "carrylive"
print(streamer)
# modify
streamer["age"] = 25
print(streamer)
# delete
streamer.pop("height")
print(streamer)


print(streamer.keys())