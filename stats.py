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


### fns to format the report with sorting
## helper fn to sort dict on
def sort_on(char_count_dict):
    return char_count_dict["num"]


def report_formatting(dicts_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count} total words")
    print("--------- Character Count -------")
    for i in dicts_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


# convert to list of dicts and sort
def get_sorted_dict(char_count_dict):
    dicts_list = []
    for i in char_count_dict:
        if i.isalpha():
            dicts_list.append({"char": i, "num": char_count_dict[i]})
    dicts_list.sort(reverse=True, key=sort_on)
    report_formatting(dicts_list)
    # print(dicts_list)
    return dicts_list
