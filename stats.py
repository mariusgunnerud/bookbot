def count_words(book_title):
    book_words = book_title.split()
    return len(book_words)

def character_count(document):
    char_dict = {}
    for i in document.lower():
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict
