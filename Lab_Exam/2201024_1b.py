def text_similarity(text1, text2):
    if text1 == text2:
        return 1
    else:
        return 0



def main():
    no_of_lines = 0
    no_of_words = 0
    no_of_spaces = 0
    max_length = 0
    total_length = 0
    is_similar = 0
    max_word = ""
    dict1 = {}
    f1 = open("test.txt", 'r')
    
    while f1:
        data = f1.readline()
        if not data:
            break
        words = data.split()
        for i in words:
            length = len(i)
            total_length += length
            if  length > max_length:
                max_length = length
                max_word = i
            if dict1.get(i) is None:
                value = 0
            else:
                value = dict1.get(i)
            dict1[i] = value + 1
        print(words)
        
    f1.close()
    
    with open("test.txt" , "r") as file:
        text = file.read()
        words = text.split()
        lines = text.split('\n')
        no_of_words = len(words)
        no_of_lines = len(lines)
        no_of_spaces = text.count(' ')
    
    with open("test.txt", 'r') as f:
        line1 = f.readline()
        line2 = f.readline()
        is_similar = text_similarity(line1, line2)
        
    
    print("Number of lines:", no_of_lines)
    print("Number of words:", no_of_words)
    print("Number of spaces:", no_of_spaces)
    for i in dict1:
        print(i, "\t", dict1.get(i))
    print("Number of unique words: ", len(dict1))
    print("Maximum Length Word: ", max_word)
    print("maximum Length: ", max_length)
    print("Average Length: ",  total_length/no_of_words)
    print("First and Second Lines are same or not:", is_similar)

main()