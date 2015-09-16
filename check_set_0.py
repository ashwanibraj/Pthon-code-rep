def check_set_0(m):
	drow = dict()
	dcol = dict()
	for i in range(len(m)):
		for j in range(len(m[0])):
			if m[i][j] == 0:
				drow[i] = 1
				dcol[j] = 1
	for key in drow:
		for j in range(len(m[0])):
			m[key][j] = 0
	for key in dcol:
		for i in range(len(m)):
			m[i][key] = 0
	print m

m = [[1,1,0,1,0], [2,3,1,5,0], [1,4,1,2,9]]

check_set_0(m)