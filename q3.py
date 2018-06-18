def changePossibilities(amount, coins):
	'''
	Assumptions: -

	Your quirky boss collects rare, old coins. They found out you're a programmer and asked you to solve something they've been wondering for a long time. 
	Write a function that, given an amount of money and an array of coin denominations, computes the number of ways to make the amount of money with coins of the available denominations. 
	Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), your program would output 4—the number of ways to make 4¢ with those denominations: 
	1¢, 1¢, 1¢, 1¢
	1¢, 1¢, 2¢
	1¢, 3¢
	2¢, 2¢
	'''
	# Store potential solutions, max # of coins needed to be added to each coin list, and modified lists of coins to allow for duplicates in generated permutations
	potential_solutions = []
	coin_counts = []
	coin_lists = []

	# Get # of coins that can satisfy amount for each coin
	for coin in coins:
		coin_counts.append(amount//coin)

	# Add # of coins calculated to each modified list of coins
	for coin_index in range(len(coins)):
		coin = coins[coin_index]
		curr_list = list(filter(lambda c: c != coin, coins))
		curr_list.extend([coin] * coin_counts[coin_index])
		coin_lists.append(curr_list[:])
		curr_list.clear()

	# Generate lists of permutations to check
	permutation_lists = []
	for permutation in coin_lists:
		permutation_lists.append(generatePermutations(permutation))

	# Check to see which permutations in each permutation list give a sum equal to amount wanted
	for permutation_list in permutation_lists:
		for permutation in permutation_list:
			perm_int = list(map(int, permutation))
			if sum(perm_int) == amount:
				potential_solutions.append(permutation)

	# Filter out zeros
	for s_index in range(len(potential_solutions)):
		potential_solutions[s_index] = list(filter(lambda n: n != 0, potential_solutions[s_index]))

	# Get rid of duplicate solutions by sorting potential solutions and checking membership in actual solutions list
	solutions = []
	for potential_solution in potential_solutions:
		if sorted(potential_solution) not in solutions:
			solutions.append(sorted(potential_solution))

	# Return # of unique solutions found
	return len(solutions)

def getBinNumbers(num):
	# Binary number generator from 0 to num
	for i in range(2**num):
		yield '0'*(num-len(bin(i)[2:])) + bin(i)[2:]


def generatePermutations(list_):
	# Use bitmasking to create list of permutations using binary number generator
	retval = []
	# For each binary number that we will use as a bitmask
	for i in getBinNumbers(len(list_)):
		perm = []
		# For each bit in bitmask, add the coin from coin_list that is in the bit's position
		for char_index in range(len(i)):
			perm.append(list_[char_index] if int(i[char_index]) else 0)
		retval.append(perm[:])
		perm.clear()
	return retval

if __name__ == '__main__':
	print(changePossibilities(4, [1, 2, 3]))