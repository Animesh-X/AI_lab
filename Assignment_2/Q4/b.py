f1 = open("testing.txt", 'r')
f2 = open("write.txt", 'w')

f2.write(f1.read())
f1.close()
f2.close()

f=open("write.txt", 'r')
text_of_file = f.read()

print("Content of file:----\n",text_of_file)
f.close()