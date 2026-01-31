import stats


def main():
    book_text_str = stats.get_book_text("./books/frankenstein.txt")
    word_count = stats.get_word_count(book_text_str)
    char_count_dict = stats.get_char_count(book_text_str)
    sorted_list = stats.get_sorted_list_of_dicts(char_count_dict)
    stats.report_formatting(sorted_list, word_count)


if __name__ == "__main__":
    main()
