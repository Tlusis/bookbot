import sys
from stats import count_words, count_char, sort_function





def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(path)} total words")
    print("--------- Character Count -------")
    sort_function(count_char(path))
    print("============= END ===============")

main()