def  print_upper_words(words,  must_start_with={"h", "y"}):
	"""Prints words in a list in all upper case that begin with the given letters """
	for word in words:
		for char in must_start_with:
			if char == word[0].lower():
				print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])