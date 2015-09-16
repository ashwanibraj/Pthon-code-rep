def check_permute(str1, str2):
	if len(str1)==len(str2):
		d = {}
		for c in str1:
			if d.get(c) is None:
				d[c] = 1
			else:
				d[c] = d[c] + 1
		for c1 in str2:
			if d.get(c1) is None:
				return 'Not permutations'
			else:
				d[c1] = d[c1] - 1
		for c in str1:
			if d[c] <> 0:
				return 'Not permutation'
		return 'Matched permutations'
	return 'Not permutations'

print check_permute(raw_input('Enter a string: '), raw_input('Enter another string: '))

