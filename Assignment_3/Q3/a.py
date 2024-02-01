import numpy as np
 

filename = "data1.txt"


# https://www.geeksforgeeks.org/import-text-files-into-numpy-arrays/
sets_of_numbers = np.genfromtxt(filename, dtype = float, delimiter = ",")
print(sets_of_numbers)

new_set = np.copy(sets_of_numbers)
print(new_set)

# https://sparkbyexamples.com/python/python-numpy-standard-deviation-function/#:~:text=2nd%20column%20values%20are%203,arr%2Caxis%3D1)%20.
mean = np.mean(sets_of_numbers, axis=1)
std = np.std(sets_of_numbers, axis=1)

print(mean)
print(std)


# https://www.geeksforgeeks.org/numpy-column_stack-in-python/
# column stack joins two arary column wise
new_set = np.column_stack((new_set, mean))
new_set = np.column_stack((new_set, std))
print("\n\n")
print(new_set)


with open("results.txt", 'w') as f:
    for set in new_set:
        f.write(str(set)+"\n")