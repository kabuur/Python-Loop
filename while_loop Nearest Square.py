limit = 40 #provide a limit, replace 40 with a number you choose
# write your while loop here
nearest_square = 1 # replace None with appropriate code
count = 1

while limit > nearest_square :
        if(count **2> limit):
                break
        nearest_square = count ** 2
        count += 1
   
print(nearest_square)


# limit = 40

# num = 0
# while (num+1)**2 < limit:
#     num += 1
# nearest_square = num**2

# print(nearest_square)