def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def get_word_count(file_content):
    word_count = len(file_content.split())
    print(f"Found {word_count} total words")


def main():
    book_text_str = get_book_text("./books/frankenstein.txt")
    # print(book_text_str)
    get_word_count(book_text_str)

main()