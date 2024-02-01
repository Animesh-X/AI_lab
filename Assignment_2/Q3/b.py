import sys


text = input("Enter the list of numbers: ")

my_list = list(map(lambda x: int(x), text.split()))
maxi = -sys.maxsize - 1

for i in range(len(my_list)):
    if maxi < my_list[i]:
        maxi = my_list[i]

print("Maximum value in: ", my_list, " is", maxi)