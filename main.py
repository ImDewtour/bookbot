from stats import get_num_words, character_count, sorted_chars, bookbot
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path) 
    word_count = get_num_words(text)
    char_dict = character_count(text)
    sort_dict = sorted_chars(char_dict)
#    print(f"{word_count} words found in the document")
#    print(char_dict.sort)
    bookbot(book_path, word_count, sort_dict)


def get_book_text(book_path):
    with open(book_path) as fp:
        return fp.read()
        

main()