import re
from collections import Counter
import math

def count_words_lines_spaces(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        lines = text.split('\n')
        total_words = len(words)
        total_lines = len(lines)
        total_spaces = text.count(' ')
    return total_words, total_lines, total_spaces

def count_unique_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        unique_words = set(words)
    return len(unique_words)

def word_frequency(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        frequency = Counter(words)
    return frequency

def longest_word(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        longest = max(words, key=len)
    return longest

def average_word_length(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        total_length = sum(len(word) for word in words)
        average_length = total_length / len(words) if len(words) > 0 else 0
    return average_length

def text_similarity(text1, text2):
    if text1 == text2:
        return 1
    else:
        return 0

def main():
    file_path = input("Enter the path to the text file: ")

    # i. Count the total number of words, lines and spaces
    total_words, total_lines, total_spaces = count_words_lines_spaces(file_path)
    print(f"Total words: {total_words}")
    print(f"Total lines: {total_lines}")
    print(f"Total spaces: {total_spaces}")

    # ii. Count the number of unique words
    unique_words_count = count_unique_words(file_path)
    print(f"Unique words: {unique_words_count}")

    # iii. Display the frequency of each word
    word_freq = word_frequency(file_path)
    print("Word frequency:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

    # iv. Find and display the longest word
    longest = longest_word(file_path)
    print(f"Longest word: {longest}")

    # v. Calculate and display the average length of words
    avg_length = average_word_length(file_path)
    print(f"Average word length: {avg_length:.2f}")

    # vi. Compare the similarity between two given texts
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")
    similarity = text_similarity(text1, text2)
    print(f"Similarity between the two texts: {similarity}")

if __name__ == "__main__":
    main()
