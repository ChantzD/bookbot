#!/usr/bin/env python3

def count_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char_ in text:
        try:
            char_counts[char_.lower()] += 1
        except:
            char_counts[char_.lower()] = 1
    return char_counts

def sort_counts(char_counts):
    char_counts = {char: count for char, count in char_counts.items() if char.isalpha()}
    return dict(sorted(char_counts.items(), reverse=True, key=lambda item: item[1]))
