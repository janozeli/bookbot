import sys
from stats import get_num_words, get_num_letter, sort_letter_dict

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()
 
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    num_words = get_num_words(book_content)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    num_letter = get_num_letter(book_content)
    num_letter = sort_letter_dict(num_letter)
    print("--------- Character Count -------")
    for dict in num_letter:
        print(f"{dict["character"]}: {dict["count"]}") if dict["character"].isalpha() else None

main()