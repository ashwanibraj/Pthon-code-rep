def string_compression(s):
	a = []
	cnt = 1
	a.append(s[0])
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			cnt = cnt+1
		else:
			a.append(str(cnt)+s[i])
			cnt = 1
	a.append(str(cnt))
	s1 = ''.join(a)

	if len(s) < len(s1):
		s1 = s
	print s1

string_compression('aabbbbbccaaa')