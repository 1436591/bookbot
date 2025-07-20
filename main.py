from stats import *
import sys

def get_book_text(book_id):
    with open(book_id) as f:
        contents = f.read()
        return contents
    
def main():
    try:
        book = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book)
    num_words = word_count(text)
    sorted_dic = sort_dic(text)
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_dic:
        character = d["name"]
        count = d["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")
main()