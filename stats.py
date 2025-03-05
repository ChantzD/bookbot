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
