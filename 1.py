def sortByStrings(s, t):
	'''
	Assumptions: - Whitespaces will be treated the same as characters
	- If characters in s are not in t, they will be appended to the end of the output string

	Sort the letters in the string s by the order they occur in the string t. 
	You can assume t will not have repetitive characters. 
	For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw". 
	For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".
	'''
	# Create a dictionary to store letters in s
	s_dict = {}
	# Output string
	retval = ''
	# Initialize values
	for char in set(s).union(set(t)):
		s_dict[char] = 0
	# Keep track of character frequencies in s
	for char in s:
		s_dict[char] += 1
	# Start building the output string
	for char in t:
		retval += char * s_dict[char]
		s_dict[char] = 0
	# Append leftover characters in s not in t
	for char_key in s_dict:
		retval += char * s_dict[char] 

	return retval