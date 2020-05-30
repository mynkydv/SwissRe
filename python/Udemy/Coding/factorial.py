
import random

def calc_factorial(num):

    prodcut = 1

    if(num == 1):
        return 1

    for x in range(2, num - 1):
        prodcut *= x
    else:
        return prodcut


number = random.randint(1,10)
factorial = calc_factorial(num=number)
print(" The factorial of number {}! is {} ".format(number, factorial))