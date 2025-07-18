def get_book_text(book_name):
	path = book_name
	with open(path) as f:
		file_contents = f.read()
	return file_contents

def count_words(book_name):
	text = get_book_text(book_name)
	words = text.split()
	word_count = len(words)
	return word_count

def count_char(book_name):
	text = get_book_text(book_name)
	text_low = text.lower()
	char = list(text_low)
	char_dict = {}
	for c in char:
		if c in char_dict:
			char_dict[c] +=1
		else:
			char_dict[c] =1
	return char_dict

def sort_on(char_dict):
	return(char_dict["value"])

def sort_function(char_dict):
	dict = char_dict
	list_dict = []
	for key in dict:
		if key.isalpha():
			list_dict.append({ 'key': key, 'value': dict[key] })
	list_dict.sort(reverse=True, key=sort_on)
	newlist =[]
	for key in list_dict:
		print(f"{key["key"]}: {key["value"]}")