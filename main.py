import sys
import stats


def main():
    if len(sys.argv) == 2:
        book_text_str = stats.get_book_text(sys.argv[1])
        word_count = stats.get_word_count(book_text_str)
        char_count_dict = stats.get_char_count(book_text_str)
        sorted_list = stats.get_sorted_list_of_dicts(char_count_dict)
        stats.report_formatting(sorted_list, word_count)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == "__main__":
    main()
