def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    print(f"The number of words in Frankenstein is {word_count}")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text_as_string = str(text)
    letter_dictionary = get_letter_count(text_as_string, letters)
    letter_list = list(letter_dictionary.items())
    letter_list.sort(key=lambda a: a[1], reverse=True)
    for entry in letter_list:
        print(f"The '{entry[0]}' character was found {entry[1]} times")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text, letters):
    letter_dictionary = {}
    text_to_count = text.lower()
    letters = letters
    for letter in letters:
        count = 0
        for character in text_to_count:
            if letter == character:
                count += 1
        letter_dictionary[letter] = count
    return letter_dictionary 

main()

