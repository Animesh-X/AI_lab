text = input("Enter the string: ")

vowel = "AEIOUaeiou"
count = 0

for i in range(len(text)):
    if text[i] in vowel:
        count = count + 1

print("NO of vowel in ", text, " is: ", count)