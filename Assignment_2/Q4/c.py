import re


f = open("testing.txt", 'r')
text_of_file = f.read()

pattern = input("Enter the pattern to search: ")
match = re.search(pattern,text_of_file)

if match:
    print(pattern, "is present" )
else:
    print(pattern, "is not present")