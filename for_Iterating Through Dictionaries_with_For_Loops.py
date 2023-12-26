cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
#find the the keys of the dictionary
print ("find the keys of the dictionary")
for key in cast:
    print(key)

print( )
print("////////////////////////////////")


cast2 = {}
# find the key and value in the dictionary
print ("find the key and value in the dictionary")
for key, value in cast.items():
    cast2[key] = value
 
print(cast2)
    