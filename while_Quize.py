start_num = 5 
#provide some start number, replace 5 with a number you choose
end_num = 100
#provide some end number that you stop when you hit, replace 100 with a number you choose
count_by = 2 
#provide some number to count by, replace 2 with a number you choose 
break_num = start_num
# write a while loop that uses break_num as the ongoing number to
while break_num < end_num:
    break_num += count_by

# check against end_num

print(break_num) #replace None with appropriate code


# count by check
print( )
print("//////////////////////////////////")
print( )

start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)