from q1 import sortByStrings
from q2 import decodeString
from q3 import changePossibilities

def main():
	# Run driver code here
	while True:
		choice = input('Question 1, 2, 3? ')
		if '1' in choice:
			s = input('String s? ')
			t = input('String t? ')
			print(sortByStrings(s, t))
		elif '2' in choice:
			s = input('String s? ')
			print(decodeString(s))
		elif '3' in choice:
			amount = int(input('Amount? '))
			coins = list(map(int, input('Coins? (Space seperated) ').split(' ')))
			print(changePossibilities(amount, coins))
		else:
			return
			
if __name__ == '__main__':
	main()