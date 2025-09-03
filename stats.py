import sys

def get_num_words():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    print(f"Found {num_words} total words")

def char_counts():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    string_integer = {}
    for char in file_contents.lower():
        if char == " ":
            continue
        if char in string_integer:
            string_integer[char] += 1
        else:
            string_integer[char] = 1
    return string_integer

def sort_char_counts(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_list.append ({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
