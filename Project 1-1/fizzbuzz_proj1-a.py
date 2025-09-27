fizzbuzzcount = 20
for x in range(1,fizzbuzzcount+1):
    print_value = ""
    if ((x % 3) ==0):
        print_value += "fizz"
    if ((x % 5) == 0):
        print_value += "buzz"
    if((x % 5) != 0) and ((x % 3) != 0):
        print_value = x
    print(print_value)