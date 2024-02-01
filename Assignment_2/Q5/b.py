def fibonacci(num):
    prev = 0
    curr = 1
    if num == 1:
        return prev
    if num == 2:
        return curr

    for i in range (1,num):
        temp = prev + curr
        prev = curr
        curr = temp

    return  curr


num = int(input("Enter number: "))

print(num,"th term is: ",fibonacci(num))