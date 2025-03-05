from stats import count_words, get_char_counts, sort_counts
import sys

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}")
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    word_count = count_words(book)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    char_counts = get_char_counts(book)
    sorted_counts = sort_counts(char_counts)
    for char_ in sorted_counts:
        print(f"{char_}: {sorted_counts[char_]}")

    print("============= END ===============")


main()
