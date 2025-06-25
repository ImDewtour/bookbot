def get_num_words(text):
    wc = len(text.split())
    return wc

def character_count(text):
    chars = {}
    for c in text:
        char = c.lower()
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars