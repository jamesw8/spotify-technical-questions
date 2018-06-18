def decodeString(s):
	'''
	Assumptions: - Encoded string is enclosed with square brackets at the highest level (s always starts with k[])

	Given an encoded string, return its corresponding decoded string. 
	The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. 
	Note: k is guaranteed to be a positive integer. 
	For s = "4[ab]", the output should be decodeString(s) = "abababab" 
	For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"
	'''
	decoded_string = ''
	encoded_string = s
	# Save k constant
	k = int(encoded_string[0])
	# Skip brackets by starting at index 2 and ending at index len(encoded_string) - 2
	char_index = 2
	while char_index < len(encoded_string) - 1:
		# If number, check if next char is a bracket
		if encoded_string[char_index].isnumeric():
			# Check if it is a number constant for encoding rule by checking bracket 
			if char_index + 1 < len(encoded_string):
				if encoded_string[char_index + 1] == '[':
					# Find the end of the encoded substring
					encoded_substring_end = encoded_string[char_index:].find(']') + char_index
					# Recursive call for smaller encoded strings
					decoded_string += decodeString(s[char_index:encoded_substring_end + 1])
					# Continue index after substring
					char_index = encoded_substring_end
			# Append number to decoded_string like normal character
			else:
				decoded_string += encoded_string[char_index]
		# Not a number
		else:
			decoded_string += encoded_string[char_index]
		# Increment index
		char_index += 1
	# Return the decoded_string multiplied by k constant
	return decoded_string * k