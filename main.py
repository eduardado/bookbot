def main():
    book_name = "frankenstein.txt"
    frankenstein_path = "books/" + book_name
    text = get_book_content(frankenstein_path)
    number_of_words = count_words(text)
    letters_dictionary = create_letters_dictionary(text)
    clean_letters_dictionary = clean(letters_dictionary)
    list_of_dictionaries = convert_dictionary_into_list_of_dictionaries(clean_letters_dictionary)
    
    print_report(list_of_dictionaries, number_of_words, book_name)

def get_book_content(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def create_letters_dictionary(text):
    words = text.split()
    letters = {}
    for word in words:
        for letter in word:
            lower_case_letter = letter.lower()
            if lower_case_letter not in letters: 
                letters[lower_case_letter] = 1
            else:
                letters[lower_case_letter] = letters[lower_case_letter] + 1
    
    return letters

def convert_dictionary_into_list_of_dictionaries(dictionary):
    list_of_dictionaries = []
    for element in dictionary:
        list_of_dictionaries.append({"letter": element, "num": dictionary[element]})

    list_of_dictionaries.sort(reverse=True, key=sort_on)
    
    return list_of_dictionaries

def sort_on(dict):
    return dict["num"]

def clean(dictionary):
    clean_dictionary = {}
    for element in dictionary:
        if element.isalpha():
            clean_dictionary[element] = dictionary[element]
    return clean_dictionary

def print_report(list_of_dictionaries, number_of_words, book_name):
    print(f"--- Begin report of books/{book_name} ---")
    print(f"{number_of_words} words found in the document\n\n")
    for element in list_of_dictionaries:
        letter = element["letter"]
        number = element["num"]
        print(f"The '{letter}' character was found {number} times")


main()