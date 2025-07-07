from stats import get_num_words, get_character_num

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    character_count = get_character_num(text)
    print(f"{get_num_words(text)} words found in the document")
    print(character_count)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()