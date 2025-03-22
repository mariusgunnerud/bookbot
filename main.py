#!/usr/bin/env python3
import sys
from stats import count_words,character_count
from collections import OrderedDict

def get_book_text(title):
    with open(title) as book:
        file_contents = book.read()
    return file_contents

def report(data):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1],reverse=True))
    for i in sorted_dict:
        if i.isalpha():
            print(f"{i}: {sorted_dict[i]}")
    print(f"============ END ============")

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
path = sys.argv[1]

frankenstein = get_book_text(path)
num_words = count_words(frankenstein)
report(character_count(frankenstein))
