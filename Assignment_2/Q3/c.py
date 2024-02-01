text = input("Enter the list of numbers: ")

my_list = list(map(lambda x: int(x), text.split()))

print("Original List: ", my_list)
my_list = list(set(my_list))
print("Removed Duplicates: ", my_list)