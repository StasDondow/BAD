from collections import defaultdict


def find_first_unique_char_of_unique_first_chars(text):
	""" The function finds the first unique character in each word of the input text, 
	and returns the first unique character from the set of such characters.
	"""

	# Add a space at the end for correct processing of the last word
	text += " "

	unique_first_symbols = defaultdict(lambda: 0)  # the first unique characters of all words of the text (if any)
	word_symbols = defaultdict(lambda: 0)  # the number of characters in a word

	# Go through the symbols of the text
	for ch in text:
		if ord("a") <= ord(ch.lower()) <= ord("z"):
			word_symbols[ch] += 1
		elif ch == "'":
			continue  # the apostrophe is also part of the word, but we don't count it
		else:
			# if it's another character, it's the end of the word or the word hasn't started yet
			if len(word_symbols) > 0:
				# Find the first unique symbol of the word
				for k in word_symbols.keys():
					if word_symbols[k] == 1:
						unique_first_symbols[k] += 1
						break
				# Clear the dictionary for the next word
				word_symbols.clear() 

	# Find the first unique character from the set of characters
	for k in unique_first_symbols.keys():
		if unique_first_symbols[k] == 1:
			return k
	return None


def read_input_text():
	""" The function allows the user to enter text in the console or read it from a file.
	"""
	c = ""
	while not c in ["1", "2"]:
		c = input(
"""How would you like to enter the text?
1 - in the colsole
2 - read from a file

cmd: """)
		if c == "1":
			text = input("Enter your text:\n")
			return text
		elif c == "2":
			fpath = input("Enter full path to the file: ")
			try:
				with open(fpath, "r") as f:
					text = f.read()
				return text
			except FileNotFoundError:
				print("No such file!\n")
		else:
			print("Wrong input! Try again!")


if __name__ == "__main__":
	text = read_input_text()
	print("\nSymbol:", find_first_unique_char_of_unique_first_chars(text))
