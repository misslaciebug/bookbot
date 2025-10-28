def get_book_text(filepath):

	with open(filepath) as f:
		file_string = f.read()
		return file_string

from stats import word_count
from stats import character_count
def main():

	book_text = get_book_text("/home/misslaciebug/bookbot/books/frankenstein.txt")
	word_count_final = word_count(book_text)
	character_count_final = character_count(book_text)
	print(word_count_final)
	print(character_count_final)

main()
