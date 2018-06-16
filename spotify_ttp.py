from 1 import sortByStrings
from 2 import decodeString
from 3 import changePossibilities

if __name__ == '__main__':
	while True:
		choice = input('Question 1, 2, 3? ')
		if '1' in choice:
			s = input('String s? ')
			t = input('String t? ')
			print(sortByStrings(s, t))
		elif '2' in choice:
			s = input('String s? ')
			print(decodeString(s))