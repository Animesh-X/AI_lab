def check_palindrome(text):
    length = len(text)
    for i in range (int(length/2)):
        if (text[i] != text[length-1-i]):
            return False

    return True

text = input("Enter the string: ")

if(check_palindrome(text)):
    print(text, "is palindrome")
else :
    print(text, " is not palindrome")