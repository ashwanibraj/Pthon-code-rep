class stack:
	def __init__(self):
		self.st = []
	def push(self, data):
		self.st.append(data)
	def pop1(self):
		return self.st.pop()
	def peek(self):
		if len(self.st) > 0:
			return self.st[-1]
		else:
			return None
	def isEmpty(self):
		if len(self.st) > 0:
			return False
		else:
			return True

x = raw_input("Enter elements for the stack:")

st1 = stack()

st2 = stack()
for i in x.split():
	st1.push(int(i))

while not(st1.isEmpty()):
	if st2.isEmpty():
		st2.push(st1.pop1())
	elif st1.peek() > st2.peek():
		temp = st1.pop1()
		while temp > st2.peek() and (st2.peek() is not None):
			st1.push(st2.pop1())
		st2.push(temp)
	else:
		st2.push(st1.pop1())

while not(st2.isEmpty()):
	st1.push(st2.pop1())

print "Sorted stack:"
while not(st1.isEmpty()):
	print str(st1.pop1())
	