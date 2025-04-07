import stats
import sys

def print_report():
    # Check if we have the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with error code 1

    # Get the book text
    path = sys.argv[1]
    text = stats.get_book_text(path)

    # Print header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    # Print word count
    print("----------- Word Count ----------")
    word_count = len(text.split())
    print(f"Found {word_count} total words")

    # Print character count
    print("--------- Character Count -------")
    char_counts = stats.count_chars(path) # Get the character count dictionary
    sorted_chars = stats.sort_char_dict(char_counts) # Sort

    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetical orders
        if char.isalpha():
            print(f"{char}: {count}")

    # Print footer
    print("============= END ===============")

print_report()
