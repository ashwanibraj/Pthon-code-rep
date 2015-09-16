def replace_space(s, l):
	s = s.strip()
	s = s.split(' ')
	print '%20'.join(s)

replace_space('Mr John Smith    ', 13)