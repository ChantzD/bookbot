from stats import count_words, get_char_counts
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book = get_book_text("./books/frankenstein.txt")

    word_count = count_words(book)
    print(f"{word_count} words found in the document")

    char_counts = get_char_counts(book)
    print(char_counts)

main()
