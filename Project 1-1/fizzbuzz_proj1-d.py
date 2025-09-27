def fizzbuzz(x_range):
    fizzbuzz_array = []
    #go through all values from 1 through max value
    for x in range(1,x_range+1):
        print_value = ""
        if ((x % 3) ==0):
            print_value += "fizz"
        if ((x % 5) == 0):
            print_value += "buzz"
        if((x % 5) != 0) and ((x % 3) != 0):
            print_value = x
        fizzbuzz_array.append(print_value)
    return fizzbuzz_array

try:
    fizzbuzzcount = int(input("please enter the value you want to count up to:"))
except ValueError:
    print("Invalid input, please enter an integer value")
    exit()
myfizzbuzz = fizzbuzz(fizzbuzzcount)
for fizz in myfizzbuzz:
    print(fizz)