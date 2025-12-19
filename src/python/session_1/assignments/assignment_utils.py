def extract_core_part(s: str) -> str:
	"""
	Extracts the core part of string (i.e. all alphabetic characters and spaces).

	Parameters:
		s (str): the raw string from which the core part will be extracted

	Returns:
		core part of a string which is also a string
	"""
	return "".join(char for char in s if char.isalpha() or char == " ")

def replace_letters(s: str, mapping: dict) -> str:
	"""
	Replaces letters in a given string with their respective mappings from the mapping dict.

	Parameters:
		s (str): input string to be processed
		mapping (dict): a dictionary containing the letters to be replaced as its keys and the letter replacements as its values

	Returns:
		updated string with replaced letters as prescribed in the mapping dict
	"""
	str_lst = list(s)   
	replaced_lst = []
	for char in str_lst:
		if char not in mapping.keys():
			replaced_lst.append(char)
		else:
			replaced_lst.append(mapping[char])

	replaced_str = "".join(replaced_lst)

	return replaced_str

def reverse_str(s: str) -> str:
	"""
	Reverses a given string (e.g. "Hello" -> "olleH")
	
	Parameters:
		s (str): input string to be reversed

	Returns:
		reversed version of the inupt string
	"""
	return s[::-1]


def last_to_first(s: str) -> str:
	"""
	Moves the last char to the beginning of the string (e.g. "Hello" -> "oHell")
	
	Parameters:
		s (str): input string to be processed
	
	Returns:
		s with its last char moved to the front
	"""
	return s[-1] + s[:-1]