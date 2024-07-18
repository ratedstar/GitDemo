# import math
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
#
# def paint_calc(height=test_h, width=test_w, cover=coverage):
#     canes = math.ceil((test_h * test_w) / coverage)
#     print(f"Total number of canes you need is {canes}")
#
#
# paint_calc(test_h, test_w)

# number is prime
num = int(input("Enter a number"))
def prime_num_checkr(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("Ita a prime number")
    else:
        print("Its not a prime number")
prime_num_checkr(num)