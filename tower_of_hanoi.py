class stack:
	def __init__(self):
		self.st = []
	def push(self, data):
		self.st.append(data)
	def pop1(self):
		return self.st.pop()

s1 = stack()

x = raw_input("Enter elements for the tower of hanoi:")

temp = x.split()

for i in temp:
	s1.push(i)

n = len(temp)

s2 = stack()

s3 = stack()

def tower_of_hanoi(num_elem, source_stack, dest_stack, mid_stack):
	if num_elem == 0:
		return
	tower_of_hanoi(num_elem - 1, source_stack, mid_stack, dest_stack)
	dest_stack.push(source_stack.pop1())
	tower_of_hanoi(num_elem - 1, mid_stack, dest_stack, source_stack)

tower_of_hanoi(n, s1, s3, s2)

print s3.pop1()