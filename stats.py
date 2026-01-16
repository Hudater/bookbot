def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def get_word_count(file_content):
    return len(file_content.split())


def get_char_count(file_content):
    split_chars = list(str.lower(file_content))
    char_count_dict = dict()
    for i in split_chars:
        if i in char_count_dict.keys():
            char_count_dict[i] = char_count_dict[i] + 1
        else:
            char_count_dict[i] = 1
    return char_count_dict
