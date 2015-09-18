class stack:
	def __init__(self):
		self.stac = []
	def push_st(self, data):
		self.stac.append(data)
	def pop_st(self):
		return self.stac.pop()

x = raw_input("Enter data for the stack separated by saces:")

temp = x.split()

st = stack()

for i in temp:
	st.push_st(i)

print "The top element popped:" + st.pop_st()

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class queue:
	def __init__(self, node):
		self.head = node
		self.tail = node
	def enqueue(self, node):
		self.tail.next = node
		self.tail = self.tail.next
	def dequeue(self):
		tem = self.head.data
		self.head = self.head.next
		return tem

x = raw_input("Enter data for queue:")
temp = x.split()

q = queue(Node(temp[0]))
for i in range(0, len(temp)-1):
	q.enqueue(Node(temp[i+1]))

print "The first element dequeued is:" + q.dequeue()