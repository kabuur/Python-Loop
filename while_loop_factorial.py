## number to find the factorial of
number = 6
## start with our product equal to one
product = 1
## track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    print(product, end="")
    product *= current
    print("*",current , "=", end="")
    print(product)
   
  
    # increment current with each iteration until it reaches number
    current += 1


## print the factorial of number
print(product)