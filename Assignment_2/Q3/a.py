my_list = []
while True:
    num = input("Enter number to add to the list (Stop to quit): ")

    if num.upper()=="STOP":
        break
    else:
        my_list.append(int(num))

total = 0
for i in range (len(my_list)):
    total += my_list[i]

print("The sum of list: ", my_list, "is: ", total)