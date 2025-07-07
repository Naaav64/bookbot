from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"{get_num_words(text)} words found in the document" )


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()