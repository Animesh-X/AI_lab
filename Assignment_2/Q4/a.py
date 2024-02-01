f = open("testing.txt", 'r')
text_of_file = f.read()
print("Content of file:----\n",text_of_file, "\nNumber of Words: ",len(text_of_file.split()))
f.close()