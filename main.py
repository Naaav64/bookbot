def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(path):
    num_words
    with open(path.split()) as n:
        num_words = len(n)
    return num_words



main()