from stats import get_num_words, character_count, sorted_chars, bookbot

def main():
    book_path = "books/frankenstein.txt"
    text = (get_book_text(book_path))
    word_count = get_num_words(text)
    char_dict = character_count(text)
    sort_dict = sorted_chars(char_dict)
#    print(f"{word_count} words found in the document")
#    print(char_dict.sort)
    bookbot(book_path, word_count, sort_dict)


def get_book_text(path):
    with open(path) as fp:
        return fp.read()


main()