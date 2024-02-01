import math


def is_prime(num):
    if num > 1:
        for i in range (2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False

        return True


num1 = int(input("Enter number: "))

if is_prime(num1):
    print(num1, "is Prime")

else:
    print(num1, "is not Prime")