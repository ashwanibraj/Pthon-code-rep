class stack:
	def __init__(self):
		self.st = []
	def push(self, data):
		self.st.append(data)
	def pop1(self):
		return self.st.pop()
	def __len__(self):
		return len(self.st)

class setofstack:
	def __init__(self):
		self.setstac = [stack()]		
	def setpush(self, data):
		setst = self.setpeek()
		if len(setst) == 5:
			st = stack()
			self.setstac.append(st)
			self.setpush(data)
		else:
			self.setstac[len(self.setstac) - 1].push(data)		
	def setpop(self):
		st = self.setpeek()
		if len(st) > 0:
			return self.setstac[len(self.setstac) - 1].pop1()
		else:
			self.setstac.pop()
			return self.setpop()		
	def setpeek(self):
		return self.setstac[len(self.setstac)-1]
	def popAt(self, index):
		if len(self.setstac[index - 1]) == 0:
			self.popAt(index + 1)
		else:
			return self.setstac[index - 1].pop1()

x = raw_input("Enter values for a stack of stacks:")

temp = x.split()

ss = setofstack()
for i in temp:
	ss.setpush(i)

print "The pop gives:" + ss.setpop()

print "The pop gives:" + ss.setpop()

print "The pop gives:" + ss.setpop()

print "The pop gives:" + ss.setpop()

print "The pop gives:" + ss.setpop()

ss.setpush("22")
ss.setpush("33")
ss.setpush("44")

print "The pop gives:" + ss.setpop()

x = raw_input("Enter the substack number you want to pop at:")

y = int(x)

print y

print "Result popped"+ss.popAt(y)		