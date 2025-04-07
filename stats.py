def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(path):
    text = get_book_text(path)
    num_words = len(text.split())
    print(f"{num_words} words found in the document")

def count_chars(path):
    text = get_book_text(path)
    char_counts = {}

    for char in text:
        char = char.lower()

        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_dict(char_dict):
    # Create a list to hold our dictionaries
    sorted_chars = []

    # Convert the char dict into a list of dictionaries
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        sorted_chars.append(char_info)

    # Define a helper function for sorting
    def sort_on(dict):
        return dict["count"]

    # Sort the list of dictionaries by count (highest to lowest)
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars
