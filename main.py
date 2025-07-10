import sys
from stats import get_num_words, get_character_num, get_report

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}\n----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words\n--------- Character Count -------")
    print(f"{get_report(text)}\n")
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
if len(sys.argv) != 2:
    raise Exception("Proper Usage: python3 main.py /path/to/book/")
    sys.exit(1)

elif len(sys.argv) == 2:
    main()
