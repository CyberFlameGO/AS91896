"""
Python Wordle thing
"""

import random
import json


def get_word_of_length(words, length):
    # (filter is just a wrapper for a generator by the looks of it)
    filter(lambda x: len(x)==length, words)  # https://stackoverflow.com/questions/26697601/how-to-return-all-list-elements-of-a-given-length

def main():
    """
    Main
    """
    raw_words = r'./wordlist.json'
    with open(raw_words) as word_list:
        wordlist = list(json.load(word_list).keys())
    word = random.choice(wordlist)

