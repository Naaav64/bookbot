from stats import get_num_words, get_character_num, get_report

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}\n----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words\n--------- Character Count -------")
    print(f"{get_report(text)}\n")
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()