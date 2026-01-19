from stats import *


def main():
    book_text_str = get_book_text("./books/frankenstein.txt")
    # print(book_text_str)
    word_count = get_word_count(book_text_str)
    # print(f"Found {word_count} total words")
    char_count_dict = get_char_count(book_text_str)
    # print(char_count_dict)
    # sorted_dict = get_sorted_dict(char_count_dict)
    # print(sorted_dict)
    get_sorted_dict(char_count_dict)
    # sort_on(char_count_dict)


if __name__ == "__main__":
    main()
