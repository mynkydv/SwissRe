
import datetime

def find_Palindrome(number):

    counter = 0
    reverse_number = 0
    while(number > 0):
        digit = number%10
        reverse_number = 10 * reverse_number + digit

        number = number//10
        counter += 1
    else:
        return reverse_number

print((datetime.datetime.now().time()))
for x in range(1, 10000):
    number = find_Palindrome(x)

    if(x == number):
        print("Ola!! We found a palindrome. {}".format(x))
print((datetime.datetime.now().time()))
    
