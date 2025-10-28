def word_count(book_text1):
        book_words = book_text1.split()
        return len(book_words)

def character_count(book_text2):
	characters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0,'s':0,'t':0,'u':0,'v':0, 'w':0,'x':0,'y':0,'z':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'!':0,'@':0,'#':0,'$':0,'%':0,'^':0,'&':0,'*':0,'(':0,')':0,'.':0, '/':0,'?':0, ' ':0, '"':0}
	lower_book_text = book_text2.lower()
	for character in lower_book_text:
		if character in characters:
			characters[character] += 1
	return characters
