def letter_combinations(digits):

	def backtrack(combination, next_digits):
		
		# when no more digits to parse, it means that a combination is formed. Store the combination & return.
		if not next_digits:
			combinations.append(combination)
			return
		
		# when there are still digits to parse, get the letters corresponding to the first digit
		# keep adding each character of the parent digit to the combination obtained so far.
		for character in dict_number_letters[next_digits[0]]:
			backtrack(combination+character, next_digits[1:])  # recursive solution	

	# collect combinations in a list.
	combinations = []

	# hard code the number-letter mapping
	dict_number_letters = {'2': 'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
	
	if digits: # handle empty input case.
		backtrack('',digits) # intially the current combination is empty

	# return the collected combinations
	return combinations

digits = ""
combinations = letter_combinations(digits)
print(combinations)
