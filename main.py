from stats import *

def get_book_text(book_id):
    with open(book_id) as f:
        contents = f.read()
        return contents
    
def main():
    book = input("Please enter bookname in lowercase as a .txt file")
    # text = get_book_text(f"books/{book}")
    text = get_book_text("books/frankentstein.txt")
    num_words = word_count(text)
    sorted_dic = sort_dic(text)
    print("============ BOOKBOT =============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    

main()