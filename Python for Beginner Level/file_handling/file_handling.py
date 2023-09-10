# write in a file
"""
Files Mode 
'w' : write mode deletes all the previous data and add new one.
'a' : appends new data at the end of the file  
"""
file = open("welcome.txt","w")
file.write("Welcome Message From AEC\n")
file.close()

with open("welcome.txt","a") as file:
    file.write("Welcome Agagin from AEC \n")
    file.write("Which course you wanna enroll into?")

# read from file
with open("welcome.txt",'r') as file:
    data = file.read()
    print(data)