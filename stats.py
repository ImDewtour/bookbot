def get_num_words(text):
    word_count = len(text.split())
    return word_count

def character_count(text):
    chars = {}
    for c in text:
        char = c.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sorted_chars(char_dict):
    sorted_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {}
    for char, count in sorted_list:
        if char.isalpha():
            sorted_dict[char] = count
    return sorted_dict



def bookbot(book_path, word_count, sort_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sort_dict:
        print(f"{char[0]}: {sort_dict[char]}")
    print("============= END ===============")
