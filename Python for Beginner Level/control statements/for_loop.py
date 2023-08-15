# syntax
# loop over a collection
# for var_name in collection_name :

# loop over lists
streamers = ["Carryminati","Gareeb","RakaZone","Tanamy Bhat","RakaZone"]
for name in streamers: # name = streamers[0]
    print(name)

# loop over tuple
streamers = ("Carryminati","Gareeb","RakaZone","Tanamy Bhat","RakaZone")
for name in streamers: # name = streamers[2]
    print(name)

print("----------DICT LOOP-------------------")
# loop thourgh dictionary
streamer = {
    "name" : "CarrryMinati",
    "age" : 24,
    "gender": "male",
    "height" : 5.6,
    "dob": "12 MArch 1999",
    "name": "rakaZone"
}
# get keys in for loop
for name in streamer: # name = streamers[2]
    print(name)
# get values in a loop 
for values in streamer.values():
    print(values)
# get both key and values in for loop
for key, value in streamer.items():
    print(f'{key} ----> {value} ')
    
# reapeat a code n number of times
streamers[:]
for x in range(4,40): # range(0,4) = [0,1,2,3] including 0 and excluding 4 
    print(f"Loop Over {x}")