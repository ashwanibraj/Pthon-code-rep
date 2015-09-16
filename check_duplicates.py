def check_duplicates():
	str = raw_input('Enter a string: ');

	bool = [False]*256
	x = 0
	for c in str:
		x = ord(c)
		if bool[x]:
			print 'Duplicate exists'
			return
		bool[x] = True
	print 'No duplicates'
	return

def check_unicode_duplicates():
	unistr = raw_input('Enter a string: ')

	inp = {}

	for i in unistr:
		if inp.get(i) is None:
			inp[i] = 1
		else:
			print 'Duplicate exists'
			return
	print 'No duplicates'
	return

check_unicode_duplicates()