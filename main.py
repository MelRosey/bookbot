import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

with open(book_path) as f:
    file_contents = f.read()

from stats import get_num_words

get_num_words()

from stats import char_counts

char_counts()

from stats import char_counts, sort_char_counts

counts = char_counts()
sorted_counts = sort_char_counts(counts)

for item in sorted_counts:
	print(f"{item['char']}: {item['num']}")

